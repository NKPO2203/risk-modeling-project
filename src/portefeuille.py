"""Moteur en montants. Les décisions sont datées dans research/portefeuilles.md."""
import numpy as np
import pandas as pd

COUT = 0.0010


def preparer_prix(prix, indice=False):
    """Sépare observation et valorisation au dernier cours connu.

    Les cours Yahoo sont déjà retraités des divisions : Stock Splits ne
    multiplie jamais une seconde fois les montants. Une valeur portée pendant
    un trou n'est pas une observation de marché sans réserve pour le risque.
    """
    if not prix.index.is_unique or not prix.index.is_monotonic_increasing:
        raise ValueError("Dates dupliquées ou non ordonnées.")
    close, div = prix.Close.astype(float), prix.Dividends.astype(float)
    if np.isinf(close).any() or close.dropna().le(0).any():
        raise ValueError("Prix non fini, nul ou négatif.")
    if np.isinf(div).any() or div.dropna().lt(0).any():
        raise ValueError("Dividende négatif ou non fini.")
    suspect = pd.Series(False, index=prix.index)
    if not indice:
        volume = prix.Volume.astype(float)
        if volume.isna().any() or volume.lt(0).any() or np.isinf(volume).any():
            raise ValueError("Volume absent, négatif ou non fini.")
        avant = ~volume.gt(0).cummax()
        if {"Open", "High", "Low"} <= set(prix.columns):
            plat = prix[["Open", "High", "Low"]].eq(close, axis=0).all(axis=1)
            suspect = volume.eq(0) & (avant | (plat & close.eq(close.shift())))
        else:
            suspect = volume.eq(0)
    observe = close.mask(suspect)
    valeur = observe.ffill()
    if (div.isna() & valeur.notna()).any():
        raise ValueError("Dividende absent pendant l'historique valorisé.")
    return pd.DataFrame({
        "rendement_observe": observe.pct_change(fill_method=None),
        "rendement_valorisation": valeur.pct_change(fill_method=None),
        "dividende": div / valeur.shift(), "disponible": observe.notna(),
        "cours_porte": observe.isna() & valeur.notna(),
        "volume_nul": False if indice else prix.Volume.eq(0)}, index=prix.index)


def rendements_et_dividendes(prix, indice=False):
    """Rendement observé et détachement en espèces rapporté au cours précédent."""
    p = preparer_prix(prix, indice)
    return p.rendement_observe, p.dividende


def poids_cibles(membres, presents):
    """Équipondère les entreprises puis partage entre classes disponibles."""
    if membres.titre.duplicated().any():
        raise ValueError("Titre dupliqué dans l'appartenance.")
    cle = "cik" if "cik" in membres else "entreprise"
    if membres[cle].isna().any():
        raise ValueError("Identité d'entreprise absente.")
    vivants = membres[membres.titre.isin(presents)]
    if vivants.empty:
        return {}
    n = vivants[cle].nunique()
    classes = vivants.groupby(cle).titre.transform("size")
    return {r.titre: 1.0 / (n * k) for r, k in zip(vivants.itertuples(), classes)}


def _executer(montant, vise, cash_vise, cout):
    """Finance les frais sur les achats et ventes réellement exécutés.

    La cible complète, trésorerie comprise, est réduite proportionnellement.
    Le solveur impose frais = coût * somme(abs(cible après frais - positions avant)).
    """
    valeur = float(vise.sum() + cash_vise.sum())
    if valeur <= 0:
        return vise.copy(), cash_vise.copy(), 0.0, 0.0
    if np.array_equal(montant, vise):
        return vise.copy(), cash_vise.copy(), 0.0, 0.0
    bas, haut = 0.0, valeur
    for _ in range(55):
        frais = (bas + haut) / 2
        facture = cout * np.abs(vise * (1 - frais / valeur) - montant).sum()
        if frais < facture:
            bas = frais
        else:
            haut = frais
    frais = (bas + haut) / 2 if cout else 0.0
    nouveau = vise * (1 - frais / valeur)
    cash = cash_vise * (1 - frais / valeur)
    return nouveau, cash, float(frais), float(np.abs(nouveau - montant).sum())


