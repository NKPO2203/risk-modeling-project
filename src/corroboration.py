"""Décrire les comptes sans valider ni invalider l'exposition à l'IA.

Chaque multiple conserve ses dates, son périmètre et ses sources. Les catégories
portent sur les seules mesures comparables. Une donnée manquante ne vaut pas zéro.
"""
from pathlib import Path
import json
import numpy as np
import pandas as pd

RACINE = Path(__file__).resolve().parents[1]
BASE_DEBUT, BASE_FIN = 2017, 2019
ANNEE_RECENTE_MIN = 2024
SEUIL_NET = 2.0
METRIQUES = {
    "chiffre_affaires": ("ventes", "ca_md"),
    "capex": ("capex", "capex_md"),
    "rd": ("recherche", "rd_md"),
}


def texte(valeur):
    return "" if pd.isna(valeur) else str(valeur)


def normaliser_cik(serie):
    valeurs = serie.astype("string").str.strip()
    if valeurs.isna().any() or not valeurs.str.fullmatch(r"\d{1,10}").all():
        raise ValueError("Chaque entreprise doit avoir un CIK numérique valide.")
    return valeurs.str.zfill(10)


def est_utilisable(ligne, metrique):
    valeur = ligne.get(metrique, np.nan)
    return (
        pd.notna(valeur) and np.isfinite(float(valeur)) and float(valeur) >= 0
        and ligne.get(f"statut_{metrique}") == "observe"
        and ligne.get(f"comparabilite_{metrique}") == "comparable"
        and bool(texte(ligne.get(f"{metrique}_perimetre_id", "")))
    )


def decrire_metrique(groupe, recente, metrique):
    """La base et le repli sont propres à chaque mesure et au même périmètre.

    Le repli utilise deux exercices distincts, strictement antérieurs à la mesure
    récente. Il ne suppose pas que la référence tardive minore la croissance.
    """
    resultat = {
        "metrique": metrique, "annee_recente": int(recente["annee"]),
        "valeur_recente": recente.get(metrique, np.nan),
        "debut_recent": texte(recente.get(f"{metrique}_debut", "")),
        "fin_recent": texte(recente.get(f"{metrique}_fin", "")),
        "depot_recent": texte(recente.get(f"{metrique}_depot", "")),
        "source_recente": texte(recente.get(f"{metrique}_source_url", "")),
        "etiquette_recente": texte(recente.get(
            "ca_etiquette" if metrique == "chiffre_affaires" else f"{metrique}_etiquette", "")),
        "perimetre_id": texte(recente.get(f"{metrique}_perimetre_id", "")),
        "base_annees": "", "base_n": 0, "base_moyenne": np.nan,
        "base_periodes": "",
        "base_repli": False, "base_observations": "[]", "multiple": np.nan,
        "statut_comparaison": "valeur_recente_manquante",
        "motif": texte(recente.get(f"{metrique}_motif_qualite", "")),
    }
    if pd.isna(resultat["valeur_recente"]):
        return resultat
    if not est_utilisable(recente, metrique):
        resultat["statut_comparaison"] = "recent_non_reconcilie"
        return resultat
    debut_recent = pd.to_datetime(recente.get(f"{metrique}_debut"), errors="coerce")
    fins = pd.to_datetime(groupe[f"{metrique}_fin"], errors="coerce")
    if pd.isna(debut_recent):
        resultat["statut_comparaison"] = "periode_recente_invalide"
        return resultat
    # Deux clôtures peuvent partager l'année civile majoritaire. Les dates
    # réelles, sans chevauchement avec la période récente, gouvernent le calcul.
    candidats = groupe[fins < debut_recent].copy()
    if len(candidats):
        candidats = candidats.loc[candidats.apply(lambda r: est_utilisable(r, metrique), axis=1)]
    candidats = candidats[
        candidats[f"{metrique}_perimetre_id"].fillna("") == resultat["perimetre_id"]
    ].sort_values("periode_fin")
    base = candidats[candidats["annee"].between(BASE_DEBUT, BASE_FIN)]
    if len(base) < 2:
        base = candidats.head(2)
        resultat["base_repli"] = True
    resultat["base_n"] = len(base)
    resultat["base_annees"] = ";".join(str(int(a)) for a in base["annee"])
    resultat["base_periodes"] = ";".join(
        f"{r[f'{metrique}_debut']}/{r[f'{metrique}_fin']}" for _, r in base.iterrows())
    observations = []
    for _, ligne in base.iterrows():
        observations.append({
            "annee": int(ligne["annee"]), "valeur": float(ligne[metrique]),
            "debut": texte(ligne.get(f"{metrique}_debut", "")),
            "fin": texte(ligne.get(f"{metrique}_fin", "")),
            "depot": texte(ligne.get(f"{metrique}_depot", "")),
            "source_url": texte(ligne.get(f"{metrique}_source_url", "")),
            "perimetre_id": texte(ligne.get(f"{metrique}_perimetre_id", "")),
        })
    resultat["base_observations"] = json.dumps(observations, ensure_ascii=False)
    if len(base) < 2:
        resultat["statut_comparaison"] = "historique_comparable_insuffisant"
        return resultat
    fin_precedente = None
    for observation in observations:
        debut = pd.to_datetime(observation["debut"], errors="coerce")
        fin = pd.to_datetime(observation["fin"], errors="coerce")
        if pd.isna(debut) or pd.isna(fin) or debut > fin:
            resultat["statut_comparaison"] = "periode_reference_invalide"
            return resultat
        if fin_precedente is not None and debut <= fin_precedente:
            resultat["statut_comparaison"] = "references_chevauchantes"
            return resultat
        fin_precedente = fin
    moyenne = float(base[metrique].mean())
    resultat["base_moyenne"] = moyenne
    if moyenne <= 0:
        resultat["statut_comparaison"] = "base_nulle_ou_negative"
        return resultat
    resultat["multiple"] = float(resultat["valeur_recente"]) / moyenne
    resultat["statut_comparaison"] = (
        "comparable_sur_repli" if resultat["base_repli"] else "comparable_sur_reference"
    )
    return resultat


