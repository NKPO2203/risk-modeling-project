"""Vérification des références de la revue de littérature reçue le 29 septembre 2026.

Exécution : python -m src.verifier_bibliographie
Entrée : data/review/bibliographie_revue.csv, qui recopie les références des
deux versions de la revue (dossier research/sources_revue_2026-09-29) avec le
DOI qu'elles donnent, et le DOI corrigé quand le premier est faux.
Sortie : data/review/bibliographie_verification.csv.

Pour chaque DOI, Crossref dit s'il existe et quel article il désigne ; le
premier auteur et le titre sont comparés à la référence citée. Pour les
prépublications, l'API d'arXiv donne le titre et les auteurs. Cette
vérification établit que l'article existe et que la référence le désigne ;
elle ne vérifie pas ce que la revue dit de son contenu.
"""
from pathlib import Path
import re
import time
import unicodedata

import pandas as pd
import requests

RACINE = Path(__file__).resolve().parents[1]
ENTREE = RACINE / "data/review/bibliographie_revue.csv"
SORTIE = RACINE / "data/review/bibliographie_verification.csv"


def _plat(texte):
    texte = re.sub(r"[\u2010-\u2015]", " ", texte or "")
    texte = unicodedata.normalize("NFKD", texte).encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9 ]", " ", texte.lower())


def _demander(url, params=None, essais=4):
    for i in range(essais):
        try:
            r = requests.get(url, params=params, timeout=30)
            if r.status_code not in (429, 500, 502, 503):
                return r
        except requests.RequestException:
            pass
        time.sleep(3 * (i + 1))
    return None


def crossref(doi):
    r = _demander(f"https://api.crossref.org/works/{doi}")
    if r is None or r.status_code != 200:
        return None
    m = r.json()["message"]
    return {"premier_auteur": (m.get("author") or [{}])[0].get("family", ""),
            "titre": (m.get("title") or [""])[0],
            "revue": (m.get("container-title") or [""])[0],
            "annee": (m.get("issued", {}).get("date-parts") or [[None]])[0][0]}


def arxiv(identifiant):
    r = _demander("https://export.arxiv.org/api/query", {"id_list": identifiant})
    if r is None or r.status_code != 200 or "<entry>" not in r.text:
        return None
    entree = r.text.split("<entry>", 1)[1]
    return {"premier_auteur": re.search(r"<name>(.*?)</name>", entree).group(1).split()[-1],
            "titre": re.sub(r"\s+", " ", re.search(r"<title>(.*?)</title>", entree, re.S).group(1)),
            "revue": "arXiv", "annee": int(re.search(r"<published>(\d{4})", entree).group(1))}


def concorde(reference, trouve):
    """Le premier auteur cité et quatre mots du titre trouvé figurent dans la référence."""
    ref = _plat(reference)
    auteur = _plat(trouve["premier_auteur"]).split()
    mots = [m for m in _plat(trouve["titre"]).split() if len(m) > 3][:4]
    return bool(auteur) and auteur[-1] in ref and sum(m in ref for m in mots) >= min(2, len(mots))


def verifier():
    refs = pd.read_csv(ENTREE, dtype=str).fillna("")
    lignes = []
    for r in refs.itertuples():
        ligne = {"n": r.n, "version": r.version, "reference": r.reference, "doi_donne": r.doi_donne,
                 "arxiv": r.arxiv, "doi_corrige": r.doi_corrige}
        if r.arxiv:
            trouve = arxiv(r.arxiv)
            ligne["verdict"] = ("prepublication existante" if trouve and concorde(r.reference, trouve)
                                else "introuvable ou discordant")
        else:
            trouve = crossref(r.doi_donne)
            if trouve and concorde(r.reference, trouve):
                ligne["verdict"] = "DOI correct"
            else:
                ligne["verdict"] = ("DOI d'un autre article" if trouve else "DOI inexistant")
                if r.doi_corrige:
                    corrige = crossref(r.doi_corrige)
                    if corrige and concorde(r.reference, corrige):
                        ligne["verdict"] += ", article existant sous le DOI corrige"
                        trouve = corrige
        if trouve:
            ligne.update({f"trouve_{k}": v for k, v in trouve.items()})
        lignes.append(ligne)
        time.sleep(0.5)
    resultat = pd.DataFrame(lignes)
    resultat.to_csv(SORTIE, index=False, encoding="utf-8", lineterminator="\n")
    return resultat


if __name__ == "__main__":
    res = verifier()
    print(res.groupby(["version", "verdict"]).size().to_string())
    print()
    print(res[~res.verdict.isin(["DOI correct", "prepublication existante"])]
          [["n", "doi_donne", "verdict", "trouve_premier_auteur", "trouve_titre"]].to_string(index=False))
