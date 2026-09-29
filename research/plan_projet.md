# Plan du projet et état d'avancement

*État final de cette version au 8 septembre 2026.*

## I. Règle d'arrêt et avancement

Je déclare une étape close lorsque les livrables demandés existent, que les calculs et leurs dépendances se reproduisent sur le cliché conservé, et que les limites sont écrites. Cette définition s'applique de la même manière aux deux premières étapes. Elle ne signifie pas validation intégrale de chaque prix ou de chaque interprétation.

L'étape 1 est close : les 500 dossiers sont tranchés, 134 ENTRE et 366 SORT, sans dossier en attente. L'étape 2 est close pour les dix groupes et leurs vingt séries construits, sous les limites finies décrites ci-dessous. L'étape 3 est close le 8 septembre 2026 : trente-sept tâches, sept phases, ses résultats dans `research/resultats_risque.md` et ses limites à la section X du même document. Elle a été corrigée le 29 septembre 2026 après un audit indépendant (section VI bis). Les étapes 4 et 5, `P11` et le rapport final, écrits le 28 septembre 2026 sur des décisions déléguées, sont des **brouillons non validés** : ils ont précédé la question de recherche, adoptée le 29 septembre au bloc 3 du Research Charter, et seront refaits.

## II. Les huit phases de l'étape 2

### Phase 0. Décisions avant collecte : close sous les limites écrites

1. **Source de prix et écriture de ses limites** : fait et vérifié sur le cliché final.
2. **Méthode de contrôle par seconde source** : fait et vérifié sur le cliché final.
3. **Traitement des classes d'actions multiples** : fait et vérifié sur le cliché final.

### Phase 1. Collecte : close sous les limites écrites

4. **Correspondance CIK vers symbole** : fait et vérifié sur le cliché final.
5. **Cours quotidiens bruts** : fait et vérifié sur le cliché final.
6. **Cours quotidiens ajustés** : fait et vérifié sur le cliché final.
7. **Dividendes** : fait et vérifié sur le cliché final.
8. **Divisions d'actions** : fait et vérifié sur le cliché final.
9. **Nombre d'actions en circulation** : couverture auxiliaire partielle écrite.
10. **Séries de comparaison** : fait et vérifié sur le cliché final.
11. **Calendrier de bourse** : fait et vérifié sur le cliché final.
12. **Manifeste de collecte** : fait et vérifié sur le cliché final.

### Phase 2. Contrôle des données : close sous les limites écrites

13. **Trous dans les séries et séances absentes** : fait et vérifié sur le cliché final.
14. **Variations quotidiennes aberrantes** : fait et vérifié sur le cliché final.
15. **Cohérence de l'ajustement** : fait et vérifié sur le cliché final.
16. **Vérification contre une seconde source** : seconde source rapprochée, réserves finies écrites.
17. **Cohérence des dates de première cotation** : couverture auxiliaire partielle écrite.
18. **Devise et place de cotation** : fait et vérifié sur le cliché final.
19. **Retraits de cote et changements de symbole** : fait et vérifié sur le cliché final.
20. **Remise du rapport de contrôle intégral** : fait et vérifié sur le cliché final.

### Phase 3. Règles de construction : close sous les limites écrites

21. **Période d'étude** : fait et vérifié sur le cliché final.
22. **Fréquence des rendements** : fait et vérifié sur le cliché final.
23. **Rendement total ou de prix** : fait et vérifié sur le cliché final.
24. **Portefeuilles à construire, donc les poids** : fait et vérifié sur le cliché final.
25. **Nombre de titres du portefeuille concentré** : sans objet dans les dix groupes retenus.
26. **Règle de rééquilibrage** : fait et vérifié sur le cliché final.
27. **Traitement des entreprises récemment cotées** : fait et vérifié sur le cliché final.
28. **Poche de liquidités ou investissement intégral** : fait et vérifié sur le cliché final.
29. **Coûts de transaction** : fait et vérifié sur le cliché final.
30. **Portefeuilles par canal d'exposition** : fait et vérifié sur le cliché final.

### Phase 4. Construction : close sous les limites écrites

31. **Rendements individuels** : fait et vérifié sur le cliché final.
32. **Alignement des dates** : fait et vérifié sur le cliché final.
33. **Traitement des valeurs manquantes** : fait et vérifié sur le cliché final.
34. **Reconstruction des capitalisations** : écartée par décision de l’auteur du 8 septembre 2026 ; aucun portefeuille de cette nature.
35. **Poids cibles aux dates de rééquilibrage** : fait et vérifié sur le cliché final.
36. **Dérive des poids entre rééquilibrages** : fait et vérifié sur le cliché final.
37. **Rendement du portefeuille par période** : fait et vérifié sur le cliché final.
38. **Série de valeur en base 100** : fait et vérifié sur le cliché final.
39. **Entrées et sorties de titres** : fait et vérifié sur le cliché final.
40. **Coûts de transaction** : fait et vérifié sur le cliché final.
41. **Portefeuilles de comparaison** : fait et vérifié sur le cliché final.
42. **Portefeuilles par canal** : fait et vérifié sur le cliché final.

### Phase 5. Contrôle des résultats : close sous les limites écrites

43. **Somme des poids égale à 1** : fait et vérifié sur le cliché final.
44. **Aucun poids négatif ni aberrant** : fait et vérifié sur le cliché final.
45. **Nombre de titres présents par date** : fait et vérifié sur le cliché final.
46. **Plausibilité des rendements cumulés** : fait et vérifié sur le cliché final.
47. **Cohérence de l'agrégation** : fait et vérifié sur le cliché final.
48. **Reconstruction comparée aux indices publiés** : comparaison sous conventions et couverture écrites.

### Phase 6. Tests : close sous les limites écrites

49. **Proposition des cas qui doivent faire échouer le code** : treize cas proposés, trois limites de collecte écrites.
50. **Écriture des tests** : 103 tests passent, dont 48 de l’étape 2.

### Phase 7. Documentation et clôture : close sous les limites écrites

51. **Règles de construction des portefeuilles** : fait et vérifié sur le cliché final.
52. **Écriture des limites** : fait et vérifié sur le cliché final.
53. **Mise à jour des notes** : fait et vérifié sur le cliché final.
54. **Intégration au pipeline** : commande séparée et manifeste vérifié.
55. **Commit** : commit de finition, identifié dans le rapport final.

## III. Résultats définitifs de cette version

| Groupe | Entreprises initiales | Entreprises finales | Titres finaux |
| --- | --- | --- | --- |
| P1 | 90 | 134 | 135 |
| P2 | 69 | 110 | 111 |
| P3 | 21 | 24 | 24 |
| P4 | 4 | 10 | 11 |
| P5 | 19 | 34 | 34 |
| P6 | 21 | 24 | 24 |
| P7 | 20 | 28 | 28 |
| P8 | 3 | 7 | 7 |
| P9 | 8 | 13 | 13 |
| P10 | 15 | 18 | 18 |



Le calcul comporte 6709 niveaux, 6708 rendements, 321 relevés mensuels et 266430 lignes de poids, y compris les poids nuls. Les 38 cours portés restent marqués. L'écart maximal de somme des poids vaut 4.441e-16, celui de l'identité quotidienne 8.969e-16. Les frais se raccordent aux montants échangés sur les vingt séries.

