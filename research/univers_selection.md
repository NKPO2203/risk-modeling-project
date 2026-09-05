# Univers de recherche retenu

*AI Concentration Risk Research. 5 septembre 2026.*
*Application de la règle version III, après les corrections documentaires et comptables.*

## I. Ce que j'ai fait

Je suis parti des 503 lignes de la composition locale du S&P 500, regroupées en 500 entreprises par CIK. Les classes d'actions restent conservées comme information.

Le corpus contient 499 rapports complets et 12 836 passages extraits. Chaque CIK possède un dossier de revue. La lecture a porté sur des passages ciblés et des contextes complémentaires ; je ne présente pas ce travail comme une lecture intégrale des cinq cents rapports ni de chaque passage extrait.

Les citations, les sources et les motifs sont dans `data/review/decisions_selection.csv`. Les textes complets et leurs empreintes permettent de contrôler les preuves. Honeywell Aerospace reste sans 10-K exploitable au CIK concerné.

## II. Le résultat actuel

| Décision | Nombre |
|---|---:|
| A_EXAMINER | 76 |
| DOUTEUX | 39 |
| ENTRE | 112 |
| SORT | 273 |

**Les 112 entreprises retenues ont toutes une preuve retrouvée dans le corpus.** Il s'agit de l'univers utilisable à ce stade, pas d'une liste définitive pour toute la suite du projet.

Les 273 exclusions sont provisoires et motivées par les passages examinés. Les 39 cas douteux signalent une frontière ou une preuve insuffisante. Les 76 dossiers à examiner ne sont pas assimilés à des exclusions ; ils peuvent demander une lecture plus large, une preuve différente ou un rapport disponible.

Une citation retrouvée prouve sa traçabilité. Elle ne remplace pas la discussion du jugement économique que j'en tire.

### Cet univers est un vivier, pas un portefeuille

Ces 112 entreprises ne forment pas un portefeuille et ne sont pas destinées à être détenues ensemble. Elles constituent l'ensemble des candidats dans lequel plusieurs portefeuilles différents seront construits.

La distinction est nécessaire pour la suite, parce que le sujet du projet est la concentration. Or **la concentration ne se mesure pas au nombre d'entreprises, elle se mesure aux poids**. Un portefeuille bâti sur une poignée de très grandes capitalisations tirées de cet univers serait extrêmement concentré. Un portefeuille équipondéré sur les 112, réparti sur neuf secteurs, ne le serait pas. Les deux sortent du même vivier, et c'est leur comparaison qui répondra à la question de recherche.

L'étalement de l'univers sur neuf secteurs n'éloigne donc pas du sujet. Il constitue au contraire un premier constat : l'exposition économique à la chaîne des infrastructures de calcul ne se limite pas à un petit nombre de grandes valeurs technologiques.

## III. Pourquoi l'univers a changé

L'ancienne sélection retenait 82 entreprises. La nouvelle en ajoute 36 et place 6 anciennes entrées en doute, soit 112 retenues. Je ne cherche pas à conserver l'ancien effectif : ce nombre doit être le résultat de la règle.

Les nouveaux cas comprennent Applied Materials, Amphenol, Trane, Carrier, Monolithic Power Systems, CDW et plusieurs fournisseurs industriels. Ils montrent pourquoi un rang faible ou un secteur autre que la technologie ne justifiait pas une exclusion automatique.

Berkshire Hathaway et Ares Management entrent sur des activités opérationnelles de filiales ou de plateformes décrites dans leurs dossiers. Leur présence ne signifie pas qu'une simple participation financière suffirait à qualifier tout gestionnaire d'actifs.

NextEra Energy, Public Service Enterprise Group, CMS Energy, PG&E, Oneok et Consolidated Edison passent en `DOUTEUX`. Les preuves examinées ne satisfont pas assez précisément la distinction entre activité ou engagement concret et perspective générale. Ce changement ne vient pas de leurs multiples comptables.

