# Portefeuilles de l'étude

*AI Concentration Risk Research. Tâche 24 de la phase 3. Mise à jour du 8 septembre 2026 après audit.*

Ce document fixe la composition et les règles courantes. Les premières règles ont été écrites avant la construction, mais les données avaient déjà été consultées. Il ne s'agit donc pas d'un protocole préenregistré à l'aveugle. Les corrections initiales sont détaillées dans `research/audit_etape_2.md`. Le complément consacré aux prix et aux opérations sur titres figure dans `research/verification_etape_2.md`.

## I. Règles communes

L'étude comporte dix portefeuilles, chacun dans deux versions. L'équipondération porte sur les entreprises, identifiées par CIK, à la constitution et aux rééquilibrages de la version annuelle. Les poids dérivent entre ces dates. La version conservée n'est pas remise à égalité chaque année.

La période va de la clôture du 3 janvier 2000 à celle du 4 septembre 2026. Elle contient 6 709 niveaux et 6 708 rendements. L'annualisation conventionnelle utilise 252 séances par an. Le départ est une base nette de constitution : les frais de mise initiale et de liquidation finale ne sont pas imputés. Les rendements sont nominaux, en dollars, avant fiscalité. Les fractions de titres sont autorisées, sans contrainte de taille ni d'impact de marché.

Une entreprise entre à la clôture de sa première observation admissible ; son rendement commence à compter à la séance suivante. C'est une règle de disponibilité dans les données, pas la preuve d'une date d'IPO. La composition grandit, de 81 entreprises et 81 titres à 113 entreprises et 114 titres. Elle ne reproduit pas les entrées et sorties historiques du S&P 500.

Alphabet compte pour une entreprise. `GOOGL` désigne la classe A et `GOOG` la classe C. La classe C est retenue seulement à partir du 3 avril 2014, son historique Yahoo antérieur reprenant celui de la classe A. L'apparition d'une seconde classe partage le montant investi dans l'entreprise entre ses classes disponibles, sans lui attribuer le poids d'une nouvelle entreprise. Les listes ci-dessous nomment l'entreprise ; `appartenance.csv` conserve ses deux titres.

Deux autres limites d'historique sont fixées dans `data/review/regles_historiques_prix.csv`, avec leurs sources : `DELL` commence le 26 décembre 2018 pour la classe C, en cotation conditionnelle avant la cotation ordinaire du 28 décembre ; `VRT` commence le 10 février 2020 après le rapprochement de Vertiv et du véhicule coté GSAH. Les segments antérieurs restent dans les fichiers bruts mais ne servent pas à ces portefeuilles. Ces corrections portent sur l'identité du titre ou de l'activité, pas sur les performances obtenues.

Les autres cotations conditionnelles, dites « when-issued », ne sont pas exclues au seul motif qu'elles précèdent la distribution juridique d'une action. Elles peuvent être réelles. Leur négociabilité, leur liquidité et leur coût d'exécution restent une limite du modèle ; le premier cours Yahoo ne prouve pas qu'une opération de n'importe quelle taille était réalisable.

Les rendements observés figurent dans `rendements_prix.csv` ; ceux qui servent à valoriser les positions figurent dans `rendements_valorisation.csv`. Les séquences initiales sans volume sont exclues. À l'intérieur de l'historique, un cours identique à la veille, avec volume nul et quatre prix identiques, est traité comme suspect. Un volume nul avec des prix variables n'est pas automatiquement effacé. Pendant un trou, le dernier cours connu sert à valoriser la position ; le mouvement cumulé est pris à la reprise. Les 18 observations portées sont signalées dans `qualite_valorisation.csv` : ce ne sont pas des observations de rendement nul utilisables sans réserve pour estimer le risque. Aucun prix n'est porté avant la première observation admissible.

## II. Les règles de gestion et de comparaison

**Rééquilibrage.** La version annuelle est remise aux poids égaux par entreprise à la première séance de janvier. La version conservée réinvestit seulement les dividendes dans le titre payeur à cette date. Les entrées ont lieu en cours d'année dans les deux versions. Si un titre déjà admis n'a pas de cours utilisable le jour d'une opération, toute l'opération est reportée à la première séance où tous les titres admis sont négociables. Trois reports concernent `P1`, `P2` et `P5`, du 2 au 5 janvier 2015, à cause de la cotation absente d'AMD. Ce report corrige l'ancienne liquidation implicite d'AMD pour toute l'année.

