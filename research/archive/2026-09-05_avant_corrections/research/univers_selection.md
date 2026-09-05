# Univers d'investissement retenu

*AI Concentration Risk Research. 4 septembre 2026.*
*Application de la règle de sélection version II. Résultat et raisonnement.*
*Mis à jour le 5 septembre 2026 : ajout de la corroboration par les comptes.*

---

## I. Ce qui a été fait

Je suis parti des 503 lignes du S&P 500, ramenées à 500 entreprises après regroupement des classes d'actions multiples.

Pour chacune, j'ai récupéré deux choses depuis les sources officielles de la SEC. D'abord ses comptes, chiffre d'affaires, dépenses d'investissement et dépenses de recherche, sur douze exercices. Ensuite le texte intégral de son dernier rapport annuel, dans lequel j'ai compté treize termes du vocabulaire de l'infrastructure de calcul et extrait les phrases qui les contiennent.

J'ai ensuite lu ces phrases et posé à chaque entreprise la question de la règle : si l'investissement en intelligence artificielle s'arrêtait demain, perdrait-elle de l'argent ?

498 entreprises ont pu être traitées, deux rapports n'ayant pas pu être récupérés.

---

## II. Le résultat

**82 entreprises entrent. 386 sortent. 30 restent douteuses.**

Réparties par canal d'exposition :

| Canal | Nombre |
|---|---|
| Elle fournit la chaîne | 54 |
| Elle vend | 22 |
| Elle dépense et elle vend | 4 |
| Elle dépense | 2 |

Et par intensité déclarée :

| Degré | Nombre |
|---|---|
| Quasi total | 5 |
| Fort | 28 |
| Partiel | 46 |
| Faible | 3 |

---

## III. Ce que la nomenclature officielle ne voit pas

L'univers retenu s'étale sur **sept secteurs officiels** :

```
Technologie                     32
Services aux collectivites      26
Industrie                       12
Immobilier                       5
Energie                          3
Communication                    2
Consommation discretionnaire     2
```

Un investisseur qui achèterait « le secteur technologique » en manquerait cinquante sur quatre-vingt-deux, soit plus de la moitié.

C'est le résultat que la règle annonçait en interdisant au secteur de servir de filtre. Il est maintenant établi sur données.

---

## IV. Le classement par fréquence ne suffisait pas

J'avais d'abord classé les entreprises par la place que le vocabulaire occupe dans leur rapport, puis lu de haut en bas. La densité des entrées décroît vite :

```
rangs   1-30  : 22 entrent
rangs  31-60  : 14 entrent
rangs  61-90  :  7 entrent
rangs  91-120 :  7 entrent
```

Mais elle ne s'éteint pas, et surtout les entrées tardives ont toutes le même profil : elles fournissent la chaîne sans employer souvent le vocabulaire.

J'ai donc complété par un **balayage intégral** des secteurs où l'exposition indirecte se cache : services aux collectivités, industrie, immobilier, matériaux, énergie.

Ce balayage a rattrapé trente-deux entreprises, dont deux qui montrent à elles seules pourquoi il était nécessaire.

**Comfort Systems USA**, rang 285. Entreprise de génie climatique qui écrit que sa demande est « particulièrement forte dans le secteur technologique, notamment pour les centres de données », et dont une filiale est spécialisée dans la climatisation de centres de données. Un classement par fréquence l'enterrait.

**Vistra**, rang 291. Producteur d'électricité qui décrit « l'émergence de grandes charges de centres de données, en réponse aux transformations technologiques comme l'IA ». C'est précisément l'entreprise dont j'avais signalé que le texte la sous-détectait.

---

## V. Ce que la règle exclut, et pourquoi c'est important

**Palantir sort.** C'est probablement l'action la plus identifiée à l'intelligence artificielle dans le grand public. Mais son profil est celui d'un éditeur de logiciel qui vend un produit contenant de l'IA, exactement comme Salesforce ou Adobe. Elle ne détient aucune infrastructure et ne fournit rien à la chaîne.

**Apple sort.** Ses seules mentions concernent les risques juridiques des fonctions d'IA de ses produits.

Ces deux exclusions sont le meilleur test de la règle. Si je gardais Palantir parce qu'elle est célèbre, la règle ne vaudrait plus rien, et le reproche de sélection par notoriété deviendrait imparable.

