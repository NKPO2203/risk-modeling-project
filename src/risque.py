"""Mesures de risque de l'etape 3.

Les conventions appliquees ici sont fixees dans la phase 0 de l'etape 3,
section VI de research/plan_projet.md. Elles ne doivent pas etre modifiees
sans que la modification soit datee et motivee dans ce document.
"""
import numpy as np
import pandas as pd

SEANCES = 252
MOIS = 12


def annualiser_rendement(niveau, periodes=SEANCES):
    """Rendement geometrique annualise, a partir du premier et du dernier niveau.

    La moyenne arithmetique multipliee par le nombre de periodes s'ecarte de la
    moitie de la variance environ, et cet ecart croit avec la volatilite : elle
    flatterait donc les series les plus agitees.
    """
    n = len(niveau)
    if n < 2:
        raise ValueError("Au moins deux niveaux sont necessaires.")
    return float((niveau.iloc[-1] / niveau.iloc[0]) ** (periodes / n) - 1)


def volatilite(rendements, periodes=SEANCES):
    """Ecart-type annualise. La racine suppose des rendements independants."""
    return float(rendements.std() * np.sqrt(periodes))


def volatilite_baisse(excedents, periodes=SEANCES):
    """Deviation a la baisse au sens de Sortino.

    Racine de la moyenne des carres des ecarts sous le seuil, calculee sur
    toutes les observations, les periodes au-dessus du seuil comptant zero.
    Ce n'est pas l'ecart-type des seules observations negatives, qui ne divise
    que par leur nombre et surestime la dispersion.
    """
    return float(np.sqrt((np.minimum(excedents, 0) ** 2).mean()) * np.sqrt(periodes))


def sharpe(rendements, sans_risque, periodes=SEANCES):
    excedents = (rendements - sans_risque.reindex(rendements.index)).dropna()
    return float(excedents.mean() * np.sqrt(periodes) / rendements.std())


def sortino(rendements, sans_risque, periodes=SEANCES):
    excedents = (rendements - sans_risque.reindex(rendements.index)).dropna()
    return float(excedents.mean() * periodes / volatilite_baisse(excedents, periodes))


def drawdown(niveau):
    """Repli maximal, ses bornes, sa duree et son temps de recuperation."""
    repli = niveau / niveau.cummax() - 1
    creux = repli.idxmin()
    sommet = niveau.loc[:creux].idxmax()
    apres = niveau.loc[creux:]
    rattrape = apres[apres >= niveau.loc[sommet]]
    retour = rattrape.index[0] if len(rattrape) else None

    position = niveau.index.get_loc
    return {"repli_max": float(repli.min()), "sommet": sommet, "creux": creux,
            "retour": retour,
            "chute": position(creux) - position(sommet),
            "recuperation": position(retour) - position(creux) if retour else None,
            "part_sous_l_eau": float((repli < -1e-12).mean())}


def var_historique(rendements, seuil=0.95):
    """Perte exprimee en positif, lue directement dans les rendements observes."""
    if not 0 < seuil < 1:
        raise ValueError("Le seuil doit etre strictement compris entre 0 et 1.")
    return float(-rendements.quantile(1 - seuil))


def perte_au_dela(rendements, seuil=0.95):
    """Perte moyenne conditionnelle a un depassement de la VaR, en positif.

    Elle est toujours superieure ou egale a la VaR : la VaR dit ou commence la
    zone dangereuse, celle-ci dit ce qu'on y trouve.
    """
    limite = rendements.quantile(1 - seuil)
    queue = rendements[rendements <= limite]
    if queue.empty:
        return float("nan")
    return float(-queue.mean())


def kupiec(n, x, p):
    """Rapport de vraisemblance de couverture, calcule en logarithmes.

    La forme directe (1-p)**(n-x) passe sous le plus petit flottant
    representable des que n depasse quelques centaines, et son logarithme vaut
    alors moins l'infini. Le calcul en logarithmes evite cet ecueil.
    """
    if not 0 < p < 1:
        raise ValueError("La probabilite doit etre strictement comprise entre 0 et 1.")
    if x <= 0 or x >= n:
        return float("nan")
    taux = x / n
    return float(-2 * ((n - x) * np.log(1 - p) + x * np.log(p)
                       - (n - x) * np.log(1 - taux) - x * np.log(taux)))


def rho_implicite(bloc):
    """Correlation moyenne deduite de la variance du portefeuille equipondere.

    Identite exacte, qui evite de former une matrice de correlation complete.
    Elle pondere chaque paire par le produit des volatilites, contrairement a
    la moyenne simple des correlations par paires.
    """
    ecarts = bloc.std().dropna()
    n = len(ecarts)
    if n < 2:
        return float("nan")
    variance = bloc[ecarts.index].mean(axis=1).var()
    carres = (ecarts ** 2).sum()
    denominateur = ecarts.sum() ** 2 - carres
    if denominateur == 0:
        return float("nan")
    return float((n ** 2 * variance - carres) / denominateur)


def n_effectif(rho, n):
    """Nombre d'actifs independants donnant la meme reduction de variance."""
    if n < 1:
        raise ValueError("Le nombre de titres doit etre au moins un.")
    return float(1 / (rho + (1 - rho) / n))


def contributions_au_risque(poids, covariance):
    """Contribution de chaque ligne a la volatilite du portefeuille.

    Les contributions somment exactement a cette volatilite, par homogeneite
    de degre un. C'est le controle du calcul.
    """
    poids = np.asarray(poids, dtype=float)
    covariance = np.asarray(covariance, dtype=float)
    if not np.allclose(poids.sum(), 1):
        raise ValueError("Les poids doivent sommer a un.")
    sigma_w = covariance @ poids
    vol = float(np.sqrt(poids @ sigma_w))
    if vol == 0:
        raise ValueError("Volatilite nulle : contributions indefinies.")
    return poids * sigma_w / vol, vol


def herfindahl(parts):
    """Somme des carres des parts ; son inverse se lit comme un nombre de lignes."""
    parts = np.asarray(parts, dtype=float)
    return float((parts ** 2).sum())


def episodes_de_tension(niveau, seuil=0.15):
    """Replis du niveau de reference d'au moins `seuil` depuis son plus haut.

    Un episode va du sommet au creux ; la date de retour au sommet est
    enregistree separement et n'en fait pas partie. La regle s'applique sans
    connaitre la suite de la serie.
    """
    if not 0 < seuil < 1:
        raise ValueError("Le seuil doit etre strictement compris entre 0 et 1.")
    sommet = niveau.cummax()
    groupe = (sommet != sommet.shift()).cumsum()

    lignes = []
    for _, segment in niveau.groupby(groupe):
        repli = segment / segment.iloc[0] - 1
        if repli.min() <= -seuil:
            dernier = segment.index[-1]
            retour = (niveau.index[niveau.index.get_loc(dernier) + 1]
                      if dernier != niveau.index[-1] else None)
            lignes.append({"debut": segment.index[0], "creux": repli.idxmin(),
                           "repli": float(repli.min()), "retour": retour,
                           "seances": len(segment)})
    return pd.DataFrame(lignes)
