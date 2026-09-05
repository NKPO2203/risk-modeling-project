"""
Récupération des données financières officielles des composantes du S&P 500
depuis la base XBRL de la SEC (API "companyfacts").

Ce script ne calcule rien et n'interprète rien. Il recopie des valeurs
déposées par les entreprises elles-mêmes dans leurs rapports annuels,
et conserve pour chaque valeur de quel dépôt elle provient.

Source : https://data.sec.gov/api/xbrl/companyfacts/CIK##########.json
La SEC impose de s'identifier dans l'en-tête User-Agent (nom + contact).

Sortie : data/raw/sec_facts_raw.csv (format long, une ligne par valeur)
         data/raw/sec_fetch_log.csv (échecs et anomalies)
"""

import json
import time
import csv
import sys
from pathlib import Path

import requests
import pandas as pd

# --------------------------------------------------------------------------
# Paramètres
# --------------------------------------------------------------------------

CONTACT = "josuenkpoman@gmail.com"
HEADERS = {
    "User-Agent": f"AI-Concentration-Risk-Research {CONTACT}",
    "Accept-Encoding": "gzip, deflate",
    "Host": "data.sec.gov",
}

RACINE = Path(__file__).resolve().parents[1]
FICHIER_CONSTITUANTS = RACINE / "data" / "raw" / "sp500_constituents.csv"
FICHIER_SORTIE = RACINE / "data" / "raw" / "sec_facts_raw.csv"
FICHIER_LOG = RACINE / "data" / "raw" / "sec_fetch_log.csv"

# Premier exercice retenu. Volontairement large : la période d'étude
# n'est pas encore fixée, il vaut mieux récupérer trop que devoir recommencer.
ANNEE_MIN = 2014

# Pause entre deux requêtes. La SEC tolère 10 requêtes par seconde,
# on reste nettement en dessous.
PAUSE = 0.15

# --------------------------------------------------------------------------
# Étiquettes comptables recherchées
#
# Une même notion peut porter des noms différents selon l'entreprise et
# selon l'année. On les cherche dans l'ordre : la première trouvée gagne,
# et on note laquelle a servi.
# --------------------------------------------------------------------------

ETIQUETTES = {
    "chiffre_affaires": [
        "Revenues",
        "RevenueFromContractWithCustomerExcludingAssessedTax",
        "RevenueFromContractWithCustomerIncludingAssessedTax",
        "RevenuesNetOfInterestExpense",
        "RegulatedAndUnregulatedOperatingRevenue",
        "SalesRevenueNet",
        "SalesRevenueGoodsNet",
    ],
    # Ordre de preference : d'abord les achats d'immobilisations classiques,
    # puis les formulations propres aux services aux collectivites
    # (construction en cours, actifs productifs), puis celles des foncieres
    # (developpement, puis acquisition d'actifs immobiliers).
    #
    # Ces cinq dernieres etiquettes ont ete ajoutees apres avoir constate que
    # sept entreprises de l'univers retenu, dont Digital Realty, Prologis,
    # Dominion et Consolidated Edison, n'avaient aucune donnee d'investissement
    # avec la liste initiale. Elles declarent bien leurs investissements, mais
    # sous des noms comptables propres a leur secteur.
    "investissement": [
        "PaymentsToAcquirePropertyPlantAndEquipment",
        "PaymentsToAcquireProductiveAssets",
        "PaymentsForProceedsFromProductiveAssets",
        "PaymentsForConstructionInProcess",
        "PaymentsForCapitalImprovements",
        "PaymentsToDevelopRealEstateAssets",
        "PaymentsToAcquireAndDevelopRealEstate",
        "PaymentsToAcquireRealEstate",
        "PaymentsToAcquireOtherPropertyPlantAndEquipment",
        "PaymentsToAcquireMachineryAndEquipment",
    ],
    "recherche": [
        "ResearchAndDevelopmentExpense",
        "ResearchAndDevelopmentExpenseExcludingAcquiredInProcessCost",
    ],
}

