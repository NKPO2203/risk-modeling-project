"""
Construction de la table de sélection à partir des données brutes de la SEC.

Le fichier brut conserve toutes les étiquettes comptables trouvées, sans en
choisir aucune. C'est ici, et seulement ici, que le choix est fait, de façon
visible et documentée.

Entrée  : data/raw/sec_facts_raw.csv
Sortie  : data/processed/base_selection.csv
          data/processed/base_selection_anomalies.csv
"""

from pathlib import Path

import pandas as pd

RACINE = Path(__file__).resolve().parents[1]
ENTREE = RACINE / "data" / "raw" / "sec_facts_raw.csv"
SORTIE = RACINE / "data" / "processed" / "base_selection.csv"
ANOMALIES = RACINE / "data" / "processed" / "base_selection_anomalies.csv"

# --------------------------------------------------------------------------
# Règle de choix du chiffre d'affaires
#
# Le problème : une même entreprise publie parfois plusieurs lignes de
# revenus, dont l'une n'est qu'une partie de l'autre.
#
#   Vistra          "Revenues" 17 738  >  "contrats clients" 17 586
#                   l'ecart correspond aux resultats de couverture
#   Essex Property  "Revenues"  1 887  >  "contrats clients"      9
#                   une fonciere encaisse des loyers, pas des ventes
#   MetLife         "Revenues" 77 084  >  "contrats clients"  2 436
#                   un assureur encaisse des primes, pas des ventes
#
# On pourrait croire qu'il suffit de préférer "Revenues". C'est faux :
# chez NetApp, Williams ou American Electric Power, "Revenues" est plus
# PETIT que la ligne des contrats clients.
#
# On pourrait croire qu'il suffit de prendre le maximum. C'est faux aussi :
# chez Brown-Forman et Constellation Brands, une étiquette inclut les taxes
# sur l'alcool et dépasse de 25 % le chiffre d'affaires réellement publié.
#
# Règle retenue : le maximum des étiquettes représentant un revenu net,
# en écartant celle qui inclut les taxes collectées, sauf si c'est la seule
# disponible.
#
# Justification : ces étiquettes sont toutes soit le total du compte de
# résultat, soit une partie de ce total. La plus grande est donc le total.
# La seule qui puisse dépasser le total est celle qui y ajoute des taxes,
# et on l'écarte pour cette raison.
# --------------------------------------------------------------------------

TAXES_INCLUSES = "RevenueFromContractWithCustomerIncludingAssessedTax"

# Au-delà de ce désaccord relatif entre étiquettes, l'entreprise est
# signalée pour vérification manuelle.
SEUIL_ALERTE = 0.05


def choisir_chiffre_affaires(groupe):
    """Applique la règle ci-dessus à un couple entreprise-année."""
    net = groupe[groupe["etiquette"] != TAXES_INCLUSES]
    source = net if len(net) else groupe
    gagnante = source.loc[source["valeur"].idxmax()]

    valeurs = source["valeur"]
    ecart = 0.0 if len(valeurs) < 2 or valeurs.max() == 0 else 1 - valeurs.min() / valeurs.max()

    return pd.Series(
        {
            "chiffre_affaires": gagnante["valeur"],
            "ca_etiquette": gagnante["etiquette"],
            "ca_nb_etiquettes": len(groupe),
            "ca_ecart_relatif": ecart,
            "fin_exercice": gagnante["fin"],
            "ca_depot": gagnante["depot"],
        }
    )


def choisir_simple(groupe):
    """
    Pour l'investissement et la recherche, on retient l'étiquette la mieux
    classée dans la liste de préférence, celle-ci étant construite du plus
    précis au plus général.
    """
    gagnante = groupe.loc[groupe["rang_preference"].idxmin()]
    return pd.Series({"valeur": gagnante["valeur"], "etiquette": gagnante["etiquette"]})


def main():
    d = pd.read_csv(ENTREE, dtype={"cik": str})
    SORTIE.parent.mkdir(parents=True, exist_ok=True)

    cle = ["cik", "nom", "symboles", "secteur", "sous_secteur", "annee"]

    ca = (
        d[d["notion"] == "chiffre_affaires"]
        .groupby(cle, as_index=False)
        .apply(choisir_chiffre_affaires, include_groups=False)
    )

    autres = []
    for notion, prefixe in [("investissement", "capex"), ("recherche", "rd")]:
        t = (
            d[d["notion"] == notion]
            .groupby(cle, as_index=False)
            .apply(choisir_simple, include_groups=False)
            .rename(columns={"valeur": prefixe, "etiquette": f"{prefixe}_etiquette"})
        )
        autres.append(t)

    table = ca
    for t in autres:
        table = table.merge(t, on=cle, how="outer")

    table = table.sort_values(["nom", "annee"])
    table.to_csv(SORTIE, index=False, encoding="utf-8")

    alertes = table[table["ca_ecart_relatif"] > SEUIL_ALERTE].copy()
    alertes = alertes.sort_values("ca_ecart_relatif", ascending=False)
    alertes.to_csv(ANOMALIES, index=False, encoding="utf-8")

    print(f"{len(table)} lignes entreprise-annee ecrites dans {SORTIE.name}")
    print(f"{table['cik'].nunique()} entreprises")
    print(f"{len(alertes)} lignes signalees pour desaccord entre etiquettes de revenu")
    print(f"  soit {alertes['cik'].nunique()} entreprises, listees dans {ANOMALIES.name}")


if __name__ == "__main__":
    main()
