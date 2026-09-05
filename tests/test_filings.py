"""Régressions des pertes de preuve et de la reproductibilité du collecteur."""
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from src import fetch_filings_text as f


class ExtractionTests(unittest.TestCase):
    def test_all_short_and_late_mentions_survive(self):
        texte = "\n".join(f"AI project number {i}." for i in range(65))
        comptes, passages, couverts = f.analyser(texte, "0001-26-000001")
        self.assertEqual((comptes["ia_sigle"], len(passages), couverts), (65, 65, 65))
        self.assertIn("number 64", passages[-1]["phrase"])

    def test_long_sentence_and_same_prefix_do_not_lose_evidence(self):
        prefixe = "Shared introductory language " * 8
        texte = (prefixe + "data center demand is contracted.\n" + prefixe
                 + "data center demand is speculative.\n" + "ordinary text " * 900
                 + "liquid cooling is an emerging demand driver.")
        comptes, passages, couverts = f.analyser(texte, "acc")
        self.assertEqual(sum(comptes.values()), couverts)
        self.assertTrue(any("contracted" in p["phrase"] for p in passages))
        self.assertTrue(any("speculative" in p["phrase"] for p in passages))
        self.assertTrue(any("liquid cooling" in p["phrase"] for p in passages))
        self.assertTrue(any(p["type_passage"] == "fenetre_longue" for p in passages))
        for p in passages:
            self.assertEqual(texte[p["debut"]:p["fin"]], p["phrase"])

    def test_repeated_passage_tracks_every_location_with_stable_id(self):
        texte = "AI demand.\nAI demand."
        comptes, passages, couverts = f.analyser(texte, "acc")
        self.assertEqual((len(passages), couverts), (1, 2))
        self.assertEqual(len(json.loads(passages[0]["offsets_json"])), 2)
        autre = f.analyser("Other preface.\nAI demand.", "acc")[1]
        self.assertEqual(passages[0]["phrase_id"], autre[0]["phrase_id"])
        self.assertNotEqual(passages[0]["phrase_id"], f.analyser("AI demand.", "new")[1][0]["phrase_id"])

    def test_multiline_match_and_empty_document(self):
        comptes, passages, couverts = f.analyser("A data\ncenter contract.")
        self.assertEqual((comptes["centre_de_donnees"], couverts), (1, 1))
        self.assertEqual(passages[0]["type_passage"], "fenetre_frontiere")
        self.assertEqual(f.analyser("Nothing relevant.")[1:], ([], 0))

    def test_multiword_terms_survive_html_line_breaks(self):
        texte = ("artificial\nintelligence; generative\nAI; machine\nlearning; "
                 "accelerated\ncomputing; graphics\nprocessing\nunit; "
                 "high-performance\ncomputing; large\nlanguage\nmodel; "
                 "foundation\nmodel; neural\nnetwork; liquid\ncooling; "
                 "cloud\ninfrastructure; data\n\ncenter")
        comptes, passages, couverts = f.analyser(texte, "acc")
        for nom in ("intelligence_artificielle", "ia_generative", "apprentissage_automatique",
                    "calcul_accelere", "processeur_graphique", "calcul_haute_performance",
                    "reseau_de_neurones", "refroidissement_liquide", "infrastructure_cloud",
                    "centre_de_donnees"):
            self.assertEqual(comptes[nom], 1, nom)
        self.assertEqual(comptes["grand_modele_de_langage"], 2)
        self.assertEqual(couverts, sum(comptes.values()))
        for p in passages:
            self.assertEqual(texte[p["debut"]:p["fin"]], p["phrase"])

    def test_visible_text_keeps_tables_but_not_hidden_facts(self):
        source = b'<html><body><script>AI fake</script><div style="display:none">AI hidden</div><p>AI demand.</p><table><tr><td>Data centers</td><td>42</td></tr></table></body></html>'
        texte = f.texte_du_html(source)
        self.assertIn("Data centers 42", texte)
        self.assertNotIn("fake", texte)
        self.assertNotIn("hidden", texte)
        self.assertEqual(f.analyser(texte)[0]["ia_sigle"], 1)

    def test_atomic_replace_failure_preserves_previous_file(self):
        with tempfile.TemporaryDirectory() as repertoire:
            chemin = Path(repertoire) / "output.csv"
            chemin.write_bytes(b"previous complete result")
            with patch.object(f.os, "replace", side_effect=PermissionError("locked")):
                with self.assertRaises(PermissionError):
                    f.ecrire_atomique(chemin, b"new")
            self.assertEqual(chemin.read_bytes(), b"previous complete result")
            self.assertEqual([p.name for p in chemin.parent.iterdir()], ["output.csv"])

    def test_cached_source_is_verified_before_reuse(self):
        with tempfile.TemporaryDirectory() as repertoire:
            cache = Path(repertoire)
            info = {"source_cik": "0000000001", "depot": "0001-26-000001",
                    "date_depot": "2026-01-01", "source_url": "https://www.sec.gov/example",
                    "report_date": "2025-12-31"}
            html_brut = ("<html><p>" + "ordinary words " * 1000 + "AI demand.</p></html>").encode()
            client = unittest.mock.Mock()
            client.obtenir.return_value = html_brut
            texte, meta = f.charger_rapport(client, cache, info)
            self.assertEqual(f.rapport_cache(cache, info), (texte, meta))
            f.chemins_cache(cache, info)[1].write_bytes(b"tampered")
            with self.assertRaisesRegex(ValueError, "Empreinte"):
                f.rapport_cache(cache, info)


if __name__ == "__main__":
    unittest.main()