| Série | Base 100 finale | Annualisé | Rotation annuelle | Effet des frais, pb/an | Repli maximal |
| --- | --- | --- | --- | --- | --- |
| P1_reeq | 9 597,07 | 18,70 % | 24,85 % | 2,95 | -51,84 % |
| P1_cons | 9 768,39 | 18,78 % | 4,58 % | 0,54 | -53,31 % |
| P10_reeq | 3 369,26 | 14,13 % | 18,12 % | 2,07 | -57,58 % |
| P10_cons | 4 940,74 | 15,78 % | 2,90 % | 0,34 | -62,33 % |
| P2_reeq | 10 985,89 | 19,31 % | 25,90 % | 3,09 | -55,50 % |
| P2_cons | 10 898,81 | 19,27 % | 4,78 % | 0,57 | -55,54 % |
| P3_reeq | 3 480,21 | 14,27 % | 16,89 % | 1,93 | -45,87 % |
| P3_cons | 3 933,68 | 14,79 % | 3,65 % | 0,42 | -51,91 % |
| P4_reeq | 47 977,33 | 26,10 % | 36,25 % | 4,57 | -70,60 % |
| P4_cons | 5 902,89 | 16,56 % | 7,02 % | 0,82 | -86,53 % |
| P5_reeq | 15 476,45 | 20,85 % | 30,49 % | 3,69 | -72,64 % |
| P5_cons | 25 576,60 | 23,16 % | 4,91 % | 0,60 | -73,08 % |
| P6_reeq | 1 998,84 | 11,91 % | 12,83 % | 1,44 | -45,11 % |
| P6_cons | 1 891,01 | 11,68 % | 4,30 % | 0,48 | -44,84 % |
| P7_reeq | 7 656,17 | 17,70 % | 17,21 % | 2,03 | -54,02 % |
| P7_cons | 7 419,05 | 17,56 % | 3,82 % | 0,45 | -53,75 % |
| P8_reeq | 6 731,43 | 17,13 % | 25,63 % | 3,00 | -64,52 % |
| P8_cons | 2 588,94 | 13,00 % | 8,56 % | 0,97 | -59,65 % |
| P9_reeq | 5 007,99 | 15,84 % | 23,51 % | 2,72 | -72,34 % |
| P9_cons | 2 284,38 | 12,47 % | 4,19 % | 0,47 | -73,13 % |



Les poids maximaux sont ceux des relevés mensuels, pas des maxima certifiés à chaque instant :

| Série | Titre | Date du relevé | Poids maximal relevé |
| --- | --- | --- | --- |
| P10_cons | TPL | 2024-11-29 | 70,91 % |
| P10_reeq | WMB | 2003-10-31 | 17,14 % |
| P1_cons | NVDA | 2025-07-31 | 24,93 % |
| P1_reeq | FSLR | 2007-12-31 | 7,14 % |
| P2_cons | NVDA | 2025-07-31 | 28,72 % |
| P2_reeq | SBAC | 2003-07-31 | 7,84 % |
| P3_cons | TPL | 2024-11-29 | 66,36 % |
| P3_reeq | FSLR | 2007-12-31 | 27,90 % |
| P4_cons | TSLA | 2022-09-30 | 62,02 % |
| P4_reeq | SBAC | 2003-07-31 | 62,56 % |
| P5_cons | NVDA | 2024-11-29 | 61,66 % |
| P5_reeq | NVDA | 2001-12-31 | 18,90 % |
| P6_cons | VST | 2025-07-31 | 19,82 % |
| P6_reeq | VST | 2024-11-29 | 12,03 % |
| P7_cons | GNRC | 2021-10-29 | 21,63 % |
| P7_reeq | PWR | 2000-06-30 | 13,87 % |
| P8_cons | O | 2002-09-30 | 61,02 % |
| P8_reeq | EQIX | 2003-12-31 | 50,87 % |
| P9_cons | FSLR | 2008-07-31 | 61,00 % |
| P9_reeq | FSLR | 2007-12-31 | 53,53 % |



## IV. Limites qui ne rouvrent pas la finition

L'univers est choisi sur les informations récentes de 2026, puis projeté sur le passé. Il comporte un biais de connaissance a posteriori et de survivance. Les résultats décrivent des paniers actuels ; ils ne prouvent ni une stratégie identifiable à l'époque, ni un risque causé par l'IA. La règle III admet des activités générales de la chaîne : centres de données hors IA, semi-conducteurs, énergie, logistique et équipements. Les 134 degrés restent non quantifiés. La maturité distingue une activité établie d'un engagement, sans mesurer leur intensité.

Yahoo est une source secondaire. Close est déjà retraité des divisions, et Adj Close dépend d'ajustements rétroactifs. Le cliché conservé, ses dividendes et ses facteurs sont reproductibles localement ; une nouvelle collecte ne promet pas les mêmes valeurs. Ce ne sont pas des cours historiques totalement non ajustés. Les nombres d'actions SEC ne doivent pas être multipliés par ces cours sans harmoniser dates, classes et divisions.

Le rapprochement Nasdaq porte maintenant sur 64 titres et 155 046 clôtures, soit 154 982 rendements comparables. L'essentiel de cette couverture commence en septembre 2016. Sur les 103 variations extrêmes du brut situées dans un historique admissible, 82 restent non corroborées et 21 concordent en rendement de prix. Les neuf divergences anciennes non arbitrées restent exactement recensées dans `data/review/divergences_finition_2026-09-08.csv`. Les coefficients de scission ne sont pas certifiés. Toute conclusion de risque appuyée sur ces extrêmes devra expliciter cette réserve. Une identité comptable correcte ne certifie pas les prix.

Les dividendes sont des créances assimilées à des espèces au détachement, réinvesties en janvier. Les dates de paiement des actions ne sont pas collectées. L'ancien contrôle SPY situe l'effet du paiement tardif de décembre à environ 0,04 point par an sur ce fonds ; il ne mesure pas l'effet sur le nouvel univers. Les distributions de titres sont réinvesties synthétiquement dans le parent, sans frais propres à la scission. Il n'existe pas de registre exhaustif des opérations sur titres ni de reproduction d'un compte réellement conservé.

Le fichier auxiliaire `premieres_cotations.csv` couvre 79 entreprises et 79 titres parmi les 134 entreprises et 135 titres retenus. Il n'a pas été réécrit. Les métadonnées des nouveaux prix contiennent leur première transaction, ce qui ne certifie pas toutes les anciennes dates d'IPO. Les cas de collecte 11 à 13 restent sans tests d'acquisition importables. Le dernier relevé mensuel est la clôture du 4 septembre 2026, pas une fin de mois. L'étape 2 conserve sa commande séparée de `src/run_pipeline.py`.

La cotation conditionnelle de SNDK au 13 février 2025 reste retenue. L'ancienne sensibilité d'environ 0,29 point par an sur P1 conservé concernait l'univers précédent et n'est pas une mesure du portefeuille actuel. La liquidité et le coût d'une transaction en cotation conditionnelle ne sont pas démontrés. Aucune de ces limites n'est transformée en chantier supplémentaire dans cette finition.

## V. Les décisions de l'auteur

