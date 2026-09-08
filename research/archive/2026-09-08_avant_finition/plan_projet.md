# Plan du projet et état d'avancement

*AI Concentration Risk Research. Mise à jour du 8 septembre 2026 après audit.*

Ce document dit où en est le projet, selon quel découpage, et à quelles conditions une étape est considérée comme close. Il existe parce qu'un audit externe a constaté que ce découpage n'apparaissait dans aucun fichier du dépôt : il ne vivait que dans les échanges de travail.

---

## I. Les cinq étapes

| | Étape | État |
|---|---|---|
| 1 | Construire un univers d'entreprises exposées à la chaîne des infrastructures de calcul | **close**, version exploratoire |
| 2 | Construire les portefeuilles à partir de cet univers | construction corrigée et rejouée ; validation des données encore partielle |
| 3 | Mesurer le risque, ses sources et son comportement en crise | non commencée |
| 4 | Étudier la couverture et la diversification | non commencée |
| 5 | Comparer les stratégies, coûts et risque résiduel | non commencée |

**Ce que « close » veut dire ici.** Une étape est close quand ses livrables existent, se régénèrent dans le schéma annoncé, et que ses limites sont écrites. Cela ne signifie pas que tous les jugements sont définitifs ni que toutes les vérifications imaginables ont été faites.

L'étape 1 est close en ce sens : 113 entreprises retenues, 38 douteuses et 76 en attente d'examen. Sur les 500 dossiers, **482 portent une citation et 18 n'en portent aucune** ; ces 18 sont tous au statut à examiner, ce qui est cohérent avec leur état mais interdit d'écrire que chaque décision est adossée à une citation.

---

## II. Le découpage de l'étape 2

Huit phases, cinquante-cinq tâches. La répartition indique qui produit quoi : **A** pour l'auteur, **C** pour l'assistant.

### Phase 0 : Décisions avant collecte : **close**

| | Tâche | | État |
|---|---|---|---|
| 1 | Source de prix et écriture de ses limites | A | yfinance retenu |
| 2 | Méthode de contrôle par seconde source | C | protocole à trois niveaux, écrit en phase 2 |
| 3 | Traitement des classes d'actions multiples | A | classes conservées séparément à la collecte |

Les deux benchmarks retenus sont `SPY`, réplique du S&P 500 pondéré par capitalisation, et `RSP`, réplique de sa version équipondérée. Trois indices sont collectés en complément pour le contexte et le contrôle.

### Phase 1 : Cliché de prix collecté, couverture auxiliaire partielle

| | Tâche | | État |
|---|---|---|---|
| 4 | Correspondance CIK vers symbole | C | faite, `BRK.B` interrogé sous `BRK-B` |
| 5 | Cours quotidiens bruts | A | 114 séries pour 113 entreprises |
| 6 | Cours quotidiens ajustés | A | mêmes fichiers |
| 7 | Dividendes | A | mêmes fichiers |
| 8 | Divisions d'actions | A | mêmes fichiers |
| 9 | Nombre d'actions en circulation | A | 8 987 lignes de notions différentes, CMS absent |
| 10 | Séries de comparaison | A | 2 fonds et 3 indices |
| 11 | Calendrier de bourse | A | 8 458 séances depuis 1993 |
| 12 | Manifeste de collecte | A | empreintes et limites écrites |

Le fichier auxiliaire des actions contient 6 444 observations `actions` pour 109 entreprises, 172 observations `actions_bilan` pour deux entreprises, 302 moyennes pondérées pour trois entreprises et 2 069 mesures de flottant en dollars. Ces notions ne sont pas interchangeables. CMS n'y figure pas ; Meta n'a pas de nombre instantané dans ce fichier, et Alphabet et Dell n'ont que les notions alternatives indiquées. Cette couverture suffit aux contrôles partiels décrits, pas à une capitalisation exhaustive. Les portefeuilles équipondérés n'utilisent aucune de ces notions comme poids.

### Phase 2 : Contrôle de la donnée brute, réserves ouvertes

Les résultats sont écrits dans `data/processed/controle_prix.csv`. Le notebook appelle maintenant `src/controle_prix.py`, qui rejoue tous les contrôles locaux sans acquisition. Le résumé conserve les tests à zéro. Le manifeste atteste les entrées du calcul, pas la validation économique de toutes les anomalies.

| | Tâche | | État |
|---|---|---|---|
| 13 | Trous dans les séries et séances absentes | A | 74 anomalies |
| 14 | Variations quotidiennes aberrantes | A | 129 anomalies |
| 15 | Cohérence de l'ajustement | A | aucune anomalie |
| 16 | Vérification contre une seconde source | A | 20 divisions non confirmées |
| 17 | Cohérence des dates de première cotation | A | 57 anomalies |
| 18 | Devise et place de cotation | A | aucune anomalie |
| 19 | Retraits de cote et changements de symbole | A | 8 394 anomalies |
| 20 | Remise du rapport de contrôle intégral | A | `research/controle_donnees_prix.md` |

