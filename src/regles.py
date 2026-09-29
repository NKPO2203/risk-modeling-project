"""Règles de construction de la seconde version des étapes 4 et 5.

Les décisions appliquées ici sont fixées dans la section IX de
research/plan_projet.md, écrite avant tout calcul. Une règle combine une
sélection annuelle, une pondération et une protection ; elle n'utilise à
chaque date que l'information disponible la veille.
"""
from math import comb, e, log, sqrt
from statistics import NormalDist

import numpy as np
import pandas as pd

SEANCES = 252
COUT = 0.0010
EULER = 0.5772156649015329
_N = NormalDist()


# --------------------------------------------------------------------------
# Covariance et pondérations
# --------------------------------------------------------------------------

def ledoit_wolf(X):
    """Covariance rétrécie vers une identité mise à l'échelle (Ledoit et Wolf, 2004).

    `X` est un tableau T x N sans valeur absente. Renvoie la matrice et
    l'intensité de rétrécissement, comprise entre 0 et 1.
    """
    X = np.asarray(X, dtype=float)
    T, N = X.shape
    if T < 2 or np.isnan(X).any():
        raise ValueError("Au moins deux observations complètes sont nécessaires.")
    Xc = X - X.mean(axis=0)
    S = Xc.T @ Xc / T
    m = np.trace(S) / N
    d2 = ((S - m * np.eye(N)) ** 2).sum()
    if d2 == 0:
        return S, 0.0
    # Somme des ||x x' - S||² sur les dates, sans former les T matrices : sum ||x||⁴ - T ||S||².
    b2 = ((Xc ** 2).sum(axis=1) ** 2).sum() / T ** 2 - (S ** 2).sum() / T
    intensite = min(b2, d2) / d2
    return intensite * m * np.eye(N) + (1 - intensite) * S, float(intensite)


def contributions_egales(cov, budgets=None, iterations=10000, tolerance=1e-12):
    """Poids positifs dont les contributions au risque sont proportionnelles aux budgets.

    Descente par coordonnées cycliques sur le problème de Maillard, Roncalli
    et Teïletche (2010) : minimiser x'Σx/2 moins la somme des budgets fois
    log x, puis normaliser.
    """
    cov = np.asarray(cov, dtype=float)
    n = len(cov)
    b = np.full(n, 1 / n) if budgets is None else np.asarray(budgets, dtype=float) / np.sum(budgets)
    x = 1 / np.sqrt(np.diag(cov))
    for _ in range(iterations):
        ancien = x.copy()
        for i in range(n):
            autres = cov[i] @ x - cov[i, i] * x[i]
            x[i] = (-autres + np.sqrt(autres ** 2 + 4 * cov[i, i] * b[i])) / (2 * cov[i, i])
        if np.abs(x - ancien).max() < tolerance * np.abs(x).max():
            break
    return x / x.sum()


def _projection_simplexe_plafonne(v, plafond):
    """Projection euclidienne sur {0 <= w <= plafond, somme = 1}, par dichotomie."""
    bas, haut = v.min() - plafond, v.max()
    for _ in range(100):
        tau = (bas + haut) / 2
        if np.clip(v - tau, 0, plafond).sum() > 1:
            bas = tau
        else:
            haut = tau
    return np.clip(v - (bas + haut) / 2, 0, plafond)


def variance_minimale(cov, plafond, iterations=5000):
    """Variance minimale sans vente à découvert, poids plafonnés, par gradient projeté."""
    cov = np.asarray(cov, dtype=float)
    n = len(cov)
    if plafond * n < 1 - 1e-12:
        raise ValueError("Le plafond ne permet pas d'investir la totalité.")
    w = np.full(n, 1 / n)
    pas = 1 / np.linalg.eigvalsh(cov).max()
    for _ in range(iterations):
        nouveau = _projection_simplexe_plafonne(w - pas * cov @ w, plafond)
        if np.abs(nouveau - w).max() < 1e-12:
            return nouveau
        w = nouveau
    return w