**I. La capitalisation est écartée, décision du 8 septembre 2026.** Aucun portefeuille pondéré par capitalisation n'est ajouté. Les dix portefeuilles conservés permettent déjà d'observer la concentration se former à partir de poids initiaux égaux. Dans les relevés mensuels de la version recalculée, Nvidia atteint 24,93 % de P1 conservé au 2025-07-31. Ce poids résulte de la trajectoire du portefeuille ; il n'a pas été fixé à ce niveau à la constitution. Cette lecture répond à la question retenue, sans prétendre isoler à elle seule l'effet de la concentration sur le risque. Le contraste SPY/RSP reste un repère portant sur le marché entier.

Les nombres instantanés d'actions SEC du cliché commencent le 2009-02-24 et ne couvrent que 54 entreprises en 2009. Cette couverture renforce le refus, mais son coût n'en est pas la seule raison. La comparaison entre gestion conservée et rééquilibrée mêle dérive des poids, opérations et frais ; elle n'est pas un effet causal pur de concentration.

**II. P4 conserve son départ en 2000, décision du 8 septembre 2026.** Le calcul reste établi sur toute la période, sans raccourcir les autres séries. Les premières années conservent l'épisode 2000 à 2002. P4 compte 4 entreprises au départ, 5 à partir du 2002-07-01, 6 à partir du 19 août 2004, 7 à partir du 2010-06-29, 8 à partir du 2012-05-18, 9 à partir du 2012-06-29 et 10 à partir du 2021-04-15.

Toute comparaison de l'étape 3 impliquant P4 doit être rapportée deux fois : sur la période complète et sur la sous-période commençant le 19 août 2004, où il compte au moins six entreprises. Les séries comparées sont alignées dans chacune de ces deux lectures, sans modifier leurs historiques conservés. Si les conclusions concordent, la faiblesse de l'effectif initial ne change pas la conclusion de cette comparaison entre les fenêtres retenues. Cela ne démontre pas un effet nul de l'effectif en général. Sinon, la divergence doit être expliquée, en distinguant l'effectif des différences de période et de composition. Cette obligation est inscrite maintenant ; aucune comparaison de risque n'est produite dans cette mise à jour.

La prochaine étape est l'analyse de risque.

---

## VI. Étape 3 : mesurer le risque, ses sources et son comportement en crise

Sept phases, trente-sept tâches. Les décisions de la phase 0 se ferment avant que la phase 1 produise le moindre chiffre : une option choisie après avoir vu son effet n'est plus une décision, c'est une sélection. Les travaux sont menés dans `src/mesurer_risque.ipynb`.

### Phase 0. Les décisions : close

**Tâche 1, la fréquence de mesure : les deux, systématiquement.** La volatilité annualisée depuis le quotidien dépasse celle annualisée depuis le mensuel de 14 % en médiane sur les vingt-cinq séries, et de 27 % sur `SPY`, 19,11 % contre 15,01 %. La cause est mesurée : l'autocorrélation quotidienne est négative sur les vingt-cinq séries, de −0,01 à −0,10, alors que la multiplication par racine de 252 suppose l'indépendance.

Le rapport n'est pas uniforme, de 0,967 sur `P4` conservé à 1,353 sur `P8` conservé. En quotidien, `P4` conservé paraît 33 % plus volatil que `P8` conservé ; en mensuel, 87 %. **La fréquence ne déplace donc pas seulement le niveau du risque, elle déforme les comparaisons entre portefeuilles**, ce qu'une étude comparative ne peut pas se permettre. Toute mesure sensible à la fréquence est publiée aux deux. Le quotidien reste la base pour les queues de distribution : à 99 %, 6 708 jours donnent 67 observations dans la queue, 320 mois en donnent 3. Deux interdits : ne jamais comparer un chiffre annualisé depuis le quotidien à un chiffre annualisé depuis le mensuel, et ne jamais présenter un écart entre deux portefeuilles sans dire à quelle fréquence il est mesuré.

**Tâche 2, les mesures retenues.** Une mesure entre dans l'étude si elle répond à l'une des six questions de recherche. Neuf sont retenues : volatilité annualisée, semi-volatilité des rendements négatifs, repli maximal avec sa durée et son temps de récupération, asymétrie et aplatissement, VaR historique, perte moyenne au-delà de la VaR, ratio de Sharpe, ratio de Sortino, bêta au marché.

Trois familles sont écartées. La VaR gaussienne sera calculée une fois, à côté de la VaR historique, pour mesurer de combien l'hypothèse de normalité se trompe ; elle ne sera pas utilisée ensuite. Les modèles de volatilité conditionnelle sont au-dessus du standard du projet et deviennent une limite écrite, non un chantier. Les ratios supplémentaires n'ajoutent rien que les neuf ne disent déjà, et chacun ajouté après coup serait une occasion de retenir celui qui flatte. Les neuf mesures sont calculées pour les vingt-cinq séries, à chaque fois.

**Correction de la tâche 2, datée du 8 septembre 2026.** La semi-volatilité y était définie comme l'écart-type des seuls rendements négatifs. C'est une définition courante mais fausse au sens strict : elle ne divise que par le nombre de jours négatifs et surestime donc la dispersion à la baisse. La définition retenue est celle de Sortino, la racine de la moyenne des carrés des écarts sous le seuil calculée sur toutes les observations, les jours au-dessus du seuil comptant zéro. Le seuil est le taux sans risque, pour rester cohérent avec le numérateur du ratio.

L'écart entre les deux conventions vaut 3 à 12 % selon la série, et il n'est pas uniforme : le rapport va de 0,879 sur `RSP` à 0,972 sur `P5` rééquilibré. Changer de convention déplace donc le classement entre portefeuilles, comme le fait le changement de fréquence. La correction est faite avant tout usage du ratio de Sortino dans une conclusion.

**Tâche 3, les fenêtres d'estimation : trois lectures.** La période complète donne un chiffre de référence comparable entre séries. La fenêtre glissante de 252 séances donne l'évolution, et c'est elle qui montrera si le risque a monté à mesure que la concentration se formait. La fenêtre de 756 séances sert de contrôle de robustesse, tâche 31.

La mesure justifie ce découpage. Sur `P1` rééquilibré, la volatilité de période complète vaut 21,73 %, tandis que la glissante sur 252 séances va de 8,91 % à 47,37 %, avec une médiane de 17,53 %. Un rapport de un à cinq, alors que l'erreur relative d'estimation ne vaut que 4,45 % sur 252 observations et 2,57 % sur 756 : **la variation est du signal, pas du bruit**. Le chiffre de période complète est par ailleurs supérieur à la médiane glissante, parce qu'il est tiré vers le haut par les crises. Tout chiffre de période complète est donc publié à côté de la médiane glissante. Les fenêtres glissantes de `RSP` et de `^SPXEW`, qui commencent en 2003 et 2006, couvrent moins de terrain ; les comparaisons glissantes les impliquant sont restreintes à la période commune et le disent.

**Tâche 4, la définition d'un épisode de tension.** Un épisode est un repli de `SPY` d'au moins 15 % depuis son plus haut ; il commence au sommet et finit au creux. La date de retour au sommet est enregistrée séparément et sert au temps de récupération, sans faire partie de l'épisode. Aucune date n'est écrite à la main : la règle s'applique mécaniquement à n'importe quelle série. Elle reste rétrospective : le creux d'un épisode n'est connu qu'une fois le retour au sommet observé. Tous les portefeuilles sont évalués sur les mêmes épisodes, faute de quoi chacun serait jugé pendant ses pires moments à lui.

