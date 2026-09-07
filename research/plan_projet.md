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
| 2 | Méthode de contrôle par seconde source | C | **à formaliser**, aucun protocole écrit dans le dépôt |
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

### Phase 2 — Contrôle de la donnée brute — non commencée

| | Tâche | |
|---|---|---|
| 13 | Trous dans les séries et séances absentes | A |
| 14 | Variations quotidiennes aberrantes | A |
| 15 | Cohérence de l'ajustement | A |
| 16 | Vérification d'un échantillon contre une seconde source | A |
| 17 | Cohérence des dates de première cotation | A |
| 18 | Devise et place de cotation | A |
| 19 | Retraits de cote et changements de symbole | A |
| 20 | Remise du rapport de contrôle intégral | A |

Un audit externe a déjà relevé deux anomalies qui relèvent de cette phase : une incohérence de barre sur `HUBB` au 5 mai 2021, où l'ouverture est inférieure au minimum, et quatorze séances absentes de `SPXEW` entre 2015 et 2019.

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
