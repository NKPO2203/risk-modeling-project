"""Oracles de richesse distribuée et protection de la preuve brute."""
from pathlib import Path
import unittest
import numpy as np
import pandas as pd
from src.corrections_prix import corriger_prix, lire_corrections
from src.construire_portefeuilles import lire_prix
from src.portefeuille import preparer_prix
from src.recouper_prix import rapprocher

ROOT = Path(__file__).resolve().parents[1]


class CorrectionsEvenementsTests(unittest.TestCase):
    def test_comparaison_refuse_le_faux_quotidien_sur_dates_absentes(self):
        p=pd.DataFrame({'Close':[100.,110.,121.],'Dividends':0.,'Stock Splits':0.},index=['2020-01-02','2020-01-03','2020-01-06'])
        n=pd.Series([100.,121.],index=['2020-01-02','2020-01-06'])
        self.assertTrue(rapprocher(p,n).ecart_r.isna().all())

    def test_comparaison_detecte_un_cours_stale(self):
        p=pd.DataFrame({'Close':[100.,110.],'Dividends':0.,'Stock Splits':0.},index=['2020-01-02','2020-01-03'])
        n=pd.Series([100.,100.],index=p.index)
        self.assertAlmostEqual(rapprocher(p,n).ecart_r.iloc[-1],-.1)

    def test_tyco_valeur_des_trois_societes(self):
        p = lire_prix(ROOT/'data/raw/prix/JCI.csv')
        avant = p.copy(deep=True)
        regle = [r for r in lire_corrections(ROOT) if r['titre']=='JCI' and r['date']=='2007-07-02']
        q = corriger_prix('JCI', p, regle)
        pp = preparer_prix(q)
        # Un lot de quatre anciennes actions donne un titre de chaque société.
        conversion_unites = p.loc['2007-07-02','Close'] / 53.36
        richesse_lot = (53.36 + 39.97 + 43.41) * conversion_unites
        attendu = richesse_lot / p.loc['2007-06-29','Close'] - 1
        self.assertAlmostEqual(pp.loc['2007-07-02','rendement_valorisation'], attendu, places=13)
        self.assertEqual(pp.loc['2007-07-02','dividende'], 0)
        pd.testing.assert_frame_equal(p, avant)
        pd.testing.assert_series_equal(q['Adj Close'], p['Adj Close'])

    def test_rendements_hors_evenements_invariants(self):
        regles = lire_corrections(ROOT)
        for t in {r['titre'] for r in regles}:
            with self.subTest(titre=t):
                p = lire_prix(ROOT/f'data/raw/prix/{t}.csv')
                a, b = preparer_prix(p), preparer_prix(corriger_prix(t,p,regles))
                masque = ~p.index.isin([r['date'] for r in regles if r['titre']==t])
                for col in ['rendement_valorisation','dividende']:
                    np.testing.assert_allclose(a.loc[masque,col], b.loc[masque,col], atol=1e-14, rtol=1e-12, equal_nan=True)

    def test_doubles_comptes_supprimes_sans_deuxieme_split(self):
        for t,date in [('ETN','2001-01-02'),('CNP','2002-10-01'),('HD','2001-11-28')]:
            p = lire_prix(ROOT/f'data/raw/prix/{t}.csv')
            regles = [r for r in lire_corrections(ROOT) if r['titre']==t and r['date']==date]
            q = corriger_prix(t,p,regles)
            pd.testing.assert_series_equal(p.Close,q.Close)
            self.assertEqual(q.loc[date,'Dividends'],0)
            if t == 'HD':
                self.assertEqual(q.loc['2001-11-27','Dividends'],.05)

    def test_reclassement_conserve_la_richesse_du_jour(self):
        for r in lire_corrections(ROOT):
            if r['statut']!='convention_non_monetaire':continue
            p=lire_prix(ROOT/f"data/raw/prix/{r['titre']}.csv")
            q=corriger_prix(r['titre'],p,[r]);jour=r['date']
            a,b=preparer_prix(p),preparer_prix(q)
            self.assertAlmostEqual(a.loc[jour,'rendement_valorisation']+a.loc[jour,'dividende'],b.loc[jour,'rendement_valorisation'],places=13)

    def test_double_application_ou_cliche_modifie_refuse(self):
        regles=lire_corrections(ROOT)
        p=lire_prix(ROOT/'data/raw/prix/JCI.csv')
        q=corriger_prix('JCI',p,regles)
        with self.assertRaises(ValueError):corriger_prix('JCI',q,regles)
        p.loc['2007-07-02','Close']+=.01
        with self.assertRaises(ValueError):corriger_prix('JCI',p,regles)


if __name__=='__main__':unittest.main()
