"""Stratégies de diversification et de couverture de l'étape 4.

Les décisions appliquées ici sont fixées dans la phase 0 de l'étape 4,
section VII de research/plan_projet.md, écrite avant tout calcul. Chaque
fonction prend des rendements quotidiens alignés sur le même calendrier et
renvoie une série de valeur partant de 100.
"""
from math import erf, sqrt

import numpy as np
import pandas as pd

SEANCES = 252
COUT_MELANGE = 0.0010   # taux de l'étape 2, sur le montant échangé
COUT_FUTUR = 0.0002     # par unité de nominal échangé
FOURCHETTE_PUT = 0.05   # part de la prime payée en plus à l'achat


def _phi(x):
    x = np.asarray(x, dtype=float)
    return 0.5 * (1 + np.vectorize(erf)(x / sqrt(2)))


def put_black_scholes(S, K, T, r, q, sigma):
    """Prix d'un put européen, taux et dividendes en composition continue.

    À l'échéance, T nul, le prix est la valeur intrinsèque. Ce prix est celui
    d'un modèle : il suppose une volatilité constante jusqu'à l'échéance.
    """
    S, K, T, r, q, sigma = (np.asarray(v, dtype=float) for v in (S, K, T, r, q, sigma))
    if np.any(S <= 0) or np.any(K <= 0) or np.any(sigma <= 0) or np.any(T < 0):
        raise ValueError("Cours, prix d'exercice et volatilité positifs, durée non négative.")
    intrinseque = np.maximum(K - S, 0.0)
    Ts = np.where(T > 0, T, 1.0)
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma ** 2) * Ts) / (sigma * np.sqrt(Ts))
    d2 = d1 - sigma * np.sqrt(Ts)
    prix = K * np.exp(-r * Ts) * _phi(-d2) - S * np.exp(-q * Ts) * _phi(-d1)
    resultat = np.where(T > 0, prix, intrinseque)
    return float(resultat) if resultat.ndim == 0 else resultat


def premieres_seances_annee(index):
    dates = pd.Series(index, index=index).astype(str)
    return set(dates.groupby(dates.str[:4]).min())


def fins_de_mois(index):
    dates = pd.Series(index, index=index).astype(str)
    return set(dates.groupby(dates.str[:7]).max())


def melange(r_a, r_b, part_a, jours_reeq, cout=COUT_MELANGE):
    """Deux actifs ramenés à leurs parts cibles aux dates données, dérive entre elles.

    Le rééquilibrage se fait à la clôture de la date. Le coût vaut `cout` fois
    le montant total échangé et il est prélevé avant la remise aux cibles.
    Aucun coût n'est payé à la constitution : la série actions a déjà payé le
    sien à l'étape 2, et l'autre actif part de la même date.
    Renvoie la valeur et le total des frais payés.
    """
    if not 0 <= part_a <= 1:
        raise ValueError("La part doit être comprise entre 0 et 1.")
    a = np.nan_to_num(np.asarray(r_a, dtype=float))
    b = np.nan_to_num(np.asarray(r_b, dtype=float))
    reeq = np.asarray([str(d) in jours_reeq for d in r_a.index])
    A, B = 100.0 * part_a, 100.0 * (1 - part_a)
    valeurs, frais = np.empty(len(a)), 0.0
    for i in range(len(a)):
        if i > 0:
            A *= 1 + a[i]
            B *= 1 + b[i]
            if reeq[i]:
                V = A + B
                paye = cout * (abs(part_a * V - A) + abs((1 - part_a) * V - B))
                V -= paye
                frais += paye
                A, B = part_a * V, (1 - part_a) * V
        valeurs[i] = A + B
    return pd.Series(valeurs, index=r_a.index), frais


def beta_glissant(r_s, r_m, fenetre=SEANCES, minimum=63):
    """Bêta de r_s sur r_m, estimé sur les `fenetre` séances précédentes.

    La valeur à une date n'utilise que les rendements jusqu'à la veille.
    Tant que moins de `minimum` observations existent, le bêta vaut un :
    complément du 28 septembre 2026, section VII du plan.
    """
    cov = r_s.rolling(fenetre, min_periods=minimum).cov(r_m)
    var = r_m.rolling(fenetre, min_periods=minimum).var()
    return (cov / var).shift(1).fillna(1.0)