**Tâche 13.** Quatorze séances absentes de `SPXEW` entre 2015 et 2019, et soixante séries antérieures au calendrier de bourse, ce dernier ne remontant qu'à 1993.

**Tâche 14.** Cent vingt-sept variations ajustées de plus de 30 %, une barre incohérente sur `HUBB` au 5 mai 2021 où l'ouverture est inférieure au minimum, et une ligne sans aucun prix sur `HUBB` au 8 août 1977. Cette dernière n'était pas détectée par le test des prix négatifs : une valeur manquante ne satisfait aucune comparaison. Un test explicite a été ajouté.

**Tâche 15.** Le prix ajusté de Yahoo se reconstruit à partir du prix de clôture et des dividendes selon une convention multiplicative, le dividende étant retiré du prix de départ et non ajouté au prix d'arrivée. La formule additive s'écarte jusqu'à 8 % sur `JCI` ; la formule multiplicative reste sous 5 × 10⁻⁵ sur les 119 fichiers. Tous les écarts additifs dépassant le seuil de 10⁻⁴ tombent sur des jours de détachement. Il subsiste ailleurs de petits écarts numériques, jusqu'à 4,83 × 10⁻⁶ : écrire « aucun écart » aurait été trop fort.

**Tâche 16.** Le rapprochement des divisions avec les comptes SEC couvre 56 événements depuis 2010 : 9 sans encadrement exploitable, 20 incompatibles avec un simple rapport d'actions égal au facteur Yahoo, 27 compatibles dans la tolérance de 2 %. Je vérifie les dates de mesure et de dépôt des observations encadrantes. Ce contrôle n'est ni une validation indépendante des cours ni une preuve exacte de chaque division. L'audit du 8 septembre ajoute le rapprochement de 135 distributions de SPY avec State Street et un cours de clôture public, détaillés dans le rapport de contrôle.

Ces vingt cas ne suffisent pas à qualifier une erreur de collecte. `Stock Splits` contient aussi des facteurs liés aux scissions ; acquisitions, émissions, rachats et classes d'actions modifient également le rapport SEC. Je ne peux donc ni dire que le nombre d'actions est inchangé dans tous les cas ni multiplier aveuglément cette colonne pour reconstituer une capitalisation.

**Tâche 19.** Aucune série ne s'arrête avant la dernière séance du calendrier, ce qui ne prouve rien : la liste des composants étant un cliché de 2026, une entreprise retirée de la cote n'a jamais eu de fichier. Six dénominations divergent entre Yahoo et le S&P 500, toutes des variantes d'écriture sauf Schlumberger, devenu SLB N.V.

En cherchant l'origine de la plus forte variation de la liste, `HUBB` au 31 octobre 1994 à +885,9 %, j'ai repéré la transition entre un segment sans volume et une série négociée. Le contrôle relève 8 273 lignes de prix figés à volume nul. Pour HUBB, 5 510 lignes satisfont ce critère strict ; 5 561 ont un volume nul, ce qui est une autre grandeur. Ces motifs justifient un traitement prudent, pas la certitude que chaque séance sans volume est fictive. Le filtre courant et les cours portés sont décrits dans `portefeuilles.md`.

**Tâche 20.** Le rapport est dans `research/controle_donnees_prix.md`. Le cliché contient 1 057 439 lignes dans 119 fichiers. Les contrôles historiques produisent 8 674 signalements sur 101 fichiers ; un signalement n'est pas une erreur confirmée. Les vérifications structurelles supplémentaires et leur couverture sont indiquées dans le rapport d'audit.

**Tâche 17.** Trente-sept fichiers de prix n'ont aucune entrée dans `data/raw/premieres_cotations.csv`, construit du temps où l'univers comptait 82 entreprises et jamais régénéré depuis. Sur les 77 restants les dates concordent, mais ce zéro ne prouve rien : les deux fichiers viennent de la même source.

Le résultat utile vient de la contrainte logique inverse. Vingt entreprises ont une date d'entrée dans le S&P 500 antérieure à la première ligne de prix fournie. Des débuts communs, douze séries au 17 mars 1980, neuf au 21 février 1973 et huit au 2 janvier 1962, suggèrent des limites de couverture de Yahoo. Plusieurs introductions le même jour ne seraient pas impossibles ; ce motif n'en est pas une preuve. Une date de début disponible n'est pas une date d'IPO vérifiée.

**Tâche 18.** Les 119 fichiers sont libellés en dollars, sur des places américaines, avec les seuls décalages horaires de New York. Les métadonnées descriptives sont collectées dans `data/raw/metadonnees_titres.csv`. Aucune anomalie après correction.

