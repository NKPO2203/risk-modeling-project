"""
Contrôle de vraisemblance des données financières, sur les 500 entreprises.

Un contrôle manuel sur trois entreprises tirées au sort vérifie que la chaîne
de récupération fonctionne. Il ne prouve rien sur les 497 autres.

Ce script fait l'inverse : il applique à toutes les entreprises des tests que
la réalité économique ne permet pas de violer. Ce qui en sort est ensuite
vérifié à la main, une par une. On ne cherche plus au hasard.

Entrée : data/processed/base_selection.csv
Sortie : data/processed/controle_qualite.csv
"""

from pathlib import Path

import pandas as pd

RACINE = Path(__file__).resolve().parents[1]
ENTREE = RACINE / "data" / "processed" / "base_selection.csv"
SORTIE = RACINE / "data" / "processed" / "controle_qualite.csv"


def main():
    b = pd.read_csv(ENTREE, dtype={"cik": str})
    b = b.sort_values(["cik", "annee"])
    alertes = []

    def signaler(ligne, test, detail):
        alertes.append(
            {
                "cik": ligne["cik"],
                "nom": ligne["nom"],
                "symboles": ligne["symboles"],
                "secteur": ligne["secteur"],
                "annee": ligne["annee"],
                "test": test,
                "detail": detail,
            }
        )

    # --- tests ligne par ligne -------------------------------------------
    for _, r in b.iterrows():
        ca, capex, rd = r["chiffre_affaires"], r["capex"], r["rd"]

        if pd.notna(ca) and ca <= 0:
            signaler(r, "chiffre d affaires nul ou negatif", f"{ca:,.0f}")

        if pd.notna(capex) and capex < 0:
            signaler(r, "investissement negatif", f"{capex:,.0f}")

        if pd.notna(ca) and pd.notna(capex) and ca > 0 and capex / ca > 1:
            signaler(r, "investissement superieur au chiffre d affaires", f"{capex / ca:.0%}")

        if pd.notna(ca) and pd.notna(rd) and ca > 0 and rd / ca > 0.5:
            signaler(r, "recherche superieure a la moitie du chiffre d affaires", f"{rd / ca:.0%}")

        if pd.notna(r["ca_ecart_relatif"]) and r["ca_ecart_relatif"] > 0.05:
            signaler(r, "etiquettes de revenu en desaccord", f"{r['ca_ecart_relatif']:.0%}")

    # --- tests sur la serie de chaque entreprise --------------------------
    for cik, g in b.groupby("cik"):
        g = g.sort_values("annee")
        ligne = g.iloc[-1]

        ca = g.dropna(subset=["chiffre_affaires"])
        if len(ca) >= 2:
            var = ca["chiffre_affaires"].pct_change()
            for annee, v in zip(ca["annee"].iloc[1:], var.iloc[1:]):
                if v > 2:
                    signaler(
                        {**ligne, "annee": annee},
                        "chiffre d affaires plus que triple en un an",
                        f"{v:+.0%}",
                    )
                elif v < -0.6:
                    signaler(
                        {**ligne, "annee": annee},
                        "chiffre d affaires effondre en un an",
                        f"{v:+.0%}",
                    )

        if len(ca) >= 2:
            attendues = set(range(int(ca["annee"].min()), int(ca["annee"].max()) + 1))
            manquantes = sorted(attendues - set(ca["annee"].astype(int)))
            if manquantes:
                signaler(ligne, "trou dans la serie", f"annees manquantes : {manquantes}")

        if len(ca) and ca["annee"].max() < 2024:
            signaler(ligne, "dernier exercice trop ancien", f"{int(ca['annee'].max())}")

        if not len(ca):
            signaler(ligne, "aucun chiffre d affaires", "")

    a = pd.DataFrame(alertes).sort_values(["test", "nom", "annee"])
    a.to_csv(SORTIE, index=False, encoding="utf-8")

    print(f"{len(a)} alertes sur {b['cik'].nunique()} entreprises\n")
    print("--- par test ---")
    recap = a.groupby("test").agg(alertes=("cik", "size"), entreprises=("cik", "nunique"))
    print(recap.sort_values("alertes", ascending=False).to_string())
    print(f"\nDetail complet : {SORTIE.name}")


if __name__ == "__main__":
    main()
