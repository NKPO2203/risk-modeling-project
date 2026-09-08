# Portefeuilles de l'étude

*AI Concentration Risk Research. Tâche 24 de la phase 3. 8 septembre 2026.*

Ce document fixe la composition des portefeuilles avant tout calcul. Il est écrit pour qu'aucune décision de construction ne puisse être révisée après avoir vu un résultat. Si une composition change, la modification sera datée et motivée ici même.

## Règles communes

Tous les portefeuilles sont **équipondérés**. Aucun ne demande de capitalisation boursière, ce qui les rend calculables sur toute la période : les nombres d'actions déclarés à la SEC ne commencent qu'en février 2009.

Chaque entreprise entre le jour de sa **première cotation réelle**, celle qui suit ses éventuelles lignes de remplissage. La composition grandit donc au cours du temps, comme celle de l'indice auquel elle est comparée. `P1` compte 81 titres au 3 janvier 2000 et 113 au 27 octobre 2025.

**Alphabet compte pour une ligne.** Ses deux classes d'actions, `GOOG` et `GOOGL`, occupent deux fichiers de prix ; leurs poids sont additionnés et l'entreprise pèse comme n'importe quelle autre.

Les rendements sont **quotidiens** et **totaux**, dividendes réinvestis, colonne `Adj Close`.

Les termes de comparaison sont `SPY`, réplique du S&P 500 pondéré par capitalisation, et `RSP`, réplique de sa version équipondérée. Toute comparaison exigeant `RSP` commence en mai 2003.

## Avertissement sur le nombre de titres

Sept portefeuilles comptent moins de vingt-cinq titres et `P4` n'en compte que six. Ils seront **mécaniquement plus volatils** que `P1`, indépendamment de tout effet lié à l'IA.

La volatilité d'un portefeuille équipondéré de n titres de volatilité σ et de corrélation moyenne ρ vaut σ multiplié par la racine de ρ plus (1 − ρ)/n. Quand n passe de 113 à 6, le second terme explose. Cet effet devra être isolé à chaque comparaison, faute de quoi on attribuera à la concentration thématique ce qui vient du simple petit nombre.

## Le thème et ses deux moitiés

`P2` et `P3` se recomposent exactement en `P1`.

### P1. Le thème entier

**Règle.** Les 113 entreprises retenues à l'étape 1.

**Question.** Thermomètre du thème. Ce n'est pas une recommandation, c'est une mesure.

**113 entreprises**, dont 81 disponibles dès le 3 janvier 2000.

### P2. Exposition établie

**Règle.** Les entreprises dont le rapport annuel documente une activité IA déjà réelle.

**Question.** Restreindre aux expositions avérées change-t-il le risque, ou le thème emporte-t-il tout.

**95 entreprises**, dont 64 disponibles dès le 3 janvier 2000.