def niveau_mouvement(multiples, seuil=SEUIL_NET):
    """Une baisse observée reste une baisse si d'autres postes manquent."""
    if seuil <= 1:
        raise ValueError("Le repère de progression doit dépasser 1.")
    connus = [float(x) for x in multiples if pd.notna(x) and np.isfinite(float(x))]
    if not connus:
        return "non evaluable"
    maximum = max(connus)
    if maximum >= seuil:
        return "doublement observe" if seuil == 2 else "seuil atteint"
    if maximum > 1:
        return "progression inferieure au seuil"
    if maximum == 1:
        return "stabilite ou recul observes"
    return "recul des mesures disponibles"


def construire_corroboration(comptes, univers):
    comptes, univers = comptes.copy(), univers.copy()
    comptes["cik"] = normaliser_cik(comptes["cik"])
    univers["cik"] = normaliser_cik(univers["cik"])
    if univers["cik"].duplicated().any() or comptes.duplicated(["cik", "periode_fin"]).any():
        raise ValueError("Doublon d'entreprise ou d'entreprise-exercice.")
    for metrique in METRIQUES:
        for prefixe in ("statut_", "comparabilite_"):
            if f"{prefixe}{metrique}" not in comptes:
                raise ValueError("Base ancienne : relancer build_screening_base.")
    pd.to_datetime(comptes["periode_fin"], errors="raise")
    groupes = {cik: g.sort_values("periode_fin") for cik, g in comptes.groupby("cik")}
    lignes, details = [], []
    for _, entreprise in univers.sort_values("cik").iterrows():
        cik = entreprise["cik"]
        ligne = {champ: entreprise.get(champ, "") for champ in
                 ("cik", "nom", "symboles", "secteur", "canal", "degre")}
        groupe = groupes.get(cik, comptes.iloc[0:0])
        recentes = groupe[groupe["periode_fin"] >= f"{ANNEE_RECENTE_MIN}-01-01"]
        if recentes.empty:
            ligne.update({"annee_recente": np.nan, "corroboration": "non evaluable",
                          "couverture_comptes": "aucune comparaison", "nb_multiples": 0,
                          "base_repli_utilisee": "", "motif_couverture": "aucun exercice recent dans la base"})
            for metrique, (nom, colonne_md) in METRIQUES.items():
                ligne[f"mult_{nom}"] = np.nan
                ligne[colonne_md] = np.nan
                ligne[f"statut_{nom}"] = "aucun_exercice_recent"
                details.append({
                    "cik": cik, "nom": entreprise["nom"], "metrique": metrique,
                    "annee_recente": np.nan, "valeur_recente": np.nan,
                    "debut_recent": "", "fin_recent": "", "depot_recent": "",
                    "source_recente": "", "etiquette_recente": "", "perimetre_id": "",
                    "base_annees": "", "base_periodes": "", "base_n": 0, "base_moyenne": np.nan,
                    "base_repli": False, "base_observations": "[]", "multiple": np.nan,
                    "statut_comparaison": "aucun_exercice_recent",
                    "motif": "aucun exercice recent dans la base",
                })
            ligne["mult_depenses"] = np.nan
            lignes.append(ligne)
            continue
        recente = recentes.iloc[-1]
        ligne["annee_recente"] = int(recente["annee"])
        ligne["fin_exercice_recent"] = recente["periode_fin"]
        calculs = []
        for metrique, (nom, colonne_md) in METRIQUES.items():
            calcul = decrire_metrique(groupe, recente, metrique)
            calculs.append(calcul)
            details.append({"cik": cik, "nom": entreprise["nom"], **calcul})
            ligne[colonne_md] = calcul["valeur_recente"] / 1e9
            ligne[f"mult_{nom}"] = calcul["multiple"]
            ligne[f"base_annees_{nom}"] = calcul["base_annees"]
            ligne[f"base_periodes_{nom}"] = calcul["base_periodes"]
            ligne[f"base_n_{nom}"] = calcul["base_n"]
            ligne[f"base_repli_{nom}"] = "oui" if calcul["base_repli"] else ""
            ligne[f"statut_{nom}"] = calcul["statut_comparaison"]
            ligne[f"fin_{nom}"] = calcul["fin_recent"]
            ligne[f"source_{nom}"] = calcul["source_recente"]
        multiples = [c["multiple"] for c in calculs]
        nombre = sum(pd.notna(x) for x in multiples)
        ligne["nb_multiples"] = nombre
        ligne["couverture_comptes"] = (
            "trois mesures comparables" if nombre == 3 else
            "observation partielle" if nombre else "aucune comparaison"
        )
        ligne["motif_couverture"] = " ; ".join(
            f"{c['metrique']}: {c['statut_comparaison']}" for c in calculs if pd.isna(c["multiple"])
        )
        ligne["base_repli_utilisee"] = "oui" if any(
            c["base_repli"] for c in calculs if pd.notna(c["multiple"])) else ""
        ligne["mult_depenses"] = max(
            (ligne[n] for n in ("mult_capex", "mult_recherche") if pd.notna(ligne[n])),
            default=np.nan)
        ligne["corroboration"] = niveau_mouvement(multiples)
        lignes.append(ligne)
    resultat = pd.DataFrame(lignes) if lignes else pd.DataFrame(columns=[
        "cik", "nom", "corroboration", "couverture_comptes", "base_repli_utilisee",
        "mult_ventes", "mult_capex", "mult_recherche", "nb_multiples",
    ])
    if not resultat.empty:
        resultat = resultat.sort_values(["corroboration", "nom"]).reset_index(drop=True)
    detail = pd.DataFrame(details) if details else pd.DataFrame(columns=[
        "cik", "nom", "metrique", "multiple", "base_observations", "base_n",
        "annee_recente", "perimetre_id", "valeur_recente", "statut_comparaison",
    ])
    return resultat, detail


