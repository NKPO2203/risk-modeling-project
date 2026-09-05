"""Cas qui empêchent de confondre croissance, couverture et comparabilité."""
import unittest
import numpy as np
import pandas as pd
from src.corroboration import construire_corroboration, decrire_metrique, niveau_mouvement


def observation(annee, ca=100.0, capex=10.0, rd=2.0, perimetre="activites_poursuivies"):
    ligne = {"cik": "0000000001", "nom": "Exemple", "annee": annee,
             "chiffre_affaires": ca, "capex": capex, "rd": rd,
             "periode_fin": f"{annee}-12-31", "periode_debut": f"{annee}-01-01",
             "periode_id": f"0000000001:{annee}-12-31"}
    for metrique in ("chiffre_affaires", "capex", "rd"):
        ligne.update({f"statut_{metrique}": "observe",
                      f"comparabilite_{metrique}": "comparable",
                      f"{metrique}_perimetre_id": perimetre,
                      f"{metrique}_debut": f"{annee}-01-01",
                      f"{metrique}_fin": f"{annee}-12-31",
                      f"{metrique}_depot": f"depot-{annee}",
                      f"{metrique}_source_url": f"https://exemple.test/{annee}"})
    return ligne


class ComparaisonsTest(unittest.TestCase):
    def test_baisse_observee_avec_depenses_absentes_ne_devient_pas_progression(self):
        self.assertEqual(niveau_mouvement([0.8, np.nan, np.nan]), "recul des mesures disponibles")
        self.assertEqual(niveau_mouvement([np.nan, np.nan]), "non evaluable")

    def test_le_repli_ne_contient_jamais_la_valeur_a_expliquer(self):
        g = pd.DataFrame([observation(2024), observation(2025, ca=300)])
        r = decrire_metrique(g, g.iloc[-1], "chiffre_affaires")
        self.assertTrue(pd.isna(r["multiple"]))
        self.assertEqual(r["base_n"], 1)
        self.assertEqual(r["base_annees"], "2024")

    def test_changement_de_perimetre_n_est_pas_un_recul(self):
        g = pd.DataFrame([observation(2017, ca=500, perimetre="avant_scission"),
                          observation(2018, ca=500, perimetre="avant_scission"),
                          observation(2025, ca=100)])
        r = decrire_metrique(g, g.iloc[-1], "chiffre_affaires")
        self.assertTrue(pd.isna(r["multiple"]))
        self.assertEqual(r["base_n"], 0)

    def test_periodes_distinctes_et_drapeau_pour_chaque_mesure(self):
        g = pd.DataFrame([observation(2017, capex=np.nan), observation(2018, capex=np.nan),
                          observation(2019, capex=np.nan), observation(2021, capex=10),
                          observation(2022, capex=30), observation(2025, ca=200, capex=80)])
        univers = pd.DataFrame([{"cik": "1", "nom": "Exemple"}])
        r, details = construire_corroboration(g, univers)
        self.assertEqual(r.iloc[0]["base_annees_ventes"], "2017;2018;2019")
        self.assertEqual(r.iloc[0]["base_annees_capex"], "2021;2022")
        self.assertEqual(r.iloc[0]["base_repli_utilisee"], "oui")
        self.assertAlmostEqual(r.iloc[0]["mult_capex"], 4.0)
        self.assertEqual(len(details), 3)

    def test_une_entreprise_sans_comptes_reste_dans_le_resultat(self):
        comptes = pd.DataFrame([observation(2025)])
        univers = pd.DataFrame([{"cik": "2", "nom": "Sans données"}])
        r, details = construire_corroboration(comptes, univers)
        self.assertEqual(len(r), 1)
        self.assertEqual(r.iloc[0]["corroboration"], "non evaluable")
        self.assertEqual(len(details), 3)
        self.assertTrue(details.multiple.isna().all())

    def test_univers_vide_conserve_un_schema_exploitable(self):
        comptes = pd.DataFrame([observation(2025)])
        univers = pd.DataFrame(columns=["cik", "nom"])
        r, details = construire_corroboration(comptes, univers)
        self.assertTrue(r.empty)
        self.assertIn("cik", r)
        self.assertIn("multiple", details)

    def test_une_mesure_signalee_n_entre_pas_dans_un_multiple(self):
        g = pd.DataFrame([observation(2017), observation(2018), observation(2025, capex=300)])
        g.loc[g.annee == 2025, "statut_capex"] = "revue_requise"
        r = decrire_metrique(g, g.iloc[-1], "capex")
        self.assertTrue(pd.isna(r["multiple"]))
        self.assertEqual(r["valeur_recente"], 300)

    def test_zero_de_reference_n_est_pas_une_croissance_infinie(self):
        g = pd.DataFrame([observation(2017, capex=0), observation(2018, capex=0),
                          observation(2025, capex=10)])
        r = decrire_metrique(g, g.iloc[-1], "capex")
        self.assertTrue(pd.isna(r["multiple"]))
        self.assertEqual(r["statut_comparaison"], "base_nulle_ou_negative")

    def test_une_baisse_et_un_doublement_peuvent_coexister(self):
        self.assertEqual(niveau_mouvement([0.5, 2.0, np.nan]), "doublement observe")

    def test_exercices_distincts_dans_la_meme_annee_ne_sont_pas_ecrases(self):
        a, b, recent = observation(2022), observation(2023), observation(2025, ca=200)
        b["annee"] = 2022  # étiquette majoritaire identique, clôture distincte
        g = pd.DataFrame([a, b, recent])
        r, details = construire_corroboration(g, pd.DataFrame([{"cik":"1", "nom":"Exemple"}]))
        self.assertEqual(r.iloc[0].mult_ventes, 2.0)
        self.assertEqual(details.iloc[0].base_n, 2)
        self.assertEqual(details.iloc[0].base_annees, "2022;2022")

    def test_reference_qui_chevauche_le_recent_est_exclue(self):
        a, b, recent = observation(2021), observation(2022), observation(2025)
        b["chiffre_affaires_fin"] = "2025-02-01"
        g = pd.DataFrame([a, b, recent])
        r = decrire_metrique(g, g.iloc[-1], "chiffre_affaires")
        self.assertTrue(pd.isna(r["multiple"]))
        self.assertEqual(r["base_n"], 1)

    def test_deux_references_qui_se_chevauchent_ne_donnent_pas_de_multiple(self):
        a, b, recent = observation(2017), observation(2018), observation(2025)
        b["chiffre_affaires_debut"] = "2017-07-01"
        b["chiffre_affaires_fin"] = "2018-06-30"
        b["periode_fin"] = "2018-06-30"
        g = pd.DataFrame([a, b, recent])
        r = decrire_metrique(g, g.iloc[-1], "chiffre_affaires")
        self.assertTrue(pd.isna(r["multiple"]))
        self.assertEqual(r["statut_comparaison"], "references_chevauchantes")


if __name__ == "__main__":
    unittest.main()
