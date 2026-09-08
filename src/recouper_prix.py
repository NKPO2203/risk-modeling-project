"""Rejoue hors réseau le rapprochement Yahoo/Nasdaq du 8 septembre 2026.

Exécution : python -m src.recouper_prix
Une concordance de rendements ne certifie ni les unités historiques ni la
liquidité. Une réponse vide et une paire de dates différentes restent absentes.
"""
from pathlib import Path
import hashlib
import json
import numpy as np
import pandas as pd
from src.construire_portefeuilles import lire_prix

ROOT = Path(__file__).resolve().parents[1]
DOSSIER = Path('data/review/sources_cloture_2026-09-08')


def rapprocher(p, n):
    """Compare seulement deux rendements calculés sur les mêmes deux dates."""
    if not n.index.is_unique or not n.index.is_monotonic_increasing:
        raise ValueError('Dates Nasdaq dupliquées ou désordonnées.')
    if not np.isfinite(n).all() or n.le(0).any():
        raise ValueError('Cours Nasdaq absent ou invalide.')
    m = pd.DataFrame({'nasdaq': n, 'yahoo': p.Close, 'split': p['Stock Splits'],
                      'div': p.Dividends}).loc[n.index.intersection(p.index)].copy()
    prev_n = pd.Series(n.index, index=n.index).shift()
    prev_p = pd.Series(p.index, index=p.index).shift()
    meme_paire = prev_n.reindex(m.index).eq(prev_p.reindex(m.index))
    m['rn'] = n.pct_change(fill_method=None).reindex(m.index).where(meme_paire)
    m['ry'] = p.Close.pct_change(fill_method=None).reindex(m.index).where(meme_paire)
    m['ecart_r'] = m.rn - m.ry
    m['ratio_prix'] = m.yahoo / m.nasdaq
    return m


def recouper(root=ROOT):
    root = Path(root)
    dossier = root / DOSSIER
    manifeste = json.loads((dossier/'nasdaq_manifest.json').read_text(encoding='utf-8'))
    rows, couverture = [], []
    for e in manifeste:
        f = (root/e['fichier']).resolve()
        if f.parent != dossier.resolve() or hashlib.sha256(f.read_bytes()).hexdigest() != e['sha256']:
            raise ValueError(f"Preuve Nasdaq modifiée : {e['titre']}")
        z = json.loads(f.read_text(encoding='utf-8'))
        data = z.get('data') or {}
        lignes = (data.get('tradesTable') or {}).get('rows') or []
        if not lignes:
            couverture.append({'titre':e['titre'], 'lignes_nasdaq':0, 'statut':'source_vide'})
            continue
        if len(lignes) != int(data['totalRecords']) or data['symbol'] != e['titre']:
            raise ValueError('Réponse Nasdaq incomplète ou mauvais symbole.')
        n = pd.DataFrame(lignes)
        n.index = pd.to_datetime(n.date,format='%m/%d/%Y').dt.strftime('%Y-%m-%d')
        n = n.sort_index()
        n['cours'] = n.close.str.replace(r'[$,]','',regex=True).astype(float)
        t = e['titre']
        p = lire_prix(root/'data/raw'/('benchmarks' if t in {'SPY','RSP'} else 'prix')/f'{t}.csv')
        m = rapprocher(p, n.cours)
        m['titre'] = t
        rows.append(m.rename_axis('date').reset_index())
        couverture.append({'titre':t, 'lignes_nasdaq':len(n), 'premiere_date':n.index[0],
            'derniere_date':n.index[-1], 'lignes_communes':len(m),
            'rendements_comparables':int(m.ecart_r.notna().sum()),
            'ecart_r_max':m.ecart_r.abs().max(), 'ecarts_sup_10pb':int(m.ecart_r.abs().gt(.001).sum()),
            'statut':'couverture_partielle'})
    a = pd.concat(rows,ignore_index=True)
    a.to_csv(dossier/'comparaison_cours.csv',index=False)
    pd.DataFrame(couverture).to_csv(dossier/'couverture.csv',index=False)
    c = pd.read_csv(root/'data/processed/controle_prix.csv',dtype=str)
    c = c[(c.test=='variation quotidienne extreme') & (c.date>='2000-01-03')].copy()
    c['titre'] = c.fichier.str.removesuffix('.csv')
    c = c.merge(a[['titre','date','nasdaq','yahoo','rn','ry','ecart_r']],on=['titre','date'],how='left')
    c['statut'] = np.where(c.ecart_r.isna(),'non_corroboré',
                          np.where(c.ecart_r.abs()<=.001,'rendement_prix_concordant','divergence'))
    c.loc[(c.titre=='JCI') & (c.date=='2007-07-02'),'statut']='erreur_scission_corrigée_source_SEC'
    c.to_csv(dossier/'variations_examines.csv',index=False)
    a[a.ecart_r.abs()>.001].to_csv(dossier/'divergences.csv',index=False)
    bilan = {'clotures_communes':len(a),'titres':len(couverture),
             'rendements_comparables':int(a.ecart_r.notna().sum()),
             'divergences_sup_10pb':int(a.ecart_r.abs().gt(.001).sum()),
             'variations_extremes':c.statut.value_counts().to_dict(),
             'limite':'Cours de prix comparés ; conventions de scission, dividendes et identité examinées séparément.'}
    (dossier/'bilan.json').write_text(json.dumps(bilan,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    return bilan


if __name__=='__main__':print(json.dumps(recouper(),ensure_ascii=False,indent=2))
