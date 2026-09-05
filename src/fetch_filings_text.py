"""Collecte SEC traçable ; extraction exhaustive du vocabulaire, sans plafond.

Sans argument : reproduction hors ligne. --refresh consulte la SEC ; --refresh
--resume reprend les métadonnées en cache. Le cache conserve HTML, texte visible,
URL, accession, dates, SHA-256. Publication préparée puis remplacement atomique de
chaque CSV, manifeste en dernier. Une erreur ne détruit aucun succès antérieur.
La couverture du vocabulaire n'est pas le rappel des expositions économiques.
"""
import argparse
import csv
import hashlib
import io
import json
import os
import re
import sys
import tempfile
import threading
import time
import urllib.error
import urllib.request
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from pathlib import Path

from lxml import html

RACINE = Path(__file__).resolve().parents[1]
UA = "AI-Concentration-Risk-Research josuenkpoman@gmail.com"
VERSION = "2.0.1"
# La normalisation HTML n'a pas changé : un nouvel extracteur de vocabulaire
# peut réutiliser le même texte canonique sans retélécharger ni modifier le HTML.
VERSION_TEXTE = "2.0.0"
PAUSE = 0.2  # Maximum global : cinq départs de requête par seconde.
ABSENCE_10K = "aucun 10-K au CIK courant; prédécesseur non substitué sans vérification"
# Source lue le 05/09/2026 : successeur registrant après redomiciliation, échange
# 1 pour 1. Aucun héritage automatique n'est autorisé pour une vraie scission.
PREDECESSEURS_VERIFIES = {
    "0002115436": {
        "cik": "0000034088",
        "source_url": "https://www.sec.gov/Archives/edgar/data/2115436/000119312526291990/d71068d8k12b.htm",
        "motif": "Redomiciliation au 01/07/2026 ; même groupe, successeur registrant, actions 1 pour 1",
        "verifie_le": "2026-09-05",
    }
}
TERMES = {
    "intelligence_artificielle": r"artificial\s+intelligence",
    "ia_sigle": r"\bai\b",
    "ia_generative": r"generative\s+ai",
    "apprentissage_automatique": r"machine\s+learning",
    "centre_de_donnees": r"data\s*cent(?:er|re)",
    "hyperscale": r"hyperscal",
    "calcul_accelere": r"accelerated\s+computing",
    "processeur_graphique": r"\bgpus?\b|graphics\s+processing\s+unit",
    "calcul_haute_performance": r"high[-\s]+performance\s+computing",
    "grand_modele_de_langage": r"large\s+language\s+model|foundation\s+model",
    "reseau_de_neurones": r"neural\s+network",
    "refroidissement_liquide": r"liquid\s+cooling",
    "infrastructure_cloud": r"cloud\s+infrastructure",
}
MOTIFS = {nom: re.compile(motif, re.IGNORECASE) for nom, motif in TERMES.items()}
COL_TERMES = ["cik", "nom", "symboles", "secteur", "sous_secteur", "date_depot",
    "depot", "taille_texte"] + list(TERMES) + ["source_url", "report_date", "source_cik", "source_kind", "source_verification_url",
    "couverture", "texte_complet_cache", "texte_sha256", "html_sha256", "nb_passages",
    "nb_occurrences_declencheuses", "nb_occurrences_extraites", "couverture_occurrences",
    "cache_metadata", "extraction_version", "statut_recuperation"]
COL_PHRASES = ["cik", "nom", "symboles", "secteur", "date_depot", "termes", "phrase",
    "depot", "source_url", "source_cik", "source_kind", "source_verification_url", "phrase_id", "debut", "fin", "offsets_json", "contexte_avant",
    "contexte_apres", "type_passage", "couverture", "texte_sha256"]
COL_LOG = ["cik", "nom", "probleme", "conservation", "depot"]


def maintenant():
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def empreinte(data):
    return hashlib.sha256(data).hexdigest()


def ecrire_atomique(chemin, data):
    """Prépare, synchronise, remplace ; conserve l'ancien en cas d'échec."""
    chemin = Path(chemin)
    chemin.parent.mkdir(parents=True, exist_ok=True)
    nom_temp = None
    try:
        with tempfile.NamedTemporaryFile(dir=chemin.parent, prefix=chemin.name + ".",
                                         suffix=".tmp", delete=False) as fichier:
            nom_temp = fichier.name
            fichier.write(data)
            fichier.flush()
            os.fsync(fichier.fileno())
        os.replace(nom_temp, chemin)
    finally:
        if nom_temp and os.path.exists(nom_temp):
            os.unlink(nom_temp)