First Solar reste douteuse lorsque le passage ne décrit que des acheteurs potentiels. Adobe, ServiceNow et AppLovin restent des cas de frontière entre investissement applicatif et capacité d'infrastructure identifiable. Je ne les exclus pas simplement parce que leur métier est le logiciel.

Les changements de verdict par rapport à l'archive sont conservés dans `data/review/changements_selection_20260905.csv`.

## IV. Les canaux et la maturité

| Canal | Nombre |
|---|---:|
| depense | 2 |
| depense et vend | 4 |
| fournit | 74 |
| vend | 32 |

L'activité est établie dans 95 dossiers ; 17 reposent sur un engagement ou un développement documenté.

La part précisément attribuable à l'IA n'est pas isolée de manière suffisamment homogène. Le degré est donc `non_quantifie` pour les 112 entreprises. Cela ne veut pas dire qu'elles ont toutes la même exposition. Cela empêche de transformer un adjectif non étayé en mesure de risque ou en poids de portefeuille.

Les centres de données servent aussi des usages autres que l'IA. Cette limite reste attachée à la preuve et à l'interprétation.

## V. La répartition sectorielle

| Secteur du fichier de composition | Nombre |
|---|---:|
| Communication Services | 2 |
| Consumer Discretionary | 2 |
| Energy | 6 |
| Financials | 2 |
| Industrials | 22 |
| Information Technology | 43 |
| Materials | 7 |
| Real Estate | 7 |
| Utilities | 21 |

L'univers couvre 9 secteurs du fichier. 69 entreprises retenues se trouvent hors de l'Information Technology.

Cela décrit la différence entre une classification sectorielle et le mécanisme que je cherche. Cela ne démontre pas que ces secteurs se comporteront de la même façon en bourse, ni que les 112 entreprises offrent 112 risques indépendants.

La composition reste celle du fichier local, source secondaire à rapprocher d'une composition officielle datée. Le périmètre S&P 500 n'est pas synonyme de toutes les entreprises cotées aux États-Unis.

## VI. Ce que les comptes décrivent maintenant

La base contient 16 722 lignes brutes et 5 707 périodes traitées pour 496 entreprises. Une clôture identifie l'exercice ; deux périodes ne sont pas fusionnées parce qu'elles partagent l'année civile majoritaire.

La description des 112 entreprises retenues donne :

| Mouvement des mesures disponibles | Nombre |
|---|---:|
| doublement observe | 50 |
| non evaluable | 6 |
| progression inferieure au seuil | 55 |
| recul des mesures disponibles | 1 |

La couverture est une autre information :

| Couverture | Nombre |
|---|---:|
| aucune comparaison | 6 |
| observation partielle | 48 |
| trois mesures comparables | 58 |

« Doublement » signifie qu'au moins une mesure comparable atteint deux fois sa moyenne de référence. Il ne signifie ni que toute l'entreprise a doublé, ni que l'IA en est la cause.

Les multiples continus sont conservés. La sensibilité aux seuils 1,5, 2 et 2,5 est publiée dans `corroboration_sensibilite.csv`. Le seuil n'est pas choisi pour faire passer certaines entreprises.

## VII. Les comparaisons qui changeaient le raisonnement

| Entreprise | Ventes | Investissement | Recherche |
|---|---:|---:|---:|
| American Electric Power | Non calculable | ×1,40 | Non calculable |
| Howmet Aerospace | ×1,19 | ×2,31 | ×1,07 |
| Western Digital | ×2,06 | ×0,91 | ×1,20 |
| Nvidia | ×20,03 | ×4,30 | ×7,93 |
| Marvell Technology | ×1,43 | ×1,31 | ×1,13 |

**American Electric Power.** La construction augmente d'environ 40 % par rapport à sa référence 2017–2019. L'ancienne multiplication par onze mélangeait des notions. Le récent correspond à 8,453 milliards de dollars de construction ; les 3,453 milliards d'acquisitions de centrales sont un autre poste. Les autres mesures restent non calculables si leurs étiquettes n'ont pas été rapprochées ou si la donnée manque.

