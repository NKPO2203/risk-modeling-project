# Journal des corrections et vérifications de l'étape 2

*Complément du 8 septembre 2026. Ce journal commence après l'audit initial de deux heures.*

## I. Les décisions prises

Le contrôle porte sur les prix effectivement utilisés, les opérations sur titres et la reconstruction des portefeuilles. Trois erreurs de richesse sont corrigées : Tyco dans JCI au 2 juillet 2007, Eaton au 2 janvier 2001, CenterPoint au 1er octobre 2002. Deux distributions en titres sont reclassées, sur CNP en janvier 2003 et JCI en octobre 2016, sans changement de richesse le jour même. Les calculs et sources sont dans `research/verification_etape_2.md` et le registre JSON des corrections.

Le programme `src/corrections_prix.py` travaille sur une copie en mémoire. Les facteurs antérieurs s'appliquent aussi aux anciens dividendes pour ne pas modifier leur rendement. Des valeurs témoins refusent un changement de cliché ou une double application. Le moteur reçoit les cours et dividendes corrigés ; le fichier brut reste la preuve du défaut initial.

Le rapprochement Nasdaq conserve 43 réponses publiques et compare 103 411 clôtures. Son programme, `src/recouper_prix.py`, travaille hors réseau, contrôle les empreintes et refuse de comparer comme quotidiens deux rendements dont les dates diffèrent. Les concordances, divergences et absences de corroboration sont séparées.

Les passages courants de `portefeuilles.md`, `controle_donnees_prix.md`, `plan_projet.md`, du contexte et du notebook ont été reformulés pour expliquer les règles directement. Le rapport initial reste un état historique ; son en-tête oriente vers le complément. Le statut n'est pas artificiellement passé à « entièrement validé » : 79 variations extrêmes anciennes et 9 écarts de rendement entre fournisseurs restent non corroborés ou non arbitrés. Les distributions synthétiques, quant à elles, restent une convention explicite et non une promesse de registre de parts réel.

## II. Validation finale

| Contrôle | Résultat |
|---|---|
| Tests complets | 99 réussis, aucun échec |
| Recalcul des portefeuilles | 20 séries, 6 709 niveaux, 6 708 rendements |
| Identité quotidienne de richesse | écart maximal 7.39 × 10⁻¹⁶ |
| Somme des poids | écart maximal 4.44 × 10⁻¹⁶ |
| Notebook Python 3.12.14 contre commande Python 3.13.9 | 18 sorties identiques à l'octet |
| Cellules de code du notebook exécutées | 1, 3, 5, 7, numérotation depuis zéro |
| Empreintes du pipeline de l'étape 2 | vérifiées par `--check-only` |
| Fichiers bruts protégés | 2 646 comparés, aucun modifié |
| Sorties du manifeste de l'étape 1 | 11 comparées, aucune modifiée |
| Recalcul préalable contre publication finale | 18 sorties identiques |
| Commit et push | aucun |

L'inventaire porte sur les différences depuis le cliché local conservé au début de ce complément. Des fichiers étaient déjà modifiés ou non suivis par Git avant ce travail ; ils ne sont pas attribués rétroactivement à ces corrections. Les CSV de prix Nasdaq ajoutés comme preuves de contrôle se trouvent dans `data/review/`, pas dans les dossiers bruts protégés.

Les empreintes avant et après complètes sont dans `data/review/sources_cloture_2026-09-08/verification_manifest.json`. Les résultats économiques avant/après sont dans `impact_corrections.csv` du même dossier. Les grandes données générées ne sont pas recopiées comme des millions de lignes de différences : leurs fichiers, empreintes et effets chiffrés permettent de les identifier.

## III. Inventaire des 75 fichiers ajoutés ou modifiés