def ecrire_json(chemin, contenu):
    ecrire_atomique(chemin, (json.dumps(contenu, ensure_ascii=False, indent=2,
                                      sort_keys=True) + "\n").encode("utf-8"))


def lire_csv(chemin):
    if not Path(chemin).exists():
        return []
    with open(chemin, encoding="utf-8-sig", newline="") as fichier:
        return list(csv.DictReader(fichier))


def csv_bytes(lignes, colonnes):
    flux = io.StringIO(newline="")
    sortie = csv.DictWriter(flux, fieldnames=colonnes, extrasaction="ignore", lineterminator="\n")
    sortie.writeheader()
    sortie.writerows(lignes)
    return flux.getvalue().encode("utf-8")


class ClientSEC:
    def __init__(self):
        self.verrou = threading.Lock()
        self.dernier = 0.0

    def obtenir(self, url):
        for essai in range(3):
            with self.verrou:
                attente = PAUSE - (time.monotonic() - self.dernier)
                if attente > 0:
                    time.sleep(attente)
                self.dernier = time.monotonic()
            try:
                requete = urllib.request.Request(url, headers={"User-Agent": UA,
                                                              "Accept-Encoding": "identity"})
                with urllib.request.urlopen(requete, timeout=45) as reponse:
                    return reponse.read()
            except urllib.error.HTTPError as exc:
                if exc.code not in (429, 500, 502, 503, 504) or essai == 2:
                    raise
            except (urllib.error.URLError, TimeoutError):
                if essai == 2:
                    raise
            time.sleep(2 ** (essai + 1))


def rapports_des_donnees(rec, cik):
    resultat = []
    for i, forme in enumerate(rec.get("form", [])):
        if forme != "10-K" or not rec["primaryDocument"][i]:
            continue
        depot = rec["accessionNumber"][i]
        dates = rec.get("reportDate", [])
        resultat.append({"source_cik": cik, "depot": depot, "date_depot": rec["filingDate"][i],
            "report_date": dates[i] if i < len(dates) else "",
            "source_url": f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/"
                          f"{depot.replace('-', '')}/{rec['primaryDocument'][i]}"})
    return resultat


def dernier_rapport_annuel(client, cik, cache, resume=False):
    fichier = cache / "submissions" / f"CIK{cik}.json"
    fichier_meta = fichier.with_suffix(".meta.json")
    if resume and fichier.exists() and fichier_meta.exists():
        contenu = fichier.read_bytes()
        meta = json.loads(fichier_meta.read_text(encoding="utf-8"))
        if empreinte(contenu) != meta["sha256"]:
            raise ValueError(f"Cache submissions corrompu : {cik}")
        donnees = json.loads(contenu)
    else:
        url = f"https://data.sec.gov/submissions/CIK{cik}.json"
        contenu = client.obtenir(url)
        donnees = json.loads(contenu)
        ecrire_atomique(fichier, contenu)
        ecrire_json(fichier_meta, {"source_url": url, "sha256": empreinte(contenu),
                                  "fetched_at": maintenant()})
    candidats = rapports_des_donnees(donnees.get("filings", {}).get("recent", {}), cik)
    if not candidats:
        for ancien in donnees.get("filings", {}).get("files", []):
            nom = ancien["name"]
            fichier_ancien = cache / "submissions" / nom
            if resume and fichier_ancien.exists():
                rec = json.loads(fichier_ancien.read_text(encoding="utf-8"))
            else:
                contenu_ancien = client.obtenir("https://data.sec.gov/submissions/" + nom)
                rec = json.loads(contenu_ancien)
                ecrire_atomique(fichier_ancien, contenu_ancien)
            candidats.extend(rapports_des_donnees(rec, cik))
    if candidats:
        return max(candidats, key=lambda x: (x["date_depot"], x["depot"]))
    if cik in PREDECESSEURS_VERIFIES:
        identite = PREDECESSEURS_VERIFIES[cik]
        preuve = cache / "identity_proofs" / f"{cik}.html"
        preuve_meta = preuve.with_suffix(".json")
        if not (resume and preuve.exists() and preuve_meta.exists()):
            contenu = client.obtenir(identite["source_url"])
            ecrire_atomique(preuve, contenu)
            ecrire_json(preuve_meta, {**identite, "sha256": empreinte(contenu), "fetched_at": maintenant()})
        if empreinte(preuve.read_bytes()) != json.loads(preuve_meta.read_text(encoding="utf-8"))["sha256"]:
            raise ValueError("Preuve de continuité d'identité corrompue")
        info = dernier_rapport_annuel(client, identite["cik"], cache, resume)
        if info:
            info["source_kind"] = "10-K_predecesseur_verifie"
            info["source_verification_url"] = identite["source_url"]
        return info
    return None