# Note sur l'ordre du chiffre d'affaires.
#
# Une même entreprise peut publier plusieurs lignes de revenus dont l'une
# n'est qu'une partie de l'autre. Vistra déclare 17 738 M$ sous "Revenues",
# qui est le total de son compte de résultat, et 17 586 M$ sous
# "RevenueFromContractWithCustomerExcludingAssessedTax", qui en exclut les
# revenus ne provenant pas de contrats avec des clients.
#
# "Revenues" passe donc en premier : c'est la ligne du compte de résultat.
#
# Ce fichier conserve néanmoins TOUTES les étiquettes trouvées, sans en
# choisir aucune. Le choix appartient à l'étape de traitement, où il est
# documenté et où les désaccords entre étiquettes peuvent être signalés.
# Un fichier de données brutes ne doit pas contenir de décision cachée.


def annee_de_reference(fin):
    """
    Rattache un exercice comptable à une année civile.

    Toutes les entreprises ne clôturent pas au 31 décembre. Nvidia clôture
    fin janvier, Microsoft fin juin. Comparer des "années 2024" reviendrait
    à comparer des périodes différentes.

    Convention retenue : l'exercice est rattaché à l'année civile dans
    laquelle il a passé le plus de temps. Concrètement, une clôture entre
    janvier et mai est rattachée à l'année précédente.

    Exemple : l'exercice de Nvidia clos le 28 janvier 2024 a couvert
    l'essentiel de l'année 2023, il est donc rattaché à 2023.
    """
    d = pd.Timestamp(fin)
    return d.year - 1 if d.month <= 5 else d.year


def extraire_valeurs_annuelles(faits, etiquette):
    """
    Sort les valeurs annuelles d'une étiquette donnée.

    Attention à un piège de la base SEC : les champs 'fy' et 'fp' d'une
    valeur désignent l'exercice du RAPPORT dans lequel elle figure, et non
    l'exercice auquel elle se rapporte. Un rapport annuel contient les deux
    exercices précédents en comparatif, tous étiquetés avec l'année du
    rapport. Se fier à 'fy' revient donc à dater les chiffres n'importe
    comment.

    On se fie uniquement à la date de clôture réelle de la période, et on
    vérifie que celle-ci couvre bien environ un an, car un rapport annuel
    contient aussi des lignes trimestrielles.
    """
    bloc = faits.get("us-gaap", {}).get(etiquette)
    if bloc is None:
        return []

    unites = bloc.get("units", {}).get("USD")
    if not unites:
        return []

    lignes = []
    for e in unites:
        if e.get("form") != "10-K" or e.get("fp") != "FY":
            continue
        debut, fin = e.get("start"), e.get("end")
        if not debut or not fin:
            continue
        duree = (pd.Timestamp(fin) - pd.Timestamp(debut)).days
        if not (330 <= duree <= 400):
            continue
        annee = annee_de_reference(fin)
        if annee < ANNEE_MIN:
            continue
        lignes.append(
            {
                "etiquette": etiquette,
                "annee": annee,
                "debut": debut,
                "fin": fin,
                "duree_jours": duree,
                "valeur": e["val"],
                "depot": e.get("accn"),
                "depose_le": e.get("filed"),
            }
        )
    return lignes


def choisir_par_exercice(lignes):
    """
    Une même valeur est redéposée dans plusieurs rapports successifs, et
    peut être retraitée entre-temps. Pour chaque exercice, on garde la
    version issue du dépôt le plus récent.
    """
    par_annee = {}
    for l in lignes:
        cle = l["annee"]
        if cle not in par_annee or l["depose_le"] > par_annee[cle]["depose_le"]:
            par_annee[cle] = l
    return sorted(par_annee.values(), key=lambda x: x["annee"])


def extraire_notion(faits, candidates):
    """
    Rassemble tout ce qui est publié pour une notion comptable, sans rien
    écarter.

    Deux raisons de tout garder.

    D'abord, une entreprise peut changer d'étiquette d'une année à l'autre.
    Nvidia déclare son chiffre d'affaires sous un nom jusqu'en 2021 et sous
    un autre ensuite. S'arrêter à la première étiquette trouvée produirait
    une série tronquée sans que rien ne le signale.

    Ensuite, deux étiquettes peuvent coexister la même année en désignant
    des périmètres différents, l'une étant une partie de l'autre. Choisir
    ici reviendrait à cacher une décision dans un fichier de données brutes.
    Le choix est fait à l'étape de traitement, où il est visible et où les
    désaccords entre étiquettes sont signalés.
    """
    lignes = []
    for rang, etiquette in enumerate(candidates):
        for l in choisir_par_exercice(extraire_valeurs_annuelles(faits, etiquette)):
            l["rang_preference"] = rang
            lignes.append(l)
    return sorted(lignes, key=lambda l: (l["annee"], l["rang_preference"]))