| Fichier | Modification | SHA-256 après |
|---|---|---|
| `data/processed/controles_portefeuilles.json` | modifie | `d7266fd81dbd558ac7d29a3d89ed0d5ee57204e42915e12cd47c63074e952504` |
| `data/processed/dividendes.csv` | modifie | `13fa490052fc312bc64ae0292043609726accd1cc2673bcfae215e3a8a9526d4` |
| `data/processed/journal_portefeuilles.csv` | modifie | `a0305910f18e366247ef3d72c7f810702f6a3c2081b9e6d2b81e66e7a76d6c4a` |
| `data/processed/mesures_portefeuilles.csv` | modifie | `49bd4d27ad4ddaccab02f760798217c4bf4357ce32a83ebae4af8074274fc933` |
| `data/processed/pipeline_portefeuilles.json` | modifie | `30dc8ade799f7712deeefee1b7fd5837c25791455af0e278b110eeada01730a9` |
| `data/processed/poids_mensuels.csv` | modifie | `26bfedeb98bbd088b2ad0c8a42b3f53eb063777d0798c93af5d03df9375e3546` |
| `data/processed/rendements_prix.csv` | modifie | `f141b0550b5ca7cbd1d2f51f210fd9bb750976c35d40e9b0b4ac601661f342f8` |
| `data/processed/rendements_valorisation.csv` | modifie | `5f56420a311770286497aa179de5f8df3f113c90c2b15a0b38c1a691dace4ceb` |
| `data/processed/valeurs_portefeuilles.csv` | modifie | `e9ec203747f5bec7fcdde26250ff6c03cb45580fd47603e68d5fc08ff6c92b68` |
| `data/review/corrections_evenements_prix.json` | ajoute | `6a094195358643046160250d9ed4246a95eb7362a7b14e42cd05dfd0c857ce83` |
| `data/review/evenements_prix_documentes.csv` | ajoute | `056715f115905fa54145cc3a28fb616bc8ce37025db70577536982168c1add2b` |
| `data/review/sources_cloture_2026-09-08/bilan.json` | ajoute | `3177c6a36c7f387d8fbdee45310f5216288da7ad560078ba4dffe6b2bc9458a2` |
| `data/review/sources_cloture_2026-09-08/comparaison_cours.csv` | ajoute | `49c1bb9cda34723384f8e8e1dbaf492c78963ac8246db8a35f9fd73d4a5e4716` |
| `data/review/sources_cloture_2026-09-08/couverture.csv` | ajoute | `472c5e3f81573b6731311ce47f6d3aa99daca3b468b7fd1ed1bce7f9f07ff322` |
| `data/review/sources_cloture_2026-09-08/divergences.csv` | ajoute | `6320b1588d9c1520b18d8b246ad4ab810bb1588f4851f6dfa3592c79b3b693ac` |
| `data/review/sources_cloture_2026-09-08/divergences_qualifiees.csv` | ajoute | `c5930647685a35ff5c2a3036e49a8a015e5d96d31b3817a0df6febef3d4eaacc` |
| `data/review/sources_cloture_2026-09-08/impact_corrections.csv` | ajoute | `3c32e9850f5627be08a305a591feba5b56843f680f2c35a1c936e8a9a60f1a87` |
| `data/review/sources_cloture_2026-09-08/nasdaq_AES.json` | ajoute | `a6f3da8d0adccbf22ebe76813eae725c35903f202a008bd3709815abcbbc0b77` |
| `data/review/sources_cloture_2026-09-08/nasdaq_AKAM.json` | ajoute | `11e1a7415e8b65ebe58d3eac7cfd57b23b845b502b15fdec959d10cab7958424` |
| `data/review/sources_cloture_2026-09-08/nasdaq_AMD.json` | ajoute | `005c178a8ceedb5d11e862d854cffe08e433498a35cbd3a2224ca1cdc31bfbb8` |
| `data/review/sources_cloture_2026-09-08/nasdaq_AMT.json` | ajoute | `2204fe512a97aa196166c4f2bc8d7ca574b25513fdb181721ad07198187bd1d0` |
| `data/review/sources_cloture_2026-09-08/nasdaq_AMZN.json` | ajoute | `22bea710fc9cbae67aa29b93d08aa536c63e35317d3255ae5fd720421a3468fe` |
| `data/review/sources_cloture_2026-09-08/nasdaq_CBRE.json` | ajoute | `beb35e74f66d729b164bfcae0dc5311d96c63b3c82d971dc66e420f46fc6ae4f` |
| `data/review/sources_cloture_2026-09-08/nasdaq_CDNS.json` | ajoute | `235d14e529a2ceba6ce73fb6cb30f584dda9386c853d2bc0a036b33b1cc33460` |
| `data/review/sources_cloture_2026-09-08/nasdaq_CIEN.json` | ajoute | `cea854ccb8a37ec44155d0362b09e79ade27110a92defce4c6d0e013a0fde4d2` |
| `data/review/sources_cloture_2026-09-08/nasdaq_CNP.json` | ajoute | `6d636297197df54276f4af2e0b3487c8ff8b15716e251a8c132c52ba97d6b068` |
| `data/review/sources_cloture_2026-09-08/nasdaq_COHR.json` | ajoute | `69aadd78eebe342e8e43c15e5205e336813f4d5feebe56862ec8ed5391f48fd5` |
| `data/review/sources_cloture_2026-09-08/nasdaq_DELL.json` | ajoute | `876e8ce5e792c2e611d94c22313f42e000dedcaa38a7685c2d10f8710a1c9993` |
| `data/review/sources_cloture_2026-09-08/nasdaq_DTE.json` | ajoute | `deb27b3c5d2965cd0f6151f04a9fac4c8dc5ba8a755831b14d6f11c97774a2e1` |
| `data/review/sources_cloture_2026-09-08/nasdaq_EQIX.json` | ajoute | `2795cd4f61a5473f5d16c82996f9f448c769590047f33867b7d904aecafe3b1b` |
| `data/review/sources_cloture_2026-09-08/nasdaq_FIX.json` | ajoute | `3a29faf93af877586bb7a6be77c0982dd51460b4fc9129bda1eec2702f844db8` |
| `data/review/sources_cloture_2026-09-08/nasdaq_FLEX.json` | ajoute | `99c65e517544169aa07733b5e9890209b85a3ec7419f164ef488527a4b6c46a5` |
| `data/review/sources_cloture_2026-09-08/nasdaq_GLW.json` | ajoute | `0000a8c8dd7e43e8db84b972e23001cc5e2fd2c7aa705fbff68f45f5ca291182` |
| `data/review/sources_cloture_2026-09-08/nasdaq_HAL.json` | ajoute | `52e211343d7c787e4e76df0a8adaada439b7d5e420ee7270ed7955fa41a9c22b` |
| `data/review/sources_cloture_2026-09-08/nasdaq_HPE.json` | ajoute | `1dab30538faa8d6e4967039b57d9500517a568f7430e1f21e0ad732690ee528e` |
| `data/review/sources_cloture_2026-09-08/nasdaq_IBM.json` | ajoute | `ac238132313d64b762e1ee631a635e26d60f4cb7763b075531999229902ba851` |
| `data/review/sources_cloture_2026-09-08/nasdaq_JBL.json` | ajoute | `2ffe138edef53338d29a5e2f27e3374d184fb177ed0d84d6d470d6131c759734` |
| `data/review/sources_cloture_2026-09-08/nasdaq_JCI.json` | ajoute | `c3348fcf2a246177f539ff27cf3c1a5f44b252ae7ba0eb7abc23f9db280ab609` |
| `data/review/sources_cloture_2026-09-08/nasdaq_LITE.json` | ajoute | `14c7b7ecea53d0c5b7b9ca0b2736468dd2eb9a9e76c7b94ea2dffe6c0dd35780` |
| `data/review/sources_cloture_2026-09-08/nasdaq_manifest.json` | ajoute | `627d2f6c802a5f3df05e6199ef74e885c68cd0dc49d693b716d5866c64d61459` |
| `data/review/sources_cloture_2026-09-08/nasdaq_MMM.json` | ajoute | `20d67eeeeba9ac4c2e9c12fe0acd1819930f70759401a5d5962e2c4f3f02114a` |
| `data/review/sources_cloture_2026-09-08/nasdaq_MRVL.json` | ajoute | `8e6d1eb9679f1f3c98ce63b10232550839d9410f714ec087ee5aab76032c2613` |
| `data/review/sources_cloture_2026-09-08/nasdaq_NTAP.json` | ajoute | `d400212204dde6d783c62f61767ba2d4a1f85c82783b419a0d88aecb93d30695` |
| `data/review/sources_cloture_2026-09-08/nasdaq_NVDA.json` | ajoute | `55a2d5ae8ac4b4c598a0d8b5f45c1ee5fd86be7038386363350399e3db165ccb` |
| `data/review/sources_cloture_2026-09-08/nasdaq_O.json` | ajoute | `355446df64d7c0634abd8aefa13a1601f1539ee09c88027a300ad0ea3b61a7de` |
| `data/review/sources_cloture_2026-09-08/nasdaq_ON.json` | ajoute | `e20065dfbf235fe4326b8a8d1f3861b18d6a5443ab31a6f17fe25e3f300b866a` |
| `data/review/sources_cloture_2026-09-08/nasdaq_ORCL.json` | ajoute | `7c5db8b67bd426dbbd66fde038c4257b0d8fe40c3ebde041358e8d76e62fd6be` |
| `data/review/sources_cloture_2026-09-08/nasdaq_PLD.json` | ajoute | `1c4aa79b98e1465c99989459f9b2fad15ae322e18c50289672530c29e1da918e` |
| `data/review/sources_cloture_2026-09-08/nasdaq_PWR.json` | ajoute | `f174abd8fe5e40a0c290e24fefa7ed0240b238941c5482a68af5051889b0bc85` |
| `data/review/sources_cloture_2026-09-08/nasdaq_RSP.json` | ajoute | `fdb0cc807bc2cc140c7bb9c66bf50bf4287c4be65854f54e0cfb4f5e260b6d75` |
| `data/review/sources_cloture_2026-09-08/nasdaq_SMCI.json` | ajoute | `7d5bee4ed2f5a6ca573530af2d77683e79eaf196e716d7d2c23af913a1ef74df` |
| `data/review/sources_cloture_2026-09-08/nasdaq_SNDK.json` | ajoute | `caad1e8a25a9e7b150c6ede7fd57b99bc08c87235b526974289a5c3e4ad134c2` |
| `data/review/sources_cloture_2026-09-08/nasdaq_SNPS.json` | ajoute | `dfe7e24917b7b9ed1a9546bb0ef0613e9157be834816c4ed38fc1dcbdb1f059e` |
| `data/review/sources_cloture_2026-09-08/nasdaq_SPY.json` | ajoute | `393520cca6d8eaf69b63ca0c88a31e7606271d5a78e101a85b327b6d009dd32d` |
| `data/review/sources_cloture_2026-09-08/nasdaq_SWKS.json` | ajoute | `48ad08333141df2f786ec5eab00efac4f83ed968073fc378d8c76762c024c871` |
| `data/review/sources_cloture_2026-09-08/nasdaq_TDY.json` | ajoute | `3523f271c24f655bb18d47835d7e8138ddde45beeee38f39a844e589f48522e1` |
| `data/review/sources_cloture_2026-09-08/nasdaq_TSLA.json` | ajoute | `4f2197575bfd85a54812db0df77326992002e0e7c0cf79a265470cb354636256` |
| `data/review/sources_cloture_2026-09-08/nasdaq_VRT.json` | ajoute | `cb3a44254b413274618ac553698aa70273392b6e58e79803724f7b391768f6db` |
| `data/review/sources_cloture_2026-09-08/nasdaq_WDC.json` | ajoute | `b975cf91bf4c974b8706a778c983930aab0f9a8f1ef61f59948acbd67f8bf006` |
| `data/review/sources_cloture_2026-09-08/nasdaq_WMB.json` | ajoute | `fbb4335394ca162dda352877e48af29d982f3d9dcf5a5b18b1489c1ec3d43545` |
| `data/review/sources_cloture_2026-09-08/nasdaq_XEL.json` | ajoute | `1eb1ec42efc758ae1364bfe31e9547910c548d0c8318350faf87e93277b1c3b1` |
| `data/review/sources_cloture_2026-09-08/variations_examines.csv` | ajoute | `da187367b4fdcb0ff4ee5508e6f1099876968f3dd192a7b9c08a5e4803bb3e33` |
| `README.md` | modifie | `3b4298af8d991f7fcc7b27f7e91d486a5c780857474c1919ecc5733c61350e3f` |
| `research/audit_etape_2.md` | modifie | `ed6d9a1385c36a6aba4bd981ec147b50b609631fcc5cffc7640391c2ef633b0b` |
| `research/controle_donnees_prix.md` | modifie | `740897a3debcc15be96a3e323084952f2efe26a73a753951c1a41ba9dd554fef` |
| `research/master_context.md` | modifie | `9b7cb3d0039acabd1747712588f1b8de1a3f3d4ddbb965efce6c5366c7e65b22` |
| `research/plan_projet.md` | modifie | `75cd75a9950d13e11a7b791c2c88501bb54690b66cfdb138e1bce09d965c1b23` |
| `research/portefeuilles.md` | modifie | `6fd3ea55b2620628f065d07ba401b387315b1bf95141fc704c4cad6f5354923f` |
| `research/verification_etape_2.md` | ajoute | `55a0e2a9e909476f3085f707deadf24c2ff5d994ad86c8079b7b5ac6ab2b7dcd` |
| `src/construire_portefeuille.ipynb` | modifie | `11cc154d4d9678c54b60c9e7ce24003a1fbfce40926e570525933c3d85d5e12b` |
| `src/construire_portefeuilles.py` | modifie | `8a9b728acd705d13db56c573c6ef828edb0011ebf92106b771283e1e4e60cd2d` |
| `src/corrections_prix.py` | ajoute | `98195c67d65b759b1cdbfd55c2a73b48b229676dbc20a8db1e8449977778f8c6` |
| `src/portefeuille.py` | modifie | `065ce80c2accf9a08dfc5edab65f0dcfb26a937a118186dd5cfef4f860af045c` |
| `src/recouper_prix.py` | ajoute | `175e749883c5c7de26b7646aec2f8a451053a5b9e8b34c4b9f4943aa54627a94` |
| `tests/test_corrections_prix.py` | ajoute | `a032a38482c124e044c4ecc2d313d786abb0f30ec5b31935f07b0a6bc4f3b795` |