Six épisodes en résultent, du 24 mars 2000 au 9 octobre 2002 pour −47,3 %, du 9 octobre 2007 au 9 mars 2009 pour −54,9 %, du 20 septembre au 24 décembre 2018 pour −19,1 %, du 19 février au 23 mars 2020 pour −33,7 %, du 3 janvier au 12 octobre 2022 pour −24,4 %, et du 19 février au 8 avril 2025 pour −18,7 %. Quatre dépassent 20 % et sont marqués majeurs. Mille trois cent quinze séances sont en tension sur 6 709, soit 19,6 % ; le reste est la période calme, ce qui laisse assez d'observations des deux côtés pour la tâche 22. Les épisodes sont enregistrés dans `data/processed/episodes_tension.csv`.

Le seuil de 15 % est retenu parce que 20 % ne laisserait que quatre observations et que 10 % ajouterait des reculs de treize jours qu'aucun détenteur n'appellerait une crise. Les deux listes étant mécaniques, en publier deux n'est pas un choix opportuniste. **Ces six épisodes ne sont pas comparables entre eux** : du sommet au creux, 638 séances pour le premier et 35 pour le dernier ; 1 670 et 88 en comptant jusqu'au retour au sommet. Ils seront traités un par un, avec leur durée affichée, sans moyenne. Le premier commence quand `P4` ne compte que quatre entreprises, ce qui rend la double lecture de `P4` prioritaire à cet endroit.

**Tâche 5, l'annualisation.** Les rendements sont annualisés géométriquement, à partir de la valeur finale. La moyenne arithmétique multipliée par 252 s'écarte de 0,82 point par an sur `P1` rééquilibré, 1,50 sur `SPY` et 3,71 sur `P5` conservé. L'écart croît avec la volatilité, approximativement comme la moitié de la variance : **la convention arithmétique flatterait systématiquement les portefeuilles les plus volatils, c'est à dire précisément ceux que l'étude examine**.

Les volatilités sont annualisées par racine de 252 en quotidien et racine de 12 en mensuel. Une exception assumée : le ratio de Sharpe utilise par définition la moyenne arithmétique des rendements excédentaires ; c'est correct pour un rapport, mais son numérateur ne sera jamais présenté comme un rendement. Les années sont comptées en séances divisées par 252, alors que la période contient 251,56 séances par année calendaire ; l'écart de 0,17 % relatif est écrit plutôt que passé sous silence.

**Tâche 6, le taux sans risque.** `^IRX`, le bon du Trésor à treize semaines, collecté dans `data/raw/taux_sans_risque.csv` et inscrit au manifeste avec son empreinte. Il couvre la période avec une moyenne de 1,92 %, un minimum de −0,10 % et un maximum de 6,22 %. Un taux constant serait faux : il valait 6 % en 2000, près de zéro de 2009 à 2015, plus de 5 % en 2023. Les sept cotations négatives de mars 2020 sont réelles et conservées. Cinq séances absentes de la source sont reportées de la veille, ce qui est légitime pour un niveau de taux et ne l'aurait pas été pour un prix.

**Tâche 7, le niveau de confiance de la VaR.** Quatre-vingt-quinze et quatre-vingt-dix-neuf pour cent, tous deux en quotidien. Le premier est le chiffre de comparaison, avec 335 observations dans la queue ; le second décrit la queue avec 67 observations et sa fragilité annoncée. En mensuel, 95 % seulement et à titre indicatif, ses 16 observations étant peu, tandis que 99 % n'en laisserait que 3 et ne sera pas calculé. La VaR est toujours accompagnée de la perte moyenne au-delà : seule, elle dit où commence le danger sans dire ce qu'on y trouve. Elle est exprimée en perte positive.

**Tâche 8, ce que je m'interdis de conclure.** Aucune performance présentée comme réalisable, l'univers étant établi en 2026 et appliqué depuis 2000. Aucune causalité : je mesure des associations, sans contrefactuel. L'écart entre gestion conservée et rééquilibrée n'est pas baptisé effet de la concentration, puisqu'il contient aussi les opérations et les frais. Aucun prix déclaré validé, quatre-vingt-deux variations extrêmes restant non corroborées et neuf divergences non arbitrées. Des poids égaux ne signifient pas une exposition égale, les degrés étant non quantifiés. Aucune conclusion tirée d'une seule fréquence, d'une seule fenêtre ou d'un seul épisode. Aucun portefeuille déclaré diversifié parce qu'il contient beaucoup de titres, ce que les tâches 15 et 18 doivent établir. Aucune extrapolation vers l'avenir. Aucune comparaison entre un chiffre annualisé depuis le quotidien et un depuis le mensuel, ni aucune moyenne arithmétique présentée comme un rendement. Aucune mesure ajoutée ni décision de phase 0 révisée après un résultat sans que ce soit daté et motivé ici.

Leur contrepartie positive : je peux dire combien de risque ces portefeuilles ont porté, d'où il venait en séparant l'effet du nombre de titres de celui de leur mouvement commun, comment ils se sont comportés pendant six épisodes identifiés mécaniquement, et comment ils se comparent au marché sur les mêmes dates.

### Phase 1. Le risque de base : close

Tâche 9, volatilité annualisée par série et par fenêtre. Tâche 10, forme de la distribution, asymétrie, aplatissement et écart à la loi normale. Tâche 11, replis maximaux, durée et temps de récupération. Tâche 12, ratios de Sharpe et de Sortino. Tâche 13, comparaison avec `SPY` et `RSP`.

### Phase 2. D'où vient le risque : close

Tâche 14, corrélation moyenne dans chaque portefeuille. Tâche 15, décomposition de la volatilité en une part due au nombre de titres et une part due à leur corrélation. Tâche 16, contribution de chaque titre au risque total. Tâche 17, concentration des poids contre concentration du risque. Tâche 18, analyse en composantes principales. Tâche 19, décomposition par maillon de chaîne.

### Phase 3. Le comportement en crise : close

Tâche 20, identification des épisodes selon la règle de la tâche 4. Tâche 21, rendement et volatilité par épisode. Tâche 22, corrélations en tension contre corrélations en période calme. Tâche 23, bêta conditionnel à la hausse et à la baisse. Tâche 24, VaR historique et perte moyenne au-delà. Tâche 25, tests de dépassement.

### Phase 4. Le risque de concentration : close

Tâche 26, évolution du poids maximal et de l'indice de concentration. Tâche 27, risque marginal du plus gros titre. Tâche 28, choc simulé sur ce titre. Tâche 29, gestion conservée contre rééquilibrée sur le risque et non sur le rendement.

### Phase 5. Les contrôles : close

Tâche 30, robustesse à la fréquence. Tâche 31, robustesse à la fenêtre. Tâche 32, robustesse à la période, avec la double lecture de `P4`. Tâche 33, sensibilité aux quatre-vingt-deux variations extrêmes non corroborées, imposée par la réserve de l'audit. Tâche 34, tests unitaires des fonctions de risque.

### Phase 6. Documentation et clôture : en cours, résultats et limites écrits

