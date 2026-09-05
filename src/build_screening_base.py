"""Base comptable traçable. Observe/comparable signifie contrôles satisfaits,
non une vérification manuelle exhaustive. Les montants incertains restent visibles.
"""
from pathlib import Path
import json
import pandas as pd

RACINE = Path(__file__).resolve().parents[1]
ENTREE = RACINE / 'data/raw/sec_facts_raw.csv'
SORTIE = RACINE / 'data/processed/base_selection.csv'
ANOMALIES = RACINE / 'data/processed/base_selection_anomalies.csv'
REGISTRE = RACINE / 'data/review/comptabilite_exceptions.json'
TAXES_INCLUSES = 'RevenueFromContractWithCustomerIncludingAssessedTax'
TOLERANCE_MONTANT = 0.01
METRIQUES = {'chiffre_affaires': 'chiffre_affaires', 'capex': 'investissement', 'rd': 'recherche'}
CLE = ['cik', 'nom', 'symboles', 'secteur', 'sous_secteur', 'annee']


def annee_majoritaire(debut, fin):
    """Année ayant le plus de jours inclus dans la période ; égalité : fin."""
    debut, fin = pd.Timestamp(debut), pd.Timestamp(fin)
    if pd.isna(debut) or pd.isna(fin) or fin < debut:
        raise ValueError('Période comptable invalide')
    jours = {a: (min(fin, pd.Timestamp(a, 12, 31)) - max(debut, pd.Timestamp(a, 1, 1))).days + 1
             for a in range(debut.year, fin.year + 1)}
    return max(jours, key=lambda a: (jours[a], a))


def source_sec(cik, depot):
    if pd.isna(depot) or not str(depot):
        return ''
    return f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{str(depot).replace('-', '')}/{depot}-index.htm"


def charger_registre(chemin=REGISTRE):
    return json.loads(Path(chemin).read_text(encoding='utf-8')) if Path(chemin).exists() else {'exceptions': []}


def _notes(*messages):
    return ' ; '.join(dict.fromkeys(str(x) for x in messages if x and str(x) != 'nan'))