Le présent journal et son manifeste de contrôle sont exclus de cette table pour éviter une empreinte circulaire. Le manifeste Nasdaq conserve en plus les URL exactes de collecte et les empreintes des réponses sources.

## IV. Différences exactes du code et des documents existants

Les blocs suivants reproduisent les modifications, avec le contexte nécessaire pour les retrouver. Les nouveaux rapports et les preuves numériques sont indexés ci-dessus ; ils ne sont pas dupliqués intégralement dans ces blocs.

### README.md

````diff
--- avant/README.md
+++ apres/README.md
@@ -2,7 +2,7 @@
 
 Je construis et compare des portefeuilles à partir d'un univers documenté d'entreprises exposées à la chaîne des infrastructures de calcul liées à l'IA, issu de la composition locale du S&P 500.
 
-L'étape 1 prépare les sources, les décisions et les comptes. L'étape 2 produit maintenant des trajectoires rétrospectives et leurs contrôles. L'analyse des sources du risque et des couvertures reste à faire.
+L'étape 1 prépare les sources, les décisions et les comptes. L'étape 2 produit maintenant des trajectoires rétrospectives et leurs contrôles. Le [complément de vérification](research/verification_etape_2.md) donne les corrections de prix, la comparaison Nasdaq et sa couverture réelle. L'analyse des sources du risque et des couvertures reste à faire.
 
 ## Lire le projet
 

````

### research/audit_etape_2.md

````diff
--- avant/research/audit_etape_2.md
+++ apres/research/audit_etape_2.md
@@ -1,6 +1,8 @@
 # Audit de l'étape 2
 
-*AI Concentration Risk Research. 8 septembre 2026. Contrôle, corrections et contre-vérifications.*
+*AI Concentration Risk Research. Audit initial du 8 septembre 2026, conservé comme historique.*
+
+**Complément postérieur :** `research/verification_etape_2.md` donne les vérifications externes, corrections d’opérations sur titres et résultats recalculés après cet audit. Les chiffres et réserves ci-dessous décrivent son état de fin, antérieur à ce complément. Le journal de différences est conservé tel quel.
 
 L'étape 2 ne doit pas être déclarée close. Ses calculs peuvent être reconstruits, mais une reconstruction correcte n'est pas une preuve de l'identité de tous les instruments ni de l'exécution réelle d'une stratégie. Les erreurs démontrées de code et de rédaction décrites ci-dessous ont été corrigées. Les dates de paiement, les opérations sur titres et la couverture de seconde source restent des réserves, pas des points réputés réglés parce que les tests passent.
 

````

### research/controle_donnees_prix.md

````diff
--- avant/research/controle_donnees_prix.md
+++ apres/research/controle_donnees_prix.md
@@ -2,9 +2,9 @@
 
 *AI Concentration Risk Research. Phase 2 de l'étape 2. Mise à jour du 8 septembre 2026 après audit.*
 
-## I. Ce que je cherche
+## I. La question du contrôle
 
-Je cherche à distinguer une propriété du marché d'un défaut de fichier. Ce contrôle précède l'interprétation des risques ; les mesures descriptives utilisées pendant l'audit ne constituent pas les résultats de l'étape 3. Une série plausible ne devient pas exacte parce qu'elle passe des tests internes.
+Une forte variation peut venir du marché, d'une opération sur titres ou d'un défaut de fichier. Le contrôle doit les distinguer. Ce contrôle précède l'interprétation des risques ; les mesures descriptives utilisées pendant l'audit ne constituent pas les résultats de l'étape 3. Une série plausible ne devient pas exacte parce qu'elle passe des tests internes.
 
 ## II. Le périmètre et la méthode
 
@@ -50,7 +50,7 @@
 
 ## IV. Ce que ces contrôles changent
 
-**Les cours figés.** Sur HUBB, 5 510 lignes portent un volume nul et quatre prix identiques, égaux à la clôture précédente. Le nombre de 5 561 concernait tous les volumes nuls, pas ce critère strict. Un long segment sans volume suivi d'une rupture, comme celle du 31 octobre 1994, ne doit pas être utilisé comme un historique ordinaire de rendements. Je ne peux cependant pas prouver avec ces seuls champs que toute séance isolée sans volume est fabriquée. Le filtre courant distingue les segments initiaux, les prix intérieurs figés et les prix variables à volume nul.
+**Les cours figés.** Sur HUBB, 5 510 lignes portent un volume nul et quatre prix identiques, égaux à la clôture précédente. Le nombre de 5 561 concernait tous les volumes nuls, pas ce critère strict. Un long segment sans volume suivi d'une rupture, comme celle du 31 octobre 1994, ne doit pas être utilisé comme un historique ordinaire de rendements. Ces seuls champs ne prouvent cependant pas que toute séance isolée sans volume est fabriquée. Le filtre courant distingue les segments initiaux, les prix intérieurs figés et les prix variables à volume nul.
 
 Après les restrictions d'identité sur GOOG, DELL et VRT, 18 observations sont portées sur la période de construction. Le mouvement cumulé est pris à la reprise ; les rendements observés restent manquants autour du trou. La liste est dans `qualite_valorisation.csv`. Estimer une volatilité ou une corrélation en traitant ces valeurs portées comme des observations ordinaires demanderait une réserve supplémentaire.
 
@@ -70,24 +70,34 @@
 
 Le contrôle SEC porte sur des actions en circulation, pas sur les cours. L'affirmation selon laquelle aucun recoupement public supplémentaire n'était possible était trop générale. L'audit a consulté le fichier de [distributions historiques de State Street](https://www.ssga.com/library-content/products/fund-data/etfs/us/spdr-etf-historical-distributions.xlsx).
 
