"""Cas de contrôle des stratégies de l'étape 4 (src/couverture.py)."""
import numpy as np
import pandas as pd
import pytest

from src import couverture as c


def jours(n, debut="2000-01-03"):
    return pd.Index(pd.bdate_range(debut, periods=n).strftime("%Y-%m-%d"), name="date")


def test_put_valeur_de_reference():
    # Hull, S = K = 100, un an, r = 5 %, sigma = 20 % : put = 5,5735.
    assert c.put_black_scholes(100, 100, 1, 0.05, 0, 0.2) == pytest.approx(5.5735, abs=1e-4)


def test_put_parite_avec_le_call():
    S, K, T, r, q, s = 100.0, 95.0, 0.25, 0.03, 0.015, 0.3
    from math import erf, exp, log, sqrt
    N = lambda x: 0.5 * (1 + erf(x / sqrt(2)))
    d1 = (log(S / K) + (r - q + s * s / 2) * T) / (s * sqrt(T))
    call = S * exp(-q * T) * N(d1) - K * exp(-r * T) * N(d1 - s * sqrt(T))
    put = c.put_black_scholes(S, K, T, r, q, s)
    assert call - put == pytest.approx(S * exp(-q * T) - K * exp(-r * T), abs=1e-10)


def test_put_bornes_et_echeance():
    S, K, T, r = 100.0, 110.0, 0.5, 0.04
    p = c.put_black_scholes(S, K, T, r, 0.0, 0.25)
    assert max(K * np.exp(-r * T) - S, 0) <= p <= K * np.exp(-r * T)
    assert c.put_black_scholes(90, 100, 0, r, 0, 0.2) == pytest.approx(10.0)
    assert c.put_black_scholes(110, 100, 0, r, 0, 0.2) == 0.0
    with pytest.raises(ValueError):
        c.put_black_scholes(100, 100, 1, 0.01, 0, 0.0)


def test_melange_part_un_rend_la_serie():
    idx = jours(300)
    rng = np.random.default_rng(1)
    a = pd.Series(rng.normal(0, 0.01, 300), index=idx)
    b = pd.Series(rng.normal(0, 0.002, 300), index=idx)
    v, frais = c.melange(a, b, 1.0, c.premieres_seances_annee(idx))
    attendu = 100 * (1 + a.iloc[1:]).cumprod()
    assert np.allclose(v.iloc[1:], attendu) and frais == 0


def test_melange_sans_reequilibrage_est_la_somme_des_poches():
    idx = jours(200)
    rng = np.random.default_rng(2)
    a = pd.Series(rng.normal(0, 0.01, 200), index=idx)
    b = pd.Series(rng.normal(0, 0.003, 200), index=idx)
    v, _ = c.melange(a, b, 0.6, set())
    a0, b0 = a.copy(), b.copy()
    a0.iloc[0] = b0.iloc[0] = 0
    attendu = 60 * (1 + a0).cumprod() + 40 * (1 + b0).cumprod()
    assert np.allclose(v, attendu)


def test_melange_frais_egaux_au_montant_echange():
    idx = pd.Index(["2000-12-29", "2001-01-02"])
    a = pd.Series([0.0, 0.5], index=idx)
    b = pd.Series([0.0, 0.0], index=idx)
    v, frais = c.melange(a, b, 0.5, {"2001-01-02"}, cout=0.01)
    # 50 -> 75 et 50 : valeur 125, cibles 62,5 et 62,5, échange 25, frais 0,25.
    assert frais == pytest.approx(0.25) and v.iloc[-1] == pytest.approx(124.75)


def test_beta_n_utilise_pas_l_avenir():
    idx = jours(400)
    rng = np.random.default_rng(3)
    m = pd.Series(rng.normal(0, 0.01, 400), index=idx)
    s = 1.5 * m + pd.Series(rng.normal(0, 0.002, 400), index=idx)
    b1 = c.beta_glissant(s, m)
    s2 = s.copy()
    s2.iloc[300:] = 0.2
    b2 = c.beta_glissant(s2, m)
    assert np.allclose(b1.iloc[:301], b2.iloc[:301])
    assert b1.iloc[10] == 1.0 and b1.iloc[-1] == pytest.approx(1.5, abs=0.05)


def test_futur_couvre_entierement_le_marche():
    idx = jours(260)
    rng = np.random.default_rng(4)
    rf = pd.Series(0.0001, index=idx)
    m = pd.Series(rng.normal(0.0005, 0.012, 260), index=idx)
    beta = pd.Series(1.0, index=idx)
    # Nominal révisé chaque jour : le portefeuille identique au marché ne gagne que le taux sans risque.
    v, _ = c.couverture_futur(m, m - rf, beta, 1.0, set(idx.astype(str)), set(), cout=0.0)
    r = v.pct_change().dropna()
    assert np.allclose(r, rf.iloc[1:])


