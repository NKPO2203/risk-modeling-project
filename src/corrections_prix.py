"""Corrections sourcées appliquées en mémoire ; les fichiers bruts restent intacts."""
import json
import math
from pathlib import Path


def corriger_prix(titre, prix, regles):
    """Retraite une distribution non monétaire dans les unités du cours.

    Le facteur s'applique strictement avant l'événement, dividendes anciens
    compris : leurs rendements restent identiques. La distribution reclassée
    ne rejoint plus les espèces. Adj Close reste la preuve Yahoo originale,
    inutilisée par le moteur, et n'est pas présenté comme un prix corrigé.
    Les valeurs témoins empêchent notamment une deuxième application.
    """
    p = prix.copy(deep=True)
    for r in sorted((r for r in regles if r['titre'] == titre), key=lambda r: r['date']):
        date = r['date']
        if date not in p.index:
            raise ValueError(f"Événement correctif absent : {titre} {date}")
        i = p.index.get_loc(date)
        if i == 0:
            raise ValueError(f"Correction sans cours précédent : {titre} {date}")
        for trouve, attendu in [(p.Close.iloc[i-1], r['close_avant']),
                                (p.Close.iloc[i], r['close_apres']),
                                (p.Dividends.iloc[i], r['dividende_brut'])]:
            if not math.isclose(float(trouve), attendu, rel_tol=0, abs_tol=1e-7):
                raise ValueError(f"Valeur témoin différente : {titre} {date}")
        facteur = r['facteur_avant']
        if not math.isfinite(facteur) or not 0 < facteur <= 1:
            raise ValueError(f"Facteur correctif invalide : {titre} {date}")
        cols = ['Open', 'High', 'Low', 'Close', 'Dividends']
        p.loc[p.index < date, cols] *= facteur
        p.loc[date, 'Dividends'] = 0.0
    return p


def lire_corrections(racine):
    return json.loads((Path(racine) / 'data/review/corrections_evenements_prix.json').read_text(encoding='utf-8'))