-Les 135 dates de distribution de SPY depuis 1993 concordent. Sur les 107 distributions de la période de construction, une différence dépasse l'arrondi au millième : le 17 décembre 2021, Yahoo porte 1,633 dollar et State Street 1,636431 dollar. Je conserve les deux valeurs dans le constat, sans réécrire la preuve brute. Remplacer les montants par ceux de State Street dans un calcul séparé modifie l'annualisation de SPY d'environ 0,01 point de base. Avant 2000, d'autres divergences existent et ne concernent pas la fenêtre de construction.
+Les 135 dates de distribution de SPY depuis 1993 concordent. Sur les 107 distributions de la période de construction, une différence dépasse l'arrondi au millième : le 17 décembre 2021, Yahoo porte 1,633 dollar et State Street 1,636431 dollar. Les deux valeurs restent consignées ; la preuve brute est conservée. Remplacer les montants par ceux de State Street dans un calcul séparé modifie l'annualisation de SPY d'environ 0,01 point de base. Avant 2000, d'autres divergences existent et ne concernent pas la fenêtre de construction.
 
 La [page officielle de SPY](https://www.ssga.com/us/en/individual/etfs/state-street-spdr-sp-500-etf-trust-spy) donne une clôture de 773,17 dollars au 3 septembre 2026 ; le fichier Yahoo contient 773,1699829101562. Ce point concorde à l'arrondi. Les volumes de place et les volumes consolidés n'ont pas le même périmètre ; leur différence ne constitue pas à elle seule une erreur. Un cours et des distributions de SPY ne valident pas les historiques des 114 actions.
 
 Le calendrier de distribution officiel révèle une autre limite : les 26 dividendes de décembre inclus depuis 2000 sont payés fin janvier suivant. Notre modèle les assimile à une poche disponible au détachement et peut donc les réinvestir avant paiement. En conservant les mêmes cours et montants Yahoo mais en attendant les paiements officiels, avec la même unique date annuelle de réinvestissement, l'annualisation de SPY diminue de 4,10 points de base. Les créances impayées restent dans la richesse ; elles ne sont pas supprimées. Cette sensibilité mesure une approximation d'exécution, pas un défaut de conservation de valeur.
 
-La dernière passe ajoute quatre clôtures de Sandisk, du 31 août au 3 septembre 2026, publiées sur sa [page investisseurs alimentée par LSEG](https://investor.sandisk.com/stock-information/historical-price-lookup). Elles concordent à l'arrondi avec le cliché : 1 566,70, 1 536,87, 1 553,40 et 1 554,99 dollars. Ce rapprochement porte sur des prix récents, pas sur toute la hausse depuis la séparation. Une sensibilité déplaçant la seule entrée de SNDK de sa cotation conditionnelle du 13 février 2025 à sa cotation ordinaire du 24 février réduit l'annualisation de P5 conservé de 64,21 points de base. Le rapport d'audit détaille ce choix d'exécution, dont l'effet est plus grand que celui des frais testés.
+L'audit initial avait rapproché quatre clôtures de Sandisk, du 31 août au 3 septembre 2026, publiées sur sa [page investisseurs alimentée par LSEG](https://investor.sandisk.com/stock-information/historical-price-lookup). Elles concordent à l'arrondi avec le cliché : 1 566,70, 1 536,87, 1 553,40 et 1 554,99 dollars. Le complément décrit ci-dessous couvre désormais les 392 clôtures de Sandisk depuis le 13 février 2025. Une sensibilité déplaçant la seule entrée de SNDK de sa cotation conditionnelle du 13 février 2025 à sa cotation ordinaire du 24 février réduit l'annualisation de P5 conservé de 64,21 points de base. Le rapport d'audit détaille ce choix d'exécution, dont l'effet est plus grand que celui des frais testés.
 
-## VI. Ce qui reste ouvert
+## VI. Vérification complémentaire du 8 septembre 2026
 
-Les dates de paiement des actions, les identités historiques des autres titres, les opérations sur titres et un échantillon de cours de plusieurs entreprises demandent encore un rapprochement externe. Une scission peut être incorporée dans un cours retraité sans que le moteur reconstruise les titres distribués. La version conservée reste donc une simulation sur séries retraitées, pas un registre certifié de titres détenus.
+Le rapprochement Nasdaq porte sur 103 411 clôtures de 43 titres, dont deux fonds, et 103 368 paires quotidiennes comparables. La source reçue ne remonte généralement pas au-delà de septembre 2016. Les réponses, empreintes, dates couvertes et écarts sont conservés dans `data/review/sources_cloture_2026-09-08/`. La commande `python -m src.recouper_prix` rejoue le rapprochement sans réseau.
+
+Les 392 clôtures de Sandisk concordent à l’arrondi. Parmi les 98 variations extrêmes signalées depuis 2000, 18 ont un rendement de prix concordant avec Nasdaq ; une correspond à la scission Tyco corrigée sur pièces SEC ; 79 restent non corroborées. Une absence de source ne valide ni ne réfute ces variations. Les résultats des contrôles bruts restent inchangés afin de conserver la trace des erreurs dans le cliché.
+
+Le registre des opérations documente 34 événements : les 20 rapprochements SEC incompatibles, les 9 sans encadrement, et les 5 événements traités dans les corrections. Une scission ne se contrôle pas en exigeant que le nombre d’actions du parent augmente du facteur de prix. La nature juridique est documentée séparément de la précision du coefficient boursier.
+
+Trois erreurs de richesse sont corrigées dans les traitements de JCI, ETN et CNP. Deux distributions non monétaires sont reclassées sans changer la richesse à leur date. Les calculs, les 27 écarts de rendement supérieurs à dix points de base entre fournisseurs et leur qualification figurent dans `research/verification_etape_2.md`. Les alertes non résolues ne sont pas déclarées validées.
+
+## VII. Limites de la vérification
+
+La couverture externe reste partielle, notamment sur 79 variations extrêmes anciennes et plusieurs différences de cours entre fournisseurs. Les dates de paiement relèvent d'une convention synthétique déjà écrite ; leur absence n'est pas assimilée à une erreur numérique du moteur. Une scission peut être incorporée dans un cours retraité sans que le moteur reconstruise les titres distribués. La version conservée reste donc une simulation sur séries retraitées, pas un registre certifié de titres détenus.
 
 Le test des fins de série ne mesure pas le biais du survivant. La composition de l'indice et les rapports sont récents, les entreprises sorties du périmètre n'ont pas été recherchées systématiquement. Les niveaux et classements rétrospectifs ne constituent pas une stratégie connue à l'époque.
 
 Yahoo peut réviser son historique lors d'une nouvelle collecte. Les CSV et empreintes fixent un cliché dont les traitements sont reproductibles ; ils ne figent pas la réponse future du fournisseur. Le carnet de collecte est conservé comme trace de démarche, séparément du programme de reconstruction.
 
-## VII. La leçon de méthode conservée
+## VIII. La leçon de méthode conservée
 
-Les premiers contrôles avaient laissé passer des prix absents, une réponse descriptive vide et des instruments homonymes. Je conserve la règle qui en est sortie : vérifier que le résultat attendu est présent, pas seulement qu'une exception n'a pas été levée.
+Les premiers contrôles avaient laissé passer des prix absents, une réponse descriptive vide et des instruments homonymes. La règle qui en est sortie reste utile : vérifier que le résultat attendu est présent, pas seulement qu'une exception n'a pas été levée.
 
 Cette règle vaut aussi pour l'audit. Un moteur qui conserve la richesse peut utiliser le mauvais titre ou le mauvais calendrier de paiement. Un rapprochement SEC stable peut comparer les mauvaises dates de mesure. Un chiffre ancien peut rester dans une note alors que le fichier a changé. Les preuves, les corrections et les limites doivent donc rester attachées aux résultats.

````

### research/master_context.md

````diff
--- avant/research/master_context.md
+++ apres/research/master_context.md
@@ -13,7 +13,7 @@
 
 ## 0. OÙ J'EN SUIS MAINTENANT
 
-L'univers exploratoire de l'étape 1 contient 113 entreprises, 114 titres avec les classes d'Alphabet. L'étape 2 construit dix groupes dans deux modes de gestion. La reconstruction locale et les tests ont été repris le 8 septembre 2026 ; cette étape reste ouverte sur les réserves de données, de paiement des dividendes et d'interprétation décrites dans `research/audit_etape_2.md`. Les règles courantes sont dans `research/portefeuilles.md`, la progression dans `research/plan_projet.md`. Les options pédagogiques anciennes ne remplacent pas ces décisions datées.
+L'univers exploratoire de l'étape 1 contient 113 entreprises, 114 titres avec les classes d'Alphabet. L'étape 2 construit dix groupes dans deux modes de gestion. La reconstruction locale et les tests ont été repris le 8 septembre 2026 ; le complément `research/verification_etape_2.md` documente les cours recoupés, trois erreurs de richesse corrigées et les limites de couverture encore ouvertes. Les conventions synthétiques de paiement et de scission sont distinctes des erreurs de calcul. Les règles courantes sont dans `research/portefeuilles.md`, la progression dans `research/plan_projet.md`. Les options pédagogiques anciennes ne remplacent pas ces décisions datées.
 
 La règle actuelle est la version III de `research/selection_rule.md`. Les résultats se trouvent dans `research/univers_selection.md`, les corrections expliquées dans `research/corrections_2026-09-05.md`, et les chiffres recalculés dans `data/processed/etat_projet.json`.
 

````

### research/plan_projet.md

````diff
--- avant/research/plan_projet.md
+++ apres/research/plan_projet.md
@@ -11,7 +11,7 @@
 | | Étape | État |
 |---|---|---|
 | 1 | Construire un univers d'entreprises exposées à la chaîne des infrastructures de calcul | **close**, version exploratoire |
-| 2 | Construire les portefeuilles à partir de cet univers | en cours, construction rejouée ; réserves de données et de méthode ouvertes |
+| 2 | Construire les portefeuilles à partir de cet univers | construction corrigée et rejouée ; validation des données encore partielle |
 | 3 | Mesurer le risque, ses sources et son comportement en crise | non commencée |
 | 4 | Étudier la couverture et la diversification | non commencée |
 | 5 | Comparer les stratégies, coûts et risque résiduel | non commencée |
@@ -99,7 +99,7 @@
 
 `DUK` reste non confirmé pour une raison réelle : le regroupement de juillet 2012 est simultané à l'absorption de Progress Energy, deux événements que le nombre d'actions ne permet pas de séparer.
 
-Le recoupement externe reste partiel : les distributions de SPY, une de ses clôtures et quatre clôtures de Sandisk ont été rapprochées, mais les historiques des 114 actions et les opérations sur titres ne sont pas tous corroborés. Je garde cette phase ouverte sur cette réserve au lieu d'assimiler présence de contrôles et validation de toute la donnée.
+Le complément du 8 septembre rapproche 103 411 clôtures de 43 titres et documente 34 événements. Les 392 clôtures de Sandisk concordent. Trois erreurs de richesse sont corrigées ; deux distributions sont reclassées. La couverture et les écarts restant non arbitrés sont détaillés dans `research/verification_etape_2.md`. Cette phase reste ouverte sur ces vérifications de données précisément recensées.
 
 ### Phase 3 : Décisions en voyant les données : **close**
 
@@ -255,7 +255,7 @@
 | | Tâche | | État |
 |---|---|---|---|
 | 49 | Proposition des cas qui doivent faire échouer le code | C | `research/cas_de_test.md`, treize cas |
-| 50 | Écriture des tests | C | 41 tests de l'étape 2, 92 tests dans l'ensemble du dépôt |
+| 50 | Écriture des tests | C | 48 tests de l'étape 2, 99 tests dans l'ensemble du dépôt |
 
 Les tests combinent des défauts déjà rencontrés et des contre-exemples construits pour mettre les règles en difficulté. Les exemples courts vérifient la mécanique ; les replays sur le cliché vérifient l'intégration. Aucun ensemble de tests ne garantit l'absence de toute erreur. Les cas et leur couverture sont dans `research/cas_de_test.md`.
 
@@ -305,6 +305,6 @@
 
 ## V. État après l'audit du 8 septembre 2026
 
-L'étape 2 n'est pas déclarée close. Le moteur, ses règles, ses tests et sa reconstruction locale ont été corrigés et rejoués. Les erreurs corrigées, les valeurs actuelles et les preuves sont dans `research/audit_etape_2.md` ; ce rapport prime sur les mesures historiques explicitement datées de ce journal.
-
-Restent ouverts le recoupement des prix et des opérations sur titres au-delà de l'échantillon, la disponibilité effective des dividendes à leur paiement, et la décision de sensibilité aux entrées et à la fréquence de gestion. Les risques, facteurs, stress, diversification et couvertures relèvent des étapes suivantes ; leur absence n'est pas une erreur de construction. Le commit reste une opération de l'auteur, séparée de la validation scientifique.
+La construction de l'étape 2 est corrigée et reproductible. Sa validation de données n'est pas intégrale : le complément `research/verification_etape_2.md` remplace le bilan courant de l'audit initial et recense exactement la couverture, les corrections et les écarts non arbitrés. L'étape n'est pas présentée comme entièrement validée.
+
+La réserve de validation porte sur les cours anciens non corroborés et les différences de fournisseurs recensées dans le complément. Le paiement des dividendes et la conservation juridique des titres sont des limites d'exécution de la convention synthétique retenue. La comparaison des fréquences de gestion relève de l'étape 3 ; elle n'est pas ajoutée aux exigences de construction. Les risques, facteurs, stress, diversification et couvertures relèvent des étapes suivantes ; leur absence n'est pas une erreur de construction. Le commit reste une opération de l'auteur, séparée de la validation scientifique.

````

### research/portefeuilles.md

````diff
--- avant/research/portefeuilles.md
+++ apres/research/portefeuilles.md
@@ -2,45 +2,51 @@
 
 *AI Concentration Risk Research. Tâche 24 de la phase 3. Mise à jour du 8 septembre 2026 après audit.*
 
-Ce document fixe la composition et les règles courantes. Les premières règles ont été écrites avant la construction, mais les données avaient déjà été consultées. Je ne présente donc pas ce document comme un protocole préenregistré à l'aveugle. Les corrections de l'audit sont datées ici et détaillées dans `research/audit_etape_2.md`.
+Ce document fixe la composition et les règles courantes. Les premières règles ont été écrites avant la construction, mais les données avaient déjà été consultées. Il ne s'agit donc pas d'un protocole préenregistré à l'aveugle. Les corrections initiales sont détaillées dans `research/audit_etape_2.md`. Le complément consacré aux prix et aux opérations sur titres figure dans `research/verification_etape_2.md`.
 
 ## I. Règles communes
 
-Je construis dix portefeuilles, chacun dans deux versions. L'équipondération porte sur les entreprises, identifiées par CIK, à la constitution et aux rééquilibrages de la version annuelle. Les poids dérivent entre ces dates. La version conservée n'est pas remise à égalité chaque année.
+L'étude comporte dix portefeuilles, chacun dans deux versions. L'équipondération porte sur les entreprises, identifiées par CIK, à la constitution et aux rééquilibrages de la version annuelle. Les poids dérivent entre ces dates. La version conservée n'est pas remise à égalité chaque année.
 
-La période va de la clôture du 3 janvier 2000 à celle du 4 septembre 2026. Elle contient 6 709 niveaux et 6 708 rendements. L'annualisation conventionnelle utilise 252 séances par an. Le départ est une base nette de constitution : je n'impute pas les frais de la mise initiale, ni ceux d'une liquidation finale. Les rendements sont nominaux, en dollars, avant fiscalité. Les fractions de titres sont autorisées, sans contrainte de taille ni d'impact de marché.
+La période va de la clôture du 3 janvier 2000 à celle du 4 septembre 2026. Elle contient 6 709 niveaux et 6 708 rendements. L'annualisation conventionnelle utilise 252 séances par an. Le départ est une base nette de constitution : les frais de mise initiale et de liquidation finale ne sont pas imputés. Les rendements sont nominaux, en dollars, avant fiscalité. Les fractions de titres sont autorisées, sans contrainte de taille ni d'impact de marché.
 
 Une entreprise entre à la clôture de sa première observation admissible ; son rendement commence à compter à la séance suivante. C'est une règle de disponibilité dans les données, pas la preuve d'une date d'IPO. La composition grandit, de 81 entreprises et 81 titres à 113 entreprises et 114 titres. Elle ne reproduit pas les entrées et sorties historiques du S&P 500.
 
-Alphabet compte pour une entreprise. `GOOGL` désigne la classe A et `GOOG` la classe C. Je retiens la classe C seulement à partir du 3 avril 2014, son historique Yahoo antérieur reprenant celui de la classe A. L'apparition d'une seconde classe partage le montant investi dans l'entreprise entre ses classes disponibles, sans lui attribuer le poids d'une nouvelle entreprise. Les listes ci-dessous nomment l'entreprise ; `appartenance.csv` conserve ses deux titres.
+Alphabet compte pour une entreprise. `GOOGL` désigne la classe A et `GOOG` la classe C. La classe C est retenue seulement à partir du 3 avril 2014, son historique Yahoo antérieur reprenant celui de la classe A. L'apparition d'une seconde classe partage le montant investi dans l'entreprise entre ses classes disponibles, sans lui attribuer le poids d'une nouvelle entreprise. Les listes ci-dessous nomment l'entreprise ; `appartenance.csv` conserve ses deux titres.
 
 Deux autres limites d'historique sont fixées dans `data/review/regles_historiques_prix.csv`, avec leurs sources : `DELL` commence le 26 décembre 2018 pour la classe C, en cotation conditionnelle avant la cotation ordinaire du 28 décembre ; `VRT` commence le 10 février 2020 après le rapprochement de Vertiv et du véhicule coté GSAH. Les segments antérieurs restent dans les fichiers bruts mais ne servent pas à ces portefeuilles. Ces corrections portent sur l'identité du titre ou de l'activité, pas sur les performances obtenues.
 
 Les autres cotations conditionnelles, dites « when-issued », ne sont pas exclues au seul motif qu'elles précèdent la distribution juridique d'une action. Elles peuvent être réelles. Leur négociabilité, leur liquidité et leur coût d'exécution restent une limite du modèle ; le premier cours Yahoo ne prouve pas qu'une opération de n'importe quelle taille était réalisable.
 
-Je sépare les rendements observés, dans `rendements_prix.csv`, de ceux utilisés pour valoriser, dans `rendements_valorisation.csv`. Les séquences initiales sans volume sont exclues. À l'intérieur de l'historique, un cours identique à la veille, avec volume nul et quatre prix identiques, est traité comme suspect. Un volume nul avec des prix variables n'est pas automatiquement effacé. Pendant un trou, je porte le dernier cours connu puis je prends le mouvement cumulé à la reprise. Les 18 observations portées sont signalées dans `qualite_valorisation.csv` : ce ne sont pas des observations de rendement nul utilisables sans réserve pour estimer le risque. Aucun prix n'est porté avant la première observation admissible.
+Les rendements observés figurent dans `rendements_prix.csv` ; ceux qui servent à valoriser les positions figurent dans `rendements_valorisation.csv`. Les séquences initiales sans volume sont exclues. À l'intérieur de l'historique, un cours identique à la veille, avec volume nul et quatre prix identiques, est traité comme suspect. Un volume nul avec des prix variables n'est pas automatiquement effacé. Pendant un trou, le dernier cours connu sert à valoriser la position ; le mouvement cumulé est pris à la reprise. Les 18 observations portées sont signalées dans `qualite_valorisation.csv` : ce ne sont pas des observations de rendement nul utilisables sans réserve pour estimer le risque. Aucun prix n'est porté avant la première observation admissible.
 
 ## II. Les règles de gestion et de comparaison
 
-**Rééquilibrage.** La version annuelle est remise aux poids égaux par entreprise à la première séance de janvier. La version conservée réinvestit seulement les dividendes dans le titre payeur à cette date. Les entrées ont lieu en cours d'année dans les deux versions. Si un titre déjà admis n'a pas de cours utilisable le jour d'une opération, je reporte toute l'opération à la première séance où tous les titres admis sont négociables. Trois reports concernent `P1`, `P2` et `P5`, du 2 au 5 janvier 2015, à cause de la cotation absente d'AMD. Je ne liquide plus implicitement AMD pour toute l'année.
+**Rééquilibrage.** La version annuelle est remise aux poids égaux par entreprise à la première séance de janvier. La version conservée réinvestit seulement les dividendes dans le titre payeur à cette date. Les entrées ont lieu en cours d'année dans les deux versions. Si un titre déjà admis n'a pas de cours utilisable le jour d'une opération, toute l'opération est reportée à la première séance où tous les titres admis sont négociables. Trois reports concernent `P1`, `P2` et `P5`, du 2 au 5 janvier 2015, à cause de la cotation absente d'AMD. Ce report corrige l'ancienne liquidation implicite d'AMD pour toute l'année.
 
 **Entrées.** Une nouvelle entreprise reçoit, après financement, un poids égal à un divisé par le nombre d'entreprises alors détenues, nouvelle comprise. Si plusieurs entrent ensemble, chacune reçoit ce poids. Le financement réduit proportionnellement les positions existantes et leur trésorerie ; hors frais, il ne crée aucune valeur. Les anciens poids conservent leur dérive. Une entrée hors janvier n'est donc pas un rééquilibrage général. Les cibles enregistrées hors janvier sont une référence d'égalité pour l'admission, pas la photographie des poids effectivement détenus.
 
-**Dividendes.** J'utilise `Close` et `Dividends`, pas `Adj Close`, pour les portefeuilles. Sur une position déjà détenue, le rendement de richesse avant frais est la variation du cours plus le dividende, rapportés au cours précédent. Le montant du dividende est comptabilisé au détachement dans une poche attachée au titre et non rémunérée. Il est réinvesti à la date annuelle : suivant les poids cibles dans la version rééquilibrée, dans le titre payeur dans la version conservée.
+**Dividendes.** Le moteur utilise `Close` et les dividendes monétaires, après application des corrections documentées dans `data/review/corrections_evenements_prix.json`. `Adj Close` reste une donnée de contrôle du fournisseur. Sur une position déjà détenue, le rendement de richesse avant frais est la variation du cours plus le dividende, rapportés au cours précédent. Le montant du dividende est comptabilisé au détachement dans une poche attachée au titre et non rémunérée. Il est réinvesti à la date annuelle : suivant les poids cibles dans la version rééquilibrée, dans le titre payeur dans la version conservée.
 
-Cette poche assimile une créance de dividende à des espèces disponibles. Les dates de paiement des actions n'ont pas été collectées. La différence est réelle : les dividendes de décembre de SPY sont payés fin janvier, après notre date de réinvestissement. Je conserve une convention synthétique commune aux portefeuilles et aux fonds de comparaison, mais je ne la présente pas comme un compte espèces strictement réalisable. Un contrôle séparé sur SPY mesure cette approximation dans le rapport d'audit. Il reste à traiter la disponibilité effective des paiements avant de revendiquer une exécution réelle.
+Cette poche assimile une créance de dividende à des espèces disponibles. Les dates de paiement des actions n'ont pas été collectées. La différence est réelle : les dividendes de décembre de SPY sont payés fin janvier, après notre date de réinvestissement. La convention synthétique est commune aux portefeuilles et aux fonds de comparaison. Elle ne décrit pas un compte espèces strictement réalisable. Un contrôle séparé sur SPY mesure cette approximation dans le rapport d'audit. Il reste à traiter la disponibilité effective des paiements avant de revendiquer une exécution réelle.
 
 **Coûts.** Le coût vaut dix points de base sur la somme des achats et des ventes effectivement exécutés, y compris les ventes qui financent une entrée et les achats de réinvestissement des dividendes. Les frais sont financés par le portefeuille ; les cibles sont réduites pour que les achats, ventes, espèces et frais se raccordent exactement. La rotation publiée est la somme de ces montants échangés rapportés à la valeur avant chaque opération, divisée par la durée en années de 252 séances. Elle compte les deux côtés des transactions. Ce taux constant est une hypothèse, pas une mesure de spread ou une garantie de prudence pour toute la période. Les sensibilités à cinq et vingt-cinq points de base figurent dans l'audit.
 
-**Comparaisons.** `SPY` et `RSP` distribuent des dividendes ; leur réinvestissement n'est pas interne au fonds pour le porteur. Je les reconstruis donc avec la même convention de créance, de réinvestissement annuel et de frais que les portefeuilles. Les séries Yahoo ajustées restent séparées dans `valeurs_comparaisons_yahoo.csv`, pour contrôler l'écart de convention. Toute comparaison exigeant `RSP` commence le 1er mai 2003 et utilise une fenêtre commune, sans prolongement antérieur.
+**Comparaisons.** `SPY` et `RSP` distribuent des dividendes ; leur réinvestissement n'est pas interne au fonds pour le porteur. Leur reconstruction applique la même convention de créance, de réinvestissement annuel et de frais que les portefeuilles. Les séries Yahoo ajustées restent séparées dans `valeurs_comparaisons_yahoo.csv`, pour contrôler l'écart de convention. Toute comparaison exigeant `RSP` commence le 1er mai 2003 et utilise une fenêtre commune, sans prolongement antérieur.
 
 Les trois indices collectés servent au contexte et au contrôle. `^SP500TR` est en rendement total ; `^GSPC` et `^SPXEW` sont des indices de prix, sans dividendes. Le dernier comporte des séances absentes. Ils ne doivent pas entrer sans adaptation dans une comparaison de performance totale. Les frais internes et les règles de suivi de SPY et RSP restent différents : leur écart n'identifie pas à lui seul l'effet causal de la concentration.
 
-**Divisions et scissions.** Les cours Yahoo sont déjà retraités des divisions. Je ne multiplie jamais une seconde fois les positions par `Stock Splits`. Cette colonne contient aussi des facteurs de scission. Le moteur suit des montants sur des cours retraités et ne reconstitue pas un registre juridique de parts, de titres distribués, d'échanges et de ventes de droits. C'est une limite de l'interprétation de la version « conservée », à rapprocher des opérations sur titres avant une affirmation d'investissabilité.
+**Divisions et scissions.** Les cours Yahoo sont déjà retraités des divisions : `Stock Splits` ne multiplie pas une seconde fois les positions. Les facteurs de scission décrivent une série synthétique restant investie dans le parent. Les actions distribuées ne sont pas ajoutées au portefeuille en plus de ce retraitement. Leur admission éventuelle dans l'univers, comme celle de Sandisk, est un achat financé distinct. Cette convention n'est pas la conservation juridique de tous les titres reçus.
+
+Le contrôle externe a établi trois erreurs : un retraitement incomplet de Tyco dans JCI au 2 juillet 2007 et deux distributions comptées à nouveau comme espèces, sur Eaton au 2 janvier 2001 et CenterPoint au 1er octobre 2002. Les corrections s'appliquent en mémoire, avant le calcul des rendements. Deux autres distributions, Texas Genco et Adient, sont reclassées en réinvestissement synthétique dans le parent : leur valeur Yahoo est conservée le jour de l'événement, sans prétendre certifier leur prix de liquidation. Les cours bruts et `Adj Close` ne sont pas réécrits.
+
+Les coefficients de scission des fournisseurs peuvent différer selon leurs cours de référence. Le registre `data/review/evenements_prix_documentes.csv` établit la nature des événements ; il ne certifie pas chaque coefficient. Cette approximation reste attachée aux rendements des jours concernés, qui ne doivent pas être interprétés sans contrôle comme des chocs économiques ordinaires.
+
+**Continuité de JCI.** Avant la fusion de 2016, la série utilisée suit Tyco, ancêtre juridique du titre actuel. Elle ne représente pas l'ancienne Johnson Controls Inc. sur toute cette période. Le raccordement juridique et la continuité d'une activité économique ne sont pas la même chose ; le biais rétrospectif de l'univers s'y ajoute.
 
 ## III. Ce que les comparaisons permettent de dire
 
-Les dix portefeuilles sont sélectionnés aujourd'hui avec des informations récentes puis projetés sur le passé. Leur performance absolue, leur classement relatif et leurs mesures de risque peuvent tous être affectés par la connaissance a posteriori et par la sélection des survivants. L'écart avec SPY ne mesure pas la taille de ce biais. Je décris la trajectoire historique de paniers actuels, sans conclure qu'ils étaient identifiables ou investissables à l'époque.
+Les dix portefeuilles sont sélectionnés aujourd'hui avec des informations récentes puis projetés sur le passé. Leur performance absolue, leur classement relatif et leurs mesures de risque peuvent tous être affectés par la connaissance a posteriori et par la sélection des survivants. L'écart avec SPY ne mesure pas la taille de ce biais. Ces résultats décrivent la trajectoire historique de paniers actuels. Ils ne prouvent pas que ces paniers étaient identifiables ou investissables à l'époque.
 
 La différence entre rééquilibrer et conserver combine la dérive des poids, les ventes des gagnants, les achats des perdants, les entrées et les coûts. Elle sert à étudier ces mécanismes ; elle n'isole pas un effet causal pur de la concentration. Cette séparation, les facteurs de marché et les épisodes de crise relèvent de l'étape 3. La comparaison trimestrielle reste à faire.
 
@@ -80,7 +86,7 @@
 
 ## V. La chaîne, sept maillons
 
-Les sept groupes somment exactement à 113. Je donne priorité au champ `canal` : dépenses vers `P4`, ventes vers `P5`. Pour le canal `fournit`, je subdivise ensuite selon le secteur GICS, vers `P6` à `P10`. Ce découpage hybride garde les grands acheteurs ensemble, mais ses groupes restent hétérogènes ; leurs noms ne constituent pas une classification économique indépendante.
+Les sept groupes somment exactement à 113. Le champ `canal` détermine d'abord le groupe : dépenses vers `P4`, ventes vers `P5`. Le canal `fournit` est ensuite subdivisé selon le secteur GICS, vers `P6` à `P10`. Ce découpage hybride garde les grands acheteurs ensemble, mais ses groupes restent hétérogènes ; leurs noms ne constituent pas une classification économique indépendante.
 
 ### P4. Les acheteurs
 
@@ -156,4 +162,4 @@
 
 Réservé. Il sera constitué à la fin du projet, une fois les mesures de risque, de couverture et de coût établies. Rien n'y est inscrit aujourd'hui, et rien ne doit y être inscrit avant que les résultats soient connus.
 
-Sa construction utilisera explicitement les résultats déjà obtenus. Je le présenterai comme une exploration après observation, à valider sur de nouvelles données. Les dix autres portefeuilles ont des règles antérieures à leur construction, ce qui ne suffit pas à certifier un choix à l'aveugle.
+Sa construction utilisera explicitement les résultats déjà obtenus. Ce sera une exploration après observation, à valider sur de nouvelles données. Les dix autres portefeuilles ont des règles antérieures à leur construction, ce qui ne suffit pas à certifier un choix à l'aveugle.

````

### src/construire_portefeuille.ipynb

````diff
--- avant/src/construire_portefeuille.ipynb
+++ apres/src/construire_portefeuille.ipynb
@@ -9,7 +9,7 @@
     "\n",
     "## I. Les règles et le moteur\n",
     "\n",
-    "Je garde ici le déroulé du calcul. Les fonctions sont dans `src/portefeuille.py` et la reconstruction complète dans `src/construire_portefeuilles.py`. Une seule version du moteur produit les valeurs, les poids et les contrôles. Les décisions corrigées le 8 septembre sont datées dans `research/portefeuilles.md`.\n"
+    "Ce notebook présente le déroulé du calcul. Les fonctions sont dans `src/portefeuille.py`, les corrections sourcées dans `src/corrections_prix.py`, et la reconstruction complète dans `src/construire_portefeuilles.py`. Une seule version du moteur produit les valeurs, les poids et les contrôles. Les règles courantes sont dans `research/portefeuilles.md` ; leurs vérifications figurent dans `research/verification_etape_2.md`.\n"
    ]
   },
   {

````

### src/construire_portefeuilles.py

````diff
--- avant/src/construire_portefeuilles.py
+++ apres/src/construire_portefeuilles.py
@@ -18,6 +18,7 @@
 import pandas as pd
 
 from src.portefeuille import COUT, poids_cibles, preparer_prix, simuler
+from src.corrections_prix import corriger_prix, lire_corrections
 
 RACINE = Path(__file__).resolve().parents[1]
 DEBUT = "2000-01-03"
@@ -127,6 +128,8 @@
         raise ValueError("Règles d'historique dupliquées ou hors univers.")
     for regle in regles.itertuples():
         prix[regle.titre] = prix[regle.titre].loc[regle.debut_admissible:]
+    corrections = lire_corrections(racine)
+    prix = {t: corriger_prix(t, p, corrections) for t, p in prix.items()}
     prepares = {t: preparer_prix(p).reindex(dates) for t, p in prix.items()}
     matrices = {champ: pd.DataFrame({t: p[champ] for t, p in prepares.items()}, index=dates)
                 for champ in ["rendement_observe", "rendement_valorisation", "dividende", "disponible", "cours_porte"]}
@@ -140,7 +143,7 @@
         entreprises = groupe.set_index("titre").cik.to_dict()
         evenements, annuel_effectif = set(), set()
         for demande in sorted(annuel | {premiers[t] for t in titres}):
-            # Je ne vends pas un titre à un cours absent. Toute l'opération est
+            # Aucune vente à un cours absent. Toute l'opération est
             # reportée à la première séance où les positions sont négociables.
             effectif = None
             for jour in dates[dates >= demande]:
@@ -257,6 +260,9 @@
             "src/controle_prix.py", "src/construire_portefeuille.ipynb", "src/controler_prix.ipynb",
             "tests/test_portefeuille.py", "tests/test_audit_portefeuilles.py", "research/portefeuilles.md"]]
         sources += sorted((racine / "tests").glob("test_pipeline_portefeuilles.py"))