def test_futur_frais_de_roulement():
    idx = jours(3)
    zero = pd.Series(0.0, index=idx)
    v, frais = c.couverture_futur(zero, zero, pd.Series(1.0, index=idx), 1.0,
                                  {idx[1]}, {idx[1]}, cout=0.001)
    # Constitution : 100 échangés. Fin de trimestre : le nominal passe de 100 à 99,9,
    # et les 100 en place sont fermés puis rouverts.
    assert frais == pytest.approx(0.1 + 0.001 * (0.1 + 2 * 100))


def test_put_identite_a_l_achat_et_protection():
    idx = jours(3)
    r_s = pd.Series([0.0, -0.3, 0.0], index=idx)
    S = pd.Series([100.0, 70.0, 70.0], index=idx)
    un = pd.Series(1.0, index=idx)
    v, primes, encaisse = c.protection_put(r_s, S, 0.2 * un, 0.0 * un, 0.0 * un, un,
                                           {idx[2]}, niveau=0.9, fourchette=0.0)
    # À la constitution, la valeur totale reste 100 sans fourchette.
    assert v.iloc[0] == pytest.approx(100.0)
    # À l'échéance, le put paie 90 - 70 = 20 par unité, pour une unité.
    assert encaisse == pytest.approx(20.0)
    assert v.iloc[2] == pytest.approx((100 - primes) * 0.7 + 20.0)


def test_part_a_risque_egal():
    idx = jours(600)
    rng = np.random.default_rng(5)
    s = pd.Series(rng.normal(0.0004, 0.012, 600), index=idx)
    liquide = pd.Series(0.0001, index=idx)
    vol = lambda r: r.std() * np.sqrt(252)
    cible = 0.5 * vol(s)
    p, valeur = c.part_a_risque_egal(s, liquide, c.premieres_seances_annee(idx), cible, vol)
    assert vol(valeur.pct_change().dropna()) == pytest.approx(cible, rel=1e-5)
    assert 0.45 < p < 0.55


def test_vente_de_puts_garantie():
    idx = jours(3)
    S = pd.Series([100.0, 80.0, 80.0], index=idx)
    un = pd.Series(1.0, index=idx)
    zero = pd.Series(0.0, index=idx)
    v = c.vente_puts_garantie(S, 0.2 * un, zero, zero, zero, {idx[2]})
    prime = c.put_black_scholes(100, 100, 2 / 252, 0, 0, 0.2)
    # Nominal : 100 / 100 = 1 put ; à l'échéance, le vendeur paie 100 - 80 = 20.
    assert v.iloc[0] == pytest.approx(100.0)
    assert v.iloc[2] == pytest.approx(100 + prime - 20)


def test_melange_multiple_egal_au_melange_a_deux():
    idx = jours(600)
    rng = np.random.default_rng(6)
    a = pd.Series(rng.normal(0, 0.01, 600), index=idx)
    b = pd.Series(rng.normal(0, 0.003, 600), index=idx)
    annuel = c.premieres_seances_annee(idx)
    deux, frais2 = c.melange(a, b, 0.7, annuel)
    w = pd.Series({"a": 0.7, "b": 0.3})
    plusieurs, frais = c.melange_multiple(pd.DataFrame({"a": a, "b": b}), {d: w for d in annuel})
    assert np.allclose(deux, plusieurs) and frais == pytest.approx(frais2)


def test_melange_multiple_refuse_des_poids_invalides():
    idx = jours(3)
    df = pd.DataFrame({"a": 0.0, "b": 0.0}, index=idx)
    with pytest.raises(ValueError):
        c.melange_multiple(df, {idx[0]: pd.Series({"a": 0.8, "b": 0.3})})
    with pytest.raises(ValueError):
        c.melange_multiple(df, {idx[1]: pd.Series({"a": 0.5, "b": 0.5})})


def test_poids_inverse_volatilite():
    idx = jours(300)
    rng = np.random.default_rng(7)
    df = pd.DataFrame({"calme": rng.normal(0, 0.01, 300), "agite": rng.normal(0, 0.03, 300)}, index=idx)
    w = c.poids_inverse_volatilite(df)
    assert w.sum() == pytest.approx(1) and w["calme"] == pytest.approx(0.75, abs=0.03)
