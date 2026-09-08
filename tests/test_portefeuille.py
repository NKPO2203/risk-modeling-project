"""Cas de regression du moteur de portefeuille.

Chaque test reproduit une erreur reellement commise pendant le projet.
Les cas sont decrits et dates dans research/cas_de_test.md.

Aucun test ne lit les fichiers du depot : les donnees sont ecrites a la main
pour que la reponse attendue se verifie de tete.
"""
import unittest

import numpy as np
import pandas as pd

from src.portefeuille import rendements_et_dividendes, poids_cibles, simuler, preparer_prix


def jours(n):
    return [f"2020-01-{j:02d}" for j in range(1, n + 1)]


def prix(closes, volumes=None, dividendes=None):
    n = len(closes)
    return pd.DataFrame({"Close": closes,
                         "Volume": [1000] * n if volumes is None else volumes,
                         "Dividends": [0.0] * n if dividendes is None else dividendes},
                        index=jours(n))


def univers(series, dividendes=None):
    """series : dict titre -> liste de rendements. Renvoie (rendements, detachements)."""
    r = pd.DataFrame(series, index=jours(len(next(iter(series.values())))))
    d = pd.DataFrame({c: [0.0] * len(r) for c in r.columns}, index=r.index)
    if dividendes:
        for c, v in dividendes.items():
            d[c] = v
    return r, d


def cibles_constantes(titres, dates, poids):
    return pd.DataFrame([poids] * len(dates), index=dates, columns=titres)


class RendementsTests(unittest.TestCase):

    def test_cas_1_seance_sans_transaction_ne_donne_ni_zero_ni_saut(self):
        p = prix([10.0, 10.0, 10.0, 100.0], volumes=[0, 0, 0, 5000])
        r, _ = rendements_et_dividendes(p)
        self.assertTrue(r.isna().all(),
                        "une seance a volume nul n'est pas une observation")

    def test_cas_2_valeur_absente_contamine_le_lendemain(self):
        p = prix([10.0, np.nan, 11.0, 12.0])
        r, _ = rendements_et_dividendes(p)
        self.assertTrue(pd.isna(r.iloc[1]))
        self.assertTrue(pd.isna(r.iloc[2]), "le rendement du jour a besoin de la veille")
        self.assertAlmostEqual(r.iloc[3], 12 / 11 - 1)

    def test_cas_3_division_retraitee_ne_produit_aucun_saut(self):
        p = prix([50.0, 51.0, 52.0])
        r, _ = rendements_et_dividendes(p)
        self.assertLess(r.dropna().abs().max(), 0.05,
                        "une division retraitee ne doit pas creer de rendement aberrant")

    def test_cas_4_dividende_en_especes_dans_le_moteur(self):
        p = prix([100.0, 95.0], dividendes=[0.0, 10.0])
        r, d = rendements_et_dividendes(p)
        r.iloc[0], d.iloc[0] = 0, 0
        cible = pd.DataFrame({"A": [1.]}, index=[p.index[0]])
        v, _, _ = simuler(r.to_frame("A"), d.to_frame("A"), ["A"], cible,
                          p.index, set(cible.index), False, cout=0)
        self.assertAlmostEqual(v.iloc[-1], 1.05, places=12)
        self.assertNotAlmostEqual(v.iloc[-1], 95 / 90, places=3)


class PoidsTests(unittest.TestCase):

    membres = pd.DataFrame({"entreprise": ["Alpha", "Alpha", "Beta", "Gamma"],
                            "titre": ["A1", "A2", "B", "G"]})

    def test_cas_10_deux_classes_ne_doublent_pas_l_entreprise(self):
        w = poids_cibles(self.membres, ["A1", "A2", "B", "G"])
        self.assertAlmostEqual(w["A1"] + w["A2"], 1 / 3, places=12)
        self.assertAlmostEqual(w["A1"], w["A2"])
        self.assertAlmostEqual(sum(w.values()), 1.0, places=12)

    def test_cas_10_bis_une_seule_classe_cotee_prend_tout_le_poids(self):
        w = poids_cibles(self.membres, ["A1", "B", "G"])
        self.assertAlmostEqual(w["A1"], 1 / 3, places=12)
        self.assertNotIn("A2", w)


