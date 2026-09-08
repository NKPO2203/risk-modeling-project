# Portefeuilles de l'étude

*État arrêté au 8 septembre 2026 après finition des étapes 1 et 2.*

## I. Objet et période

L'univers final de cette version compte 134 entreprises et 135 titres, Alphabet ayant deux classes. Dix groupes P1 à P10 sont construits, chacun rééquilibré annuellement ou conservé, soit vingt séries. P11 reste une réserve sans composition ni calcul. La mention antérieure de onze portefeuilles ne signifiait donc pas onze séries construites.

La période va de la clôture du 2000-01-03 à celle du 2026-09-04, avec 6709 niveaux et 6708 rendements. L'annualisation utilise 252 séances par an. 90 entreprises sont disponibles au départ. Les entrées ultérieures suivent les observations admissibles ; aucune sortie historique du S&P 500 n'est reproduite.

## II. Continuité de l'instrument

La portion admissible doit représenter les droits économiques de l'action retenue ou de son prédécesseur économique documenté. Un symbole ou une continuité juridique ne suffisent pas. Un véhicule sans activité, une action traçante sur un autre actif ou une classe qui n'existait pas encore sont exclus. Dans une fusion qui dissocie l'émetteur coté et la lignée économique, le prédécesseur comptable publié sert de repère explicite : si le cliché suit la société acquise, l'admission commence avec l'action du groupe combiné. Ce repère ne prétend pas mesurer une continuité parfaite des métiers.

Une acquisition ordinaire, une réorganisation juridique à actifs continus ou une scission laissant le parent dans la même lignée ne redémarrent pas mécaniquement l'historique. Une cotation conditionnelle est conservée lorsqu'elle porte déjà sur l'action à recevoir, distinctement du parent. Ces bornes reposent sur les pièces d’identité des instruments, sans optimisation des performances. Le protocole reste exploratoire : les données avaient déjà été consultées. Ces bornes ne datent pas le commencement de l'exposition à l'IA.