Une famille entière sort pour la même raison : les éditeurs de logiciels. Adobe, Salesforce, ServiceNow, Workday, CrowdStrike, Fortinet, Palo Alto Networks, GoDaddy. Elles remontent haut dans le classement textuel parce qu'elles emploient beaucoup le vocabulaire, mais pour deux motifs qui ne sont pas des expositions : elles mettent de l'IA dans leurs produits, et elles louent des centres de données pour héberger leurs services. Dans les deux cas, un arrêt de l'investissement leur ferait **baisser leurs coûts**.

Deux autres sortent par le quatrième canal, celui de la menace. **Gartner** écrit que l'IA « pourrait modifier le marché de ses offres de façon imprévisible et réduire la demande de ses clients ». **CoStar** écrit que l'IA générative « pourrait abaisser la barrière à l'entrée pour de nouveaux concurrents ». Elles sont de l'autre côté du choc.

---

## VI. Trois entrées que je n'aurais pas trouvées autrement

**Tesla**, par le canal de la dépense : « plus de 20 milliards de dollars d'investissement prévus en 2026, tirés par nos initiatives en IA, incluant l'infrastructure de calcul et les centres de données ».

**Constellation Energy** et **Entergy**, par la fourniture : contrats d'alimentation électrique de campus de centres de données, l'un avec Microsoft, l'autre sur un site où Amazon Web Services est impliqué.

**Texas Pacific Land**, propriétaire foncier au Texas, qui a signé un accord stratégique pour développer des campus de centres de données sur ses terrains.

Aucune de ces entreprises n'apparaîtrait dans une liste construite à partir du mot « intelligence artificielle ».

---

## VII. Le problème que ce résultat pose, et qu'il faudra trancher

**Vingt-six services aux collectivités sur quatre-vingt-deux entreprises.** Presque un tiers de l'univers.

Leur exposition est réelle et documentée : beaucoup écrivent noir sur blanc que leurs plans d'investissement dépendent de la croissance des centres de données raccordés à leur réseau. Certaines ont un facteur de risque dédié à ces clients.

Mais leur situation n'est pas celle de Nvidia, et il faut le dire clairement.

Si l'investissement en IA s'arrêtait demain, Nvidia perdrait **du chiffre d'affaires existant**. Un service aux collectivités régulé perdrait **de la croissance future**. Son activité de base, facturer l'électricité à des foyers et à des industriels sous un tarif approuvé par un régulateur, continuerait.

Ce ne sont pas les mêmes entreprises face au même choc, même si toutes deux répondent oui à la question de la règle.

C'est pourquoi le champ **degré** existe. Vingt-six des vingt-huit entreprises classées « fort » ou plus sont dans la technologie ou l'équipement, tandis que la quasi-totalité des services aux collectivités est classée « partiel » ou « faible ».

**Ce point devra être tranché au moment de construire le portefeuille**, et il ouvre trois options : pondérer par le degré, séparer l'univers en deux sous-portefeuilles à comparer, ou conserver l'univers entier en montrant que les deux familles ne se comportent pas de la même façon.

La troisième me paraît la plus intéressante, parce qu'elle transforme une difficulté en résultat. Mais c'est une décision à prendre plus tard, et pas seul.

---

## VIII. La corroboration par les comptes

La règle exige qu'une entreprise entre si elle déclare une dépendance à l'infrastructure de calcul **et** si ses comptes montrent que quelque chose a effectivement bougé. La lecture des rapports annuels a établi la première moitié. Cette étape établit la seconde.

Chaque entreprise est comparée à son propre passé, jamais aux autres, et sur deux multiples : celui de son chiffre d'affaires, et le plus élevé de ses dépenses d'investissement et de recherche. La période de référence est la moyenne 2017 à 2019.

Cette étape ne trie pas et ne retire personne. Elle mesure, en trois niveaux dont les bornes sont 1 et 2, c'est-à-dire l'absence de progression et le doublement.

| Niveau | Nombre |
|---|---|
| Mouvement net, un multiple atteint 2 | 42 |
| Mouvement modéré | 38 |
| Aucun mouvement, les deux multiples sont inférieurs ou égaux à 1 | 2 |

### Les deux seules contradictions

**Howmet Aerospace**, ventes ×0,92, investissement ×0,68, recherche ×0,62.
**Western Digital**, ventes ×0,69, investissement ×0,55, recherche ×0,50.