3M (MMM), AES Corporation (AES), Advanced Micro Devices (AMD), Akamai Technologies (AKAM), Alliant Energy (LNT), Alphabet Inc. (Class A) (GOOG), Amazon (AMZN), American Tower (AMT), Ametek (AME), Amphenol (APH), Analog Devices (ADI), Applied Materials (AMAT), Ares Management (ARES), Arista Networks (ANET), Baker Hughes (BKR), Berkshire Hathaway (BRK-B), Broadcom (AVGO), CBRE Group (CBRE), CDW Corporation (CDW), CRH plc (CRH), Cadence Design Systems (CDNS), Carrier Global (CARR), Caterpillar Inc. (CAT), Ciena (CIEN), Cisco (CSCO), Coherent Corp. (COHR), Comfort Systems USA (FIX), Constellation Energy (CEG), Corning Inc. (GLW), Cummins (CMI), Dell Technologies (DELL), Digital Realty (DLR), Dominion Energy (D), Dover Corporation (DOV), Dow Inc. (DOW), Duke Energy (DUK), Eaton Corporation (ETN), Ecolab (ECL), Emcor (EME), Equinix (EQIX), Fastenal (FAST), FirstEnergy (FE), Flex Ltd. (FLEX), GE Vernova (GEV), Generac (GNRC), General Dynamics (GD), Hewlett Packard Enterprise (HPE), Howmet Aerospace (HWM), Hubbell Incorporated (HUBB), IBM (IBM), IDEX Corporation (IEX), Intel (INTC), Iron Mountain (IRM), Jabil (JBL), Johnson Controls (JCI), KLA Corporation (KLAC), Keysight Technologies (KEYS), Lam Research (LRCX), Lennox International (LII), Lumentum (LITE), Martin Marietta Materials (MLM), Marvell Technology (MRVL), Meta Platforms (META), Microchip Technology (MCHP), Micron Technology (MU), Microsoft (MSFT), Monolithic Power Systems (MPWR), NRG Energy (NRG), NetApp (NTAP), Nucor (NUE), Nvidia (NVDA), ON Semiconductor (ON), Oracle Corporation (ORCL), Pinnacle West Capital (PNW), Prologis (PLD), Qnity Electronics (Q), Quanta Services (PWR), Sandisk (SNDK), Schlumberger (SLB), Seagate Technology (STX), Skyworks Solutions (SWKS), Steel Dynamics (STLD), Supermicro (SMCI), Synopsys (SNPS), TE Connectivity (TEL), Teledyne Technologies (TDY), Teradyne (TER), Tesla, Inc. (TSLA), Texas Instruments (TXN), Trane Technologies (TT), Vertiv (VRT), Vulcan Materials Company (VMC), Western Digital (WDC), Xcel Energy (XEL), Xylem Inc. (XYL)

### P3. Engagement documenté

**Règle.** Les entreprises ayant annoncé un engagement sans l'avoir encore réalisé.

**Question.** Le marché traite-t-il une promesse comme une réalité.

**18 entreprises**, dont 17 disponibles dès le 3 janvier 2000.

Ameren (AEE), American Electric Power (AEP), CMS Energy (CMS), CenterPoint Energy (CNP), Chevron Corporation (CVX), DTE Energy (DTE), Entergy (ETR), Evergy (EVRG), Halliburton (HAL), NiSource (NI), PPL Corporation (PPL), Realty Income (O), Sempra (SRE), Southern Company (SO), Texas Pacific Land Corporation (TPL), Vistra Corp. (VST), WEC Energy Group (WEC), Williams Companies (WMB)

## La chaîne, sept maillons

Les sept maillons somment exactement à 113. Le découpage suit le champ `canal` de la sélection de l'étape 1, et non la classification sectorielle GICS : celle-ci range Alphabet et Meta dans les services de communication et Amazon dans la consommation discrétionnaire, ce qui disperserait les acteurs les plus centraux dans un groupe résiduel.

### P4. Les acheteurs

**Règle.** Canal depense ou depense et vend : celles qui financent l'infrastructure.

**Question.** Que fait le risque chez ceux qui paient la facture.

**6 entreprises**, dont 3 disponibles dès le 3 janvier 2000.

Alphabet Inc. (Class A) (GOOG), Amazon (AMZN), Meta Platforms (META), Microsoft (MSFT), Oracle Corporation (ORCL), Tesla, Inc. (TSLA)

### P5. Les vendeurs

**Règle.** Canal vend : puces, matériel et logiciel vendus au marché de l'IA.

**Question.** Que fait le risque chez ceux qui encaissent la dépense.

**32 entreprises**, dont 19 disponibles dès le 3 janvier 2000.

Advanced Micro Devices (AMD), Akamai Technologies (AKAM), Amphenol (APH), Analog Devices (ADI), Arista Networks (ANET), Broadcom (AVGO), Ciena (CIEN), Cisco (CSCO), Coherent Corp. (COHR), Corning Inc. (GLW), Dell Technologies (DELL), Dow Inc. (DOW), Ecolab (ECL), Hewlett Packard Enterprise (HPE), IBM (IBM), Intel (INTC), Lumentum (LITE), Marvell Technology (MRVL), Microchip Technology (MCHP), Micron Technology (MU), Monolithic Power Systems (MPWR), NetApp (NTAP), Nvidia (NVDA), ON Semiconductor (ON), Sandisk (SNDK), Seagate Technology (STX), Skyworks Solutions (SWKS), Supermicro (SMCI), TE Connectivity (TEL), Teledyne Technologies (TDY), Texas Instruments (TXN), Western Digital (WDC)