def _selection(g, metric, exceptions):
    prefixe = 'ca' if metric == 'chiffre_affaires' else metric
    r = {metric: float('nan'), f'{prefixe}_etiquette': '', f'statut_{metric}': 'manquant',
         f'comparabilite_{metric}': 'manquant', f'{metric}_motif_qualite': 'Aucune valeur annuelle collectée',
         f'{metric}_perimetre_id': '', f'{metric}_methode': 'absence_collecte'}
    for champ in ('debut', 'fin', 'depot', 'depose_le', 'source_url'):
        r[f'{metric}_{champ}'] = ''
    r[f'{metric}_reconciliation_regle'] = ''
    r[f'{metric}_reconciliation_source_url'] = ''
    if g.empty:
        return r
    g = g.dropna(subset=['valeur']).sort_values(['etiquette', 'depose_le', 'depot'], kind='stable')
    if g.empty:
        return r
    notes = []
    statut, comp = 'observe', 'comparable'
    methode = 'coherence_automatique_sans_reconciliation_manuelle'
    regles = [e for e in exceptions if str(e['cik']).zfill(10) == str(g.iloc[0].cik).zfill(10)
              and metric in e.get('metriques', [metric])]
    choix = next((e for e in regles if e['type'] == 'etiquette_imposee'), None)
    if choix:
        source = g[g.etiquette == choix['etiquette']]
        if source.empty:
            r[f'{metric}_motif_qualite'] = 'Étiquette réconciliée absente ; aucun remplacement implicite'
            return r
        gagnante = source.sort_values('depose_le').iloc[-1]
        methode = 'etiquette_reconciliee_document_officiel'
        notes.append(choix['motif'])
    elif metric == 'chiffre_affaires':
        net = g[g.etiquette != TAXES_INCLUSES]
        source = net if not net.empty else g
        gagnante = source.loc[source.valeur.idxmax()]
        if net.empty:
            statut, comp = 'revue_requise', 'non_etablie'
            notes.append('Revenu incluant taxes : total net non réconcilié')
        # Une faible divergence ne prouve pas l'équivalence de deux notions.
        # La tolérance absolue couvre seulement le bruit d'arrondi numérique.
        if source.valeur.max() - source.valeur.min() > TOLERANCE_MONTANT:
            statut, comp = 'revue_requise', 'non_etablie'
            notes.append('Montants de revenu différents sans rapprochement ; maximum conservé comme candidat')
        if gagnante.secteur == 'Real Estate' and gagnante.etiquette != 'Revenues':
            statut, comp = 'revue_requise', 'non_etablie'
            notes.append('Foncière : revenu total non réconcilié avec les loyers')
    else:
        source = g
        gagnante = g.sort_values(['rang_preference', 'depose_le'], ascending=[True, False]).iloc[0]
        if source.valeur.max() - source.valeur.min() > TOLERANCE_MONTANT:
            statut, comp = 'revue_requise', 'non_etablie'
            notes.append('Postes de dépenses non équivalents ; préférence non réconciliée')
    valeur = float(gagnante.valeur)
    if gagnante.get('collecte_mode', '') == 'complement_document_officiel':
        methode = 'lecture_ligne_10K_documentee'
        notes.append(gagnante.get('note_source', ''))
    fin = str(gagnante.fin)
    perimetre = f"{str(gagnante.cik).zfill(10)}:{metric}:{gagnante.etiquette}"
    if valeur < 0 or (metric == 'chiffre_affaires' and valeur == 0):
        statut, comp = 'revue_requise', 'non_etablie'
        notes.append('Ventes nulles ou montant négatif à vérifier')
    if len(g[['debut', 'fin']].drop_duplicates()) > 1:
        statut, comp = 'revue_requise', 'non_etablie'
        notes.append('Plusieurs périodes distinctes rattachées à la même année')
    provenance = {c: gagnante.get(c, '') for c in ('debut', 'fin', 'depot', 'depose_le')}
    url = gagnante.get('source_url', '')
    url = url if pd.notna(url) and url else source_sec(gagnante.cik, gagnante.depot)
    valeur_originale = valeur
    for regle in regles:
        if regle['type'] == 'perimetre':
            if fin < regle['fin_min_comparable']:
                comp, statut = 'hors_perimetre_actuel', 'revue_requise'
                notes.append(regle['motif'])
                perimetre = regle['perimetre_id'] + ':historique_non_reconcilie'
            else:
                perimetre = regle['perimetre_id']
                notes.append('Périmètre délimité par ' + regle['id'])
        elif regle['type'] == 'reconciliation' and fin == regle['fin']:
            if abs(valeur - regle['valeur_brute_attendue']) > .01:
                statut, comp = 'revue_requise', 'non_etablie'
                notes.append('Valeur brute différente de celle visée par ' + regle['id'])
                continue
            valeur = regle['valeur_brute_attendue'] - regle['activites_abandonnees']
            statut, comp, perimetre = 'observe', 'comparable', regle['perimetre_id']
            methode = 'soustraction_activites_abandonnees_documentee'
            provenance['depot'], provenance['depose_le'] = regle['depot'], regle['depose_le']
            url = regle['source_url']
            notes.append(regle['motif'])
        elif regle['type'] == 'information':
            notes.append(regle['motif'])
        elif regle['type'] == 'equivalence_etiquettes':
            if not (regle['fin_min'] <= fin <= regle['fin_max'] and
                    gagnante.etiquette in regle['etiquettes']):
                continue
            attendue = regle.get('valeurs_controlees', {}).get(fin)
            equivalents = g[g.etiquette.isin(regle['etiquettes'])]
            # Le rapprochement de notion ne dispense pas de contrôler les
            # montants : une révision du comparatif doit être revue à nouveau.
            ecart = equivalents.valeur.max() - equivalents.valeur.min()
            if ((attendue is not None and abs(valeur - attendue) > .01) or ecart > .01):
                statut, comp = 'revue_requise', 'non_etablie'
                notes.append('Montants différents du rapprochement documenté ' + regle['id'])
                continue
            if statut == 'observe' and comp == 'comparable':
                perimetre = regle['perimetre_id']
                methode = 'equivalence_etiquettes_documentee'
                r[f'{metric}_reconciliation_regle'] = regle['id']
                r[f'{metric}_reconciliation_source_url'] = regle['source_url']
                notes.append(regle['motif'])
    r.update({metric: valeur, f'{prefixe}_etiquette': gagnante.etiquette,
              f'statut_{metric}': statut, f'comparabilite_{metric}': comp,
              f'{metric}_motif_qualite': _notes(*notes), f'{metric}_perimetre_id': perimetre,
              f'{metric}_methode': methode, f'{metric}_valeur_avant_reconciliation': valeur_originale,
              f'{metric}_source_url': url})
    r.update({f'{metric}_{c}': v for c, v in provenance.items()})
    if metric == 'chiffre_affaires':
        source = g[g.etiquette != TAXES_INCLUSES]
        source = source if not source.empty else g
        r.update(ca_nb_etiquettes=len(g), ca_ecart_relatif=(0. if source.valeur.max() == 0 else 1-source.valeur.min()/source.valeur.max()),
                 fin_exercice=provenance['fin'], ca_depot=provenance['depot'])
    return r