Ces deux entreprises déclarent une exposition à l'infrastructure de calcul et tout recule chez elles. Ce sont les seuls cas où les comptes contredisent le discours.

### Le cas Intel, qui n'est pas une contradiction mais mérite d'être noté

Intel est classée en exposition forte sur la foi d'un texte explicite : la demande de calcul fortement accrue pour les systèmes GPU, tirée par les charges d'IA générative. Ses comptes sont plats. Chiffre d'affaires ×0,77, investissement ×1,02, recherche ×1,03.

Elle décrit un marché en expansion dont elle ne capte manifestement rien. Ce n'est pas une erreur de sélection, elle est bien exposée au cycle, mais elle en subit le mauvais côté. Cette nuance n'apparaît qu'en croisant le texte et les comptes.

### Ce que cela confirme sur les services aux collectivités

Sur les vingt-six retenus, seize montrent un mouvement modéré et dix un mouvement net. Deux tiers d'entre eux progressent réellement mais ordinairement.

C'est la confirmation chiffrée de ce qui n'était jusqu'ici qu'un raisonnement : leur exposition porte sur leur croissance future, pas sur leur activité existante. Les exceptions le disent aussi bien, American Electric Power ayant multiplié son investissement par onze et Vistra par six.

### Cinq entreprises jugées sur une base affaiblie

Constellation Energy, GE Vernova, Qnity Electronics, Marvell et Sandisk sont des entités récentes issues de scissions. Leur base de comparaison se situe déjà à l'intérieur de la période étudiée, de sorte que leur multiple est mécaniquement sous-estimé. Elles portent le drapeau `base_courte` dans le fichier.

Le détail figure dans `data/processed/corroboration.csv`, avec pour chaque entreprise les trois multiples, la période de base utilisée et le niveau retenu.

---

## IX. Les limites de ce résultat

**Trente entreprises restent douteuses** et n'ont été ni retenues ni écartées. Ce sont pour la plupart des producteurs de matériaux ou des industriels qui citent les centres de données dans une énumération de débouchés, sans en faire un moteur déclaré. Nucor, Vulcan, CRH, Freeport, Caterpillar, Carrier. Elles figurent dans le fichier avec ce statut, et il faudra décider ce qu'on en fait.

**Le jugement humain est présent** à l'étape de lecture, et il est irréductible. Il est rendu contestable par la consignation d'un motif par entreprise, tiré du texte de l'entreprise elle-même.

**Deux rapports n'ont pas pu être récupérés**, et une quinzaine d'entreprises présentent des défauts dans leurs données financières, principalement des banques et des foncières qui sortent de toute façon du périmètre.

**Le périmètre reste américain**, ce qui exclut volontairement des acteurs centraux de la chaîne, notamment en fabrication de semi-conducteurs et en équipement de gravure.

**Trois entreprises restent non évaluables sur les comptes.** NextEra, CMS Energy et DTE Energy ne déclarent leurs dépenses d'investissement sous aucune étiquette comptable standard. Elles conservent leur place dans l'univers, mais la seconde moitié de la règle n'a pas pu leur être appliquée.

---

## X. Fichiers produits

| Fichier | Contenu |
|---|---|
| `data/raw/sp500_constituents.csv` | les 503 lignes de l'indice, avec secteur et identifiant SEC |
| `data/raw/sec_facts_raw.csv` | 16 084 valeurs comptables, toutes étiquettes conservées |
| `data/raw/filings_termes.csv` | comptage des treize termes pour 498 entreprises |
| `data/raw/filings_phrases.csv` | 4 591 phrases extraites des rapports annuels |
| `data/processed/base_selection.csv` | comptes retraités, une ligne par entreprise et par exercice |
| `data/processed/classement_texte.csv` | classement par ampleur et densité du vocabulaire |
| `data/processed/classification_manuelle.csv` | les 498 verdicts, avec canal, degré et motif |
| `data/processed/univers_retenu.csv` | les 82 entreprises retenues |
| `data/processed/controle_qualite.csv` | les alertes de vraisemblance sur les 500 |
| `data/processed/corroboration.csv` | les multiples et le niveau de corroboration des 82 |

Chaque valeur du fichier brut porte la référence du dépôt SEC dont elle provient.
