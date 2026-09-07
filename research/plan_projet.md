# Plan du projet et état d'avancement

*AI Concentration Risk Research. 7 septembre 2026.*

Ce document dit où en est le projet, selon quel découpage, et à quelles conditions une étape est considérée comme close. Il existe parce qu'un audit externe a constaté que ce découpage n'apparaissait dans aucun fichier du dépôt : il ne vivait que dans les échanges de travail.

---

## I. Les cinq étapes

| | Étape | État |
|---|---|---|
| 1 | Construire un univers d'entreprises exposées à la chaîne des infrastructures de calcul | **close**, version exploratoire |
| 2 | Construire les portefeuilles à partir de cet univers | en cours, phase 1 sur 8 close |
| 3 | Mesurer le risque, ses sources et son comportement en crise | non commencée |
| 4 | Étudier la couverture et la diversification | non commencée |
| 5 | Comparer les stratégies, coûts et risque résiduel | non commencée |

**Ce que « close » veut dire ici.** Une étape est close quand ses livrables existent, se régénèrent dans le schéma annoncé, et que ses limites sont écrites. Cela ne signifie pas que tous les jugements sont définitifs ni que toutes les vérifications imaginables ont été faites.

L'étape 1 est close en ce sens : 113 entreprises retenues, 38 douteuses et 76 en attente d'examen. Sur les 500 dossiers, **482 portent une citation et 18 n'en portent aucune** ; ces 18 sont tous au statut à examiner, ce qui est cohérent avec leur état mais interdit d'écrire que chaque décision est adossée à une citation.

---

## II. Le découpage de l'étape 2

Huit phases, cinquante-cinq tâches. La répartition indique qui produit quoi : **A** pour l'auteur, **C** pour l'assistant.

### Phase 0 — Décisions avant collecte — **close**

| | Tâche | | État |
|---|---|---|---|
| 1 | Source de prix et écriture de ses limites | A | yfinance retenu |
| 2 | Méthode de contrôle par seconde source | C | protocole à trois niveaux, écrit en phase 2 |
| 3 | Traitement des classes d'actions multiples | A | classes conservées séparément à la collecte |

Les deux benchmarks retenus sont `SPY`, réplique du S&P 500 pondéré par capitalisation, et `RSP`, réplique de sa version équipondérée. Trois indices sont collectés en complément pour le contexte et le contrôle.

### Phase 1 — Collecte — **close**

| | Tâche | | État |
|---|---|---|---|
| 4 | Correspondance CIK vers symbole | C | faite, `BRK.B` interrogé sous `BRK-B` |
| 5 | Cours quotidiens bruts | A | 113 séries |
| 6 | Cours quotidiens ajustés | A | mêmes fichiers |
| 7 | Dividendes | A | mêmes fichiers |
| 8 | Divisions d'actions | A | mêmes fichiers |
| 9 | Nombre d'actions en circulation | A | 8 987 lignes, 112 entreprises |
| 10 | Séries de comparaison | A | 2 fonds et 3 indices |
| 11 | Calendrier de bourse | A | 8 458 séances depuis 1993 |
| 12 | Manifeste de collecte | A | empreintes et limites écrites |

### Phase 2 — Contrôle de la donnée brute — **close**

Les résultats sont écrits dans `data/processed/controle_prix.csv`, une ligne par anomalie, avec le fichier, le test, la date et un détail. Chaque bloc de `src/controler_prix.ipynb` réécrit ses propres tests et laisse les autres intacts, de sorte qu'on peut le relancer seul.

| | Tâche | | État |
|---|---|---|---|
| 13 | Trous dans les séries et séances absentes | A | 73 anomalies |
| 14 | Variations quotidiennes aberrantes | A | 128 anomalies |
| 15 | Cohérence de l'ajustement | A | aucune anomalie |
| 16 | Vérification contre une seconde source | A | 20 divisions non confirmées |
| 17 | Cohérence des dates de première cotation | A | 56 anomalies |
| 18 | Devise et place de cotation | A | aucune anomalie |
| 19 | Retraits de cote et changements de symbole | A | 8 393 anomalies |
| 20 | Remise du rapport de contrôle intégral | A | `research/controle_donnees_prix.md` |

**Tâche 13.** Quatorze séances absentes de `SPXEW` entre 2015 et 2019, et cinquante-neuf séries antérieures au calendrier de bourse, ce dernier ne remontant qu'à 1993.

**Tâche 14.** Cent vingt-six variations ajustées de plus de 30 %, une barre incohérente sur `HUBB` au 5 mai 2021 où l'ouverture est inférieure au minimum, et une ligne sans aucun prix sur `HUBB` au 8 août 1977. Cette dernière n'était pas détectée par le test des prix négatifs : une valeur manquante ne satisfait aucune comparaison. Un test explicite a été ajouté.

**Tâche 15.** Le prix ajusté de Yahoo se reconstruit à partir du prix de clôture et des dividendes selon une convention multiplicative, le dividende étant retiré du prix de départ et non ajouté au prix d'arrivée. La formule additive s'écarte jusqu'à 8 % sur `JCI` ; la formule multiplicative reste sous 5 × 10⁻⁵ sur les 118 fichiers. Tous les écarts de la formule additive tombent sur des jours de détachement, aucun ailleurs.

