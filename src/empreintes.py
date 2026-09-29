"""Empreintes SHA-256 et leur vérification indépendante des fins de ligne.

Git convertit les fins de ligne des fichiers texte : un CSV écrit sous Windows
avec CRLF est stocké avec LF, puis rendu avec LF sous Linux ou macOS. Une
empreinte calculée sur les octets bruts échoue alors sur une machine qui n'a
pas produit le fichier, alors que le contenu est identique.

La vérification accepte donc, pour un fichier texte, l'empreinte des octets
tels qu'ils sont, puis celle du même contenu en fins de ligne LF, puis en CRLF.
Un fichier binaire n'est comparé que sur ses octets.

Depuis le 29 septembre 2026, le dépôt stocke et extrait tous ses fichiers texte
en LF (fichier .gitattributes), et `empreinte` calcule celle d'un fichier texte
sur son contenu en LF. Un manifeste écrit sous Windows porte ainsi les mêmes
empreintes qu'un manifeste écrit sous Linux. Les manifestes plus anciens,
écrits sur les octets bruts, restent vérifiables par `correspond`.
"""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json

TEXTE = {".csv", ".json", ".md", ".txt", ".py", ".ipynb", ".html", ".htm"}


def empreinte(path):
    """Empreinte d'un fichier : contenu en LF pour un texte, octets pour un binaire."""
    contenu = path.read_bytes()
    if path.suffix.lower() in TEXTE:
        contenu = contenu.replace(b"\r\n", b"\n")
    return hashlib.sha256(contenu).hexdigest()


def variantes(contenu):
    """Le contenu brut, puis en fins de ligne LF, puis en CRLF."""
    yield contenu
    lf = contenu.replace(b"\r\n", b"\n")
    yield lf
    yield lf.replace(b"\n", b"\r\n")


def correspond(path, attendu):
    """Vrai si le fichier a l'empreinte attendue, aux fins de ligne près pour un texte."""
    contenu = path.read_bytes()
    if path.suffix.lower() not in TEXTE:
        return hashlib.sha256(contenu).hexdigest() == attendu
    return any(hashlib.sha256(v).hexdigest() == attendu for v in variantes(contenu))


def chemin_relatif(path, racine):
    return Path(path).resolve().relative_to(Path(racine).resolve()).as_posix()


def ecrire_manifeste(chemin, racine, entrees, sorties, **infos):
    """Manifeste d'une étape : ses entrées, son code et ses sorties, par empreinte.

    Les chemins sont relatifs à la racine du dépôt, en notation POSIX.
    """
    manifeste = {"statut": "termine",
                 "produit_le": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                 **infos,
                 "entrees_sha256": {chemin_relatif(p, racine): empreinte(Path(p)) for p in entrees},
                 "sorties_sha256": {chemin_relatif(p, racine): empreinte(Path(p)) for p in sorties}}
    Path(chemin).write_text(json.dumps(manifeste, ensure_ascii=False, indent=2) + "\n",
                            encoding="utf-8", newline="\n")
    return manifeste


def verifier_manifeste(chemin, racine):
    """Refuse un manifeste inachevé, ou dont une entrée ou une sortie a changé.

    À appeler avant de lire les sorties d'une étape : un résultat calculé sur
    des fichiers qui ne sont plus ceux de l'étape n'est pas reproductible.
    """
    racine = Path(racine).resolve()
    manifeste = json.loads(Path(chemin).read_text(encoding="utf-8"))
    if manifeste.get("statut") != "termine":
        raise ValueError(f"Étape inachevée : {Path(chemin).name}")
    for groupe in ("entrees_sha256", "sorties_sha256"):
        if not manifeste.get(groupe):
            raise ValueError(f"Manifeste incomplet, {groupe} absent : {Path(chemin).name}")
        for nom, attendu in manifeste[groupe].items():
            p = (racine / nom).resolve()
            if not p.is_relative_to(racine) or not p.is_file() or not correspond(p, attendu):
                raise ValueError(f"{nom} a changé depuis {Path(chemin).name} : relancer l'étape qui le produit.")
    return manifeste
