"""Une empreinte ne doit pas dépendre du système qui a extrait le dépôt."""
import hashlib
import tempfile
import unittest
from pathlib import Path

from src.empreintes import correspond, empreinte


class EmpreintesTests(unittest.TestCase):

    def setUp(self):
        self.dossier = tempfile.TemporaryDirectory()
        self.racine = Path(self.dossier.name)

    def tearDown(self):
        self.dossier.cleanup()

    def ecrire(self, nom, contenu):
        p = self.racine / nom
        p.write_bytes(contenu)
        return p

    def test_csv_produit_sous_windows_et_extrait_sous_linux(self):
        attendu = hashlib.sha256(b"date,prix\r\n2000-01-03,10\r\n").hexdigest()
        p = self.ecrire("a.csv", b"date,prix\n2000-01-03,10\n")
        self.assertNotEqual(empreinte(p), attendu)
        self.assertTrue(correspond(p, attendu))

    def test_csv_produit_sous_linux_et_extrait_sous_windows(self):
        attendu = hashlib.sha256(b"date,prix\n2000-01-03,10\n").hexdigest()
        p = self.ecrire("a.csv", b"date,prix\r\n2000-01-03,10\r\n")
        self.assertTrue(correspond(p, attendu))

    def test_un_contenu_modifie_reste_refuse(self):
        attendu = hashlib.sha256(b"date,prix\r\n2000-01-03,10\r\n").hexdigest()
        p = self.ecrire("a.csv", b"date,prix\n2000-01-03,11\n")
        self.assertFalse(correspond(p, attendu))

    def test_l_empreinte_d_un_texte_ne_depend_pas_du_systeme(self):
        lf = self.ecrire("lf.csv", b"date,prix\n2000-01-03,10\n")
        crlf = self.ecrire("crlf.csv", b"date,prix\r\n2000-01-03,10\r\n")
        self.assertEqual(empreinte(lf), empreinte(crlf))
        self.assertEqual(empreinte(lf), hashlib.sha256(b"date,prix\n2000-01-03,10\n").hexdigest())

    def test_l_empreinte_d_un_binaire_porte_sur_ses_octets(self):
        a = self.ecrire("a.xlsx", b"PK\n")
        b = self.ecrire("b.xlsx", b"PK\r\n")
        self.assertNotEqual(empreinte(a), empreinte(b))

    def test_un_fichier_binaire_n_est_pas_normalise(self):
        attendu = hashlib.sha256(b"PK\r\n").hexdigest()
        p = self.ecrire("a.xlsx", b"PK\n")
        self.assertFalse(correspond(p, attendu))


if __name__ == "__main__":
    unittest.main()
