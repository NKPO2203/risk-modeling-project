# Audit de l'étape 2 : état après finition

*8 septembre 2026. Les constats de l'audit précédent sont conservés dans `archive/2026-09-08_avant_finition/audit_etape_2.md`. Leurs anciens résultats ne sont plus les chiffres courants.*

## I. Ce qui a changé

La clôture des 114 dossiers ajoute 17 entreprises. Les portefeuilles sont entièrement recalculés sur 130 entreprises et 131 titres. Les continuités JCI, PLD, BKR et SWKS sont bornées selon une même règle, documentée dans `portefeuilles.md`. Les trois bornes GOOG, DELL et VRT restent en place.

La revue des nouvelles distributions confirme les deux versements spéciaux LDOS, conserve les facteurs APD et LDOS comme conventions de fournisseur, et retire le doublon de dividende HD du 28 novembre 2001. Les cours bruts sont intacts. Les cinq corrections antérieures restent dans le registre ; JCI 2007 est désormais hors période admissible de ce titre.

## II. Ce qui a été vérifié

La reconstruction locale et les 103 tests réussissent. Le contrôle quotidien porte sur les vingt séries, y compris les jours d'opération. L'écart maximal d'identité est 7.685e-16. Les partitions de maturité et de chaîne recomposent les mêmes CIK que P1, sans doublon interne. Les 38 valorisations portées sont tracées. Le rapprochement externe couvre 60 titres et 144990 clôtures.

| Groupe | Entreprises initiales | Entreprises finales | Titres finaux |
| --- | --- | --- | --- |
| P1 | 87 | 130 | 131 |
| P2 | 68 | 109 | 110 |
| P3 | 19 | 21 | 21 |
| P4 | 4 | 10 | 11 |
| P5 | 19 | 34 | 34 |
| P6 | 20 | 23 | 23 |
| P7 | 20 | 28 | 28 |
| P8 | 3 | 7 | 7 |
| P9 | 8 | 13 | 13 |
| P10 | 13 | 15 | 15 |


| Série | Base 100 finale | Annualisé | Rotation annuelle | Effet des frais, pb/an | Repli maximal |
| --- | --- | --- | --- | --- | --- |
| P1_reeq | 9 991,06 | 18,88 % | 25,07 % | 2,98 | -51,69 % |
| P1_cons | 10 018,86 | 18,90 % | 4,60 % | 0,55 | -53,07 % |
| P10_reeq | 3 662,96 | 14,49 % | 18,41 % | 2,11 | -56,82 % |
| P10_cons | 5 626,77 | 16,35 % | 2,64 % | 0,31 | -62,18 % |
| P2_reeq | 10 990,93 | 19,31 % | 25,97 % | 3,10 | -55,54 % |
| P2_cons | 10 903,34 | 19,27 % | 4,81 % | 0,57 | -55,10 % |
| P3_reeq | 3 917,48 | 14,77 % | 17,27 % | 1,98 | -44,82 % |
| P3_cons | 4 357,12 | 15,23 % | 3,45 % | 0,40 | -51,54 % |
| P4_reeq | 47 977,33 | 26,10 % | 36,25 % | 4,57 | -70,60 % |
| P4_cons | 5 902,89 | 16,56 % | 7,02 % | 0,82 | -86,53 % |
| P5_reeq | 15 476,45 | 20,85 % | 30,49 % | 3,69 | -72,64 % |
| P5_cons | 25 576,60 | 23,16 % | 4,91 % | 0,60 | -73,08 % |
| P6_reeq | 2 032,55 | 11,98 % | 13,06 % | 1,46 | -44,99 % |
| P6_cons | 1 923,69 | 11,75 % | 4,33 % | 0,48 | -44,62 % |
| P7_reeq | 7 656,17 | 17,70 % | 17,21 % | 2,03 | -54,02 % |
| P7_cons | 7 419,05 | 17,56 % | 3,82 % | 0,45 | -53,75 % |
| P8_reeq | 6 731,43 | 17,13 % | 25,63 % | 3,00 | -64,52 % |
| P8_cons | 2 588,94 | 13,00 % | 8,56 % | 0,97 | -59,65 % |
| P9_reeq | 5 007,99 | 15,84 % | 23,51 % | 2,72 | -72,34 % |
| P9_cons | 2 284,38 | 12,47 % | 4,19 % | 0,47 | -73,13 % |


| Série | Titre | Date du relevé | Poids maximal relevé |
| --- | --- | --- | --- |
| P10_cons | TPL | 2024-11-29 | 73,66 % |
| P10_reeq | WMB | 2003-10-31 | 19,05 % |
| P1_cons | NVDA | 2025-07-31 | 25,24 % |
| P1_reeq | FSLR | 2007-12-31 | 7,37 % |
| P2_cons | NVDA | 2025-07-31 | 29,04 % |
| P2_reeq | SBAC | 2003-07-31 | 7,92 % |
| P3_cons | TPL | 2024-11-29 | 67,97 % |
| P3_reeq | FSLR | 2007-12-31 | 30,37 % |
| P4_cons | TSLA | 2022-09-30 | 62,02 % |
| P4_reeq | SBAC | 2003-07-31 | 62,56 % |
| P5_cons | NVDA | 2024-11-29 | 61,66 % |
| P5_reeq | NVDA | 2001-12-31 | 18,90 % |
| P6_cons | VST | 2025-07-31 | 20,49 % |
| P6_reeq | VST | 2024-11-29 | 12,60 % |
| P7_cons | GNRC | 2021-10-29 | 21,63 % |
| P7_reeq | PWR | 2000-06-30 | 13,87 % |
| P8_cons | O | 2002-09-30 | 61,02 % |
| P8_reeq | EQIX | 2003-12-31 | 50,87 % |
| P9_cons | FSLR | 2008-07-31 | 61,00 % |
| P9_reeq | FSLR | 2007-12-31 | 53,53 % |


