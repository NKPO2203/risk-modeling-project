"""Contre-exemples de l'audit du 8 septembre, calculables indépendamment du moteur."""
import unittest
import numpy as np
import pandas as pd
from src.portefeuille import preparer_prix, simuler, poids_cibles


class AuditMoteurTests(unittest.TestCase):
    def run_case(self, r, w, *, reeq=False, cout=0, d=None, entreprises=None, annuel=None):
        r = pd.DataFrame(r)
        r.index = [f"2020-01-{i+1:02d}" for i in range(len(r))]
        d = pd.DataFrame(0., index=r.index, columns=r.columns) if d is None else pd.DataFrame(d, index=r.index)
        c = pd.DataFrame(w, columns=r.columns)
        c.index = r.index[[0, len(r)-1]] if len(c)==2 else r.index[:1]
        journal=[]
        result = simuler(r,d,list(r),c,r.index,set(annuel or [r.index[0]]),reeq,cout,
                         fins_de_mois=set(r.index),entreprises=entreprises,journal=journal)
        return (*result,journal)

    def test_entree_hors_janvier_financee_dans_les_deux_versions(self):
        for reeq in [False,True]:
            v,_,w,_=self.run_case({'A':[0,0],'B':[np.nan,0]},[[1,0],[.5,.5]],reeq=reeq)
            self.assertAlmostEqual(v.iloc[-1],1)
            self.assertAlmostEqual(w.B.iloc[-1],.5)

    def test_achats_et_ventes_factures(self):
        v,_,_,j=self.run_case({'A':[0,0],'B':[np.nan,0]},[[1,0],[.5,.5]],cout=.001)
        self.assertAlmostEqual(v.iloc[-1],.999,places=12)
        self.assertAlmostEqual(j[-1]['echange'],1,places=12)
        self.assertAlmostEqual(j[-1]['frais'],.001,places=12)

    def test_frais_reinvestissement_dividende_conserve(self):
        v,_,_,j=self.run_case({'A':[0,-.1]},[[1],[1]],d={'A':[0,.1]},cout=.001,
                              annuel=['2020-01-01','2020-01-02'])
        self.assertAlmostEqual(j[-1]['frais'],.0001/1.001,places=12)
        self.assertAlmostEqual(v.iloc[-1],1-.0001/1.001,places=12)

    def test_faillite_ne_recree_pas_de_mise(self):
        v,_,_,_=self.run_case({'A':[0,-1,0]},[[1],[1]],annuel=['2020-01-01','2020-01-03'])
        self.assertEqual(v.tolist(),[1.,0.,0.])

    def test_deuxieme_classe_ne_dilue_pas_une_autre_entreprise(self):
        v,_,w,_=self.run_case({'A1':[0,0],'B':[0,0],'A2':[np.nan,0]},
            [[.5,.5,0],[.25,.5,.25]],entreprises={'A1':'1','A2':'1','B':'2'})
        self.assertAlmostEqual(w.B.iloc[-1],.5)
        self.assertAlmostEqual(w.A1.iloc[-1]+w.A2.iloc[-1],.5)
        self.assertAlmostEqual(v.iloc[-1],1)

    def test_nouvelle_entreprise_comptee_par_cik(self):
        _,_,w,_=self.run_case({'A1':[0,0],'A2':[0,0],'B':[0,0],'C':[np.nan,0]},
            [[.25,.25,.5,0],[1/6,1/6,1/3,1/3]],entreprises={'A1':'1','A2':'1','B':'2','C':'3'})
        self.assertAlmostEqual(w.C.iloc[-1],1/3)

    def test_dividende_sans_baisse_du_prix_est_possible(self):
        v,_,_,_=self.run_case({'A':[0,0]},[[1]],d={'A':[0,.1]})
        self.assertAlmostEqual(v.iloc[-1],1.1)

    def test_manquant_sur_position_refuse(self):
        with self.assertRaisesRegex(ValueError,'inconnu'):
            self.run_case({'A':[0,np.nan]},[[1]])

    def test_infini_et_rendement_inferieur_a_moins_un_refuses(self):
        for valeur in [np.inf,-np.inf,-1.01]:
            with self.assertRaises(ValueError):
                self.run_case({'A':[0,valeur]},[[1]])

    def test_cibles_invalides_refusees(self):
        for w in [[np.nan],[np.inf],[-1],[.9],[1.1]]:
            with self.assertRaises(ValueError):
                self.run_case({'A':[0,0]},[w])

    def test_dates_desalignees_refusees(self):
        r=pd.DataFrame({'A':[0,0]},index=['2020-01-01','2020-01-02'])
        with self.assertRaises(ValueError):
            simuler(r,r.iloc[::-1],['A'],pd.DataFrame({'A':[1]},index=r.index[:1]),r.index,{r.index[0]},False)

    def test_cibles_reordonnees_par_symbole(self):
        r=pd.DataFrame({'A':[0,.2],'B':[0,0]},index=['2020-01-01','2020-01-02'])
        w=pd.DataFrame({'B':[.2],'A':[.8]},index=r.index[:1])
        v,_,_=simuler(r,r*0,['A','B'],w,r.index,{r.index[0]},False,cout=0)
        self.assertAlmostEqual(v.iloc[-1],1.16)

    def test_encadrement_inclut_cash_dividendes_et_frais(self):
        v,_,_,j=self.run_case({'A':[0,-.1,0],'B':[0,0,.2]},[[.5,.5],[.5,.5]],
             d={'A':[0,.1,0],'B':[0,0,0]},cout=.001,reeq=True,
             annuel=['2020-01-01','2020-01-03'])
        for i in range(1,len(v)):
            actual=v.iloc[i]/v.iloc[i-1]-1
            self.assertAlmostEqual(actual,j[i]['rendement_attendu_avant_frais']-j[i]['frais']/j[i]['valeur_avant'])


