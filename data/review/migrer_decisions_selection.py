"""Migration ponctuelle de la revue des 500 CIK du 5 septembre 2026.

Les rangs ci-dessous designent UNIQUEMENT le corpus archive immuable.
Le resultat permanent est identifie par CIK. Cette migration refuse d'ecraser
un registre existant. Le pipeline courant ne lance jamais ce fichier.
Les priorites de lecture n'attribuent aucun verdict automatiquement.
"""
import csv
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ARCHIVE = ROOT / 'research/archive/2026-09-05_avant_corrections'
SORTIE = ROOT / 'data/review/decisions_selection.csv'

# Changements decides apres lecture des passages des 498 dossiers disponibles.
# Les autres decisions anterieures ont ete reexaminees, pas indexees au rang courant.
AJOUTS = {35, 58, 59, 69, 85, 91, 104, 117, 123, 153, 161, 202, 208,
          221, 230, 241, 267, 268, 273, 300, 311, 317, 329, 370, 372, 420}
PROSPECTIFS = {185, 238, 263, 294, 338, 358, 399}
FRONTIERES = {26, 63, 77, 130, 131, 174, 188, 191, 201, 217, 222, 227,
              231, 243, 246, 252, 266, 269, 271, 292, 319}
INSUFFISANTS = {112, 187, 196, 213, 214, 219, 220, 229, 242, 249, 256, 265,
                272, 278, 288, 301, 304, 309, 313, 324, 340, 341, 356, 362,
                363, 379, 388, 396, 403, 407, 409, 410, 415, 418, 423, 429,
                430, 433, 434, 439, 441, 443, 448, 450, 452, 453, 454, 456,
                457, 460, 464, 465, 470, 474, 475, 476, 478, 480, 481, 482, 484, 486}

# Index des passages priorises qui ont effectivement ete relus. Les indices
# secondaires proviennent de la revue complementaire documentee dans la note.
CHOIX = {1:1, 4:1, 5:7, 7:1, 8:3, 10:1, 11:3, 12:1, 13:1, 16:1,
         20:4, 25:3, 27:1, 32:1, 33:1, 34:1, 40:1, 45:1, 47:1, 48:7,
         49:4, 50:1, 58:0, 59:1, 62:1, 65:1, 69:1, 71:0, 74:1, 76:0,
         77:1, 80:1, 85:0, 90:1, 91:2, 94:1, 96:1, 97:1, 98:1,
         101:0, 104:2, 107:4, 111:1, 114:1, 115:1, 118:1, 119:1,
         123:2, 129:1, 131:5, 134:0, 135:1, 137:1, 138:2, 143:1,
         145:1, 151:1, 153:0, 156:1, 161:1, 165:0, 166:0, 167:1,
         174:1, 177:1, 178:1, 181:0, 183:0, 185:4, 188:0, 191:1,
         192:0, 197:0, 198:0, 199:0, 201:1, 202:1, 207:1, 208:0,
         217:0, 221:0, 222:0, 230:4, 232:1, 238:5, 241:0, 243:0,
         246:0, 250:1, 251:1, 253:1, 263:3, 267:1, 268:0, 269:0,
         273:0, 279:1, 285:1, 290:0, 291:1, 292:0, 294:8, 300:1,
         305:5, 306:1, 311:0, 317:0, 323:0, 329:1, 330:0, 334:8,
         338:1, 346:3, 350:0, 355:1, 358:0, 364:1, 370:0, 372:1,
         374:1, 382:0, 385:1, 399:0, 400:1, 404:1, 406:0, 411:1,
         413:1, 416:1, 420:1, 426:1, 431:1, 435:1, 437:0, 459:0,
         469:1, 479:0, 485:0, 487:0}

