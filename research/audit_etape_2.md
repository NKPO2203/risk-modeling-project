# Audit de l'étape 2 : état après finition

*8 septembre 2026. Les constats de l'audit précédent sont conservés dans `archive/2026-09-08_avant_finition/audit_etape_2.md`. Leurs anciens résultats ne sont plus les chiffres courants.*

## I. Ce qui a changé

La clôture des 114 dossiers avait ajouté 17 entreprises. L'application ultérieure d'A-08 à 20 exclusions en ajoute 4 autres. Les portefeuilles sont entièrement recalculés sur 134 entreprises et 135 titres. Les continuités JCI, PLD, BKR et SWKS sont bornées selon une même règle, documentée dans `portefeuilles.md`. Les trois bornes GOOG, DELL et VRT restent en place.

La revue des nouvelles distributions confirme les deux versements spéciaux LDOS, conserve les facteurs APD et LDOS comme conventions de fournisseur, et retire le doublon de dividende HD du 28 novembre 2001. Les cours bruts sont intacts. Les cinq corrections antérieures restent dans le registre ; JCI 2007 est désormais hors période admissible de ce titre.

## II. Ce qui a été vérifié

La reconstruction locale et les 103 tests réussissent. Le contrôle quotidien porte sur les vingt séries, y compris les jours d'opération. L'écart maximal d'identité est 8.969e-16. Les partitions de maturité et de chaîne recomposent les mêmes CIK que P1, sans doublon interne. Les 38 valorisations portées sont tracées. Le rapprochement externe couvre 64 titres et 155046 clôtures.

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



## III. Ce qui demeure limité

L'univers est choisi sur les informations récentes de 2026, puis projeté sur le passé. Il comporte un biais de connaissance a posteriori et de survivance. Les résultats décrivent des paniers actuels ; ils ne prouvent ni une stratégie identifiable à l'époque, ni un risque causé par l'IA. La règle III admet des activités générales de la chaîne : centres de données hors IA, semi-conducteurs, énergie, logistique et équipements. Les 134 degrés restent non quantifiés. La maturité distingue une activité établie d'un engagement, sans mesurer leur intensité.

Yahoo est une source secondaire. Close est déjà retraité des divisions, et Adj Close dépend d'ajustements rétroactifs. Le cliché conservé, ses dividendes et ses facteurs sont reproductibles localement ; une nouvelle collecte ne promet pas les mêmes valeurs. Ce ne sont pas des cours historiques totalement non ajustés. Les nombres d'actions SEC ne doivent pas être multipliés par ces cours sans harmoniser dates, classes et divisions.

Le rapprochement Nasdaq porte maintenant sur 64 titres et 155 046 clôtures, soit 154 982 rendements comparables. L'essentiel de cette couverture commence en septembre 2016. Sur les 103 variations extrêmes du brut situées dans un historique admissible, 82 restent non corroborées et 21 concordent en rendement de prix. Les neuf divergences anciennes non arbitrées restent exactement recensées dans `data/review/divergences_finition_2026-09-08.csv`. Les coefficients de scission ne sont pas certifiés. Toute conclusion de risque appuyée sur ces extrêmes devra expliciter cette réserve. Une identité comptable correcte ne certifie pas les prix.

Les dividendes sont des créances assimilées à des espèces au détachement, réinvesties en janvier. Les dates de paiement des actions ne sont pas collectées. L'ancien contrôle SPY situe l'effet du paiement tardif de décembre à environ 0,04 point par an sur ce fonds ; il ne mesure pas l'effet sur le nouvel univers. Les distributions de titres sont réinvesties synthétiquement dans le parent, sans frais propres à la scission. Il n'existe pas de registre exhaustif des opérations sur titres ni de reproduction d'un compte réellement conservé.

Le fichier auxiliaire `premieres_cotations.csv` couvre 79 entreprises et 79 titres parmi les 134 entreprises et 135 titres retenus. Il n'a pas été réécrit. Les métadonnées des nouveaux prix contiennent leur première transaction, ce qui ne certifie pas toutes les anciennes dates d'IPO. Les cas de collecte 11 à 13 restent sans tests d'acquisition importables. Le dernier relevé mensuel est la clôture du 4 septembre 2026, pas une fin de mois. L'étape 2 conserve sa commande séparée de `src/run_pipeline.py`.

La cotation conditionnelle de SNDK au 13 février 2025 reste retenue. L'ancienne sensibilité d'environ 0,29 point par an sur P1 conservé concernait l'univers précédent et n'est pas une mesure du portefeuille actuel. La liquidité et le coût d'une transaction en cotation conditionnelle ne sont pas démontrés. Aucune de ces limites n'est transformée en chantier supplémentaire dans cette finition.

**I. La capitalisation est écartée, décision du 8 septembre 2026.** Aucun portefeuille pondéré par capitalisation n'est ajouté. Les dix portefeuilles conservés permettent déjà d'observer la concentration se former à partir de poids initiaux égaux. Dans les relevés mensuels de la version recalculée, Nvidia atteint 24,93 % de P1 conservé au 2025-07-31. Ce poids résulte de la trajectoire du portefeuille ; il n'a pas été fixé à ce niveau à la constitution. Cette lecture répond à la question retenue, sans prétendre isoler à elle seule l'effet de la concentration sur le risque. Le contraste SPY/RSP reste un repère portant sur le marché entier.

Les nombres instantanés d'actions SEC du cliché commencent le 2009-02-24 et ne couvrent que 54 entreprises en 2009. Cette couverture renforce le refus, mais son coût n'en est pas la seule raison. La comparaison entre gestion conservée et rééquilibrée mêle dérive des poids, opérations et frais ; elle n'est pas un effet causal pur de concentration.

**II. P4 conserve son départ en 2000, décision du 8 septembre 2026.** Le calcul reste établi sur toute la période, sans raccourcir les autres séries. Les premières années conservent l'épisode 2000 à 2002. P4 compte 4 entreprises au départ, 5 à partir du 2002-07-01, 6 à partir du 19 août 2004, 7 à partir du 2010-06-29, 8 à partir du 2012-05-18, 9 à partir du 2012-06-29 et 10 à partir du 2021-04-15.

Toute comparaison de l'étape 3 impliquant P4 doit être rapportée deux fois : sur la période complète et sur la sous-période commençant le 19 août 2004, où il compte au moins six entreprises. Les séries comparées sont alignées dans chacune de ces deux lectures, sans modifier leurs historiques conservés. Si les conclusions concordent, la faiblesse de l'effectif initial ne change pas la conclusion de cette comparaison entre les fenêtres retenues. Cela ne démontre pas un effet nul de l'effectif en général. Sinon, la divergence doit être expliquée, en distinguant l'effectif des différences de période et de composition. Cette obligation est inscrite maintenant ; aucune comparaison de risque n'est produite dans cette mise à jour.

## IV. Conclusion de clôture

Les livrables demandés des étapes 1 et 2 permettent de déclarer cette version close selon la règle d'arrêt de l'auteur. Cette clôture conserve les réserves de données ; elle ne les transforme pas en anomalies résolues. Le journal de finition identifie les fichiers et les vérifications. Aucune étape 3 n'est commencée.
