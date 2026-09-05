"""Applique un registre de decisions documentees identifiees par CIK.

Le registre data/review/decisions_selection.csv est une entree : ce script ne
le reecrit jamais. Un rang ne peut plus transmettre le jugement d'une societe
a une autre. Toute entreprise sans decision ou sans preuve verifiable reste
A_EXAMINER ; une absence de preuve n'est pas une preuve d'absence d'exposition.
"""

from pathlib import Path
import hashlib
import re

import pandas as pd

RACINE = Path(__file__).resolve().parents[1]
REGISTRE = RACINE / "data" / "review" / "decisions_selection.csv"
VERDICTS = {"ENTRE", "SORT", "DOUTEUX", "A_EXAMINER"}
CHAMPS_REGISTRE = [
    "cik", "verdict", "canal", "degre", "motif", "depot", "phrase_decisive",
    "source_url", "maturite_exposition", "statut_revue", "limite_preuve", "revue_le",
]


def normaliser_espaces(texte):
    return re.sub(r"\s+", " ", texte).strip()


def appliquer_decisions(classement, decisions, phrases, termes, textes=None):
    cl, d, p, t = (x.copy().fillna("") for x in (classement, decisions, phrases, termes))
    for table in (cl, d, p, t):
        table["cik"] = table["cik"].astype(str).str.zfill(10)
    if cl.cik.duplicated().any() or d.cik.duplicated().any() or t.cik.duplicated().any():
        raise ValueError("Les CIK du classement, du registre et des rapports doivent etre uniques")
    manque = set(CHAMPS_REGISTRE) - set(d.columns)
    if manque:
        raise ValueError(f"Champs absents du registre : {sorted(manque)}")
    if not set(d.verdict).issubset(VERDICTS):
        raise ValueError("Verdict inconnu dans le registre")
    # Compatibilite avec l'ancien extracteur : le depot est joint par CIK.
    if "depot" not in p:
        p = p.merge(t[["cik", "depot"]], on="cik", how="left", validate="many_to_one")
    preuves = p.groupby(["cik", "depot"])["phrase"].agg(list).to_dict()
    urls = t.set_index("cik")["source_url"].to_dict() if "source_url" in t else {}
    r = cl.merge(d[CHAMPS_REGISTRE].rename(columns={"depot": "depot_preuve", "source_url": "source_url_preuve"}),
                 on="cik", how="left", validate="one_to_one").fillna("")
    r["verdict_registre"] = r["verdict"]
    r["preuve_verifiee"] = "non"
    r["support_verification"] = ""
    for idx, row in r.iterrows():
        if not row["verdict"]:
            r.loc[idx, "verdict"] = "A_EXAMINER"
            r.loc[idx, "motif"] = "Aucune decision documentee pour ce CIK dans le registre."
            r.loc[idx, "statut_revue"] = "a_completer"
            continue
        # La citation reste litterale ; une nouvelle segmentation peut seulement
        # ajouter du contexte autour. Aucun rapprochement semantique n'est admis.
        passages = preuves.get((row.cik, row.depot_preuve), [])
        citation = normaliser_espaces(row.phrase_decisive)
        dans_passage = bool(citation and any(citation in normaliser_espaces(phrase) for phrase in passages))
        texte = (textes or {}).get((row.cik, row.depot_preuve), "")
        dans_texte = bool(citation and texte and citation in normaliser_espaces(texte))
        url_courante = urls.get(row.cik, "")
        url_index = (url_courante.rsplit("/", 1)[0] + "/" + row.depot_preuve + "-index.html") if url_courante else ""
        url_valide = not url_courante or row.source_url_preuve in (url_courante, url_index)
        valide = bool(citation and row.depot_preuve and row.source_url_preuve
                      and url_valide and (dans_passage or dans_texte))
        if valide:
            r.loc[idx, "preuve_verifiee"] = "oui"
            r.loc[idx, "support_verification"] = "passage" if dans_passage else "texte_complet_sha256"
        elif row.verdict != "A_EXAMINER":
            r.loc[idx, "verdict"] = "A_EXAMINER"
            r.loc[idx, "statut_revue"] = "preuve_a_reverifier"
            r.loc[idx, "limite_preuve"] = "La preuve du registre ne correspond pas au corpus courant ; decision conservee dans verdict_registre."
    # Les metadonnees du depot decisif restent distinctes du rapport courant.
    r["depot_courant"] = r.get("depot", "")
    r["depot"] = r["depot_preuve"]
    r["source_url_courante"] = r.get("source_url", "")
    r["source_url"] = r["source_url_preuve"]
    return r.drop(columns=["depot_preuve", "source_url_preuve"]).sort_values("rang")


def charger_textes_verifies(termes, racine=RACINE):
    """Charge seulement le cache local dont l'empreinte est celle du corpus."""
    textes = {}
    for row in termes.to_dict("records"):
        if not row.get("cache_metadata") or not row.get("texte_sha256"):
            continue
        fichier = (racine / row["cache_metadata"]).with_suffix(".txt").resolve()
        if not fichier.is_relative_to((racine / "data/raw/filings_text").resolve()):
            raise ValueError("Texte cache hors du repertoire des rapports")
        if not fichier.exists():
            continue
        contenu = fichier.read_bytes()
        if hashlib.sha256(contenu).hexdigest() != row["texte_sha256"]:
            raise ValueError(f"Empreinte du texte cache incorrecte : {row['cik']}")
        textes[(str(row["cik"]).zfill(10), row["depot"])] = contenu.decode("utf-8")
    return textes


def main():
    raw, processed = RACINE / "data" / "raw", RACINE / "data" / "processed"
    def lire(path):
        return pd.read_csv(path, dtype={"cik": str}, keep_default_na=False)
    classement = lire(processed / "classement_texte.csv")
    decisions = lire(REGISTRE) if REGISTRE.exists() else pd.DataFrame(columns=CHAMPS_REGISTRE)
    termes = lire(raw / "filings_termes.csv")
    r = appliquer_decisions(classement, decisions, lire(raw / "filings_phrases.csv"),
                            termes, charger_textes_verifies(termes))
    processed.mkdir(parents=True, exist_ok=True)
    r.to_csv(processed / "classification_manuelle.csv", index=False, encoding="utf-8")
    r[r.verdict == "ENTRE"].to_csv(processed / "univers_retenu.csv", index=False, encoding="utf-8")
    print(f"{len(r)} entreprises, CIK conserves ; decisions lues dans {REGISTRE.name}")
    print(r.verdict.value_counts().to_string())
    print(f"{(r.preuve_verifiee == 'oui').sum()} preuves retrouvees exactement dans le corpus courant")


if __name__ == "__main__":
    main()