Trois versions de la collecte descriptive ont été nécessaires : une réponse vide avait été comptée comme un succès, puis des indices d'options homonymes avaient été acceptés pour `SPY` et `RSP`. Une date de première transaction est nécessaire mais ne prouve pas à elle seule l'identité. Je contrôle aussi le symbole demandé, le type attendu, la devise et le raccordement au fichier.

**La règle qui en sort : vérifier la présence du succès attendu, jamais l'absence de l'échec imaginé.** Le même défaut avait produit la valeur manquante non détectée de la tâche 14.

La colonne `symbole` de `BRK-B.csv` conserve `BRK.B` alors que la collecte s'est faite sous `BRK-B`. Le fichier de prix est correct, son étiquette de provenance ne l'est pas. Écart documenté plutôt que corrigé, pour ne pas invalider l'empreinte du manifeste.

Une première version du contrôle SEC dépendait du tri entre déclarations ex aequo. Le tri est désormais explicite et stable. L'audit ajoute une condition omise : la date de mesure doit elle aussi encadrer l'événement, pas seulement la date de dépôt. Un dépôt postérieur peut encore rapporter un nombre d'actions antérieur. Les observations encadrantes sont enregistrées pour rendre ce choix vérifiable.

`DUK` reste non confirmé pour une raison réelle : le regroupement de juillet 2012 est simultané à l'absorption de Progress Energy, deux événements que le nombre d'actions ne permet pas de séparer.

Le complément du 8 septembre rapproche 103 411 clôtures de 43 titres et documente 34 événements. Les 392 clôtures de Sandisk concordent. Trois erreurs de richesse sont corrigées ; deux distributions sont reclassées. La couverture et les écarts restant non arbitrés sont détaillés dans `research/verification_etape_2.md`. Cette phase reste ouverte sur ces vérifications de données précisément recensées.

### Phase 3 : Décisions en voyant les données : **close**

| | Tâche | | État |
|---|---|---|---|
| 21 | Période d'étude | A | **décidée** |
| 22 | Fréquence des rendements | A | **décidée** |
| 23 | Rendement total ou de prix | A | **décidée** |
| 24 | Portefeuilles à construire, donc les poids | A | **décidée**, `research/portefeuilles.md` |
| 25 | Nombre de titres du portefeuille concentré | A | sans objet, voir tâche 24 |
| 26 | Règle de rééquilibrage | A | **décidée** |
| 27 | Traitement des entreprises récemment cotées | A | **décidée** |
| 28 | Poche de liquidités ou investissement intégral | A | **décidée** |
| 29 | Coûts de transaction | A | **décidée** |
| 30 | Portefeuilles par canal d'exposition | A | faite dans la tâche 24 |

**Tâche 21.** Période retenue : **de la clôture du 3 janvier 2000 à celle du 4 septembre 2026**, chaque titre entrant à sa première observation admissible selon les règles d'identité et de qualité écrites dans `portefeuilles.md`.

Quatre-vingt-une entreprises et autant de titres sont présents au départ. Trente-trois titres sont ensuite admis, dont une seconde classe d'Alphabet : cela fait trente-deux entreprises supplémentaires. Les dates admissibles tiennent compte des corrections GOOG, DELL et VRT. La composition ne reproduit pas un indice historique, elle ajoute les survivants de l'univers actuel lorsqu'un historique utilisable apparaît.

Trois raisons avaient conduit au départ en 2000 : observer l'éclatement technologique, la crise financière, mars 2020 et 2022 ; conserver un historique long ; traiter séparément les données suspectes. L'audit retient 18 cours portés après les corrections d'identité, au lieu d'effacer le rendement du jour de reprise. La présence de ces épisodes ne constitue pas encore leur définition statistique, qui appartient à l'étape 3.

Exiger que les 113 entreprises soient présentes aurait ramené l'étude à la fenêtre débutant le 27 octobre 2025, première observation de Qnity. GEV et CEG, issues de scissions en 2024 et 2022, illustrent aussi les historiques courts, mais ne déterminent pas la date de départ commune la plus tardive.

**Tâche 22.** Rendements **quotidiens**, soit environ 6 700 observations sur la période.

Le quotidien est retenu parce qu'il se laisse agréger et que l'inverse est impossible : on passe du jour à la semaine ou au mois, jamais du mois au jour. Il donne davantage d'observations pour étudier les événements rares, alors qu'une base mensuelle n'en offrirait qu'environ 320 et pourrait masquer un krach suivi d'une reprise dans le même mois. Cela ne garantit pas un nombre suffisant d'extrêmes indépendants pour estimer précisément les queues de distribution.

Sa faiblesse est connue : des cotations non synchrones et la microstructure peuvent déformer les corrélations quotidiennes. Il n'existe pas une corrélation « réelle » nécessairement supérieure. Les rendements portés doivent être signalés et les résultats comparés en quotidien et en mensuel, sans choisir la fréquence qui confirme l'intuition.