**GOOG, 2014-04-03.** La classe C ne cote sous GOOG en marché régulier qu'à partir de cette date. L'historique antérieur sous ce symbole ne constitue pas une deuxième classe négociable. [Pièce](https://www.nasdaqtrader.com/TraderNews.aspx?id=ETA2014-24).

**DELL, 2018-12-26.** Début des échanges sous condition de la classe C, puis marché régulier le 28 décembre. Le segment antérieur n'est pas assimilé à cette action. [Pièce](https://www.dell.com/en-us/dt/corporate/newsroom/20181228.htm).

**VRT, 2020-02-10.** Début de cotation de Vertiv après la fusion. L'historique antérieur appartient au véhicule d'acquisition GSAH et ne décrit pas l'entreprise industrielle. [Pièce](https://www.vertiv.com/en-emea/about/news-and-events/news-releases/2020/vertiv-lists-on-the-new-york-stock-exchange/).

**JCI, 2016-09-06.** La série avant fusion représente Tyco ; Johnson Controls Inc. est le prédécesseur comptable du groupe combiné. Première séance après conversion des actions Tyco et changement de symbole. [Pièce](https://www.sec.gov/Archives/edgar/data/833444/000083344417000007/q1fy1710-q.htm).

**PLD, 2011-06-03.** Les cours de janvier et mai 2011 du cliché sont ceux de AMB (32.86, 32.93 et 36.36 dollars), pas ceux du prédécesseur comptable ProLogis (14.70, 15.21 et 16.29). Admission du groupe combiné au début de cotation sous PLD. [Pièce](https://ir.prologis.com/financials/sec-filings/content/0000950123-11-043952/d81723sv4.htm).

**BKR, 2017-07-05.** La série antérieure suit Baker Hughes Inc., tandis que GE Oil & Gas est le prédécesseur comptable du groupe issu de la fusion. Première cotation de la classe A BHGE ; le droit transitoire du 3 juillet comprend encore le dividende spécial de 17.50 dollars. [Pièce](https://www.sec.gov/Archives/edgar/data/1701605/000170160518000029/fiscalyear2017form10-k.htm).

**SWKS, 2002-06-26.** La série antérieure suit Alpha Industries. Le rapprochement est une acquisition inversée avec Washington/Mexicali, activité sans fil de Conexant, comme prédécesseur comptable. Première cotation du groupe combiné Skyworks. [Pièce](https://www.sec.gov/Archives/edgar/data/4127/000000412703000006/secondquarter.htm).


Les historiques AVGO/Avago, COHR/II-VI, EVRG/Westar, HWM/Arconic et TT/ancien Ingersoll-Rand sont conservés pour les raisons individuelles du registre `data/review/continuite_examinee_2026-09-08.csv`. Les transformations TPL et SBA ne sont pas des véhicules en attente. Les naissances de CARR, CEG, DOW, GEV, HPE, KEYS, LITE, Q et SNDK ont été distinguées des anciens cours de leur parent.

Les corrections de distribution s'appliquent au cliché complet avant la coupe d'admissibilité. Ainsi, la preuve JCI de juillet 2007 reste contrôlée et archivée, mais ce rendement est désormais hors des portefeuilles. Aucun fichier brut n'est corrigé sur place.

## III. Gestion du portefeuille

Je conserve l'équipondération par entreprise à la constitution et aux rééquilibrages annuels. Les classes d'Alphabet partagent le poids de l'entreprise entre les classes disponibles. Entre les opérations, les poids dérivent avec les cours et les espèces attachées aux titres.

L'admission a lieu à la clôture du premier prix utilisable. Son rendement compte à partir de la séance suivante. Chaque nouvelle entreprise reçoit un poids de 1/n après financement ; les positions et espèces existantes diminuent proportionnellement. Cette entrée n'est pas une remise à égalité des anciennes entreprises. Le modèle n'autorise ni création de richesse ni emprunt implicite.

La version annuelle est rééquilibrée à la première séance de janvier. La version conservée réinvestit les dividendes dans le titre payeur à cette date. Une opération exige un prix utilisable pour tous les titres admis ; sinon elle est reportée. Le coût reste de dix points de base sur les achats et ventes exécutés, financé par le portefeuille. Les frais initiaux de constitution, la liquidation finale, la fiscalité et l'impact de marché restent exclus. Les montants sont nominaux, en dollars ; les fractions d'actions sont autorisées.

Close et les distributions monétaires corrigées déterminent la richesse. Adj Close est une référence de contrôle. Un cours porté valorise une position pendant un trou ; le rendement observé reste manquant et le mouvement cumulé est pris à la reprise. Les 38 cours portés sont identifiés séparément. Les divisions Yahoo ne multiplient jamais une seconde fois les positions.

SPY et RSP appliquent la même convention de créance, de réinvestissement annuel et de frais. RSP commence le 1er mai 2003 : une comparaison avec lui utilise une fenêtre commune. Les trois indices servent au contexte ; SP500TR est en rendement total, GSPC et SPXEW en prix. SPXEW comporte des séances absentes. Aucun indice n'est prolongé artificiellement.

## IV. Composition

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



P2 et P3 partitionnent P1. P4 à P10 constituent une autre partition de P1. Ces égalités d'appartenance ne signifient pas qu'un mélange fixe de séries reproduit P1 avec des opérations et des frais différents.

P4 regroupe les canaux « depense » et « depense et vend » ; P5 le canal « vend ». Le canal « fournit » est partagé selon les secteurs : Utilities pour P6, Industrials pour P7, Real Estate pour P8, Information Technology pour P9, autres secteurs pour P10. Ces noms ne prouvent pas la pureté des métiers : FSLR reste dans P9 suivant cette convention existante et HD entre dans P10. Aucun nouveau groupe n'est créé.

### P1. Thème entier

3M (MMM), AES Corporation (AES), Accenture (ACN), Advanced Micro Devices (AMD), Air Products (APD), Akamai Technologies (AKAM), Alliant Energy (LNT), Alphabet Inc. (GOOG|GOOGL), Amazon (AMZN), Ameren (AEE), American Electric Power (AEP), American Tower (AMT), Ametek (AME), Amphenol (APH), Analog Devices (ADI), AppLovin (APP), Applied Materials (AMAT), Ares Management (ARES), Arista Networks (ANET), Baker Hughes (BKR), Berkshire Hathaway (BRK-B), Broadcom (AVGO), CBRE Group (CBRE), CDW Corporation (CDW), CMS Energy (CMS), CRH plc (CRH), Cadence Design Systems (CDNS), Carrier Global (CARR), Caterpillar Inc. (CAT), CenterPoint Energy (CNP), Chevron Corporation (CVX), Ciena (CIEN), Cisco (CSCO), Coherent Corp. (COHR), Comfort Systems USA (FIX), Constellation Energy (CEG), Corning Inc. (GLW), Cummins (CMI), DTE Energy (DTE), Dell Technologies (DELL), Digital Realty (DLR), Dominion Energy (D), Dover Corporation (DOV), Dow Inc. (DOW), Duke Energy (DUK), EQT Corporation (EQT), Eaton Corporation (ETN), Ecolab (ECL), Emcor (EME), Emerson Electric (EMR), Entergy (ETR), Equinix (EQIX), Evergy (EVRG), Expeditors International (EXPD), Fastenal (FAST), First Solar (FSLR), FirstEnergy (FE), Flex Ltd. (FLEX), GE Vernova (GEV), Generac (GNRC), General Dynamics (GD), Halliburton (HAL), Hewlett Packard Enterprise (HPE), Home Depot (The) (HD), Howmet Aerospace (HWM), Hubbell Incorporated (HUBB), IBM (IBM), IDEX Corporation (IEX), Illinois Tool Works (ITW), Intel (INTC), Iron Mountain (IRM), Jabil (JBL), Johnson Controls (JCI), KLA Corporation (KLAC), Keysight Technologies (KEYS), Kinder Morgan (KMI), Lam Research (LRCX), Leidos (LDOS), Lennox International (LII), Loews Corporation (L), Lumentum (LITE), Martin Marietta Materials (MLM), Marvell Technology (MRVL), Meta Platforms (META), Microchip Technology (MCHP), Micron Technology (MU), Microsoft (MSFT), Monolithic Power Systems (MPWR), NRG Energy (NRG), NXP Semiconductors (NXPI), Nasdaq, Inc. (NDAQ), NetApp (NTAP), NextEra Energy (NEE), NiSource (NI), Nordson Corporation (NDSN), Nucor (NUE), Nvidia (NVDA), ON Semiconductor (ON), Oracle Corporation (ORCL), PPL Corporation (PPL), Parker Hannifin (PH), Pinnacle West Capital (PNW), Prologis (PLD), Public Service Enterprise Group (PEG), Qnity Electronics (Q), Qualcomm (QCOM), Quanta Services (PWR), Realty Income (O), SBA Communications (SBAC), Sandisk (SNDK), Schlumberger (SLB), Seagate Technology (STX), Sempra (SRE), ServiceNow (NOW), Skyworks Solutions (SWKS), Southern Company (SO), Steel Dynamics (STLD), Supermicro (SMCI), Synopsys (SNPS), TE Connectivity (TEL), Teledyne Technologies (TDY), Teradyne (TER), Tesla, Inc. (TSLA), Texas Instruments (TXN), Texas Pacific Land Corporation (TPL), Trane Technologies (TT), Vertiv (VRT), Vistra Corp. (VST), Vulcan Materials Company (VMC), WEC Energy Group (WEC), Western Digital (WDC), Williams Companies (WMB), Xcel Energy (XEL), Xylem Inc. (XYL).

### P2. Exposition établie

3M (MMM), AES Corporation (AES), Accenture (ACN), Advanced Micro Devices (AMD), Air Products (APD), Akamai Technologies (AKAM), Alliant Energy (LNT), Alphabet Inc. (GOOG|GOOGL), Amazon (AMZN), American Tower (AMT), Ametek (AME), Amphenol (APH), Analog Devices (ADI), AppLovin (APP), Applied Materials (AMAT), Ares Management (ARES), Arista Networks (ANET), Baker Hughes (BKR), Berkshire Hathaway (BRK-B), Broadcom (AVGO), CBRE Group (CBRE), CDW Corporation (CDW), CRH plc (CRH), Cadence Design Systems (CDNS), Carrier Global (CARR), Caterpillar Inc. (CAT), Ciena (CIEN), Cisco (CSCO), Coherent Corp. (COHR), Comfort Systems USA (FIX), Constellation Energy (CEG), Corning Inc. (GLW), Cummins (CMI), Dell Technologies (DELL), Digital Realty (DLR), Dominion Energy (D), Dover Corporation (DOV), Dow Inc. (DOW), Duke Energy (DUK), EQT Corporation (EQT), Eaton Corporation (ETN), Ecolab (ECL), Emcor (EME), Emerson Electric (EMR), Equinix (EQIX), Expeditors International (EXPD), Fastenal (FAST), FirstEnergy (FE), Flex Ltd. (FLEX), GE Vernova (GEV), Generac (GNRC), General Dynamics (GD), Hewlett Packard Enterprise (HPE), Home Depot (The) (HD), Howmet Aerospace (HWM), Hubbell Incorporated (HUBB), IBM (IBM), IDEX Corporation (IEX), Illinois Tool Works (ITW), Intel (INTC), Iron Mountain (IRM), Jabil (JBL), Johnson Controls (JCI), KLA Corporation (KLAC), Keysight Technologies (KEYS), Lam Research (LRCX), Leidos (LDOS), Lennox International (LII), Lumentum (LITE), Martin Marietta Materials (MLM), Marvell Technology (MRVL), Meta Platforms (META), Microchip Technology (MCHP), Micron Technology (MU), Microsoft (MSFT), Monolithic Power Systems (MPWR), NRG Energy (NRG), NXP Semiconductors (NXPI), Nasdaq, Inc. (NDAQ), NetApp (NTAP), Nordson Corporation (NDSN), Nucor (NUE), Nvidia (NVDA), ON Semiconductor (ON), Oracle Corporation (ORCL), Parker Hannifin (PH), Pinnacle West Capital (PNW), Prologis (PLD), Qnity Electronics (Q), Quanta Services (PWR), SBA Communications (SBAC), Sandisk (SNDK), Schlumberger (SLB), Seagate Technology (STX), ServiceNow (NOW), Skyworks Solutions (SWKS), Steel Dynamics (STLD), Supermicro (SMCI), Synopsys (SNPS), TE Connectivity (TEL), Teledyne Technologies (TDY), Teradyne (TER), Tesla, Inc. (TSLA), Texas Instruments (TXN), Trane Technologies (TT), Vertiv (VRT), Vulcan Materials Company (VMC), Western Digital (WDC), Xcel Energy (XEL), Xylem Inc. (XYL).

### P3. Engagement documenté

Ameren (AEE), American Electric Power (AEP), CMS Energy (CMS), CenterPoint Energy (CNP), Chevron Corporation (CVX), DTE Energy (DTE), Entergy (ETR), Evergy (EVRG), First Solar (FSLR), Halliburton (HAL), Kinder Morgan (KMI), Loews Corporation (L), NextEra Energy (NEE), NiSource (NI), PPL Corporation (PPL), Public Service Enterprise Group (PEG), Qualcomm (QCOM), Realty Income (O), Sempra (SRE), Southern Company (SO), Texas Pacific Land Corporation (TPL), Vistra Corp. (VST), WEC Energy Group (WEC), Williams Companies (WMB).

### P4. Dépense et exploitation

Alphabet Inc. (GOOG|GOOGL), Amazon (AMZN), AppLovin (APP), Meta Platforms (META), Microsoft (MSFT), Nasdaq, Inc. (NDAQ), Oracle Corporation (ORCL), SBA Communications (SBAC), ServiceNow (NOW), Tesla, Inc. (TSLA).

### P5. Vente

Advanced Micro Devices (AMD), Akamai Technologies (AKAM), Amphenol (APH), Analog Devices (ADI), Arista Networks (ANET), Broadcom (AVGO), Ciena (CIEN), Cisco (CSCO), Coherent Corp. (COHR), Corning Inc. (GLW), Dell Technologies (DELL), Dow Inc. (DOW), Ecolab (ECL), Hewlett Packard Enterprise (HPE), IBM (IBM), Intel (INTC), Lumentum (LITE), Marvell Technology (MRVL), Microchip Technology (MCHP), Micron Technology (MU), Monolithic Power Systems (MPWR), NXP Semiconductors (NXPI), NetApp (NTAP), Nvidia (NVDA), ON Semiconductor (ON), Qualcomm (QCOM), Sandisk (SNDK), Seagate Technology (STX), Skyworks Solutions (SWKS), Supermicro (SMCI), TE Connectivity (TEL), Teledyne Technologies (TDY), Texas Instruments (TXN), Western Digital (WDC).

### P6. Électricité

AES Corporation (AES), Alliant Energy (LNT), Ameren (AEE), American Electric Power (AEP), CMS Energy (CMS), CenterPoint Energy (CNP), Constellation Energy (CEG), DTE Energy (DTE), Dominion Energy (D), Duke Energy (DUK), Entergy (ETR), Evergy (EVRG), FirstEnergy (FE), NRG Energy (NRG), NextEra Energy (NEE), NiSource (NI), PPL Corporation (PPL), Pinnacle West Capital (PNW), Public Service Enterprise Group (PEG), Sempra (SRE), Southern Company (SO), Vistra Corp. (VST), WEC Energy Group (WEC), Xcel Energy (XEL).

### P7. Équipement industriel

3M (MMM), Ametek (AME), Carrier Global (CARR), Caterpillar Inc. (CAT), Comfort Systems USA (FIX), Cummins (CMI), Dover Corporation (DOV), Eaton Corporation (ETN), Emcor (EME), Emerson Electric (EMR), Expeditors International (EXPD), Fastenal (FAST), GE Vernova (GEV), Generac (GNRC), General Dynamics (GD), Howmet Aerospace (HWM), Hubbell Incorporated (HUBB), IDEX Corporation (IEX), Illinois Tool Works (ITW), Johnson Controls (JCI), Leidos (LDOS), Lennox International (LII), Nordson Corporation (NDSN), Parker Hannifin (PH), Quanta Services (PWR), Trane Technologies (TT), Vertiv (VRT), Xylem Inc. (XYL).

### P8. Immobilier

American Tower (AMT), CBRE Group (CBRE), Digital Realty (DLR), Equinix (EQIX), Iron Mountain (IRM), Prologis (PLD), Realty Income (O).

### P9. Fournisseurs technologiques

Accenture (ACN), Applied Materials (AMAT), CDW Corporation (CDW), Cadence Design Systems (CDNS), First Solar (FSLR), Flex Ltd. (FLEX), Jabil (JBL), KLA Corporation (KLAC), Keysight Technologies (KEYS), Lam Research (LRCX), Qnity Electronics (Q), Synopsys (SNPS), Teradyne (TER).

### P10. Autres fournisseurs

Air Products (APD), Ares Management (ARES), Baker Hughes (BKR), Berkshire Hathaway (BRK-B), CRH plc (CRH), Chevron Corporation (CVX), EQT Corporation (EQT), Halliburton (HAL), Home Depot (The) (HD), Kinder Morgan (KMI), Loews Corporation (L), Martin Marietta Materials (MLM), Nucor (NUE), Schlumberger (SLB), Steel Dynamics (STLD), Texas Pacific Land Corporation (TPL), Vulcan Materials Company (VMC), Williams Companies (WMB).

## V. Résultats de construction

Les replis ci-dessous sont des contrôles descriptifs de trajectoire ; leur analyse de risque relève de l’étape 3.

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



## VI. Limites et décisions de l’auteur

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