Tâche 35, écriture des résultats : faite, `research/resultats_risque.md`. Tâche 36, écriture des limites : faite, section X du même document. Tâche 37, commit : à faire.

**Ce que l'étape 3 établit.** Le portefeuille du thème est 1,14 fois plus volatil que le marché, 21,73 % contre 19,11 %, et ses maillons vont de 0,97 à 1,84 fois le marché : le thème n'est pas un bloc. Sa distribution n'est normale sur aucune des vingt-cinq séries, ce qui fait sous-estimer une VaR gaussienne de 13 % à 21,5 %.

La diversification par le nombre est épuisée. Avec une corrélation moyenne de 0,338, les 135 lignes de `P1` réduisent le risque autant que 2,92 titres indépendants, et il ne reste que seize centièmes de point de volatilité à gagner en ajoutant des entreprises. L'analyse en composantes principales confirme par une autre voie, le premier facteur expliquant 27,6 % de la variance.

Le risque du thème vient des vendeurs à la chaîne : `P5` détient 35 % de l'argent de `P1` et porte 62 % du risque ; avec les fournisseurs technologiques de `P9`, 45 % de l'argent et 77 % du risque. L'électricité en détient 14 % et en porte 2 %. Élargir l'univers a dilué le poids sans diluer le risque. *Corrigé le 29 septembre 2026 : ces groupes étaient appelés « semi-conducteurs », alors qu'ils en débordent largement (section VI bis).*

La concentration s'est formée en six ans et non en vingt-six : le nombre effectif de lignes de `P1` conservé passe de 78 en 2000 à 54 en 2019, puis à 11,6 en 2026. La version rééquilibrée termine à 106,9.

En période de tension, la corrélation interne brute monte dans les dix portefeuilles sans exception et `P1` perd un tiers de sa diversification effective ; corrigée de la hausse de variance du marché, cette hausse disparaît dans dix séries sur onze (section XI des résultats). La VaR à 99 % est dépassée 1,4 à 1,8 fois trop souvent, et le test de Kupiec la rejette sur les vingt-cinq séries, `SPY` compris.

**L'arbitrage de gestion.** Le rendement brut ne tranche pas, six victoires sur dix, et ce compte tombe à quatre en excluant les années 2000 à 2004. Les mesures de risque tranchent toutes dans le même sens, sept à dix victoires sur dix, dont dix sur dix pour la perte moyenne au-delà de la VaR. La formulation retenue est que le rééquilibrage réduit le risque sur huit portefeuilles aux deux fréquences, que `P5` fait exception et que `P6` est indécidable. L'avantage n'est pas continu : il n'apparaît que dans 64 % des fenêtres glissantes de trois ans, et se concentre dans les épisodes où une ligne prend une place démesurée.

**Ce que les contrôles ont montré.** Les verdicts de volatilité sont identiques aux deux fréquences sur les dix portefeuilles, et le retrait des 82 variations extrêmes non corroborées par l'audit n'en change aucun. La réserve sur l'effectif initial de `P4` est levée. En revanche la conclusion sur le rendement dépend de l'inclusion de 2000 à 2004, ce qui justifie rétrospectivement la décision de la tâche 21 de commencer en 2000.

**Les fonctions de mesure** vivent dans `src/risque.py` et sont couvertes par trente-sept cas dans `tests/test_risque.py`.

**Corrections du 28 septembre 2026.** `src/mesurer_risque.ipynb` redéfinissait ses propres fonctions au lieu d'appeler `src/risque.py` : les tests portaient sur un code qui ne produisait pas les chiffres publiés. Le notebook appelle désormais le module testé, et sa réexécution redonne les mêmes sorties, à une exception près. La part du temps passée sous le plus haut utilise le seuil du module, un repli strictement négatif, au lieu d'un repli de plus de 0,01 % ; elle augmente d'au plus 0,34 point et reste comprise entre 86 % et 94 %. La ligne `SPXEW` de `risque_beta_conditionnel.csv` change aussi : le fichier avait été produit avec pandas 2, qui comblait les séances absentes avant de calculer un rendement, alors que la référence déclarée est pandas 3, qui ne le fait plus. Le bêta de `SPXEW` passe de 1,038 à 1,033 ; aucun chiffre du rapport n'en dépend.

Le fichier des épisodes distinguait mal deux durées. La colonne `seances` compte du sommet à la veille du retour au sommet ; la nouvelle colonne `seances_repli` compte du sommet au creux, c'est-à-dire la période de tension, et sa somme donne les 1 315 séances. L'ancien test affirmant que la règle ne regarde pas l'avenir était faux en général : il est remplacé par un test montrant que le creux n'est connu qu'après coup, et par un test des deux durées.

**Ajouts du 28 septembre 2026, après une relecture critique.** Cinq faiblesses ont été relevées et traitées.

1. *Reproductibilité.* Les empreintes de l'étape 2 avaient été calculées sous Windows, sur des fichiers à fins de ligne CRLF ; Git les rend en LF sur les autres systèmes, et `--check-only` échouait sur les 140 fichiers de prix. `src/empreintes.py` vérifie désormais les empreintes aux fins de ligne près. Le manifeste de l'étape 2 était aussi périmé : `prix_manifest.json`, `decisions_selection.csv` et `controle_prix.py` avaient changé après sa production du 8 septembre. L'étape 2 a été reconstruite : ses sorties sont identiques à 10⁻¹² près, et le manifeste a été régénéré. Le manifeste de l'étape 1, `data/processed/pipeline_manifest.json`, est lui aussi périmé : neuf de ses entrées et sorties ont changé depuis sa production, dont `decisions_selection.csv` et `univers_retenu.csv`. Il n'a pas été rafistolé, car sa reconstruction exige le corpus local de 2,5 Go ; il faut relancer `python -B src/run_pipeline.py` sur la machine qui détient ce corpus. *Fait le 29 septembre 2026, section VI bis.*
2. *Groupe témoin.* Les 366 entreprises SORT sont collectées (`src/collecter_temoin.py`) et construites avec le même moteur (`src/construire_temoin.py`), en version équipondérée et en version aux parts sectorielles de `P1`. La boucle de simulation de l'étape 2 a été extraite dans `simuler_groupe` pour être partagée ; la reconstruction de l'étape 2 est identique octet pour octet.
3. *Significativité.* Un bootstrap circulaire par blocs d'un trimestre éprouve les écarts entre gestions et entre thème et témoin.
4. *Corrélation de crise.* La correction de Forbes et Rigobon est appliquée et discutée.
5. *Présentation.* Six figures sont produites par `src/figures.ipynb` ; les blocs 2 et 3 du Research Charter sont proposés et restent à valider.

Les résultats et ce qu'ils changent sont dans la section XI de `research/resultats_risque.md`. La suite complète compte désormais 146 tests.
 Les hypothèses testables, les fenêtres communes et le traitement explicite des extrêmes non corroborés devront y être posés avant de conclure. Cette étape n'est pas réalisée par le présent document.

## VI bis. Corrections du 29 septembre 2026, après un audit indépendant

Un audit de la version `3a2affb` a relevé dix-huit problèmes. Ceux qui touchent les étapes 1 à 3 sont corrigés ici. Ceux qui touchent les étapes 4 et 5, `P11` et le rapport final ne le sont pas : ces documents sont déclarés brouillons non validés et seront refaits, et chacun de leurs problèmes deviendra une règle de la nouvelle version. Ceux qui demandent un choix de méthode attendent la revue de littérature.

