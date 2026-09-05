"""Regressions de selection sur donnees synthetiques, sans lecture/ecriture CSV.

Execution : python -B tests/test_classification.py
"""
import importlib.util
from pathlib import Path
import unittest

import pandas as pd
from pandas.testing import assert_frame_equal


RACINE = Path(__file__).resolve().parents[1]


def charger_module(nom, fichier):
    spec = importlib.util.spec_from_file_location(nom, RACINE / "src" / fichier)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


selection = charger_module("selection_sous_test", "classification_manuelle.py")
classement = charger_module("classement_sous_test", "build_text_ranking.py")


class TestClassification(unittest.TestCase):
    def setUp(self):
        self.cik_a, self.cik_b = "0000000001", "0000000002"
        self.depot_a, self.depot_b = "0000000001-26-000001", "0000000002-26-000001"
        self.url_a = "https://www.sec.gov/Archives/edgar/data/1/000000000126000001/a.htm"
        self.url_b = "https://www.sec.gov/Archives/edgar/data/2/000000000226000001/b.htm"
        self.rangs = pd.DataFrame([
            {"cik": self.cik_a, "rang": 1, "nom": "Societe A", "depot": self.depot_a, "source_url": self.url_a},
            {"cik": self.cik_b, "rang": 2, "nom": "Societe B", "depot": self.depot_b, "source_url": self.url_b},
        ])
        self.termes = self.rangs[["cik", "depot", "source_url"]].copy()
        self.decisions = pd.DataFrame([
            self.decision(self.cik_a, self.depot_a, self.url_a, "ENTRE", "We sell AI servers.", "Vente documentee"),
            self.decision(self.cik_b, self.depot_b, self.url_b, "DOUTEUX", "We may develop cooling equipment.", "Projet encore prospectif"),
        ])
        self.phrases = pd.DataFrame([
            {"cik": self.cik_a, "depot": self.depot_a, "phrase": "Context. We sell AI servers. Further context."},
            {"cik": self.cik_b, "depot": self.depot_b, "phrase": "We may develop cooling equipment."},
        ])

    @staticmethod
    def decision(cik, depot, url, verdict, citation, motif):
        row = {champ: "" for champ in selection.CHAMPS_REGISTRE}
        row.update(cik=cik, depot=depot, source_url=url, verdict=verdict,
                   phrase_decisive=citation, motif=motif, revue_le="2026-09-05")
        return row

    def appliquer(self, decisions=None, phrases=None, rangs=None, termes=None, textes=None):
        return selection.appliquer_decisions(
            self.rangs if rangs is None else rangs,
            self.decisions if decisions is None else decisions,
            self.phrases if phrases is None else phrases,
            self.termes if termes is None else termes,
            textes=textes,
        ).set_index("cik")

    def assert_a_examiner(self, resultat):
        self.assertEqual(resultat.loc[self.cik_a, "verdict"], "A_EXAMINER")
        self.assertEqual(resultat.loc[self.cik_a, "verdict_registre"], "ENTRE")
        self.assertEqual(resultat.loc[self.cik_a, "preuve_verifiee"], "non")

    def test_changer_rangs_et_ordre_ne_deplace_pas_les_decisions(self):
        rangs = self.rangs.iloc[::-1].copy()
        rangs["rang"] = [7, 400]
        resultat = self.appliquer(rangs=rangs, decisions=self.decisions.iloc[::-1])
        self.assertEqual(resultat["verdict"].to_dict(), {self.cik_b: "DOUTEUX", self.cik_a: "ENTRE"})
        self.assertEqual(resultat.loc[self.cik_a, "motif"], "Vente documentee")
        self.assertEqual(resultat.loc[self.cik_b, "motif"], "Projet encore prospectif")
        self.assertEqual(resultat["rang"].tolist(), [7, 400])

    def test_sans_decision_ne_devient_pas_sort(self):
        resultat = self.appliquer(decisions=self.decisions.iloc[1:])
        self.assertEqual(resultat.loc[self.cik_a, "verdict"], "A_EXAMINER")
        self.assertEqual(resultat.loc[self.cik_a, "verdict_registre"], "")
        self.assertEqual(resultat.loc[self.cik_b, "verdict"], "DOUTEUX")

    def test_registre_vide_conserve_tout_univers_a_examiner(self):
        resultat = self.appliquer(decisions=self.decisions.iloc[:0])
        self.assertEqual(set(resultat.index), {self.cik_a, self.cik_b})
        self.assertEqual(set(resultat["verdict"]), {"A_EXAMINER"})

    def test_citation_inventee_invalide_la_sortie_et_preserve_le_jugement(self):
        decisions = self.decisions.copy()
        decisions.loc[0, "phrase_decisive"] = "We supply imaginary products."
        self.assert_a_examiner(self.appliquer(decisions=decisions))

    def test_une_url_different_du_depot_invalide_la_preuve(self):
        decisions = self.decisions.copy()
        decisions.loc[0, "source_url"] = "https://example.org/another-report"
        self.assert_a_examiner(self.appliquer(decisions=decisions))

    def test_index_sec_du_meme_depot_est_admis(self):
        decisions = self.decisions.copy()
        decisions.loc[0, "source_url"] = self.url_a.rsplit("/", 1)[0] + "/" + self.depot_a + "-index.html"
        resultat = self.appliquer(decisions=decisions)
        self.assertEqual(resultat.loc[self.cik_a, "verdict"], "ENTRE")
        self.assertEqual(resultat.loc[self.cik_a, "preuve_verifiee"], "oui")

    def test_citation_dune_autre_societe_ne_valide_pas_le_cik(self):
        phrases = self.phrases.copy()
        phrases.loc[0, "cik"] = self.cik_b
        self.assert_a_examiner(self.appliquer(phrases=phrases))

    def test_citation_dun_autre_depot_ne_valide_pas_la_preuve(self):
        phrases = self.phrases.copy()
        phrases.loc[0, "depot"] = self.depot_b
        self.assert_a_examiner(self.appliquer(phrases=phrases))

    def test_citation_fragmentee_retrouvee_dans_texte_integral(self):
        textes = {(self.cik_a, self.depot_a): "More context. We\n sell\tAI\u00a0servers. End."}
        resultat = self.appliquer(phrases=self.phrases.iloc[1:], textes=textes)
        self.assertEqual(resultat.loc[self.cik_a, "verdict"], "ENTRE")
        self.assertEqual(resultat.loc[self.cik_a, "support_verification"], "texte_complet_sha256")

    def test_normalisation_des_espaces_naccepte_pas_une_reformulation(self):
        textes = {(self.cik_a, self.depot_a): "We provide artificial intelligence servers."}
        self.assert_a_examiner(self.appliquer(phrases=self.phrases.iloc[1:], textes=textes))

    def test_doublons_cik_refuses_dans_les_tables_de_reference(self):
        for nom, table in (("rangs", self.rangs), ("decisions", self.decisions), ("termes", self.termes)):
            with self.subTest(table=nom):
                with self.assertRaises(ValueError):
                    self.appliquer(**{nom: pd.concat([table, table.iloc[:1]], ignore_index=True)})

    def test_application_ne_modifie_aucune_entree(self):
        tables = [self.rangs, self.decisions, self.phrases, self.termes]
        avant = [table.copy(deep=True) for table in tables]
        self.appliquer()
        for originale, copie in zip(tables, avant):
            assert_frame_equal(originale, copie)