def ponderer(methode, passe, titres, groupe_de, entreprise_de):
    """Poids cibles d'une sélection de titres.

    `passe` est le tableau des rendements des séances précédant la date, déjà
    limité à la fenêtre voulue. W1 équipondère les entreprises et partage leur
    poids entre leurs classes ; les autres méthodes traitent chaque titre.
    """
    titres = list(titres)
    if methode == "W1":
        entreprises = pd.Series({t: entreprise_de[t] for t in titres})
        n = entreprises.nunique()
        classes = entreprises.map(entreprises.value_counts())
        return 1 / (n * classes)
    bloc = passe[titres].fillna(0.0).to_numpy()
    cov, _ = ledoit_wolf(bloc)
    if methode == "W2":
        w = 1 / np.sqrt(np.diag(cov))
    elif methode == "W4":
        w = contributions_egales(cov)
    elif methode == "W5":
        w = variance_minimale(cov, max(0.05, 1.5 / len(titres)))
    elif methode == "W3":
        groupes = pd.Series({t: groupe_de[t] for t in titres})
        noms = sorted(groupes.unique())
        A = np.array([(groupes == g).to_numpy() / (groupes == g).sum() for g in noms])  # groupes x titres
        cov_groupes = A @ cov @ A.T
        wg = contributions_egales(cov_groupes)
        w = A.T @ wg
    else:
        raise ValueError(f"Pondération inconnue : {methode}")
    return pd.Series(w / w.sum(), index=titres)


# --------------------------------------------------------------------------
# Simulation
# --------------------------------------------------------------------------

def simuler(rendements, cibles, cout=COUT):
    """Poches ramenées à leurs cibles aux dates données, dérive entre elles.

    Mêmes conventions que `couverture.melange_multiple`, mais les titres
    absents d'une cible valent zéro et le calcul se fait par blocs entre deux
    rééquilibrages. Renvoie la valeur, partant de 100, et les frais.
    """
    R = np.nan_to_num(rendements.to_numpy(dtype=float))
    colonnes = rendements.columns
    dates = [str(d) for d in rendements.index]
    if dates[0] not in cibles:
        raise ValueError("La première date doit porter des poids cibles.")
    debuts = [i for i, d in enumerate(dates) if d in cibles]
    valeurs, frais = np.empty(len(dates)), 0.0
    V, poches = 100.0, None
    for k, i0 in enumerate(debuts):
        # Les positions fixées à la clôture de i0 gagnent les rendements de i0 + 1
        # jusqu'au prochain rééquilibrage inclus, où elles sont remises aux cibles.
        i1 = debuts[k + 1] if k + 1 < len(debuts) else len(dates) - 1
        w = cibles[dates[i0]].reindex(colonnes).fillna(0.0).to_numpy(dtype=float)
        if w.min() < 0 or not np.isclose(w.sum(), 1):
            raise ValueError(f"Poids invalides au {dates[i0]}.")
        if poches is not None:
            paye = cout * np.abs(w * V - poches).sum()
            frais += paye
            V -= paye
        valeurs[i0] = V
        poches = V * w
        if i1 > i0:
            croissance = np.cumprod(1 + R[i0 + 1:i1 + 1], axis=0)
            chemin = V * croissance @ w
            valeurs[i0 + 1:i1 + 1] = chemin
            poches = V * w * croissance[-1]
            V = chemin[-1]
    return pd.Series(valeurs, index=rendements.index), frais


def exposition_pilotee(r, cible, fenetre, fins):
    """Exposition fixée en fin de mois : min(1, cible / volatilité réalisée sur `fenetre`).

    Tant que la règle n'a pas `fenetre` rendements, l'exposition vaut un.
    """
    vol = r.rolling(fenetre, min_periods=fenetre).std() * sqrt(SEANCES)
    brute = np.minimum(1.0, cible / vol).where(vol.notna(), 1.0)
    fixee = brute.where([str(d) in fins for d in r.index]).ffill().fillna(1.0)
    return fixee.shift(1).fillna(1.0)


def pilotage_volatilite(r, r_reste, cible, fenetre, fins, cout=COUT):
    """Valeur d'une règle dont l'exposition suit `exposition_pilotee`, le reste en `r_reste`."""
    s = exposition_pilotee(r, cible, fenetre, fins).to_numpy()
    rr = np.nan_to_num(r.to_numpy())
    rreste = np.nan_to_num(r_reste.reindex(r.index).to_numpy())
    changement = np.abs(np.diff(s, prepend=s[0]))
    facteur = (1 + s * rr + (1 - s) * rreste) * (1 - cout * changement)
    facteur[0] = 1.0
    return pd.Series(100 * np.cumprod(facteur), index=r.index)


