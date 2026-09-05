"""Classement documentaire reproductible, sans decision d'investissement.

Les 500 entreprises (CIK uniques) restent presentes, y compris sans rapport.
Ordre lexicographique : nombre de termes distincts, nombre d'occurrences,
densite par 100 000 caracteres, puis CIK pour departager les ex aequo.
Le sigle AI seul est exclu de ces trois indicateurs, car trop peu specifique.
Le rang sert uniquement a organiser la lecture ; il n'identifie aucune decision.
"""

from pathlib import Path

import pandas as pd

RACINE = Path(__file__).resolve().parents[1]
TERMES = (
    "intelligence_artificielle", "ia_generative", "apprentissage_automatique",
    "centre_de_donnees", "hyperscale", "calcul_accelere", "processeur_graphique",
    "calcul_haute_performance", "grand_modele_de_langage", "reseau_de_neurones",
    "refroidissement_liquide", "infrastructure_cloud",
)


def entreprises_constituantes(path):
    c = pd.read_csv(path, dtype={"CIK": str}, keep_default_na=False)
    c["CIK"] = c["CIK"].str.zfill(10)
    return c.groupby("CIK", as_index=False).agg(
        nom=("Security", "first"),
        symboles=("Symbol", lambda s: "|".join(sorted(set(s)))),
        secteur=("GICS Sector", "first"),
        sous_secteur=("GICS Sub-Industry", "first"),
    ).rename(columns={"CIK": "cik"})


def construire_classement(entreprises, termes):
    t = termes.copy()
    t["cik"] = t["cik"].astype(str).str.zfill(10)
    if t["cik"].duplicated().any():
        raise ValueError("Plusieurs rapports courants pour le meme CIK")
    for col in TERMES:
        if col not in t:
            raise ValueError(f"Comptage absent : {col}")
        t[col] = pd.to_numeric(t[col].replace("", pd.NA), errors="raise")
    t["n_actifs"] = t[list(TERMES)].gt(0).sum(axis=1)
    t["total"] = t[list(TERMES)].sum(axis=1)
    taille = pd.to_numeric(t["taille_texte"].replace("", pd.NA), errors="raise")
    disponible = taille.fillna(0).gt(0)
    t["densite"] = t["total"] * 100_000 / taille.where(disponible)
    t["rapport_disponible"] = disponible.map({True: "oui", False: "non"})
    t.loc[~disponible, ["n_actifs", "total", "densite"]] = pd.NA
    cols = ["cik", "n_actifs", "total", "densite", "rapport_disponible"]
    cols += [c for c in ("depot", "date_depot", "report_date", "source_url",
                         "source_cik", "source_kind", "source_verification_url",
                         "couverture", "statut_recuperation") if c in t]
    r = entreprises.merge(t[cols], on="cik", how="left", validate="one_to_one")
    r["rapport_disponible"] = r["rapport_disponible"].fillna("non")
    # Ne pas confondre rapport absent et rapport comportant zero occurrence.
    r = r.sort_values(["n_actifs", "total", "densite", "cik"],
                      ascending=[False, False, False, True], na_position="last")
    r.insert(0, "rang", range(1, len(r) + 1))
    r["methode_classement"] = "lexicographique_n_actifs_total_densite_cik_v1"
    return r.reset_index(drop=True)


def main():
    raw = RACINE / "data" / "raw"
    t = pd.read_csv(raw / "filings_termes.csv", dtype={"cik": str}, keep_default_na=False)
    r = construire_classement(entreprises_constituantes(raw / "sp500_constituents.csv"), t)
    sortie = RACINE / "data" / "processed" / "classement_texte.csv"
    sortie.parent.mkdir(parents=True, exist_ok=True)
    r.to_csv(sortie, index=False, encoding="utf-8")
    print(f"Classement documentaire : {len(r)} CIK, {(r.rapport_disponible == 'non').sum()} sans rapport")


if __name__ == "__main__":
    main()
