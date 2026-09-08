"""Le complément documentaire ne doit pas contourner l'identité de la preuve."""
import hashlib
import tempfile
import unittest
from pathlib import Path
import pandas as pd
from src.classification_manuelle import charger_complements


class ComplementTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.p = self.root/'data/review/sources_finition_2026-09-08/preuve.txt'
        self.p.parent.mkdir(parents=True)
        self.p.write_text('Activité documentée.', encoding='utf-8')
        self.termes = pd.DataFrame([dict(cik='0000000001', depot='', source_url='')])
        self.source = dict(cik='0000000001', depot='0000000001-26-000001',
            source_url='https://www.sec.gov/Archives/edgar/data/1/000000000126000001/a.htm',
            texte=self.p.relative_to(self.root).as_posix(),
            texte_sha256=hashlib.sha256(self.p.read_bytes()).hexdigest())

    def charger(self):
        pd.DataFrame([self.source]).to_csv(self.root/'data/review/decisions_sources_complementaires.csv', index=False)
        return charger_complements(self.termes, self.root)

    def test_complement_rattache_sans_modifier_le_corpus(self):
        t, textes = self.charger()
        self.assertEqual(t.depot.iloc[0],self.source['depot'])
        self.assertEqual(textes[('0000000001',self.source['depot'])], 'Activité documentée.')
        self.assertEqual(self.termes.depot.iloc[0], '')

    def test_preuve_alteree_refusee(self):
        self.p.write_text('Texte remplacé.', encoding='utf-8')
        with self.assertRaisesRegex(ValueError,'Empreinte'): self.charger()

    def test_identite_etrangere_refusee(self):
        self.source['source_url'] = self.source['source_url'].replace('/data/1/','/data/2/')
        with self.assertRaisesRegex(ValueError,'CIK'): self.charger()

    def test_complement_ne_remplace_pas_un_rapport(self):
        self.termes.loc[0,'depot'] = 'nouveau rapport'
        with self.assertRaisesRegex(ValueError,'remplacer'): self.charger()


if __name__ == '__main__': unittest.main()
