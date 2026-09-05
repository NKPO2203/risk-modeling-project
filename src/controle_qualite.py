"""Contrôles déclarés de qualité ; une alerte n'est pas une preuve d'erreur.

La fonction controler_base est pure. main produit un nouveau contrôle lié par
SHA-256 à la base effectivement examinée, ainsi qu'un registre de couverture.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import pandas as pd

RACINE = Path(__file__).resolve().parents[1]
ENTREE = RACINE / 'data/processed/base_selection.csv'
SORTIE = RACINE / 'data/processed/controle_qualite.csv'
MANIFESTE = RACINE / 'data/review/comptabilite_controle_manifest.json'
METRIQUES = ('chiffre_affaires', 'capex', 'rd')
COLONNES = ['cik', 'nom', 'symboles', 'secteur', 'annee', 'periode_id', 'periode_fin', 'metrique', 'test', 'detail', 'gravite']


def controler_base(b, constituants=None):
    """Renvoie les alertes sans modifier b ni écrire de fichiers."""
    ordre = 'periode_fin' if 'periode_fin' in b else 'annee'
    b = b.copy().sort_values(['cik', ordre])
    alertes = []
    def signaler(r, test, detail='', metric='', gravite='revue'):
        alertes.append({**{c: r.get(c, '') for c in COLONNES[:7]},
                        'metrique': metric, 'test': test, 'detail': str(detail), 'gravite': gravite})
    if b.empty:
        return pd.DataFrame(columns=COLONNES)
    for _, r in b.iterrows():
        ca = r.chiffre_affaires
        for metric in METRIQUES:
            v = r[metric]
            if pd.isna(v):
                continue
            if v < 0 or (metric == 'chiffre_affaires' and v == 0):
                signaler(r, 'valeur négative ou ventes nulles', f'{v:g}', metric)
            if r.get(f'statut_{metric}', '') == 'revue_requise':
                signaler(r, 'valeur non réconciliée', r.get(f'{metric}_motif_qualite', ''), metric)
            if r.get(f'comparabilite_{metric}', '') == 'hors_perimetre_actuel':
                signaler(r, 'périmètre historique non comparable', r.get(f'{metric}_motif_qualite', ''), metric)
            if r.get(f'{metric}_changement_etiquette', '') == 'oui':
                signaler(r, "changement d'étiquette", r.get(f'{metric}_motif_qualite', ''), metric)
            debut, fin = r.get(f'{metric}_debut'), r.get(f'{metric}_fin')
            if pd.notna(debut) and pd.notna(fin) and debut and fin:
                jours = (pd.Timestamp(fin) - pd.Timestamp(debut)).days
                if not 330 <= jours <= 400:
                    signaler(r, 'durée hors intervalle annuel', jours, metric)
            if not r.get(f'{metric}_depot') or pd.isna(r.get(f'{metric}_depot')):
                signaler(r, 'provenance absente', 'Dépôt manquant', metric)
        if pd.notna(ca) and ca > 0:
            if pd.notna(r.capex) and r.capex / ca > 1:
                signaler(r, 'investissement supérieur au chiffre d affaires', f'{r.capex/ca:.3f}', 'capex')
            if pd.notna(r.rd) and r.rd / ca > .5:
                signaler(r, 'recherche supérieure à la moitié du chiffre d affaires', f'{r.rd/ca:.3f}', 'rd')
        if pd.notna(r.get('ca_ecart_relatif')) and r.ca_ecart_relatif > .05:
            signaler(r, 'étiquettes de revenu en désaccord', f'{r.ca_ecart_relatif:.3f}', 'chiffre_affaires')
        dates = {str(r.get(f'{m}_debut')) + '/' + str(r.get(f'{m}_fin')) for m in METRIQUES if pd.notna(r[m]) and pd.notna(r.get(f'{m}_fin'))}
        if len(dates) > 1:
            signaler(r, 'périodes des métriques différentes', ' | '.join(sorted(dates)))
    for _, g in b.groupby('cik'):
        g = g.sort_values(ordre)
        dernier = g.iloc[-1]
        for metric in METRIQUES:
            serie = g.dropna(subset=[metric])
            if serie.empty:
                signaler(dernier, 'métrique absente sur tout l historique', '', metric, 'couverture')
                continue
            if pd.isna(dernier[metric]):
                signaler(dernier, 'métrique absente au dernier exercice', f'Dernière année disponible : {int(serie.annee.max())}', metric, 'couverture')
            if ordre == 'annee':
                attendues = set(range(int(serie.annee.min()), int(serie.annee.max()) + 1))
                trous = sorted(attendues - set(serie.annee.astype(int)))
                if trous:
                    signaler(dernier, 'trou dans la série', trous, metric, 'couverture')
            if serie.annee.max() < 2024:
                signaler(dernier, 'dernier exercice trop ancien', int(serie.annee.max()), metric, 'couverture')
            precedent = None
            for _, r in serie.iterrows():
                intervalle = ((pd.Timestamp(r.periode_fin)-pd.Timestamp(precedent.periode_fin)).days
                              if precedent is not None and ordre == 'periode_fin' else None)
                if intervalle is not None and intervalle > 400:
                    signaler(r, 'trou dans la série', f'{precedent.periode_fin} -> {r.periode_fin}', metric, 'couverture')
                consecutif = (330 <= intervalle <= 400) if intervalle is not None else (precedent is not None and r.annee - precedent.annee == 1)
                if precedent is not None and consecutif:
                    ancien = precedent[metric]
                    if ancien == 0 and r[metric] != 0:
                        signaler(r, 'passage depuis zéro', f'0 -> {r[metric]:g}', metric)
                    elif ancien > 0:
                        variation = r[metric] / ancien - 1
                        if variation > 2 or variation < -.6:
                            signaler(r, 'rupture de série à vérifier', f'{variation:+.1%}', metric)
                precedent = r
    if constituants is not None:
        couverts = set(b.cik.astype(str).str.zfill(10))
        for _, r in constituants.drop_duplicates('CIK').iterrows():
            if str(r.CIK).zfill(10) not in couverts:
                signaler({'cik': str(r.CIK).zfill(10), 'nom': r.Security, 'symboles': r.Symbol, 'secteur': r['GICS Sector']},
                         'entreprise sans données comptables', 'Aucune ligne dans la base', gravite='couverture')
    return pd.DataFrame(alertes, columns=COLONNES).sort_values(['test', 'nom', 'annee', 'metrique']).reset_index(drop=True)


def main():
    b = pd.read_csv(ENTREE, dtype={'cik': str})
    constituants = pd.read_csv(RACINE / 'data/raw/sp500_constituents.csv', dtype={'CIK': str})
    a = controler_base(b, constituants)
    a.to_csv(SORTIE, index=False, encoding='utf-8')
    MANIFESTE.parent.mkdir(parents=True, exist_ok=True)
    sources = {}
    for path in [ENTREE, RACINE/'data/raw/sec_facts_raw.csv', RACINE/'data/review/comptabilite_exceptions.json']:
        if path.exists():
            sources[str(path.relative_to(RACINE))] = hashlib.sha256(path.read_bytes()).hexdigest()
    manifest = {'produit_le': datetime.now(timezone.utc).isoformat(), 'sources_sha256': sources,
                'lignes_base': len(b), 'entreprises_base': int(b.cik.nunique()), 'alertes': len(a),
                'portee': "Vraisemblance et couverture ; ne certifie pas l'exactitude de tous les comptes ni la causalité IA.",
                'par_test': a.groupby('test').size().to_dict()}
    MANIFESTE.write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(f'{len(a)} alertes ; {b.cik.nunique()} entreprises couvertes ; manifeste lié à la base par SHA-256')


if __name__ == '__main__':
    main()
