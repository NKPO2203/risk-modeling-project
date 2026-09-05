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
import os
import tempfile
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path
import pandas as pd

# --------------------------------------------------------------------------
# Paramètres
# --------------------------------------------------------------------------

CONTACT = "josuenkpoman@gmail.com"
HEADERS = {
    "User-Agent": f"AI-Concentration-Risk-Research {CONTACT}",
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


def annee_de_reference(fin, debut=None):
    """
    Rattache un exercice comptable à une année civile.

    Toutes les entreprises ne clôturent pas au 31 décembre. Nvidia clôture
    fin janvier, Microsoft fin juin. Comparer des "années 2024" reviendrait
    à comparer des périodes différentes.

    Convention retenue : compter les jours de la période réelle dans chaque
    année civile. Une clôture en juin peut aussi appartenir à l'année
    précédente ; la règle ne repose donc pas sur un seuil de mois.

    Exemple : l'exercice de Nvidia clos le 28 janvier 2024 a couvert
    l'essentiel de l'année 2023, il est donc rattaché à 2023.
    """
    if debut is None:
        raise ValueError("La date de début est requise pour compter les jours par année")
    a, b = pd.Timestamp(debut), pd.Timestamp(fin)
    if pd.isna(a) or pd.isna(b) or b < a:
        raise ValueError("Période annuelle invalide")
    jours = {annee: (min(b, pd.Timestamp(annee, 12, 31)) - max(a, pd.Timestamp(annee, 1, 1))).days + 1
             for annee in range(a.year, b.year + 1)}
    return max(jours, key=lambda annee: (jours[annee], annee))


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
        if e.get("form") not in {"10-K", "10-K/A"}:
            continue
        debut, fin = e.get("start"), e.get("end")
        if not debut or not fin:
            continue
        duree = (pd.Timestamp(fin) - pd.Timestamp(debut)).days
        if not (330 <= duree <= 400):
            continue
        annee = annee_de_reference(fin, debut)
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
                "formulaire": e.get("form"),
                "unite": "USD",
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
        # Des exercices distincts peuvent partager une année majoritaire.
        # Je conserve les périodes distinctes pour les signaler au traitement.
        cle = (l["debut"], l["fin"])
        if cle not in par_annee or (l["depose_le"], l["depot"]) > (par_annee[cle]["depose_le"], par_annee[cle]["depot"]):
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
    "formulaire", "unite", "source_url", "recupere_le",
]


def recuperer_json(url, tentatives=3):
    """Client SEC standard, reprises bornées ; aucun paquet requests requis."""
    for tentative in range(tentatives):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=HEADERS), timeout=45) as reponse:
                return json.load(reponse)
        except urllib.error.HTTPError as exc:
            if exc.code not in {429, 500, 502, 503, 504} or tentative == tentatives - 1:
                raise
        except (urllib.error.URLError, TimeoutError):
            if tentative == tentatives - 1:
                raise
        time.sleep(min(2 ** tentative, 4))


def main():
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

    # Le fichier exploité par les analyses n'est remplacé qu'à la fin d'une
    # collecte sans échec réseau. Une interruption conserve la version acquise.
    FICHIER_SORTIE.parent.mkdir(parents=True, exist_ok=True)
    sortie = tempfile.NamedTemporaryFile(mode="w", newline="", encoding="utf-8", prefix="sec_facts_", suffix=".part", dir=FICHIER_SORTIE.parent, delete=False)
    ecrivain = csv.DictWriter(sortie, fieldnames=COLONNES)
    ecrivain.writeheader()

    n_valeurs = 0
    journal = []
    echecs = 0
    recupere_le = datetime.now(timezone.utc).isoformat()

    for i, ligne in entreprises.iterrows():
        cik = ligne["CIK"]
        url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"

        try:
            document = recuperer_json(url)
            if not isinstance(document, dict) or "facts" not in document:
                raise ValueError("Réponse companyfacts sans objet facts")
            faits = document["facts"]
        except Exception as exc:
            echecs += 1
            journal.append({"cik": cik, "nom": ligne["nom"], "probleme": f"reseau: {type(exc).__name__}"})
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
                        "source_url": url,
                        "recupere_le": recupere_le,
                    }
                )
                n_valeurs += 1

        if (i + 1) % 25 == 0:
            sortie.flush()
            print(f"  {i + 1} entreprises traitees, {n_valeurs} valeurs", flush=True)

        time.sleep(PAUSE)

    sortie.close()
    if echecs or n_valeurs == 0:
        journal_path = Path(sortie.name).with_suffix('.log.csv')
        pd.DataFrame(journal, columns=["cik", "nom", "probleme"]).to_csv(journal_path, index=False, encoding="utf-8")
        raise RuntimeError(f"{echecs} échecs réseau : anciennes données conservées ; collecte partielle {sortie.name}, journal {journal_path}")
    os.replace(sortie.name, FICHIER_SORTIE)
    pd.DataFrame(journal, columns=["cik", "nom", "probleme"]).to_csv(FICHIER_LOG, index=False, encoding="utf-8")

    print(f"\nTermine. {n_valeurs} valeurs ecrites dans {FICHIER_SORTIE.name}", flush=True)
    print(f"{len(journal)} anomalies consignees dans {FICHIER_LOG.name}", flush=True)


if __name__ == "__main__":
    main()