+        sources += [racine / p for p in ['src/corrections_prix.py',
+            'src/recouper_prix.py', 'data/review/corrections_evenements_prix.json',
+            'tests/test_corrections_prix.py']]
         fichiers = sorted(stage.iterdir())
         manifeste = {"statut": "termine", "produit_le": datetime.now(timezone.utc).isoformat(),
             "python": sys.version.split()[0], "bibliotheques": {p: importlib.metadata.version(p) for p in ["pandas", "numpy"]},

````

### src/corrections_prix.py

````diff
--- avant/src/corrections_prix.py
+++ apres/src/corrections_prix.py
@@ -0,0 +1,39 @@
+"""Corrections sourcées appliquées en mémoire ; les fichiers bruts restent intacts."""
+import json
+import math
+from pathlib import Path
+
+
+def corriger_prix(titre, prix, regles):
+    """Retraite une distribution non monétaire dans les unités du cours.
+
+    Le facteur s'applique strictement avant l'événement, dividendes anciens
+    compris : leurs rendements restent identiques. La distribution reclassée
+    ne rejoint plus les espèces. Adj Close reste la preuve Yahoo originale,
+    inutilisée par le moteur, et n'est pas présenté comme un prix corrigé.
+    Les valeurs témoins empêchent notamment une deuxième application.
+    """
+    p = prix.copy(deep=True)
+    for r in sorted((r for r in regles if r['titre'] == titre), key=lambda r: r['date']):
+        date = r['date']
+        if date not in p.index:
+            raise ValueError(f"Événement correctif absent : {titre} {date}")
+        i = p.index.get_loc(date)
+        if i == 0:
+            raise ValueError(f"Correction sans cours précédent : {titre} {date}")
+        for trouve, attendu in [(p.Close.iloc[i-1], r['close_avant']),
+                                (p.Close.iloc[i], r['close_apres']),
+                                (p.Dividends.iloc[i], r['dividende_brut'])]:
+            if not math.isclose(float(trouve), attendu, rel_tol=0, abs_tol=1e-7):
+                raise ValueError(f"Valeur témoin différente : {titre} {date}")
+        facteur = r['facteur_avant']
+        if not math.isfinite(facteur) or not 0 < facteur <= 1:
+            raise ValueError(f"Facteur correctif invalide : {titre} {date}")
+        cols = ['Open', 'High', 'Low', 'Close', 'Dividends']
+        p.loc[p.index < date, cols] *= facteur
+        p.loc[date, 'Dividends'] = 0.0
+    return p
+
+
+def lire_corrections(racine):
+    return json.loads((Path(racine) / 'data/review/corrections_evenements_prix.json').read_text(encoding='utf-8'))

````

### src/portefeuille.py

````diff
--- avant/src/portefeuille.py
+++ apres/src/portefeuille.py
@@ -67,7 +67,7 @@
     """Finance les frais sur les achats et ventes réellement exécutés.
 
     La cible complète, trésorerie comprise, est réduite proportionnellement.
-    Je résous frais = coût * somme(abs(cible après frais - positions avant)).
+    Le solveur impose frais = coût * somme(abs(cible après frais - positions avant)).
     """
     valeur = float(vise.sum() + cash_vise.sum())
     if valeur <= 0:

````

### src/recouper_prix.py

````diff
--- avant/src/recouper_prix.py
+++ apres/src/recouper_prix.py
@@ -0,0 +1,88 @@
+"""Rejoue hors réseau le rapprochement Yahoo/Nasdaq du 8 septembre 2026.
+
+Exécution : python -m src.recouper_prix
+Une concordance de rendements ne certifie ni les unités historiques ni la
+liquidité. Une réponse vide et une paire de dates différentes restent absentes.
+"""
+from pathlib import Path
+import hashlib
+import json
+import numpy as np
+import pandas as pd
+from src.construire_portefeuilles import lire_prix
+
+ROOT = Path(__file__).resolve().parents[1]
+DOSSIER = Path('data/review/sources_cloture_2026-09-08')
+
+
+def rapprocher(p, n):
+    """Compare seulement deux rendements calculés sur les mêmes deux dates."""
+    if not n.index.is_unique or not n.index.is_monotonic_increasing:
+        raise ValueError('Dates Nasdaq dupliquées ou désordonnées.')
+    if not np.isfinite(n).all() or n.le(0).any():
+        raise ValueError('Cours Nasdaq absent ou invalide.')
+    m = pd.DataFrame({'nasdaq': n, 'yahoo': p.Close, 'split': p['Stock Splits'],
+                      'div': p.Dividends}).loc[n.index.intersection(p.index)].copy()
+    prev_n = pd.Series(n.index, index=n.index).shift()
+    prev_p = pd.Series(p.index, index=p.index).shift()
+    meme_paire = prev_n.reindex(m.index).eq(prev_p.reindex(m.index))
+    m['rn'] = n.pct_change(fill_method=None).reindex(m.index).where(meme_paire)
+    m['ry'] = p.Close.pct_change(fill_method=None).reindex(m.index).where(meme_paire)
+    m['ecart_r'] = m.rn - m.ry
+    m['ratio_prix'] = m.yahoo / m.nasdaq
+    return m
+
+
+def recouper(root=ROOT):
+    root = Path(root)
+    dossier = root / DOSSIER
+    manifeste = json.loads((dossier/'nasdaq_manifest.json').read_text(encoding='utf-8'))
+    rows, couverture = [], []
+    for e in manifeste:
+        f = (root/e['fichier']).resolve()
+        if f.parent != dossier.resolve() or hashlib.sha256(f.read_bytes()).hexdigest() != e['sha256']:
+            raise ValueError(f"Preuve Nasdaq modifiée : {e['titre']}")
+        z = json.loads(f.read_text(encoding='utf-8'))
+        data = z.get('data') or {}
+        lignes = (data.get('tradesTable') or {}).get('rows') or []
+        if not lignes:
+            couverture.append({'titre':e['titre'], 'lignes_nasdaq':0, 'statut':'source_vide'})
+            continue
+        if len(lignes) != int(data['totalRecords']) or data['symbol'] != e['titre']:
+            raise ValueError('Réponse Nasdaq incomplète ou mauvais symbole.')
+        n = pd.DataFrame(lignes)
+        n.index = pd.to_datetime(n.date,format='%m/%d/%Y').dt.strftime('%Y-%m-%d')
+        n = n.sort_index()
+        n['cours'] = n.close.str.replace(r'[$,]','',regex=True).astype(float)
+        t = e['titre']
+        p = lire_prix(root/'data/raw'/('benchmarks' if t in {'SPY','RSP'} else 'prix')/f'{t}.csv')
+        m = rapprocher(p, n.cours)
+        m['titre'] = t
+        rows.append(m.rename_axis('date').reset_index())
+        couverture.append({'titre':t, 'lignes_nasdaq':len(n), 'premiere_date':n.index[0],
+            'derniere_date':n.index[-1], 'lignes_communes':len(m),
+            'rendements_comparables':int(m.ecart_r.notna().sum()),
+            'ecart_r_max':m.ecart_r.abs().max(), 'ecarts_sup_10pb':int(m.ecart_r.abs().gt(.001).sum()),
+            'statut':'couverture_partielle'})
+    a = pd.concat(rows,ignore_index=True)
+    a.to_csv(dossier/'comparaison_cours.csv',index=False)
+    pd.DataFrame(couverture).to_csv(dossier/'couverture.csv',index=False)
+    c = pd.read_csv(root/'data/processed/controle_prix.csv',dtype=str)
+    c = c[(c.test=='variation quotidienne extreme') & (c.date>='2000-01-03')].copy()
+    c['titre'] = c.fichier.str.removesuffix('.csv')
+    c = c.merge(a[['titre','date','nasdaq','yahoo','rn','ry','ecart_r']],on=['titre','date'],how='left')
+    c['statut'] = np.where(c.ecart_r.isna(),'non_corroboré',
+                          np.where(c.ecart_r.abs()<=.001,'rendement_prix_concordant','divergence'))
+    c.loc[(c.titre=='JCI') & (c.date=='2007-07-02'),'statut']='erreur_scission_corrigée_source_SEC'
+    c.to_csv(dossier/'variations_examines.csv',index=False)
+    a[a.ecart_r.abs()>.001].to_csv(dossier/'divergences.csv',index=False)
+    bilan = {'clotures_communes':len(a),'titres':len(couverture),
+             'rendements_comparables':int(a.ecart_r.notna().sum()),
+             'divergences_sup_10pb':int(a.ecart_r.abs().gt(.001).sum()),
+             'variations_extremes':c.statut.value_counts().to_dict(),
+             'limite':'Cours de prix comparés ; conventions de scission, dividendes et identité examinées séparément.'}
+    (dossier/'bilan.json').write_text(json.dumps(bilan,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
+    return bilan
+
+
+if __name__=='__main__':print(json.dumps(recouper(),ensure_ascii=False,indent=2))

````

### tests/test_corrections_prix.py

````diff
--- avant/tests/test_corrections_prix.py
+++ apres/tests/test_corrections_prix.py
@@ -0,0 +1,75 @@
+"""Oracles de richesse distribuée et protection de la preuve brute."""
+from pathlib import Path
+import unittest
+import numpy as np
+import pandas as pd
+from src.corrections_prix import corriger_prix, lire_corrections
+from src.construire_portefeuilles import lire_prix
+from src.portefeuille import preparer_prix
+from src.recouper_prix import rapprocher
+
+ROOT = Path(__file__).resolve().parents[1]
+
+
+class CorrectionsEvenementsTests(unittest.TestCase):
+    def test_comparaison_refuse_le_faux_quotidien_sur_dates_absentes(self):
+        p=pd.DataFrame({'Close':[100.,110.,121.],'Dividends':0.,'Stock Splits':0.},index=['2020-01-02','2020-01-03','2020-01-06'])
+        n=pd.Series([100.,121.],index=['2020-01-02','2020-01-06'])
+        self.assertTrue(rapprocher(p,n).ecart_r.isna().all())
+
+    def test_comparaison_detecte_un_cours_stale(self):
+        p=pd.DataFrame({'Close':[100.,110.],'Dividends':0.,'Stock Splits':0.},index=['2020-01-02','2020-01-03'])
+        n=pd.Series([100.,100.],index=p.index)
+        self.assertAlmostEqual(rapprocher(p,n).ecart_r.iloc[-1],-.1)
+
+    def test_tyco_valeur_des_trois_societes(self):
+        p = lire_prix(ROOT/'data/raw/prix/JCI.csv')
+        avant = p.copy(deep=True)
+        regle = [r for r in lire_corrections(ROOT) if r['titre']=='JCI' and r['date']=='2007-07-02']
+        q = corriger_prix('JCI', p, regle)
+        pp = preparer_prix(q)
+        # Un lot de quatre anciennes actions donne un titre de chaque société.
+        conversion_unites = p.loc['2007-07-02','Close'] / 53.36
+        richesse_lot = (53.36 + 39.97 + 43.41) * conversion_unites
+        attendu = richesse_lot / p.loc['2007-06-29','Close'] - 1
+        self.assertAlmostEqual(pp.loc['2007-07-02','rendement_valorisation'], attendu, places=13)
+        self.assertEqual(pp.loc['2007-07-02','dividende'], 0)
+        pd.testing.assert_frame_equal(p, avant)
+        pd.testing.assert_series_equal(q['Adj Close'], p['Adj Close'])
+
+    def test_rendements_hors_evenements_invariants(self):
+        regles = lire_corrections(ROOT)
+        for t in {r['titre'] for r in regles}:
+            with self.subTest(titre=t):
+                p = lire_prix(ROOT/f'data/raw/prix/{t}.csv')
+                a, b = preparer_prix(p), preparer_prix(corriger_prix(t,p,regles))
+                masque = ~p.index.isin([r['date'] for r in regles if r['titre']==t])
+                for col in ['rendement_valorisation','dividende']:
+                    np.testing.assert_allclose(a.loc[masque,col], b.loc[masque,col], atol=1e-14, rtol=1e-12, equal_nan=True)
+
+    def test_doubles_comptes_supprimes_sans_deuxieme_split(self):
+        for t,date in [('ETN','2001-01-02'),('CNP','2002-10-01')]:
+            p = lire_prix(ROOT/f'data/raw/prix/{t}.csv')
+            regles = [r for r in lire_corrections(ROOT) if r['titre']==t and r['date']==date]
+            q = corriger_prix(t,p,regles)
+            pd.testing.assert_series_equal(p.Close,q.Close)
+            self.assertEqual(q.loc[date,'Dividends'],0)
+
+    def test_reclassement_conserve_la_richesse_du_jour(self):
+        for r in lire_corrections(ROOT):
+            if r['statut']!='convention_non_monetaire':continue
+            p=lire_prix(ROOT/f"data/raw/prix/{r['titre']}.csv")
+            q=corriger_prix(r['titre'],p,[r]);jour=r['date']
+            a,b=preparer_prix(p),preparer_prix(q)
+            self.assertAlmostEqual(a.loc[jour,'rendement_valorisation']+a.loc[jour,'dividende'],b.loc[jour,'rendement_valorisation'],places=13)
+
+    def test_double_application_ou_cliche_modifie_refuse(self):
+        regles=lire_corrections(ROOT)
+        p=lire_prix(ROOT/'data/raw/prix/JCI.csv')
+        q=corriger_prix('JCI',p,regles)
+        with self.assertRaises(ValueError):corriger_prix('JCI',q,regles)
+        p.loc['2007-07-02','Close']+=.01
+        with self.assertRaises(ValueError):corriger_prix('JCI',p,regles)
+
+
+if __name__=='__main__':unittest.main()

````