class TestClassementDocumentaire(unittest.TestCase):
    @staticmethod
    def univers(nombre):
        return pd.DataFrame([{"cik": str(i).zfill(10), "nom": f"Societe {i}"} for i in range(1, nombre + 1)])

    @staticmethod
    def rapport(cik, taille=1000, **comptes):
        return {"cik": str(cik).zfill(10), "taille_texte": taille,
                **{terme: comptes.get(terme, 0) for terme in classement.TERMES}}

    def test_sans_occurrence_et_sans_rapport_restent_dans_univers(self):
        termes = pd.DataFrame([
            self.rapport(1, intelligence_artificielle=3),
            self.rapport(2),
            self.rapport(3, taille=0),
            # CIK 4 n'a meme pas de ligne de rapport.
        ])
        resultat = classement.construire_classement(self.univers(4), termes).set_index("cik")
        self.assertEqual(len(resultat), 4)
        self.assertEqual(resultat.loc["0000000002", "rapport_disponible"], "oui")
        self.assertEqual(resultat.loc["0000000002", "total"], 0)
        for cik in ("0000000003", "0000000004"):
            self.assertEqual(resultat.loc[cik, "rapport_disponible"], "non")
            self.assertTrue(pd.isna(resultat.loc[cik, "total"]))
        self.assertEqual(resultat["rang"].tolist(), [1, 2, 3, 4])

    def test_classement_reproductible_et_priorites_explicites(self):
        termes = pd.DataFrame([
            self.rapport(1, intelligence_artificielle=20),
            self.rapport(2, intelligence_artificielle=1, centre_de_donnees=1),
            self.rapport(3, taille=1000, intelligence_artificielle=2),
            self.rapport(4, taille=2000, intelligence_artificielle=2),
            self.rapport(5, taille=2000, intelligence_artificielle=2),
        ])
        entreprises = self.univers(5)
        premier = classement.construire_classement(entreprises, termes)
        second = classement.construire_classement(entreprises.iloc[::-1], termes.iloc[::-1])
        assert_frame_equal(premier, second)
        self.assertEqual(premier["cik"].tolist(), ["0000000002", "0000000001", "0000000003", "0000000004", "0000000005"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