**Howmet.** Les ventes et la recherche utilisent les comptes de résultat retraités de 2018–2019. L'investissement utilise 2021–2022, les deux premiers exercices complets admissibles après la scission. Le doublement de l'investissement ne transforme pas ces références différentes en un horizon unique.

**Western Digital.** Les références portent sur les activités poursuivies et les flux rapprochés des activités abandonnées. Ce sont les exercices clos le 30 juin 2023 et le 28 juin 2024 ; le récent clôture le 3 juillet 2026. Les ventes peuvent augmenter pendant que l'investissement recule. Je ne parle plus d'une contradiction générale avec le discours.

**Nvidia.** Les ventes ont une référence 2017–2019 après rapprochement documenté des deux étiquettes. La recherche utilise aussi 2017–2019, mais l'investissement utilise le repli 2021–2022. Ces trois multiples ne décrivent pas la même durée.

**Marvell.** Le changement de structure lié à Inphi et au nouveau CIK interdit un raccordement automatique. Les références sont les premiers exercices admissibles du périmètre documenté.

Les montants, dates, périmètres et dépôts de chaque calcul sont dans `data/processed/corroboration_details.csv`. Les sources expliquant les rapprochements figurent dans le journal des corrections et le registre comptable.

## VIII. Les compagnies d'électricité ne constituent pas un seul cas

Certaines fournissent déjà des centres de données, d'autres ont signé des contrats ou engagé des capacités, et d'autres évoquent surtout une croissance espérée. Le dossier de Dominion décrit, par exemple, des ventes d'électricité déjà réalisées à ces clients.

Je ne peux donc plus présenter tous les services aux collectivités comme uniquement exposés à une croissance future. Je ne peux pas non plus déduire la nature de cette exposition d'une hausse du chiffre d'affaires total.

Les 21 entreprises retenues dans ce secteur ne définissent pas un poids de portefeuille. La comparaison des situations économiques, de la régulation et des dépendances boursières viendra avant toute pondération.

## IX. Ce qui reste à vérifier

1 636 périodes comptables sont signalées pour revue, sur l'ensemble de la base. Les 3 724 alertes automatiques couvrent plusieurs types de contrôles et peuvent concerner une même période. Elles ne représentent pas autant d'erreurs démontrées.

Un montant non réconcilié reste visible mais ne sert pas au multiple. Les dépenses absentes ne sont pas remplacées par zéro. Les corrections connues n'équivalent pas à un audit de toutes les acquisitions et cessions de toutes les entreprises.

L'exposition économique n'est pas encore une exposition boursière mesurée. Les derniers rapports, la composition locale actuelle et les comptes retraités ne forment pas un historique de stratégie sans anticipation.

La prochaine étape est de relire les décisions et les comparaisons, puis de définir les portefeuilles, les périodes, les benchmarks et les hypothèses à tester.

## X. Où retrouver les résultats

| Fichier | Contenu |
|---|---|
| `data/review/decisions_selection.csv` | Registre des 500 dossiers avec preuves et limites |
| `data/processed/classement_texte.csv` | Ordre de lecture reproductible |
| `data/processed/classification_manuelle.csv` | Verdicts appliqués et preuves vérifiées |
| `data/processed/univers_retenu.csv` | Les 112 entreprises actuellement retenues |
| `data/processed/base_selection.csv` | Les 5 707 périodes et statuts par mesure |
| `data/processed/corroboration_details.csv` | Références exactes et sources des multiples |
| `data/processed/controle_qualite.csv` | Alertes recalculées sur la base actuelle |
| `data/processed/etat_projet.json` | Effectifs courants sans recopie manuelle |
| `data/processed/pipeline_manifest.json` | Empreintes des entrées et sorties |
| `outputs/01a0708c-acb3-72c2-885a-9b76b6070a14/univers_retenu.xlsx` | Excel, preuves, couverture et récapitulatif |

L'ancien `univers_82.xlsx` reste un état antérieur. Le nouvel export ne fige plus l'effectif dans son nom.
