# Vérification complémentaire de l'étape 2

*AI Concentration Risk Research. 8 septembre 2026. Complément postérieur à l'audit de deux heures.*

## I. Conclusion et périmètre

Trois erreurs de richesse sont corrigées. Deux distributions non monétaires sont reclassées pour rendre leur traitement cohérent avec les séries synthétiques. Les vingt portefeuilles sont recalculés avec les mêmes groupes, la même période et les mêmes règles d'admission. Le rapprochement externe couvre 103 411 clôtures de 43 titres.

**La construction est corrigée et reproductible ; la validation complète des prix n'est pas acquise.** Parmi les 98 variations extrêmes de la période utilisée, 18 rendements de prix concordent avec Nasdaq et un événement est corrigé sur pièce SEC. Les 79 autres n'ont pas de corroboration indépendante chiffrée dans ce complément. Neuf écarts quotidiens entre fournisseurs restent non arbitrés, dont certains sont les deux faces d'une même différence de clôture. Les appeler des erreurs Yahoo serait aussi injustifié que les déclarer validés.

Ce bilan termine le contrôle complémentaire effectué ; il ne vaut pas certification de l'ensemble des observations. Les résultats permettent des explorations sous ces réserves. Une conclusion de risque reposant sur les extrêmes non corroborés ou sur les rendements de scission devra traiter ces observations explicitement. Aucun nouveau tour général d'audit n'est proposé ici : les réserves portent sur des lignes recensées dans les annexes.

Le contrôle ne recommence pas la sélection de l'étape 1, ne construit pas de capitalisations et ne commence ni l'attribution du risque ni les couvertures. Les données brutes sont conservées. Les différences économiques sont mesurées contre le cliché local sauvegardé au début de ce complément, et non contre un commit supposé sur GitHub.

## II. Les erreurs confirmées et leur correction

### A. Tyco dans JCI : une distribution de deux sociétés était perdue

Le 2 juillet 2007, la série `data/raw/prix/JCI.csv` passe de 70.3539657593 à 27.7751369476 dans ses unités retraitées. Elle porte aussi 10.691554 dans `Dividends` et 0.25 dans `Stock Splits`. Le moteur avait appliqué ces données telles quelles. La richesse calculée par `(Close + Dividends) / Close précédent − 1` chutait donc artificiellement.

