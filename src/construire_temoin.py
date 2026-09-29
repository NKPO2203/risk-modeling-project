"""Groupe témoin : les entreprises SORT, construites comme les portefeuilles du thème.

Exécution : python -m src.construire_temoin
Prérequis : data/processed de l'étape 2, et le manifeste de l'étape 3 pour
episodes_tension.csv. Les deux sont vérifiés avant tout calcul.

Le thème et le témoin sont tous deux tirés de la composition du S&P 500 de
2026, avec la même équipondération et les mêmes règles d'entrée, de
rééquilibrage et de frais. Partager le biais de survie ne veut pas dire en
subir le même effet : l'écart entre les deux est une comparaison descriptive
entre deux univers de 2026 reconstitués dans le passé. Il ne mesure isolément
ni le biais de survie ni l'effet de l'IA.

Deux témoins sont construits :
- T1, toutes les entreprises SORT à poids égaux, comme P1 ;
- T1S, les mêmes entreprises repondérées selon la répartition sectorielle des
  134 entreprises retenues en 2026, fixe sur toute la période. P1 change de
  composition et ses poids dérivent : l'écart P1 - T1S peut encore devoir une
  partie de sa valeur aux secteurs.

Les cours du témoin n'ont reçu ni seconde source ni correction manuelle.
Les séances absentes chez Yahoo sont traitées comme des cotations absentes :
le dernier cours est porté et aucune opération n'y est faite.
"""
from pathlib import Path
import argparse
import json

import numpy as np
import pandas as pd

from src import risque
from src.construire_portefeuilles import lire_prix, simuler_groupe, verifier
from src.empreintes import correspond, ecrire_manifeste, verifier_manifeste
from src.portefeuille import COUT, poids_cibles, preparer_prix

RACINE = Path(__file__).resolve().parents[1]
DEBUT = "2000-01-03"
EXTREME = 0.5


def verifier_prix(racine):
    raw = racine / "data/raw"
    m = json.loads((raw / "prix_temoin_manifest.json").read_text(encoding="utf-8"))
    attendus = {e["fichier"] for e in m["prix"]}
    if attendus != {p.name for p in (raw / "prix_temoin").glob("*.csv.gz")}:
        raise ValueError("Inventaire du témoin différent du manifeste.")
    for e in m["prix"]:
        if not correspond(raw / "prix_temoin" / e["fichier"], e["sha256"]):
            raise ValueError(f"Empreinte invalide : {e['fichier']}")


def membres_temoin(decisions):
    sort = decisions[decisions.verdict == "SORT"]
    lignes = []
    for r in sort.itertuples():
        titres = r.symboles.replace(".", "-").split("|")
        for titre in titres:
            lignes.append({"entreprise": r.nom, "cik": r.cik, "titre": titre,
                           "classes": len(titres), "secteur": r.secteur})
    return pd.DataFrame(lignes)


def ponderation_sectorielle(parts):
    """Poids par secteur fixés à ceux de P1, égaux entre entreprises d'un secteur."""
    def ponderer(groupe, admis):
        vivants = groupe[groupe.titre.isin(admis)]
        presents = parts[parts.index.isin(vivants.secteur)]
        presents = presents / presents.sum()
        poids = {}
        for secteur, part in presents.items():
            bloc = vivants[vivants.secteur == secteur]
            for titre, w in poids_cibles(bloc, list(bloc.titre)).items():
                poids[titre] = part * w
        return poids
    return ponderer


def completer_seances(prix, dates):
    """Ajoute les séances du calendrier absentes chez Yahoo, sans cours ni dividende."""
    periode = dates[(dates >= prix.index[0]) & (dates <= prix.index[-1])]
    manquantes = periode.difference(prix.index)
    if len(manquantes):
        vide = pd.DataFrame({"Close": np.nan, "Volume": 0.0, "Dividends": 0.0,
                             "Open": np.nan, "High": np.nan, "Low": np.nan}, index=manquantes)
        prix = pd.concat([prix, vide]).sort_index()
    return prix, len(manquantes)


