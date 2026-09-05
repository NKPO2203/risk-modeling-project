"""
Corroboration par les comptes des 82 entreprises retenues.

Etape cinq de la regle de selection : une entreprise entre si elle declare une
dependance a l'infrastructure de calcul ET si ses comptes montrent que quelque
chose a effectivement bouge.

Entrees : data/processed/base_selection.csv
          data/processed/univers_retenu.csv
Sortie  : data/processed/corroboration.csv
"""

from pathlib import Path

import numpy as np
import pandas as pd

RACINE = Path(__file__).resolve().parents[1]
COMPTES = RACINE / "data" / "processed" / "base_selection.csv"
UNIVERS = RACINE / "data" / "processed" / "univers_retenu.csv"
SORTIE = RACINE / "data" / "processed" / "corroboration.csv"

# --------------------------------------------------------------------------
# LE CRITERE
#
# Chaque entreprise est comparee a son propre passe, jamais aux autres. Une
# compagnie d'electricite investit lourdement depuis toujours, un concepteur
# de puces sans usine investit peu par nature : les comparer entre elles ne
# dirait rien.
#
# Periode de reference : moyenne des exercices 2017 a 2019, qui precede a la
# fois la pandemie et la vague d'investissement actuelle. Quand une entreprise
# n'existait pas encore sous sa forme actuelle, on prend les deux exercices
# les plus anciens disponibles, et on le signale : la comparaison est alors
# plus faible, puisque la base se situe deja dans la periode etudiee.
#
# LA CORROBORATION EST UNE MESURE, PAS UN EXAMEN.
#
# Deux versions anterieures ont ete abandonnees, et il faut dire pourquoi.
#
# La premiere demandait si les depenses avaient cru plus vite que l'activite.
# Elle classait Nvidia, dont le chiffre d'affaires a ete multiplie par vingt,
# en "non confirmee", parce que ses ventes avaient cru plus vite encore que sa
# recherche. En divisant par la croissance du chiffre d'affaires, on efface le
# signal qu'on cherche.
#
# La seconde faisait dependre le critere du canal d'exposition. Elle classait
# Vertiv, qui a triple son chiffre d'affaires et quadruple son investissement,
# en "non confirmee", parce que le canal "fournit" melange des vendeurs
# d'equipements, dont la preuve est le chiffre d'affaires, et des
# infrastructures regulees, dont la preuve est la depense.
#
# Une troisieme correction du critere aurait ete defendable sur le fond. Mais
# ajuster une regle jusqu'a ce que les entreprises auxquelles on croit la
# passent, c'est fabriquer un resultat au lieu de le mesurer. On arrete.
#
# On ne trie donc plus. On mesure, et on laisse voir.
#
# Deux multiples, chaque entreprise comparee a elle-meme :
#   multiple des ventes   = chiffre d'affaires recent / base
#   multiple des depenses = le plus eleve entre investissement et recherche
#
# Trois niveaux, avec des bornes qui ne se negocient pas :
#   AUCUN MOUVEMENT  les deux multiples sont <= 1, rien n'a bouge ni meme
#                    progresse. Seul cas qui CONTREDIT la declaration.
#   MOUVEMENT NET    au moins un multiple >= 2, l'entreprise a double.
#   MOUVEMENT MODERE tout le reste : progression reelle mais ordinaire.
#
# 1 et 2 sont des reperes naturels, pas des valeurs ajustees apres coup.
# Aucune entreprise n'est retiree de l'univers par cette etape.
# --------------------------------------------------------------------------

BASE_DEBUT, BASE_FIN = 2017, 2019
SEUIL_NET = 2.0
SEUIL_NUL = 1.0


def moyenne_base(g, colonne):
    """Moyenne de reference, avec repli sur les plus anciens exercices dispo."""
    dispo = g.dropna(subset=[colonne])
    if dispo.empty:
        return np.nan, ""
    fenetre = dispo[dispo["annee"].between(BASE_DEBUT, BASE_FIN)]
    if len(fenetre) >= 2:
        return fenetre[colonne].mean(), f"{int(fenetre.annee.min())}-{int(fenetre.annee.max())}"
    repli = dispo.nsmallest(2, "annee")
    if len(repli) < 2:
        return np.nan, ""
    return repli[colonne].mean(), f"{int(repli.annee.min())}-{int(repli.annee.max())} (repli)"


def main():
    comptes = pd.read_csv(COMPTES, dtype={"cik": str})
    univers = pd.read_csv(UNIVERS)
    canaux = dict(zip(univers["nom"], univers["canal"]))

    lignes = []
    for (cik, nom), g in comptes[comptes["nom"].isin(canaux)].groupby(["cik", "nom"]):
        g = g.sort_values("annee")
        recent = g[g["annee"] >= 2024]
        if recent.empty:
            continue
        derniere = recent.iloc[-1]
        canal = canaux[nom]

        base_ca, ans_ca = moyenne_base(g, "chiffre_affaires")
        base_capex, _ = moyenne_base(g, "capex")
        base_rd, _ = moyenne_base(g, "rd")
        ca, capex, rd = derniere["chiffre_affaires"], derniere["capex"], derniere["rd"]

        def mult(valeur, base):
            return valeur / base if pd.notna(valeur) and pd.notna(base) and base > 0 else np.nan

        croiss_ca = mult(ca, base_ca)
        croiss_capex = mult(capex, base_capex)
        croiss_rd = mult(rd, base_rd)

        depenses = [x for x in (croiss_capex, croiss_rd) if pd.notna(x)]
        mult_depenses = max(depenses) if depenses else np.nan

        connus = [x for x in (croiss_ca, mult_depenses) if pd.notna(x)]
        if not connus:
            niveau = "non evaluable"
        elif max(connus) >= SEUIL_NET:
            niveau = "mouvement net"
        elif all(x <= SEUIL_NUL for x in connus) and len(connus) == 2:
            niveau = "aucun mouvement"
        else:
            niveau = "mouvement modere"

        lignes.append({
            "nom": nom, "canal": canal,
            "annee_recente": int(derniere["annee"]), "base_annees": ans_ca,
            "base_courte": "oui" if "repli" in ans_ca else "",
            "ca_md": ca / 1e9 if pd.notna(ca) else np.nan,
            "capex_md": capex / 1e9 if pd.notna(capex) else np.nan,
            "rd_md": rd / 1e9 if pd.notna(rd) else np.nan,
            "mult_ventes": croiss_ca,
            "mult_capex": croiss_capex,
            "mult_recherche": croiss_rd,
            "mult_depenses": mult_depenses,
            "corroboration": niveau,
        })

    r = pd.DataFrame(lignes).merge(
        univers[["nom", "symboles", "secteur", "degre"]], on="nom", how="left")
    r = r.sort_values(["corroboration", "canal", "nom"])
    r.to_csv(SORTIE, index=False, encoding="utf-8")

    print(f"{len(r)} entreprises evaluees sur {len(univers)} retenues\n")
    print(r["corroboration"].value_counts().to_string())
    print("\n--- par canal ---")
    print(pd.crosstab(r["canal"], r["corroboration"]).to_string())
    print("\n--- par secteur ---")
    print(pd.crosstab(r["secteur"], r["corroboration"]).to_string())
    tardives = r[r["base_annees"].str.contains("repli", na=False)]
    print(f"\n{len(tardives)} entreprises jugees sur une base de repli (historique incomplet)")


if __name__ == "__main__":
    main()
