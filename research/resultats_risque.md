# Résultats de l'étape 3 : le risque, ses sources et son comportement en crise

*AI Concentration Risk Research. 8 septembre 2026.*

Ce document rapporte ce que la mesure établit, question par question. Les huit décisions de méthode ont été fixées et écrites avant qu'aucun chiffre de risque ne soit produit ; elles figurent à la section VI de `research/plan_projet.md`. Les calculs sont dans `src/mesurer_risque.ipynb` et `src/risque.py`, les cas de contrôle dans `tests/test_risque.py`, et les sorties dans `data/processed/`.

Je réponds dans l'ordre des six questions de la section 8 du contexte maître.

> **Mise à jour du 28 septembre 2026.** Trois contrôles ont été ajoutés après la rédaction initiale : un groupe témoin construit avec les 366 entreprises SORT, un bootstrap des écarts entre gestions, et la correction de Forbes et Rigobon sur la corrélation de crise. Ils confirment les résultats sur la volatilité et la concentration du risque, mais en affaiblissent trois : l'avantage de Sharpe du rééquilibrage, la montée de la corrélation en crise, et le caractère propre au thème d'une diversification épuisée. Les passages concernés renvoient à la section XI, qui donne les chiffres.

---

## I. La concentration apporte-t-elle un supplément de rendement

Non, ou pas de façon décidable.

Sur les dix portefeuilles, la gestion qui laisse la concentration se former rapporte davantage que la gestion rééquilibrée dans **six cas sur dix**. C'est le résultat le moins net de toute l'étude, et il ne survit pas au changement de période : depuis le 19 août 2004, il tombe à **quatre sur dix**.

Sur `P1`, le thermomètre du thème, l'écart annualisé vaut **huit centièmes de point**, 18,78 % contre 18,70 %. Deux gestions du même univers sur la même période, indiscernables.

Ce classement a changé de sens trois fois au cours du projet, au fil des corrections du moteur de construction. Il ne peut pas porter une conclusion.

**Les niveaux eux-mêmes ne sont pas interprétables.** Les portefeuilles ressortent entre 11,0 % et 21,7 % par an quand `SPY` fait 8,35 %. Cet écart n'est pas un résultat sur l'intelligence artificielle, c'est la taille du biais de connaissance a posteriori : l'univers a été établi avec des rapports de 2026 puis appliqué à des prix depuis 2000. Aucune performance de ce document ne décrit une stratégie qu'un investisseur aurait pu suivre. Le groupe témoin chiffre ce biais : les 366 entreprises SORT, construites de la même façon, rapportent 16,07 % par an. Environ 7,7 des 10,4 points d'écart entre `P1` et `SPY` se retrouvent donc hors du thème (section XI).

## II. Quel risque faut-il supporter

Le portefeuille du thème est plus risqué que le marché, et moins que ce qu'on pourrait croire.

`P1` rééquilibré présente une volatilité annualisée de **21,73 %** contre **19,11 %** pour `SPY`, soit **1,14 fois** le marché. Quatorze pour cent de risque en plus, mesuré sur 6 708 rendements quotidiens.

**Le thème n'est pas un bloc.** Deux de ses maillons sont moins volatils que le marché : les engagements documentés à 18,46 % et l'électricité à 18,94 %. À l'autre extrémité, l'amont des semi-conducteurs atteint 35,18 %, soit 1,84 fois le marché. Un rapport de près de deux entre deux morceaux de la même chaîne.

La distribution n'est pas normale, et l'écart n'est pas marginal. L'aplatissement excédentaire va de **4,3 à 14,8** quand il devrait valoir zéro, les journées au-delà de trois écarts-types représentent **1,31 % à 1,82 %** du total contre 0,27 % attendus, et le test de Jarque-Bera rejette la normalité sur **les vingt-cinq séries**. En conséquence, une VaR gaussienne sous-estime la perte de **13 % à 21,5 %**, toujours dans le sens rassurant. Elle est écartée de l'étude et ne figure qu'à titre de démonstration de son propre défaut.

Le risque vécu se mesure aussi en durée. Toutes les séries passent **86 % à 94 % de leur temps sous leur plus haut**, `SPY` compris. Les replis maximaux vont de 45 % à 87 %, et le pire, celui des acheteurs d'infrastructure en version conservée, a demandé **2 372 séances, soit plus de neuf ans**, pour être effacé.

