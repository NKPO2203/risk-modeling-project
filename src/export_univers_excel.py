"""Préparer l'export Excel depuis les résultats corrigés, avec jointures par CIK.

L'historique Yahoo existant est une indication documentaire non vérifiée :
sa première date disponible n'est pas une date d'introduction en bourse.
L'écriture XLSX est confiée au moteur JavaScript artifact-tool ; --json-only
permet de préparer les données sans ce moteur optionnel.
"""
from pathlib import Path
import argparse
import json
import os
import subprocess

import pandas as pd

RACINE = Path(__file__).resolve().parents[1]
SORTIE = RACINE / "outputs/01a0708c-acb3-72c2-885a-9b76b6070a14/univers_retenu.xlsx"


def construire():
    def lire(path):
        return pd.read_csv(RACINE / path, dtype={"cik": str, "CIK": str}, keep_default_na=False)
    univers = lire("data/processed/univers_retenu.csv")
    corro = lire("data/processed/corroboration.csv")
    const = lire("data/raw/sp500_constituents.csv")
    const["CIK"] = const["CIK"].str.zfill(10)
    infos = const.groupby("CIK", as_index=False).agg(
        fondee=("Founded", "first"), entree_indice=("Date added", "min")).rename(columns={"CIK": "cik"})
    colonnes_comptes = ["cik", "corroboration", "couverture_comptes",
                       "mult_ventes", "mult_capex", "mult_recherche",
                       "base_periodes_ventes", "base_periodes_capex", "base_periodes_recherche"]
    t = univers.merge(infos, on="cik", how="left", validate="one_to_one")
    t = t.merge(corro.reindex(columns=colonnes_comptes), on="cik", how="left", validate="one_to_one")
    t["ticker"] = t.symboles.str.split("|", regex=False).str[0]
    dates = lire("data/raw/premieres_cotations.csv")
    if dates.ticker.duplicated().any():
        raise ValueError("Plusieurs premières dates pour le même symbole.")
    t = t.merge(dates[["ticker", "premiere_cotation"]], on="ticker", how="left", validate="many_to_one")
    t["tickers"] = t.symboles.str.replace("|", " / ", regex=False)
    an_fond = pd.to_numeric(t.fondee.astype(str).str.extract(r"(\d{4})", expand=False), errors="coerce")
    an_hist = pd.to_numeric(t.premiere_cotation.str[:4], errors="coerce")
    t["anteriorite"] = ""
    t.loc[an_hist < an_fond, "anteriorite"] = "à vérifier : historique antérieur à la fondation indiquée"
    t["source_historique"] = t.premiere_cotation.notna().map({
        True: "Yahoo Finance ; fichier premieres_cotations.csv ; date de collecte non documentée",
        False: "non collecté dans le fichier existant"})
    cols = {
        "ticker": "Ticker", "tickers": "Tickers", "nom": "Entreprise", "secteur": "Secteur",
        "sous_secteur": "Sous-secteur", "canal": "Canal", "degre": "Degré",
        "maturite_exposition": "Maturité de l'exposition", "corroboration": "Mouvement comptable",
        "couverture_comptes": "Couverture comptable",
        "premiere_cotation": "Première date d'historique Yahoo",
        "anteriorite": "Antériorité à vérifier", "fondee": "Fondation indiquée",
        "entree_indice": "Entrée dans l'indice", "motif": "Motif retenu", "cik": "CIK",
        "depot": "Dépôt de la preuve", "source_url": "Source de la preuve",
        "limite_preuve": "Limite de la preuve", "source_historique": "Source de la date d'historique",
        "mult_ventes": "Multiple des ventes", "mult_capex": "Multiple de l'investissement",
        "mult_recherche": "Multiple de la recherche",
        "base_periodes_ventes": "Référence des ventes",
        "base_periodes_capex": "Référence de l'investissement",
        "base_periodes_recherche": "Référence de la recherche",
    }
    t = t.reindex(columns=cols).rename(columns=cols)
    for col in ("Multiple des ventes", "Multiple de l'investissement", "Multiple de la recherche"):
        t[col] = pd.to_numeric(t[col], errors="coerce")
    return t


def payload():
    t = construire()
    tris = {"Par anciennete": ["Première date d'historique Yahoo", "Entreprise"],
            "Par secteur": ["Secteur", "Entreprise"], "Par canal": ["Canal", "Entreprise"]}
    sheets = {}
    for nom, cles in tris.items():
        tri = t.sort_values(cles, ascending=nom != "Par anciennete", na_position="last")
        sheets[nom] = json.loads(tri.to_json(orient="values", force_ascii=False))
    return {"columns": list(t.columns), "sheets": sheets,
            "summary": json.loads((RACINE / "data/processed/etat_projet.json").read_text(encoding="utf-8")),
            "snapshot": "2026-09-05", "input_workbook": str(RACINE / "univers_82.xlsx")}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=SORTIE)
    parser.add_argument("--json-only", action="store_true")
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    chemin_json = args.output.with_suffix(".json")
    chemin_json.write_text(json.dumps(payload(), ensure_ascii=False, indent=2, allow_nan=False), encoding="utf-8")
    if args.json_only:
        print(chemin_json)
        return
    node = os.environ.get("NODE_EXECUTABLE", "node")
    subprocess.run([node, str(RACINE / "src/export_univers_excel.mjs"),
                    str(chemin_json), str(args.output)], check=True, cwd=RACINE)
    print(args.output)


if __name__ == "__main__":
    main()
