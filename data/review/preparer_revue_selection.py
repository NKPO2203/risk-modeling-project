"""Prepare des passages a relire ; ne cree et ne remplace aucune decision.

L'ordre des passages est une aide de lecture, jamais un score d'exposition.
Utilisation : python -B data/review/preparer_revue_selection.py DEBUT FIN
"""
import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = ROOT / 'research/archive/2026-09-05_avant_corrections'

def lire(path):
    with path.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))

def ordre(p):
    text = p['phrase'].lower()
    infrastructure = len(re.findall(r'data.?cent|hyperscal|liquid cooling|ai infrastructure|ai server|ai chip|gpu|high.performance computing', text))
    commercial = len(re.findall(r'our (?:products|customers|sales)|revenue|sales|demand|growth|supply|supplier|sell|sold|provide|orders|backlog|invest|capacity|contract|deliver|manufactur', text))
    interne = len(re.findall(r'cyber|security incident|privacy|legal|regulat|litigat|unauthori|threat|attack|data breach|internal|our (?:operations|employees|workforce)|efficien', text))
    return infrastructure * 5 + commercial * 2 - interne * 3

def dossier():
    ranks = lire(ARCHIVE / 'data/processed/classement_texte.csv')
    old = {r['nom']: r for r in lire(ARCHIVE / 'data/processed/classification_manuelle.csv')}
    texts = lire(ROOT / 'data/raw/filings_phrases.csv')
    grouped = {}
    for p in texts:
        grouped.setdefault(p['cik'].zfill(10), []).append(p)
    result = []
    for r in ranks:
        choices = sorted(grouped.get(r['cik'], []), key=ordre, reverse=True)
        result.append(dict(r, ancien=old[r['nom']], passages=choices))
    return result

if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    start, end = (int(v) for v in sys.argv[1:3])
    for r in dossier():
        if start <= int(r['rang']) <= end:
            print(f"\n{r['rang']} {r['cik']} {r['nom']} [{r['ancien']['verdict']}] ({len(r['passages'])} passages)")
            for i, p in enumerate(r['passages'][:2]):
                print(f"  P{i}: {p['phrase']}")