def texte_du_html(contenu):
    """Texte visible sans plafond ; HTML d'origine conservé, tableaux compris."""
    document = html.fromstring(contenu)
    for element in list(document.iter()):
        if not isinstance(element.tag, str):
            continue
        nom = element.tag.lower().split("}")[-1]
        style = re.sub(r"\s+", "", element.get("style", "").lower())
        if (nom in ("script", "style", "noscript", "ix:header", "ix:hidden")
                or element.get("hidden") is not None
                or "display:none" in style or "visibility:hidden" in style):
            if element.getparent() is not None:
                element.drop_tree()
    blocs = {"p", "div", "br", "li", "tr", "h1", "h2", "h3", "h4", "h5", "h6"}
    for element in document.iter():
        if not isinstance(element.tag, str):
            continue
        nom = element.tag.lower().split("}")[-1]
        if nom in blocs:
            element.tail = "\n" + (element.tail or "")
        elif nom in ("td", "th"):
            element.tail = " " + (element.tail or "")
    lignes = [re.sub(r"[^\S\n]+", " ", ligne).strip()
              for ligne in document.text_content().splitlines()]
    return "\n".join(ligne for ligne in lignes if ligne)


def bornes_phrases(texte):
    debut = 0
    for separateur in re.finditer(r"(?<=[.!?])\s+|\n+", texte):
        if separateur.start() > debut:
            yield debut, separateur.start()
        debut = separateur.end()
    if debut < len(texte):
        yield debut, len(texte)


def analyser(texte, depot=""):
    """Tous les motifs déclenchent ; longs passages fenêtrés autour de chaque hit.

    IDs : SHA-256(accession + NUL + texte exact), 24 caractères. Les répétitions
    textuelles ont une ligne et plusieurs offsets (en caractères, fin exclue).
    """
    occurrences = sorted((m.start(), m.end(), nom) for nom, motif in MOTIFS.items()
                         for m in motif.finditer(texte))
    comptes = {nom: 0 for nom in TERMES}
    for _, _, nom in occurrences:
        comptes[nom] += 1
    passages = {}
    curseur = 0

    def ajouter(a, b, type_passage):
        phrase = texte[a:b]
        if phrase in passages:
            passages[phrase]["_offsets"].append([a, b])
            return
        passages[phrase] = {"phrase": phrase,
            "phrase_id": empreinte((depot + "\0" + phrase).encode("utf-8"))[:24],
            "termes": "|".join(nom for nom, motif in MOTIFS.items() if motif.search(phrase)),
            "debut": a, "fin": b, "_offsets": [[a, b]],
            "contexte_avant": texte[max(0, a - 300):a],
            "contexte_apres": texte[b:min(len(texte), b + 300)],
            "type_passage": type_passage}

    for debut, fin in bornes_phrases(texte):
        touches = []
        while curseur < len(occurrences) and occurrences[curseur][0] < fin:
            touche = occurrences[curseur]
            if touche[0] >= debut and touche[1] <= fin:
                touches.append(touche)
            curseur += 1
        if not touches:
            continue
        if fin - debut <= 2400:
            plages = [[debut, fin]]
        else:
            plages = []
            for a, b, _ in touches:
                gauche, droite = max(debut, a - 550), min(fin, b + 550)
                while gauche > debut and not texte[gauche - 1].isspace():
                    gauche -= 1
                while droite < fin and not texte[droite].isspace():
                    droite += 1
                if plages and gauche <= plages[-1][1]:
                    plages[-1][1] = max(plages[-1][1], droite)
                else:
                    plages.append([gauche, droite])
        for a, b in plages:
            ajouter(a, b, "phrase" if fin - debut <= 2400 else "fenetre_longue")
    plages_couvertes = [plage for passage in passages.values() for plage in passage["_offsets"]]
    # Cas des motifs traversant une frontière de bloc, par exemple data\ncenter.
    for a, b, _ in occurrences:
        if not any(x <= a and b <= y for x, y in plages_couvertes):
            x, y = max(0, a - 550), min(len(texte), b + 550)
            ajouter(x, y, "fenetre_frontiere")
            plages_couvertes.append([x, y])
    couverts = sum(any(x <= a and b <= y for x, y in plages_couvertes)
                  for a, b, _ in occurrences)
    if couverts != len(occurrences):
        raise ValueError("Occurrences sans extrait : extraction interrompue")
    resultat = sorted(passages.values(), key=lambda p: (p["debut"], p["phrase_id"]))
    for passage in resultat:
        passage["offsets_json"] = json.dumps(passage.pop("_offsets"), separators=(",", ":"))
    return comptes, resultat, couverts


