"""Revision explicite du registre apres lecture du corpus integralement collecte.

Operation ponctuelle, hors pipeline. Les CIK/IDs ci-dessous sont des decisions
documentees le 05/09/2026, pas des regles automatiques de selection.
Les citations remplacees ont ete relues ; aucune similarite semantique ne valide
une preuve. Le journal conserve les anciennes et nouvelles decisions/citations.
"""
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REGISTRE = ROOT / "data/review/decisions_selection.csv"
VERSION = "2026-09-05_v2_corpus_complet"

# Renouvellement des citations dont la presentation HTML a change.
CITATIONS = {
    "0000002488": "4de716b721478046c08560e5",
    "0000010456": "e86e6da1ffc2abc3cf95e134",
    "0000019617": "5ded8986ecb513833e3f6c6e",
    "0000032604": "8ab5ab90a16877314f26f577",
    "0000056873": "32020d5328cba23f43f12c10",
    "0000064040": "436f1aee8b9a4b8fe020bfa2",
    "0000065984": "b5b4e30a5b2992b8f8836449",
    "0000072741": "93d102a1f0b372763cf85daa",
    "0000087347": "3ec6170f623f02cae973fec7",
    "0000217346": "5f184fe6800fe760dba41eb4",
    "0000310158": "6eb28c1348763bb7526cc576",
    "0000313616": "c5fe7584f9b83e745283864f",
    "0000352915": "66ae7829d96e847b78ca4f03",
    "0000740260": "4080b37e0eea79c94900a218",
    "0000796343": "151ff930e5850ea4a201ea53",
    "0000820313": "8e12718b3c7bc80395677afd",
    "0000860730": "b635339606cc63641abb697e",
    "0000866787": "90ed5cd03ea85f67d05d309e",
    "0000879169": "dd4821858be56d086bcb06cb",
    "0000883241": "d79b12d548bd821caf8df1cb",
    "0000898173": "8c46b682a54820003241e536",
    "0000910521": "d92a239451f395bfcda9c70c",
    "0000920148": "b60955deb32f5f441baa8aca",
    "0001043277": "cb13b70d98ad69299fec6135",
    "0001069183": "03ca8fa342d61f612f24a7d8",
    "0001071739": "4abb4f60a6a1ab01a8bd394a",
    "0001086222": "a8fd4efa33cbc3adcb92515c",
    "0001100682": "b36c524e103da039673c11e6",
    "0001375365": "cbcc7d5d7d125429c399657f",
    "0001385157": "eb8516d0c3e1f689022d2cd4",
    "0001415404": "bda9a04508fe2482a25f5277",
    "0001513761": "aafd022c15d77bb8c86695b5",
    "0001555280": "bdeffc036384dfcd2083fc46",
    "0001571996": "17735d6220eed30c835fd56e",
    "0001601046": "e37b0133b7985a25c507446a",
    "0001652044": "3a4c24f294eeba4e1a374d5f",
    "0001751788": "8739d173a03f3ed26efb62d4",
    "0001757898": "dc9088170805890177c3036a",
    "0001783180": "5f645d4c1c977865d61ec360",
    "0001967680": "edab5fab1adbe26f8f668167",
    "0002041610": "bcd1ddeeaadeb1fad231b779",
    "0002058873": "ec5dab5e47b27173cc76e295",
}