**Tâche 23.** Je retiens une richesse incluant les dividendes. La décision initiale d'utiliser `Adj Close` a été remplacée par la tâche 28 : `Close` et `Dividends`, créance au détachement puis réinvestissement annuel, dans les portefeuilles et dans SPY/RSP. Les séries Yahoo ajustées restent séparées pour le contrôle. La formule multiplicative qui reproduit Yahoo ne remplace pas l'identité additive d'un compte de titres et d'espèces.

L'écart moyen entre annualisation Yahoo ajustée et annualisation de prix vaut 2,05 points sur les 114 titres, chacun sur sa fenêtre disponible depuis 2000. Seulement 81 titres couvrent toute la période : ce n'est pas une moyenne de 112 historiques complets. Sur Southern, 10 000 deviennent 63 398 au cours seul et 211 679 selon Yahoo ajusté. La différence représente environ 73,5 % du gain ajusté au-dessus de la mise initiale ; elle mêle distributions et convention de réinvestissement, pas une attribution causale de la performance.

Ignorer les dividendes défavorise les titres distributeurs. Cela peut modifier différemment les paniers selon leurs poids en utilities, immobilier ou technologie. La direction et l'ampleur de l'effet doivent être calculées sur les portefeuilles effectivement comparés ; elles ne se déduisent pas universellement de l'étiquette équipondérée ou pondérée par capitalisation.

Réserve : les rendements totaux publiés et notre convention annuelle ne sont pas identiques. Même les deux formules de détachement, richesse additive et ajustement Yahoo multiplicatif, diffèrent. Les impôts et les délais effectifs de paiement restent hors du modèle principal. Ces choix sont écrits dans `portefeuilles.md` et mesurés séparément lorsqu'une source permet le rapprochement.

**Réserve écrite avant tout calcul.** Les benchmarks équipondérés ne couvrent pas le début de la période : `RSP` commence en mai 2003, `^SPXEW` en décembre 2006. Toute comparaison exigeant l'un d'eux sera restreinte à la sous-période correspondante et le dira. Ces séries ne seront pas prolongées ni reconstruites.

Une première version de cette décision fixait le départ à janvier 2007 pour disposer des deux benchmarks dès le premier jour. L'auteur a objecté que l'indisponibilité d'une seule comparaison ne justifiait pas de tronquer toute l'étude. L'objection est retenue.

**Tâche 25, sans objet.** Le portefeuille concentré n'a pas à être défini séparément : les sept maillons de la tâche 24 couvrent la gamme, de six entreprises pour les acheteurs à trente-deux pour les vendeurs. Les acheteurs ont sept titres, puisque les deux classes d'Alphabet représentent une entreprise.

**Tâche 27.** Chaque titre entre à sa **première observation admissible**, sans délai d'observation préalable, sous réserve du report d'une opération quand un cours nécessaire manque.

La mesure initiale comparait la volatilité des soixante premières séances à celle de la suite. Elle ne permet pas d'attribuer les écarts à la nouveauté plutôt qu'au régime de marché, ni de prouver l'absence d'un effet d'introduction. Le départ immédiat est une convention exploratoire de disponibilité, à tester plus tard avec un délai fixé à l'avance. Les cotations conditionnelles et les raccordements historiques demandent une vérification d'identité distincte.

**Tâche 30, faite dans la tâche 24.** Les sept maillons de chaîne sont les portefeuilles par canal d'exposition.

**Tâche 29.** Je conserve dix points de base sur le montant réellement échangé. L'audit applique ce coût aux achats et aux ventes, y compris le financement des entrées et les achats de réinvestissement des dividendes. La version conservée supporte donc aussi des frais de réinvestissement. La rotation est annualisée sur la durée observée et compte les deux côtés de chaque opération.

Le taux représente globalement commission et écart acheteur-vendeur. Il n'est pas estimé titre par titre et ne couvre pas de façon démontrée l'impact de marché, les cotations conditionnelles ou la liquidité de toute la période. Je le garde comme hypothèse constante, sans le qualifier de prudent sur toutes les observations.

La mesure des frais doit être comparée aux effets sur la performance et sur le risque. Un coût faible dans ce modèle n'annule ni les autres contraintes d'exécution ni l'arbitrage de rendement. Je ne peux pas conclure que le choix entre conserver et rééquilibrer se joue sur le seul risque.

Deux limites. Le taux est une hypothèse et non une mesure, et il est tenu constant alors que les coûts réels ont fortement baissé depuis 2000. La conclusion sera testée à cinq et à vingt-cinq points de base.

**Tâche 28.** Aucune poche de liquidités permanente. Les dividendes sont **accumulés en trésorerie puis réinvestis à la date annuelle**, répartis selon les poids cibles dans la version rééquilibrée et réinvestis dans le titre qui les a versés dans la version conservée.

