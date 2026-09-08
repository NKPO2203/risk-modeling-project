"""Cas de regression des mesures de risque de l'etape 3.

Chaque test porte sur une donnee ecrite a la main dont la reponse se verifie
de tete, ou sur une identite mathematique qui doit tenir exactement.
Aucun test ne lit les fichiers du depot.
"""
import unittest

import numpy as np
import pandas as pd

from src.risque import (annualiser_rendement, contributions_au_risque, drawdown,
                        episodes_de_tension, herfindahl, kupiec, n_effectif,
                        perte_au_dela, rho_implicite, sharpe, sortino,
                        var_historique, volatilite, volatilite_baisse)


def jours(n):
    return pd.date_range("2020-01-01", periods=n, freq="D").strftime("%Y-%m-%d")


class RendementTests(unittest.TestCase):

    def test_annualisation_geometrique_et_non_arithmetique(self):
        # -50 % puis +50 % laisse 75 % du capital, pas 100 %
        niveau = pd.Series([100.0, 50.0, 75.0], index=jours(3))
        r = niveau.pct_change().dropna()
        self.assertAlmostEqual(r.mean(), 0.0, places=12)
        self.assertLess(annualiser_rendement(niveau, periodes=3), 0)

    def test_annualisation_refuse_une_serie_trop_courte(self):
        with self.assertRaises(ValueError):
            annualiser_rendement(pd.Series([100.0], index=jours(1)))


class VolatiliteTests(unittest.TestCase):

    def test_serie_constante_a_une_volatilite_nulle(self):
        r = pd.Series([0.0] * 10, index=jours(10))
        self.assertAlmostEqual(volatilite(r), 0.0, places=12)

    def test_annualisation_par_racine_du_nombre_de_seances(self):
        r = pd.Series([0.01, -0.01] * 200, index=jours(400))
        self.assertAlmostEqual(volatilite(r), r.std() * np.sqrt(252), places=12)

    def test_volatilite_baisse_nulle_si_tout_est_positif(self):
        e = pd.Series([0.01, 0.02, 0.03], index=jours(3))
        self.assertAlmostEqual(volatilite_baisse(e), 0.0, places=12)

    def test_convention_sortino_et_non_ecart_type_des_negatifs(self):
        # trois jours positifs, un seul a -2 % : la convention de Sortino divise
        # par quatre, l'ecart-type des negatifs seuls diviserait par un
        e = pd.Series([0.01, 0.01, 0.01, -0.02], index=jours(4))
        attendu = np.sqrt((0.02 ** 2) / 4) * np.sqrt(252)
        self.assertAlmostEqual(volatilite_baisse(e), attendu, places=12)
        self.assertLess(volatilite_baisse(e), 0.02 * np.sqrt(252))


class RatiosTests(unittest.TestCase):

    def test_sharpe_nul_quand_le_rendement_egale_le_taux_sans_risque(self):
        r = pd.Series([0.001] * 100, index=jours(100))
        rf = pd.Series([0.001] * 100, index=jours(100))
        r = r + pd.Series([0.01, -0.01] * 50, index=jours(100))
        self.assertAlmostEqual(sharpe(r, rf), 0.0, places=10)

    def test_sortino_depasse_sharpe_quand_les_baisses_sont_rares(self):
        valeurs = [0.01] * 90 + [-0.05] * 10
        r = pd.Series(valeurs, index=jours(100))
        rf = pd.Series([0.0] * 100, index=jours(100))
        self.assertGreater(sortino(r, rf), sharpe(r, rf))


class DrawdownTests(unittest.TestCase):

    def test_repli_de_moitie_puis_retour(self):
        niveau = pd.Series([100.0, 50.0, 80.0, 100.0, 110.0], index=jours(5))
        d = drawdown(niveau)
        self.assertAlmostEqual(d["repli_max"], -0.5, places=12)
        self.assertEqual(d["chute"], 1)
        self.assertEqual(d["recuperation"], 2)

    def test_repli_jamais_rattrape(self):
        niveau = pd.Series([100.0, 50.0, 60.0], index=jours(3))
        d = drawdown(niveau)
        self.assertIsNone(d["retour"])
        self.assertIsNone(d["recuperation"])

    def test_serie_croissante_ne_passe_jamais_sous_l_eau(self):
        niveau = pd.Series([1.0, 2.0, 3.0, 4.0], index=jours(4))
        self.assertAlmostEqual(drawdown(niveau)["part_sous_l_eau"], 0.0, places=12)


