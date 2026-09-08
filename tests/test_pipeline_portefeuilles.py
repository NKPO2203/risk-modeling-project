"""Échecs de fichier et oracle de compte de parts, indépendants du replay réel."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import numpy as np
import pandas as pd

from src.controle_prix import verifier_structure_prix
from src.construire_portefeuilles import appartenance, verifier, verifier_bruts
from src.portefeuille import preparer_prix, simuler


class ContratsDonneesTests(unittest.TestCase):
    def prix(self):
        return pd.DataFrame({'date':['2020-01-02','2020-01-03'],
            'Open':[100.,101.], 'High':[100.,101.], 'Low':[100.,101.],
            'Close':[100.,101.], 'Adj Close':[100.,101.],
            'Volume':[100.,100.], 'Dividends':[0.,0.], 'Stock Splits':[0.,0.]})

    def test_prix_infinis_et_evenements_inconnus_refuses(self):
        for col,val in [('Open',np.inf),('Adj Close',np.inf),('Dividends',np.nan),
                        ('Stock Splits',-2.),('Volume',np.nan),('Close','texte')]:
            with self.subTest(col=col,val=val):
                p=self.prix();p[col]=p[col].astype(object);p.loc[1,col]=val
                with self.assertRaises((ValueError,TypeError)):
                    verifier_structure_prix(p,'essai.csv')

    def test_absence_prix_reste_identifiable_sans_faux_zero(self):
        p=self.prix();p.loc[1,['Open','High','Low','Close','Adj Close']]=np.nan
        verifier_structure_prix(p,'essai.csv')
        prepare=preparer_prix(p)
        self.assertTrue(prepare.cours_porte.iloc[1])
        self.assertTrue(np.isnan(prepare.rendement_observe.iloc[1]))

    def test_fichier_vide_ou_dates_impossibles_refuses(self):
        with self.assertRaises(ValueError):verifier_structure_prix(self.prix().iloc[:0],'vide.csv')
        p=self.prix();p.loc[1,'date']='2020-02-31'
        with self.assertRaises(ValueError):verifier_structure_prix(p,'date.csv')

    def test_disponibilite_texte_ne_devient_pas_vrai(self):
        r=pd.DataFrame({'A':[0.,.1]},index=['2020-01-02','2020-01-03'])
        c=pd.DataFrame({'A':[1.]},index=r.index[:1])
        dispo=pd.DataFrame({'A':['False','False']},index=r.index)
        with self.assertRaisesRegex(ValueError,'booléen'):
            simuler(r,r*0,['A'],c,r.index,{r.index[0]},False,disponibilite=dispo)

    def test_manifeste_vide_ne_vaut_pas_validation(self):
        with tempfile.TemporaryDirectory() as tmp:
            path=Path(tmp)
            (path/'pipeline_portefeuilles.json').write_text(json.dumps(
                {'statut':'termine','entrees_sha256':{},'sorties_sha256':{}}))
            with patch('src.construire_portefeuilles.verifier_bruts',return_value=[]):
                with self.assertRaisesRegex(ValueError,'incomplet'):verifier(path,path)

    def test_brut_modifie_refuse_avant_calcul(self):
        with tempfile.TemporaryDirectory() as tmp:
            root=Path(tmp);raw=root/'data/raw';(raw/'prix').mkdir(parents=True);(raw/'benchmarks').mkdir()
            (raw/'prix/A.csv').write_text('modification')
            (raw/'prix_manifest.json').write_text(json.dumps({'prix':[{'fichier':'A.csv','sha256':'0'*64}], 'benchmarks':[]}))
            with self.assertRaisesRegex(ValueError,'Empreinte'):verifier_bruts(root)

    def test_registre_hors_regle_refuse(self):
        d=pd.DataFrame([{'verdict':'ENTRE','cik':'1','maturite_exposition':'inconnue',
                         'canal':'vend','secteur':'Information Technology','symboles':'A','nom':'A'}])
        with self.assertRaisesRegex(ValueError,'Maturité'):appartenance(d)
        d.loc[0,'maturite_exposition']='etablie';d.loc[0,'canal']='autre'
        with self.assertRaisesRegex(ValueError,'Canal'):appartenance(d)


class OraclePartsTests(unittest.TestCase):
    def test_comptes_de_parts_aleatoires_entree_dividendes_et_frais(self):
        """Deux titres au départ, un entrant, puis janvier : 40 scénarios fixés.

        L'oracle tient des quantités de parts et des créances nominales. Les
        frais sont obtenus par point fixe, pas par le solveur du moteur.
        """
        rng=np.random.default_rng(8092026)
        dates=pd.Index(['2020-12-28','2020-12-29','2020-12-30','2020-12-31','2021-01-04','2021-01-05'])
        for scenario in range(40):
            prices=100*np.exp(np.cumsum(rng.normal(0,.1,(6,3)),axis=0))
            div=rng.uniform(0,2,(6,3));div[0]=0;div[:3,2]=0
            returns=np.vstack([np.zeros(3),prices[1:]/prices[:-1]-1]);returns[:3,2]=np.nan
            det=np.vstack([np.zeros(3),div[1:]/prices[:-1]])
            targets=pd.DataFrame([[.5,.5,0],[1/3]*3,[1/3]*3],index=dates[[0,3,4]],columns=['A','B','C'])
            for reeq in [False,True]:
                rate=float(rng.uniform(0,.02))
                units=np.array([.5/prices[0,0],.5/prices[0,1],0.]);cash=np.zeros(3);expected=[]
                for i in range(6):
                    if i:cash+=units*div[i]
                    old=units*prices[i];value=old.sum()+cash.sum()
                    if i==3:
                        target=old*(2/3);reserve=cash*(2/3);target[2]=value/3
                    elif i==4:
                        target=np.full(3,value/3) if reeq else old+cash
                        reserve=np.zeros(3)
                    else:
                        expected.append(value);continue
                    fee=0.
                    for _ in range(100):
                        next_fee=rate*np.abs(target*(1-fee/value)-old).sum()
                        if abs(next_fee-fee)<1e-15:fee=next_fee;break
                        fee=next_fee
                    units=target*(1-fee/value)/prices[i];cash=reserve*(1-fee/value)
                    expected.append((units*prices[i]).sum()+cash.sum())
                r=pd.DataFrame(returns,index=dates,columns=targets.columns)
                d=pd.DataFrame(det,index=dates,columns=targets.columns)
                actual,_,_=simuler(r,d,list(r),targets,dates,{dates[0],dates[4]},reeq,rate)
                np.testing.assert_allclose(actual,expected,rtol=0,atol=2e-14,
                                           err_msg=f'scenario={scenario},reeq={reeq}')


if __name__=='__main__':unittest.main()