def construire_base(d, registre=None):
    """Transformation pure d'un DataFrame brut, sans réseau ni écriture."""
    d = d.copy()
    if d.empty:
        return pd.DataFrame(columns=CLE)
    d['cik'] = d.cik.astype(str).str.zfill(10)
    d['valeur'] = pd.to_numeric(d.valeur, errors='coerce')
    registre = registre if registre is not None else charger_registre()
    ajouts = []
    for supplement in registre.get('complements', []):
        compagnie = d[d.cik == supplement['cik']]
        if compagnie.empty:
            continue
        # Les compléments explicites remplissent une lacune, jamais un montant
        # déjà présent sous la même étiquette et sur la même période.
        if ((compagnie.notion == METRIQUES[supplement['metric']]) &
            (compagnie.etiquette == supplement['etiquette']) &
            (compagnie.fin == supplement['fin'])).any():
            continue
        ajout = {c: compagnie.iloc[0][c] for c in CLE if c != 'annee'}
        ajout.update({c: supplement[c] for c in ('debut', 'fin', 'valeur', 'etiquette', 'rang_preference', 'depot', 'depose_le', 'source_url')})
        ajout.update(notion=METRIQUES[supplement['metric']], annee=int(supplement['fin'][:4]),
                     collecte_mode='complement_document_officiel', note_source=supplement['motif'])
        ajouts.append(ajout)
    if ajouts:
        d = pd.concat([d, pd.DataFrame(ajouts)], ignore_index=True)
    d['annee_source'] = d.annee
    d['annee'] = [annee_majoritaire(a, b) for a, b in zip(d.debut, d.fin)]
    exceptions = registre.get('exceptions', [])
    lignes = []
    cle_periode = [c for c in CLE if c != 'annee'] + ['fin']
    for cle, g in d.groupby(cle_periode, dropna=False, sort=True):
        ligne = dict(zip(cle_periode, cle))
        fin = str(ligne.pop('fin'))
        debut = str(g.debut.mode().iloc[0])
        ligne.update(periode_id=f"{ligne['cik']}:{fin}", periode_debut=debut, periode_fin=fin,
                     annee=annee_majoritaire(debut, fin))
        for metric, notion in METRIQUES.items():
            ligne.update(_selection(g[g.notion == notion], metric, exceptions))
        lignes.append(ligne)
    table = pd.DataFrame(lignes).sort_values(['cik', 'periode_fin']).reset_index(drop=True)
    for metric in METRIQUES:
        pref = 'ca' if metric == 'chiffre_affaires' else metric
        table[f'{metric}_changement_etiquette'] = ''
        for _, g in table.groupby('cik'):
            precedent = None
            perimetre_precedent = None
            for idx, r in g[g[metric].notna()].iterrows():
                tag = r[f'{pref}_etiquette']
                if precedent is not None and tag != precedent:
                    table.at[idx, f'{metric}_changement_etiquette'] = 'oui'
                    rapproche = (r[f'{metric}_methode'] == 'equivalence_etiquettes_documentee'
                                  and r[f'{metric}_perimetre_id'] == perimetre_precedent)
                    message = ("Changement d'étiquette rapproché par une preuve comparative documentée" if rapproche
                               else "Changement d'étiquette ; comparaison inter-étiquettes non autorisée sans rapprochement")
                    table.at[idx, f'{metric}_motif_qualite'] = _notes(r[f'{metric}_motif_qualite'], message)
                precedent = tag
                perimetre_precedent = r[f'{metric}_perimetre_id']
    return table.sort_values(['nom', 'periode_fin']).reset_index(drop=True)


def main():
    table = construire_base(pd.read_csv(ENTREE, dtype={'cik': str}))
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    table.to_csv(SORTIE, index=False, encoding='utf-8')
    mask = table[[f'statut_{m}' for m in METRIQUES]].eq('revue_requise').any(axis=1)
    table.loc[mask].to_csv(ANOMALIES, index=False, encoding='utf-8')
    print(f'{len(table)} observations ; {table.cik.nunique()} entreprises ; {mask.sum()} observations à revoir')


if __name__ == '__main__':
    main()