**Entrées.** Une nouvelle entreprise reçoit, après financement, un poids égal à un divisé par le nombre d'entreprises alors détenues, nouvelle comprise. Si plusieurs entrent ensemble, chacune reçoit ce poids. Le financement réduit proportionnellement les positions existantes et leur trésorerie ; hors frais, il ne crée aucune valeur. Les anciens poids conservent leur dérive. Une entrée hors janvier n'est donc pas un rééquilibrage général. Les cibles enregistrées hors janvier sont une référence d'égalité pour l'admission, pas la photographie des poids effectivement détenus.

**Dividendes.** Le moteur utilise `Close` et les dividendes monétaires, après application des corrections documentées dans `data/review/corrections_evenements_prix.json`. `Adj Close` reste une donnée de contrôle du fournisseur. Sur une position déjà détenue, le rendement de richesse avant frais est la variation du cours plus le dividende, rapportés au cours précédent. Le montant du dividende est comptabilisé au détachement dans une poche attachée au titre et non rémunérée. Il est réinvesti à la date annuelle : suivant les poids cibles dans la version rééquilibrée, dans le titre payeur dans la version conservée.

Cette poche assimile une créance de dividende à des espèces disponibles. Les dates de paiement des actions n'ont pas été collectées. La différence est réelle : les dividendes de décembre de SPY sont payés fin janvier, après notre date de réinvestissement. La convention synthétique est commune aux portefeuilles et aux fonds de comparaison. Elle ne décrit pas un compte espèces strictement réalisable. Un contrôle séparé sur SPY mesure cette approximation dans le rapport d'audit. Il reste à traiter la disponibilité effective des paiements avant de revendiquer une exécution réelle.

**Coûts.** Le coût vaut dix points de base sur la somme des achats et des ventes effectivement exécutés, y compris les ventes qui financent une entrée et les achats de réinvestissement des dividendes. Les frais sont financés par le portefeuille ; les cibles sont réduites pour que les achats, ventes, espèces et frais se raccordent exactement. La rotation publiée est la somme de ces montants échangés rapportés à la valeur avant chaque opération, divisée par la durée en années de 252 séances. Elle compte les deux côtés des transactions. Ce taux constant est une hypothèse, pas une mesure de spread ou une garantie de prudence pour toute la période. Les sensibilités à cinq et vingt-cinq points de base figurent dans l'audit.

**Comparaisons.** `SPY` et `RSP` distribuent des dividendes ; leur réinvestissement n'est pas interne au fonds pour le porteur. Leur reconstruction applique la même convention de créance, de réinvestissement annuel et de frais que les portefeuilles. Les séries Yahoo ajustées restent séparées dans `valeurs_comparaisons_yahoo.csv`, pour contrôler l'écart de convention. Toute comparaison exigeant `RSP` commence le 1er mai 2003 et utilise une fenêtre commune, sans prolongement antérieur.

Les trois indices collectés servent au contexte et au contrôle. `^SP500TR` est en rendement total ; `^GSPC` et `^SPXEW` sont des indices de prix, sans dividendes. Le dernier comporte des séances absentes. Ils ne doivent pas entrer sans adaptation dans une comparaison de performance totale. Les frais internes et les règles de suivi de SPY et RSP restent différents : leur écart n'identifie pas à lui seul l'effet causal de la concentration.

**Divisions et scissions.** Les cours Yahoo sont déjà retraités des divisions : `Stock Splits` ne multiplie pas une seconde fois les positions. Les facteurs de scission décrivent une série synthétique restant investie dans le parent. Les actions distribuées ne sont pas ajoutées au portefeuille en plus de ce retraitement. Leur admission éventuelle dans l'univers, comme celle de Sandisk, est un achat financé distinct. Cette convention n'est pas la conservation juridique de tous les titres reçus.

Le contrôle externe a établi trois erreurs : un retraitement incomplet de Tyco dans JCI au 2 juillet 2007 et deux distributions comptées à nouveau comme espèces, sur Eaton au 2 janvier 2001 et CenterPoint au 1er octobre 2002. Les corrections s'appliquent en mémoire, avant le calcul des rendements. Deux autres distributions, Texas Genco et Adient, sont reclassées en réinvestissement synthétique dans le parent : leur valeur Yahoo est conservée le jour de l'événement, sans prétendre certifier leur prix de liquidation. Les cours bruts et `Adj Close` ne sont pas réécrits.