## III. Ce qui demeure limité

L'univers est choisi sur les informations récentes de 2026, puis projeté sur le passé. Il comporte un biais de connaissance a posteriori et de survivance. Les résultats décrivent des paniers actuels ; ils ne prouvent ni une stratégie identifiable à l'époque, ni un risque causé par l'IA. La règle III admet des activités générales de la chaîne : centres de données hors IA, semi-conducteurs, énergie, logistique et équipements. Les 130 degrés restent non quantifiés. La maturité distingue une activité établie d'un engagement, sans mesurer leur intensité.

Yahoo est une source secondaire. Close est déjà retraité des divisions, et Adj Close dépend d'ajustements rétroactifs. Le cliché conservé, ses dividendes et ses facteurs sont reproductibles localement ; une nouvelle collecte ne promet pas les mêmes valeurs. Ce ne sont pas des cours historiques totalement non ajustés. Les nombres d'actions SEC ne doivent pas être multipliés par ces cours sans harmoniser dates, classes et divisions.

Le rapprochement Nasdaq porte maintenant sur 60 titres et 144 990 clôtures, soit 144 930 rendements comparables. L'essentiel de cette couverture commence en septembre 2016. Sur les 102 variations extrêmes du brut situées dans un historique admissible, 82 restent non corroborées et 20 concordent en rendement de prix. Les neuf divergences anciennes non arbitrées restent exactement recensées dans `data/review/divergences_finition_2026-09-08.csv`. Les coefficients de scission ne sont pas certifiés. Toute conclusion de risque appuyée sur ces extrêmes devra expliciter cette réserve. Une identité comptable correcte ne certifie pas les prix.

Les dividendes sont des créances assimilées à des espèces au détachement, réinvesties en janvier. Les dates de paiement des actions ne sont pas collectées. L'ancien contrôle SPY situe l'effet du paiement tardif de décembre à environ 0,04 point par an sur ce fonds ; il ne mesure pas l'effet sur le nouvel univers. Les distributions de titres sont réinvesties synthétiquement dans le parent, sans frais propres à la scission. Il n'existe pas de registre exhaustif des opérations sur titres ni de reproduction d'un compte réellement conservé.

Le fichier auxiliaire `premieres_cotations.csv` couvre 78 entreprises et 78 titres parmi les 130 entreprises et 131 titres retenus. Il n'a pas été réécrit. Les métadonnées des nouveaux prix contiennent leur première transaction, ce qui ne certifie pas toutes les anciennes dates d'IPO. Les cas de collecte 11 à 13 restent sans tests d'acquisition importables. Le dernier relevé mensuel est la clôture du 4 septembre 2026, pas une fin de mois. L'étape 2 conserve sa commande séparée de `src/run_pipeline.py`.

La cotation conditionnelle de SNDK au 13 février 2025 reste retenue. L'ancienne sensibilité d'environ 0,29 point par an sur P1 conservé concernait l'univers précédent et n'est pas une mesure du portefeuille actuel. La liquidité et le coût d'une transaction en cotation conditionnelle ne sont pas démontrés. Aucune de ces limites n'est transformée en chantier supplémentaire dans cette finition.

Aucun portefeuille de cet univers n'est pondéré par capitalisation. Le contraste SPY/RSP concerne le marché entier ; la comparaison conservé/rééquilibré mêle dérive, opérations et frais. Elle n'isole pas un effet pur de concentration des poids.

**Option de capitalisation, à décider par l'auteur.** Les nombres instantanés SEC du cliché commencent le 2009-02-24 et couvrent 54 entreprises en 2009. Une variante à partir d'une date commune demanderait de collecter les actions manquantes, vérifier chaque classe et retraiter les divisions sans anticipation. Coût indicatif : plusieurs journées de préparation et de validation, davantage pour un historique complet depuis 2000. Aucun poids de cette nature n'est ajouté.

**Option de départ retardé de P4, à décider par l'auteur.** P4 compte maintenant 4 entreprises à la première date, contre trois avant l'ajout de SBA Communications, et 10 à la fin. Retarder son départ atténuerait le problème d'effectif, tout en retirant une partie des crises et en raccourcissant la comparaison. Les autres séries et benchmarks devraient être ramenés à la même fenêtre. Coût indicatif : une demi-journée pour un scénario de départ arrêté par l'auteur, recalcul et rédaction compris. Aucune nouvelle date n'est fixée ici.

## IV. Conclusion de clôture

Les livrables demandés des étapes 1 et 2 permettent de déclarer cette version close selon la règle d'arrêt de l'auteur. Cette clôture conserve les réserves de données ; elle ne les transforme pas en anomalies résolues. Le journal de finition identifie les fichiers et les vérifications. Aucune étape 3 n'est commencée.