MOTIFS = {
    26: "Activite de centres de donnees en developpement et commercialisation ; exposition commerciale et stade a preciser, sans seuil de materialite implicite.",
    35: "Le rapport relie la demande de refroidissement hyperscale et centres de donnees a l'IA et au calcul intensif.",
    58: "Activite industrielle Data Center Solutions : fabrication d'enveloppes, de refroidissement et de materiels pour hyperscalers.",
    59: "Croissance du sous-marche filaire explicitement attribuee a l'expansion des infrastructures de centres de donnees pour l'IA.",
    69: "Les marches servis comprennent les centres de donnees IA ; leur contribution n'est pas isolee du poste autres marches.",
    85: "Services techniques et gestion d'installations de centres de donnees, notamment pour hyperscalers ; offre operationnelle distincte du seul courtage immobilier.",
    91: "Un milliard de dollars de commandes 2025 est explicitement lie aux applications de centres de donnees.",
    104: "Offre explicite de serveurs et stockage sur site et dans le cloud ; le motif porte sur l'infrastructure vendue, pas sur le conseil ou le logiciel applicatif.",
    107: "Le rapport decrit des centres de donnees propres et leurs besoins de puissance dans le developpement des produits IA. Les 20 milliards annonces ne sont pas assimiles a du CAPEX IA pur.",
    117: "Produits de refroidissement utilises dans les centres de donnees ; activite industrielle presente, part non quantifiee.",
    123: "Le fabricant relie l'expansion des centres de donnees et charges IA a la demande de generation et aux acheteurs de ses modules.",
    131: "Processeurs specialises pour inference IA en peripherie ; frontiere entre equipement de calcul et puce embarquee applicative a fixer avant inclusion.",
    145: "Demande de transport attribuee en partie a l'infrastructure IA ; le role logistique general est une frontiere du perimetre technique, pas une absence de lien economique.",
    147: "Investissement realise et accord de developpement de campus sur ses propres terrains ; engagement de capital, commercialisation future incertaine.",
    153: "Le rapport relie explicitement une partie des ventes de produits au CAPEX IA et aux infrastructures de centres de donnees.",
    161: "Capacite industrielle reservee pour 400 MW de systemes de generation destines aux centres de donnees ; livraison future, engagement deja decrit.",
    202: "Le fabricant de composants decrit une activite en croissance sur plusieurs marches dont les centres de donnees ; part propre a l'IA non fournie.",
    208: "La demande de composants est explicitement tiree notamment par les centres de donnees ; stocks et capacites sont destines aux clients actuels.",
    221: "Les investissements des clients en equipements semi-conducteurs sont relies a l'IA, aux centres de donnees et a la memoire avancee.",
    230: "Fluide de transfert thermique DOWFROST LC developpe pour le refroidissement liquide direct des processeurs de centres de donnees.",
    241: "Croissance des ventes du segment high-tech explicitement tiree par les centres de donnees et la microelectronique.",
    267: "Produits techniques de confinement d'air, armoires et autres composants pour construction et renovation de centres de donnees.",
    268: "Fourniture explicite d'alimentations sans interruption et d'equipements specialises pour centres de donnees.",
    273: "L'entreprise d'equipements semi-conducteurs identifie HPC et centres de donnees soutenus par l'IA comme moteurs de la croissance et de l'investissement de son industrie.",
    300: "Travaux engages sur un premier projet de production electrique pour centres de donnees ; le projet est en developpement, sans revenu de fourniture etabli dans l'extrait.",
    305: "Les centres de donnees representent 28 % des ventes d'electricite de Virginia Power en 2025 ; cette part n'est ni celle du groupe entier ni une part IA pure.",
    311: "Interconnexions pour un marche IT datacom representant 36 % des ventes 2025 ; applications comprenant IA, serveurs, cloud et centres de donnees, sans assimiler tout ce poste a l'IA.",
    317: "Solution Carrier QuantumLeap developpee pour le refroidissement traditionnel et liquide de centres de donnees.",
    329: "Hausse de commandes de production electrique principale en provenance de clients centres de donnees.",
    334: "Contrats signes ou examines par le regulateur avec centres de donnees et autres grandes charges, environ 9 GW cumules ; ce total n'est pas attribue integralement a l'IA.",
    370: "Demande de construction non residentielle explicitement soutenue par l'expansion des centres de donnees ; fournisseur de materiaux, part non quantifiee.",
    372: "Filiales operationnelles fabriquant systemes HVAC et structures pour centres de donnees ; inclusion fondee sur une offre industrielle, pas sur les seules participations financieres du groupe.",
    420: "Le fabricant identifie les centres de donnees parmi les moteurs effectifs de la demande de ses produits.",
}

def lire(path):
    with path.open(encoding='utf-8-sig', newline='') as f:
        return list(csv.DictReader(f))

