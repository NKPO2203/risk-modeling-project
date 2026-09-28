"""Cas de contrôle des stratégies de l'étape 4 (src/couverture.py).

Écrit avec unittest, comme le reste de la suite, pour être collecté par
`python -B -m unittest discover -s tests`. La méthode `proche` reproduit la
sémantique de pytest.approx : égalité à un écart relatif près, ou à un écart
absolu près, le plus large des deux l'emportant.
"""
import builtins
import unittest
from math import erf, exp, log, sqrt

import numpy as np
import pandas as pd

from src import couverture as c


def jours(n, debut="2000-01-03"):
    return pd.Index(pd.bdate_range(debut, periods=n).strftime("%Y-%m-%d"), name="date")


class CasCouverture(unittest.TestCase):

    def proche(self, obtenu, attendu, rel=1e-6, abs=1e-12):
        tolerance = max(rel * builtins.abs(attendu), abs)
        self.assertLessEqual(builtins.abs(obtenu - attendu), tolerance,
                             f"{obtenu} n'est pas proche de {attendu} a {tolerance} pres")



class PutTests(CasCouverture):

    def test_put_valeur_de_reference(self):
        # Hull, S = K = 100, un an, r = 5 %, sigma = 20 % : put = 5,5735.
        self.proche(c.put_black_scholes(100, 100, 1, 0.05, 0, 0.2), 5.5735, abs=1e-4)

    def test_put_parite_avec_le_call(self):
        S, K, T, r, q, s = 100.0, 95.0, 0.25, 0.03, 0.015, 0.3
        N = lambda x: 0.5 * (1 + erf(x / sqrt(2)))
        d1 = (log(S / K) + (r - q + s * s / 2) * T) / (s * sqrt(T))
        call = S * exp(-q * T) * N(d1) - K * exp(-r * T) * N(d1 - s * sqrt(T))
        put = c.put_black_scholes(S, K, T, r, q, s)
        self.proche(call - put, S * exp(-q * T) - K * exp(-r * T), abs=1e-10)

    def test_put_bornes_et_echeance(self):
        S, K, T, r = 100.0, 110.0, 0.5, 0.04
        p = c.put_black_scholes(S, K, T, r, 0.0, 0.25)
        self.assertLessEqual(max(K * np.exp(-r * T) - S, 0), p)
        self.assertLessEqual(p, K * np.exp(-r * T))
        self.proche(c.put_black_scholes(90, 100, 0, r, 0, 0.2), 10.0)
        self.assertEqual(c.put_black_scholes(110, 100, 0, r, 0, 0.2), 0.0)
        with self.assertRaises(ValueError):
            c.put_black_scholes(100, 100, 1, 0.01, 0, 0.0)

    def test_put_identite_a_l_achat_et_protection(self):
        idx = jours(3)
        r_s = pd.Series([0.0, -0.3, 0.0], index=idx)
        S = pd.Series([100.0, 70.0, 70.0], index=idx)
        un = pd.Series(1.0, index=idx)
        v, primes, encaisse = c.protection_put(r_s, S, 0.2 * un, 0.0 * un, 0.0 * un, un,
                                               {idx[2]}, niveau=0.9, fourchette=0.0)
        # À la constitution, la valeur totale reste 100 sans fourchette.
        self.proche(v.iloc[0], 100.0)
        # À l'échéance, le put paie 90 - 70 = 20 par unité, pour une unité.
        self.proche(encaisse, 20.0)
        self.proche(v.iloc[2], (100 - primes) * 0.7 + 20.0)

    def test_vente_de_puts_garantie(self):
        idx = jours(3)
        S = pd.Series([100.0, 80.0, 80.0], index=idx)
        un = pd.Series(1.0, index=idx)
        zero = pd.Series(0.0, index=idx)
        v = c.vente_puts_garantie(S, 0.2 * un, zero, zero, zero, {idx[2]})
        prime = c.put_black_scholes(100, 100, 2 / 252, 0, 0, 0.2)
        # Nominal : 100 / 100 = 1 put ; à l'échéance, le vendeur paie 100 - 80 = 20.
        self.proche(v.iloc[0], 100.0)
        self.proche(v.iloc[2], 100 + prime - 20)