def couverture_futur(r_s, excedent_marche, beta, part, fins, trimestres, cout=COUT_FUTUR):
    """Portefeuille et vente d'un nominal de contrat à terme révisé en fin de mois.

    `excedent_marche` est le rendement du marché diminué du taux sans risque,
    rendement d'un contrat à terme sous la relation de portage. Le nominal,
    `part` fois le bêta fois la valeur, est fixé à la clôture de chaque fin de
    mois et reste constant en dollars jusqu'à la suivante. Aux fins de
    trimestre, le nominal est aussi réputé fermé et rouvert.
    """
    s = np.nan_to_num(np.asarray(r_s, dtype=float))
    e = np.nan_to_num(np.asarray(excedent_marche, dtype=float))
    b = np.asarray(beta, dtype=float)
    dates = [str(d) for d in r_s.index]
    V, N = 100.0, 0.0
    valeurs, frais = np.empty(len(s)), 0.0
    for i, jour in enumerate(dates):
        if i > 0:
            V = V * (1 + s[i]) - N * e[i]
        if i == 0 or jour in fins:
            nouveau = part * b[i] * V
            echange = abs(nouveau - N) + (2 * N if jour in trimestres else 0.0)
            V -= cout * echange
            frais += cout * echange
            N = nouveau
        valeurs[i] = V
    return pd.Series(valeurs, index=r_s.index), frais


def protection_put(r_s, S, sigma, r, q, beta, fins, niveau, fourchette=FOURCHETTE_PUT):
    """Portefeuille et achat mensuel de puts à un mois sur l'indice.

    À chaque date de renouvellement, le put échu vaut sa valeur intrinsèque et
    est encaissé ; un nouveau put au prix d'exercice `niveau` fois le cours est
    acheté sur un nominal égal au bêta fois la valeur, et payé en vendant des
    actions, fourchette comprise. Entre deux dates, le put est revalorisé
    chaque jour avec la volatilité et la durée restante du jour.
    Renvoie la valeur, les primes payées et les montants encaissés.
    """
    s = np.nan_to_num(np.asarray(r_s, dtype=float))
    S, sigma, r, q, b = (np.asarray(v, dtype=float) for v in (S, sigma, r, q, beta))
    dates = [str(d) for d in r_s.index]
    roulements = [0] + [i for i, d in enumerate(dates) if d in fins and i > 0]
    echeance = {debut: fin for debut, fin in zip(roulements, roulements[1:] + [len(dates) - 1])}
    E, n, K, fin = 100.0, 0.0, 1.0, 0
    valeurs, primes, encaisse = np.empty(len(s)), 0.0, 0.0
    for i in range(len(s)):
        if i > 0:
            E *= 1 + s[i]
        T = max(fin - i, 0) / SEANCES
        option = n * put_black_scholes(S[i], K, T, r[i], q[i], sigma[i]) if n else 0.0
        if i in echeance and i > 0:
            E += option              # le put échu vaut sa valeur intrinsèque
            encaisse += option
            option, n = 0.0, 0.0
        if i in echeance and echeance[i] > i:
            fin = echeance[i]
            K = niveau * S[i]
            n = b[i] * E / S[i]
            prix = put_black_scholes(S[i], K, (fin - i) / SEANCES, r[i], q[i], sigma[i])
            E -= n * prix * (1 + fourchette)
            primes += n * prix * (1 + fourchette)
            option = n * prix
        valeurs[i] = E + option
    return pd.Series(valeurs, index=r_s.index), primes, encaisse


def part_a_risque_egal(r_s, r_liquide, jours_reeq, cible, mesure, cout=COUT_MELANGE,
                       tolerance=1e-7):
    """Part de la série, mêlée aux liquidités, qui atteint la mesure de risque cible.

    Recherche par dichotomie : la mesure croît avec la part de la série.
    Renvoie la part et la valeur du mélange. Si la cible dépasse le risque de
    la série seule, la part vaut un et le mélange est la série.
    """
    def risque_de(p):
        valeur, _ = melange(r_s, r_liquide, p, jours_reeq, cout)
        return mesure(valeur.pct_change().dropna()), valeur

    haut, valeur_haut = risque_de(1.0)
    if cible >= haut:
        return 1.0, valeur_haut
    bas_p, haut_p = 0.0, 1.0
    while haut_p - bas_p > tolerance:
        milieu = (bas_p + haut_p) / 2
        if risque_de(milieu)[0] < cible:
            bas_p = milieu
        else:
            haut_p = milieu
    p = (bas_p + haut_p) / 2
    return p, risque_de(p)[1]