Le [document fiscal de Tyco déposé à la SEC](https://www.sec.gov/Archives/edgar/data/833444/000110465907052190/a07-17393_3ex99d1.htm), daté du 3 juillet 2007, établit les titres distribués et les clôtures de la première séance : après regroupement, un lot donne une action Tyco à 53.36 dollars, une Tyco Electronics à 39.97 et une Covidien à 43.41. La richesse du lot est 136.74 dollars. La conversion vers les unités du fichier vaut `27.7751369476 / 53.36`. Le rendement économique de l'événement est donc `136.74 × conversion / 70.3539657593 − 1`.

La correction applique strictement avant l'événement le facteur `53.36 / 136.74 = 0.3902296328799181` aux cours OHLC et aux anciens dividendes. Le pseudo-dividende du jour est retiré des espèces. Cette opération traduit un réinvestissement synthétique de la distribution dans le parent. Elle ne remet pas une deuxième fois le regroupement 1 pour 4 dans les positions. Les rendements et rendements de dividendes des autres jours restent identiques à la précision numérique.

**Origine de l'erreur :** confondre une colonne événementielle du fournisseur avec une série homogène de versements monétaires. La cohérence entre `Close`, `Dividends` et `Adj Close` validait la formule Yahoo, tout en laissant passer une richesse fausse.

### B. Eaton : la scission Axcelis était comptée une seconde fois en espèces

Au 2 janvier 2001, `data/raw/prix/ETN.csv` contient déjà le facteur de scission 1.1524720526, mais ajoute 2.616 dans `Dividends`. La [SEC](https://www.sec.gov/Archives/edgar/data/1113232/000111323201500010/form10q.htm) documente une distribution de 1.179023 action Axcelis par action Eaton. La [FAQ d'Axcelis](https://investor.axcelis.com/shareholder-services/investor-faqs) donne l'ouverture d'Eaton à 65.25 dollars et l'allocation de valeur entre les sociétés. Après les deux divisions ultérieures, `65.25 / 4 = 16.3125`, exactement l'ouverture du fichier : le cours est celui du parent après séparation, déjà raccordé par son facteur de scission.

La correction retire 2.616 des espèces au 2 janvier. Le prix et son facteur sont conservés. Le facteur historique reste une approximation de fournisseur fondée sur des prix de référence ; sa conservation ne certifie pas un registre d'actions liquidées à la clôture. **L'erreur corrigée est le double compte**, pas la promesse d'un coefficient d'exécution exact.

### C. CenterPoint : des actions Reliant Resources avaient été prises pour des dollars

Au 1er octobre 2002, `data/raw/prix/CNP.csv` porte un facteur de scission 1.18624 et un pseudo-dividende de 0.843. Le [communiqué de Reliant](https://investors.centerpointenergy.com/news-releases/news-release-details/reliant-energy-establishes-distribution-ratio) établit une distribution de 0.788603 action Reliant Resources par action du parent, et non un versement monétaire de ce montant. Le retraitement du cours incorpore déjà la scission.

La correction supprime le second versement en espèces, tout en conservant le facteur de prix du fournisseur. Comme pour Eaton, le double compte est corrigé ; le détail du prix de liquidation de chaque titre reçu n'est pas reconstruit.

### D. Deux reclassements de convention, distincts des trois erreurs

La distribution de Texas Genco aux porteurs CenterPoint, visible au 7 janvier 2003, et celle d'Adient aux porteurs JCI, au 31 octobre 2016, figurent chez Yahoo dans `Dividends`, sans facteur de scission correspondant. Leur nature en titres est documentée par [CenterPoint/SEC](https://www.sec.gov/Archives/edgar/data/1188303/000119312504152157/dprem14c.htm) et [Adient](https://investors.adient.com/news-releases/2016/10-31-2016).

Les équivalents Yahoo de 0.493 et 4.7 sont conservés mais réinvestis synthétiquement dans le parent au détachement. Le facteur appliqué aux valeurs antérieures est `Close / (Close + distribution)`. La richesse de la séance reste identique ; la trajectoire suivante change parce que ce montant ne reste plus en espèces jusqu'au janvier suivant. Il s'agit d'une convention explicitée et testée, **pas d'une nouvelle certification indépendante des montants de 0.493 et 4.7**.

Les réinvestissements implicites des scissions ne déclenchent pas de frais spécifiques dans ces séries synthétiques. Les frais du moteur portent sur les transactions de son calendrier de gestion. Cette distinction fait partie de la limite d'exécution ; la valeur obtenue n'est pas celle d'un compte réalisant chaque vente de titres distribués.

### E. Mesure exacte des effets au jour de l'événement

| Titre | Date | Ligne brute | Richesse avant | Richesse après | Statut |
|---|---|---|---|---|---|
| JCI | 2007-07-02 | 4985 | -45.324062 % | +1.168982 % | erreur_confirmee |
| ETN | 2001-01-02 | 7224 | +19.215627 % | +3.176434 % | erreur_confirmee |
| CNP | 2002-10-01 | 10259 | +16.052394 % | +6.062383 % | erreur_confirmee |
| CNP | 2003-01-07 | 10326 | +0.035090 % | +0.035090 % | convention_non_monetaire |
| JCI | 2016-10-31 | 7336 | +2.879345 % | +2.879345 % | convention_non_monetaire |

Les lignes renvoient aux CSV bruts, en comptant leur en-tête. Les corrections figurent dans `data/review/corrections_evenements_prix.json` ; `src/corrections_prix.py` les applique en mémoire avant `preparer_prix`. Des valeurs témoins font échouer une double application ou un changement inattendu du cliché. `Adj Close` reste la preuve originale Yahoo, inutilisée dans ces calculs corrigés.

## III. Le recoupement des cours

### A. Couverture et méthode

L'API publique Nasdaq a livré 43 historiques, archivés avec leur URL et leur empreinte. Ils comprennent 41 actions et les fonds SPY et RSP. Les dates réellement reçues priment sur la date de début demandée à l'API. La plupart des réponses commencent en septembre 2016 ; Coherent commence plus tard et l'historique Sandisk est entièrement couvert depuis février 2025. Une réponse de 2 514 lignes à une demande depuis 2000 n'est donc pas une couverture depuis 2000.

La comparaison porte sur **103 411 clôtures communes et 103 368 rendements calculés sur les mêmes deux dates**. Les prix ajustés pour des divisions futures peuvent avoir des unités différentes entre fournisseurs : les niveaux ne sont pas comparés aveuglément. Le rendement de prix et le rapport entre les niveaux sont conservés. Un dividende n'est pas ajouté à la série Nasdaq pour prétendre en avoir vérifié le rendement total. Le seuil de revue des écarts quotidiens est dix points de base ; il ne signifie pas que les différences plus petites valent zéro.

Les 392 clôtures de Sandisk concordent, avec un écart maximal de rendement de prix de l'ordre de 1.1 × 10⁻⁷. Cela renforce le constat sur l'historique depuis la séparation, y compris le départ conditionnel à 36 dollars et la clôture finale à 1 740 dollars. La sensibilité au choix de première admission reste distincte de l'exactitude des cours.

Les fichiers `couverture.csv`, `comparaison_cours.csv`, `variations_examines.csv` et `divergences_qualifiees.csv` rendent le contrôle vérifiable. `python -m src.recouper_prix` le rejoue localement et refuse une empreinte Nasdaq modifiée. Les sources vides, dates absentes, divergences et concordances restent des statuts différents.

### B. Les vingt-sept divergences supérieures au seuil

| titre | date | nasdaq | yahoo | ecart_r | qualification |
|---|---|---|---|---|---|
| DELL | 2018-12-21 | 21.4289 | 28.83051872253418 | -562.40 pb | hors rendement détenu : segment exclu ou jour de première admission |
| DELL | 2018-12-24 | 21.4289 | 22.59181022644043 | +2163.93 pb | hors rendement détenu : segment exclu ou jour de première admission |
| DELL | 2018-12-26 | 22.8195 | 22.768617630004883 | +570.67 pb | hors rendement détenu : segment exclu ou jour de première admission |
| DELL | 2018-12-27 | 22.662 | 22.451488494873047 | +70.26 pb | différence de cours non arbitrée ; prix Yahoo conservé, aucune preuve de remplacement |
| DELL | 2018-12-28 | 23.0837 | 23.025848388671875 | -69.74 pb | différence de cours non arbitrée ; prix Yahoo conservé, aucune preuve de remplacement |
| DELL | 2019-08-13 | 25.1619 | 25.098833084106445 | -10.10 pb | différence de cours non arbitrée ; prix Yahoo conservé, aucune preuve de remplacement |
| DELL | 2021-11-02 | 54.61 | 54.61000061035156 | -24.22 pb | opération non monétaire documentée ; coefficients de fournisseurs différents |
| DTE | 2021-07-01 | 111.88 | 111.87999725341795 | -91.33 pb | opération non monétaire documentée ; coefficients de fournisseurs différents |
| FLEX | 2024-01-02 | 21.2682 | 22.833459854125977 | -348.39 pb | veille de scission ; convention de retraitement différente |
| FLEX | 2024-01-03 | 23.74 | 23.739999771118164 | +765.18 pb | opération non monétaire documentée ; coefficients de fournisseurs différents |
| HPE | 2017-04-03 | 13.7466 | 13.63072109222412 | -134.48 pb | opération non monétaire documentée ; coefficients de fournisseurs différents |
| HPE | 2017-09-01 | 14.31 | 14.3100004196167 | -86.12 pb | opération non monétaire documentée ; coefficients de fournisseurs différents |
| IBM | 2021-11-04 | 120.85 | 120.8499984741211 | -122.08 pb | opération non monétaire documentée ; coefficients de fournisseurs différents |
| JCI | 2016-10-31 | 40.32 | 40.31999969482422 | +1048.26 pb | Adient ; Nasdaq ajuste le prix, Yahoo encode une distribution reclassée |
| MMM | 2024-04-01 | 94.02 | 94.0199966430664 | -275.10 pb | opération non monétaire documentée ; coefficients de fournisseurs différents |
| O | 2021-11-15 | 71.14 | 71.13999938964844 | -125.23 pb | opération non monétaire documentée ; coefficients de fournisseurs différents |
| SMCI | 2019-10-11 | 1.876 | 1.8910000324249268 | -78.95 pb | différence de cours non arbitrée ; prix Yahoo conservé, aucune preuve de remplacement |
| SMCI | 2019-10-14 | 1.875 | 1.875 | +79.28 pb | différence de cours non arbitrée ; prix Yahoo conservé, aucune preuve de remplacement |
| SMCI | 2020-01-14 | 2.7 | 2.7720000743865967 | -252.54 pb | différence de cours non arbitrée ; prix Yahoo conservé, aucune preuve de remplacement |
| SMCI | 2020-01-15 | 2.77 | 2.7699999809265137 | +266.47 pb | différence de cours non arbitrée ; prix Yahoo conservé, aucune preuve de remplacement |
| SPY | 2026-04-20 | 710.14 | 708.719970703125 | +20.00 pb | Yahoo corroboré par Finviz et FinancialContent ; Nasdaq divergent |
| SPY | 2026-04-21 | 704.08 | 704.0800170898438 | -19.87 pb | Yahoo corroboré par Finviz et FinancialContent ; Nasdaq divergent |
| VRT | 2019-08-12 | 10.23 | 10.1899995803833 | +39.25 pb | hors rendement détenu : segment exclu ou jour de première admission |
| VRT | 2019-08-13 | 10.23 | 10.229999542236328 | -39.25 pb | hors rendement détenu : segment exclu ou jour de première admission |
| VRT | 2023-02-16 | 16.03 | 16.149999618530273 | -74.67 pb | différence de cours non arbitrée ; prix Yahoo conservé, aucune preuve de remplacement |
| VRT | 2023-02-17 | 16.06 | 16.059999465942383 | +74.44 pb | différence de cours non arbitrée ; prix Yahoo conservé, aucune preuve de remplacement |
| WDC | 2025-02-24 | 49.02 | 49.02000045776367 | -121.10 pb | opération non monétaire documentée ; coefficients de fournisseurs différents |

Cinq lignes ne correspondent pas à un rendement porté par une position détenue : anciennes séries exclues de DELL/VRT ou jour d'admission. Onze lignes touchent une opération non monétaire ou sa veille. Pour ces lignes, le rapprochement identifie la différence de traitement sans certifier le coefficient de l'un des fournisseurs. Deux lignes concernent SPY : Nasdaq reprend 710.14 au 20 avril 2026, tandis que Yahoo donne 708.72, corroboré par [Finviz](https://finviz.com/quote?bd=bd-map&e=2026-04-20&ov=chain_date&p=d&t=SPY&ta=1&tt=tt-table&ty=oc) et [FinancialContent](https://markets.financialcontent.com/postgazette/quote/historical?Symbol=NY%3ASPY). Le cours Yahoo est conservé.

Les neuf lignes restantes sont des divergences de cours non arbitrées, surtout autour de quelques clôtures de DELL, SMCI et VRT. Elles ne sont pas corrigées par préférence automatique pour Nasdaq. Les valeurs source restent visibles dans le tableau ; une différence au jour t peut produire un écart inverse au jour t+1. Neuf rendements divergents ne signifient donc pas neuf prix faux indépendants.

### C. Les variations anciennes

Le contrôle brut signale 127 variations ajustées supérieures à 30 % sur tous les historiques, dont 98 depuis 2000 et après admission dans les portefeuilles concernés. La comparaison Nasdaq en couvre 18. La pièce SEC résout JCI en 2007. Les **79 autres restent non corroborées** dans ce contrôle chiffré. Des articles anciens peuvent en expliquer le contexte ; cela ne reconstitue pas automatiquement leurs deux cours de clôture.

Les accès testés à des historiques publics plus anciens n'ont pas fourni une couverture exploitable et homogène : Nasdaq renvoie zéro ligne sur certaines fenêtres de 2007 ; Stooq présente une page de contrôle d'accès ; le connecteur Financial Datasets annonce un solde nul. Aucune réponse vide n'est comptée comme un succès, aucun service payant n'a été souscrit, et les séries Yahoo n'ont pas été effacées pour faire disparaître ces alertes.

## IV. Les opérations et les continuités historiques

Le registre `data/review/evenements_prix_documentes.csv` contient 34 lignes. Les 29 premiers cas couvrent exactement les 20 rapprochements SEC incompatibles et les 9 cas sans encadrement exploitable. Les 5 autres décrivent les corrections et reclassements ci-dessus. **La nature d'une opération est distinguée de son coefficient de prix.**

| titre | date | facteur_yahoo | nature | source |
|---|---|---|---|---|
| BRK-B | 2010-01-21 | 50.0 | division 50 pour 1 de la classe B | https://berkshirehathaway.com/news/jan2010.pdf |
| DOV | 2014-03-03 | 1.205 | scission Knowles | https://investor.knowles.com/news/news-details/2014/Knowles-Corporation-Debuts-as-Independent-Public-Company-Following-Spin-Off-from-Dover-Corporation-03-03-2014/default.aspx |
| DOV | 2018-05-09 | 1.238 | scission Apergy | https://www.sec.gov/Archives/edgar/data/29905/000002990518000043/a2018063010-q.htm |
| DTE | 2021-07-01 | 1.175 | scission DT Midstream, 0.5 action distribuée | https://www.dteenergy.com/us/en/newsroom/2021/DTE-Energy-Completes-Spin-Off-of-DT-Midstream.html |
| DUK | 2012-07-03 | 0.3333333333333333 | regroupement 1 pour 3 et fusion Progress Energy | https://news.duke-energy.com/releases/duke-energy-progress-energy-complete-merger |
| FLEX | 2024-01-03 | 1.327 | scission Nextracker, 0.174185 action distribuée | https://www.nasdaqtrader.com/TraderNews.aspx?id=ECA2023-752 |
| HPE | 2017-04-03 | 1.3348 | scission Enterprise Services et fusion CSC donnant DXC | https://www.sec.gov/Archives/edgar/data/1688568/000119312517112036/d250548d8k.htm |
| HPE | 2017-09-01 | 1.289 | scission logiciels et Micro Focus, 0.13732611 ADS | https://investors.hpe.com/~/media/Files/H/HP-Enterprise-IR/documents/hpe-fy2017-form-10k.pdf |
| IBM | 2021-11-04 | 1.046 | scission Kyndryl, 0.2 action distribuée | https://www.ibm.com/investor/services/faqs-about-the-kyndryl-holdings-inc-distribution |
| IRM | 2014-09-26 | 1.082 | distribution exceptionnelle mixte liée à la conversion REIT, paiement le 4 novembre | https://investors.ironmountain.com/news/news-details/2014/Iron-Mountain-Announces-Results-of-the-Special-Distribution/default.aspx |
| JCI | 2012-10-01 | 2.011667672500503 | scissions Tyco ADT et Flow Control fusionné avec Pentair | https://www.sec.gov/Archives/edgar/vprr/1300/13000220.pdf |
| JCI | 2016-09-06 | 0.955 | fusion Tyco Johnson Controls, 0.955 action par ancienne action Tyco | https://www.sec.gov/Archives/edgar/data/833444/000083344417000007/q1fy1710-q.htm |
| MMM | 2024-04-01 | 1.196 | scission Solventum, 0.25 action distribuée | https://investors.3m.com/financials/sec-filings/content/0000066740-24-000044/mmm-20240401.htm |
| NI | 2015-07-02 | 2.545 | scission Columbia Pipeline, distribution le 1er juillet à 23h59 puis cotation le 2 | https://www.prnewswire.com/news-releases/nisource-columbia-pipeline-group-complete-separation-300107971.html |
| O | 2021-11-15 | 1.032 | scission Orion après rapprochement VEREIT | https://www.realtyincome.com/investors/press-releases/realty-income-completes-spin-orion-office-reit |
| PPL | 2015-06-02 | 1.0736525660296328 | scission Talen, 0.124906 action, clôtures PPL 31.81 et Talen 18.76 | https://www.pplweb.com/wp-content/uploads/2015/06/PPL-Form-8397-Signed-v6-Talen-website-addition-2015-06-04.pdf |
| TT | 2013-12-02 | 1.252 | scission Allegion depuis Ingersoll Rand | https://www.allegion.com/corp/en/news/year/2013/allegion-debuts-as-public-company2.html |
| TT | 2020-03-02 | 1.289 | scission industrielle et fusion Gardner Denver, 0.8824 action distribuée | https://investors.tranetechnologies.com/news-and-events/news-releases/news-release-details/2020/Trane-Technologies-Completes-Reverse-Morris-Trust-Transaction-and-Begins-Trading-Today-on-NYSE/default.aspx |
| WDC | 2025-02-24 | 1.323 | scission Sandisk | https://investor.wdc.com/static-files/ccceedf3-a9ac-4a5b-9306-f177c9389399 |
| WMB | 2012-01-03 | 1.2266928361138372 | scission WPX, un tiers d’action distribué | https://investor.williams.com/stock-information/dividend-history |
| APH | 2026-09-03 | 2.0 | division 2 pour 1, distribution le 2 septembre | https://www.sec.gov/Archives/edgar/data/820313/000110465926091969/tm2622441d1_8k.htm |
| DELL | 2018-12-28 | 1.806 | échange classe V vers classe C, ratio 1.8066 et option espèces, pas une division de classe C | https://www.prnewswire.com/news-releases/dell-technologies-completes-class-v-transaction-300771234.html |
| DELL | 2021-11-02 | 1.973 | scission VMware, les espèces spéciales de VMware reviennent d’abord à Dell et servent à réduire sa dette | https://www.sec.gov/Archives/edgar/data/1571996/000157199621000063/dell-20211029.htm |
| ETN | 2011-03-01 | 2.0 | division 2 pour 1, actions distribuées le 28 février | https://www.sec.gov/Archives/edgar/data/31277/000115752311000401/a6586529ex99.htm |
| GOOG | 2014-03-27 | 2.002 | date d’enregistrement de la distribution de classe C ; segment exclu avant le 3 avril | https://www.sec.gov/Archives/edgar/data/1288776/000128877615000021/googq12015exhibit991.htm |
| GOOG | 2015-04-27 | 1.0027455 | ajustement compensatoire en classe C, nature documentée, date précise et coefficient non corroborés par cette pièce | https://www.sec.gov/Archives/edgar/data/1288776/000128877615000021/googq12015exhibit991.htm |
| GOOG | 2022-07-18 | 20.0 | division 20 pour 1 | https://www.eurex.com/ex-en/rules-regs/corporate-actions/corporate-action-information/Alphabet-Inc.-Stock-Split-3112924 |
| GOOGL | 2014-04-03 | 1.998 | distribution de la classe C aux porteurs A et B | https://www.sec.gov/Archives/edgar/data/1288776/000128877615000021/googq12015exhibit991.htm |
| GOOGL | 2022-07-18 | 20.0 | division 20 pour 1 | https://www.miaxglobal.com/sites/default/files/alert-files/GOOGL_Split__50542.pdf |

NiSource illustre un faux positif écarté : la distribution juridique est achevée le 1er juillet 2015 à 23 h 59 et le marché ordinaire commence le 2 juillet. La date Yahoo du 2 juillet ne doit pas être décalée simplement parce qu'un rapport annuel résume l'opération au 1er. Pour GOOG au 27 avril 2015, la pièce consultée confirme la compensation en actions de classe C, mais ne suffit pas à corroborer la date de marché et le facteur précis ; cette restriction est écrite dans le registre.

Les nombres d'actions SEC ne sont pas utilisés comme pondérations. Le facteur 1.806 de DELL en décembre 2018 décrit un raccordement avec l'ancienne classe V ; l'annonce finale porte 1.8066. Il ne s'agit pas d'une division de la classe C à appliquer aux positions déjà constituées. Le moteur n'applique pas ce facteur une seconde fois. Les différences de cours autour des cotations conditionnelles restent recensées dans la comparaison Nasdaq.

Pour JCI, l'histoire antérieure à la fusion de 2016 suit Tyco. Les anciens comptes de Johnson Controls et l'ancien historique de marché de Tyco ne sont pas interchangeables. La règle de portefeuille décrit désormais cette continuité sans prétendre que l'activité actuelle existait à l'identique sur toute la période.

## V. Les vingt résultats recalculés

| Série | Base 100 avant | Base 100 après | Annualisation après | Écart annualisé |
|---|---|---|---|---|
| P1_reeq | 9057.00 | 9066.92 | 18.4503 % | +0.487 pb |
| P1_cons | 11043.61 | 11029.56 | 19.3254 % | -0.571 pb |
| P10_reeq | 3849.92 | 3849.92 | 14.6993 % | +0.000 pb |
| P10_cons | 6239.95 | 6239.95 | 16.7992 % | +0.000 pb |
| P2_reeq | 10310.31 | 10327.62 | 19.0310 % | +0.750 pb |
| P2_cons | 12033.25 | 12016.91 | 19.7104 % | -0.611 pb |
| P3_reeq | 2968.24 | 2963.15 | 13.5768 % | -0.733 pb |
| P3_cons | 4785.09 | 4781.46 | 15.6368 % | -0.330 pb |
| P4_reeq | 14065.19 | 14065.19 | 20.4203 % | +0.000 pb |
| P4_cons | 6679.44 | 6679.44 | 17.0982 % | +0.000 pb |
| P5_reeq | 16006.49 | 16006.49 | 21.0066 % | +0.000 pb |
| P5_cons | 27343.23 | 27343.23 | 23.4654 % | +0.000 pb |
| P6_reeq | 1954.11 | 1950.58 | 11.8067 % | -0.760 pb |
| P6_cons | 1804.25 | 1800.61 | 11.4711 % | -0.844 pb |
| P7_reeq | 9725.85 | 9810.42 | 18.8015 % | +3.863 pb |
| P7_cons | 9078.74 | 9044.53 | 18.4393 % | -1.680 pb |
| P8_reeq | 6360.14 | 6360.14 | 16.8829 % | +0.000 pb |
| P8_cons | 2597.83 | 2597.83 | 13.0167 % | +0.000 pb |
| P9_reeq | 2707.97 | 2707.97 | 13.1932 % | +0.000 pb |
| P9_cons | 2397.55 | 2397.55 | 12.6766 % | +0.000 pb |

Les groupes, la période et le nombre de titres n'ont pas changé. Les seuls écarts économiques viennent des événements corrigés ou reclassés. Les dix séries de P4, P5, P8, P9 et P10 ne changent pas. Les effets positifs et négatifs peuvent se compenser dans un panier : une faible différence finale ne rend pas les erreurs individuelles négligeables, notamment pour une future étude des queues de distribution.

## VI. Vérifications du code et portée du résultat

La suite complète compte 99 tests, dont 7 ajoutés pour les corrections et le rapprochement. Les cas nouveaux contrôlent la richesse du lot Tyco à partir des trois clôtures SEC, l'invariance des autres rendements, la suppression des doubles comptes, la conservation de richesse lors des reclassements, le refus d'une double application, les dates manquantes entre deux sources et la détection d'un cours repris de la veille.

Les vingt séries contiennent 6709 niveaux, soit 6708 rendements. Les 225 984 poids mensuels somment à un avec un écart maximal de 4.44e-16. L'identité quotidienne entre richesse, rendements des positions, distributions et frais présente un écart maximal de 7.39e-16. Les 18 cours portés restent identifiés. Ces identités prouvent la mécanique du compte ; elles ne prouvent pas chaque cours de marché.

Commandes locales de reproduction :

```powershell
python -B -m src.recouper_prix
python -B -m unittest discover -s tests
python -B -m src.construire_portefeuilles
python -B -m src.construire_portefeuilles --check-only
```

Le rejeu des quatre cellules de code du notebook sous Python 3.12.14 retrouve à l'octet les 18 sorties produites par la commande sous Python 3.13.9. Le contrôle final des empreintes confirme que les 2 646 fichiers bruts protégés et les 11 sorties du manifeste de l'étape 1 sont inchangés. Le contrôle `--check-only` de l'étape 2 passe également.

Le journal `research/journal_verification_etape_2.md` donne l'inventaire des modifications, les empreintes et les résultats des contrôles finaux. Le rapport initial `research/audit_etape_2.md` conserve ses valeurs et différences historiques ; son en-tête renvoie à ce complément. Aucun commit ni envoi GitHub n'est effectué par ce contrôle.

## VII. Ce qui est une limite, ce qui reste une réserve de données

Le paiement au détachement, les fractions de titres, les frais constants, le réinvestissement synthétique des distributions non monétaires et l'univers choisi rétrospectivement sont des limites écrites du modèle. Ils ne deviennent pas des contrôles manquants à ajouter indéfiniment à l'étape 2. Le calcul d'un compte exécutable demanderait un autre périmètre.

Les 79 variations non corroborées, les 9 divergences quotidiennes non arbitrées et les différences de coefficients de scission sont en revanche des réserves sur les données. Leur liste est finie et jointe. Elles empêchent une affirmation de validation intégrale. Elles n'autorisent ni l'effacement des observations, ni une conclusion selon laquelle tous les prix seraient faux.

Les attributions de risque, sensibilités aux fréquences de gestion, crises, corrélations, facteurs et couvertures sont les travaux des étapes suivantes. Leur absence n'est pas utilisée ici pour remettre en cause la mécanique de construction.

## VIII. Registre des 98 variations extrêmes examinées

| titre | date | detail | statut |
|---|---|---|---|
| AES | 2001-09-26 | -49.5 % | non_corroboré |
| AES | 2002-02-19 | -32.1 % | non_corroboré |
| AES | 2002-07-29 | +41.0 % | non_corroboré |
| AES | 2002-08-22 | +30.7 % | non_corroboré |
| AES | 2002-10-31 | +39.4 % | non_corroboré |
| AKAM | 2000-04-18 | +30.7 % | non_corroboré |
| AKAM | 2000-10-19 | +30.8 % | non_corroboré |
| AKAM | 2000-12-05 | +42.5 % | non_corroboré |
| AKAM | 2001-04-19 | +39.4 % | non_corroboré |
| AKAM | 2002-11-21 | +45.7 % | non_corroboré |
| AKAM | 2003-04-23 | +35.6 % | non_corroboré |
| AKAM | 2003-10-30 | +34.2 % | non_corroboré |
| AMD | 2002-10-03 | -32.4 % | non_corroboré |
| AMD | 2016-04-22 | +52.3 % | non_corroboré |
| AMT | 2001-11-06 | -35.4 % | non_corroboré |
| AMT | 2002-11-18 | +34.7 % | non_corroboré |
| AMZN | 2001-04-09 | +33.6 % | non_corroboré |
| AMZN | 2001-11-14 | +30.2 % | non_corroboré |
| AMZN | 2001-11-26 | +34.5 % | non_corroboré |
| CBRE | 2008-11-13 | +43.0 % | non_corroboré |
| CBRE | 2008-11-24 | +45.0 % | non_corroboré |
| CBRE | 2009-03-25 | +64.0 % | non_corroboré |
| CDNS | 2008-01-31 | -33.0 % | non_corroboré |
| CDNS | 2008-07-24 | -30.8 % | non_corroboré |
| CIEN | 2001-08-16 | -30.2 % | non_corroboré |
| CNP | 2002-07-23 | -42.2 % | non_corroboré |
| CNP | 2002-07-24 | -31.6 % | non_corroboré |
| CNP | 2002-07-25 | +63.0 % | non_corroboré |
| COHR | 2000-03-02 | +71.4 % | non_corroboré |
| COHR | 2000-08-18 | +66.5 % | non_corroboré |
| DELL | 2024-03-01 | +31.6 % | rendement_prix_concordant |
| DELL | 2026-05-29 | +32.8 % | rendement_prix_concordant |
| EQIX | 2000-10-13 | +45.8 % | non_corroboré |
| EQIX | 2001-04-06 | -42.4 % | non_corroboré |
| EQIX | 2001-04-09 | +54.9 % | non_corroboré |
| EQIX | 2001-05-02 | +31.1 % | non_corroboré |
| EQIX | 2001-07-16 | +32.0 % | non_corroboré |
| EQIX | 2002-09-27 | +32.0 % | non_corroboré |
| EQIX | 2003-01-07 | +36.5 % | non_corroboré |
| EQIX | 2003-05-05 | +32.8 % | non_corroboré |
| EQIX | 2010-10-06 | -33.1 % | non_corroboré |
| FIX | 2001-05-10 | +30.0 % | non_corroboré |
| FLEX | 2018-10-26 | -35.0 % | rendement_prix_concordant |
| FLEX | 2026-05-06 | +39.7 % | rendement_prix_concordant |
| GLW | 2002-07-31 | -35.2 % | non_corroboré |
| HAL | 2001-12-07 | -42.4 % | non_corroboré |
| HAL | 2020-03-09 | -37.6 % | rendement_prix_concordant |
| JBL | 2009-03-25 | +36.5 % | non_corroboré |
| JCI | 2002-06-07 | -30.8 % | non_corroboré |
| JCI | 2002-06-13 | +36.0 % | non_corroboré |
| JCI | 2002-07-26 | +45.8 % | non_corroboré |
| JCI | 2007-07-02 | -53.4 % | erreur_scission_corrigée_source_SEC |
| LITE | 2018-11-12 | -33.0 % | rendement_prix_concordant |
| MRVL | 2000-10-17 | -30.2 % | non_corroboré |
| MRVL | 2001-09-27 | -32.1 % | non_corroboré |
| MRVL | 2023-05-26 | +32.4 % | rendement_prix_concordant |
| MRVL | 2026-06-02 | +32.5 % | rendement_prix_concordant |
| NTAP | 2000-04-25 | +35.8 % | non_corroboré |
| NTAP | 2000-12-05 | +40.9 % | non_corroboré |
| NVDA | 2000-03-07 | +42.4 % | non_corroboré |
| NVDA | 2001-01-03 | +30.7 % | non_corroboré |
| NVDA | 2002-07-31 | -31.8 % | non_corroboré |
| NVDA | 2003-05-09 | +33.1 % | non_corroboré |
| NVDA | 2004-08-06 | -35.2 % | non_corroboré |
| NVDA | 2008-07-03 | -30.7 % | non_corroboré |
| ON | 2002-01-03 | +55.6 % | non_corroboré |
| ORCL | 2025-09-10 | +35.9 % | rendement_prix_concordant |
| PLD | 2008-11-12 | -30.1 % | non_corroboré |
| PWR | 2002-07-02 | -68.1 % | non_corroboré |
| PWR | 2003-08-06 | -30.8 % | non_corroboré |
| SMCI | 2018-10-04 | -41.1 % | rendement_prix_concordant |
| SMCI | 2022-05-04 | +31.2 % | rendement_prix_concordant |
| SMCI | 2024-01-19 | +35.9 % | rendement_prix_concordant |
| SMCI | 2024-02-22 | +32.9 % | rendement_prix_concordant |
| SMCI | 2024-10-30 | -32.7 % | rendement_prix_concordant |
| SMCI | 2024-11-19 | +31.2 % | rendement_prix_concordant |
| SMCI | 2026-03-20 | -33.3 % | rendement_prix_concordant |
| SNPS | 2004-08-19 | -31.2 % | non_corroboré |
| SNPS | 2025-09-10 | -35.8 % | rendement_prix_concordant |
| SWKS | 2000-10-19 | +35.7 % | non_corroboré |
| SWKS | 2000-12-05 | +31.4 % | non_corroboré |
| SWKS | 2001-04-18 | +31.5 % | non_corroboré |
| SWKS | 2006-10-03 | +35.4 % | non_corroboré |
| SWKS | 2009-02-06 | +34.9 % | non_corroboré |
| TDY | 2000-03-28 | +41.5 % | non_corroboré |
| VRT | 2022-02-23 | -36.7 % | rendement_prix_concordant |
| WDC | 2000-01-19 | +30.5 % | non_corroboré |
| WDC | 2000-03-09 | +31.5 % | non_corroboré |
| WDC | 2000-03-13 | +39.8 % | non_corroboré |
| WDC | 2000-12-04 | -32.1 % | non_corroboré |
| WMB | 2002-07-22 | -61.0 % | non_corroboré |
| WMB | 2002-07-23 | -40.8 % | non_corroboré |
| WMB | 2002-07-29 | +101.0 % | non_corroboré |
| WMB | 2002-08-01 | +40.7 % | non_corroboré |
| WMB | 2002-08-05 | -32.1 % | non_corroboré |
| WMB | 2016-01-14 | +34.4 % | non_corroboré |
| WMB | 2016-02-08 | -34.8 % | non_corroboré |
| XEL | 2002-07-26 | -36.8 % | non_corroboré |
