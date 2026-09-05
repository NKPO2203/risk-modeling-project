"""
Extraction du texte des rapports annuels des composantes du S&P 500.

Pour chaque entreprise : on récupère son dernier rapport annuel, on compte les
occurrences d'un vocabulaire opérationnel lié à l'infrastructure de calcul, et
on extrait les phrases qui contiennent ces termes.

Ce script ne juge rien. Il fournit la matière à lire.

Sorties :
    data/raw/filings_termes.csv    une ligne par entreprise, comptages
    data/raw/filings_phrases.csv   une ligne par phrase extraite
    data/raw/filings_log.csv       échecs
"""

import csv
import re
import sys
import time
import warnings
from pathlib import Path

import pandas as pd
import requests
from bs4 import BeautifulSoup

warnings.filterwarnings("ignore")

CONTACT = "josuenkpoman@gmail.com"
UA = f"AI-Concentration-Risk-Research {CONTACT}"

RACINE = Path(__file__).resolve().parents[1]
CONSTITUANTS = RACINE / "data" / "raw" / "sp500_constituents.csv"
F_TERMES = RACINE / "data" / "raw" / "filings_termes.csv"
F_PHRASES = RACINE / "data" / "raw" / "filings_phrases.csv"
F_LOG = RACINE / "data" / "raw" / "filings_log.csv"

PAUSE = 0.12
MAX_PHRASES = 40

# --------------------------------------------------------------------------
# Le vocabulaire cherché.
#
# Volontairement centré sur les mots du métier plutôt que sur l'expression
# "intelligence artificielle". Le cas Eaton a montré que ce dernier terme
# conduit à la conclusion inverse de la réalité : Eaton l'emploie quatre fois,
# uniquement pour parler d'efficacité interne et de risques juridiques, alors
# que ses vingt-quatre mentions de centres de données révèlent une exposition
# forte et documentée par quatre acquisitions.
#
# Les termes marqués \b sont cherchés en mot entier, pour éviter qu'un "ai"
# ne se déclenche dans "said" ou "maintain".
# --------------------------------------------------------------------------

TERMES = {
    "intelligence_artificielle": r"artificial intelligence",
    "ia_sigle": r"\bai\b",
    "ia_generative": r"generative ai",
    "apprentissage_automatique": r"machine learning",
    "centre_de_donnees": r"data\s?cent(?:er|re)",
    "hyperscale": r"hyperscal",
    "calcul_accelere": r"accelerated computing",
    "processeur_graphique": r"\bgpus?\b|graphics processing unit",
    "calcul_haute_performance": r"high[- ]performance computing",
    "grand_modele_de_langage": r"large language model|foundation model",
    "reseau_de_neurones": r"neural network",
    "refroidissement_liquide": r"liquid cooling",
    "infrastructure_cloud": r"cloud infrastructure",
}

# Termes qui déclenchent l'extraction de phrases. On écarte le sigle seul,
# trop bruyant, et on garde le vocabulaire porteur de sens.
TERMES_PHRASES = [
    k for k in TERMES if k not in ("ia_sigle",)
]


def session_sec():
    s = requests.Session()
    s.headers.update({"User-Agent": UA, "Accept-Encoding": "gzip, deflate"})
    return s


def dernier_rapport_annuel(s, cik):
    """Renvoie l'adresse du dernier 10-K, sa date et sa référence de dépôt."""
    r = s.get(
        f"https://data.sec.gov/submissions/CIK{cik}.json",
        headers={"Host": "data.sec.gov"},
        timeout=45,
    )
    if r.status_code != 200:
        return None
    rec = r.json().get("filings", {}).get("recent", {})
    for i, forme in enumerate(rec.get("form", [])):
        if forme == "10-K":
            doc = rec["primaryDocument"][i]
            if not doc:
                continue
            acc = rec["accessionNumber"][i].replace("-", "")
            url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{acc}/{doc}"
            return url, rec["filingDate"][i], rec["accessionNumber"][i]
    return None


def texte_du_document(s, url):
    r = s.get(url, headers={"Host": "www.sec.gov"}, timeout=120)
    if r.status_code != 200:
        return None
    soupe = BeautifulSoup(r.content, "lxml")
    for balise in soupe(["script", "style"]):
        balise.decompose()
    return re.sub(r"\s+", " ", soupe.get_text(" "))