# Verdict, canal, maturite, preuve, motif : revue explicite, sans seuil de CA.
REVISIONS = {
    "0001176948": ("ENTRE", "fournit", "etablie", "5aada6f998a0210bc2c180b7",
        "Activite integree de developpement et exploitation de centres de donnees, avec plateforme operationnelle Ada Infrastructure. L'inclusion porte sur cette activite, pas sur toute la gestion d'actifs du groupe."),
    "0001402057": ("ENTRE", "fournit", "etablie", "7069180b569163b68779079b",
        "Offre actuelle de serveurs, stockage, alimentation/refroidissement et reseaux de centres de donnees, completee par des services de colocation et d'infrastructure. La distribution technique fait partie de la chaine ; part IA non fournie."),
    "0000726728": ("ENTRE", "fournit", "engagement_ou_developpement_documente", "f4624aad410538429d3abb32",
        "Coentreprise de centres de donnees deja loues depuis 2024, avec extension pour le client existant et quote-part de couts restant a engager de 216,8 millions de dollars. Engagement immobilier operationnel, pas simple placement diversifie."),
    "0001466258": ("ENTRE", "fournit", "etablie", "74496be744c051b4423625d3",
        "Le catalogue de produits/services comprend HVAC, refroidissement liquide, controles et services de centres de donnees. Offre actuelle documentee ; volume vendu et part propre a l'IA non quantifies."),
    "0000066740": ("ENTRE", "fournit", "etablie", "b1a2eaa1e76e63cfd0a1f363",
        "Solutions pour centres de donnees dans la liste des produits du segment Transportation and Electronics, aux cotes des materiaux semi-conducteurs et interconnexions. Offre presente, sans quantification de ventes IA."),
    "0001002910": ("ENTRE", "fournit", "engagement_ou_developpement_documente", "74521850f9a366c013b78197",
        "Le rapport mentionne des contrats de fourniture electrique signes en fevrier 2026 avec de grandes charges dans le contexte de l'expansion des centres de donnees. Le volume effectivement livre et la part IA restent a etablir."),
    "0000040533": ("ENTRE", "fournit", "etablie", "b4276c8f26cdb721158e8e8e",
        "GDIT fournit sous contrat des services de centres de donnees/cloud hybride et d'ingenierie, de mise en oeuvre et d'exploitation informatique. Offre technique operationnelle ; part propre a l'IA non quantifiee."),
    "0001396009": ("ENTRE", "fournit", "etablie", "7cacb0ea8a49fe54482edeb1",
        "Les granulats, asphalte et beton vendus sont utilises pour la construction de centres de donnees parmi d'autres ouvrages. Fourniture industrielle amont documentee, sans attribuer tout le segment construction a l'IA."),
    "0001524472": ("ENTRE", "fournit", "etablie", "e7a43285d5e84246f0720864",
        "Le marche industriel servi par les solutions de gestion de l'eau comprend explicitement les developpeurs et exploitants de centres de donnees. Fourniture technique presente, part IA non isolee."),
    "0000849395": ("ENTRE", "fournit", "etablie", "7038f92a3a906bb3f8d3250a",
        "Croissance 2025 du segment Building & Infrastructure Solutions soutenue notamment par l'activite du marche centres de donnees. Materiaux/solutions industriels fournis ; le total du segment n'est pas une part IA."),
    "0000815556": ("ENTRE", "fournit", "etablie", "52bb5e3a677462447520f118",
        "Le distributeur de fournitures industrielles sert explicitement les centres de donnees et leurs operations parmi ses clients. Contribution precise et part liee a l'IA non quantifiees."),
    "0001280452": ("ENTRE", "vend", "etablie", "7c4b6471323af9d2c6ca2d85",
        "Convertisseurs DC/DC utilises notamment dans les serveurs CPU cloud et sur site, systemes IA et memoires. Offre de composants pour capacites de calcul explicite, retrouvee grace a l'extraction du sigle AI."),
    "0001274494": ("DOUTEUX", "fournit", "prospective_a_confirmer", "",
        "L'expansion des centres de donnees et de l'IA elargit les acheteurs potentiels de modules solaires ; le passage ne documente pas une vente ou un contrat propre a ce marche. Opportunite, pas exposition realisee demontree."),
    "0001373715": ("DOUTEUX", "investit", "engagement_ou_developpement_documente", "8a15fdecd41a6324939ebf28",
        "Engagement contractuel de 1,9 milliard de dollars pour etendre les centres de donnees. La capacite propre a l'IA n'est pas isolee de l'hebergement general de la plateforme ; cette frontiere motive le doute, pas le statut d'editeur."),
    "0000796343": ("DOUTEUX", "investit", "indeterminee", "151ff930e5850ea4a201ea53",
        "Couts d'entrainement IA et de centres de donnees dans la R&D, et couts d'inference dans l'exploitation. La source n'isole pas un engagement de capacite d'infrastructure propre ; frontiere avec l'usage applicatif a preciser."),
    "0001751008": ("DOUTEUX", "investit", "indeterminee", "438f61447624befda6f7d574",
        "Couts de centres de donnees associes aux ameliorations du moteur de recommandation Axon AI. Engagement de capacite propre et frontiere entre application et infrastructure insuffisamment isoles."),
    "0002115436": ("DOUTEUX", "fournit", "prospective_a_confirmer", "0f2add9fff4819ed9af4fb35",
        "Le rapport du predecesseur verifie relie la demande energetique possible a l'expansion des centres IA, sans isoler dans le passage une fourniture ou un contrat actuel propre a ce marche. Redomiciliation verifiee, pas substitution arbitraire de societe."),
}


def lire(path):
    with path.open(encoding="utf-8-sig", newline="") as fichier:
        return list(csv.DictReader(fichier))


def normaliser(s):
    return re.sub(r"\s+", " ", s).strip()


