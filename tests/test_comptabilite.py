"""Cas de régression ayant une conséquence sur les comparaisons économiques."""
import unittest
import pandas as pd
from src.build_screening_base import construire_base, annee_majoritaire, charger_registre
from src.fetch_sec_financials import extraire_valeurs_annuelles, choisir_par_exercice
from src.controle_qualite import controler_base


def valeur(metric='chiffre_affaires', tag='Revenues', value=100, year=2025,
           cik='0000000001', **extra):
    return dict(cik=cik, nom='Exemple', symboles='EX', secteur='Industrials', sous_secteur='Exemple',
                notion=metric, etiquette=tag, rang_preference=0, annee=year,
                debut=f'{year}-01-01', fin=f'{year}-12-31', valeur=value,
                depot='0000000001-26-000001', depose_le='2026-02-01', **extra)


class ComptabiliteTests(unittest.TestCase):
    def test_nvda_equivalence_documentee_retablit_reference_sans_changer_montants(self):
        from src.corroboration import construire_corroboration
        lignes = []
        for debut, fin, montant in [('2017-01-30', '2018-01-28', 9714e6),
                                    ('2018-01-29', '2019-01-27', 11716e6),
                                    ('2019-01-28', '2020-01-26', 10918e6)]:
            r = valeur(tag='RevenueFromContractWithCustomerExcludingAssessedTax', value=montant, cik='0001045810')
            r.update(debut=debut, fin=fin)
            lignes.append(r)
        recent = valeur(value=215938e6, cik='0001045810')
        recent.update(debut='2025-01-27', fin='2026-01-25')
        lignes.append(recent)
        b = construire_base(pd.DataFrame(lignes))
        self.assertEqual(b.chiffre_affaires_perimetre_id.nunique(), 1)
        self.assertEqual(b.chiffre_affaires.sum(), sum(r['valeur'] for r in lignes))
        u = b[['cik', 'nom']].drop_duplicates()
        _, details = construire_corroboration(b, u)
        ca = details[details.metrique == 'chiffre_affaires'].iloc[0]
        self.assertEqual(ca.base_annees, '2017;2018;2019')
        self.assertFalse(ca.base_repli)
        self.assertAlmostEqual(ca.multiple, 215938 / ((9714+11716+10918)/3))

    def test_nvda_equivalence_bornee_ne_masque_pas_revision_comparative(self):
        source = valeur(tag='RevenueFromContractWithCustomerExcludingAssessedTax', value=9700e6, cik='0001045810')
        source.update(debut='2017-01-30', fin='2018-01-28')
        revision = construire_base(pd.DataFrame([source])).iloc[0]
        self.assertEqual(revision.chiffre_affaires, 9700e6)
        self.assertEqual(revision.statut_chiffre_affaires, 'revue_requise')
        source['valeur'] = 9714e6
        source['cik'] = '0000000001'
        autre = construire_base(pd.DataFrame([source])).iloc[0]
        self.assertNotEqual(autre.chiffre_affaires_methode, 'equivalence_etiquettes_documentee')
        futur = construire_base(pd.DataFrame([valeur(year=2027, cik='0001045810')])).iloc[0]
        self.assertNotEqual(futur.chiffre_affaires_methode, 'equivalence_etiquettes_documentee')

    def test_annee_majoritaire_juin_et_janvier(self):
        self.assertEqual(annee_majoritaire('2024-07-01', '2025-06-30'), 2024)
        self.assertEqual(annee_majoritaire('2025-01-27', '2026-01-25'), 2025)

    def test_aep_ne_prend_pas_acquisitions_de_centrales(self):
        d = pd.DataFrame([valeur('investissement', 'PaymentsToAcquireProductiveAssets', 3453e6, cik='0000004904'),
                          valeur('investissement', 'PaymentsForConstructionInProcess', 8453e6, cik='0000004904')])
        d.loc[1, 'rang_preference'] = 3
        b = construire_base(d)
        self.assertEqual(b.iloc[0].capex, 8453e6)
        self.assertEqual(b.iloc[0].statut_capex, 'observe')
        self.assertTrue(b.iloc[0].capex_source_url)

    def test_wdc_reconciliation_flux_et_perimetre_distinct(self):
        a = valeur('investissement', 'PaymentsToAcquirePropertyPlantAndEquipment', 821e6, 2023, '0000106040')
        a.update(debut='2022-07-02', fin='2023-06-30')
        b = construire_base(pd.DataFrame([a, valeur('investissement', 'PaymentsToAcquirePropertyPlantAndEquipment', 500e6, 2018, '0000106040')]))
        recent = b[b.capex_fin == '2023-06-30'].iloc[0]
        self.assertEqual(recent.capex, 602e6)
        self.assertEqual(recent.capex_valeur_avant_reconciliation, 821e6)
        self.assertEqual(recent.comparabilite_capex, 'comparable')
        self.assertEqual(b[b.capex_fin == '2018-12-31'].iloc[0].comparabilite_capex, 'hors_perimetre_actuel')

    def test_reconciliation_ne_survit_pas_a_valeur_brute_changee(self):
        a = valeur('investissement', 'PaymentsToAcquirePropertyPlantAndEquipment', 999e6, 2023, '0000106040')
        a.update(debut='2022-07-02', fin='2023-06-30')
        b = construire_base(pd.DataFrame([a])).iloc[0]
        self.assertEqual(b.capex, 999e6)
        self.assertEqual(b.statut_capex, 'revue_requise')

    def test_revenu_non_reconcilie_reste_visible(self):
        a = valeur(value=100)
        b = valeur(tag='RevenueFromContractWithCustomerExcludingAssessedTax', value=10)
        out = construire_base(pd.DataFrame([a, b]), {'exceptions': []}).iloc[0]
        self.assertEqual(out.chiffre_affaires, 100)
        self.assertEqual(out.statut_chiffre_affaires, 'revue_requise')
        self.assertTrue(pd.isna(out.capex))

    def test_faible_divergence_ne_prouve_pas_equivalence(self):
        for notion, metric, tags in [
            ('chiffre_affaires', 'chiffre_affaires', ('Revenues', 'RevenueFromContractWithCustomerExcludingAssessedTax')),
            ('investissement', 'capex', ('PaymentsToAcquirePropertyPlantAndEquipment', 'PaymentsToAcquireProductiveAssets')),
            ('recherche', 'rd', ('ResearchAndDevelopmentExpense', 'ResearchAndDevelopmentExpenseExcludingAcquiredInProcessCost')),
        ]:
            with self.subTest(metrique=metric):
                a = valeur(notion, tags[0], 100)
                b = valeur(notion, tags[1], 99)
                b['rang_preference'] = 1
                out = construire_base(pd.DataFrame([a, b]), {'exceptions': []}).iloc[0]
                self.assertEqual(out[metric], 100)
                self.assertEqual(out[f'statut_{metric}'], 'revue_requise')
                self.assertEqual(out[f'comparabilite_{metric}'], 'non_etablie')
                b['valeur'] = 99.995
                arrondi = construire_base(pd.DataFrame([a, b]), {'exceptions': []}).iloc[0]
                self.assertEqual(arrondi[f'statut_{metric}'], 'observe')

    def test_cms_complement_identifie_et_pas_impute(self):
        out = construire_base(pd.DataFrame([valeur(cik='0000811156')]))
        r = out[out.annee == 2025].iloc[0]
        self.assertEqual(r.capex, 3824e6)
        self.assertEqual(r.capex_methode, 'lecture_ligne_10K_documentee')
        self.assertEqual(r.capex_depose_le, '2026-02-10')

    def test_deux_periodes_meme_annee_non_ecrasees(self):
        lignes = [dict(annee=2025, debut='2025-01-01', fin='2025-12-31', depose_le='2026-02-01', depot='a'),
                  dict(annee=2025, debut='2024-12-30', fin='2025-12-28', depose_le='2026-02-01', depot='b')]
        self.assertEqual(len(choisir_par_exercice(lignes)), 2)

    def test_base_conserve_clotures_distinctes_meme_annee_majoritaire(self):
        a, b = valeur(year=2022), valeur(year=2023)
        a.update(debut='2021-07-03', fin='2022-07-01')
        b.update(debut='2022-07-02', fin='2023-06-30')
        out = construire_base(pd.DataFrame([a, b]), {'exceptions': []})
        self.assertEqual(len(out), 2)
        self.assertEqual(out.annee.nunique(), 1)
        self.assertEqual(out.periode_id.nunique(), 2)

    def test_metriques_meme_cloture_debuts_differents_restent_reunies(self):
        a = valeur()
        b = valeur('investissement', 'PaymentsToAcquirePropertyPlantAndEquipment', 30)
        b['debut'] = '2024-12-31'
        out = construire_base(pd.DataFrame([a, b]), {'exceptions': []})
        self.assertEqual(len(out), 1)
        self.assertEqual(out.iloc[0].capex, 30)
        self.assertIn('périodes des métriques différentes', set(controler_base(out).test))

    def test_amendement_annuel_retenu_sans_dependre_fp(self):
        facts={'us-gaap': {'Revenues': {'units': {'USD': [dict(form='10-K/A',fp='Q4',start='2025-01-01',end='2025-12-31',val=100,accn='a',filed='2026-02-01')]}}}}
        self.assertEqual(len(extraire_valeurs_annuelles(facts, 'Revenues')), 1)

    def test_controle_couvre_manquants_et_ne_mesure_pas_gap_comme_un_an(self):
        d=pd.DataFrame([valeur(value=10, year=2020), valeur(value=100, year=2025)])
        b=construire_base(d, {'exceptions': []})
        q=controler_base(b)
        self.assertIn('trou dans la série', set(q.test))
        self.assertNotIn('rupture de série à vérifier', set(q.test))


if __name__ == '__main__':
    unittest.main()