## III. Le rendement compense-t-il le risque

Sur la comparaison qui nous occupe, non.

Le ratio de Sharpe donne l'avantage au rééquilibrage dans **neuf portefeuilles sur dix**, et le Sortino dans huit. Là où le rendement brut ne tranchait pas, le rendement rapporté au risque tranche.

En rassemblant les huit critères de la tâche 29 :

| Critère | Victoires du rééquilibrage |
|---|---|
| Volatilité | 9 sur 10 |
| Semi-volatilité | 9 sur 10 |
| Drawdown | 7 sur 10 |
| VaR à 99 % | 8 sur 10 |
| Perte moyenne au-delà | **10 sur 10** |
| Sharpe | 9 sur 10 |
| Sortino | 8 sur 10 |
| Rendement | 6 sur 10 |

Sur la mesure la plus exigeante, la perte moyenne au-delà de la VaR à 99 %, le rééquilibrage l'emporte **sans exception**.

Deux nuances imposées par les contrôles. `P6` est indécidable : ses deux gestions diffèrent de six dixièmes de point de volatilité, et le verdict change selon la fréquence de mesure. `P5`, les vendeurs de puces, est la seule vraie exception : sa version conservée gagne au Sharpe, au Sortino et au rendement, tout en perdant sur les cinq mesures de risque pur. Elle a été payée pour son risque supplémentaire, contrairement aux neuf autres.

La formulation exacte est donc : **le rééquilibrage réduit le risque sur huit portefeuilles aux deux fréquences, `P5` fait exception, et `P6` est indécidable.**

Le bootstrap de la section XI précise la portée de ces décomptes. La baisse de volatilité est significative à 5 % sur huit portefeuilles sur dix. L'avantage de Sharpe ne l'est que sur `P4` : pour les neuf autres, l'écart observé reste dans ce que le hasard d'échantillonnage produit. Le rééquilibrage réduit donc le risque de façon établie, mais son meilleur rendement ajusté du risque n'est pas démontré.

## IV. Que devient le portefeuille en marché défavorable

Six épisodes de tension sont identifiés mécaniquement, comme un repli de `SPY` d'au moins 15 % depuis son plus haut. Du sommet au creux, ils couvrent 1 315 séances sur 6 709, soit 19,6 % de la période. Aucune date n'est choisie à la main.

**Le pire moment n'est pas le même pour tout le monde.** Les maillons liés aux puces ont leur repli maximal en 2000-2002, où ils perdent 65 % à 87 %. Les autres, et le marché, l'ont en 2008-2009, avec 52 % à 58 %. Un investisseur qui aurait mesuré le risque de ce thème en 2007 en regardant les cinq années précédentes n'aurait rien vu venir.

**L'électricité est l'amortisseur du thème.** Sur les six épisodes, elle en traverse quatre presque intacte : +4,3 % en 2000-2002 quand le marché perd 47,3 %, −0,3 % en 2018, −8,4 % en 2025. Elle ne souffre que dans les deux épisodes où tout tombe, 2008 et 2020.

**La diversification s'évapore quand elle servirait.** La corrélation interne monte en période de tension dans les **dix portefeuilles sans exception**, de 9 % sur l'électricité à 72 % sur les acheteurs. Traduit avec la formule de décomposition, `P1` passe de **3,21 actifs indépendants équivalents au calme à 2,29 en tension**, et les acheteurs de 2,58 à 1,66.

Cette hausse est brute. La variance de `SPY` est multipliée par 3,73 pendant les épisodes de tension, et une corrélation mesurée quand la variance du marché augmente monte mécaniquement. Après la correction de Forbes et Rigobon, la corrélation de tension devient inférieure à la corrélation de calme dans neuf portefeuilles sur dix et dans le témoin ; seul `P4` garde une hausse, de 0,006. Cette correction est elle-même discutée et ne prouve pas l'absence de contagion. La phrase juste est donc : les titres bougent davantage ensemble en crise ; cette hausse est compatible avec la seule domination du facteur de marché, sans que l'on puisse exclure un renforcement de leur lien propre (section XI).