def protection_indice(r, jambe, beta, part, fins):
    """Ajoute `part` fois le bêta fixé en fin de mois fois le rendement d'une jambe d'options."""
    b = beta.where([str(d) in fins for d in r.index]).ffill().shift(1).fillna(1.0)
    total = np.nan_to_num(r.to_numpy()) + part * b.to_numpy() * np.nan_to_num(jambe.reindex(r.index).to_numpy())
    total[0] = 0.0
    return pd.Series(100 * np.cumprod(1 + total), index=r.index)


# --------------------------------------------------------------------------
# Notes fondamentales
# --------------------------------------------------------------------------

FLUX = {"benefice": ["NetIncomeLoss"],
        "flux_exploitation": ["NetCashProvidedByUsedInOperatingActivities",
                              "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations"],
        "marge_brute": ["GrossProfit"],
        "chiffre_affaires": ["Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax", "SalesRevenueNet"],
        "cout_ventes": ["CostOfRevenue", "CostOfGoodsAndServicesSold", "CostOfGoodsSold"]}
STOCKS = {"actif": ["Assets"],
          "capitaux_propres": ["StockholdersEquity",
                               "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"]}


def _premiere_publication(faits, etiquettes, fin, duree):
    """Première valeur publiée pour la fin d'exercice donnée, dans l'ordre de préférence des étiquettes."""
    for etiquette in etiquettes:
        f = faits[(faits.etiquette == etiquette) & (faits.fin == fin)]
        if duree:
            jours = (pd.to_datetime(f.fin) - pd.to_datetime(f.debut)).dt.days
            f = f[(jours >= 330) & (jours <= 400)]
        if len(f):
            return float(f.sort_values("depose_le").valeur.iloc[0])
    return np.nan


def fondamentaux_a_date(faits, date):
    """Chiffres du dernier rapport annuel déposé avant `date`, entreprise par entreprise.

    `faits` vient de data/raw/fondamentaux/faits_10k.csv. Un chiffre n'est
    connu qu'à partir du lendemain de son dépôt. Renvoie une ligne par CIK.
    """
    connus = faits[faits.depose_le < date]
    lignes = {}
    for cik, f in connus.groupby("cik"):
        actif = f[f.etiquette == "Assets"]
        if actif.empty:
            continue
        fin = actif.fin.max()
        ligne = {"fin_exercice": fin}
        for nom, etiquettes in FLUX.items():
            ligne[nom] = _premiere_publication(f, etiquettes, fin, True)
        for nom, etiquettes in STOCKS.items():
            ligne[nom] = _premiere_publication(f, etiquettes, fin, False)
        anterieures = sorted(d for d in actif.fin.unique()
                             if 330 <= (pd.Timestamp(fin) - pd.Timestamp(d)).days <= 400)
        ligne["actif_precedent"] = (_premiere_publication(f, ["Assets"], anterieures[-1], False)
                                    if anterieures else np.nan)
        flottant = f[(f.etiquette == "EntityPublicFloat") & (f.valeur > 0)].sort_values(["depose_le", "fin"])
        ligne["flottant"] = float(flottant.valeur.iloc[-1]) if len(flottant) else np.nan
        ligne["date_flottant"] = flottant.fin.iloc[-1] if len(flottant) else None
        lignes[cik] = ligne
    return pd.DataFrame.from_dict(lignes, orient="index")


def criteres(fonda, indice_prix, titre_de, date):
    """Les cinq critères de la section IX ; le sens est tel que plus haut vaut mieux."""
    c = pd.DataFrame(index=fonda.index)
    marge = fonda.marge_brute.fillna(fonda.chiffre_affaires - fonda.cout_ventes)
    c["profitabilite"] = marge / fonda.actif
    c["qualite"] = (fonda.flux_exploitation - fonda.benefice) / fonda.actif
    c["croissance_actif"] = -(fonda.actif / fonda.actif_precedent - 1)
    capitalisation = pd.Series(np.nan, index=fonda.index)
    for cik, ligne in fonda.iterrows():
        titre = titre_de.get(cik)
        if titre is None or pd.isna(ligne.flottant) or ligne.date_flottant is None:
            continue
        serie = indice_prix[titre]
        avant = serie.loc[:date].iloc[:-1].dropna()
        au_flottant = serie.loc[:ligne.date_flottant].dropna()
        if len(avant) and len(au_flottant):
            capitalisation[cik] = ligne.flottant * avant.iloc[-1] / au_flottant.iloc[-1]
    c["rendement_benefice"] = fonda.benefice / capitalisation
    c["solidite"] = fonda.capitaux_propres / fonda.actif
    return c.replace([np.inf, -np.inf], np.nan)


