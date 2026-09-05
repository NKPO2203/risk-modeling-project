"""Contrôles hors ligne du corpus livré, de ses sources et de ses citations.

Ces tests utilisent les artefacts du dépôt ; ils ne téléchargent et ne modifient
rien. Ils détectent une publication CSV incomplète, un cache altéré et une
attribution de citation à un mauvais document ou à de mauvais offsets.
"""
import csv
import hashlib
import json
import unittest
from functools import lru_cache
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"


def sha256_bytes(contenu):
    return hashlib.sha256(contenu).hexdigest()


def lignes_csv(chemin):
    with chemin.open(encoding="utf-8", newline="") as fichier:
        return list(csv.DictReader(fichier))


class IntegriteCorpusTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads((RAW / "filings_manifest.json").read_text(encoding="utf-8"))
        cls.termes = lignes_csv(RAW / "filings_termes.csv")
        cls.par_cik = {ligne["cik"]: ligne for ligne in cls.termes}
        cls.phrases = lignes_csv(RAW / "filings_phrases.csv")

    def test_manifest_identifie_exactement_les_csv_publies(self):
        self.assertEqual(set(self.manifest["files"]), {
            "filings_termes.csv", "filings_phrases.csv", "filings_log.csv"})
        for nom, attendu in self.manifest["files"].items():
            with self.subTest(fichier=nom):
                contenu = (RAW / nom).read_bytes()
                self.assertEqual(len(contenu), attendu["bytes"])
                self.assertEqual(sha256_bytes(contenu), attendu["sha256"])
        self.assertEqual(len(self.termes), self.manifest["entreprises"])
        self.assertEqual(len(self.par_cik), len(self.termes))
        attendus = {ligne["CIK"].zfill(10) for ligne in lignes_csv(RAW / "sp500_constituents.csv")}
        self.assertEqual(set(self.par_cik), attendus)
        self.assertEqual(len(self.phrases), self.manifest["passages"])
        complets = sum(ligne["couverture"] == "vocabulaire_complet" for ligne in self.termes)
        self.assertEqual(complets, self.manifest["rapports_complets"])

    def test_sources_cachees_et_identites_correspondent_aux_empreintes(self):
        for ligne in self.termes:
            if ligne["couverture"] != "vocabulaire_complet":
                continue
            with self.subTest(cik=ligne["cik"], depot=ligne["depot"]):
                chemin_meta = ROOT / ligne["cache_metadata"]
                self.assertTrue(chemin_meta.resolve().is_relative_to((RAW / "filings_text").resolve()))
                meta = json.loads(chemin_meta.read_text(encoding="utf-8"))
                for cle in ("depot", "source_cik", "source_url", "date_depot", "texte_sha256", "html_sha256"):
                    self.assertEqual(meta[cle], ligne[cle], cle)
                for extension, cle in ((".html", "html_sha256"), (".txt", "texte_sha256")):
                    self.assertEqual(sha256_bytes(chemin_meta.with_suffix(extension).read_bytes()), meta[cle])
                if ligne["cik"] != ligne["source_cik"]:
                    self.assertEqual(ligne["source_kind"], "10-K_predecesseur_verifie")
                    preuve = RAW / "filings_text" / "identity_proofs" / (ligne["cik"] + ".html")
                    identite = json.loads(preuve.with_suffix(".json").read_text(encoding="utf-8"))
                    self.assertEqual(sha256_bytes(preuve.read_bytes()), identite["sha256"])
                    self.assertEqual(identite["cik"], ligne["source_cik"])
                    self.assertEqual(identite["source_url"], ligne["source_verification_url"])

    def test_chaque_citation_et_ses_repetitions_existent_aux_offsets_declares(self):
        @lru_cache(maxsize=4)
        def texte_du_cik(cik):
            chemin = (ROOT / self.par_cik[cik]["cache_metadata"]).with_suffix(".txt")
            return chemin.read_text(encoding="utf-8")

        ids = set()
        nombres = {}
        for passage in self.phrases:
            cik, depot = passage["cik"], passage["depot"]
            with self.subTest(cik=cik, phrase_id=passage["phrase_id"]):
                ligne = self.par_cik[cik]
                self.assertEqual(depot, ligne["depot"])
                self.assertEqual(passage["source_url"], ligne["source_url"])
                self.assertEqual(passage["texte_sha256"], ligne["texte_sha256"])
                self.assertEqual(passage["couverture"], "vocabulaire_complet")
                texte = texte_du_cik(cik)
                debut, fin = int(passage["debut"]), int(passage["fin"])
                offsets = json.loads(passage["offsets_json"])
                self.assertIn([debut, fin], offsets)
                for gauche, droite in offsets:
                    self.assertTrue(0 <= gauche < droite <= len(texte))
                    self.assertEqual(texte[gauche:droite], passage["phrase"])
                attendu = sha256_bytes((depot + "\0" + passage["phrase"]).encode("utf-8"))[:24]
                self.assertEqual(passage["phrase_id"], attendu)
                self.assertNotIn((cik, attendu), ids)
                ids.add((cik, attendu))
                nombres[cik] = nombres.get(cik, 0) + 1
        for ligne in self.termes:
            if ligne["couverture"] == "vocabulaire_complet":
                self.assertEqual(nombres.get(ligne["cik"], 0), int(ligne["nb_passages"]))


if __name__ == "__main__":
    unittest.main()