**Les portefeuilles qui paraissent défensifs perdent leur caractère défensif à la baisse.** Le bêta conditionnel de `P10` conservé vaut 0,980 quand le marché monte et **1,103** quand il baisse. Le même écart, positif donc défavorable, se retrouve sur les engagements documentés, l'immobilier et l'électricité. À l'inverse, les maillons des puces, dont le bêta dépasse 1,35, participent moins aux baisses qu'aux hausses.

**La VaR n'est pas honnête, et je le chiffre.** Estimée sur 252 séances glissantes et testée le lendemain, la VaR à 99 % est dépassée entre **1,39 % et 1,81 % du temps** au lieu de 1 %, et le test de Kupiec la rejette sur **les vingt-cinq séries, `SPY` compris**. Les dépassements arrivent de plus en paquets, dix à vingt fois plus souvent que l'indépendance ne le permettrait. Perdre plus que sa VaR n'est pas un accident isolé, c'est un état qui dure plusieurs jours.

## V. Peut-on réduire ces risques par la diversification

Par le nombre de titres, non : cette voie est déjà épuisée.

La corrélation moyenne interne de `P1` vaut **0,338**. En appliquant la décomposition de la volatilité d'un portefeuille équipondéré, ses 135 lignes réduisent le risque autant que le feraient **2,92 titres parfaitement indépendants**. Le plancher, celui qu'atteindrait un portefeuille de taille infinie, vaut 22,69 % contre 22,85 % pour la volatilité prédite : il reste **quarante-deux centièmes de point à gagner** en ajoutant des entreprises. Rien.

Aucun des dix portefeuilles ne dépasse **trois actifs indépendants équivalents**. Passer de vingt-quatre à cent trente-cinq entreprises, soit 5,6 fois plus, achète six dixièmes d'actif indépendant.

Ce plafond n'est pas propre au thème. Les 368 titres du témoin ont une corrélation moyenne de 0,309 et valent 3,21 actifs indépendants, contre 0,338 et 2,92 pour `P1`. La diversification par le nombre est épuisée pour l'ensemble des survivants du S&P 500, et le thème n'y est qu'un peu plus exposé (section XI).

L'analyse en composantes principales confirme par une autre voie. Le premier facteur explique 27,6 % de la variance de `P1`, et son inverse vaut 3,6, du même ordre que le 2,92 obtenu par la corrélation. Deux méthodes indépendantes s'accordent autour de trois. Il faut **22 facteurs pour expliquer 70 %** de la variance de 132 titres, et sur l'électricité un seul facteur en explique **57,8 %**.

Ajouter des entreprises d'un même thème ajoute des lignes, pas des directions.

## VI. Quels risques ne peuvent pas être éliminés

Trois, et ils sont chiffrés.

**Le risque de corrélation.** Sur les 39,03 % de volatilité individuelle moyenne des titres de `P1`, la diversification par le nombre en retire 41,45 %. Il reste **22,69 % que rien ne peut retirer par ce moyen**, parce que ces entreprises bougent ensemble. C'est le plancher de la section précédente, vu comme une contrainte.

**La concentration du risque, qui ne se voit pas dans les poids.** Dans les vingt séries sans exception, le risque est plus concentré que l'argent. `P1` rééquilibré détient 135 lignes, son argent se répartit comme sur 107, et **son risque comme sur 30**. Le rapport entre les deux concentrations atteint 3,60, et il est **plus élevé dans les versions rééquilibrées** : à poids égaux, un portefeuille qui mêle des électriciens à 15 % de volatilité et des semi-conducteurs à 60 % ne répartit jamais son risque également. Regarder les poids pour juger de la concentration du risque est trompeur.

**La contagion.** `P1` rééquilibré ne détient que 3,7 % de sa première ligne. Si celle-ci perdait la moitié de sa valeur, le portefeuille perdrait **8,2 %**, soit quatre fois et demie son exposition directe, parce que les 134 autres lignes bougeraient avec elle. L'équipondération protège de l'exposition directe, pas de la contagion. Et ce chiffre est un minorant : les bêtas utilisés viennent d'une période normale, alors que la corrélation monte en crise.

## VII. Deux résultats qui n'étaient dans aucune question