class VarTests(unittest.TestCase):

    def test_var_exprimee_en_perte_positive(self):
        r = pd.Series(np.linspace(-0.10, 0.10, 101), index=jours(101))
        self.assertGreater(var_historique(r, 0.95), 0)

    def test_perte_au_dela_toujours_superieure_ou_egale_a_la_var(self):
        alea = np.random.default_rng(0).standard_normal(2000) / 100
        r = pd.Series(alea, index=jours(2000))
        for seuil in (0.90, 0.95, 0.99):
            self.assertGreaterEqual(perte_au_dela(r, seuil), var_historique(r, seuil))

    def test_seuil_hors_bornes_refuse(self):
        r = pd.Series([0.0, 0.1], index=jours(2))
        with self.assertRaises(ValueError):
            var_historique(r, 1.5)


class KupiecTests(unittest.TestCase):

    def test_statistique_nulle_quand_la_couverture_est_exacte(self):
        self.assertAlmostEqual(kupiec(1000, 50, 0.05), 0.0, places=9)

    def test_stabilite_numerique_sur_un_grand_echantillon(self):
        # (1-p)**(n-x) vaut zero pour la machine des cette taille ; le calcul
        # en logarithmes doit rester fini
        valeur = kupiec(6456, 108, 0.01)
        self.assertTrue(np.isfinite(valeur))
        self.assertGreater(valeur, 3.84)

    def test_aucun_depassement_ne_donne_pas_de_statistique(self):
        self.assertTrue(np.isnan(kupiec(1000, 0, 0.05)))


class DecompositionTests(unittest.TestCase):

    def test_n_effectif_vaut_n_quand_les_titres_sont_independants(self):
        self.assertAlmostEqual(n_effectif(0.0, 25), 25.0, places=12)

    def test_n_effectif_vaut_un_quand_tout_bouge_ensemble(self):
        self.assertAlmostEqual(n_effectif(1.0, 135), 1.0, places=12)

    def test_n_effectif_plafonne_par_l_inverse_de_la_correlation(self):
        # avec rho = 0,338, aucun nombre de titres ne depasse 1/rho
        self.assertLess(n_effectif(0.338, 10_000), 1 / 0.338)

    def test_rho_implicite_retrouve_zero_sur_des_series_independantes(self):
        alea = np.random.default_rng(1).standard_normal((4000, 30)) / 100
        bloc = pd.DataFrame(alea, index=jours(4000))
        self.assertAlmostEqual(rho_implicite(bloc), 0.0, places=1)

    def test_rho_implicite_retrouve_un_sur_des_series_identiques(self):
        base = np.random.default_rng(2).standard_normal(2000) / 100
        bloc = pd.DataFrame({c: base for c in range(10)}, index=jours(2000))
        self.assertAlmostEqual(rho_implicite(bloc), 1.0, places=6)


class ContributionsTests(unittest.TestCase):

    covariance = np.array([[0.04, 0.01, 0.00],
                           [0.01, 0.09, 0.02],
                           [0.00, 0.02, 0.16]])

    def test_les_contributions_somment_a_la_volatilite(self):
        poids = np.array([0.5, 0.3, 0.2])
        contributions, vol = contributions_au_risque(poids, self.covariance)
        self.assertAlmostEqual(contributions.sum(), vol, places=12)

    def test_poids_qui_ne_somment_pas_a_un_refuses(self):
        with self.assertRaises(ValueError):
            contributions_au_risque(np.array([0.5, 0.3, 0.1]), self.covariance)

    def test_le_risque_peut_etre_plus_concentre_que_les_poids(self):
        poids = np.array([1 / 3, 1 / 3, 1 / 3])
        contributions, vol = contributions_au_risque(poids, self.covariance)
        parts = contributions / vol
        self.assertGreater(herfindahl(parts), herfindahl(poids))


class EpisodesTests(unittest.TestCase):

    def test_un_repli_de_vingt_pour_cent_est_detecte(self):
        niveau = pd.Series([100.0, 90.0, 80.0, 95.0, 105.0], index=jours(5))
        e = episodes_de_tension(niveau, 0.15)
        self.assertEqual(len(e), 1)
        self.assertAlmostEqual(e.repli.iloc[0], -0.2, places=12)
        self.assertEqual(e.debut.iloc[0], niveau.index[0])
        self.assertEqual(e.creux.iloc[0], niveau.index[2])

    def test_un_repli_trop_faible_est_ignore(self):
        niveau = pd.Series([100.0, 95.0, 98.0, 105.0], index=jours(4))
        self.assertEqual(len(episodes_de_tension(niveau, 0.15)), 0)

    def test_la_regle_ne_regarde_pas_l_avenir(self):
        # tronquer la serie apres le creux ne doit pas changer l'episode detecte
        niveau = pd.Series([100.0, 90.0, 80.0, 95.0, 105.0], index=jours(5))
        complet = episodes_de_tension(niveau, 0.15)
        tronque = episodes_de_tension(niveau.iloc[:3], 0.15)
        self.assertEqual(complet.creux.iloc[0], tronque.creux.iloc[0])
        self.assertAlmostEqual(complet.repli.iloc[0], tronque.repli.iloc[0], places=12)


if __name__ == "__main__":
    unittest.main()
