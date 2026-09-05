# AI Concentration Risk Research

Je construis un univers documenté d'entreprises exposées à la chaîne des infrastructures de calcul liées à l'IA, à partir de la composition locale du S&P 500. Cet ensemble servira ensuite à construire et comparer plusieurs portefeuilles.

Cette étape prépare les sources, les décisions et les comptes. Elle ne calcule pas encore la performance, les corrélations ou le risque d'un portefeuille.

## Lire le projet

- [Contexte et état actuel](research/master_context.md)
- [Research Charter — bloc 1 finalisé et sourcé](research/research_charter.md)
- [Règle de sélection, version III](research/selection_rule.md)
- [Univers et interprétation des résultats](research/univers_selection.md)
- [Erreurs rencontrées et raisons des corrections](research/corrections_2026-09-05.md)
- [Chiffres recalculés](data/processed/synthese_resultats.md)

La rédaction de recherche explique mon raisonnement. Les nombres courants sont produits depuis les fichiers ; les anciens états sont conservés dans `research/archive/2026-09-05_avant_corrections/`.

## Reproduire les calculs sans réseau

Environnement vérifié : Python 3.12.14. Les versions de pandas, NumPy et lxml sont fixées dans `requirements.txt`. La collecte utilise la bibliothèque standard Python pour les requêtes ; les tests utilisent `unittest`.

Après installation des dépendances dans un environnement Python :

```powershell
python -m pip install -r requirements.txt
python -B src/run_pipeline.py
python -B -m unittest discover -s tests -v
python -B src/run_pipeline.py --check-only
```

Le pipeline vérifie d'abord les empreintes du corpus, puis reconstruit le classement, applique le registre de décisions, traite les comptes, recalcule les alertes et décrit les mouvements comptables. Il termine par les contrôles entre fichiers et un manifeste d'entrées/sorties.

`--check-only` vérifie les données présentes et leurs empreintes, sans les recalculer. Une modification d'une entrée, d'un script de calcul ou d'une sortie depuis l'exécution est signalée. L'export Excel est une opération séparée. `pipeline_status.json` indique si la dernière exécution s'est terminée ; un échec ne doit pas être présenté comme une génération complète.

## Comprendre les données

| Dossier ou fichier | Rôle |
|---|---|
| `data/raw/sp500_constituents.csv` | Composition locale de l'indice, source secondaire à rapprocher d'une source officielle datée |
| `data/raw/sec_facts_raw.csv` | Valeurs comptables acquises, avec notions, dates et dépôts |
| `data/raw/filings_text/` | Rapports HTML, textes, métadonnées, empreintes et générations du corpus |
| `data/raw/filings_termes.csv` | Occurrences et couverture de chaque entreprise |
| `data/raw/filings_phrases.csv` | Passages et positions permettant de revenir au rapport |
| `data/raw/filings_manifest.json` | Empreintes des CSV documentaires de la génération |
| `data/review/decisions_selection.csv` | Décisions documentées par CIK ; source de la classification |
| `data/review/comptabilite_exceptions.json` | Rapprochements comptables et compléments officiels, avec justification |
| `data/processed/` | Résultats reconstruits, contrôles, synthèse et manifeste |

Les CSV sont encodés en UTF-8. Le CIK doit être lu comme du texte de dix caractères. Une entreprise peut avoir plusieurs symboles. Dans les comptes, la clé est le CIK et la date de clôture ; l'année civile majoritaire est informative et peut se répéter.

Les décisions possibles sont `ENTRE`, `SORT`, `DOUTEUX` et `A_EXAMINER`. Une absence de décision ou une preuve introuvable ne devient pas une exclusion. Les décisions sont éditées dans le registre de revue, jamais dans un classement généré.

Les montants non rapprochés restent visibles avec un statut. Une valeur manquante n'est pas zéro. Le fichier `corroboration_details.csv` contient les montants, périodes, périmètres et sources de chaque comparaison ; `corroboration.csv` sépare le mouvement de la couverture.

## Actualiser les sources

Pour reconstruire les passages depuis les rapports déjà archivés, sans réseau :

```powershell
python -B src/fetch_filings_text.py
python -B src/run_pipeline.py
```

Pour consulter de nouveau les dépôts SEC :

```powershell
python -B src/fetch_filings_text.py --refresh
```

`--refresh --resume` reprend une collecte avec les métadonnées déjà récupérées. Cette option sert à terminer une collecte interrompue ; elle ne garantit pas une nouvelle interrogation de toutes les métadonnées.

La collecte financière reste une commande séparée :

```powershell
python -B src/fetch_sec_financials.py
```

Les accès SEC emploient un identifiant de recherche et un rythme limité, définis dans les collecteurs. Une actualisation peut changer la composition ou les dépôts utilisés. Il faut ensuite refaire la revue des preuves invalidées et relancer le pipeline. Un rapport manquant ou une erreur réseau reste consigné ; les succès documentaires antérieurs sont conservés.

Les chiffres comptables courants ont été retraités depuis le brut existant et complétés sur des sources ciblées. Une nouvelle collecte financière intégrale n'a pas été nécessaire à cette correction.

## Export Excel

L'export courant se trouve dans `outputs/01a0708c-acb3-72c2-885a-9b76b6070a14/univers_retenu.xlsx`. Il conserve les trois vues de l'ancien classeur, ajoute les preuves et la couverture, et propose un récapitulatif recalculé.

```powershell
python -B src/export_univers_excel.py
```

L'écriture XLSX nécessite Node.js et le module `@oai/artifact-tool` disponible dans l'environnement. Les variables `NODE_EXECUTABLE` et `ARTIFACT_TOOL_MODULE` permettent de désigner un runtime et un module déjà installés. La préparation seule reste disponible sans ce moteur :

```powershell
python -B src/export_univers_excel.py --json-only
```

Le fichier racine `univers_82.xlsx` est conservé comme état antérieur et n'est plus la sortie courante. Le nouveau nom ne fige pas le nombre d'entreprises.

La première date issue du fichier Yahoo existant est une date d'historique disponible, dont la collecte d'origine n'est pas datée. Elle n'est pas une date d'IPO vérifiée. Les nouveaux candidats sans cette information restent sans date.

## Ce que cette étape ne démontre pas

Les derniers rapports, la composition actuelle et les comptes retraités décrivent une photographie du projet. Ils ne constituent pas un univers historique investissable sans anticipation.

Une exposition économique documentée ne démontre ni une corrélation boursière, ni une causalité entre l'IA et la croissance totale. Les cas douteux, les données absentes et les limites de comparabilité restent dans les résultats.

Les tests contrôlent des erreurs précises et la cohérence des artefacts. Ils ne remplacent pas la lecture critique des sources et ne certifient pas l'absence de toute erreur.

`main.py` et `risk_analysis.ipynb` restent les exercices initiaux du workflow, distincts du traitement de recherche dans `src/`.