La moyenne des rendements annuels de dividendes calculés titre par titre sur leurs fenêtres disponibles vaut 1,84 %, la médiane 1,62 %, et 30 titres dépassent 3 %. Ces fenêtres ne sont pas toutes identiques. La poche de créances et espèces des vingt séries corrigées représente 0,92 % en moyenne des photographies mensuelles, et 5,64 % au maximum ; ce sont des observations du modèle, pas la preuve d'un effet nul sur le risque.

Le réinvestissement immédiat et l'accumulation définitive des distributions sont deux conventions alternatives. La première ne demande pas littéralement une opération « à la seconde » ; elle constitue une convention de rendement. La seconde introduit une poche croissante non rémunérée. Je retiens l'annuel pour les comparer de manière homogène, avec la réserve explicite sur les dates de paiement manquantes.

**Conséquence sur la tâche 23.** `Close` et `Dividends` servent au compte de richesse, dans les portefeuilles et les deux fonds. `Adj Close` reste une série de contrôle du fournisseur. SPY et RSP distribuent leurs dividendes, ils ne les réinvestissent pas à la place du porteur.

**Tâche 26.** Chaque portefeuille est calculé en **deux versions**, l'une remise à égalité à la date annuelle de janvier, l'autre sans remise à égalité annuelle. Les entrées et le réinvestissement des dividendes donnent lieu à des transactions dans les deux versions. Vingt séries au lieu de dix.

Les deux versions permettent de suivre la dérive des poids et l'effet de la remise à égalité. Leur différence inclut aussi les transactions, les entrées, les facteurs de marché et les coûts : elle n'est pas un estimateur causal pur du coût de la concentration. La version annuelle ne supprime pas toute concentration entre deux janvier.

La fréquence annuelle limite les remises à égalité, mais il faut y ajouter les entrées en cours d'année. Les dates effectives peuvent être reportées faute de cours. Une sensibilité trimestrielle reste à faire, avec les mêmes règles de dividendes et de coûts. L'accord de deux résultats ne prouverait pas que le choix de fréquence n'a aucun effet.

Dans les deux versions, une entreprise entrant entre deux janvier reçoit un poids moyen par entreprise, financé par une réduction proportionnelle des positions et des espèces existantes. Une seconde classe d'actions partage le poids de son entreprise ; elle ne compte pas comme une entreprise nouvelle.

**Tâche 24, décidée.** Composition complète dans `research/portefeuilles.md`, entreprise par entreprise. Dix portefeuilles construits dans deux modes de gestion, avec équipondération des entreprises à la constitution : `P1` le thème complet, `P2` et `P3` sa partition par maturité, `P4` à `P10` sa partition par canal puis secteur. `P11` est réservé et laissé vide. Les poids ne restent pas égaux entre deux opérations.

Le découpage donne priorité au canal de l'étape 1 pour les acheteurs et vendeurs, puis utilise GICS pour subdiviser les fournisseurs. C'est donc une règle hybride. Les groupes immobilier et fournisseurs technologiques débordent respectivement les seules foncières de centres de données et les seuls fabricants d'outils pour puces. Leurs définitions exactes sont dans `portefeuilles.md`.

Alphabet compte pour une ligne, les poids de ses deux classes d'actions étant additionnés.

`P11`, dit portefeuille d'avenir, est réservé à une exploration fondée sur les résultats futurs du projet. Les dix autres groupes ont des règles antérieures à leur construction ; je ne dispose pas pour autant d'un protocole préenregistré prouvant qu'ils ont été choisis à l'aveugle.

Sept groupes comptent moins de vingt-cinq entreprises. Cela réduit une possibilité de diversification à risques individuels et dépendances donnés, mais ne les rend pas nécessairement plus volatils que `P1`. L'étape 3 devra séparer la taille, les secteurs, les facteurs et les dépendances.

Deux constats matériels ont conduit à cette forme.

Le premier est matériel. Les nombres d'actions instantanés déclarés à la SEC commencent le 24 février 2009 et ne couvrent que 54 entreprises cette année-là. Reconstruire une capitalisation quotidienne depuis 2000 est donc impossible avec les données du dépôt, et non pas seulement difficile. Toute pondération par capitalisation portant sur nos propres portefeuilles est écartée sur la majeure partie de la période. `SPY` et `RSP` apportent deux références de pondération, mais leurs différences ne mesurent pas le seul effet des poids ; le compte du porteur est reconstruit selon notre convention commune de dividendes et de frais.

Le second est méthodologique. Je choisis les groupes issus de la classification de l'étape 1 pour comparer les canaux et la maturité de l'exposition. Une pondération fondée sur des capitalisations connues à chaque date serait une autre comparaison pertinente ; elle ne serait pas anachronique du seul fait d'utiliser la taille. Employer des tailles actuelles dans le passé poserait en revanche ce problème. La classification retenue ne demande pas de capitalisation historique, mais elle reste elle-même fondée sur des informations récentes. Je ne transforme pas cette solution au manque de données en preuve de supériorité méthodologique.