Les coefficients de scission des fournisseurs peuvent différer selon leurs cours de référence. Le registre `data/review/evenements_prix_documentes.csv` établit la nature des événements ; il ne certifie pas chaque coefficient. Cette approximation reste attachée aux rendements des jours concernés, qui ne doivent pas être interprétés sans contrôle comme des chocs économiques ordinaires.

**Continuité de JCI.** Avant la fusion de 2016, la série utilisée suit Tyco, ancêtre juridique du titre actuel. Elle ne représente pas l'ancienne Johnson Controls Inc. sur toute cette période. Le raccordement juridique et la continuité d'une activité économique ne sont pas la même chose ; le biais rétrospectif de l'univers s'y ajoute.

## III. Ce que les comparaisons permettent de dire

Les dix portefeuilles sont sélectionnés aujourd'hui avec des informations récentes puis projetés sur le passé. Leur performance absolue, leur classement relatif et leurs mesures de risque peuvent tous être affectés par la connaissance a posteriori et par la sélection des survivants. L'écart avec SPY ne mesure pas la taille de ce biais. Ces résultats décrivent la trajectoire historique de paniers actuels. Ils ne prouvent pas que ces paniers étaient identifiables ou investissables à l'époque.

La différence entre rééquilibrer et conserver combine la dérive des poids, les ventes des gagnants, les achats des perdants, les entrées et les coûts. Elle sert à étudier ces mécanismes ; elle n'isole pas un effet causal pur de la concentration. Cette séparation, les facteurs de marché et les épisodes de crise relèvent de l'étape 3. La comparaison trimestrielle reste à faire.

Sept portefeuilles comptent moins de vingt-cinq entreprises et `P4` en compte six. À volatilités individuelles égales et corrélation moyenne donnée, la volatilité d'un portefeuille équipondéré vaut σ multiplié par la racine de ρ + (1 − ρ)/n. Réduire n augmente alors la part non diversifiée. Nos groupes n'ont ni les mêmes volatilités ni les mêmes corrélations : leur petit effectif ne prouve donc pas qu'ils seront plus volatils que `P1`. L'effet de taille devra être distingué des secteurs et des dépendances observées.

## IV. Le thème et ses deux composantes

Les entreprises de `P2` et `P3` forment une partition de celles de `P1`. Cette identité d'appartenance n'implique pas qu'un mélange fixe de leurs séries reproduise `P1` en présence d'entrées, de rééquilibrages et de frais.

### P1. Le thème entier

**Règle.** Les 113 entreprises retenues à l'étape 1.

**Question.** Thermomètre du thème. Ce n'est pas une recommandation, c'est une mesure.

**113 entreprises**, dont 81 disponibles dès le 3 janvier 2000.

### P2. Exposition établie

**Règle.** Les entreprises classées `etablie` dans le registre de sélection : une activité liée à la chaîne de calcul est documentée. Cela ne mesure ni une part de revenus IA ni une intensité homogène d'exposition.

**Question.** Restreindre aux expositions avérées change-t-il le risque, ou le thème emporte-t-il tout.

**95 entreprises**, dont 64 disponibles dès le 3 janvier 2000.

