"""Collecte des cours du groupe témoin : les entreprises classées SORT.

Exécution : python -m src.collecter_temoin
Un fichier déjà présent n'est jamais retéléchargé ; le manifeste est réécrit
à partir des fichiers présents. Les cours sont coupés à la période d'étude,
du 1er décembre 1999 à la dernière séance du calendrier de l'étape 2, et
compressés : le dépôt garde ainsi 58 Mo au lieu de 395 Mo.

Ces cours n'ont pas reçu les contrôles de l'étape 2 : aucune seconde source,
aucune correction manuelle. Les limites sont écrites dans le manifeste.
"""
from pathlib import Path
from datetime import datetime, timezone
import gzip
import json
import time

import pandas as pd

from src.empreintes import empreinte

RACINE = Path(__file__).resolve().parents[1]
DOSSIER = RACINE / "data/raw/prix_temoin"
MANIFESTE = RACINE / "data/raw/prix_temoin_manifest.json"
COLONNES = ["Open", "High", "Low", "Close", "Adj Close", "Volume", "Dividends", "Stock Splits"]
DEBUT = "1999-12-01"


def ecrire_gz(texte, chemin):
    """Garde l'en-tête et les lignes de la période ; gzip sans date, donc reproductible."""
    lignes = texte.splitlines(keepends=True)
    garde = [lignes[0]] + [l for l in lignes[1:] if l[:10] >= DEBUT]
    chemin.write_bytes(gzip.compress("".join(garde).encode("utf-8"), mtime=0))


def symboles_sort(racine=RACINE):
    decisions = pd.read_csv(racine / "data/review/decisions_selection.csv", dtype=str)
    sort = decisions[decisions.verdict == "SORT"]
    return sorted({s.replace(".", "-") for liste in sort.symboles for s in liste.split("|")})


def collecter(racine=RACINE):
    import yfinance as yf

    fin = pd.read_csv(racine / "data/raw/calendrier_bourse.csv").date.astype(str).max()
    DOSSIER.mkdir(parents=True, exist_ok=True)
    echecs = []
    for symbole in symboles_sort(racine):
        chemin = DOSSIER / f"{symbole}.csv.gz"
        if chemin.exists():
            continue
        try:
            histo = yf.Ticker(symbole).history(period="max", auto_adjust=False)
        except Exception as erreur:
            echecs.append({"symbole": symbole, "motif": f"{type(erreur).__name__} : {erreur}"[:200]})
            continue
        if histo.empty:
            echecs.append({"symbole": symbole, "motif": "aucune donnee"})
            continue
        histo = histo[COLONNES]
        histo.index.name = "date"
        histo = histo[histo.index.strftime("%Y-%m-%d") <= fin]
        histo["symbole"] = symbole
        ecrire_gz(histo.to_csv(lineterminator="\n"), chemin)
        time.sleep(0.3)

    fichiers = sorted(DOSSIER.glob("*.csv.gz"))
    manifeste = {
        "produit_le": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source_prix": "Yahoo Finance, via la bibliotheque yfinance",
        "perimetre": "entreprises au verdict SORT de data/review/decisions_selection.csv",
        "fin": fin,
        "limites": [
            "Aucune seconde source ni correction manuelle, contrairement aux titres du theme.",
            "Composition du S&P 500 de 2026 : meme biais de survie que le theme.",
            "Yahoo Finance n est pas une source officielle.",
        ],
        "echecs": echecs,
        "debut": DEBUT,
        "prix": [{"fichier": p.name, "lignes": gzip.decompress(p.read_bytes()).count(b"\n") - 1,
                  "sha256": empreinte(p)} for p in fichiers],
    }
    MANIFESTE.write_text(json.dumps(manifeste, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return manifeste


if __name__ == "__main__":
    m = collecter()
    print(len(m["prix"]), "fichiers,", len(m["echecs"]), "echecs")
    for e in m["echecs"]:
        print(" -", e["symbole"], ":", e["motif"])