class AuditPrixTests(unittest.TestCase):
    def prix(self,close,volume=None):
        return pd.DataFrame({'Close':close,'Open':close,'High':close,'Low':close,
            'Volume':volume if volume is not None else [100]*len(close),'Dividends':[0]*len(close)})

    def test_reprise_recupere_tout_le_mouvement(self):
        p=preparer_prix(self.prix([100,np.nan,121,133.1]))
        self.assertTrue(p.rendement_observe.iloc[1:3].isna().all())
        self.assertAlmostEqual((1+p.rendement_valorisation.iloc[1:]).prod(),1.331)
        self.assertEqual(p.cours_porte.tolist(),[False,True,False,False])

    def test_pas_de_prolongement_avant_le_premier_cours(self):
        p=preparer_prix(self.prix([np.nan,np.nan,100,110]))
        self.assertTrue(p.rendement_valorisation.iloc[:3].isna().all())

    def test_volume_nul_variable_ne_signifie_pas_prix_fabrique(self):
        p=preparer_prix(self.prix([100,101,102],[100,0,100]))
        self.assertTrue(p.disponible.all())

    def test_prix_fige_suspect_est_porte_puis_raccorde(self):
        p=preparer_prix(self.prix([100,100,110],[100,0,100]))
        self.assertFalse(p.disponible.iloc[1])
        self.assertAlmostEqual(p.rendement_valorisation.iloc[2],.1)

    def test_indice_volume_zero_reste_entier(self):
        p=preparer_prix(self.prix([100,101,102],[0,0,0]),indice=True)
        self.assertTrue(p.disponible.all())

    def test_division_deja_retraitee_n_est_pas_appliquee_deux_fois(self):
        prix=self.prix([50,51,52]);prix['Stock Splits']=[0,2,0]
        p=preparer_prix(prix)
        self.assertAlmostEqual((1+p.rendement_valorisation.dropna()).prod(),52/50)

    def test_dividende_absent_apres_debut_refuse(self):
        p=self.prix([100,101]);p.loc[1,'Dividends']=np.nan
        with self.assertRaises(ValueError):preparer_prix(p)

    def test_cik_prioritaire_sur_nom(self):
        membres=pd.DataFrame({'titre':['A1','A2','B'],'entreprise':['ancien nom','nouveau nom','autre'],'cik':['1','1','2']})
        w=poids_cibles(membres,list(membres.titre))
        self.assertEqual(w,{'A1':.25,'A2':.25,'B':.5})


if __name__=='__main__':unittest.main()