**Tâche 16.** Aucune source externe automatisable n'a été trouvée sans compte : Stooq sert désormais ses fichiers derrière une vérification anti-robot. Le contrôle retenu confronte les divisions d'actions déclarées par Yahoo au nombre d'actions déposé à la SEC au trimestre suivant, deux collectes d'origines indépendantes. Sur 56 divisions depuis 2010, 9 ne sont pas encadrées par des dépôts et 20 ne sont pas confirmées.

Ces vingt cas ne sont pas des erreurs de collecte. La colonne `Stock Splits` de Yahoo contient deux natures d'événements : les divisions véritables, que la SEC confirme, et les facteurs d'ajustement de prix consécutifs à une scission, où le nombre d'actions ne bouge pas. `MMM` en avril 2024 pour Solventum, `IBM` en novembre 2021 pour Kyndryl. **Conséquence pour la tâche 34** : le facteur cumulé des divisions ne peut pas être lu directement dans cette colonne.

**Tâche 19.** Aucune série ne s'arrête avant la dernière séance du calendrier, ce qui ne prouve rien : la liste des composants étant un cliché de 2026, une entreprise retirée de la cote n'a jamais eu de fichier. Six dénominations divergent entre Yahoo et le S&P 500, toutes des variantes d'écriture sauf Schlumberger, devenu SLB N.V.

En cherchant l'origine de la plus forte variation de la liste, `HUBB` au 31 octobre 1994 à +885,9 %, j'ai trouvé un défaut que le plan n'avait pas prévu de tester. Ce n'est pas un mouvement de marché mais la soudure entre un segment fabriqué et le début des vraies cotations. **Huit mille deux cent soixante-douze lignes portent un volume nul et quatre cours identiques, égaux à la clôture de la veille**, réparties sur 44 fichiers, dont 41 % de l'historique de `HUBB` et 18 % de celui de `CRH`. Elles produiraient des rendements nuls et abaisseraient toute volatilité calculée sur les périodes anciennes. Deux tests ajoutés, séance sans transaction et prix figé.

**Tâche 20.** Rapport intégral dans `research/controle_donnees_prix.md` : vingt-trois tests, huit mille six cent soixante-dix anomalies sur 1 043 940 lignes, cent fichiers concernés sur cent dix-huit. Le rapport liste aussi les tests restés à zéro, que le fichier de contrôle ne peut pas montrer.

**Tâche 17.** Trente-sept fichiers de prix n'ont aucune entrée dans `data/raw/premieres_cotations.csv`, construit du temps où l'univers comptait 82 entreprises et jamais régénéré depuis. Sur les 76 restants les dates concordent, mais ce zéro ne prouve rien : les deux fichiers viennent de la même source.

Le résultat utile vient de la contrainte logique inverse. Dix-neuf entreprises sont entrées dans le S&P 500 avant la première ligne de prix que Yahoo nous donne. Douze séries commencent exactement le 17 mars 1980, neuf le 21 février 1973, huit le 2 janvier 1962. Aucune entreprise n'introduit ses actions le même matin que onze autres : ce sont les strates de départ de la base de Yahoo. **Une date de début de série ne dit pas quand le titre a commencé d'exister, elle dit à partir de quand Yahoo en parle.** À retenir pour les tâches 21 et 27.

**Tâche 18.** Les 118 fichiers sont libellés en dollars, sur des places américaines, avec les seuls décalages horaires de New York. Les métadonnées descriptives sont collectées dans `data/raw/metadonnees_titres.csv`. Aucune anomalie après correction.

Trois versions ont été nécessaires, et les trois échecs relèvent du même défaut de conception. La première interrogeait Yahoo avec la valeur de la colonne `symbole`, qui vaut `BRK.B` dans le fichier de Berkshire alors que la donnée avait été collectée sous `BRK-B` ; Yahoo répond un dictionnaire vide sans lever d'erreur, et le compteur annonçait 118 succès pour 117. La deuxième traitait toute réponse non vide comme un succès ; interrogée avec `^RSP` et `^SPY`, elle a reçu la description d'indices d'options homonymes, réels mais sans historique de prix. La troisième exige une date de première transaction, seule preuve qu'il s'agit d'un instrument négociable.

**La règle qui en sort : vérifier la présence du succès attendu, jamais l'absence de l'échec imaginé.** Le même défaut avait produit la valeur manquante non détectée de la tâche 14.

La colonne `symbole` de `BRK-B.csv` conserve `BRK.B` alors que la collecte s'est faite sous `BRK-B`. Le fichier de prix est correct, son étiquette de provenance ne l'est pas. Écart documenté plutôt que corrigé, pour ne pas invalider l'empreinte du manifeste.