**Le code de l'étape 3.**

1. `annualiser_rendement` divisait l'exposant par le nombre de niveaux au lieu du nombre de rendements. Sur `P1` rééquilibré, 18,70037 % devient 18,70340 %. Aucun verdict ne change ; l'écart le plus grand vaut 0,004 point.
2. `rho_implicite` acceptait des titres absents une partie de la période, alors que son identité suppose tous les titres observés aux mêmes dates : deux séries parfaitement corrélées pouvaient sortir à 0,4. La fonction refuse désormais un bloc incomplet, et le carnet ne garde que les titres observés sur toute la fenêtre. Sur toute la période, la corrélation implicite des 90 titres complets vaut 0,339, contre 0,313 avec l'ancien mélange. En fenêtre glissante, la médiane passe de 0,299 à 0,303, et les pics restent ceux de 2009, 2012 et 2020. La moyenne par paires, 0,338, et les 2,92 actifs indépendants ne changent pas : ils ne passaient pas par cette fonction.
3. `n_effectif` écrit ses hypothèses : poids égaux, volatilités égales, corrélation uniforme. C'est un ordre de grandeur.
4. L'analyse en composantes principales citée dans les résultats n'avait aucun code dans le dépôt. Sa cellule est ajoutée ; elle reproduit les chiffres publiés sur les 756 dernières séances, et les donne pour les dix portefeuilles dans `risque_composantes.csv`.
5. Le bootstrap des gestions lit `P4` deux fois, sur la période complète et depuis le 19 août 2004, comme sa règle l'exige. Les deux lectures concordent.

**Les noms et les phrases.** `P5` et `P9` étaient appelés « puces » ou « semi-conducteurs ». `P5` rassemble le canal de vente à la chaîne, qui mêle semi-conducteurs, réseau, stockage, serveurs, IBM, Ecolab et Dow ; `P9` des fournisseurs technologiques, dont Accenture et First Solar. Ils portent désormais leur nom exact, et un vrai périmètre des semi-conducteurs reste une décision à prendre. L'écart entre le thème et le témoin n'est plus présenté comme une mesure du biais de survie, ni comme libéré des secteurs : les parts sectorielles de `T1S` sont celles de 2026, fixes, alors que `P1` évolue. Le scénario de choc n'est plus présenté comme un minorant.

**Les chiffres faux trouvés en vérifiant le texte contre les fichiers.** `SPY` rapporte 8,27 % par an et non 8,35 %. Les portefeuilles vont de 11,7 % à 26,1 % et non de 11,0 % à 21,7 %. Les résultats de l'électricité par épisode mélangeaient ses deux versions. Le plus gros titre de `P1` conservé a atteint 9,7 % avant 2020. L'écart médian de volatilité sur `P1` vaut 1,2 % et non 1,3 %. Il restait seize centièmes de point de volatilité à gagner par la diversification, et non quarante-deux. La section I des résultats inversait le décompte du rendement entre les deux gestions. Tous sont corrigés dans `research/resultats_risque.md`, dont l'encadré du 29 septembre donne la liste.

**La reproductibilité.**

1. Le dépôt fixe une seule convention de fins de ligne, LF, dans l'index comme dans la copie de travail (`.gitattributes`). `empreinte` calcule celle d'un fichier texte sur son contenu en LF. Les tests du corpus comparent le contenu aux fins de ligne près, et la suite passe désormais aussi sous Windows.
2. Le manifeste de l'étape 1 portait sept empreintes qui ne correspondaient à aucune version des fichiers. L'étape 1 a été reconstruite dans un dossier temporaire à partir du corpus local : ses onze sorties sont identiques, au contenu près, à celles du dépôt. Le manifeste a ensuite été régénéré par cette reconstruction. `classification_manuelle.py` et `controle_qualite.py` vérifient et écrivent leurs empreintes sous la même convention.
3. Chaque partie de l'étape 3 vérifie les empreintes de ce qu'elle lit avant de calculer, et écrit un manifeste de ses entrées, de son code et de ses sorties : `risque_manifest.json`, `temoin_manifest.json`, `robustesse_manifest.json`. Les figures vérifient les trois. GitHub refait ces vérifications à chaque envoi.

La suite compte 169 tests, dont 37 pour `src/risque.py`.

**Ce qui attend la revue de littérature, et pourquoi.** Reconstruire `T1S` avec des parts sectorielles qui suivent `P1` dans le temps suppose de choisir la neutralisation voulue. Mesurer réellement le biais de survie suppose des compositions historiques de l'indice. Définir un périmètre des semi-conducteurs, graduer l'intensité de l'exposition et former des sous-univers selon la solidité des preuves sont des choix de méthode. Plusieurs scénarios de choc relèvent des tests de résistance. La vérification ciblée des prix extrêmes portera sur les observations qui pèsent sur les conclusions, une fois celles-ci fixées.

---

## VII. Étape 4 : couverture et diversification par des actifs extérieurs au thème

> **Brouillon non validé, 29 septembre 2026.** Cette étape a été conçue avant la question de recherche et sur des décisions déléguées. Un audit y a relevé un calendrier des options qui dépend de la fin du fichier, des durées d'options incohérentes avec la convention du `VIX`, et un calibrage des puts qui ne permet pas d'isoler une erreur de prix. Elle sera refaite ; ses chiffres ne doivent pas être cités.

*Phase 0 écrite le 28 septembre 2026, avant la collecte des instruments et avant tout calcul de stratégie. L'auteur m'a délégué ces décisions pour ce tour de travail ; chacune est une proposition qu'il pourra renverser à sa relecture, et chaque renversement devra être daté ici. Les calculs seront menés dans `src/couvrir_diversifier.ipynb`, les fonctions dans `src/couverture.py`, leurs cas de contrôle dans `tests/test_couverture.py`.*

Le point de départ est fixé par l'étape 3. La diversification par le nombre est épuisée : les 135 lignes de `P1` valent environ trois actifs indépendants, et le témoin de 368 titres n'en vaut que 3,2. Ajouter des entreprises, du thème ou du reste de l'indice, ne peut presque plus rien retirer. Tout gain doit donc venir d'actifs dont les rendements ne suivent pas ceux des actions, ou d'instruments qui transfèrent une partie de la perte à quelqu'un d'autre contre paiement.

### Phase 0. Les décisions : close avant calcul

**Tâche 1, les séries traitées : les vingt, avec deux lectures principales.** Chaque stratégie est appliquée aux vingt séries de l'étape 2, parce qu'une stratégie qui ne marche que sur `P1` ne dit rien du thème. La lecture principale porte sur `P1` rééquilibré, le thermomètre de l'étape 3, et sur `P1` conservé, qui est le portefeuille réellement concentré, avec Nvidia au quart de sa valeur en 2025. Le témoin `T1` rééquilibré reçoit les mêmes stratégies, pour savoir si un effet est propre au thème. `P4` est lu deux fois, sur la période complète et depuis le 19 août 2004, comme l'impose la décision du 8 septembre.

**Tâche 2, les instruments candidats.** Quatre familles sont retenues, et chacune a un rôle précis.