def sensibilite(resultat):
    lignes = []
    for seuil in (1.5, 2.0, 2.5):
        niveaux = resultat.apply(lambda r: niveau_mouvement(
            [r.get("mult_ventes"), r.get("mult_capex"), r.get("mult_recherche")], seuil), axis=1)
        for niveau, nombre in niveaux.value_counts().sort_index().items():
            lignes.append({"seuil_progression": seuil, "niveau": niveau, "nombre": int(nombre)})
    return pd.DataFrame(lignes, columns=["seuil_progression", "niveau", "nombre"])


def main():
    comptes = pd.read_csv(RACINE / "data/processed/base_selection.csv", dtype={"cik": str})
    univers = pd.read_csv(RACINE / "data/processed/univers_retenu.csv", dtype={"cik": str})
    resultat, details = construire_corroboration(comptes, univers)
    for nom, table in (("corroboration.csv", resultat), ("corroboration_details.csv", details),
                       ("corroboration_sensibilite.csv", sensibilite(resultat))):
        chemin = RACINE / "data/processed" / nom
        temporaire = chemin.with_suffix(".csv.tmp")
        table.to_csv(temporaire, index=False, encoding="utf-8")
        temporaire.replace(chemin)
    print(f"{len(resultat)} entreprises decrites ; aucune exclusion par les comptes.")
    print(resultat["corroboration"].value_counts().to_string())
    print(resultat["couverture_comptes"].value_counts().to_string())


if __name__ == "__main__":
    main()