**Le risque du thème vient des puces, et la largeur de l'univers n'y change rien.** Dans `P1` rééquilibré, les vendeurs et l'amont des semi-conducteurs détiennent 45 % de l'argent et portent **77 % du risque**. L'électricité détient 14 % de l'argent et porte **2 % du risque**, avec une amplification de 0,15 : elle n'y contribue pas, elle l'absorbe. L'immobilier et les matières sont dans le même cas.

Élargir l'univers à 134 entreprises sur neuf secteurs a donc dilué le poids sans diluer le risque. En risque, ce portefeuille est un portefeuille de semi-conducteurs accompagné de passagers. Toute conclusion devra le dire dans ces termes.

**La concentration ne s'est pas installée progressivement, elle s'est produite en six ans.** De 2000 à 2019, le plus gros titre de `P1` conservé ne dépasse jamais 8 % et le nombre effectif de lignes reste entre 52 et 78. En 2020 il tombe à 26, et en 2026 à **11,6**, avec Nvidia à 19,4 % et les cinq premières lignes à 52 % du portefeuille. La version rééquilibrée, elle, termine à 106,9 lignes effectives, plus haut qu'en 2000.

Le même univers, la même période, et une opération par an sépare les deux.

## VIII. Ce que les contrôles ont établi

**La conclusion sur le risque résiste à toutes les découpes testées.** Aux deux fréquences, les verdicts de volatilité et de semi-volatilité sont identiques sur les dix portefeuilles. Sur la fenêtre depuis 2004, la volatilité passe même de neuf à dix victoires du rééquilibrage. En retirant les 82 variations extrêmes que l'audit n'a pas pu corroborer, les dix verdicts de volatilité et neuf des dix verdicts de Sharpe restent inchangés, et les niveaux ne bougent que d'un à trois pour cent relatifs.

**La conclusion sur le rendement ne résiste pas.** Elle passe de six à quatre victoires sur dix quand on exclut les années 2000 à 2004. L'avantage de rendement du rééquilibrage repose sur une seule crise, celle de l'éclatement des valeurs technologiques, où la version conservée des acheteurs a perdu 86,2 % contre 68,1 % pour la rééquilibrée.

**L'avantage n'est pas continu.** Sur 284 fenêtres glissantes de trois ans, le rééquilibrage réduit la volatilité dans **64 % des cas seulement**, et l'écart médian ne vaut que 1,3 % sur `P1`. Sur `P6` et `P9`, la version conservée est même la moins volatile dans 61 % et 70 % des fenêtres, alors qu'elle perd sur la période complète. Le bénéfice du rééquilibrage est un bénéfice d'assurance : nul la plupart du temps, considérable quand une ligne s'envole. Les écarts extrêmes atteignent 53 % sur les engagements documentés et 48 % sur les matières, dans les fenêtres contenant l'ascension puis la chute de Texas Pacific Land.

**La réserve sur les acheteurs est levée.** Ce portefeuille ne comptait que quatre entreprises en 2000, et la double lecture décidée à cette occasion montre que son verdict ne change pas : le rééquilibrage y gagne sur les quatre critères, sur la période complète comme depuis le 19 août 2004.

## IX. Ce que je m'interdis de conclure, et qui a été respecté

Les onze interdits posés à la tâche 8 avant tout calcul restent en vigueur, et ce document s'y tient.

Aucune performance n'est présentée comme réalisable. Aucune causalité n'est affirmée : les associations mesurées ne disent pas que l'intelligence artificielle cause ce risque. L'écart entre gestion conservée et rééquilibrée n'est pas baptisé effet de la concentration, puisqu'il contient aussi les opérations et les frais. Aucun prix n'est déclaré validé, 82 variations extrêmes restant non corroborées et neuf divergences entre fournisseurs non arbitrées. Des poids égaux ne signifient pas une exposition égale, les 134 degrés d'exposition étant non quantifiés. Aucune conclusion ne repose sur une seule fréquence, une seule fenêtre ou un seul épisode. Aucun portefeuille n'est déclaré diversifié parce qu'il contient beaucoup de titres. Aucune extrapolation vers l'avenir n'est faite : un risque mesuré est un risque passé.

## X. Les limites propres à cette étape