def main():
    lignes = lire(REGISTRE)
    if any(r.get("revue_version") == VERSION for r in lignes):
        raise SystemExit("Revision deja appliquee : aucune reecriture.")
    sources = {r["cik"]: r for r in lire(ROOT / "data/raw/filings_termes.csv")}
    corpus = lire(ROOT / "data/raw/filings_phrases.csv")
    passages = {(r["cik"], r["phrase_id"]): r for r in corpus}
    textes = {cik: (ROOT / r["cache_metadata"]).with_suffix(".txt").read_text(encoding="utf-8")
              for cik, r in sources.items() if r.get("cache_metadata")}
    journal = []
    for row in lignes:
        avant = row.copy()
        cik = row["cik"]
        source = sources[cik]
        pid = CITATIONS.get(cik, "")
        if cik in REVISIONS:
            verdict, canal, maturite, preuve, motif = REVISIONS[cik]
            row.update(verdict=verdict, canal=canal, maturite_exposition=maturite, motif=motif)
            pid = preuve or pid
        if pid:
            row["phrase_decisive"] = passages[(cik, pid)]["phrase"]
        # Quatre citations de contexte integral relues, hors segmentation.
        if cik == "0001996810":
            texte = textes[cik]
            debut = texte.index("We also continue to benefit from higher growth in orders from other")
            fin = texte.index("existing grid infrastructure.", debut) + len("existing grid infrastructure.")
            row["phrase_decisive"] = texte[debut:fin]
        if cik == "0000006951":
            row["phrase_decisive"] = textes[cik][126291:127020]
            row["motif"] = "Ventes 2025 d'equipements semi-conducteurs soutenues par les investissements effectifs des clients en capacites et technologies ; perspectives reliees a l'IA, aux centres de donnees et aux memoires avancees. La part IA des ventes n'est pas isolee."
        if cik == "0000004904":
            row["phrase_decisive"] = textes[cik].splitlines()[1407]
            row["motif"] = "Achat de 100 MW de piles a combustible en novembre 2024 ; offre aux centres de donnees et grandes charges, avec deux contrats totalisant environ 98 MW approuves en mai 2025. Engagement identifie, sans assimiler toute la capacite a l'IA."
            row["maturite_exposition"] = "engagement_ou_developpement_documente"
        if cik == "0001692819":
            row["phrase_decisive"] = textes[cik].splitlines()[1076]
            row["motif"] = "Contrat de fourniture electrique de vingt ans signe avec AWS pour 1 200 MW ; livraison annoncee a partir de fin 2027, plein volume en 2032. Engagement commercial etabli, pas livraison deja realisee."
            row["maturite_exposition"] = "engagement_ou_developpement_documente"
        if cik == "0000820313":
            row["motif"] = "La croissance des ventes IT datacom est explicitement reliee notamment a la demande de produits IA, reseaux, serveurs et cloud. Le poste entier n'est pas une part de chiffre d'affaires IA."
        # Une citation partielle de phrase peut etre completee par son contexte
        # exact en cache, sans modifier sa signification (cas Deckers).
        if cik == "0000910521":
            texte = textes[cik]
            debut = texte.index("We and our third-party service providers are increasingly using AI,")
            fin = texte.index(".", debut) + 1
            row["phrase_decisive"] = texte[debut:fin]
        row.update({c: source.get(c, "") for c in ("nom", "symboles", "secteur", "sous_secteur", "source_cik", "source_kind", "source_verification_url")})
        row["source_url"] = source.get("source_url", "")
        row["depot"] = source.get("depot", "")
        row["degre"] = "non_quantifie" if row["verdict"] in ("ENTRE", "DOUTEUX") else ""
        row["couverture_source"] = source.get("couverture", "")
        row["preuve_texte_sha256"] = source.get("texte_sha256", "")
        row["nombre_passages_disponibles"] = source.get("nb_passages", "0")
        row["statut_revue"] = "revue_ciblee_extraits" if row["phrase_decisive"] else "revue_insuffisante_sans_preuve_decisive"
        row["limite_preuve"] = "Revue ciblee assistee de passages et de contextes, pas lecture integrale du rapport. Tous les CIK ont ete reexamines ; la couverture complete du vocabulaire ne prouve pas l'exhaustivite des expositions economiques."
        row["revue_version"] = VERSION
        citation = normaliser(row["phrase_decisive"])
        texte = normaliser(textes.get(cik, ""))
        row["citation_debut_normalise"] = str(texte.index(citation)) if citation and citation in texte else ""
        row["citation_fin_normalise"] = str(texte.index(citation) + len(citation)) if citation and citation in texte else ""
        row["normalisation_citation"] = "espaces_unicode_reduits_v1"
        row["phrase_id"] = next((r["phrase_id"] for r in corpus if r["cik"] == cik and normaliser(r["phrase"]) == citation), "")
        if row["verdict"] != "A_EXAMINER" and not row["citation_debut_normalise"]:
            raise ValueError(f"Citation non retrouvee pour {cik}")
        if row != avant:
            journal.append({"cik": cik, "nom": row["nom"], "avant": avant, "apres": row.copy()})
    sortie_journal = ROOT / "data/review/journal_revision_20260905.json"
    if sortie_journal.exists():
        raise SystemExit("Journal deja existant : revision refusee.")
    sortie_journal.write_text(json.dumps(journal, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    colonnes = list(dict.fromkeys(c for row in lignes for c in row))
    with REGISTRE.open("w", encoding="utf-8", newline="") as fichier:
        writer = csv.DictWriter(fichier, fieldnames=colonnes)
        writer.writeheader()
        writer.writerows(lignes)
    from collections import Counter
    print(Counter(r["verdict"] for r in lignes))


if __name__ == "__main__":
    main()
