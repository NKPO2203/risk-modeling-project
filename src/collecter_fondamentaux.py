"""Collecte des faits comptables XBRL des entreprises du thème, avec leur date de dépôt.

Exécution : python -m src.collecter_fondamentaux
Source : interface `companyfacts` de la SEC, une requête par entreprise, avec
l'identification exigée par la SEC dans l'en-tête User-Agent.
Sortie : data/raw/fondamentaux/faits_10k.csv et son manifeste.

Seuls les faits portés par un rapport annuel 10-K sont gardés, avec le numéro
de dépôt et sa date, pour qu'un calcul ultérieur n'utilise un chiffre qu'à
partir du lendemain de son dépôt. Les étiquettes retenues sont celles des
cinq critères de la section IX de research/plan_projet.md. Le fichier JSON
complet n'est pas conservé : il pèse plusieurs mégaoctets par entreprise.
"""
from pathlib import Path
from datetime import datetime, timezone
import http.client
import json
import time
import urllib.error
import urllib.request

import pandas as pd

from src.empreintes import empreinte

RACINE = Path(__file__).resolve().parents[1]
DOSSIER = RACINE / "data/raw/fondamentaux"
SORTIE = DOSSIER / "faits_10k.csv"
MANIFESTE = DOSSIER / "manifeste.json"
CONTACT = "josuenkpoman@gmail.com"
ENTETES = {"User-Agent": f"AI-Concentration-Risk-Research {CONTACT}"}
ETIQUETTES = {
    "us-gaap": ["Assets", "GrossProfit", "Revenues", "RevenueFromContractWithCustomerExcludingAssessedTax",
                "SalesRevenueNet", "CostOfRevenue", "CostOfGoodsAndServicesSold", "CostOfGoodsSold",
                "NetIncomeLoss", "NetCashProvidedByUsedInOperatingActivities",
                "NetCashProvidedByUsedInOperatingActivitiesContinuingOperations",
                "StockholdersEquity", "StockholdersEquityIncludingPortionAttributableToNoncontrollingInterest"],
    "dei": ["EntityPublicFloat"],
}


def entreprises(racine=RACINE):
    a = pd.read_csv(racine / "data/processed/appartenance.csv", dtype=str)
    p1 = a[a.portefeuille == "P1"]
    return p1.groupby("cik").entreprise.first()


def telecharger(cik, essais=6):
    url = f"https://data.sec.gov/api/xbrl/companyfacts/CIK{cik}.json"
    for i in range(essais):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=ENTETES), timeout=60) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
        except (urllib.error.URLError, TimeoutError, http.client.IncompleteRead, ConnectionError):
            pass
        time.sleep(2 * (i + 1))
    raise RuntimeError(f"Téléchargement impossible : CIK {cik}")


def extraire(cik, donnees):
    lignes = []
    for taxonomie, noms in ETIQUETTES.items():
        faits = donnees.get("facts", {}).get(taxonomie, {})
        for nom in noms:
            for unite, valeurs in faits.get(nom, {}).get("units", {}).items():
                if unite != "USD":
                    continue
                for v in valeurs:
                    if v.get("form") != "10-K":
                        continue
                    lignes.append({"cik": cik, "taxonomie": taxonomie, "etiquette": nom,
                                   "debut": v.get("start", ""), "fin": v["end"], "valeur": v["val"],
                                   "depose_le": v["filed"], "depot": v["accn"],
                                   "exercice": v.get("fy"), "periode": v.get("fp")})
    return lignes


def collecter(racine=RACINE):
    DOSSIER.mkdir(parents=True, exist_ok=True)
    noms = entreprises(racine)
    lignes, absentes = [], []
    for cik, nom in noms.items():
        donnees = telecharger(cik)
        if donnees is None:
            absentes.append({"cik": cik, "entreprise": nom})
            continue
        lignes += extraire(cik, donnees)
        time.sleep(0.15)
    faits = (pd.DataFrame(lignes).drop_duplicates()
             .sort_values(["cik", "etiquette", "fin", "depose_le", "debut"]))
    faits.to_csv(SORTIE, index=False, encoding="utf-8", lineterminator="\n")
    manifeste = {
        "produit_le": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "commande": "python -m src.collecter_fondamentaux",
        "source": "SEC, interface XBRL companyfacts (data.sec.gov)",
        "entreprises": len(noms), "entreprises_sans_faits": absentes,
        "etiquettes": ETIQUETTES, "lignes": len(faits),
        "limites": ["Seuls les rapports annuels 10-K sont gardes ; les 10-K/A et les 10-Q sont exclus.",
                    "Les faits XBRL commencent avec les depots de 2009 et 2010.",
                    "Une entreprise etrangere deposant des 20-F n'a pas de faits 10-K."],
        "sha256": empreinte(SORTIE),
    }
    MANIFESTE.write_text(json.dumps(manifeste, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return faits, manifeste


if __name__ == "__main__":
    f, m = collecter()
    print(m["lignes"], "lignes,", f.cik.nunique(), "entreprises ;", len(m["entreprises_sans_faits"]), "sans faits")
