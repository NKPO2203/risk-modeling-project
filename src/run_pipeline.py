"""Reconstruire et contrôler les résultats locaux, sans accès réseau.

Les collectes sont des opérations distinctes. Le manifeste de succès n'est
publié qu'après les étapes et contrôles ; un échec laisse un statut explicite.
"""
from pathlib import Path
import argparse
import hashlib
import importlib.metadata
import json
import subprocess
import sys

import numpy as np
import pandas as pd

RACINE = Path(__file__).resolve().parents[1]
PROCESSED = RACINE / "data" / "processed"
ETAPES = (
    "build_text_ranking.py", "classification_manuelle.py",
    "build_screening_base.py", "controle_qualite.py", "corroboration.py",
)
SORTIES = (
    "classement_texte.csv", "classification_manuelle.csv", "univers_retenu.csv",
    "base_selection.csv", "base_selection_anomalies.csv", "controle_qualite.csv",
    "corroboration.csv", "corroboration_details.csv", "corroboration_sensibilite.csv",
)


def lire(nom):
    return pd.read_csv(PROCESSED / nom, dtype={"cik": str})


def ecrire_json(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps(obj, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    temp.replace(path)


def empreinte(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verifier_sources_locales():
    raw = RACINE / "data/raw"
    manifeste = json.loads((raw / "filings_manifest.json").read_text(encoding="utf-8"))
    if set(manifeste["files"]) != {"filings_termes.csv", "filings_phrases.csv", "filings_log.csv"}:
        raise ValueError("Le manifeste documentaire ne décrit pas les trois CSV attendus.")
    for nom, info in manifeste["files"].items():
        if empreinte(raw / nom) != info["sha256"]:
            raise ValueError(f"Corpus incomplet ou modifié après publication : {nom}")
    termes = pd.read_csv(raw / "filings_termes.csv", dtype={"cik": str}, keep_default_na=False)
    for _, ligne in termes[termes.couverture == "vocabulaire_complet"].iterrows():
        path = (RACINE / ligne.cache_metadata).resolve()
        if not path.is_relative_to((raw / "filings_text").resolve()):
            raise ValueError("Un cache sort du dossier documentaire attendu.")
        meta = json.loads(path.read_text(encoding="utf-8"))
        for cle in ("depot", "source_cik", "source_url", "texte_sha256", "html_sha256"):
            if meta[cle] != ligne[cle]:
                raise ValueError(f"Métadonnées incohérentes : {ligne.cik} {cle}")
        for ext, cle in ((".txt", "texte_sha256"), (".html", "html_sha256")):
            if empreinte(path.with_suffix(ext)) != ligne[cle]:
                raise ValueError(f"Cache documentaire altéré : {ligne.cik} {ext}")


def verifier_manifeste():
    statut = json.loads((PROCESSED / "pipeline_status.json").read_text(encoding="utf-8"))
    if statut.get("statut") != "termine":
        raise ValueError("La dernière exécution n'est pas terminée.")
    manifeste = json.loads((PROCESSED / "pipeline_manifest.json").read_text(encoding="utf-8"))
    for groupe in ("entrees_sha256", "sorties_sha256"):
        for nom, attendu in manifeste[groupe].items():
            chemin = (RACINE / nom).resolve()
            if not chemin.is_relative_to(RACINE.resolve()) or not chemin.is_file() or empreinte(chemin) != attendu:
                raise ValueError(f"Le fichier a changé depuis le calcul : {nom}. Relancer le pipeline.")


def verifier_sorties():
    from build_text_ranking import entreprises_constituantes
    attendus = set(entreprises_constituantes(RACINE / "data/raw/sp500_constituents.csv").cik)
    classement, decisions, univers = map(lire, (
        "classement_texte.csv", "classification_manuelle.csv", "univers_retenu.csv"))
    comptes, corro, details = map(lire, (
        "base_selection.csv", "corroboration.csv", "corroboration_details.csv"))
    for nom, df in (("classement", classement), ("classification", decisions),
                    ("univers", univers), ("corroboration", corro)):
        if df.cik.isna().any() or df.cik.duplicated().any():
            raise ValueError(f"CIK absent ou dupliqué : {nom}")
    if set(classement.cik) != attendus or set(decisions.cik) != attendus:
        raise ValueError("Le classement et la revue doivent conserver tous les CIK de la composition.")
    if not set(decisions.verdict) <= {"ENTRE", "SORT", "DOUTEUX", "A_EXAMINER"}:
        raise ValueError("Verdict absent ou inconnu.")
    if set(univers.cik) != set(decisions.loc[decisions.verdict == "ENTRE", "cik"]):
        raise ValueError("L'univers diffère des décisions appliquées.")
    if not univers.preuve_verifiee.eq("oui").all():
        raise ValueError("Une entreprise retenue n'a pas de preuve retrouvée.")
    if comptes.duplicated(["cik", "periode_fin"]).any():
        raise ValueError("Plusieurs observations comptables pour le même CIK et la même clôture.")
    if set(corro.cik) != set(univers.cik):
        raise ValueError("La description comptable a perdu ou ajouté une entreprise.")
    if set(details.cik) != set(univers.cik) or len(details) != 3 * len(univers) or details.duplicated(["cik", "metrique"]).any():
        raise ValueError("Chaque entreprise doit conserver trois mesures détaillées.")
    for _, r in details[details.multiple.notna()].iterrows():
        obs = json.loads(r.base_observations)
        if not np.isfinite(r.multiple) or r.base_n < 2 or len(obs) != r.base_n:
            raise ValueError(f"Base invalide : {r.cik} {r.metrique}")
        if any(pd.Timestamp(o["fin"]) >= pd.Timestamp(r.debut_recent) for o in obs):
            raise ValueError("Une référence chevauche l'exercice récent ou inclut un exercice futur.")
        if len({o["fin"] for o in obs}) != len(obs):
            raise ValueError("Une période de référence est comptée deux fois.")
        chronologie = sorted(obs, key=lambda o: o["fin"])
        if any(pd.Timestamp(b["debut"]) <= pd.Timestamp(a["fin"]) for a, b in zip(chronologie, chronologie[1:])):
            raise ValueError("Deux références se chevauchent.")
        if any(str(o["perimetre_id"]) != str(r.perimetre_id) for o in obs):
            raise ValueError("Une comparaison traverse deux périmètres.")
        moyenne = np.mean([float(o["valeur"]) for o in obs])
        if moyenne <= 0 or not np.isclose(r.multiple, r.valeur_recente / moyenne):
            raise ValueError("Le multiple n'est pas reproductible à partir de sa référence.")
    for col in ("mult_ventes", "mult_capex", "mult_recherche"):
        if np.isinf(pd.to_numeric(corro[col], errors="coerce")).any():
            raise ValueError("Multiple infini.")
    return decisions, univers, comptes, corro


def compter(serie):
    return {str(k): int(v) for k, v in serie.fillna("non_renseigne").value_counts().sort_index().items()}


def synthese(decisions, univers, comptes, corro):
    raw = RACINE / "data" / "raw"
    termes = pd.read_csv(raw / "filings_termes.csv", dtype={"cik": str})
    phrases = pd.read_csv(raw / "filings_phrases.csv", dtype={"cik": str})
    facts = pd.read_csv(raw / "sec_facts_raw.csv", dtype={"cik": str})
    alertes = lire("controle_qualite.csv")
    resume = {
        "composition_lignes": int(len(pd.read_csv(raw / "sp500_constituents.csv"))),
        "entreprises_composition": int(len(decisions)),
        "comptes_bruts_lignes": int(len(facts)),
        "comptes_lignes": int(len(comptes)),
        "entreprises_avec_comptes": int(comptes.cik.nunique()),
        "rapports_comptes": int(pd.to_numeric(termes.taille_texte, errors="coerce").gt(0).sum()),
        "passages_extraits": int(len(phrases)),
        "verdicts": compter(decisions.verdict),
        "canaux_retenus": compter(univers.canal),
        "degres_retenus": compter(univers.degre),
        "maturites_retenues": compter(univers.maturite_exposition),
        "secteurs_retenus": compter(univers.secteur),
        "mouvements_comptables": compter(corro.corroboration),
        "couverture_comptable": compter(corro.couverture_comptes),
        "replis_de_reference": int(corro.base_repli_utilisee.eq("oui").sum()),
        "alertes_qualite": int(len(alertes)),
        "entreprises_avec_alerte": int(alertes.cik.nunique()),
        "limites": [
            "Composition locale issue d'une source secondaire, non intégralement rapprochée d'un historique officiel.",
            "Revue documentaire des passages repérés ; aucune prétention d'audit intégral de tous les rapports.",
            "Comparabilité sous les contrôles déclarés, sans garantie d'absence de restructuration non détectée.",
            "Photographie actuelle, pas un univers historique investissable sans anticipation.",
            "Mouvements comptables descriptifs, sans attribution causale à l'IA.",
        ],
    }
    ecrire_json(PROCESSED / "etat_projet.json", resume)
    texte = ["# Résultats recalculés", "",
             "Cette page est produite par `src/run_pipeline.py` à partir des CSV locaux.",
             "Les limites et la règle de lecture figurent dans `research/selection_rule.md`.", ""]
    for key, value in resume.items():
        if isinstance(value, dict):
            texte += ["## " + key, "", "| Catégorie | Nombre |", "|---|---:|"]
            texte += [f"| {k} | {v} |" for k, v in value.items()]
            texte.append("")
        elif isinstance(value, int):
            texte.append(f"- {key} : {value}")
    (PROCESSED / "synthese_resultats.md").write_text("\n".join(texte) + "\n", encoding="utf-8")
    return resume


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-only", action="store_true", help="Vérifier les sorties présentes sans les recalculer.")
    args = parser.parse_args()
    if args.check_only:
        verifier_sources_locales()
        verifier_manifeste()
        verifier_sorties()
        print("Contrôles de cohérence réussis.")
        return
    statut = PROCESSED / "pipeline_status.json"
    ecrire_json(statut, {"statut": "en_cours", "etapes": list(ETAPES)})
    try:
        verifier_sources_locales()
        for nom in ETAPES:
            print(f"Étape : {nom}", flush=True)
            subprocess.run([sys.executable, "-X", "utf8", "-B", str(RACINE / "src" / nom)],
                           cwd=RACINE, check=True)
        resume = synthese(*verifier_sorties())
        inputs = sorted((RACINE / "data/raw").glob("*.csv"))
        inputs += sorted((RACINE / "data/review").glob("decisions*.csv"))
        inputs += sorted((RACINE / "data/review").glob("comptabilite_exceptions*.json"))
        inputs += [p for p in sorted((RACINE / "src").glob("*.py"))
                   if not p.name.startswith("export_")]
        inputs += [RACINE / "data/raw/filings_manifest.json"]
        outputs = [PROCESSED / nom for nom in SORTIES]
        outputs += [PROCESSED / "etat_projet.json", PROCESSED / "synthese_resultats.md"]
        fichiers = lambda chemins: {str(p.relative_to(RACINE)).replace("\\", "/"): empreinte(p)
                                    for p in chemins if p.is_file()}
        manifeste = {
            "statut": "termine", "python": sys.version.split()[0],
            "bibliotheques": {p: importlib.metadata.version(p) for p in ("pandas", "numpy", "lxml")},
            "entrees_sha256": fichiers(inputs), "sorties_sha256": fichiers(outputs),
        }
        ecrire_json(PROCESSED / "pipeline_manifest.json", manifeste)
        ecrire_json(statut, {"statut": "termine", "entreprises_retenues": resume["verdicts"].get("ENTRE", 0)})
        print(json.dumps(resume["verdicts"], ensure_ascii=False))
    except Exception as exc:
        ecrire_json(statut, {"statut": "echec", "erreur": str(exc),
                            "instruction": "Ne pas présenter les sorties comme une exécution complète ; corriger puis relancer."})
        raise


if __name__ == "__main__":
    main()