def main():
    if SORTIE.exists():
        raise SystemExit("Registre existant : migration refusee. Editer le registre CIK explicitement.")
    spec = importlib.util.spec_from_file_location('aide_revue', ROOT/'data/review/preparer_revue_selection.py')
    aide = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(aide)
    # Rejouer exactement les passages historiques qui ont ete relus.
    corpus = lire(ARCHIVE/'data/raw/filings_phrases.csv')
    groupes = {}
    for p in corpus:
        groupes.setdefault(p['cik'], []).append(p)
    rapports = {r['cik']: r for r in lire(ARCHIVE/'data/raw/filings_termes.csv')}
    anciens = {r['nom']: r for r in lire(ARCHIVE/'data/processed/classification_manuelle.csv')}
    rangs = {r['cik']: r for r in lire(ARCHIVE/'data/processed/classement_texte.csv')}
    constituants = lire(ARCHIVE/'data/raw/sp500_constituents.csv')
    entreprises = {r['CIK'].zfill(10): r for r in constituants}
    lignes = []
    for cik, entreprise in sorted(entreprises.items()):
        dossier = rangs.get(cik)
        rang = int(dossier['rang']) if dossier else None
        ancien = anciens.get(dossier['nom'], {}) if dossier else {}
        passages = sorted(groupes.get(cik, []), key=aide.ordre, reverse=True)
        preuve = passages[min(CHOIX.get(rang, 0), len(passages)-1)]['phrase'] if passages else ''
        verdict = ancien.get('verdict', 'A_EXAMINER')
        if rang in AJOUTS: verdict = 'ENTRE'
        if rang in PROSPECTIFS | FRONTIERES: verdict = 'DOUTEUX'
        if rang in INSUFFISANTS or not preuve: verdict = 'A_EXAMINER'
        canal = ancien.get('canal', '')
        if verdict == 'ENTRE' and ancien.get('verdict') != 'ENTRE':
            canal = 'vend' if rang in {59,69,104,153,202,208,230,241,311} else 'fournit'
        maturite = 'etablie' if verdict == 'ENTRE' else 'indeterminee'
        if rang in {83,98,106,143,147,151,161,295,300,310,334,346,364,374}:
            maturite = 'engagement_ou_developpement_documente'
        if rang in PROSPECTIFS or rang in {26,193,292,422,426,451}:
            maturite = 'prospective_a_confirmer'
        if verdict == 'SORT':
            maturite = 'hors_perimetre_dans_passages_relus'
            canal = 'utilise_ou_applicatif'
            motif = "Passages relus portant sur des usages applicatifs, l'hebergement propre, des fonctions internes ou des risques de l'IA. L'offre d'infrastructure visee n'est pas etablie dans ces extraits ; exclusion provisoire de ce perimetre, sans prediction du rendement ni du signe d'un choc."
        elif verdict == 'DOUTEUX':
            motif = "Lien avec les centres de donnees mentionne, mais perimetre technique, activite propre ou stade de l'engagement insuffisamment etablis. Ne pas confondre intention, exposition financiere indirecte et fourniture actuelle."
            if rang in PROSPECTIFS:
                motif = "Projection de demande ou opportunite de fourniture aux centres de donnees ; l'extrait ne suffit pas a etablir un contrat ou un investissement specifique deja engage."
        elif verdict == 'A_EXAMINER':
            motif = "Extraits absents ou insuffisants pour attribuer un role economique dans la chaine. Aucun verdict d'absence d'exposition ne peut etre deduit de cette couverture."
        else:
            motif = "Le passage decrit une offre, des clients, une demande ou un engagement de capital lies aux capacites de calcul et a leurs infrastructures. La part propre a l'IA et la sensibilite boursiere restent a mesurer."
        motif = MOTIFS.get(rang, motif)
        depot = rapports.get(cik, {}).get('depot', '')
        url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{depot.replace('-', '')}/{depot}-index.html" if depot else ''
        lignes.append(dict(cik=cik, verdict=verdict, canal=canal, degre='non_quantifie' if verdict in ('ENTRE','DOUTEUX') else '',
            motif=motif, depot=depot, phrase_decisive=preuve, source_url=url, maturite_exposition=maturite,
            statut_revue='revue_ciblee_extraits' if preuve else 'a_completer',
            limite_preuve="Revue ciblee de passages, pas lecture integrale du rapport. Corpus historique plafonne et sans sigle AI seul ; absence de preuve non exhaustive.",
            revue_le='2026-09-05', ancien_verdict=ancien.get('verdict',''), ancien_rang=rang or '',
            nombre_passages_disponibles=len(passages), revue_version='2026-09-05_v1'))
    SORTIE.parent.mkdir(parents=True, exist_ok=True)
    with SORTIE.open('w', encoding='utf8', newline='') as f:
        writer=csv.DictWriter(f, fieldnames=list(lignes[0])); writer.writeheader(); writer.writerows(lignes)
    from collections import Counter
    print(len(lignes), Counter(r['verdict'] for r in lignes))

if __name__ == '__main__': main()