Une première version de ce contrôle donnait deux résultats différents sur deux machines pour `DUK` au 3 juillet 2012. Cause : soixante-six couples entreprise et date de mesure portent deux déclarations distinctes, l'entreprise réexprimant une date déjà publiée après un regroupement, et le tri par défaut de pandas n'est pas stable entre ex aequo. Corrigé en triant explicitement sur la date de dépôt plutôt que sur la date de mesure, une déclaration ne pouvant refléter une division que si elle a été écrite après. Les deux exécutions concordent désormais à la sixième décimale.

`DUK` reste non confirmé pour une raison réelle : le regroupement de juillet 2012 est simultané à l'absorption de Progress Energy, deux événements que le nombre d'actions ne permet pas de séparer.

Un point reste ouvert sur cette phase : le niveau manuel du protocole de seconde source, un échantillon relevé à la main sur un site public, n'a pas encore été exécuté.

### Phase 3 — Décisions en voyant les données — non commencée

| | Tâche | |
|---|---|---|
| 21 | Période d'étude | A |
| 22 | Fréquence des rendements | A |
| 23 | Rendement total ou de prix | A |
| 24 | Portefeuilles à construire, donc les poids | A |
| 25 | Nombre de titres du portefeuille concentré | A |
| 26 | Règle de rééquilibrage | A |
| 27 | Traitement des entreprises récemment cotées | A |
| 28 | Poche de liquidités ou investissement intégral | A |
| 29 | Coûts de transaction | A |
| 30 | Portefeuilles par canal d'exposition | A |

### Phase 4 — Construction — non commencée

| | Tâche | |
|---|---|---|
| 31 | Rendements individuels | A |
| 32 | Alignement des dates | A |
| 33 | Traitement des valeurs manquantes | A |
| 34 | Reconstruction des capitalisations | A |
| 35 | Poids cibles aux dates de rééquilibrage | A |
| 36 | Dérive des poids entre rééquilibrages | A |
| 37 | Rendement du portefeuille par période | A |
| 38 | Série de valeur en base 100 | A |
| 39 | Entrées et sorties de titres | A |
| 40 | Coûts de transaction | A |
| 41 | Portefeuilles de comparaison | A |
| 42 | Portefeuilles par canal | A |

### Phase 5 — Contrôle des résultats — non commencée

| | Tâche | |
|---|---|---|
| 43 | Somme des poids égale à 1 | A |
| 44 | Aucun poids négatif ni aberrant | A |
| 45 | Nombre de titres présents par date | A |
| 46 | Plausibilité des rendements cumulés | A |
| 47 | Cohérence de l'agrégation | A |
| 48 | Reconstruction du S&P 500 comparée à l'indice publié | A |

### Phase 6 — Tests — non commencée

| | Tâche | |
|---|---|---|
| 49 | Proposition des cas qui doivent faire échouer le code | C |
| 50 | Écriture des tests | A |

### Phase 7 — Documentation et clôture — non commencée

| | Tâche | |
|---|---|---|
| 51 | Règles de construction des portefeuilles | A |
| 52 | Écriture des limites | A |
| 53 | Mise à jour des notes | A |
| 54 | Intégration au pipeline | C |
| 55 | Commit | A |

---

## III. Deux pièges connus, à traiter au moment prévu

**Les capitalisations, tâche 34.** Les prix de Yahoo sont retraités des divisions d'actions ; les nombres d'actions déclarés à la SEC ne le sont pas. Les multiplier tels quels donnerait une capitalisation fausse d'un facteur égal au cumul des divisions. Aucun calcul du dépôt ne fait aujourd'hui cette multiplication. Le contrôle sera simple : une division d'actions ne doit produire aucun saut dans la série de capitalisation.

**Les historiques courts, tâches 21 et 27.** Sur les 113 séries, la plus courte compte 216 séances, depuis le 27 octobre 2025. Exiger les 113 simultanément réduirait la période à dix mois.

Cette fenêtre n'est pas calme pour autant. Le S&P 500 y enregistre un repli maximal de 8,89 %, entre le sommet du 27 janvier 2026 et le creux du 30 mars 2026. L'argument contre une période aussi courte n'est donc pas l'absence de tension, mais le manque de profondeur et de diversité des régimes de marché traversés. Les seuils définissant un épisode de stress restent à établir, et ils le seront avant toute comparaison.

Le benchmark équipondéré `RSP` ne remonte par ailleurs qu'à 2003.

---

## IV. Limites qui traversent tout le projet

**Connaissance a posteriori.** L'univers est sélectionné avec des rapports de 2026 et sera appliqué à des prix antérieurs. Toute performance calculée décrit le passé d'un panier constitué aujourd'hui ; elle ne décrit pas une stratégie qu'un investisseur aurait pu suivre.

**Composition d'indice figée.** La liste des composants du S&P 500 est celle d'une date donnée. Les entreprises sorties de l'indice n'y figurent pas.

**Source de prix non officielle.** Yahoo Finance réécrit rétroactivement ses prix ajustés à chaque dividende et chaque division. Une nouvelle collecte ne redonnera pas les mêmes valeurs. Les fichiers conservés et leurs empreintes fixent un cliché daté ; les calculs faits à partir de ce cliché restent reproductibles.

**Univers provisoire.** Soixante-seize dossiers restent à examiner. La composition peut donc encore changer.