def notes_par_groupe(crit, groupe_de_cik, eligibles):
    """Moyenne des rangs centiles de chaque critère, calculés dans chaque groupe ; absent = 0,5."""
    crit = crit.reindex(sorted(eligibles))
    groupes = pd.Series({c: groupe_de_cik[c] for c in crit.index})
    centiles = crit.groupby(groupes).rank(pct=True)
    return centiles.fillna(0.5).mean(axis=1)


def selectionner(regle, notes, groupe_de_cik):
    """Entreprises retenues : S0 toutes, S1 moitié par groupe, S2 tiers par groupe, S3 moitié globale."""
    if regle == "S0":
        return list(notes.index)
    if regle == "S3":
        return list(notes.sort_values(ascending=False).index[:int(np.ceil(len(notes) / 2))])
    part = {"S1": 2, "S2": 3}[regle]
    retenues = []
    groupes = pd.Series({c: groupe_de_cik[c] for c in notes.index})
    for _, bloc in notes.groupby(groupes):
        retenues += list(bloc.sort_values(ascending=False).index[:int(np.ceil(len(bloc) / part))])
    return retenues


# --------------------------------------------------------------------------
# Mesures et contrôles statistiques
# --------------------------------------------------------------------------

def sharpe_quotidien(r, rf):
    x = r - rf
    return float(x.mean() / x.std(ddof=1))


def sharpe_deflate(sr, variance_sr, essais, T, asymetrie, aplatissement):
    """Deflated Sharpe Ratio (Bailey et López de Prado, 2014).

    `sr` et `variance_sr` sont exprimés par période, `aplatissement` est le
    moment d'ordre quatre non excédentaire. Renvoie la probabilité que le vrai
    Sharpe dépasse le maximum attendu de `essais` stratégies sans talent.
    """
    if essais < 2:
        raise ValueError("Au moins deux essais.")
    sr0 = sqrt(variance_sr) * ((1 - EULER) * _N.inv_cdf(1 - 1 / essais)
                               + EULER * _N.inv_cdf(1 - 1 / (essais * e)))
    denominateur = sqrt(1 - asymetrie * sr + (aplatissement - 1) / 4 * sr ** 2)
    return _N.cdf((sr - sr0) * sqrt(T - 1) / denominateur), sr0