def verifier_ecriture(chemin):
    """
    Vérifie qu'on pourra écrire le fichier AVANT de lancer la collecte.

    Sous Windows, un fichier ouvert dans Excel est verrouillé et ne peut pas
    être réécrit. Sans cette vérification, on découvrirait le problème après
    dix minutes de téléchargement, au moment d'enregistrer, et tout serait
    perdu.
    """
    try:
        with open(chemin, "a", encoding="utf-8"):
            pass
    except PermissionError:
        print(
            f"\nARRET : le fichier {chemin.name} est verrouille.\n"
            f"Il est probablement ouvert dans Excel. Ferme-le et relance.\n",
            file=sys.stderr,
        )
        sys.exit(1)


COLONNES = [
    "cik", "nom", "symboles", "secteur", "sous_secteur",
    "notion", "etiquette", "rang_preference", "annee",
    "debut", "fin", "duree_jours", "valeur", "depot", "depose_le",
]


def main():
    verifier_ecriture(FICHIER_SORTIE)
    verifier_ecriture(FICHIER_LOG)

    constituants = pd.read_csv(FICHIER_CONSTITUANTS, dtype={"CIK": str})
    constituants["CIK"] = constituants["CIK"].str.zfill(10)

    # Une entreprise compte pour une entreprise : on regroupe les classes
    # d'actions multiples et on garde les symboles associés.
    entreprises = (
        constituants.groupby("CIK")
        .agg(
            nom=("Security", "first"),
            symboles=("Symbol", lambda s: "|".join(sorted(s))),
            secteur=("GICS Sector", "first"),
            sous_secteur=("GICS Sub-Industry", "first"),
        )
        .reset_index()
    )

    print(f"{len(entreprises)} entreprises a traiter", flush=True)

    session = requests.Session()
    session.headers.update(HEADERS)

    # On ecrit au fil de l'eau. Si la collecte s'interrompt, ce qui a deja
    # ete recupere est sur le disque au lieu d'etre perdu.
    sortie = open(FICHIER_SORTIE, "w", newline="", encoding="utf-8")
    ecrivain = csv.DictWriter(sortie, fieldnames=COLONNES)
    ecrivain.writeheader()

    n_valeurs = 0
    journal = []

    for i, ligne in entreprises.iterrows():
        cik = ligne["CIK"]
        url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"

        try:
            r = session.get(url, timeout=45)
        except Exception as exc:
            journal.append({"cik": cik, "nom": ligne["nom"], "probleme": f"reseau: {type(exc).__name__}"})
            time.sleep(PAUSE)
            continue

        if r.status_code != 200:
            journal.append({"cik": cik, "nom": ligne["nom"], "probleme": f"http {r.status_code}"})
            time.sleep(PAUSE)
            continue

        try:
            faits = r.json().get("facts", {})
        except Exception:
            journal.append({"cik": cik, "nom": ligne["nom"], "probleme": "json illisible"})
            time.sleep(PAUSE)
            continue

        for notion, candidates in ETIQUETTES.items():
            trouve = extraire_notion(faits, candidates)

            if not trouve:
                journal.append(
                    {"cik": cik, "nom": ligne["nom"], "probleme": f"aucune etiquette pour {notion}"}
                )
                continue

            for l in trouve:
                ecrivain.writerow(
                    {
                        "cik": cik,
                        "nom": ligne["nom"],
                        "symboles": ligne["symboles"],
                        "secteur": ligne["secteur"],
                        "sous_secteur": ligne["sous_secteur"],
                        "notion": notion,
                        **l,
                    }
                )
                n_valeurs += 1

        if (i + 1) % 25 == 0:
            sortie.flush()
            print(f"  {i + 1} entreprises traitees, {n_valeurs} valeurs", flush=True)

        time.sleep(PAUSE)

    sortie.close()
    pd.DataFrame(journal).to_csv(FICHIER_LOG, index=False, encoding="utf-8")

    print(f"\nTermine. {n_valeurs} valeurs ecrites dans {FICHIER_SORTIE.name}", flush=True)
    print(f"{len(journal)} anomalies consignees dans {FICHIER_LOG.name}", flush=True)


if __name__ == "__main__":
    main()