**Les six épisodes ne sont pas comparables entre eux.** Du sommet au creux, le premier dure 638 séances et le dernier 35 ; jusqu'au retour au sommet, 1 670 et 88. Ils sont traités un par un, sans moyenne, et aucune statistique n'est calculée sur leur ensemble.

**La covariance des tâches 16 à 19 et 27 à 28 est estimée sur les 252 dernières séances.** Les hiérarchies qu'elle produit décrivent l'état au 4 septembre 2026, pas une propriété permanente. La domination de `SNDK` et de `TPL` reflète leur agitation récente.

**Le découpage en maillons est une décision, pas une donnée.** Il vient du champ `canal` de la sélection et du secteur GICS pour départager les fournisseurs. Un autre découpage donnerait d'autres parts de risque. Trois maillons de `P3` ne comptent qu'un seul titre et ne sont donc pas commentés.

**La partition par maturité recoupe une partition sectorielle.** Vingt et une des vingt-quatre entreprises à engagement documenté sont des électriciens ou des énergéticiens, alors que le critère était la maturité de l'exposition et non le secteur. Toute comparaison entre exposition établie et engagement documenté compare donc aussi, sans le dire, des semi-conducteurs à des services aux collectivités.

**Les modèles de volatilité conditionnelle et les lois à queues épaisses ne sont pas employés.** Ils sont au-dessus du standard fixé pour ce projet et deviennent une limite écrite. La VaR historique est donc la seule utilisée, avec son taux de dépassement réel publié à côté.

**Les cinq séries de comparaison n'ont pas de composition.** Les analyses de contribution, de concentration et de maillon portent sur vingt séries de portefeuille et non sur vingt-cinq, parce que la composition ligne à ligne de `SPY` et de `RSP` n'a jamais été collectée.

## XI. Ce que changent le témoin et les tests statistiques

*Ajouté le 28 septembre 2026. Calculs : `src/construire_temoin.py` et `src/robustesse_statistique.ipynb`. Figures : `figures/`.*

**Le groupe témoin.** Les 366 entreprises SORT, soit 368 titres, sont construites avec le même moteur, les mêmes règles d'entrée, le même rééquilibrage de janvier et les mêmes frais que `P1`. Elles partagent avec le thème la composition du S&P 500 de 2026, donc le même biais de survie. `T1` les équipondère ; `T1S` les repondère pour reproduire la répartition sectorielle de `P1`, 35,8 % de technologie, 20,9 % d'industrie, 17,9 % de services aux collectivités, etc. Leurs cours viennent de Yahoo sans seconde source ni correction manuelle ; une séance manquante a été complétée et 38 variations de plus de 50 % en une séance ont été examinées, qui correspondent à des événements réels ou à des scissions déjà compensées par le fournisseur.

| Série, gestion rééquilibrée | Annualisé | Volatilité | Sharpe | Repli maximal | Bêta à `SPY` |
|---|---|---|---|---|---|
| `P1`, thème | 18,70 % | 21,73 % | 0,81 | −51,8 % | 1,05 |
| `T1S`, témoin aux mêmes secteurs | 16,27 % | 19,53 % | 0,77 | −50,4 % | 0,95 |
| `T1`, témoin équipondéré | 16,07 % | 18,86 % | 0,79 | −51,8 % | 0,92 |
| `SPY` | 8,35 % | 19,11 % | | −54,9 % | 1,00 |

Trois conclusions en découlent.

1. **La plus grande partie de la performance n'a rien à voir avec l'IA.** Un portefeuille équipondéré de survivants du S&P 500 fait déjà 16 % par an. Le supplément propre au thème, face à `T1S`, vaut 2,5 points de rendement excédentaire, avec un intervalle à 95 % de −1,0 à +6,1 points : il n'est pas significatif (p = 0,17).
2. **Le thème est plus risqué, et cela est établi.** Sa volatilité dépasse celle de `T1S` de 2,2 points, intervalle de 1,7 à 2,8 points. Même à secteurs égaux, les entreprises du thème bougent davantage.
3. **Le rendement supplémentaire paie à peu près ce risque supplémentaire, sans plus.** L'écart de Sharpe avec `T1S` vaut 0,04, intervalle de −0,13 à +0,20 (p = 0,70).