def probabilite_surapprentissage(R, blocs=16):
    """Probabilité de surapprentissage par validation croisée combinatoire.

    `R` est un tableau T x K de rendements excédentaires. Pour chaque moitié
    des blocs prise comme échantillon d'apprentissage, la meilleure stratégie
    y est choisie au Sharpe, et son rang est lu sur l'autre moitié. La
    probabilité est la part des cas où elle finit sous la médiane.
    """
    R = np.asarray(R, dtype=float)
    T, K = R.shape
    bornes = np.linspace(0, T, blocs + 1).astype(int)
    s1 = np.array([R[a:b].sum(0) for a, b in zip(bornes[:-1], bornes[1:])])
    s2 = np.array([(R[a:b] ** 2).sum(0) for a, b in zip(bornes[:-1], bornes[1:])])
    n = np.diff(bornes)
    from itertools import combinations

    def sharpe(masque):
        m = n[masque].sum()
        moy = s1[masque].sum(0) / m
        var = s2[masque].sum(0) / m - moy ** 2
        return moy / np.sqrt(np.maximum(var, 1e-300))

    logits = []
    for choix in combinations(range(blocs), blocs // 2):
        masque = np.zeros(blocs, bool)
        masque[list(choix)] = True
        meilleur = np.argmax(sharpe(masque))
        hors = sharpe(~masque)
        omega = (hors < hors[meilleur]).sum() / K + 0.5 / K
        logits.append(log(omega / (1 - omega)))
    logits = np.array(logits)
    return float((logits <= 0).mean()), logits


def test_white(R, reference, indices):
    """Test de White (2000) sur le maximum des écarts de Sharpe avec une référence.

    `R` est T x K, `reference` de longueur T, en rendements excédentaires ;
    `indices` vient d'un bootstrap par blocs. Renvoie l'écart maximal observé
    et la probabilité qu'un maximum aussi grand apparaisse sans talent.
    """
    R = np.asarray(R, dtype=float)
    ref = np.asarray(reference, dtype=float)

    def ecarts(X, y):
        return X.mean(0) / X.std(0, ddof=1) - y.mean() / y.std(ddof=1)

    observe = ecarts(R, ref)
    maxima = np.array([(ecarts(R[i], ref[i]) - observe).max() for i in indices])
    return float(observe.max()), float((maxima >= observe.max()).mean())


def christoffersen(depassements):
    """Rapport de vraisemblance d'indépendance des dépassements (Christoffersen, 1998)."""
    x = np.asarray(depassements, dtype=int)
    a, b = x[:-1], x[1:]
    n00, n01 = int(((a == 0) & (b == 0)).sum()), int(((a == 0) & (b == 1)).sum())
    n10, n11 = int(((a == 1) & (b == 0)).sum()), int(((a == 1) & (b == 1)).sum())
    if n01 + n11 == 0 or n00 + n10 == 0:
        return float("nan")
    p01, p11 = n01 / (n00 + n01), n11 / max(n10 + n11, 1)
    p = (n01 + n11) / (n00 + n01 + n10 + n11)

    def l(k, q):
        return k * log(q) if k > 0 else 0.0

    libre = l(n00, 1 - p01) + l(n01, p01) + l(n10, 1 - p11) + l(n11, p11)
    contraint = l(n00 + n10, 1 - p) + l(n01 + n11, p)
    return float(-2 * (contraint - libre))


# --------------------------------------------------------------------------
# Portefeuilles aléatoires
# --------------------------------------------------------------------------

def portefeuilles_aleatoires(R, eligibles, n, graine, rf, cout=COUT, paquet=5000, taille_min=10):
    """Mesures de `n` portefeuilles tirés au hasard, rééquilibrés aux dates d'`eligibles`.

    `R` est le tableau T x N des rendements totaux ; `eligibles` associe à
    chaque date de rééquilibrage la liste des titres éligibles. Chaque
    portefeuille a une taille, un ordre de priorité et des poids bruts tirés
    une fois pour toutes (section IX, tâche 6). Renvoie un tableau de mesures.
    """
    rng = np.random.default_rng(graine)
    colonnes = list(R.columns)
    X = np.nan_to_num(R.to_numpy(dtype=np.float64))
    dates = [str(d) for d in R.index]
    debuts = [i for i, d in enumerate(dates) if d in eligibles]
    if debuts[0] != 0:
        raise ValueError("La première date doit être une date de rééquilibrage.")
    masques = {i: np.isin(colonnes, eligibles[dates[i]]) for i in debuts}
    rfv = np.nan_to_num(rf.reindex(R.index).to_numpy())[1:]
    resultats = []
    for depart in range(0, n, paquet):
        m = min(paquet, n - depart)
        taille = rng.integers(taille_min, len(colonnes) + 1, m)
        priorite = rng.random((m, len(colonnes)))
        brut = rng.exponential(1.0, (m, len(colonnes)))
        valeurs = np.empty((len(dates), m))
        V = np.full(m, 100.0)
        poches = None
        for k, i0 in enumerate(debuts):
            i1 = debuts[k + 1] if k + 1 < len(debuts) else len(dates) - 1
            p = np.where(masques[i0], priorite, -1.0)
            rang = np.argsort(np.argsort(-p, axis=1), axis=1)
            limite = np.minimum(taille, masques[i0].sum())[:, None]
            w = np.where(rang < limite, brut, 0.0)
            w /= w.sum(1, keepdims=True)
            if poches is not None:
                V = V - cout * np.abs(w * V[:, None] - poches).sum(1)
            valeurs[i0] = V
            poches = w * V[:, None]
            if i1 > i0:
                croissance = np.cumprod(1 + X[i0 + 1:i1 + 1], axis=0)
                chemin = croissance @ (w * V[:, None]).T
                valeurs[i0 + 1:i1 + 1] = chemin
                poches = (w * V[:, None]) * croissance[-1]
                V = chemin[-1]
        r = valeurs[1:] / valeurs[:-1] - 1
        ex = r - rfv[:, None]
        pic = np.maximum.accumulate(valeurs, axis=0)
        q = np.quantile(r, 0.01, axis=0)
        es = np.array([-r[r[:, j] <= q[j], j].mean() for j in range(m)])
        resultats.append(pd.DataFrame({
            "taille": taille, "annualise": (valeurs[-1] / valeurs[0]) ** (SEANCES / len(r)) - 1,
            "volatilite": r.std(0, ddof=1) * sqrt(SEANCES),
            "sharpe": ex.mean(0) / ex.std(0, ddof=1) * sqrt(SEANCES),
            "repli_max": (valeurs / pic - 1).min(0), "es99": es}))
    return pd.concat(resultats, ignore_index=True)