1. *Les liquidités*, au taux du bon du Trésor à treize semaines déjà collecté. Ce n'est pas une diversification, c'est une réduction d'exposition. Elle sert d'étalon : un actif ne mérite le nom de diversifiant que s'il fait mieux que les liquidités à part égale. Sans cette comparaison, une baisse de risque obtenue en vendant des actions serait attribuée à l'actif acheté.
2. *Les obligations du Trésor américain à échéance intermédiaire*, par le fonds Vanguard Intermediate-Term Treasury, symbole `VFITX`, dont la valeur liquidative ajustée des distributions couvre toute la période depuis 1991. Les frais du fonds sont déjà déduits de sa valeur. Je retiens un fonds et non un ETF parce que les ETF du Trésor, `IEF` et `TLT`, ne commencent qu'en juillet 2002 et amputeraient l'épisode 2000 à 2002, le plus long de l'étude. Je retiens le Trésor et non les obligations d'entreprises parce qu'une obligation d'entreprise porte un risque de crédit qui monte précisément quand les actions baissent : elle mêlerait deux effets.
3. *Les obligations du Trésor longues*, par `VUSTX`, depuis 1986, en variante de duration. Plus sensibles aux taux, elles amortissent davantage une baisse des taux en crise et souffrent davantage d'une hausse. La comparaison des deux échéances répond à la question de la duration sans en faire un paramètre libre.
4. *Les actions hors du thème*, par le témoin `T1` rééquilibré. Ce n'est pas un actif extérieur aux actions, et c'est volontaire : la question que tout lecteur posera est de savoir si l'on se protège du thème en achetant le reste du marché. La réserve écrite à la section XI de `research/resultats_risque.md` s'applique : le témoin contient des faux négatifs de la sélection.

Pour la couverture, deux instruments sur l'indice S&P 500, parce que c'est le seul sous-jacent pour lequel je dispose, sur toute la période et dans une source reproductible, d'une mesure de volatilité implicite, le `VIX`.

5. *La vente de contrats à terme sur le S&P 500*, couverture linéaire. Je la modélise par le rendement de `SPY` diminué du taux sans risque, qui est le rendement d'un contrat à terme sous la relation de portage, à l'écart de base près. Le nominal vendu vaut le bêta de la série sur `SPY`, estimé sur les 252 séances précédentes et arrêté la veille de chaque fin de mois, de sorte qu'aucune information future n'entre dans la couverture. Le nominal reste fixe en dollars pendant le mois.
6. *L'achat d'options de vente sur le S&P 500*, couverture non linéaire, dite protection par put. Chaque fin de mois, j'achète des puts à un mois sur un nominal égal au même bêta estimé multiplié par la valeur du portefeuille ; la prime est financée en vendant des actions du portefeuille, et la valeur à l'échéance y est réinvestie. Je n'ai pas de prix de marché des options sur vingt-six ans. Les puts sont donc évalués par la formule de Black et Scholes, avec le cours de clôture de `^GSPC`, le taux du bon du Trésor, le rendement des dividendes de `SPY` sur les douze mois précédents, et une volatilité égale au `VIX` du jour augmentée de trois points. Le `VIX` mesure une volatilité à trente jours proche de la monnaie ; un put à 90 % du cours se traite plus cher, c'est la pente du smile, et trois points est l'ordre de grandeur que je retiens sans l'avoir mesuré. Les variantes à zéro et six points encadrent ce choix. L'option est revalorisée chaque jour avec le `VIX` du jour et la durée restante, et vaut sa valeur intrinsèque à l'échéance.

**Instruments écartés, avec leur motif.** L'or : aucune série investissable de rendement total ne couvre la période dans ma source, `GLD` commençant en novembre 2004 ; le mesurer sur une période plus courte le rendrait incomparable aux autres. Les options sur un indice de semi-conducteurs ou la vente d'un fonds de semi-conducteurs : elles viseraient bien la source du risque identifiée à l'étape 3, soixante-dix-sept pour cent dans les puces, mais vendre les puces revient à supprimer l'exposition que l'investisseur voulait garder, et je n'ai pas de volatilité implicite historique pour les évaluer. Les options sur le `VIX` et les tunnels d'options : ils ajoutent des paramètres, donc des occasions de choisir après coup, sans répondre à une question que les deux couvertures retenues laissent ouverte. Les obligations d'entreprises : motif donné plus haut. Ces exclusions deviennent des limites écrites.

**Tâche 3, la taille.** Une grille fixée maintenant et qui ne bougera pas. Pour les liquidités, les deux échéances d'obligations et les actions hors thème : 80 % de la série et 20 % de l'autre actif, puis 60 % et 40 %. Ce sont les deux proportions du contexte maître ; je n'en cherche pas une optimale, car une proportion optimisée sur l'échantillon est un résultat de l'échantillon. Pour les contrats à terme : couverture de la moitié du bêta, puis du bêta entier. Pour les puts : prix d'exercice à 90 % du cours, puis à 95 %, sur le bêta entier. Cela fait douze stratégies par série, plus la série non couverte, soit treize lignes.

**Tâche 4, la gestion des mélanges.** Les mélanges à deux actifs sont ramenés à leurs proportions cibles à la première séance de chaque année, comme les portefeuilles de l'étape 2, et dérivent entre deux dates. Un rééquilibrage mensuel aurait l'air plus soigné, mais il changerait la règle de gestion entre les étapes, et l'écart entre les deux gestions de l'étape 3 montre que cette règle pèse sur le risque.

**Tâche 5, la période.** Du 3 janvier 2000 au 4 septembre 2026, le même calendrier que l'étape 2. Tous les instruments retenus la couvrent. Les nouvelles séries sont coupées à la dernière séance du cliché, même si la source va plus loin, pour que tous les résultats décrivent la même fenêtre. Deux sous-périodes sont fixées avant de regarder : jusqu'au 31 décembre 2021 et à partir du 1er janvier 2022. Ce découpage n'est pas tiré des données de cette étude. Il vient du rapport du FMI d'avril 2026, vérifié sur document primaire, qui décrit une érosion de la relation de couverture entre actions et obligations sur la période qui suit la pandémie. La seconde sous-période ne compte que 4,7 ans, et sera lue comme telle. Les six épisodes de tension de l'étape 3 sont repris un par un.

**Tâche 6, les coûts.** Les échanges de mélanges paient 10 points de base du montant échangé, le taux de l'étape 2, y compris sur le fonds obligataire, pour lequel c'est une hypothèse prudente. Les contrats à terme paient 2 points de base du nominal échangé à chaque révision mensuelle, et le nominal entier est réputé fermé et rouvert aux fins de mars, juin, septembre et décembre, pour tenir compte du renouvellement des échéances. Les puts paient la prime de modèle augmentée de 5 % de cette prime, pour la fourchette d'achat ; la variante à 10 % encadre ce choix. Aucune fiscalité n'est modélisée. Je publierai séparément le coût explicite, frais et primes nettes de ce qu'elles rapportent, et le coût d'opportunité, le rendement abandonné.