class SimulationTests(unittest.TestCase):

    def moteur(self, series, reequilibrer, poids, dividendes=None, cout=0.0):
        r, d = univers(series, dividendes)
        titres = list(series)
        dates = list(r.index)
        cibles = cibles_constantes(titres, [dates[0]], poids)
        return simuler(r, d, titres, cibles, dates, {dates[0]}, reequilibrer,
                       cout, fins_de_mois=set(dates))

    def test_cas_5_la_tresorerie_dort_puis_est_reinvestie(self):
        # le detachement fait baisser le cours d'autant : un dividende de 10 %
        # du cours de la veille s'accompagne d'un rendement de prix de -10 %.
        r, d = univers({"A": [0.0, -0.10, 0.0], "B": [0.0, 0.0, 0.0]},
                       dividendes={"A": [0.0, 0.10, 0.0]})
        dates = list(r.index)
        cibles = cibles_constantes(["A", "B"], [dates[0]], [0.5, 0.5])
        _, _, photos = simuler(r, d, ["A", "B"], cibles, dates, {dates[0]},
                               reequilibrer=True, cout=0.0, fins_de_mois=set(dates))
        tresorerie = photos["_tresorerie"]
        self.assertAlmostEqual(tresorerie.iloc[0], 0.0, places=12)
        self.assertAlmostEqual(tresorerie.iloc[1], 0.05, places=12)
        self.assertAlmostEqual(tresorerie.iloc[2], 0.05, places=12,
                               msg="la tresorerie ne rapporte rien entre deux janviers")

    def test_cas_6_la_somme_des_poids_vaut_un_apres_derive(self):
        _, _, photos = self.moteur({"A": [0.0, 0.50, 0.10], "B": [0.0, -0.30, 0.20]},
                                   reequilibrer=True, poids=[0.5, 0.5])
        self.assertTrue(np.allclose(photos.sum(axis=1), 1.0, atol=1e-12))

    def test_cas_7_l_entrant_ne_change_pas_la_valeur_totale(self):
        r, d = univers({"A": [0.0, 0.0], "B": [0.0, 0.0], "C": [np.nan, 0.0]})
        dates = list(r.index)
        cibles = pd.DataFrame([[0.5, 0.5, 0.0], [1 / 3, 1 / 3, 1 / 3]],
                              index=dates, columns=["A", "B", "C"])
        valeurs, _, photos = simuler(r, d, ["A", "B", "C"], cibles, dates, set(dates),
                                     reequilibrer=False, cout=0.0, fins_de_mois=set(dates))
        self.assertAlmostEqual(valeurs.iloc[1], valeurs.iloc[0], places=12,
                               msg="l'entree d'un titre est financee par les autres")
        self.assertAlmostEqual(photos["C"].iloc[1], 1 / 3, places=12)

    def test_cas_7_bis_aucun_poids_avant_la_premiere_cotation(self):
        r, d = univers({"A": [0.0, 0.0], "C": [np.nan, 0.0]})
        dates = list(r.index)
        cibles = pd.DataFrame([[1.0, 0.0], [0.5, 0.5]], index=dates, columns=["A", "C"])
        _, _, photos = simuler(r, d, ["A", "C"], cibles, dates, set(dates),
                               reequilibrer=False, cout=0.0, fins_de_mois=set(dates))
        self.assertAlmostEqual(photos["C"].iloc[0], 0.0, places=12)

    def test_cas_8_le_rendement_reste_encadre_par_ses_titres(self):
        valeurs, _, _ = self.moteur({"A": [0.0, 0.20, -0.10], "B": [0.0, 0.05, 0.30]},
                                    reequilibrer=True, poids=[0.5, 0.5])
        rendement = valeurs.pct_change()
        self.assertGreaterEqual(rendement.iloc[1], 0.05 - 1e-12)
        self.assertLessEqual(rendement.iloc[1], 0.20 + 1e-12)
        self.assertGreaterEqual(rendement.iloc[2], -0.10 - 1e-12)
        self.assertLessEqual(rendement.iloc[2], 0.30 + 1e-12)

    def test_cas_9_les_moities_reconstituent_le_tout(self):
        series = {"A": [0.0, 0.30, -0.10], "B": [0.0, -0.20, 0.05],
                  "C": [0.0, 0.10, 0.15], "D": [0.0, 0.00, -0.05]}
        r, d = univers(series)
        dates = list(r.index)

        def valeur(titres):
            n = len(titres)
            cibles = cibles_constantes(titres, [dates[0]], [1 / n] * n)
            v, _, _ = simuler(r, d, titres, cibles, dates, {dates[0]},
                              reequilibrer=True, cout=0.0)
            return v / v.iloc[0]

        tout = valeur(["A", "B", "C", "D"])
        melange = 0.5 * valeur(["A", "B"]) + 0.5 * valeur(["C", "D"])
        self.assertTrue(np.allclose(tout, melange, atol=1e-12),
                        "le melange des moities doit reproduire le tout")


if __name__ == "__main__":
    unittest.main()