La proposition initiale de sept groupes était une piste de travail. Elle est remplacée par les dix groupes et leurs deux modes de gestion dans `portefeuilles.md`. Le nombre de lignes et la concentration des poids ne suffisent pas à décrire la concentration du risque, qui demande les dépendances entre titres.

**Décision sur la connaissance a posteriori, précisée le 8 septembre.** Je conserve l'exercice rétrospectif sur l'univers actuel, avec interdiction d'en tirer une performance historiquement réalisable ou une attribution causale à l'IA. Les mesures relatives de risque ne sont pas immunisées contre ce biais. Une sélection datée sur un millésime ancien, puis testée sur des données ultérieures, reste une extension nécessaire pour une conclusion prédictive.

### Phase 4 : Construction : **close**

La reconstruction locale est `python -B -m src.construire_portefeuilles`. `src/construire_portefeuille.ipynb` appelle ce même traitement. Les sorties et leurs empreintes sont vérifiées après la construction ; le notebook ne redéfinit plus un second moteur.

| | Tâche | | État |
|---|---|---|---|
| 31 | Rendements individuels | A | `rendements_prix.csv`, `dividendes.csv` |
| 32 | Alignement des dates | A | 6 709 séances, zéro écart |
| 33 | Traitement des valeurs manquantes | A | 18 cours portés, signalés séparément |
| 34 | Reconstruction des capitalisations | A | sans objet, voir tâche 24 |
| 35 | Poids cibles aux dates de rééquilibrage | A | `poids_cibles.csv` |
| 36 | Dérive des poids entre rééquilibrages | A | moteur en montants |
| 37 | Rendement du portefeuille par période | A | idem |
| 38 | Série de valeur en base 100 | A | `valeurs_portefeuilles.csv` |
| 39 | Entrées et sorties de titres | A | idem |
| 40 | Coûts de transaction | A | idem |
| 41 | Portefeuilles de comparaison | A | `valeurs_comparaisons.csv` |
| 42 | Portefeuilles par canal | A | faite dans la tâche 24 |

**Le moteur.** Il suit des montants et non des poids, ce qui rend la dérive automatique et supprime toute renormalisation. Chaque jour, le montant d'un titre est multiplié par un plus son rendement de prix ; le dividende versé alimente une trésorerie attachée à ce titre, réinvestie à la première séance de janvier. Le rendement du portefeuille est la variation de la somme des montants et des trésoreries. Vingt séries en sortent, dix portefeuilles en version rééquilibrée et conservée.

**Validation du moteur.** Les identités de richesse et de frais sont contrôlées chaque jour, y compris les opérations, et un calcul indépendant en nombres de parts reproduit SPY. L'écart avec Yahoo ajusté mélange le calendrier de réinvestissement, la formule de détachement et les coûts ; il ne peut pas être attribué entièrement au délai jusqu'à janvier. Le rapprochement avec un indice publié reste un contrôle de plausibilité, pas une certification de tous les cours.

**Coûts de transaction, mesure corrigée.** La rotation annualisée de `P1` rééquilibré vaut 24,24 % et la perte d'annualisation par rapport au même moteur sans frais vaut 2,87 points de base. Les vingt mesures sont dans `mesures_portefeuilles.csv`. Les sensibilités du rapport d'audit comparent la même construction à différents taux ; leur portée reste celle d'un modèle sans impact de marché.

**Un défaut corrigé.** La première version des séries de comparaison appliquait aux indices le filtre de volume nul conçu pour les actions. Un indice ne s'échange pas et Yahoo lui attribue un volume nul sur toutes ses séances : le filtre effaçait l'intégralité de `^SP500TR` et de `^SPXEW`, et la première disparaissait du tableau sans message. Corrigé en n'appliquant le filtre qu'aux titres dont le champ `type` des métadonnées n'est pas `INDEX`. C'est le même défaut de conception que les trois de la phase 2 : une règle validée sur une population, appliquée sans examen à une autre.

**Comparaison descriptive, à ne pas confondre avec une attribution.** Les chiffres de 11,56 % et 11,36 % par an pour SPY et RSP concernaient les séries Yahoo ajustées sur leur fenêtre commune depuis mai 2003. Les références principales ont maintenant la convention annuelle commune aux portefeuilles ; leurs résultats sont dans l'audit. Les différences de poids, de rééquilibrage et de frais internes empêchent d'attribuer à la seule concentration l'écart entre les fonds.

**Rappel contraignant.** L'écart entre les portefeuilles et SPY n'est pas une mesure de la taille du biais de connaissance a posteriori. Il combine la sélection, les secteurs, la pondération, les entrées et d'autres effets. Les mesures absolues comme relatives décrivent des paniers choisis aujourd'hui ; leur robustesse et leurs facteurs restent à étudier.

