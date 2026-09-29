"""Cas de contrôle des règles de la seconde version des étapes 4 et 5 (src/regles.py)."""
import unittest

import numpy as np
import pandas as pd

from src import couverture, regles, risque


def jours(n, debut="2010-01-04"):
    return pd.Index(pd.bdate_range(debut, periods=n).strftime("%Y-%m-%d"), name="date")


class CasRegles(unittest.TestCase):

    def test_ledoit_wolf(self):
        rng = np.random.default_rng(1)
        X = rng.normal(0, 0.01, (60, 40))
        cov, intensite = regles.ledoit_wolf(X)
        self.assertTrue(0 <= intensite <= 1)
        self.assertTrue(np.allclose(cov, cov.T))
        self.assertGreater(np.linalg.eigvalsh(cov).min(), 0)
        # Avec beaucoup d'observations et peu de titres, le rétrécissement devient faible.
        _, faible = regles.ledoit_wolf(rng.normal(0, 0.01, (20000, 3)) @ np.diag([1, 2, 3]))
        self.assertLess(faible, 0.01)
        # Formule rapide égale à la définition.
        Xc = X - X.mean(0)
        S = Xc.T @ Xc / len(X)
        direct = sum(((np.outer(x, x) - S) ** 2).sum() for x in Xc) / len(X) ** 2
        rapide = ((Xc ** 2).sum(1) ** 2).sum() / len(X) ** 2 - (S ** 2).sum() / len(X)
        self.assertAlmostEqual(direct, rapide, places=18)

    def test_contributions_egales(self):
        rng = np.random.default_rng(2)
        A = rng.normal(size=(6, 6))
        cov = A @ A.T + 6 * np.eye(6)
        w = regles.contributions_egales(cov)
        contributions, vol = risque.contributions_au_risque(w, cov)
        self.assertTrue(np.allclose(contributions, vol / 6, rtol=1e-8))

    def test_variance_minimale(self):
        cov = np.array([[0.04, 0.0], [0.0, 0.01]])
        w = regles.variance_minimale(cov, 1.0)
        self.assertTrue(np.allclose(w, [0.2, 0.8], atol=1e-8))
        w = regles.variance_minimale(cov, 0.7)
        self.assertTrue(np.allclose(w, [0.3, 0.7], atol=1e-8))
        with self.assertRaises(ValueError):
            regles.variance_minimale(cov, 0.4)

    def test_ponderation_par_groupes(self):
        rng = np.random.default_rng(3)
        passe = pd.DataFrame(rng.normal(0, 0.01, (300, 4)) * [1, 1, 3, 3], columns=list("abcd"))
        groupe = {"a": "calme", "b": "calme", "c": "agite", "d": "agite"}
        w = regles.ponderer("W3", passe, list("abcd"), groupe, {t: t for t in "abcd"})
        self.assertAlmostEqual(w.sum(), 1)
        self.assertAlmostEqual(w["a"], w["b"])
        self.assertGreater(w["a"], w["c"])
        w1 = regles.ponderer("W1", passe, ["a", "c", "d"], groupe, {"a": "x", "c": "y", "d": "y"})
        self.assertTrue(np.allclose(w1[["a", "c", "d"]], [0.5, 0.25, 0.25]))

    def test_simuler_egal_au_melange_multiple(self):
        idx = jours(600)
        rng = np.random.default_rng(4)
        R = pd.DataFrame(rng.normal(0, 0.01, (600, 3)), index=idx, columns=list("abc"))
        dates = couverture.premieres_seances_annee(idx)
        cibles = {d: pd.Series({"a": 0.5, "b": 0.3, "c": 0.2}) for d in dates}
        v1, f1 = regles.simuler(R, cibles)
        v2, f2 = couverture.melange_multiple(R, cibles)
        self.assertTrue(np.allclose(v1, v2) and np.isclose(f1, f2))

    def test_exposition_n_utilise_pas_l_avenir(self):
        idx = jours(300)
        rng = np.random.default_rng(5)
        r = pd.Series(rng.normal(0, 0.02, 300), index=idx)
        fins = couverture.fins_de_mois(idx)
        s1 = regles.exposition_pilotee(r, 0.15, 21, fins)
        r2 = r.copy()
        r2.iloc[200:] *= 5
        s2 = regles.exposition_pilotee(r2, 0.15, 21, fins)
        self.assertTrue(np.allclose(s1.iloc[:201], s2.iloc[:201]))
        self.assertLessEqual(s1.max(), 1.0)

    def test_sharpe_deflate(self):
        p, sr0 = regles.sharpe_deflate(0.1, 0.0004, 100, 1000, 0.0, 3.0)
        milieu, _ = regles.sharpe_deflate(sr0, 0.0004, 100, 1000, 0.0, 3.0)
        self.assertAlmostEqual(milieu, 0.5)
        self.assertGreater(p, 0.5)

    def test_probabilite_de_surapprentissage(self):
        rng = np.random.default_rng(6)
        bruit = rng.normal(0, 0.01, (1600, 20))
        pbo, _ = regles.probabilite_surapprentissage(bruit, blocs=8)
        self.assertGreater(pbo, 0.3)
        bruit[:, 0] += 0.01
        pbo, _ = regles.probabilite_surapprentissage(bruit, blocs=8)
        self.assertLess(pbo, 0.05)

    def test_christoffersen(self):
        independants = np.zeros(1000, int)
        independants[::100] = 1
        groupes = np.zeros(1000, int)
        groupes[500:510] = 1
        self.assertLess(regles.christoffersen(independants), 1)
        self.assertGreater(regles.christoffersen(groupes), 20)

    def test_fondamentaux_au_depot_et_premiere_publication(self):
        f = pd.DataFrame([
            ("1", "Assets", "", "2019-12-31", 100.0, "2020-02-15"),
            ("1", "Assets", "", "2020-12-31", 120.0, "2021-02-15"),
            ("1", "Assets", "", "2019-12-31", 999.0, "2021-02-15"),
            ("1", "NetIncomeLoss", "2020-01-01", "2020-12-31", 12.0, "2021-02-15"),
        ], columns=["cik", "etiquette", "debut", "fin", "valeur", "depose_le"])
        f["taxonomie"] = "us-gaap"
        avant = regles.fondamentaux_a_date(f, "2021-02-15")
        self.assertEqual(avant.loc["1", "fin_exercice"], "2019-12-31")
        apres = regles.fondamentaux_a_date(f, "2021-02-16")
        self.assertEqual(apres.loc["1", "actif"], 120.0)
        self.assertEqual(apres.loc["1", "actif_precedent"], 100.0)
        self.assertEqual(apres.loc["1", "benefice"], 12.0)

    def test_selections(self):
        notes = pd.Series({"a": 0.9, "b": 0.1, "c": 0.5, "d": 0.8, "e": 0.2})
        groupe = {"a": 1, "b": 1, "c": 1, "d": 2, "e": 2}
        self.assertEqual(sorted(regles.selectionner("S1", notes, groupe)), ["a", "c", "d"])
        self.assertEqual(sorted(regles.selectionner("S2", notes, groupe)), ["a", "d"])
        self.assertEqual(sorted(regles.selectionner("S3", notes, groupe)), ["a", "c", "d"])

    def test_portefeuilles_aleatoires(self):
        idx = jours(520)
        R = pd.DataFrame(0.001, index=idx, columns=[f"t{i}" for i in range(12)])
        eligibles = {d: list(R.columns) for d in couverture.premieres_seances_annee(idx)}
        m = regles.portefeuilles_aleatoires(R, eligibles, 50, 0, pd.Series(0.0, index=idx), cout=0.0)
        self.assertTrue(np.allclose(m.annualise, 1.001 ** 252 - 1))
        self.assertTrue(((m.taille >= 10) & (m.taille <= 12)).all())


if __name__ == "__main__":
    unittest.main()