**Le bootstrap des deux gestions.** Chaque paire de séries est retirée 2 000 fois par blocs d'un trimestre, aux mêmes dates, ce qui conserve à la fois l'agrégation des jours agités et la corrélation entre les deux gestions. La baisse de volatilité due au rééquilibrage est significative sur huit portefeuilles ; `P8` et `P9` sont les exceptions. L'écart de Sharpe n'est significatif que pour `P4`, les acheteurs d'infrastructure, dont la version conservée a porté la chute de 2000-2002. Le « neuf sur dix » de la section III est un décompte de signes, pas une preuve.

**La corrélation de crise corrigée.** La correction de Forbes et Rigobon divise la corrélation de tension par $\sqrt{1+\delta(1-\rho^2)}$, où $\delta = 2{,}73$ est la hausse relative de la variance de `SPY`. Appliquée à la corrélation moyenne entre titres, c'est une approximation. La corrélation corrigée de `P1` vaut 0,241 en tension contre 0,307 au calme. La hausse disparaît dans dix séries sur onze. Cette correction est elle-même discutée : elle suppose que la hausse de variance vient d'un choc commun et non d'une contagion, et tend donc à conclure à l'absence de contagion. Les deux lectures sont écrites ; aucune n'est retenue seule.

**Le plafond de diversification est celui du marché.** Le témoin atteint 3,21 actifs indépendants avec 368 titres, le thème 2,92 avec 135. Le résultat de la section V reste vrai, mais il décrit les grandes entreprises américaines en général, dont le thème est un sous-ensemble un peu plus corrélé.

**Deux réserves qui encadrent cette section.** *Ajoutées le 28 septembre 2026. Calculs : section 4 de `src/robustesse_statistique.ipynb`, sortie `data/processed/temoin_contamination.csv`.*

La première porte sur le témoin lui-même. Il est formé des entreprises que la règle de sélection a écartées, et cette règle a des faux négatifs dont je ne connais pas le nombre : une entreprise réellement exposée aux infrastructures de calcul, mais dont la preuve n'a pas été trouvée dans les passages relus, se trouve dans le témoin. Chaque faux négatif rapproche le témoin du thème. Tous les écarts de cette section entre `P1` et `T1` ou `T1S` sont donc, en principe, des minorants de l'écart entre le thème et un témoin propre. J'ai cherché à mesurer ce biais sur les dossiers qui y sont les plus exposés, les 93 entreprises classées SORT le 8 septembre par la consigne de clôture parce que leur preuve restait insuffisante, dont 71 étaient `A_EXAMINER` et 22 `DOUTEUX`. Leurs titres sont un peu plus corrélés à `P1` que les autres, 0,522 contre 0,491 en médiane. Mais les retirer ne creuse pas l'écart : face au témoin sans eux, `P1` ne garde que 1,95 point de rendement d'avance au lieu de 2,63, et 2,72 points de volatilité au lieu de 2,87. Ce contrôle ne confirme donc pas le sens attendu du biais, sans l'infirmer non plus, puisqu'un faux négatif peut se cacher parmi les 273 autres entreprises. La réserve reste écrite comme une limite non chiffrée. Le même calcul révèle un point que `T1S` cachait : les sept services aux collectivités du témoin font tous partie de ces 93 dossiers fragiles, si bien que la poche de 17,9 % que `T1S` leur donne pour imiter `P1` est entièrement composée d'entreprises dont l'exclusion est la moins assurée.

La seconde porte sur la corrélation de crise. La correction de Forbes et Rigobon est une correction discutée, pas une preuve d'absence de contagion. Elle suppose que toute la hausse de variance du marché vient d'un choc commun exogène ; si une partie de cette hausse venait justement de la contagion entre titres, la correction retirerait ce qu'elle prétend tester. Elle est aussi appliquée ici à une corrélation moyenne alors qu'elle est définie pour une paire, et avec un seul `δ` pour six épisodes de natures différentes. La phrase juste est donc double : la hausse brute de la corrélation en tension est un fait mesuré ; son interprétation comme contagion propre au thème n'est pas établie, et son interprétation comme simple effet du marché ne l'est pas davantage.

**Ce qui résiste.** La concentration du risque dans les puces (figure 3), la concentration qui se forme sans rééquilibrage (figure 4), la baisse de volatilité due au rééquilibrage et le surcroît de volatilité du thème sont confirmés par ces contrôles.
