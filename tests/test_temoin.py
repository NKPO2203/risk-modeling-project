"""Règles propres au groupe témoin, sur des données écrites à la main."""
import unittest

import numpy as np
import pandas as pd

from src.construire_temoin import completer_seances, membres_temoin, ponderation_sectorielle


class TemoinTests(unittest.TestCase):

    groupe = pd.DataFrame({
        "titre": ["A", "B", "C", "D1", "D2"],
        "cik": ["1", "2", "3", "4", "4"],
        "secteur": ["Tech", "Tech", "Energie", "Finance", "Finance"]})

    def test_les_parts_sectorielles_du_theme_sont_reproduites(self):
        parts = pd.Series({"Tech": 0.6, "Energie": 0.3, "Finance": 0.1})
        w = ponderation_sectorielle(parts)(self.groupe, list(self.groupe.titre))
        self.assertAlmostEqual(sum(w.values()), 1.0, places=12)
        self.assertAlmostEqual(w["A"] + w["B"], 0.6, places=12)
        self.assertAlmostEqual(w["C"], 0.3, places=12)
        # deux classes d'une même entreprise se partagent sa part
        self.assertAlmostEqual(w["D1"], 0.05, places=12)

    def test_un_secteur_absent_est_redistribue_proportionnellement(self):
        parts = pd.Series({"Tech": 0.6, "Energie": 0.3, "Finance": 0.1})
        w = ponderation_sectorielle(parts)(self.groupe, ["A", "B", "D1", "D2"])
        self.assertAlmostEqual(w["A"] + w["B"], 0.6 / 0.7, places=12)
        self.assertNotIn("C", w)

    def test_une_seance_absente_devient_un_cours_manquant_sans_dividende(self):
        dates = pd.Index(["2020-01-02", "2020-01-03", "2020-01-06"])
        prix = pd.DataFrame({"Close": [10.0, 11.0], "Volume": [5.0, 5.0], "Dividends": [0.0, 0.0],
                             "Open": [10.0, 11.0], "High": [10.0, 11.0], "Low": [10.0, 11.0]},
                            index=pd.Index(["2020-01-02", "2020-01-06"]))
        complet, n = completer_seances(prix, dates)
        self.assertEqual(n, 1)
        self.assertTrue(np.isnan(complet.loc["2020-01-03", "Close"]))
        self.assertEqual(complet.loc["2020-01-03", "Dividends"], 0.0)

    def test_seules_les_entreprises_sort_forment_le_temoin(self):
        decisions = pd.DataFrame({"verdict": ["SORT", "ENTRE", "SORT"], "nom": ["X", "Y", "Z"],
                                  "cik": ["1", "2", "3"], "symboles": ["X", "Y", "Z.A|Z.B"],
                                  "secteur": ["S", "S", "S"]})
        m = membres_temoin(decisions)
        self.assertEqual(sorted(m.titre), ["X", "Z-A", "Z-B"])


if __name__ == "__main__":
    unittest.main()