class MelangeTests(CasCouverture):

    def test_melange_part_un_rend_la_serie(self):
        idx = jours(300)
        rng = np.random.default_rng(1)
        a = pd.Series(rng.normal(0, 0.01, 300), index=idx)
        b = pd.Series(rng.normal(0, 0.002, 300), index=idx)
        v, frais = c.melange(a, b, 1.0, c.premieres_seances_annee(idx))
        attendu = 100 * (1 + a.iloc[1:]).cumprod()
        self.assertTrue(np.allclose(v.iloc[1:], attendu))
        self.assertEqual(frais, 0)

    def test_melange_sans_reequilibrage_est_la_somme_des_poches(self):
        idx = jours(200)
        rng = np.random.default_rng(2)
        a = pd.Series(rng.normal(0, 0.01, 200), index=idx)
        b = pd.Series(rng.normal(0, 0.003, 200), index=idx)
        v, _ = c.melange(a, b, 0.6, set())
        a0, b0 = a.copy(), b.copy()
        a0.iloc[0] = b0.iloc[0] = 0
        attendu = 60 * (1 + a0).cumprod() + 40 * (1 + b0).cumprod()
        self.assertTrue(np.allclose(v, attendu))

    def test_melange_frais_egaux_au_montant_echange(self):
        idx = pd.Index(["2000-12-29", "2001-01-02"])
        a = pd.Series([0.0, 0.5], index=idx)
        b = pd.Series([0.0, 0.0], index=idx)
        v, frais = c.melange(a, b, 0.5, {"2001-01-02"}, cout=0.01)
        # 50 -> 75 et 50 : valeur 125, cibles 62,5 et 62,5, échange 25, frais 0,25.
        self.proche(frais, 0.25)
        self.proche(v.iloc[-1], 124.75)

    def test_melange_multiple_egal_au_melange_a_deux(self):
        idx = jours(600)
        rng = np.random.default_rng(6)
        a = pd.Series(rng.normal(0, 0.01, 600), index=idx)
        b = pd.Series(rng.normal(0, 0.003, 600), index=idx)
        annuel = c.premieres_seances_annee(idx)
        deux, frais2 = c.melange(a, b, 0.7, annuel)
        w = pd.Series({"a": 0.7, "b": 0.3})
        plusieurs, frais = c.melange_multiple(pd.DataFrame({"a": a, "b": b}),
                                              {d: w for d in annuel})
        self.assertTrue(np.allclose(deux, plusieurs))
        self.proche(frais, frais2)

    def test_melange_multiple_refuse_des_poids_invalides(self):
        idx = jours(3)
        df = pd.DataFrame({"a": 0.0, "b": 0.0}, index=idx)
        with self.assertRaises(ValueError):
            c.melange_multiple(df, {idx[0]: pd.Series({"a": 0.8, "b": 0.3})})
        with self.assertRaises(ValueError):
            c.melange_multiple(df, {idx[1]: pd.Series({"a": 0.5, "b": 0.5})})

    def test_part_a_risque_egal(self):
        idx = jours(600)
        rng = np.random.default_rng(5)
        s = pd.Series(rng.normal(0.0004, 0.012, 600), index=idx)
        liquide = pd.Series(0.0001, index=idx)
        vol = lambda r: r.std() * np.sqrt(252)
        cible = 0.5 * vol(s)
        p, valeur = c.part_a_risque_egal(s, liquide, c.premieres_seances_annee(idx), cible, vol)
        self.proche(vol(valeur.pct_change().dropna()), cible, rel=1e-5)
        self.assertTrue(0.45 < p < 0.55)

    def test_poids_inverse_volatilite(self):
        idx = jours(300)
        rng = np.random.default_rng(7)
        df = pd.DataFrame({"calme": rng.normal(0, 0.01, 300),
                           "agite": rng.normal(0, 0.03, 300)}, index=idx)
        w = c.poids_inverse_volatilite(df)
        self.proche(w.sum(), 1)
        self.proche(w["calme"], 0.75, abs=0.03)


class FuturTests(CasCouverture):

    def test_beta_n_utilise_pas_l_avenir(self):
        idx = jours(400)
        rng = np.random.default_rng(3)
        m = pd.Series(rng.normal(0, 0.01, 400), index=idx)
        s = 1.5 * m + pd.Series(rng.normal(0, 0.002, 400), index=idx)
        b1 = c.beta_glissant(s, m)
        s2 = s.copy()
        s2.iloc[300:] = 0.2
        b2 = c.beta_glissant(s2, m)
        self.assertTrue(np.allclose(b1.iloc[:301], b2.iloc[:301]))
        self.assertEqual(b1.iloc[10], 1.0)
        self.proche(b1.iloc[-1], 1.5, abs=0.05)

    def test_futur_couvre_entierement_le_marche(self):
        idx = jours(260)
        rng = np.random.default_rng(4)
        rf = pd.Series(0.0001, index=idx)
        m = pd.Series(rng.normal(0.0005, 0.012, 260), index=idx)
        beta = pd.Series(1.0, index=idx)
        # Nominal révisé chaque jour : le portefeuille identique au marché
        # ne gagne que le taux sans risque.
        v, _ = c.couverture_futur(m, m - rf, beta, 1.0, set(idx.astype(str)), set(), cout=0.0)
        r = v.pct_change().dropna()
        self.assertTrue(np.allclose(r, rf.iloc[1:]))

    def test_futur_frais_de_roulement(self):
        idx = jours(3)
        zero = pd.Series(0.0, index=idx)
        v, frais = c.couverture_futur(zero, zero, pd.Series(1.0, index=idx), 1.0,
                                      {idx[1]}, {idx[1]}, cout=0.001)
        # Constitution : 100 échangés. Fin de trimestre : le nominal passe de 100
        # à 99,9, et les 100 en place sont fermés puis rouverts.
        self.proche(frais, 0.1 + 0.001 * (0.1 + 2 * 100))


if __name__ == "__main__":
    unittest.main()
