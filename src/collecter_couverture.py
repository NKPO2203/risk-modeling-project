"""Collecte des instruments de l'étape 4 : obligations du Trésor et VIX.

Exécution : python -m src.collecter_couverture
Les choix d'instruments sont écrits dans la section VII de
research/plan_projet.md, avant la collecte. Un fichier déjà présent n'est
jamais retéléchargé ; le manifeste est réécrit à partir des fichiers présents.
Les séries sont coupées du 1er janvier 1999, pour disposer d'une année
d'historique avant la période d'étude, à la dernière séance du calendrier de
l'étape 2.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import time

import pandas as pd

from src.empreintes import correspond, empreinte

RACINE = Path(__file__).resolve().parents[1]
DOSSIER = RACINE / "data/raw/couverture"
MANIFESTE = RACINE / "data/raw/couverture_manifest.json"
COLONNES = ["Open", "High", "Low", "Close", "Adj Close", "Volume", "Dividends"]
DEBUT = "1999-01-01"
INSTRUMENTS = {
    "VFITX": "Vanguard Intermediate-Term Treasury Fund, parts Investor : obligations du Tresor a echeance intermediaire",
    "VUSTX": "Vanguard Long-Term Treasury Fund, parts Investor : obligations du Tresor longues",
    "^VIX": "Indice de volatilite implicite a trente jours du S&P 500, CBOE",
    "^PUT": "Indice CBOE S&P 500 PutWrite : vente mensuelle de puts a la monnaie garantie par des bons du Tresor ; "
            "sert au controle du modele de prix des options, ajoute le 28 septembre 2026",
}


def fichier(symbole):
    return DOSSIER / f"{symbole.replace('^', '')}.csv"


def collecter(racine=RACINE):
    import yfinance as yf

    fin = pd.read_csv(racine / "data/raw/calendrier_bourse.csv").date.astype(str).max()
    DOSSIER.mkdir(parents=True, exist_ok=True)
    for symbole in INSTRUMENTS:
        chemin = fichier(symbole)
        if chemin.exists():
            continue
        histo = yf.Ticker(symbole).history(period="max", auto_adjust=False)
        if histo.empty:
            raise RuntimeError(f"Aucune donnee pour {symbole}")
        histo = histo[[c for c in COLONNES if c in histo]]
        histo.index = histo.index.strftime("%Y-%m-%d")
        histo.index.name = "date"
        histo = histo[(histo.index >= DEBUT) & (histo.index <= fin)]
        histo["symbole"] = symbole
        chemin.write_text(histo.to_csv(lineterminator="\n"), encoding="utf-8")
        time.sleep(0.3)

    manifeste = {
        "produit_le": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "commande": "python -m src.collecter_couverture",
        "source": "Yahoo Finance, via la bibliotheque yfinance",
        "debut": DEBUT,
        "fin": fin,
        "limites": [
            "Yahoo Finance n est pas une source officielle ; aucune seconde source.",
            "Adj Close des fonds est la valeur liquidative ajustee des distributions ; "
            "les frais de gestion y sont deja deduits.",
            "Le VIX est un indice, pas un prix d option : il sert a evaluer des options par un modele.",
            "Une nouvelle collecte ne promet pas les memes valeurs ajustees.",
        ],
        "instruments": [{"symbole": s, "description": d, "fichier": fichier(s).name,
                         "lignes": len(pd.read_csv(fichier(s))), "sha256": empreinte(fichier(s))}
                        for s, d in INSTRUMENTS.items()],
    }
    MANIFESTE.write_text(json.dumps(manifeste, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return manifeste


def verifier(racine=RACINE):
    """Vérifie inventaire et empreintes avant tout calcul de l'étape 4."""
    raw = Path(racine) / "data/raw"
    m = json.loads((raw / "couverture_manifest.json").read_text(encoding="utf-8"))
    attendus = {e["fichier"] for e in m["instruments"]}
    if attendus != {p.name for p in (raw / "couverture").glob("*.csv")}:
        raise ValueError("Inventaire des instruments different du manifeste.")
    for e in m["instruments"]:
        if not correspond(raw / "couverture" / e["fichier"], e["sha256"]):
            raise ValueError(f"Empreinte invalide : {e['fichier']}")
    return m


if __name__ == "__main__":
    m = collecter()
    for e in m["instruments"]:
        print(e["symbole"], e["lignes"], "lignes")