### Phase 5 : Contrôle des résultats, identités vérifiées et interprétation réservée

| | Tâche | | État |
|---|---|---|---|
| 43 | Somme des poids égale à 1 | A | écart maximal 4,45 × 10⁻¹⁶ |
| 44 | Aucun poids négatif ni aberrant | A | aucun cas |
| 45 | Nombre de titres présents par date | A | aucun cas |
| 46 | Plausibilité des rendements cumulés | A | aucun cas |
| 47 | Cohérence de l'agrégation | A | identité quotidienne, écart inférieur à 10⁻¹² |
| 48 | Reconstruction comparée aux indices publiés | A | contrôles de convention et oracle SPY, couverture externe partielle |

Les poids sont photographiés à la dernière séance disponible de chaque mois, soit 321 relevés et 225 984 lignes, y compris les poids nuls, dans `data/processed/poids_mensuels.csv`. Le dernier relevé est au 4 septembre, fin du cliché et non fin du mois civil. La fréquence mensuelle permet de suivre la dérive entre les opérations ; une photographie annuelle n'aurait une dérive nulle que si elle était prise immédiatement après une remise à égalité.

**Tâche 47, portée du contrôle.** La partition des entreprises permet une identité de mélange à poids initiaux égaux, sans frais et sans opérations différentes entre les sous-groupes. Cette identité ne certifie pas la trajectoire complète avec entrées et rééquilibrages. Le contrôle décisif porte maintenant chaque jour sur la richesse avant opérations, les rendements, les dividendes et les frais réellement facturés.

**Tâche 48.** L'écart d'environ neuf points de base entre SPY ajusté et `SP500TR` est proche des frais internes annoncés du fonds, sans les identifier exactement : conventions, suivi de l'indice et fenêtres interviennent aussi. L'écart entre `^GSPC` et `SP500TR` est celui de deux conventions d'indice. Il ne se transpose pas automatiquement à la contribution des dividendes d'un compte espèces.

**Une erreur de description corrigée.** `^SPXEW` est un indice de prix, sans dividendes. Que RSP, dividendes inclus, le dépasse n'a donc rien d'impossible ; c'était une comparaison de conventions différentes. Il reste un contrôle en prix, et RSP la référence équipondérée avec distributions à partir de mai 2003.

**Une erreur de test corrigée par cet audit.** Exclure les dates de rééquilibrage du contrôle masquait une faiblesse. Réinvestir des espèces ne crée pas de richesse. Le rendement avant frais doit se raccorder à la moyenne des rendements totaux des positions, espèces à rendement nul incluses ; les frais expliquent ensuite la différence. Ce contrôle s'applique aussi les jours d'opération, sans leur donner une exemption.

**Replis maximaux mesurés.** Les ordres de grandeur des séries corrigées sont de −83 % pour `P9` conservé, −45 % pour `P6`, −54 % pour `P1` et −55 % pour SPY reconstruit. Leurs dates, les deux modes de gestion et les fenêtres doivent accompagner une comparaison ; leur plausibilité historique ne prouve pas l'exactitude de toutes les observations.

**Concentration, résultats mis à jour.** Les chiffres précédents, 24,8 % sur Nvidia dans `P1` conservé et 59,5 % sur Tesla dans `P4` conservé, correspondaient bien aux poids des fichiers avant cet audit. Les nouvelles règles d'entrée et d'identité ont changé les trajectoires : les mesures actuelles figurent dans le rapport d'audit. La dérive vient des rendements sous une règle de gestion choisie ; l'absence de remise à égalité est elle-même une décision, pas l'absence de toute décision.

### Phase 6 : Tests : **close**

| | Tâche | | État |
|---|---|---|---|
| 49 | Proposition des cas qui doivent faire échouer le code | C | `research/cas_de_test.md`, treize cas |
| 50 | Écriture des tests | C | 48 tests de l'étape 2, 99 tests dans l'ensemble du dépôt |

Les tests combinent des défauts déjà rencontrés et des contre-exemples construits pour mettre les règles en difficulté. Les exemples courts vérifient la mécanique ; les replays sur le cliché vérifient l'intégration. Aucun ensemble de tests ne garantit l'absence de toute erreur. Les cas et leur couverture sont dans `research/cas_de_test.md`.

Écrire les tests a d'abord exigé de sortir le moteur du notebook vers `src/portefeuille.py` : `import` sait lire un fichier `.py` et non un `.ipynb`. Le notebook importe désormais ses fonctions au lieu de les définir. Le partage du travail est acté à partir de là : les fichiers `.py` reviennent à l'assistant, les notebooks à l'auteur.

**Le test a trouvé un défaut réel du moteur, et il changeait une conclusion.** Dans la version conservée, un titre entrant en cours de période recevait son montant sans que les titres déjà détenus soient réduits en face : le portefeuille créait de la valeur à chaque nouvelle cotation, lors des admissions effectuées par cette ancienne version. La tâche 26 énonçait pourtant la bonne règle, une entrée financée par une réduction proportionnelle des autres ; le code en appliquait une autre.