3M (MMM), AES Corporation (AES), Advanced Micro Devices (AMD), Akamai Technologies (AKAM), Alliant Energy (LNT), Alphabet (GOOGL classe A, GOOG classe C), Amazon (AMZN), American Tower (AMT), Ametek (AME), Amphenol (APH), Analog Devices (ADI), Applied Materials (AMAT), Ares Management (ARES), Arista Networks (ANET), Baker Hughes (BKR), Berkshire Hathaway (BRK-B), Broadcom (AVGO), CBRE Group (CBRE), CDW Corporation (CDW), CRH plc (CRH), Cadence Design Systems (CDNS), Carrier Global (CARR), Caterpillar Inc. (CAT), Ciena (CIEN), Cisco (CSCO), Coherent Corp. (COHR), Comfort Systems USA (FIX), Constellation Energy (CEG), Corning Inc. (GLW), Cummins (CMI), Dell Technologies (DELL), Digital Realty (DLR), Dominion Energy (D), Dover Corporation (DOV), Dow Inc. (DOW), Duke Energy (DUK), Eaton Corporation (ETN), Ecolab (ECL), Emcor (EME), Equinix (EQIX), Fastenal (FAST), FirstEnergy (FE), Flex Ltd. (FLEX), GE Vernova (GEV), Generac (GNRC), General Dynamics (GD), Hewlett Packard Enterprise (HPE), Howmet Aerospace (HWM), Hubbell Incorporated (HUBB), IBM (IBM), IDEX Corporation (IEX), Intel (INTC), Iron Mountain (IRM), Jabil (JBL), Johnson Controls (JCI), KLA Corporation (KLAC), Keysight Technologies (KEYS), Lam Research (LRCX), Lennox International (LII), Lumentum (LITE), Martin Marietta Materials (MLM), Marvell Technology (MRVL), Meta Platforms (META), Microchip Technology (MCHP), Micron Technology (MU), Microsoft (MSFT), Monolithic Power Systems (MPWR), NRG Energy (NRG), NetApp (NTAP), Nucor (NUE), Nvidia (NVDA), ON Semiconductor (ON), Oracle Corporation (ORCL), Pinnacle West Capital (PNW), Prologis (PLD), Qnity Electronics (Q), Quanta Services (PWR), Sandisk (SNDK), Schlumberger (SLB), Seagate Technology (STX), Skyworks Solutions (SWKS), Steel Dynamics (STLD), Supermicro (SMCI), Synopsys (SNPS), TE Connectivity (TEL), Teledyne Technologies (TDY), Teradyne (TER), Tesla, Inc. (TSLA), Texas Instruments (TXN), Trane Technologies (TT), Vertiv (VRT), Vulcan Materials Company (VMC), Western Digital (WDC), Xcel Energy (XEL), Xylem Inc. (XYL)

### P3. Engagement documenté

**Règle.** Les entreprises classées `engagement_ou_developpement_documente`. La preuve porte sur un engagement ou un développement ; elle ne permet pas de réduire toutes ces entreprises à une promesse entièrement irréalisée.

**Question.** La maturité de l'exposition documentée est-elle associée à un comportement boursier différent.

**18 entreprises**, dont 17 disponibles dès le 3 janvier 2000.

Ameren (AEE), American Electric Power (AEP), CMS Energy (CMS), CenterPoint Energy (CNP), Chevron Corporation (CVX), DTE Energy (DTE), Entergy (ETR), Evergy (EVRG), Halliburton (HAL), NiSource (NI), PPL Corporation (PPL), Realty Income (O), Sempra (SRE), Southern Company (SO), Texas Pacific Land Corporation (TPL), Vistra Corp. (VST), WEC Energy Group (WEC), Williams Companies (WMB)

## V. La chaîne, sept maillons

Les sept groupes somment exactement à 113. Le champ `canal` détermine d'abord le groupe : dépenses vers `P4`, ventes vers `P5`. Le canal `fournit` est ensuite subdivisé selon le secteur GICS, vers `P6` à `P10`. Ce découpage hybride garde les grands acheteurs ensemble, mais ses groupes restent hétérogènes ; leurs noms ne constituent pas une classification économique indépendante.

### P4. Les acheteurs

**Règle.** Canal depense ou depense et vend : celles qui financent l'infrastructure.

**Question.** Que fait le risque chez ceux qui paient la facture.

**6 entreprises**, dont 3 disponibles dès le 3 janvier 2000.

Alphabet (GOOGL classe A, GOOG classe C), Amazon (AMZN), Meta Platforms (META), Microsoft (MSFT), Oracle Corporation (ORCL), Tesla, Inc. (TSLA)

### P5. Les vendeurs

**Règle.** Canal vend : puces, matériel et logiciel vendus au marché de l'IA.

**Question.** Que fait le risque chez ceux qui encaissent la dépense.

**32 entreprises**, dont 19 disponibles dès le 3 janvier 2000.

Advanced Micro Devices (AMD), Akamai Technologies (AKAM), Amphenol (APH), Analog Devices (ADI), Arista Networks (ANET), Broadcom (AVGO), Ciena (CIEN), Cisco (CSCO), Coherent Corp. (COHR), Corning Inc. (GLW), Dell Technologies (DELL), Dow Inc. (DOW), Ecolab (ECL), Hewlett Packard Enterprise (HPE), IBM (IBM), Intel (INTC), Lumentum (LITE), Marvell Technology (MRVL), Microchip Technology (MCHP), Micron Technology (MU), Monolithic Power Systems (MPWR), NetApp (NTAP), Nvidia (NVDA), ON Semiconductor (ON), Sandisk (SNDK), Seagate Technology (STX), Skyworks Solutions (SWKS), Supermicro (SMCI), TE Connectivity (TEL), Teledyne Technologies (TDY), Texas Instruments (TXN), Western Digital (WDC)