def analyser(texte):
    """Compte les occurrences et extrait les phrases porteuses."""
    bas = texte.lower()
    comptes = {nom: len(re.findall(motif, bas)) for nom, motif in TERMES.items()}

    phrases = []
    if any(comptes[t] for t in TERMES_PHRASES):
        motifs = {t: re.compile(TERMES[t]) for t in TERMES_PHRASES}
        vues = set()
        for phrase in re.split(r"(?<=[.!?]) +", texte):
            if not (60 < len(phrase) < 700):
                continue
            p_bas = phrase.lower()
            touches = [t for t, m in motifs.items() if m.search(p_bas)]
            if not touches:
                continue
            empreinte = p_bas[:120]
            if empreinte in vues:
                continue
            vues.add(empreinte)
            phrases.append((phrase.strip(), "|".join(touches)))
            if len(phrases) >= MAX_PHRASES:
                break

    return comptes, phrases


def verifier_ecriture(chemin):
    try:
        with open(chemin, "a", encoding="utf-8"):
            pass
    except PermissionError:
        print(f"\nARRET : {chemin.name} est verrouille. Ferme-le et relance.\n", file=sys.stderr)
        sys.exit(1)


def main():
    for f in (F_TERMES, F_PHRASES, F_LOG):
        verifier_ecriture(f)

    c = pd.read_csv(CONSTITUANTS, dtype={"CIK": str})
    c["CIK"] = c["CIK"].str.zfill(10)
    entreprises = (
        c.groupby("CIK")
        .agg(
            nom=("Security", "first"),
            symboles=("Symbol", lambda x: "|".join(sorted(x))),
            secteur=("GICS Sector", "first"),
            sous_secteur=("GICS Sub-Industry", "first"),
        )
        .reset_index()
    )

    s = session_sec()
    journal = []

    ft = open(F_TERMES, "w", newline="", encoding="utf-8")
    colonnes_t = ["cik", "nom", "symboles", "secteur", "sous_secteur",
                  "date_depot", "depot", "taille_texte"] + list(TERMES)
    wt = csv.DictWriter(ft, fieldnames=colonnes_t)
    wt.writeheader()

    fp = open(F_PHRASES, "w", newline="", encoding="utf-8")
    wp = csv.DictWriter(fp, fieldnames=["cik", "nom", "symboles", "secteur",
                                        "date_depot", "termes", "phrase"])
    wp.writeheader()

    print(f"{len(entreprises)} entreprises", flush=True)

    for i, ligne in entreprises.iterrows():
        cik = ligne["CIK"]
        try:
            info = dernier_rapport_annuel(s, cik)
            if info is None:
                journal.append({"cik": cik, "nom": ligne["nom"], "probleme": "aucun 10-K trouve"})
                time.sleep(PAUSE)
                continue

            url, date, depot = info
            time.sleep(PAUSE)
            texte = texte_du_document(s, url)
            if not texte:
                journal.append({"cik": cik, "nom": ligne["nom"], "probleme": "document illisible"})
                time.sleep(PAUSE)
                continue

            comptes, phrases = analyser(texte)

            wt.writerow({
                "cik": cik, "nom": ligne["nom"], "symboles": ligne["symboles"],
                "secteur": ligne["secteur"], "sous_secteur": ligne["sous_secteur"],
                "date_depot": date, "depot": depot, "taille_texte": len(texte),
                **comptes,
            })
            for phrase, termes in phrases:
                wp.writerow({
                    "cik": cik, "nom": ligne["nom"], "symboles": ligne["symboles"],
                    "secteur": ligne["secteur"], "date_depot": date,
                    "termes": termes, "phrase": phrase,
                })

        except Exception as exc:
            journal.append({"cik": cik, "nom": ligne["nom"], "probleme": f"{type(exc).__name__}: {exc}"})

        if (i + 1) % 25 == 0:
            ft.flush()
            fp.flush()
            print(f"  {i + 1} entreprises", flush=True)

        time.sleep(PAUSE)

    ft.close()
    fp.close()
    pd.DataFrame(journal).to_csv(F_LOG, index=False, encoding="utf-8")
    print(f"\nTermine. {len(journal)} echecs consignes.", flush=True)


if __name__ == "__main__":
    main()
