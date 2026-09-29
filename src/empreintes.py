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
import hashlib

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