def chemins_cache(cache, info):
    base = cache / info["source_cik"] / info["depot"]
    return base.with_suffix(".html"), base.with_suffix(".txt"), base.with_suffix(".json")


def rapport_cache(cache, info):
    fichier_html, fichier_texte, fichier_meta = chemins_cache(cache, info)
    meta = json.loads(fichier_meta.read_text(encoding="utf-8"))
    contenu, texte_brut = fichier_html.read_bytes(), fichier_texte.read_bytes()
    if empreinte(contenu) != meta["html_sha256"] or empreinte(texte_brut) != meta["texte_sha256"]:
        raise ValueError(f"Empreinte invalide : cache {info['depot']}")
    if meta["depot"] != info["depot"] or meta["source_cik"] != info["source_cik"]:
        raise ValueError("Identité du cache incohérente")
    if meta.get("text_parser_version", meta.get("extraction_version")) != VERSION_TEXTE:
        raise ValueError("Version du parseur différente ; refresh requis")
    # Le texte canonique fait partie du cache audité : les deux empreintes sont
    # contrôlées. Reparser systématiquement 500 arbres HTML n'est pas nécessaire.
    return texte_brut.decode("utf-8"), meta


def dernier_cache(cache, cik):
    candidats = [json.loads(chemin.read_text(encoding="utf-8"))
                 for chemin in (cache / cik).glob("*.json")]
    if not candidats and cik in PREDECESSEURS_VERIFIES:
        return dernier_cache(cache, PREDECESSEURS_VERIFIES[cik]["cik"])
    return max(candidats, key=lambda x: (x["date_depot"], x["depot"])) if candidats else None


def charger_rapport(client, cache, info):
    fichiers = chemins_cache(cache, info)
    if all(f.exists() for f in fichiers):
        try:
            return rapport_cache(cache, info)
        except ValueError:
            # Un refresh explicite peut réparer un cache corrompu ou périmé.
            pass
    contenu = client.obtenir(info["source_url"])
    texte = texte_du_html(contenu)
    if len(texte) < 10000:
        raise ValueError(f"Document anormalement court ({len(texte)} caractères), non publié")
    texte_brut = texte.encode("utf-8")
    meta = {**info, "fetched_at": maintenant(), "html_sha256": empreinte(contenu),
            "texte_sha256": empreinte(texte_brut), "html_bytes": len(contenu),
            "taille_texte": len(texte), "extraction_version": VERSION,
            "text_parser_version": VERSION_TEXTE,
            "texte_definition": "HTML visible, scripts/styles/blocs cachés iXBRL retirés, tableaux conservés"}
    ecrire_atomique(fichiers[0], contenu)
    ecrire_atomique(fichiers[1], texte_brut)
    ecrire_json(fichiers[2], meta)  # marqueur de cache complet, publié en dernier
    return texte, meta


def entreprises_depuis_csv(chemin):
    groupes = defaultdict(list)
    for ligne in lire_csv(chemin):
        groupes[ligne["CIK"].zfill(10)].append(ligne)
    return [{"cik": cik, "nom": lignes[0]["Security"],
             "symboles": "|".join(sorted({ligne["Symbol"] for ligne in lignes})),
             "secteur": lignes[0]["GICS Sector"],
             "sous_secteur": lignes[0]["GICS Sub-Industry"]}
            for cik, lignes in sorted(groupes.items())]