def simuler(rendements, detachements, titres, cibles, dates, jours_reeq,
            reequilibrer, cout=COUT, fins_de_mois=frozenset(), *,
            disponibilite=None, entreprises=None, journal=None):
    """Renvoie valeurs, rotation annualisée et photographies des poids.

    Une cible hors janvier est un événement d'entrée, jamais un rééquilibrage
    général. L'achat est à la clôture ; le nouveau titre ne rapporte que dès
    la séance suivante. La mise initiale est une base nette de sa constitution.
    Aucun apport n'est autorisé ensuite, même après une perte totale.
    """
    dates = pd.Index(dates)
    if (not len(dates) or not dates.is_unique or not dates.is_monotonic_increasing
            or len(set(titres)) != len(titres) or not titres):
        raise ValueError("Dates ou liste de titres invalides.")
    if not np.isfinite(cout) or not 0 <= cout < 1:
        raise ValueError("Coût invalide.")
    for df in (rendements, detachements):
        if not df.index.equals(dates) or not df.columns.is_unique:
            raise ValueError("Dates désalignées ou colonnes dupliquées.")
    if not cibles.index.is_unique or not set(cibles.index) <= set(dates):
        raise ValueError("Dates de cibles invalides.")
    if not set(titres) <= set(cibles.columns):
        raise ValueError("Cibles incomplètes.")
    if dates[0] not in cibles.index or not set(jours_reeq) <= set(cibles.index):
        raise ValueError("Cible initiale ou annuelle absente.")
    r = rendements[titres].to_numpy(dtype=float)
    d = detachements[titres].to_numpy(dtype=float)
    if np.isinf(r).any() or np.isinf(d).any() or (r < -1).any() or (d < 0).any():
        raise ValueError("Rendement ou détachement invalide.")
    if disponibilite is None:
        cote = ~np.isnan(r)
    else:
        if not disponibilite.index.equals(dates) or disponibilite[titres].isna().any().any():
            raise ValueError("Disponibilités désalignées ou inconnues.")
        if not all(pd.api.types.is_bool_dtype(disponibilite[t].dtype) for t in titres):
            raise ValueError("Une disponibilité doit être un booléen, pas un texte ou un nombre.")
        cote = disponibilite[titres].to_numpy(dtype=bool)
    wc = cibles.loc[:, titres].to_numpy(dtype=float)
    if not np.isfinite(wc).all() or (wc < 0).any() or not np.allclose(wc.sum(axis=1), 1, rtol=0, atol=1e-12):
        raise ValueError("Poids cibles non finis, négatifs ou de somme différente de un.")
    groupes = np.array([entreprises[t] if entreprises is not None else t for t in titres])
    montant, tresorerie = np.zeros(len(titres)), np.zeros(len(titres))
    deja_entre = np.zeros(len(titres), dtype=bool)
    valeurs, rotations, photos = [], [], []
    for i, jour in enumerate(dates):
        precedent = float(montant.sum() + tresorerie.sum())
        poids_avant = montant / precedent if precedent else montant.copy()
        if i > 0:
            detenus = montant > 0
            if (detenus & (~np.isfinite(r[i]) | ~np.isfinite(d[i]))).any():
                raise ValueError(f"Rendement ou dividende inconnu sur une position détenue : {jour}")
            tresorerie += montant * np.nan_to_num(d[i], nan=0)
            montant *= 1 + np.nan_to_num(r[i], nan=0)
        avant_operation = float(montant.sum() + tresorerie.sum())
        frais = echange = 0.0
        if jour in cibles.index:
            w = cibles.loc[jour, titres].to_numpy(dtype=float)
            if ((w > 0) & ~cote[i]).any():
                raise ValueError(f"Cible sur un titre sans cotation : {jour}")
            if i == 0:
                montant = w.copy()
                deja_entre = w > 0
            elif avant_operation > 0:
                annuel = jour in jours_reeq
                nouveaux = (w > 0) & ~deja_entre
                vise, cash_vise = montant.copy(), tresorerie.copy()
                if annuel and reequilibrer:
                    vise, cash_vise = avant_operation * w, np.zeros(len(titres))
                else:
                    if annuel:
                        vise += cash_vise
                        cash_vise[:] = 0
                    if nouveaux.any():
                        anciens = set(groupes[(montant + tresorerie) > 0])
                        nouveaux_groupes = set(groupes[nouveaux]) - anciens
                        n, k = len(anciens), len(nouveaux_groupes)
                        vise *= n / (n + k)
                        cash_vise *= n / (n + k)
                        for groupe in sorted(set(groupes[nouveaux])):
                            selection = (groupes == groupe) & (deja_entre | nouveaux)
                            if groupe in nouveaux_groupes:
                                vise[selection] = avant_operation / (n + k) / selection.sum()
                            else:
                                # Une deuxième classe ne crée pas une entreprise.
                                vise[selection] = vise[selection].sum() / selection.sum()
                montant, tresorerie, frais, echange = _executer(montant, vise, cash_vise, cout)
                rotations.append(echange / avant_operation)
                deja_entre |= nouveaux
        valeur = float(montant.sum() + tresorerie.sum())
        if not np.isfinite(valeur) or (montant < -1e-13).any() or (tresorerie < -1e-13).any():
            raise ValueError(f"État de portefeuille invalide : {jour}")
        if i and abs(valeur + frais - avant_operation) > 1e-10 * max(1, avant_operation):
            raise ArithmeticError(f"L'opération crée ou détruit de la valeur : {jour}")
        if journal is not None:
            attendu = float(np.dot(poids_avant, np.nan_to_num(r[i] + d[i], nan=0))) if i else 0.0
            journal.append({"date": jour, "valeur_avant": precedent,
                            "valeur_avant_operation": avant_operation, "valeur": valeur,
                            "frais": frais, "echange": echange,
                            "rendement_attendu_avant_frais": attendu,
                            "tresorerie": float(tresorerie.sum())})
        valeurs.append(valeur)
        if jour in fins_de_mois and valeur > 0:
            photo = pd.Series(montant / valeur, index=titres, name=jour)
            photo["_tresorerie"] = tresorerie.sum() / valeur
            photos.append(photo)
    annees = max((len(dates) - 1) / 252, 1 / 252)
    return pd.Series(valeurs, index=dates), float(sum(rotations) / annees), pd.DataFrame(photos)