def statistiques(nom, niveau, sans_risque, marche):
    r = niveau.pct_change().dropna()
    m = marche.pct_change().reindex(r.index)
    ok = m.notna()
    return {"serie": nom,
            "annualise": risque.annualiser_rendement(niveau),
            "volatilite": risque.volatilite(r),
            "sharpe": risque.sharpe(r, sans_risque),
            "sortino": risque.sortino(r, sans_risque),
            "repli_max": risque.drawdown(niveau)["repli_max"],
            "var99": risque.var_historique(r, 0.99),
            "perte_au_dela_99": risque.perte_au_dela(r, 0.99),
            "beta_spy": float(np.polyfit(m[ok], r[ok], 1)[0])}


def correlation_moyenne(rendements, masque=None, minimum=250):
    bloc = rendements if masque is None else rendements.loc[masque]
    matrice = bloc.corr(min_periods=minimum).to_numpy()
    paires = matrice[np.triu_indices_from(matrice, 1)]
    return float(np.nanmean(paires))


def construire(racine=RACINE, cout=COUT):
    racine = Path(racine).resolve()
    raw, processed = racine / "data/raw", racine / "data/processed"
    verifier_prix(racine)
    verifier(processed, racine)
    verifier_manifeste(processed / "risque_manifest.json", racine)
    dates = pd.Index(pd.read_csv(raw / "calendrier_bourse.csv").date.astype(str), name="date")
    dates = dates[dates >= DEBUT]
    annuel = set(pd.Series(dates).groupby(pd.Series(dates).str[:4]).min())
    fins = set(pd.Series(dates).groupby(pd.Series(dates).str[:7]).max())
    decisions = pd.read_csv(racine / "data/review/decisions_selection.csv", dtype=str)
    membres = membres_temoin(decisions)

    prepares, qualite = {}, []
    for titre in membres.titre:
        brut = lire_prix(raw / "prix_temoin" / f"{titre}.csv.gz")
        brut, completees = completer_seances(brut, dates)
        p = preparer_prix(brut).reindex(dates)
        rendements = p.rendement_valorisation.dropna()
        qualite.append({"titre": titre, "premier_cours": p.index[p.disponible.fillna(False).astype(bool)].min(),
                        "dernier_cours": brut.index[-1], "seances_completees": completees,
                        "cours_portes": int(p.cours_porte.fillna(False).sum()),
                        "variations_extremes": int((rendements.abs() > EXTREME).sum())})
        prepares[titre] = p
    qualite = pd.DataFrame(qualite)
    arretes = qualite[qualite.dernier_cours != dates[-1]]
    if len(arretes):
        raise ValueError(f"Historiques arrêtés avant la fin : {sorted(arretes.titre)}")

    r = pd.DataFrame({t: p.rendement_valorisation for t, p in prepares.items()}, index=dates)
    d = pd.DataFrame({t: p.dividende for t, p in prepares.items()}, index=dates)
    dispo = pd.DataFrame({t: p.disponible for t, p in prepares.items()}, index=dates).fillna(False).astype(bool)
    premiers = {t: dispo.index[dispo[t]][0] for t in dispo}

    entre = decisions[decisions.verdict == "ENTRE"]
    parts = entre.secteur.value_counts() / len(entre)
    if not set(parts.index) <= set(membres.secteur):
        raise ValueError("Un secteur du thème n'a aucune entreprise témoin.")
    cibles, valeurs, photos, journaux, resumes, reports = [], {}, [], [], [], []
    for pf, ponderer in [("T1", poids_cibles), ("T1S", ponderation_sectorielle(parts))]:
        simuler_groupe(pf, membres.assign(portefeuille=pf), dates, annuel, fins, dispo, premiers,
                       r, d, cout, cibles, valeurs, photos, journaux, resumes, reports, ponderer=ponderer)
    valeurs = pd.DataFrame(valeurs, index=dates)
    photos = pd.concat(photos, ignore_index=True)
    sommes = photos.groupby(["date", "serie"]).poids.sum()
    if not np.allclose(sommes, 1, rtol=0, atol=1e-12) or photos.poids.lt(0).any():
        raise ArithmeticError("Les poids du témoin sont invalides.")

    # Comparaison avec le thème, sur les mêmes conventions que l'étape 3.
    theme = pd.read_csv(processed / "valeurs_portefeuilles.csv", index_col=0)
    marche = pd.read_csv(processed / "valeurs_comparaisons.csv", index_col=0)["SPY"]
    taux = pd.read_csv(raw / "taux_sans_risque.csv", index_col=0)["taux_annuel_pct"].reindex(dates).ffill()
    sans_risque = (1 + taux / 100) ** (1 / 252) - 1
    series = {**{s: theme[s] for s in ["P1_reeq", "P1_cons"]}, **{s: valeurs[s] for s in valeurs}}
    comparaison = []
    for depuis in [None, "2004-08-19"]:
        for nom, niveau in series.items():
            n = niveau.dropna() if depuis is None else niveau.dropna().loc[depuis:]
            ligne = statistiques(nom, n, sans_risque, marche)
            ligne["periode"] = "complete" if depuis is None else f"depuis_{depuis}"
            comparaison.append(ligne)
    comparaison = pd.DataFrame(comparaison)

    episodes = pd.read_csv(processed / "episodes_tension.csv")
    tension = pd.Series(False, index=dates)
    for e in episodes.itertuples():
        tension.loc[e.debut:e.creux] = True
    rendements_theme = pd.read_csv(processed / "rendements_valorisation.csv", index_col=0)
    titres_p1 = pd.read_csv(processed / "appartenance.csv").query("portefeuille == 'P1'").titre
    correlations = []
    for nom, bloc in [("P1", rendements_theme[list(titres_p1)]), ("T1", r)]:
        rho = correlation_moyenne(bloc)
        rho_calme = correlation_moyenne(bloc, (~tension).values, 100)
        rho_tension = correlation_moyenne(bloc, tension.values, 100)
        n = bloc.shape[1]
        correlations.append({"groupe": nom, "titres": n, "rho_moyen": rho,
                             "n_effectif": risque.n_effectif(rho, n),
                             "rho_calme": rho_calme, "rho_tension": rho_tension,
                             "n_effectif_calme": risque.n_effectif(rho_calme, n),
                             "n_effectif_tension": risque.n_effectif(rho_tension, n)})
    correlations = pd.DataFrame(correlations)

    sorties = {"temoin_valeurs.csv": (valeurs, True),
               "temoin_mesures.csv": (pd.DataFrame(resumes), False),
               "temoin_qualite.csv": (qualite, False),
               "temoin_comparaison.csv": (comparaison, False),
               "temoin_correlations.csv": (correlations, False)}
    for nom, (df, index) in sorties.items():
        df.to_csv(processed / nom, index=index, encoding="utf-8")
    entrees = [raw / "prix_temoin_manifest.json", raw / "calendrier_bourse.csv",
               raw / "taux_sans_risque.csv", racine / "data/review/decisions_selection.csv",
               processed / "pipeline_portefeuilles.json", processed / "risque_manifest.json",
               *[racine / "src" / nom for nom in ("construire_temoin.py", "construire_portefeuilles.py",
                                                  "portefeuille.py", "risque.py", "empreintes.py")]]
    manifeste = ecrire_manifeste(
        processed / "temoin_manifest.json", racine, entrees, [processed / nom for nom in sorties],
        commande="python -m src.construire_temoin", cout=cout,
        titres=len(membres), entreprises=int(membres.cik.nunique()),
        parts_sectorielles_2026=parts.round(6).to_dict(),
        seances_completees=int(qualite.seances_completees.sum()),
        variations_extremes=int(qualite.variations_extremes.sum()))
    return comparaison, correlations, manifeste


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cout", type=float, default=COUT)
    comparaison, correlations, manifeste = construire(cout=parser.parse_args().cout)
    pd.set_option("display.width", 200)
    print(comparaison.round(4).to_string(index=False))
    print()
    print(correlations.round(4).to_string(index=False))
    print()
    print({k: v for k, v in manifeste.items() if not k.endswith("_sha256")})


if __name__ == "__main__":
    main()