Lors de cette correction antérieure à l'audit du 8 septembre, `P1` conservé était passé de 12 464 à 8 978 en base 100 et `P5` conservé de 30 266 à 18 501. Les fichiers présents au début de l'audit donnaient un avantage de performance à la version rééquilibrée dans six groupes sur dix, et non sept comme je l'avais écrit. Ces niveaux sont historiques : les corrections d'entrée, d'identité et de coûts de cet audit changent aussi les séries rééquilibrées. Les vingt résultats courants et leur comparaison avec ce cliché précédent sont publiés dans l'audit.

Les poids relatifs du fichier précédent ont été recalculés et concordaient avec les chiffres du journal. Cela ne prouve pas qu'une correction d'entrée préserve toujours la concentration : les nouvelles dates et le financement des entrées peuvent la modifier.

Un second échec de test avait été attribué à un dividende sans baisse de cours. Cette justification était fausse : une hausse de marché peut compenser le détachement. Le test doit accepter un dividende avec un cours stable ou en hausse et vérifier la richesse correspondante, sans imposer une baisse mécanique observée.

### Phase 7 : Documentation et clôture : en cours, 4 tâches sur 5

| | Tâche | |
|---|---|---|
| 51 | Règles de construction des portefeuilles | A | **faite**, `research/portefeuilles.md` |
| 52 | Écriture des limites | A | **faite**, section IV et `portefeuilles.md` |
| 53 | Mise à jour des notes | A | **faite** |
| 54 | Intégration au pipeline | C | **faite**, `data/processed/pipeline_portefeuilles.json`, commande locale documentée |
| 55 | Commit | A | à faire |

---

## III. Deux pièges connus, à traiter au moment prévu

**Les capitalisations, tâche 34.** Les prix de Yahoo sont retraités des divisions d'actions ; les nombres d'actions déclarés à la SEC ne le sont pas. Les multiplier tels quels donnerait une capitalisation fausse d'un facteur égal au cumul des divisions. Aucun calcul du dépôt ne fait aujourd'hui cette multiplication. Le contrôle sera simple : une division d'actions ne doit produire aucun saut dans la série de capitalisation.

**Les historiques courts, tâches 21 et 27.** Sur les 114 séries pour 113 entreprises, la plus courte compte 216 séances, depuis le 27 octobre 2025. Exiger les 113 simultanément réduirait la période à dix mois.

Cette fenêtre n'est pas dépourvue de mouvement : `^GSPC`, indice de prix, y présente un repli maximal de 9,10 %, tandis que `^SP500TR`, dividendes inclus, donne 8,89 %. Le chiffre précédent était défendable en rendement total mais ne précisait pas la série. Une fenêtre aussi courte manque surtout de profondeur et de diversité de régimes ; les épisodes de stress seront définis avant leur comparaison à l'étape 3.

Le benchmark équipondéré `RSP` ne remonte par ailleurs qu'à 2003.

---

## IV. Limites qui traversent tout le projet

**Connaissance a posteriori.** L'univers est sélectionné avec des rapports de 2026 et sera appliqué à des prix antérieurs. Toute performance calculée décrit le passé d'un panier constitué aujourd'hui ; elle ne décrit pas une stratégie qu'un investisseur aurait pu suivre.

**Composition d'indice figée.** La liste des composants du S&P 500 est celle d'une date donnée. Les entreprises sorties de l'indice n'y figurent pas.

**Source de prix non officielle.** Yahoo Finance réécrit rétroactivement ses prix ajustés à chaque dividende et chaque division. Une nouvelle collecte ne redonnera pas les mêmes valeurs. Les fichiers conservés et leurs empreintes fixent un cliché daté ; les calculs faits à partir de ce cliché restent reproductibles.

**Univers provisoire.** Soixante-seize dossiers restent à examiner. La composition peut donc encore changer.

## V. État après l'audit du 8 septembre 2026

La construction de l'étape 2 est corrigée et reproductible. Sa validation de données n'est pas intégrale : le complément `research/verification_etape_2.md` remplace le bilan courant de l'audit initial et recense exactement la couverture, les corrections et les écarts non arbitrés. L'étape n'est pas présentée comme entièrement validée.

La réserve de validation porte sur les cours anciens non corroborés et les différences de fournisseurs recensées dans le complément. Le paiement des dividendes et la conservation juridique des titres sont des limites d'exécution de la convention synthétique retenue. La comparaison des fréquences de gestion relève de l'étape 3 ; elle n'est pas ajoutée aux exigences de construction. Les risques, facteurs, stress, diversification et couvertures relèvent des étapes suivantes ; leur absence n'est pas une erreur de construction. Le commit reste une opération de l'auteur, séparée de la validation scientifique.