**Tâche 7, les mesures.** Les neuf mesures de l'étape 3, aux mêmes conventions, pour chaque stratégie et chaque série, la volatilité aux deux fréquences. Trois mesures s'ajoutent parce qu'elles répondent directement à la question de l'étape. Le rendement annualisé abandonné face à la série non couverte. La corrélation entre la série et l'actif ajouté, au calme et en tension, et sur les deux sous-périodes. Le résultat par épisode de tension. La significativité des écarts de volatilité et de Sharpe entre chaque stratégie et la série non couverte est éprouvée par le bootstrap par blocs d'un trimestre de l'étape 3, aux mêmes dates, 2 000 tirages.

**Tâche 8, les hypothèses et ce qui les contredirait.** J'écris trois attentes avant de regarder, pour pouvoir constater qu'elles sont fausses.

1. À part égale, les obligations du Trésor réduisent davantage le risque que les liquidités sur la période qui s'arrête en 2021, et non depuis 2022. Serait une contradiction : une volatilité ou une perte au-delà de la VaR du mélange obligataire supérieure à celle du mélange de liquidités avant 2022, ou inférieure depuis 2022.
2. Les actions hors du thème réduisent peu le risque. Serait une contradiction : une baisse de volatilité du mélange 60 % et 40 % supérieure à celle du mélange de liquidités de même proportion.
3. La couverture par l'indice retire le risque de marché et laisse le risque propre du thème, si bien qu'elle protège mal dans l'épisode 2000 à 2002, où le thème est tombé plus que le marché. Serait une contradiction : une perte de `P1` couvert en 2000 à 2002 inférieure à la moitié de celle de `P1` non couvert.

**Tâche 9, ce que je m'interdis de conclure.** Aucun prix d'option n'est présenté comme un prix de marché : ce sont des prix de modèle, qui sous-estiment probablement le coût réel des puts hors de la monnaie. Aucune stratégie n'est recommandée à un investisseur. Aucune stratégie n'est déclarée meilleure qu'une autre sur la seule période complète, sans les deux sous-périodes et les épisodes. Aucune couverture par l'indice n'est présentée comme couvrant le thème. Aucune baisse de risque n'est attribuée aux obligations sans la comparaison avec les liquidités à part égale. Aucune corrélation entre actions et obligations n'est extrapolée à l'avenir. Aucune proportion, aucun prix d'exercice, aucune pente de volatilité n'est changé après un résultat sans datation ici. Les interdits de la tâche 8 de l'étape 3 restent en vigueur : aucun rendement n'est réalisable, l'univers étant connu de 2026.

### Phases suivantes

Phase 1, collecte de `VFITX`, `VUSTX` et `^VIX` dans `data/raw/couverture/`, avec leur manifeste et leurs empreintes, par `python -m src.collecter_couverture`. Phase 2, construction des douze stratégies sur les vingt séries et le témoin. Phase 3, mesure. Phase 4, contrôles : identités comptables des mélanges, parité et bornes des prix d'option, absence d'information future dans le bêta, sensibilité à la pente de volatilité et aux coûts. Phase 5, tests. Phase 6, écriture des résultats dans `research/resultats_couverture.md`.

## VIII. Étape 5 : comparaison des stratégies, coûts et risque résiduel

> **Brouillon non validé, 29 septembre 2026.** Un audit y a relevé que la valeur ajoutée publiée compare des rendements géométriques alors que le bootstrap teste des moyennes quotidiennes, que le poids du mélange de référence est estimé une fois et tenu fixe dans les tirages, et que cinq cents comparaisons sont faites sans correction pour leur nombre. Elle sera refaite ; ses chiffres ne doivent pas être cités.

*Critères écrits le 28 septembre 2026, avec la phase 0 de l'étape 4, donc avant tout résultat de couverture. Même statut de proposition renversable.*

**Tâche 1, le critère de comparaison : à risque égal.** Comparer les rendements de stratégies de risques différents ne dit rien : une stratégie moins risquée rapporte presque toujours moins. Pour chaque stratégie, je construis le mélange de la série non couverte et de liquidités qui atteint exactement la même volatilité quotidienne sur la période complète, puis la même perte moyenne au-delà de la VaR à 99 %. L'écart de rendement annualisé entre la stratégie et ce mélange est sa valeur ajoutée à risque égal. Une stratégie qui réduit le risque sans valeur ajoutée positive ne fait rien que la vente d'actions ne fasse aussi bien. Le mélange de référence est géré comme les autres, rééquilibré en janvier.

**Tâche 2, la robustesse exigée.** Une stratégie n'est dite supérieure à une autre que si sa valeur ajoutée à risque égal est de même signe sur les deux moitiés de la période, coupées au 1er mai 2013, et si l'intervalle à 95 % du bootstrap par blocs exclut zéro. À défaut, le résultat est écrit comme indécidable.

**Tâche 3, le coût.** Pour chaque stratégie, le coût explicite annuel, le rendement abandonné, et la réduction obtenue sur trois mesures : volatilité, repli maximal, perte moyenne au-delà de la VaR à 99 %. Le rapport entre la réduction et le rendement abandonné est publié, sans être converti en classement unique : il n'existe pas de taux de change objectif entre un point de repli et un point de rendement.

**Tâche 4, le risque résiduel.** Pour chaque stratégie appliquée à `P1`, trois mesures de ce qui reste : la part de la variance que le marché n'explique pas, la pire perte par épisode, et la perte moyenne au-delà de la VaR à 99 % calculée sur les seules séances de tension. Le risque résiduel est aussi décomposé par maillon pour la couverture par contrats à terme, afin de dire si ce qui reste est encore le risque des puces.

**Tâche 5, ce que je m'interdis.** Aucune stratégie optimale, aucun poids optimisé. Aucune conclusion tirée de la seule sous-période depuis 2022. Aucun classement unique mêlant rendement et risque par une pondération que je choisirais.

### État de l'étape 4 au 28 septembre 2026 : close

Les six phases sont faites. Collecte : `VFITX`, `VUSTX`, `^VIX` et, pour un contrôle ajouté en cours de route, l'indice `^PUT`, avec leur manifeste. Construction et mesure : douze stratégies sur vingt et une séries, dans `src/couvrir_diversifier.ipynb`. Contrôles : identité des mélanges, positivité des valeurs, ordre de grandeur des primes, et niveau des prix d'option confronté à l'indice CBOE PutWrite. Tests : douze cas dans `tests/test_couverture.py`. Résultats : `research/resultats_couverture.md`.

Deux décisions ont été prises après la phase 0 et sont datées dans le carnet : le bêta estimé dès 63 séances et fixé à un avant, écrit avant tout résultat ; la variante de prix d'option à trois points sous le `VIX`, ajoutée après le contrôle PutWrite, qui a montré que le modèle surévalue les puts à la monnaie d'environ 3,8 points de volatilité, à rebours de ce que la phase 0 annonçait. Des trois hypothèses écrites avant calcul, deux sont confirmées et la troisième, sur la couverture par l'indice en 2000 à 2002, est contredite.

### État de l'étape 5 au 28 septembre 2026 : close

Les cinq tâches de la section VIII sont faites dans `src/comparer_strategies.ipynb`, et les résultats sont écrits dans `research/resultats_strategies.md`. Trois écarts à la section VIII sont datés du même jour. Les mélanges de liquidités sont retirés des candidats, parce qu'ils sont leurs propres jumeaux. Les puts sont aussi comparés dans la variante calibrée sur l'indice PutWrite. Les moitiés sont lues avec le jumeau de la période complète.