### P6. L'électricité

**Règle.** Canal fournit, secteur Utilities : les producteurs qui alimentent les centres de données.

**Question.** L'exposition IA d'un service public se comporte-t-elle comme celle d'un fabricant de puces.

**22 entreprises**, dont 19 disponibles dès le 3 janvier 2000.

AES Corporation (AES), Alliant Energy (LNT), Ameren (AEE), American Electric Power (AEP), CMS Energy (CMS), CenterPoint Energy (CNP), Constellation Energy (CEG), DTE Energy (DTE), Dominion Energy (D), Duke Energy (DUK), Entergy (ETR), Evergy (EVRG), FirstEnergy (FE), NRG Energy (NRG), NiSource (NI), PPL Corporation (PPL), Pinnacle West Capital (PNW), Sempra (SRE), Southern Company (SO), Vistra Corp. (VST), WEC Energy Group (WEC), Xcel Energy (XEL)

### P7. L'équipement industriel

**Règle.** Canal fournit, secteur Industrials : refroidissement, alimentation, construction.

**Question.** Le maillon industriel suit-il le maillon technologique.

**22 entreprises**, dont 16 disponibles dès le 3 janvier 2000.

3M (MMM), Ametek (AME), Carrier Global (CARR), Caterpillar Inc. (CAT), Comfort Systems USA (FIX), Cummins (CMI), Dover Corporation (DOV), Eaton Corporation (ETN), Emcor (EME), Fastenal (FAST), GE Vernova (GEV), Generac (GNRC), General Dynamics (GD), Howmet Aerospace (HWM), Hubbell Incorporated (HUBB), IDEX Corporation (IEX), Johnson Controls (JCI), Lennox International (LII), Quanta Services (PWR), Trane Technologies (TT), Vertiv (VRT), Xylem Inc. (XYL)

### P8. L'immobilier

**Règle.** Canal fournit, secteur Real Estate : les foncières de centres de données.

**Question.** Un actif immobilier adossé à l'IA reste-t-il un actif immobilier.

**7 entreprises**, dont 4 disponibles dès le 3 janvier 2000.

American Tower (AMT), CBRE Group (CBRE), Digital Realty (DLR), Equinix (EQIX), Iron Mountain (IRM), Prologis (PLD), Realty Income (O)

### P9. L'amont des puces

**Règle.** Canal fournit, secteur Information Technology : les outils qui fabriquent les puces.

**Question.** L'amont amplifie-t-il ou amortit-il les mouvements de l'aval.

**11 entreprises**, dont 8 disponibles dès le 3 janvier 2000.

Applied Materials (AMAT), CDW Corporation (CDW), Cadence Design Systems (CDNS), Flex Ltd. (FLEX), Jabil (JBL), KLA Corporation (KLAC), Keysight Technologies (KEYS), Lam Research (LRCX), Qnity Electronics (Q), Synopsys (SNPS), Teradyne (TER)

### P10. Matières et énergie primaire

**Règle.** Canal fournit, autres secteurs : ciment, acier, gaz, services pétroliers, capital.

**Question.** Les intrants physiques portent-ils une part du risque IA.

**13 entreprises**, dont 12 disponibles dès le 3 janvier 2000.

Ares Management (ARES), Baker Hughes (BKR), Berkshire Hathaway (BRK-B), CRH plc (CRH), Chevron Corporation (CVX), Halliburton (HAL), Martin Marietta Materials (MLM), Nucor (NUE), Schlumberger (SLB), Steel Dynamics (STLD), Texas Pacific Land Corporation (TPL), Vulcan Materials Company (VMC), Williams Companies (WMB)

## P11. Portefeuille d'avenir

Réservé. Il sera constitué à la fin du projet, une fois les mesures de risque, de couverture et de coût établies. Rien n'y est inscrit aujourd'hui, et rien ne doit y être inscrit avant que les résultats soient connus.

Sa vocation est d'être le seul portefeuille du document construit **en connaissance des résultats**, et il sera présenté comme tel, distinct des dix autres qui sont définis à l'aveugle.