### P6. L'électricité

**Règle.** Canal fournit, secteur Utilities : les services aux collectivités dont l'activité ou l'engagement envers la chaîne de calcul est documenté.

**Question.** L'exposition IA d'un service public se comporte-t-elle comme celle d'un fabricant de puces.

**22 entreprises**, dont 19 disponibles dès le 3 janvier 2000.

AES Corporation (AES), Alliant Energy (LNT), Ameren (AEE), American Electric Power (AEP), CMS Energy (CMS), CenterPoint Energy (CNP), Constellation Energy (CEG), DTE Energy (DTE), Dominion Energy (D), Duke Energy (DUK), Entergy (ETR), Evergy (EVRG), FirstEnergy (FE), NRG Energy (NRG), NiSource (NI), PPL Corporation (PPL), Pinnacle West Capital (PNW), Sempra (SRE), Southern Company (SO), Vistra Corp. (VST), WEC Energy Group (WEC), Xcel Energy (XEL)

### P7. L'équipement industriel

**Règle.** Canal fournit, secteur Industrials : refroidissement, alimentation, construction.

**Question.** Le maillon industriel suit-il le maillon technologique.

**22 entreprises**, dont 16 disponibles dès le 3 janvier 2000.

3M (MMM), Ametek (AME), Carrier Global (CARR), Caterpillar Inc. (CAT), Comfort Systems USA (FIX), Cummins (CMI), Dover Corporation (DOV), Eaton Corporation (ETN), Emcor (EME), Fastenal (FAST), GE Vernova (GEV), Generac (GNRC), General Dynamics (GD), Howmet Aerospace (HWM), Hubbell Incorporated (HUBB), IDEX Corporation (IEX), Johnson Controls (JCI), Lennox International (LII), Quanta Services (PWR), Trane Technologies (TT), Vertiv (VRT), Xylem Inc. (XYL)

### P8. L'immobilier

**Règle.** Canal fournit, secteur Real Estate : immobilier et services immobiliers, dont les centres de données. Toutes les entreprises de ce groupe ne sont pas des foncières spécialisées dans ces centres.

**Question.** Un actif immobilier adossé à l'IA reste-t-il un actif immobilier.

**7 entreprises**, dont 4 disponibles dès le 3 janvier 2000.

American Tower (AMT), CBRE Group (CBRE), Digital Realty (DLR), Equinix (EQIX), Iron Mountain (IRM), Prologis (PLD), Realty Income (O)

### P9. Les fournisseurs technologiques

**Règle.** Canal fournit, secteur Information Technology : équipements, conception, test, assemblage et distribution. CDW, Flex et Jabil montrent que ce groupe déborde les seuls outils de fabrication des puces.

**Question.** L'amont amplifie-t-il ou amortit-il les mouvements de l'aval.

**11 entreprises**, dont 8 disponibles dès le 3 janvier 2000.

Applied Materials (AMAT), CDW Corporation (CDW), Cadence Design Systems (CDNS), Flex Ltd. (FLEX), Jabil (JBL), KLA Corporation (KLAC), Keysight Technologies (KEYS), Lam Research (LRCX), Qnity Electronics (Q), Synopsys (SNPS), Teradyne (TER)

### P10. Matières et énergie primaire

**Règle.** Canal fournit, autres secteurs : ciment, acier, gaz, services pétroliers, capital.

**Question.** Les intrants physiques portent-ils une part du risque IA.

**13 entreprises**, dont 12 disponibles dès le 3 janvier 2000.

Ares Management (ARES), Baker Hughes (BKR), Berkshire Hathaway (BRK-B), CRH plc (CRH), Chevron Corporation (CVX), Halliburton (HAL), Martin Marietta Materials (MLM), Nucor (NUE), Schlumberger (SLB), Steel Dynamics (STLD), Texas Pacific Land Corporation (TPL), Vulcan Materials Company (VMC), Williams Companies (WMB)

## VI. P11. Portefeuille d'avenir

Réservé. Il sera constitué à la fin du projet, une fois les mesures de risque, de couverture et de coût établies. Rien n'y est inscrit aujourd'hui, et rien ne doit y être inscrit avant que les résultats soient connus.

Sa construction utilisera explicitement les résultats déjà obtenus. Ce sera une exploration après observation, à valider sur de nouvelles données. Les dix autres portefeuilles ont des règles antérieures à leur construction, ce qui ne suffit pas à certifier un choix à l'aveugle.