def resultat_complet(entreprise, texte, meta, cache, racine):
    comptes, passages, couverts = analyser(texte, meta["depot"])
    total = sum(comptes.values())
    infos = {k: meta[k] for k in ("depot", "date_depot", "source_url", "source_cik",
                                "report_date", "html_sha256", "texte_sha256")}
    infos["source_kind"] = meta.get("source_kind", "10-K_entite_courante")
    infos["source_verification_url"] = meta.get("source_verification_url", "")
    terme = {**entreprise, **infos, "taille_texte": len(texte), **comptes,
             "couverture": "vocabulaire_complet", "texte_complet_cache": "oui",
             "nb_passages": len(passages), "nb_occurrences_declencheuses": total,
             "nb_occurrences_extraites": couverts,
             "couverture_occurrences": "1" if total else "sans_occurrence",
             "cache_metadata": chemins_cache(cache, meta)[2].relative_to(racine).as_posix(),
             "extraction_version": VERSION, "statut_recuperation": "cache_verifie"}
    phrases = [{**entreprise, **infos, **passage, "couverture": "vocabulaire_complet"}
               for passage in passages]
    return terme, phrases


def conserver_historique(entreprise, ancien, phrases_anciennes, raison):
    if not ancien or not ancien.get("depot"):
        return ({**entreprise, "couverture": "aucun_document", "texte_complet_cache": "non",
                 "statut_recuperation": raison}, [])
    if ancien.get("couverture") == "vocabulaire_complet":
        conservation = {**ancien, **entreprise, "statut_recuperation": raison}
        if raison == "non_actualise":
            conservation["couverture"] = "rapport_complet_non_verifie"
            conservation["texte_complet_cache"] = "a_verifier"
        return conservation, phrases_anciennes
    terme = {**ancien, **entreprise, "source_cik": entreprise["cik"],
             "couverture": "extraits_historiques_tronques", "texte_complet_cache": "non",
             "nb_passages": len(phrases_anciennes), "extraction_version": "1_historique",
             "statut_recuperation": raison}
    phrases = []
    for passage in phrases_anciennes:
        texte = passage["phrase"]
        phrases.append({**passage, "depot": ancien["depot"],
            "source_url": ancien.get("source_url", ""),
            "phrase_id": empreinte((ancien["depot"] + "\0" + texte).encode("utf-8"))[:24],
            "couverture": "extraits_historiques_tronques", "type_passage": "historique"})
    return terme, phrases


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--refresh", action="store_true", help="Consulter la SEC")
    parser.add_argument("--offline", action="store_true", help="Reproduire le cache (défaut)")
    parser.add_argument("--resume", action="store_true", help="Reprendre les submissions en cache")
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--cik", action="append", help="Actualiser ces CIK, conserver les autres")
    parser.add_argument("--root", type=Path, default=RACINE)
    args = parser.parse_args(argv)
    if args.offline and args.refresh:
        parser.error("--offline et --refresh sont exclusifs")
    if not 1 <= args.workers <= 6:
        parser.error("--workers doit être entre 1 et 6")
    racine = args.root.resolve()
    raw, cache = racine / "data" / "raw", racine / "data" / "raw" / "filings_text"
    entreprises = entreprises_depuis_csv(raw / "sp500_constituents.csv")
    anciens = {ligne["cik"].zfill(10): ligne for ligne in lire_csv(raw / "filings_termes.csv")}
    anciens_logs = {ligne["cik"].zfill(10): ligne for ligne in lire_csv(raw / "filings_log.csv")}
    phrases_anciennes = defaultdict(list)
    for ligne in lire_csv(raw / "filings_phrases.csv"):
        phrases_anciennes[ligne["cik"].zfill(10)].append(ligne)
    selection = {cik.zfill(10) for cik in args.cik} if args.cik else None
    if selection and selection - {e["cik"] for e in entreprises}:
        parser.error("--cik contient un identifiant absent de l'univers courant")
    client = ClientSEC()

    def traiter(entreprise):
        cik = entreprise["cik"]
        if selection is not None and cik not in selection:
            return conserver_historique(entreprise, anciens.get(cik), phrases_anciennes[cik],
                        anciens.get(cik, {}).get("statut_recuperation", "non_actualise")), anciens_logs.get(cik)
        try:
            if args.refresh:
                info = dernier_rapport_annuel(client, cik, cache, args.resume)
                if info is None:
                    raise LookupError(ABSENCE_10K)
                texte, meta = charger_rapport(client, cache, info)
            else:
                info = dernier_cache(cache, cik)
                if info is None:
                    submissions = cache / "submissions" / f"CIK{cik}.json"
                    meta_sub = submissions.with_suffix(".meta.json")
                    if submissions.exists() and meta_sub.exists():
                        contenu = submissions.read_bytes()
                        if empreinte(contenu) != json.loads(meta_sub.read_text(encoding="utf-8"))["sha256"]:
                            raise ValueError("Cache submissions corrompu")
                        rec = json.loads(contenu).get("filings", {})
                        if not rapports_des_donnees(rec.get("recent", {}), cik) and not rec.get("files", []):
                            raise LookupError(ABSENCE_10K)
                    raise LookupError("aucun rapport intégral en cache")
                texte, meta = rapport_cache(cache, info)
            return resultat_complet(entreprise, texte, meta, cache, racine), None
        except Exception as exc:
            probleme = f"{type(exc).__name__}: {exc}"
            try:
                info = dernier_cache(cache, cik)
                if info is not None:
                    texte, meta = rapport_cache(cache, info)
                    resultat = resultat_complet(entreprise, texte, meta, cache, racine)
                    resultat[0]["statut_recuperation"] = "echec_actualisation_cache_conserve"
                    return resultat, {"cik": cik, "nom": entreprise["nom"], "probleme": probleme,
                                      "conservation": "rapport_complet_anterieur", "depot": meta["depot"]}
            except Exception:
                pass
            resultat = conserver_historique(entreprise, anciens.get(cik), phrases_anciennes[cik], "non_actualise")
            return resultat, {"cik": cik, "nom": entreprise["nom"], "probleme": probleme,
                               "conservation": resultat[0]["couverture"], "depot": resultat[0].get("depot", "")}

    print(f"{len(entreprises)} entreprises ; {'refresh SEC' if args.refresh else 'reproduction hors ligne'}", flush=True)
    termes, phrases, journal = [], [], []
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        travaux = [executor.submit(traiter, entreprise) for entreprise in entreprises]
        for i, travail in enumerate(as_completed(travaux), 1):
            (terme, passages), erreur = travail.result()
            termes.append(terme)
            phrases.extend(passages)
            if erreur:
                journal.append(erreur)
                print(f"  {terme['symboles']}: {erreur['probleme']}", flush=True)
            if i % 25 == 0:
                print(f"  {i}/{len(entreprises)}, {len(journal)} non actualisés, {len(phrases)} passages", flush=True)
    termes.sort(key=lambda ligne: ligne["cik"])
    phrases.sort(key=lambda ligne: (ligne["cik"], int(ligne.get("debut") or 0), ligne["phrase_id"]))
    journal.sort(key=lambda ligne: ligne["cik"])
    fichiers = {"filings_termes.csv": csv_bytes(termes, COL_TERMES),
                "filings_phrases.csv": csv_bytes(phrases, COL_PHRASES),
                "filings_log.csv": csv_bytes(journal, COL_LOG)}
    generation = empreinte(b"".join(fichiers[nom] for nom in sorted(fichiers)))[:20]
    complet = sum(ligne["couverture"] == "vocabulaire_complet" for ligne in termes)
    manifeste = {"schema_version": 1, "extraction_version": VERSION, "generation": generation,
        "entreprises": len(termes), "rapports_complets": complet, "passages": len(phrases),
        "non_actualises": len(journal), "vocabulaire": TERMES,
        "predecesseurs_verifies": PREDECESSEURS_VERIFIES,
        "couverture_definition": "toutes les occurrences des 13 motifs ; pas le rappel économique",
        "offsets_definition": "caractères du texte en cache, début inclus et fin exclue",
        "files": {nom: {"sha256": empreinte(contenu), "bytes": len(contenu)}
                  for nom, contenu in fichiers.items()}}
    snapshot = cache / "generations" / generation
    for nom, contenu in fichiers.items():
        ecrire_atomique(snapshot / nom, contenu)
    ecrire_json(snapshot / "manifest.json", manifeste)
    for nom, contenu in fichiers.items():
        ecrire_atomique(raw / nom, contenu)
    ecrire_json(raw / "filings_manifest.json", manifeste)
    print(f"Publié : {complet}/{len(termes)} rapports complets, {len(phrases)} passages ; génération {generation}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