def vente_puts_garantie(S, sigma, r, q, rendement_liquide, fins, niveau=1.0):
    """Vente mensuelle de puts garantie par des liquidités, pour contrôler le modèle.

    Réplique la logique de l'indice CBOE PutWrite : à chaque date de
    renouvellement, le vendeur encaisse la prime de puts sur un nominal égal à
    sa valeur, au prix d'exercice `niveau` fois le cours, et paie la valeur
    intrinsèque à l'échéance. Les liquidités rapportent `rendement_liquide`.
    Si le modèle surévalue les puts, cette réplique rapporte plus que l'indice.
    """
    S, sigma, r, q = (np.asarray(v, dtype=float) for v in (S, sigma, r, q))
    liquide = np.nan_to_num(np.asarray(rendement_liquide, dtype=float))
    dates = [str(d) for d in rendement_liquide.index]
    roulements = [0] + [i for i, d in enumerate(dates) if d in fins and i > 0]
    echeance = {debut: fin for debut, fin in zip(roulements, roulements[1:] + [len(dates) - 1])}
    L, n, K, fin = 100.0, 0.0, 1.0, 0
    valeurs = np.empty(len(dates))
    for i in range(len(dates)):
        if i > 0:
            L *= 1 + liquide[i]
        T = max(fin - i, 0) / SEANCES
        dette = n * put_black_scholes(S[i], K, T, r[i], q[i], sigma[i]) if n else 0.0
        if i in echeance and i > 0:
            L -= dette
            dette, n = 0.0, 0.0
        if i in echeance and echeance[i] > i:
            fin = echeance[i]
            K = niveau * S[i]
            n = L / K
            prime = put_black_scholes(S[i], K, (fin - i) / SEANCES, r[i], q[i], sigma[i])
            L += n * prime
            dette = n * prime
        valeurs[i] = L - dette
    return pd.Series(valeurs, index=rendement_liquide.index)


def melange_multiple(rendements, cibles, cout=COUT_MELANGE):
    """Plusieurs poches ramenées à leurs poids cibles aux dates de `cibles`, dérive entre elles.

    `rendements` est un tableau de rendements quotidiens, une colonne par poche.
    `cibles` associe à chaque date de rééquilibrage une série de poids qui
    somment à un ; la première date du tableau doit y figurer. Le coût vaut
    `cout` fois le montant total échangé, prélevé avant la remise aux cibles,
    sauf à la constitution. Renvoie la valeur et le total des frais.
    """
    r = np.nan_to_num(rendements.to_numpy(dtype=float))
    colonnes = list(rendements.columns)
    dates = [str(d) for d in rendements.index]
    if dates[0] not in cibles:
        raise ValueError("La première date doit porter des poids cibles.")
    for w in cibles.values():
        if not np.isclose(sum(w.values) if hasattr(w, "values") else sum(w), 1) or min(w) < 0:
            raise ValueError("Les poids cibles doivent être positifs et sommer à un.")
    poches = 100.0 * cibles[dates[0]].reindex(colonnes).to_numpy(dtype=float)
    valeurs, frais = np.empty(len(dates)), 0.0
    for i, jour in enumerate(dates):
        if i > 0:
            poches = poches * (1 + r[i])
            if jour in cibles:
                w = cibles[jour].reindex(colonnes).to_numpy(dtype=float)
                V = poches.sum()
                paye = cout * np.abs(w * V - poches).sum()
                frais += paye
                poches = w * (V - paye)
        valeurs[i] = poches.sum()
    return pd.Series(valeurs, index=rendements.index), frais


def poids_inverse_volatilite(rendements, fenetre=SEANCES, minimum=63):
    """Poids inversement proportionnels à la volatilité des poches sur la fenêtre.

    Les poches dont l'historique est trop court reçoivent la volatilité
    médiane des autres. Ce n'est une égalité des contributions au risque que
    si les corrélations entre poches sont égales.
    """
    bloc = rendements.iloc[-fenetre:]
    vol = bloc.std().where(bloc.count() >= minimum)
    if vol.isna().all():
        return pd.Series(1 / len(vol), index=vol.index)
    vol = vol.fillna(vol.median())
    inverse = 1 / vol
    return inverse / inverse.sum()
