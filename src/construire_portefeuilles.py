"""Reconstruction locale de l'étape 2, sans collecte ni modification des preuves.

Exécution : python -m src.construire_portefeuilles
Contrôle des empreintes : python -m src.construire_portefeuilles --check-only
"""
from pathlib import Path
import argparse
import hashlib
import importlib.metadata
import json
import re
import shutil
import sys
import tempfile
from datetime import datetime, timezone

import numpy as np
import pandas as pd

from src.portefeuille import COUT, poids_cibles, preparer_prix, simuler
from src.corrections_prix import corriger_prix, lire_corrections

RACINE = Path(__file__).resolve().parents[1]
DEBUT = "2000-01-03"


def empreinte(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def ecrire_json(path, contenu):
    path.write_text(json.dumps(contenu, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")


def verifier_bruts(racine):
    raw = racine / "data/raw"
    m = json.loads((raw / "prix_manifest.json").read_text(encoding="utf-8"))
    sources = [raw / "prix_manifest.json"]
    for groupe in ("prix", "benchmarks"):
        attendus = {e["fichier"] for e in m[groupe]}
        if attendus != {p.name for p in (raw / groupe).glob("*.csv")}:
            raise ValueError(f"Inventaire brut différent du manifeste : {groupe}")
        if len(attendus) != len(m[groupe]):
            raise ValueError(f"Fichier répété dans le manifeste : {groupe}")
        for e in m[groupe]:
            p = raw / groupe / e["fichier"]
            if p.parent.resolve() != (raw / groupe).resolve() or empreinte(p) != e["sha256"]:
                raise ValueError(f"Empreinte brute invalide : {p.name}")
            sources.append(p)
    for groupe in ("calendrier", "actions", "metadonnees"):
        e = m[groupe]
        p = raw / e["fichier"]
        if p.parent.resolve() != raw.resolve() or empreinte(p) != e["sha256"]:
            raise ValueError(f"Empreinte invalide : {groupe}")
        sources.append(p)
    return sources


def lire_prix(path):
    df = pd.read_csv(path)
    df.index = pd.Index(df.date.str[:10], name="date")
    if df.empty or not df.index.is_unique or not df.index.is_monotonic_increasing:
        raise ValueError(f"Historique vide, dupliqué ou désordonné : {path.name}")
    return df


def appartenance(decisions):
    retenues = decisions[decisions.verdict == "ENTRE"]
    if retenues.cik.duplicated().any() or retenues.cik.isna().any():
        raise ValueError("CIK retenu absent ou dupliqué.")
    lignes = []
    for r in retenues.itertuples():
        if r.maturite_exposition not in {"etablie", "engagement_ou_developpement_documente"}:
            raise ValueError(f"Maturité inconnue : {r.cik}, {r.maturite_exposition}")
        if r.canal in {"depense", "depense et vend"}:
            maillon = "P4"
        elif r.canal == "vend":
            maillon = "P5"
        elif r.canal == "fournit":
            maillon = {"Utilities": "P6", "Industrials": "P7", "Real Estate": "P8",
                       "Information Technology": "P9"}.get(r.secteur, "P10")
        else:
            raise ValueError(f"Canal inconnu : {r.cik}, {r.canal}")
        titres = r.symboles.replace(".", "-").split("|")
        if not all(titres) or len(set(titres)) != len(titres):
            raise ValueError(f"Symboles invalides : {r.cik}")
        for pf in ["P1", "P2" if r.maturite_exposition == "etablie" else "P3", maillon]:
            for titre in titres:
                nom = re.sub(r"\s*\(Class [A-Z]\)$", "", r.nom) if len(titres) > 1 else r.nom
                lignes.append({"portefeuille": pf, "entreprise": nom, "cik": r.cik,
                               "titre": titre, "classes": len(titres)})
    membres = pd.DataFrame(lignes)
    if membres.duplicated(["portefeuille", "titre"]).any():
        raise ValueError("Un symbole appartient à plusieurs entreprises.")
    return membres


def annualise(valeurs):
    """252 séances par an ; N niveaux contiennent N-1 rendements."""
    v = valeurs.dropna()
    return float((v.iloc[-1] / v.iloc[0]) ** (252 / (len(v) - 1)) - 1) if len(v) > 1 else None


def construire(racine=RACINE, sortie=None, cout=COUT, controles_prix=True):
    racine = Path(racine).resolve()
    sortie = Path(sortie or racine / "data/processed").resolve()
    if sortie.is_relative_to(racine / "data/raw"):
        raise ValueError("Une reconstruction ne peut jamais écrire dans les données brutes.")
    sources = verifier_bruts(racine)
    raw = racine / "data/raw"
    dates = pd.Index(pd.read_csv(raw / "calendrier_bourse.csv").date.astype(str), name="date")
    dates = dates[dates >= DEBUT]
    if not len(dates) or dates[0] != DEBUT or not dates.is_unique or not dates.is_monotonic_increasing:
        raise ValueError("Calendrier invalide.")
    annuel = set(pd.Series(dates).groupby(pd.Series(dates).str[:4]).min())
    fins = set(pd.Series(dates).groupby(pd.Series(dates).str[:7]).max())
    decisions = pd.read_csv(racine / "data/review/decisions_selection.csv", dtype=str)
    membres = appartenance(decisions)
    prix = {p.stem: lire_prix(p) for p in sorted((raw / "prix").glob("*.csv"))}
    if set(membres.titre) != set(prix):
        raise ValueError("Les fichiers de prix et les symboles retenus diffèrent.")
    for titre, p in prix.items():
        requis = dates[(dates >= p.index[0]) & (dates <= p.index[-1])]
        if not set(requis) <= set(p.index) or p.index[-1] != dates[-1]:
            raise ValueError(f"Séance brute absente ou historique arrêté : {titre}")
    regles = pd.read_csv(racine / "data/review/regles_historiques_prix.csv", dtype=str)
    if regles.titre.duplicated().any() or not set(regles.titre) <= set(prix):
        raise ValueError("Règles d'historique dupliquées ou hors univers.")
    corrections = lire_corrections(racine)
    # Vérifier les corrections sur le cliché complet avant de couper l'histoire.
    # Une correction archivée peut précéder la portion désormais admissible.
    prix = {t: corriger_prix(t, p, corrections) for t, p in prix.items()}
    for regle in regles.itertuples():
        prix[regle.titre] = prix[regle.titre].loc[regle.debut_admissible:]
    prepares = {t: preparer_prix(p).reindex(dates) for t, p in prix.items()}
    matrices = {champ: pd.DataFrame({t: p[champ] for t, p in prepares.items()}, index=dates)
                for champ in ["rendement_observe", "rendement_valorisation", "dividende", "disponible", "cours_porte"]}
    r, d = matrices["rendement_valorisation"], matrices["dividende"]
    dispo = matrices["disponible"].fillna(False).astype(bool)
    # La présence commence au premier cours utilisable, pas au premier rendement.
    premiers = {t: dispo.index[dispo[t]][0] for t in dispo}
    cibles_lignes, valeurs, photos, journaux, resumes, reports = [], {}, [], [], [], []
    for pf, groupe in membres.groupby("portefeuille", sort=True):
        titres = sorted(groupe.titre)
        entreprises = groupe.set_index("titre").cik.to_dict()
        evenements, annuel_effectif = set(), set()
        for demande in sorted(annuel | {premiers[t] for t in titres}):
            # Aucune vente à un cours absent. Toute l'opération est
            # reportée à la première séance où les positions sont négociables.
            effectif = None
            for jour in dates[dates >= demande]:
                admis = [t for t in titres if premiers[t] <= jour]
                if dispo.loc[jour, admis].all():
                    effectif = jour
                    break
            if effectif is None:
                raise ValueError(f"Opération impossible avant la fin de série : {pf}, {demande}")
            evenements.add(effectif)
            if demande in annuel:
                annuel_effectif.add(effectif)
            if effectif != demande:
                reports.append({"portefeuille": pf, "date_prevue": demande, "date_effective": effectif,
                                "motif": "cotation absente, aucune opération au cours porté"})
        evenements = sorted(evenements)
        cibles = []
        for jour in evenements:
            admis = [t for t in titres if premiers[t] <= jour]
            if not dispo.loc[jour, admis].all():
                raise ValueError(f"Cotation absente lors d'une opération : {pf}, {jour}")
            w = poids_cibles(groupe, admis)
            if not w:
                raise ValueError(f"Portefeuille sans titre initial : {pf}")
            cibles.append({t: w.get(t, 0.0) for t in titres})
            for t, poids in w.items():
                cibles_lignes.append({"portefeuille": pf, "date": jour, "titre": t,
                    "entreprise": groupe.set_index("titre").at[t, "entreprise"],
                    "poids": poids, "motif": "annuel" if jour in annuel_effectif else "entree"})
        cible = pd.DataFrame(cibles, index=evenements, columns=titres)
        for reeq, suffixe in [(True, "reeq"), (False, "cons")]:
            nom = pf + "_" + suffixe
            journal = []
            v, rotation, photo = simuler(r, d, titres, cible, dates, annuel_effectif, reeq, cout,
                fins_de_mois=fins, disponibilite=dispo, entreprises=entreprises, journal=journal)
            valeurs[nom] = 100 * v / v.iloc[0]
            ph = photo.rename_axis("date").reset_index().melt("date", var_name="titre", value_name="poids")
            ph["serie"] = nom
            photos.append(ph[["date", "serie", "titre", "poids"]])
            j = pd.DataFrame(journal)
            j["serie"] = nom
            journaux.append(j)
            brut, _, _ = simuler(r, d, titres, cible, dates, annuel_effectif, reeq, 0,
                disponibilite=dispo, entreprises=entreprises)
            resumes.append({"serie": nom, "base100": valeurs[nom].iloc[-1],
                "annualise": annualise(v), "rotation_annuelle": rotation,
                "cout_annualise_pb": 10000 * (annualise(brut) - annualise(v)),
                "repli_maximal": float((v / v.cummax() - 1).min())})
    valeurs = pd.DataFrame(valeurs, index=dates)
    photos, journal = pd.concat(photos, ignore_index=True), pd.concat(journaux, ignore_index=True)
    sommes = photos.groupby(["date", "serie"]).poids.sum()
    if not np.allclose(sommes, 1, rtol=0, atol=1e-12) or photos.poids.lt(0).any():
        raise ArithmeticError("Les poids produits sont invalides.")
    j = journal[journal.valeur_avant > 0]
    ecart = (j.valeur / j.valeur_avant - 1 - j.rendement_attendu_avant_frais + j.frais / j.valeur_avant).abs()
    if not np.isfinite(ecart).all() or ecart.max() > 1e-12:
        raise ArithmeticError("La valeur n'est pas expliquée par les positions, dividendes et frais.")
    if not np.allclose(j.frais, cout * j.echange, rtol=1e-10, atol=1e-14):
        raise ArithmeticError("La facture ne correspond pas aux transactions.")
    # Références homogènes : dividendes du fonds en espèces, réinvestis en janvier.
    # Les valeurs ajustées du fournisseur restent disponibles séparément.
    comparaisons, yahoo = {}, {}
    for fichier in sorted((raw / "benchmarks").glob("*.csv")):
        t = fichier.stem
        p = lire_prix(fichier)
        if not np.isfinite(p['Adj Close']).all() or p['Adj Close'].le(0).any():
            raise ValueError(f"Cours ajusté de comparaison invalide : {t}")
        adj = p['Adj Close'].reindex(dates)
        yahoo[t] = adj / adj.dropna().iloc[0] * 100
        if t not in {"SPY", "RSP"}:
            comparaisons[t] = yahoo[t]
            continue
        ds = dates[dates >= p.index[0]]
        pp = preparer_prix(p).reindex(ds)
        if not pp.disponible.all():
            raise ValueError(f"Observation manquante dans le fonds de comparaison : {t}")
        ja = set(pd.Series(ds).groupby(pd.Series(ds).str[:4]).min())
        cible = pd.DataFrame({t: 1.0}, index=sorted(ja))
        v, _, _ = simuler(pp[["rendement_valorisation"]].rename(columns={"rendement_valorisation": t}),
            pp[["dividende"]].rename(columns={"dividende": t}), [t], cible, ds, ja, False, cout,
            disponibilite=pp[["disponible"]].rename(columns={"disponible": t}))
        comparaisons[t] = v / v.iloc[0] * 100
    qualite = []
    for t, pp in prepares.items():
        for jour in pp.index[pp.cours_porte.fillna(False)]:
            qualite.append({"titre": t, "date": jour, "motif": "dernier cours connu porté",
                "reprise": pp.index[(pp.index > jour) & pp.disponible.fillna(False)].min()})
    resume_controles = {"seances": len(dates), "titres": len(prix), "entreprises": membres.cik.nunique(),
        "series": len(valeurs.columns), "releves_mensuels": len(fins), "lignes_poids": len(photos),
        "ecart_somme_poids": float((sommes - 1).abs().max()), "ecart_identite_quotidienne": float(ecart.max()),
        "cours_portes": len(qualite), "cout": cout,
        "limite": "Identités comptables contrôlées, exactitude des prix non garantie par ces identités."}
    sortie.mkdir(parents=True, exist_ok=True)
    # Les résultats complets sont contrôlés en mémoire avant leur publication.
    with tempfile.TemporaryDirectory(prefix="portefeuilles_") as tmp:
        stage = Path(tmp).resolve()
        tables = {"appartenance.csv": (membres, False), "poids_cibles.csv": (pd.DataFrame(cibles_lignes), False),
            "rendements_prix.csv": (matrices["rendement_observe"], True),
            "rendements_valorisation.csv": (r, True), "dividendes.csv": (d, True),
            "valeurs_portefeuilles.csv": (valeurs, True), "poids_mensuels.csv": (photos, False),
            "journal_portefeuilles.csv": (journal, False), "mesures_portefeuilles.csv": (pd.DataFrame(resumes), False),
            "qualite_valorisation.csv": (pd.DataFrame(qualite, columns=["titre", "date", "motif", "reprise"]), False),
            "operations_reportees.csv": (pd.DataFrame(reports, columns=["portefeuille", "date_prevue", "date_effective", "motif"]), False),
            "valeurs_comparaisons.csv": (pd.DataFrame(comparaisons, index=dates), True),
            "valeurs_comparaisons_yahoo.csv": (pd.DataFrame(yahoo, index=dates), True)}
        for nom, (df, index) in tables.items():
            df.to_csv(stage / nom, index=index, encoding="utf-8")
        ecrire_json(stage / "controles_portefeuilles.json", resume_controles)
        if controles_prix:
            from src.controle_prix import controler
            controler(racine, stage)
        sources += [racine / p for p in ["data/review/decisions_selection.csv", "data/review/regles_historiques_prix.csv", "data/raw/sp500_constituents.csv",
            "data/raw/premieres_cotations.csv", "requirements.txt", "src/portefeuille.py", "src/construire_portefeuilles.py",
            "src/controle_prix.py", "src/construire_portefeuille.ipynb", "src/controler_prix.ipynb",
            "tests/test_portefeuille.py", "tests/test_audit_portefeuilles.py", "research/portefeuilles.md"]]
        sources += sorted((racine / "tests").glob("test_pipeline_portefeuilles.py"))
        sources += [racine / p for p in ['src/corrections_prix.py',
            'src/recouper_prix.py', 'data/review/corrections_evenements_prix.json',
            'tests/test_corrections_prix.py']]
        fichiers = sorted(stage.iterdir())
        manifeste = {"statut": "termine", "produit_le": datetime.now(timezone.utc).isoformat(),
            "python": sys.version.split()[0], "bibliotheques": {p: importlib.metadata.version(p) for p in ["pandas", "numpy"]},
            "commande": "python -m src.construire_portefeuilles", "regles": resume_controles,
            "entrees_sha256": {str(p.relative_to(racine)).replace('\\', '/'): empreinte(p) for p in sources},
            "sorties_sha256": {p.name: empreinte(p) for p in fichiers}}
        for p in fichiers:
            shutil.copyfile(p, sortie / p.name)
        ecrire_json(sortie / "pipeline_portefeuilles.json", manifeste)
    return resume_controles


def verifier(sortie, racine=RACINE):
    sortie, racine = Path(sortie).resolve(), Path(racine).resolve()
    verifier_bruts(racine)
    manifeste = json.loads((sortie / "pipeline_portefeuilles.json").read_text(encoding="utf-8"))
    if manifeste.get("statut") != "termine":
        raise ValueError("Reconstruction non terminée.")
    obligatoires = {"valeurs_portefeuilles.csv", "poids_mensuels.csv", "appartenance.csv",
                   "valeurs_comparaisons.csv", "rendements_valorisation.csv", "journal_portefeuilles.csv",
                   "mesures_portefeuilles.csv", "controles_portefeuilles.json"}
    if not obligatoires <= set(manifeste.get("sorties_sha256", {})) or not manifeste.get("entrees_sha256"):
        raise ValueError("Manifeste incomplet.")
    for nom, attendu in manifeste["entrees_sha256"].items():
        p = (racine / nom).resolve()
        if not p.is_relative_to(racine.resolve()) or empreinte(p) != attendu:
            raise ValueError(f"Entrée modifiée depuis le calcul : {nom}")
    for nom, attendu in manifeste["sorties_sha256"].items():
        p = (sortie / nom).resolve()
        if p.parent != sortie.resolve() or empreinte(p) != attendu:
            raise ValueError(f"Sortie modifiée depuis le calcul : {nom}")
    return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-only", action="store_true")
    parser.add_argument("--output", type=Path, default=RACINE / "data/processed")
    parser.add_argument("--cout", type=float, default=COUT)
    args = parser.parse_args()
    if args.check_only:
        verifier(args.output)
        print("Empreintes de l'étape 2 vérifiées.")
    else:
        print(json.dumps(construire(sortie=args.output, cout=args.cout), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
