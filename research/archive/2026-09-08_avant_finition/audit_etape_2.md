# Audit de l'étape 2

*AI Concentration Risk Research. Audit initial du 8 septembre 2026, conservé comme historique.*

**Complément postérieur :** `research/verification_etape_2.md` donne les vérifications externes, corrections d’opérations sur titres et résultats recalculés après cet audit. Les chiffres et réserves ci-dessous décrivent son état de fin, antérieur à ce complément. Le journal de différences est conservé tel quel.

L'étape 2 ne doit pas être déclarée close. Ses calculs peuvent être reconstruits, mais une reconstruction correcte n'est pas une preuve de l'identité de tous les instruments ni de l'exécution réelle d'une stratégie. Les erreurs démontrées de code et de rédaction décrites ci-dessous ont été corrigées. Les dates de paiement, les opérations sur titres et la couverture de seconde source restent des réserves, pas des points réputés réglés parce que les tests passent.

Le diagnostic porte sur l'état local présent au début de l'audit, y compris les fichiers non encore suivis par Git. Les lignes dites « avant » renvoient à ce cliché conservé hors dépôt, pas à une version supposée sur GitHub. Pour les notebooks, la cellule est numérotée depuis zéro et la ligne depuis un. Le journal final donne aussi les plages de lignes du fichier avant et après chaque modification.

Je distingue quatre statuts : erreur confirmée par le code, les données ou un contre-exemple ; risque conditionnel qui dépend d'un usage futur ; limite déjà assumée dans les documents ; travail prévu pour une autre étape. Une hypothèse documentée n'est pas effacée de l'étude, mais sa portée doit être respectée.

## I. Ce qui est juste

Le rejeu du code initial retrouve exactement les huit CSV de construction présents avant l'audit. Le contrôle des prix retrouve aussi les 8 674 signalements déjà enregistrés. Le défaut principal n'était donc pas une absence de reproductibilité numérique : les règles écrites et certains contrôles ne correspondaient pas au calcul final.

L'univers courant contient 113 entreprises, 114 titres, 95 expositions établies et 18 engagements ou développements documentés. Les deux classes d'Alphabet doivent être regroupées pour compter les entreprises. Le registre complet conserve 273 exclusions, 38 cas douteux et 76 dossiers à examiner. Les 113 degrés `non_quantifie` interdisent de lire les poids égaux comme des intensités égales d'exposition à l'IA. Cette limite était déjà écrite dans la règle de sélection.

Les 119 fichiers de prix comprennent 1 057 439 lignes ; le calendrier comporte 8 458 séances. La fenêtre de construction contient 6 709 niveaux quotidiens, donc 6 708 rendements. Les groupes et leurs deux versions donnent vingt séries, sans portefeuille P11. Les partitions d'entreprises sont exactes ; cela ne suffit pas à démontrer une identité de toutes leurs trajectoires.

Les cours et dividendes bruts, les comptes SEC et les fichiers documentaires protégés n'ont pas été réécrits. Le contrôle final des empreintes est consigné à la fin du rapport. Le calendrier a également été recomposé hors du dépôt à partir des jours ouvrés, jours fériés et fermetures exceptionnelles : aucun écart sur la période couverte. Ce contrôle ne porte pas sur les dates antérieures au calendrier.

Les erreurs comptables déjà corrigées à l'étape 1 n'ont pas été réintroduites par les travaux sur les portefeuilles. Le pipeline de l'étape 1 est rejoué et ses résultats économiques comparés au cliché initial. Cet audit ne prétend pas refaire la lecture intégrale de tous les rapports annuels.

## II. Ce qui est approximatif

### 1. La convention d'entrée de Sandisk a un effet matériel

**Sensibilité confirmée, pas preuve d'un cours faux.** Sandisk commence dans le fichier le 13 février 2025, en cotation conditionnelle, à 36 dollars ; sa cotation ordinaire commence le 24 février, avec une clôture de 48,60 dollars dans le cliché. Retarder cette seule entrée au 24 février, sans modifier aucun autre cours, groupe ou coût, fait passer P1 conservé de 11 043,61 à 10 341,95 en base 100, et P5 conservé de 27 343,23 à 23 799,44. L'annualisation diminue respectivement de 29,39 et 64,21 points de base ; la baisse vaut 6,06 et 16,08 points de base dans leurs versions rééquilibrées.

Cette sensibilité dépasse celle des frais testés. Elle ne justifie pas de choisir une date d'entrée après observation du résultat : le 13 février correspond à un marché conditionnel documenté, tandis que la liquidité et les conditions d'exécution y restent une réserve. Je conserve la règle de première observation admissible et publie son effet. Le contrôle a aussi rapproché quatre clôtures du 31 août au 3 septembre 2026 avec la page investisseurs de Sandisk, alimentée par LSEG : 1 566,70, 1 536,87, 1 553,40 et 1 554,99 dollars, toutes concordantes à l'arrondi. Il ne valide pas l'intégralité de la hausse depuis l'entrée. Coût du contrôle et de la sensibilité : réalisé ; validation d'exécution plus complète conditionnelle. [Historique publié par Sandisk](https://investor.sandisk.com/stock-information/historical-price-lookup), [annonce de séparation et cotation](https://investor.sandisk.com/news-releases/news-release-details/sandisk-celebrates-nasdaq-listing-after-completing-separation).

### 2. La poche de dividendes est une créance assimilée à des espèces

**Limite d'exécution confirmée, rendue explicite.** Avant, `research/portefeuilles.md`, ligne 25, et la tâche 28 parlaient de trésorerie disponible, sans date de paiement. Le moteur crédite le détachement puis réinvestit à la première séance de janvier. Le calendrier officiel de State Street montre que les 26 distributions de décembre de SPY incluses depuis 2000 sont payées fin janvier. Par exemple, le dividende détaché le 19 décembre 2025 est payé le 30 janvier 2026 : il n'est pas disponible le 2 janvier.

J'ai construit un compte indépendant en nombres de parts, espèces et créances. Il retrouve la série SPY du moteur à moins de 5 × 10⁻¹² en base 100. En conservant les cours et montants Yahoo et en attendant les dates de paiement, toujours avec une unique date annuelle de réinvestissement, la valeur finale passe de 829,5077 à 821,1797 et l'annualisation de 8,27231 % à 8,23128 %, soit −4,10350 points de base. Les créances restent valorisées entre détachement et paiement. Une distribution reçue après janvier attend donc le janvier suivant dans cette sensibilité.

La convention principale reste synthétique et commune aux portefeuilles et aux fonds. Je ne remplace pas les dates absentes des actions par un délai inventé. La correction complète d'un compte réalisable demande une collecte des paiements et un calendrier d'exécution, puis un nouveau contrôle. Coût estimé : plusieurs jours de rapprochement selon la couverture du fournisseur. La clarification et la sensibilité SPY sont réalisées. [Distributions historiques de State Street](https://www.ssga.com/library-content/products/fund-data/etfs/us/spdr-etf-historical-distributions.xlsx).

### 3. La version conservée ne reconstitue pas tous les titres juridiquement détenus

**Risque conditionnel confirmé dans sa cause.** Les cours Yahoo sont retraités de divisions et de certains événements de scission. Le moteur conserve des montants sur ces séries, mais ne tient pas le registre des actions distribuées, droits, fusions et cessions qui permettrait de reproduire un compte réel. La colonne `Stock Splits` ne suffit pas à le faire, comme le montrent les facteurs de scission repérés dans le contrôle SEC.

Les règles et le nom « conservée » sont désormais accompagnés de cette réserve. Ajouter des actions reçues sans retirer l'ajustement déjà incorporé au cours pourrait au contraire compter deux fois une distribution. La correction complète demande un registre d'opérations et une politique explicite pour les titres reçus hors univers. Coût estimé : plusieurs jours pour les premiers cas, puis dépendance à une source historique. Aucun brut n'a été retouché pour masquer ce manque.

### 4. Les comparaisons ne mesurent pas un effet causal pur de concentration

**Erreur d'interprétation corrigée, identification encore à construire.** La tâche 26 attribuait à la concentration toute différence entre remettre à égalité et conserver. Ces versions diffèrent aussi par les ventes des gagnants, les achats des perdants, les entrées et les frais. SPY et RSP diffèrent eux-mêmes par leurs règles de suivi et leurs frais internes. Je peux comparer leurs trajectoires ; je ne peux pas appeler automatiquement l'écart « effet de la concentration ».

La même réserve vaut pour les groupes : P2 signifie activité d'infrastructure établie selon le registre, pas activité exclusivement IA ; P3 ne signifie pas que toute l'entreprise serait une promesse irréalisée. Le découpage donne priorité au canal puis utilise GICS pour les fournisseurs. P8 déborde les foncières de centres de données et P9 déborde les outils de fabrication de puces. Les définitions ont été corrigées sans déplacer arbitrairement les entreprises. Coût de rédaction réalisé ; décomposition par facteurs et mécanismes prévue à l'étape 3.

### 5. Plusieurs chiffres étaient plausibles mais privés de leur périmètre

La moyenne de rendement de dividende doit préciser qu'elle mélange des fenêtres de disponibilité. Les mesures de volatilité des premières séances ne permettent pas d'attribuer un effet au seul fait d'une introduction : CARR arrive au milieu de mars 2020, par exemple. La règle d'entrée immédiate reste un choix exploratoire ; sa justification causale a été retirée.

Le repli de 8,89 % cité pour la courte fenêtre depuis le 27 octobre 2025 est défendable pour `SP500TR` : je retrouve 8,89056 %. Pour `GSPC`, je retrouve 9,09752 %. Il s'agissait d'une convention non précisée, pas de la preuve d'un nombre inventé. Le journal donne maintenant les deux séries. La première suspicion d'erreur numérique a donc été écartée après contre-vérification.

Les 321 photographies mensuelles incluent le 4 septembre 2026, dernière séance du cliché, qui n'est pas la fin du mois civil. Elles peuvent servir à suivre les poids, mais ne doivent pas être toutes qualifiées de mois complets pour une analyse de rendement mensuel.

Le contrôle de la formule additive ne donne pas exactement zéro hors dividende : son écart maximal y est de 4,82746 × 10⁻⁶. C'est l'absence d'écart dépassant 10⁻⁴ hors détachement qui est confirmée sur les 119 fichiers. La tâche 15 a été précisée en ce sens. Les six acheteurs sont aussi six entreprises, mais sept titres avec les deux classes d'Alphabet ; la tâche 25 confondait les deux unités.

## III. Ce qui était faux et a été corrigé

Les constats suivants sont classés par conséquence sur le résultat ou sur sa lecture. Le coût indiqué est un ordre de grandeur pour reproduire la correction et son contrôle ; ce n'est pas un relevé de temps facturé.

### 1. Des historiques étaient utilisés avant l'existence du titre ou de l'activité visée

**Erreur confirmée, forte conséquence.** Le filtre initial vérifiait essentiellement le volume et la première ligne Yahoo. Il ne pouvait pas détecter qu'un historique courant contenait un autre instrument ou le véhicule qui avait précédé l'activité.

Pour GOOG, l'historique commençait en 2004 et le titre était admis en janvier 2005. Le bulletin Nasdaq distingue la classe A, renommée GOOGL, et la classe C cotée sous GOOG à partir du 3 avril 2014. Avant cette date, les deux fichiers n'étaient pas deux classes simultanément investissables comme le supposait l'allocation. GOOGL garde l'historique de la classe A ; GOOG entre le 3 avril 2014. [Nasdaq, bulletin ETA2014-24](https://www.nasdaqtrader.com/TraderNews.aspx?id=ETA2014-24).

Pour DELL, le segment commençant en 2016 précède la classe C actuelle. Dell indique une cotation conditionnelle de cette classe à partir du 26 décembre 2018, puis ordinaire le 28 décembre. L'admission précédente en janvier 2017 est remplacée par le 26 décembre 2018. Je retiens la cotation conditionnelle documentée, sans imposer rétroactivement une règle de cotation ordinaire à tout l'univers. [Dell, entrée en cotation de la classe C](https://www.dell.com/en-us/dt/corporate/newsroom/20181228.htm).

Pour VRT, le segment de 2018 relève du véhicule GSAH. La société industrielle Vertiv commence à se négocier sous VRT le 10 février 2020 après le rapprochement. L'admission antérieure en janvier 2019 exposait donc à un véhicule dont l'activité n'était pas celle retenue par le projet. [Vertiv, communiqué de cotation](https://www.vertiv.com/en-emea/about/news-and-events/news-releases/2020/vertiv-lists-on-the-new-york-stock-exchange/).

Les bornes et sources sont conservées dans `data/review/regles_historiques_prix.csv`, lignes 2 à 4. Les séries brutes restent intactes. La restriction agit avant la préparation des rendements et les événements d'entrée. Les autres identités ne sont pas réputées toutes vérifiées pour autant. Coût réalisé : règles dérivées, contrôles des dates et rejeu ; ordre de grandeur de quelques heures avec les rapprochements.

### 2. La première cotation promise devenait une entrée au janvier suivant

**Erreur confirmée sur les données.** `research/portefeuilles.md`, avant ligne 11, promettait la première cotation. Dans `src/portefeuille.py`, avant ligne 73, seule l'appartenance à `jours_reeq` ouvrait la branche d'admission. Le carnet construisait ces cibles une fois par an. META commençait le 18 mai 2012 mais n'entrait que le 2 janvier 2013 ; Q commençait le 27 octobre 2025 mais attendait le 2 janvier 2026. Les premiers mois de rendement étaient écartés malgré la règle écrite.

Le programme construit maintenant les événements annuels et les premières observations admissibles. Dans les deux versions, l'achat est à la clôture de l'événement ; le titre ne rapporte qu'à partir du lendemain. Hors janvier, les anciens poids gardent leur dérive : l'entrée ne provoque pas une remise générale à égalité. Le coût porte sur le financement effectif. Les tests distinguent ces deux types d'événement et les résultats ont été recalculés. Coût réalisé : moteur, pipeline, tests et documents ; plusieurs heures pour une reprise autonome complète.

### 3. Un cours absent effaçait le mouvement de reprise et pouvait sortir un titre pendant un an

**Erreur confirmée.** Dans `src/portefeuille.py`, avant lignes 23–24, tout volume nul rendait le cours manquant. Avant lignes 67–69, un rendement manquant devenait un mouvement nul pour une position détenue. Comme le rendement du lendemain était lui aussi manquant, le déplacement entre le dernier cours valide et la reprise était perdu définitivement.

Le contre-exemple est 100, absent, 121, 133,1. Une valorisation conservant le titre doit finir à 133,1 pour une mise de 100. L'ancien enchaînement perd le passage de 100 à 121. Je sépare désormais observation et valorisation : dernier cours porté pendant le trou, déplacement cumulé à la reprise, indicateur visible pour l'analyse de risque.

Le 2 janvier 2015, `data/raw/prix/AMD.csv`, ligne 8779, porte un volume nul et les quatre prix égaux à 2,6700000762939453. Le cours du 5 janvier, ligne 8780, est 2,6600000858306885. Les anciennes cibles de P1, P2 et P5 ne contenaient aucun AMD en 2015. La version rééquilibrée le liquidait donc implicitement pour l'année ; la version conservée ne le liquidait pas, mais restait touchée par la perte du rendement de reprise. La correction reporte les trois opérations au 5 janvier, quand les cours sont utilisables. Le rapport ne prétend pas que les deux versions subissaient exactement la même erreur. Coût réalisé : séparation des matrices, reports, journal de qualité et tests ; quelques heures avec le rejeu.

### 4. Les transactions de la version conservée n'étaient pas toutes facturées

**Erreur confirmée.** Avant lignes 99–103 de `src/portefeuille.py`, `echange` comptait seulement l'achat des entrants. Les ventes qui le finançaient n'étaient pas facturées, et l'achat annuel de réinvestissement des dividendes n'avait aucun coût. La version rééquilibrée calculait aussi ses frais sur la cible avant prélèvement, au lieu des montants finalement exécutés.

Une entrée portant le nouveau titre à la moitié d'un portefeuille de valeur un échange une moitié vendue et une moitié achetée. À dix points de base, la facture vaut 0,001 dans le cas symétrique testé, pas 0,0005. Le nouveau calcul résout exactement `frais = taux × somme des achats et ventes après financement des frais`. L'identité est vérifiée chaque jour dans le journal.

La rotation était une moyenne par événement, présentée comme annuelle. Elle est maintenant la somme des montants échangés rapportés aux valeurs préalables, divisée par la durée en années de 252 séances. Coût réalisé : solveur, oracle indépendant, sensibilité à trois taux et rédaction ; quelques heures. Le modèle ne prétend toujours pas mesurer l'impact de marché.

### 5. Une faillite pouvait recréer une mise de départ

**Échec silencieux confirmé par contre-exemple, non rencontré dans le cliché.** Dans `src/portefeuille.py`, avant ligne 76, `valeur == 0` relançait une initialisation à un, y compris après une perte totale. Une série de portefeuille 1, 0 redevenait 1 à la date annuelle suivante sans apport. L'initialisation dépend maintenant exclusivement de la première date ; 1, 0 reste à 0. Le test empêche cette résurrection. La donnée de prix actuelle ne contient pas un tel cas, donc je ne lui attribue aucune part du changement de performance réel. Coût réalisé : inférieur à une heure avec le test.

### 6. Les admissions comptaient les titres au lieu des entreprises

**Erreur de règle confirmée.** Dans `src/portefeuille.py`, avant lignes 92–98, le nombre de positions positives déterminait le financement des entrants. Deux classes d'Alphabet pouvaient donc compter comme deux entreprises, alors que `poids_cibles` était déjà équipondéré par entreprise. Le CIK est désormais la clé dans les deux fonctions. L'apparition d'une seconde classe partage le montant de son entreprise ; l'arrivée d'une nouvelle entreprise utilise le nombre d'entreprises effectivement détenues.

Les noms issus de la composition pouvaient aussi étiqueter toute l'entreprise « Class A » en incluant GOOG classe C. L'étiquette de classe a été retirée du nom d'entreprise dans l'appartenance et l'export, sans changer les symboles ni les preuves du registre. Coût réalisé : inférieur à une heure hors rejeu.

### 7. Les contrôles du notebook ne contrôlaient pas le moteur qui écrivait les dernières sorties

**Erreur confirmée par lecture et rejeu cellule par cellule.** `src/construire_portefeuille.ipynb` contenait plusieurs définitions successives de simulation, dans les cellules 5 et 7. Les contrôles des cellules 9 et 10 précédaient l'import final du module, cellule 11, puis la réécriture des valeurs et des poids, cellule 12. Des contrôles pouvaient donc réussir pour un moteur, puis le carnet publier les résultats d'un autre sans leur réappliquer les mêmes tests.

Le module final initial reproduisait pourtant les CSV : la suspicion d'un fichier final impossible à reconstruire est rejetée. La correction consiste à utiliser une seule implémentation, appelée par le notebook et la commande locale, et à contrôler les objets effectivement publiés. Le carnet ne redéfinit plus le moteur. Coût réalisé : extraction du pipeline, simplification des carnets, rejeu complet ; quelques heures.

### 8. Le test de dividende vérifiait une formule Yahoo au lieu du compte simulé

**Erreur confirmée.** `research/cas_de_test.md`, avant ligne 21, attendait 95/90 − 1 pour un cours de 100, un détachement de 10 et un cours final de 95. Le test calculait cette formule lui-même ; il n'appelait pas le moteur. Pour une action détenue, la richesse est 95 + 10 = 105, soit 5 %. Le moteur doit suivre cette identité additive. La convention multiplicative reste utile pour rapprocher `Adj Close`, mais ce n'est pas le même objet.

Le test appelle maintenant le moteur et vérifie le résultat de 5 %. Un autre cas vérifie qu'un cours peut rester stable malgré le dividende : une autre variation de marché peut compenser le détachement. La phrase « ce qu'aucun marché ne fait », dans le journal, était fausse. Coût réalisé : inférieur à une heure.

### 9. Les benchmarks n'avaient pas la convention des portefeuilles

**Erreur confirmée.** Avant ligne 165 de `research/plan_projet.md`, SPY et RSP étaient décrits comme des fonds au réinvestissement interne, justifiant l'emploi de `Adj Close` face à des portefeuilles réinvestissant en janvier. Les deux fonds distribuent ; l'ajustement Yahoo suppose une autre convention pour le porteur.

Les références principales SPY/RSP sont maintenant reconstruites avec la même convention synthétique de dividendes, le même réinvestissement annuel et les mêmes frais de transaction que les portefeuilles. Les références Yahoo sont conservées dans un fichier distinct. Les indices de prix restent identifiés comme tels ; `SPXEW` n'est pas utilisé comme un indice équipondéré à dividendes réinvestis. Coût réalisé : calcul et documentation, puis oracle SPY ; une à quelques heures.

### 10. Les jours de rééquilibrage recevaient une exemption injustifiée du contrôle de richesse

**Erreur de contrôle confirmée.** Avant ligne 245 du plan et ligne 31 des cas de test, les dates annuelles étaient exclues de l'encadrement au motif que réinvestir la trésorerie ferait bouger la richesse. Réinvestir change sa composition, pas son montant avant frais. La borne doit inclure les dividendes, le rendement nul des espèces et les frais ; l'identité comptable reste valable tous les jours.

Le nouveau journal permet le raccordement quotidien `rendement net = rendement des positions et dividendes − frais / valeur précédente`, sans exclure les opérations. La partition P2/P3 n'est plus présentée comme une certification algébrique générale du moteur : un mélange à poids fixes ne reproduit pas nécessairement des sous-groupes qui ont des opérations et frais différents. Coût réalisé : contrôle quotidien et tests, une à quelques heures.

### 11. Des conversions silencieuses pouvaient valider des entrées invalides

**Risques conditionnels démontrés par tests.** Les cibles manquantes étaient transformées en zéro, les colonnes pouvaient être interprétées dans leur ordre au lieu de leur symbole, et les rendements inconnus sur une position détenue étaient neutralisés. Des comparaisons sur des séries entièrement absentes pouvaient ne rien signaler.

Le moteur refuse les cibles non finies, négatives ou de somme différente de un, les dates désalignées, les valeurs infinies, les rendements inférieurs à −100 % et les données inconnues sur une position détenue. Il réaligne les cibles par symbole et exige des disponibilités booléennes, pour que le texte « False » ne devienne pas vrai lors d'une conversion. Le contrôle de fichier refuse les structures vides et conserve le nombre de comparaisons d'ajustement réellement calculables. Un manifeste vide avec seulement un statut de succès est également refusé. Coût réalisé : gardes, fixtures et oracle ; quelques heures. Ces contre-exemples n'ont pas tous été rencontrés dans les fichiers réels.

### 12. Le contrôle SEC confondait date du dépôt et date de la mesure

**Erreur de rapprochement confirmée.** Le tri sur `depose_le` rendait le résultat stable, mais ne garantissait pas que le nombre d'actions mesuré se situait après la division. Un dépôt récent peut contenir une mesure antérieure. L'encadrement impose maintenant aussi les dates `fin`, avec départage stable entre déclarations.

Les totaux restent 56 événements, 9 sans encadrement, 20 non compatibles et 27 compatibles, mais certaines valeurs changent. Pour DUK au 3 juillet 2012, le rapport passe d'environ 0,526211 à 0,526299 ; ce rapprochement reste influencé par l'acquisition simultanée. Pour MMM en avril 2024, le rapport passe d'environ 1,001196 à 0,993945. Ces cas réfutent aussi la phrase selon laquelle les vingt rapports non confirmés variaient tous de moins de 0,1 %. Le fichier détaillé conserve les dates utilisées. Coût réalisé : correction locale et replay, inférieur à une heure, sans prétendre résoudre toutes les opérations juridiques.

### 13. Les carnets de contrôle et de collecte pouvaient altérer le cliché

**Chemin destructif confirmé à la lecture, non exécuté pendant l'audit.** Le carnet de contrôle contenait des acquisitions de métadonnées et de CMS. Le carnet de collecte se terminait par une compression suivie de la suppression des CSV bruts attendus par le manifeste. Un « tout exécuter » n'était donc pas une opération de simple vérification.

Les acquisitions ont été retirées du carnet de contrôle. La collecte ordinaire est arrêtée si le manifeste du cliché existe, et la cellule supprimant les CSV a été remplacée par une explication. Une exécution manuelle de cellules isolées peut toujours contourner l'ordre d'un notebook : ce verrou ne remplace pas une architecture de collecte versionnée. Les acquisitions réseau n'ont pas été rejouées. Coût réalisé : inférieur à une heure ; un collecteur de production versionné reste un travail distinct.

### 14. Des conclusions dépassaient ce que les nombres pouvaient démontrer

**Erreurs logiques confirmées, rédaction corrigée.** Avant ligne 224 du plan, l'écart de performance avec SPY était appelé « taille du biais de connaissance a posteriori » et les seules grandeurs relatives déclarées exploitables. Aucun contrefactuel ne permet ce calcul. Les mesures relatives de risque sont elles aussi conditionnées par le choix des survivants et par l'information récente.

Avant ligne 33 de `portefeuilles.md`, les petits groupes étaient dits mécaniquement plus volatils. La formule invoquée suppose des volatilités individuelles comparables et une corrélation donnée ; ces conditions ne sont pas vérifiées entre les groupes. Avant ligne 71, le découpage était dit indépendant de GICS alors que le code utilise GICS pour les fournisseurs. Enfin, des frais modestes ne rendent pas le choix de gestion indépendant de la performance ni de l'exécution réelle.

Ces phrases ont été corrigées sans chercher une conclusion opposée. Un résultat défavorable à la concentration comme favorable doit rester possible. Coût de rédaction réalisé ; les tests empiriques relèvent de l'étape 3 et ne sont pas inventés ici.

La dernière relecture a également retiré une justification incorrecte de la tâche 24 : utiliser une taille connue à chaque date n'est pas anachronique en soi. Employer une taille actuelle dans le passé le serait. L'absence de capitalisations exploitables dans le dépôt justifie le choix opérationnel présent ; elle ne démontre pas que la pondération par taille serait étrangère à la question de recherche. Les fonds SPY et RSP restent deux références de pondération, avec leurs autres différences, et leur compte de porteur demande bien la reconstruction désormais appliquée. De même, disposer de rendements quotidiens ne garantit pas à lui seul un nombre suffisant d'extrêmes indépendants.

### 15. Les notes et l'export ne correspondaient plus aux données courantes

**Erreurs numériques confirmées.** Les écarts de taille du cliché et de contrôles venaient principalement de l'ajout de CMS sans mise à jour de toutes les notes. Le classeur annoncé comme courant portait encore 112 entreprises : CMS n'apparaissait dans aucune de ses trois vues et `Recapitulatif!B3` valait 112. Il a été régénéré à 113 avec le même export, les mêmes feuilles et les mêmes formules ; le titre identifie maintenant l'empreinte du registre plutôt qu'une date figée dans le code.

Le tableau suivant distingue les nombres précédemment faux de ceux devenus historiques après modification des règles. Les comptes sont recalculés depuis les CSV, pas déduits des paragraphes.

| Grandeur | Avant dans la note | Recalcul du cliché initial |
|---|---:|---:|
| Fichiers actions | 113 | 114 |
| Fichiers avec benchmarks | 118 | 119 |
| Lignes de prix | 1 043 940 | 1 057 439 |
| Signalements de prix | 8 670 | 8 674 |
| Fichiers signalés | 100 | 101 |
| Séries antérieures au calendrier | 59 | 60 |
| Variations ajustées extrêmes | 126 | 127 |
| Historiques tronqués | 19 | 20 |
| Prix figés stricts | 8 272 | 8 273 |
| Lignes HUBB figées strictes | 5 561 | 5 510 |
| Titres couvrant la période depuis 2000 | 112 | 81 |
| Rendement moyen de dividende sur fenêtres propres | 1,81 % | 1,83685 % |
| Médiane de ces rendements | 1,57 % | 1,61585 % |
| Titres dépassant 3 % | 29 | 30 |
| Groupes où le rééquilibré dépasse le conservé | 7 | 6 |

Après les corrections de cet audit, le dernier compte devient cinq groupes sur dix. Il ne faut pas conserver la conclusion ancienne en remplaçant seulement les fichiers sous-jacents. Les niveaux de concentration publiés avant l'audit correspondaient en revanche aux poids présents : les qualifier tous de faux aurait été un faux positif. Ils sont datés comme résultats antérieurs et recalculés ci-dessous. Coût réalisé : calculs de vérification, mise à jour des documents et de l'export ; quelques heures.

Le reçu `outputs/01a0708c-acb3-72c2-885a-9b76b6070a14/verification_livraison.json` désignait encore le classeur à 112 entreprises et son ancienne empreinte. Le contrôle courant rapproche 8 814 cellules de données des trois vues avec le JSON d'export, retrouve CMS dans chacune et 113 dans le récapitulatif. Le reçu précédent est conservé dans un champ historique ; le nouveau porte l'empreinte du classeur effectivement livré. Aucun succès de contrôle de l'ancien fichier n'est transféré implicitement au nouveau.

### 16. Le manifeste de l'étape 2 n'avait pas de commande de reconstruction

**Défaut d'intégration confirmé.** La présence de `pipeline_portefeuilles.json` ne suffisait pas à démontrer l'intégration annoncée par la tâche 54. Les étapes et le manifeste dépendaient de cellules successives, sans commande locale autonome produisant et contrôlant l'ensemble.

`python -B -m src.construire_portefeuilles` reconstruit maintenant les sorties depuis les preuves locales, contrôle les empreintes avant calcul, vérifie les identités avant publication puis écrit le manifeste. `--check-only` refuse un fichier d'entrée ou de sortie modifié. Le manifeste décrit le Python et les bibliothèques réellement utilisés ; son heure de production change normalement entre deux exécutions.

L'étape 1 incorporait dans ses empreintes tous les modules Python, y compris le moteur de l'étape 2. Sa liste de dépendances est limitée aux traitements qu'elle exécute, à son lanceur et aux dépendances déclarées. Une correction du moteur de portefeuille ne rend plus artificiellement périmés les résultats économiques de l'étape 1. Le cache documentaire ignoré par Git reste nécessaire pour rejouer cette dernière hors réseau : les empreintes seules ne reconstruisent pas le texte absent. Le README et le commentaire de `.gitignore` ont été précisés. Coût réalisé : pipeline, manifestes et vérifications sur deux environnements ; quelques heures.

### 17. La couverture des nombres d'actions n'était pas celle suggérée par le total de lignes

**Lacune confirmée, sans effet sur les poids courants.** `actions_en_circulation.csv` contient 8 987 lignes pour 112 entreprises, mais mélange 6 444 observations instantanées `actions` pour 109 entreprises, 172 `actions_bilan` pour deux, 302 moyennes pondérées pour trois et 2 069 flottants exprimés en dollars. CMS est absent. Meta n'a que la moyenne pondérée et le flottant dans ce fichier ; Alphabet et Dell ont aussi les observations de bilan, ce qui ne les rend pas automatiquement équivalentes au même périmètre de classes.

La première mesure de la notion `actions` est le 24 février 2009 ; 54 entreprises ont une telle mesure datée de 2009. Ce nombre était juste. Utiliser le minimum de toutes les notions aurait trouvé 2008, mais il s'agissait alors du flottant en dollars : cette contre-vérification évite une fausse correction. Le programme n'utilise pas ces valeurs pour pondérer les portefeuilles. La couverture a été explicitée ; une reconstitution exhaustive de capitalisations demanderait d'autres données et contrôles. Coût documentaire réalisé ; collecte complémentaire conditionnelle, non nécessaire à l'équipondération actuelle.

## IV. Ce qui manque encore et ce qui vient plus tard

### 1. Les réserves qui empêchent une clôture sans qualification

Le recoupement externe couvre maintenant 135 distributions de SPY, une clôture de SPY et quatre de Sandisk, en plus des rapprochements SEC. Depuis 2000, la distribution SPY du 17 décembre 2021 diffère de l'historique officiel au-delà de l'arrondi : 1,633 contre 1,636431 dollar. Cet écart ne justifie pas une réécriture du brut. Une sensibilité remplaçant les seuls montants SPY modifie l'annualisation d'environ 0,0104 point de base. Les fichiers et la source restent identifiables. Le coût d'un recoupement d'autres actions représentatives est de l'ordre d'une à quelques journées selon l'accès ; le rapprochement intégral est plus large.

Il reste à vérifier davantage d'identités historiques et à définir le traitement complet des titres reçus lors de scissions ou fusions. Les trois corrections GOOG, DELL et VRT ne constituent pas un contrôle universel. La preuve d'un cours « when-issued » ne prouve pas sa liquidité ni la faisabilité des achats retenus. Coût variable, dépendant des opérations et des sources.

Les dates de paiement des actions et la séparation des créances non encore encaissées manquent pour une simulation strictement réalisable. La convention actuelle est écrite et sa limite chiffrée sur SPY. Elle permet une comparaison synthétique homogène ; elle ne doit pas se transformer en affirmation d'exécution réelle.

Le collecteur historique reste un notebook pédagogique. Le contrôle et la reconstruction sont maintenant séparés et testés, mais une collecte future devrait publier un nouveau cliché dans un autre dossier après validation complète. Les fichiers bruts actuels et leurs empreintes ne doivent pas être écrasés au cours de cette évolution.

### 2. Les limites déjà assumées

La sélection par des documents récents, la composition actuelle de l'indice, les dossiers encore ouverts, les parts d'activité non quantifiées et l'absence de causalité comptable étaient déjà reconnues dans `selection_rule.md`. Je ne les présente pas comme des découvertes de cet audit. Le défaut était de leur donner ensuite une portée trop faible dans l'interprétation des portefeuilles.

Les prix sont un cliché d'une source secondaire. Les fractions de titres, l'absence de fiscalité, la base initiale nette de frais de constitution, l'absence de liquidation finale et le coût constant définissent une simulation. Ces hypothèses ont été explicitées. Elles ne constituent pas des erreurs arithmétiques ; elles limitent le passage d'une comparaison de recherche à un investissement réel.

### 3. Les travaux ultérieurs, pas des erreurs à corriger en cachette

La formulation testable des blocs 2 et 3 du Research Charter reste ouverte. Les sources du risque, les modèles de facteurs, la définition des crises, la contribution au risque, les couvertures et leurs coûts appartiennent aux étapes 3 à 5. Une sensibilité trimestrielle, des délais d'entrée fixés avant comparaison et, pour une prétention prédictive, un univers réellement daté puis testé hors échantillon sont encore nécessaires. Je n'invente pas ces décisions à la place de l'auteur pendant un audit du moteur.

P11 demeure vide. Les simulations de portefeuilles et les modèles de risque futurs ne doivent pas être utilisés pour sélectionner après coup le résultat le plus favorable puis le présenter comme prévu avant observation.

### 4. Contre-vérifications qui ont fait rejeter des soupçons

Le cliché initial est reproductible ; les valeurs finales n'étaient pas les anciennes sorties du moteur créateur de valeur resté dans des cellules antérieures. Les chiffres de concentration correspondaient aux poids initiaux. Le repli de 8,89 % est cohérent avec l'indice à dividendes réinvestis. La date SEC de février 2009 est correcte pour la notion instantanée utilisée. Ces points ont été conservés ou précisés, pas corrigés sur la seule base d'un doute.

Les cotations anticipant une scission ne sont pas nécessairement fictives : les annonces officielles de Qnity, Sandisk, Carrier et GE Vernova documentent des négociations conditionnelles. Je n'ai donc pas tronqué automatiquement ces séries à la date de séparation juridique. Pour NRG, le fichier commence après la période ancienne susceptible de faillite ; je n'ai pas trouvé de preuve d'un raccordement de l'ancienne action annulée à la nouvelle dans ce fichier. Ce soupçon n'a entraîné aucune correction de données.

Le fichier State Street nommé « Fund Data » consulté pendant le contrôle décrivait des primes et décotes, pas un historique de prix. Il n'a pas été utilisé comme une seconde série de clôtures. De même, un volume coté sur une seule place n'a pas été comparé à un volume consolidé comme s'il s'agissait de la même mesure.

### 5. Résultats actuels et comparaison avec le cliché initial

Les rendements annualisés ci-dessous utilisent 252/(N − 1), avec N niveaux observés. Les valeurs sont nominales en dollars, base initiale 100, du 3 janvier 2000 au 4 septembre 2026. Les corrections de dates et de règles changent l'objet calculé ; les écarts ne constituent pas une amélioration de performance recherchée. Le repli est `valeur / maximum atteint − 1`.

| Série | Base 100 avant audit | Base 100 corrigée | Annualisé corrigé | Repli maximal corrigé |
|---|---:|---:|---:|---:|
| P1_reeq | 8 598,99 | 9 057,00 | 18,4454 % | -53,90 % |
| P1_cons | 8 978,13 | 11 043,61 | 19,3311 % | -54,10 % |
| P2_reeq | 9 710,25 | 10 310,31 | 19,0235 % | -57,49 % |
| P2_cons | 9 604,24 | 12 033,25 | 19,7165 % | -56,69 % |
| P3_reeq | 2 962,90 | 2 968,24 | 13,5841 % | -46,18 % |
| P3_cons | 4 857,04 | 4 785,09 | 15,6401 % | -47,40 % |
| P4_reeq | 13 345,17 | 14 065,19 | 20,4203 % | -70,03 % |
| P4_cons | 6 376,91 | 6 679,44 | 17,0982 % | -74,96 % |
| P5_reeq | 15 392,42 | 16 006,49 | 21,0066 % | -73,83 % |
| P5_cons | 18 500,99 | 27 343,23 | 23,4654 % | -74,07 % |
| P6_reeq | 1 859,94 | 1 954,11 | 11,8143 % | -45,30 % |
| P6_cons | 1 625,50 | 1 804,25 | 11,4796 % | -45,05 % |
| P7_reeq | 9 011,99 | 9 725,85 | 18,7629 % | -54,86 % |
| P7_cons | 8 262,87 | 9 078,74 | 18,4561 % | -54,67 % |
| P8_reeq | 6 848,99 | 6 360,14 | 16,8829 % | -61,74 % |
| P8_cons | 2 502,92 | 2 597,83 | 13,0167 % | -63,59 % |
| P9_reeq | 2 696,58 | 2 707,97 | 13,1932 % | -82,34 % |
| P9_cons | 2 424,13 | 2 397,55 | 12,6766 % | -83,08 % |
| P10_reeq | 3 859,47 | 3 849,92 | 14,6993 % | -59,63 % |
| P10_cons | 6 370,49 | 6 239,95 | 16,7992 % | -63,34 % |

La version rééquilibrée dépasse la conservée dans cinq groupes sur dix après correction. Cela ne clôt pas la comparaison de risque et ne désigne pas une stratégie optimale. Les poids mensuels comprennent désormais les zéros avant admission, de sorte que leur présence ou absence peut être vérifiée directement.

| Série | Plus grand poids au dernier relevé | Titre | Maximum d'un poids sur les relevés mensuels |
|---|---:|---|---:|
| P1_cons | 21,4656 % | SNDK | 27,4827 % |
| P1_reeq | 4,1526 % | SNDK | 5,9520 % |
| P4_cons | 60,1573 % | TSLA | 76,5498 % |
| P5_cons | 44,5910 % | SNDK | 63,1951 % |

La poche de créances et espèces représente 0,91832 % en moyenne des photographies mensuelles des vingt séries et 5,64470 % au maximum. Cette moyenne n'est ni une moyenne pondérée par le capital final ni une observation quotidienne. Elle ne prouve pas que la poche est sans effet sur le risque.

Les références homogènes ci-dessous sont comparées sur leur fenêtre commune du 1er mai 2003 au 4 septembre 2026. Les frais internes du fonds sont incorporés dans ses cours et restent différents entre fonds ; les frais de transaction du modèle sont ajoutés au réinvestissement.

La fenêtre commune reprend des comptes déjà construits : SPY conserve donc l'état de sa poche de dividendes issue du calcul commencé en 2000. Elle ne représente pas deux comptes neufs ouverts simultanément en mai 2003. Un contrôle séparé réinitialisant uniquement SPY au 1er mai 2003, entièrement investi à cette date puis géré selon les mêmes règles, donne 11,47170 % annualisés au lieu de 11,46832 %, soit 0,33769 point de base de différence. Je précise le périmètre du tableau sans changer les séries courantes : une future comparaison de nouvelles mises simultanées devra initialiser tous les comptes à sa date commune. Le calcul est conservé dans `spy_common_start.py` et son résultat JSON, hors dépôt.

| Référence et convention | Annualisé | Volatilité quotidienne annualisée | Repli maximal |
|---|---:|---:|---:|
| SPY, créance et réinvestissement annuel | 11,4683 % | 18,3294 % | -54,9217 % |
| RSP, créance et réinvestissement annuel | 11,2734 % | 19,5805 % | -59,6863 % |
| SPY, ajustement Yahoo | 11,5627 % | 18,4905 % | -55,1894 % |
| RSP, ajustement Yahoo | 11,3586 % | 19,7282 % | -59,9228 % |

La sensibilité des frais conserve les mêmes données, groupes, dates et conventions. Elle porte sur les vingt séries ; le tableau présente P1. Aucun des trois taux ne change les cinq groupes où la version rééquilibrée dépasse la conservée. Cela ne prouve pas la robustesse à une autre règle d'entrée ou à un autre univers.

| Coût par montant échangé | Série | Rotation annualisée, achats et ventes | Perte d'annualisation contre coût nul |
|---|---|---:|---:|
| 5 pb | P1_reeq | 24,2429 % | 1,4361 pb |
| 5 pb | P1_cons | 4,1936 % | 0,2502 pb |
| 10 pb | P1_reeq | 24,2419 % | 2,8720 pb |
| 10 pb | P1_cons | 4,1945 % | 0,5005 pb |
| 25 pb | P1_reeq | 24,2392 % | 7,1791 pb |
| 25 pb | P1_cons | 4,1971 % | 1,2521 pb |

### 6. Couverture de l'audit et limites de lecture

La première passe a reconstruit la progression, figé les empreintes et rejoué les calculs antérieurs. La deuxième a confronté les règles, les données et les sources ciblées, corrigé les écarts puis régénéré les résultats. La dernière a cherché des faux positifs, utilisé un oracle distinct, des scénarios contradictoires et des replays sur deux environnements. Les notes et copies intermédiaires restent hors du dépôt ; le journal ci-dessous est la trace publiée des changements.

Les preuves de travail sont conservées dans `C:/Users/josue/.codex/visualizations/2026/09/05/01a0708c-acb3-72c2-885a-9b76b6070a14/audit3_20260908/`. `inventory_initial.json` fixe les fichiers et empreintes avant audit ; `before/` contient les copies utilisées pour les différences ; `precise_evidence.json` porte les observations ciblées. Les recalculs, rapprochements et replays sont conservés avec leurs scripts, notamment `closing_checks.json`, `notebook_replay.json`, `replay_cross_environment.json`, `sndk_entry_sensitivity.csv` et `final_integrity.json`. Ce dossier local hors dépôt est une annexe de travail, pas une dépendance du moteur publié.

Les modules et notebooks de construction, collecte et contrôle des prix, leurs tests, le plan, les portefeuilles, les cas de test et le rapport de prix ont été examinés et repris. `master_context.md`, `selection_rule.md`, `univers_selection.md` et `research_charter.md` ont été relus pour le cadre et les dépendances. Les traitements de l'étape 1 ont été contrôlés comme dépendances et rejoués ; leurs choix économiques ne font pas l'objet d'un nouvel audit exhaustif.

`couverture_fichiers.csv`, dans l'annexe de travail, recense les 10 590 fichiers du cliché initial avec leur empreinte et le niveau de contrôle. Il distingue la lecture, le calcul programmatique, le contrôle des dépendances documentaires et le simple inventaire hors cible. Les nouveaux fichiers produits pendant l'audit sont recensés par le journal des modifications ; ils n'appartenaient pas à cet inventaire initial.

Tous les 119 fichiers de prix, le calendrier, les métadonnées, les décisions, les observations de nombres d'actions et les dérivés utilisés ont fait l'objet de contrôles programmatiques. Il ne s'agit pas de lire visuellement un million de lignes une par une. Les empreintes du corpus documentaire ont été vérifiées ; cela ne constitue pas une nouvelle lecture économique de chacun des 499 rapports.

Les archives de `research/archive/2026-09-05_avant_corrections/`, les anciennes générations de caches, les exercices initiaux `main.py` et `risk_analysis.ipynb`, et les contenus intégralement archivés des rapports n'ont pas reçu une nouvelle revue ligne par ligne. `src/explorer_prix.ipynb` a été lu comme exploration mais n'a pas été rejoué contre le réseau. Les appels de collecte des carnets historiques n'ont pas été exécutés. Les statistiques citées de publications externes dans le Research Charter restent des chiffres attribués à leurs sources, pas des statistiques que les données du dépôt permettraient de recalculer. Aucun audit indépendant de toutes les acquisitions, scissions ou dividendes des 114 actions n'a été réalisé.

Le classeur courant a été rapproché des CSV, régénéré, contrôlé pour CMS et ses totaux, et ses vues affectées vérifiées visuellement. Les anciens classeurs explicitement archivés n'ont pas été remis à jour. Le cache ignoré par Git explique qu'un clone seul ne puisse pas rejouer entièrement l'étape 1 sans disposer aussi de ces preuves locales. La reconstruction de l'étape 2 utilise le cliché de prix conservé et ne dépend pas de ces HTML.

## V. Journal des modifications

Les raisons sont celles des constats précédents. Les blocs suivants recensent les fichiers modifiés, leurs lignes avant et après, le contenu remplacé et la raison de la modification. Les recalculs de grands CSV sont décrits par fichier, colonnes, nombre de lignes et empreintes ; les sorties ne sont pas corrigées cellule par cellule indépendamment de leur moteur.

<!-- JOURNAL_BEGIN -->
### `.gitignore`

Préciser que des empreintes ne remplacent pas les caches absents dans un clone.

Avant : `9c465de11068825247cadd08da49041c2db2410fdb7ca94a848c49ec61a21b22`. Après : `190db14852251a22f28200b24364f6360a4a08ab30714a035491f74bad8356cc`.

Lignes physiques : 233 avant, 235 après.

Les repères `@@` indiquent les lignes avant et après. `-` contient le texte retiré, `+` le texte retenu.

<details>
<summary>Contenu exact des changements</summary>

```diff
--- .gitignore avant
+++ .gitignore après
@@ -223,7 +223,9 @@
 # ---------------------------------------------------------------------------
 # Cache local des rapports annuels : 2,5 Go de HTML et de texte bruts.
-# Il est reconstruit par `python src/fetch_filings_text.py --refresh`.
-# Ce que le depot doit conserver, ce sont les empreintes et le manifeste, qui
-# suffisent a prouver quel document a ete lu :
+# Une nouvelle collecte peut être tentée avec fetch_filings_text.py --refresh,
+# mais ne garantit pas la reproduction exacte d'un ancien corpus.
+# Les empreintes identifient les fichiers attendus ; sans les caches elles
+# ne permettent pas de relire la preuve ni de rejouer le pipeline hors réseau.
+# Les références conservées comprennent :
 #   data/raw/filings_manifest.json
 #   data/raw/filings_termes.csv  (colonnes texte_sha256 et html_sha256)
```

</details>

### `README.md`

Décrire la progression réelle, les environnements et les commandes locales de l’étape 2.

Avant : `3922fbe656d8c4b71469266dcdac655e191d0e1600fc7dff5a463c83535d690e`. Après : `3e81171a489b5327e602546b7c6627f41e7b049e1b2ad5e05030a91c07aaeb87`.

Lignes physiques : 108 avant, 127 après.

Les repères `@@` indiquent les lignes avant et après. `-` contient le texte retiré, `+` le texte retenu.

<details>
<summary>Contenu exact des changements</summary>

````diff
--- README.md avant
+++ README.md après
@@ -1,7 +1,7 @@
 # AI Concentration Risk Research
 
-Je construis un univers documenté d'entreprises exposées à la chaîne des infrastructures de calcul liées à l'IA, à partir de la composition locale du S&P 500. Cet ensemble servira ensuite à construire et comparer plusieurs portefeuilles.
+Je construis et compare des portefeuilles à partir d'un univers documenté d'entreprises exposées à la chaîne des infrastructures de calcul liées à l'IA, issu de la composition locale du S&P 500.
 
-Cette étape prépare les sources, les décisions et les comptes. Elle ne calcule pas encore la performance, les corrélations ou le risque d'un portefeuille.
+L'étape 1 prépare les sources, les décisions et les comptes. L'étape 2 produit maintenant des trajectoires rétrospectives et leurs contrôles. L'analyse des sources du risque et des couvertures reste à faire.
 
 ## Lire le projet
@@ -18,5 +18,5 @@
 ## Reproduire les calculs sans réseau
 
-Environnement vérifié : Python 3.12.14. Les versions de pandas, NumPy et lxml sont fixées dans `requirements.txt`. La collecte utilise la bibliothèque standard Python pour les requêtes ; les tests utilisent `unittest`.
+Environnement de référence actuel : Python 3.13.9 ; le replay de l'étape 2 a aussi été vérifié sous Python 3.12.14. Les versions des bibliothèques sont fixées dans `requirements.txt`. Les collectes SEC utilisent la bibliothèque standard Python, celle des prix utilise yfinance ; les tests utilisent `unittest`.
 
 Après installation des dépendances dans un environnement Python :
@@ -107,2 +107,21 @@
 
 `main.py` et `risk_analysis.ipynb` restent les exercices initiaux du workflow, distincts du traitement de recherche dans `src/`.
+
+
+## Étape 2 : reconstruction des portefeuilles
+
+L'univers courant comprend 113 entreprises et 114 titres. Dix groupes sont calculés dans deux modes de gestion. L'étape 2 reste ouverte sur les réserves exposées dans [l'audit](research/audit_etape_2.md), notamment l'identité historique des instruments, la couverture de seconde source et la disponibilité des dividendes.
+
+Les règles courantes sont dans [Portefeuilles](research/portefeuilles.md), la progression dans [Plan du projet](research/plan_projet.md). Le notebook de construction appelle le même traitement local que ces commandes, sans collecte :
+
+```powershell
+python -B -m src.construire_portefeuilles
+python -B -m src.construire_portefeuilles --check-only
+python -B -m unittest discover -s tests -v
+```
+
+Les versions de référence sont celles de `requirements.txt`, avec Python 3.13.9 ; la version effectivement utilisée est enregistrée dans chaque manifeste. `--output` permet une reconstruction dans un autre dossier et `--cout` une sensibilité du coût unitaire. Les manifestes vérifient les fichiers locaux ; ils ne garantissent pas qu'une nouvelle interrogation de Yahoo redonnera le même cliché.
+
+Les CSV de prix, benchmarks, calendrier et métadonnées du cliché sont nécessaires à cette reconstruction. Le corpus documentaire de l'étape 1 comporte des caches locaux dont la disponibilité dans un clone doit être contrôlée séparément ; le succès local n'est pas une promesse de reconstitution du corpus intégral par une collecte future.
+
+Le carnet de collecte conserve la démarche d'acquisition, mais bloque la collecte ordinaire si le manifeste existe. Pour consulter ou recalculer le cliché, utiliser les carnets de contrôle et de construction. Les preuves brutes ne sont pas réécrites lors de ces opérations.
````

</details>

### `data/processed/appartenance.csv`

Régénérer ce livrable par le traitement corrigé ; aucune valeur de portefeuille n’est ajustée à la main.

Avant : `9d5ae1250b01d3a63dcc73c035474537db3cc3d377524bfc0d1e83cd0877bfe5`. Après : `92db297fe2df037f6b17de655220947bb96a60b507837391b1e5ad1458e6d760`.

Lignes physiques : 343 avant, 343 après.

Après : 342 enregistrements. Colonnes : `portefeuille`, `entreprise`, `cik`, `titre`, `classes`.

Avant : 342 enregistrements. La plage de données commence à la ligne 2 ; les colonnes de prix, rendements, poids ou diagnostics sont recalculées selon les règles du fichier producteur.

### `data/processed/controle_divisions_sec.csv`

Régénérer ce livrable par le traitement corrigé ; aucune valeur de portefeuille n’est ajustée à la main.

Avant : fichier absent. Après : `111847592e3c3030adee6569e48f0698bc0c091a0d9b618fced069a076caaefb`.

Lignes physiques : 0 avant, 57 après.

Après : 56 enregistrements. Colonnes : `symbole`, `date`, `annonce`, `mesure`, `ecart`, `avant_fin`, `apres_fin`, `avant_depose`, `apres_depose`.

### `data/processed/controle_prix.csv`

Régénérer ce livrable par le traitement corrigé ; aucune valeur de portefeuille n’est ajustée à la main.

Avant : `5839ac35202483c4da40f0a6b8fffd42c664c94dfa4bb2592d5014bc9e25b96f`. Après : `d583ed03019a7a94da2344f0bc4e82b1df3e03b7363965266e62ecba61a3b18e`.

Lignes physiques : 8675 avant, 8675 après.

Après : 8674 enregistrements. Colonnes : `fichier`, `test`, `date`, `detail`.

Avant : 8674 enregistrements. La plage de données commence à la ligne 2 ; les colonnes de prix, rendements, poids ou diagnostics sont recalculées selon les règles du fichier producteur.

### `data/processed/controles_portefeuilles.json`

Régénérer ce livrable par le traitement corrigé ; aucune valeur de portefeuille n’est ajustée à la main.

Avant : fichier absent. Après : `b1d136b654124704abc69ea3e7aa0c06a1859b99f6800b77499303644b0b4d9c`.

Lignes physiques : 0 avant, 13 après.

Champs modifiés ou ajoutés : `cours_portes`, `cout`, `ecart_identite_quotidienne`, `ecart_somme_poids`, `entreprises`, `lignes_poids`, `limite`, `releves_mensuels`, `seances`, `series`, `titres`.

```json
{
  "seances": 6709,
  "titres": 114,
  "entreprises": 113,
  "series": 20,
  "releves_mensuels": 321,
  "lignes_poids": 225984,
  "ecart_somme_poids": 4.440892098500626e-16,
  "ecart_identite_quotidienne": 7.554720737878995e-16,
  "cours_portes": 18,
  "cout": 0.001,
  "limite": "Identités comptables contrôlées, exactitude des prix non garantie par ces identités."
}
```


### `data/processed/couverture_controle_prix.json`

Régénérer ce livrable par le traitement corrigé ; aucune valeur de portefeuille n’est ajustée à la main.

Avant : fichier absent. Après : `49e51f2b93e6e88451d03ffe77c1f3b0110a7fd092a35e68e571f2057f8da1f2`.

Lignes physiques : 0 avant, 1342 après.

Champs modifiés ou ajoutés : `comparaisons_ajustement`, `fichiers`, `limite`, `signalements`, `tests`.

### `data/processed/dividendes.csv`

Régénérer ce livrable par le traitement corrigé ; aucune valeur de portefeuille n’est ajustée à la main.

Avant : `89dbe7ce9fe3cf05c8edbc0673c9ed697c4d6a64c7a8587f15322e6058eb628d`. Après : `3cd66e075baa79bffa2fa3b6e5675424fda8761c46cdbce110592f095855340a`.

Lignes physiques : 6710 avant, 6710 après.

Après : 6709 enregistrements. Colonnes : `date`, `ADI`, `AEE`, `AEP`, `AES`, `AKAM`, `AMAT`, `AMD`, `AME`, `AMT`, `AMZN`, `ANET`, `APH`, `ARES`, `AVGO`, `BKR`, `BRK-B`, `CARR`, `CAT`, `CBRE`, `CDNS`, `CDW`, `CEG`, `CIEN`, `CMI`, `CMS`, `CNP`, `COHR`, `CRH`, `CSCO`, `CVX`, `D`, `DELL`, `DLR`, `DOV`, `DOW`, `DTE`, `DUK`, `ECL`, `EME`, `EQIX`, `ETN`, `ETR`, `EVRG`, `FAST`, `FE`, `FIX`, `FLEX`, `GD`, `GEV`, `GLW`, `GNRC`, `GOOG`, `GOOGL`, `HAL`, `HPE`, `HUBB`, `HWM`, `IBM`, `IEX`, `INTC`, `IRM`, `JBL`, `JCI`, `KEYS`, `KLAC`, `LII`, `LITE`, `LNT`, `LRCX`, `MCHP`, `META`, `MLM`, `MMM`, `MPWR`, `MRVL`, `MSFT`, `MU`, `NI`, `NRG`, `NTAP`, `NUE`, `NVDA`, `O`, `ON`, `ORCL`, `PLD`, `PNW`, `PPL`, `PWR`, `Q`, `SLB`, `SMCI`, `SNDK`, `SNPS`, `SO`, `SRE`, `STLD`, `STX`, `SWKS`, `TDY`, `TEL`, `TER`, `TPL`, `TSLA`, `TT`, `TXN`, `VMC`, `VRT`, `VST`, `WDC`, `WEC`, `WMB`, `XEL`, `XYL`.

Avant : 6709 enregistrements. La plage de données commence à la ligne 2 ; les colonnes de prix, rendements, poids ou diagnostics sont recalculées selon les règles du fichier producteur.

### `data/processed/journal_portefeuilles.csv`

Régénérer ce livrable par le traitement corrigé ; aucune valeur de portefeuille n’est ajustée à la main.

Avant : fichier absent. Après : `9f8a0952172f83dacb0735786a2f6b120e8479f2ef53a2c1df96aaca62aa927e`.

Lignes physiques : 0 avant, 134181 après.

Après : 134180 enregistrements. Colonnes : `date`, `valeur_avant`, `valeur_avant_operation`, `valeur`, `frais`, `echange`, `rendement_attendu_avant_frais`, `tresorerie`, `serie`.

### `data/processed/mesures_portefeuilles.csv`

Régénérer ce livrable par le traitement corrigé ; aucune valeur de portefeuille n’est ajustée à la main.

Avant : fichier absent. Après : `e677c5c2744dc592d7b99e45ebce37919955a6c744003a6df309236d9e00e809`.

Lignes physiques : 0 avant, 21 après.

Après : 20 enregistrements. Colonnes : `serie`, `base100`, `annualise`, `rotation_annuelle`, `cout_annualise_pb`, `repli_maximal`.

### `data/processed/operations_reportees.csv`

Régénérer ce livrable par le traitement corrigé ; aucune valeur de portefeuille n’est ajustée à la main.

Avant : fichier absent. Après : `674c13f94dd354d2ea5b7d75235816cc49d0e6ff453ee2a5b83916cd86c02eef`.

Lignes physiques : 0 avant, 4 après.

Après : 3 enregistrements. Colonnes : `portefeuille`, `date_prevue`, `date_effective`, `motif`.

### `data/processed/pipeline_manifest.json`

Publier l’état et les empreintes de l’exécution réellement achevée, avec son environnement et ses dépendances.

Avant : `da80776eaa575bfd1aaad1938a391198507c11227b4821d9ab754127c1452e4f`. Après : `545ae6a95033a594cb24608f79638805913f61c58f68e459bfdf49af99a601d2`.

Lignes physiques : 44 avant, 44 après.

Champs modifiés ou ajoutés : `entrees_sha256`.

### `data/processed/pipeline_portefeuilles.json`

Publier l’état et les empreintes de l’exécution réellement achevée, avec son environnement et ses dépendances.

Avant : `d1d43e554a4e13c17a80bb3acb85c190eb7f8ec620ee140f3a595e5d140ebfb1`. Après : `7db85321fae36291b14fc63617105fc5384374dfd000f076ff1f3c40ca46d5e9`.

Lignes physiques : 47 avant, 182 après.

Champs modifiés ou ajoutés : `code`, `commande`, `entrees_sha256`, `produit_le`, `regles`, `sorties_sha256`.

### `data/processed/pipeline_status.json`

Publier l’état et les empreintes de l’exécution réellement achevée, avec son environnement et ses dépendances.

Avant : `97494e424857ffbbd28523d0dc2413de99038a1f30a2561eca9584a1bc194b6a`. Après : `240fe6f6095ed0549e9489fbc1d1ea3237bf6dd64af9a5e2698f31e53651e129`.

Lignes physiques : 9 avant, 4 après.

Champs modifiés ou ajoutés : `etape_2_portefeuilles`.

```json
{
  "statut": "termine",
  "entreprises_retenues": 113
}
```


### `data/processed/poids_cibles.csv`

Régénérer ce livrable par le traitement corrigé ; aucune valeur de portefeuille n’est ajustée à la main.

Avant : `e0844137277c242191f8c94652485a16bbd90c8b487c7b54debb8a912f839db4`. Après : `4036f43744da005272eda2e8c3be3eba93a29b6f07a8271c3d9e1c697259afcd`.

Lignes physiques : 8002 avant, 14392 après.

Après : 14391 enregistrements. Colonnes : `portefeuille`, `date`, `titre`, `entreprise`, `poids`, `motif`.

Avant : 8001 enregistrements. La plage de données commence à la ligne 2 ; les colonnes de prix, rendements, poids ou diagnostics sont recalculées selon les règles du fichier producteur.

### `data/processed/poids_mensuels.csv`

Régénérer ce livrable par le traitement corrigé ; aucune valeur de portefeuille n’est ajustée à la main.

Avant : `498a7f683d13e10df505e9ba353162250a05e3d7f21f9455ea799fb2d75261c7`. Après : `9c536972546cb836add072a20708e83ccf8f907f768448968c2cb5a696ef54e6`.

Lignes physiques : 196111 avant, 225985 après.

Après : 225984 enregistrements. Colonnes : `date`, `serie`, `titre`, `poids`.

Avant : 196110 enregistrements. La plage de données commence à la ligne 2 ; les colonnes de prix, rendements, poids ou diagnostics sont recalculées selon les règles du fichier producteur.

### `data/processed/qualite_valorisation.csv`

Régénérer ce livrable par le traitement corrigé ; aucune valeur de portefeuille n’est ajustée à la main.

Avant : fichier absent. Après : `6e20d7b8f3f7fe587099857aa029f4730db397e0a8a90839a0ebe5021bb9becd`.

Lignes physiques : 0 avant, 19 après.

Après : 18 enregistrements. Colonnes : `titre`, `date`, `motif`, `reprise`.

### `data/processed/rendements_prix.csv`

Régénérer ce livrable par le traitement corrigé ; aucune valeur de portefeuille n’est ajustée à la main.

Avant : `f6ce72fde5fc70b271235fa7f17a125109193947a755957d4cd9c2bf41e08932`. Après : `da8eebbc31bdc5e2393cf40631c7eef937c5b15c3b9c0b72ee2224165bf77932`.

Lignes physiques : 6710 avant, 6710 après.

Après : 6709 enregistrements. Colonnes : `date`, `ADI`, `AEE`, `AEP`, `AES`, `AKAM`, `AMAT`, `AMD`, `AME`, `AMT`, `AMZN`, `ANET`, `APH`, `ARES`, `AVGO`, `BKR`, `BRK-B`, `CARR`, `CAT`, `CBRE`, `CDNS`, `CDW`, `CEG`, `CIEN`, `CMI`, `CMS`, `CNP`, `COHR`, `CRH`, `CSCO`, `CVX`, `D`, `DELL`, `DLR`, `DOV`, `DOW`, `DTE`, `DUK`, `ECL`, `EME`, `EQIX`, `ETN`, `ETR`, `EVRG`, `FAST`, `FE`, `FIX`, `FLEX`, `GD`, `GEV`, `GLW`, `GNRC`, `GOOG`, `GOOGL`, `HAL`, `HPE`, `HUBB`, `HWM`, `IBM`, `IEX`, `INTC`, `IRM`, `JBL`, `JCI`, `KEYS`, `KLAC`, `LII`, `LITE`, `LNT`, `LRCX`, `MCHP`, `META`, `MLM`, `MMM`, `MPWR`, `MRVL`, `MSFT`, `MU`, `NI`, `NRG`, `NTAP`, `NUE`, `NVDA`, `O`, `ON`, `ORCL`, `PLD`, `PNW`, `PPL`, `PWR`, `Q`, `SLB`, `SMCI`, `SNDK`, `SNPS`, `SO`, `SRE`, `STLD`, `STX`, `SWKS`, `TDY`, `TEL`, `TER`, `TPL`, `TSLA`, `TT`, `TXN`, `VMC`, `VRT`, `VST`, `WDC`, `WEC`, `WMB`, `XEL`, `XYL`.

Avant : 6709 enregistrements. La plage de données commence à la ligne 2 ; les colonnes de prix, rendements, poids ou diagnostics sont recalculées selon les règles du fichier producteur.

### `data/processed/rendements_valorisation.csv`

Régénérer ce livrable par le traitement corrigé ; aucune valeur de portefeuille n’est ajustée à la main.

Avant : fichier absent. Après : `1e2c00f53b29219a82a15270c694662db9f6042eb01e8b56937d3447126a0759`.

Lignes physiques : 0 avant, 6710 après.

Après : 6709 enregistrements. Colonnes : `date`, `ADI`, `AEE`, `AEP`, `AES`, `AKAM`, `AMAT`, `AMD`, `AME`, `AMT`, `AMZN`, `ANET`, `APH`, `ARES`, `AVGO`, `BKR`, `BRK-B`, `CARR`, `CAT`, `CBRE`, `CDNS`, `CDW`, `CEG`, `CIEN`, `CMI`, `CMS`, `CNP`, `COHR`, `CRH`, `CSCO`, `CVX`, `D`, `DELL`, `DLR`, `DOV`, `DOW`, `DTE`, `DUK`, `ECL`, `EME`, `EQIX`, `ETN`, `ETR`, `EVRG`, `FAST`, `FE`, `FIX`, `FLEX`, `GD`, `GEV`, `GLW`, `GNRC`, `GOOG`, `GOOGL`, `HAL`, `HPE`, `HUBB`, `HWM`, `IBM`, `IEX`, `INTC`, `IRM`, `JBL`, `JCI`, `KEYS`, `KLAC`, `LII`, `LITE`, `LNT`, `LRCX`, `MCHP`, `META`, `MLM`, `MMM`, `MPWR`, `MRVL`, `MSFT`, `MU`, `NI`, `NRG`, `NTAP`, `NUE`, `NVDA`, `O`, `ON`, `ORCL`, `PLD`, `PNW`, `PPL`, `PWR`, `Q`, `SLB`, `SMCI`, `SNDK`, `SNPS`, `SO`, `SRE`, `STLD`, `STX`, `SWKS`, `TDY`, `TEL`, `TER`, `TPL`, `TSLA`, `TT`, `TXN`, `VMC`, `VRT`, `VST`, `WDC`, `WEC`, `WMB`, `XEL`, `XYL`.

### `data/processed/resume_controle_prix.csv`

Régénérer ce livrable par le traitement corrigé ; aucune valeur de portefeuille n’est ajustée à la main.

Avant : fichier absent. Après : `330c7ecc41625937b12959c4c8ff41982c56afb2c95588743e4e368169cb73b0`.

Lignes physiques : 0 avant, 24 après.

Après : 23 enregistrements. Colonnes : `test`, `cas`.

### `data/processed/valeurs_comparaisons.csv`

Régénérer ce livrable par le traitement corrigé ; aucune valeur de portefeuille n’est ajustée à la main.

Avant : `4728a90df47d877679d3cbe72bd07285378a455586b931a0cfe0df02fcd70b42`. Après : `eafc61c13a6268a54b4eb91c0a8cbca37aa666d86f99bfd97ab7f658b7ccdf5b`.

Lignes physiques : 6710 avant, 6710 après.

Après : 6709 enregistrements. Colonnes : `date`, `GSPC`, `RSP`, `SP500TR`, `SPXEW`, `SPY`.

Avant : 6709 enregistrements. La plage de données commence à la ligne 2 ; les colonnes de prix, rendements, poids ou diagnostics sont recalculées selon les règles du fichier producteur.

### `data/processed/valeurs_comparaisons_yahoo.csv`

Régénérer ce livrable par le traitement corrigé ; aucune valeur de portefeuille n’est ajustée à la main.

Avant : fichier absent. Après : `243144448d5ae7a0274e19170dc6d1fc9c8f9b87ea1c80fd87825a47166762de`.

Lignes physiques : 0 avant, 6710 après.

Après : 6709 enregistrements. Colonnes : `date`, `GSPC`, `RSP`, `SP500TR`, `SPXEW`, `SPY`.

### `data/processed/valeurs_portefeuilles.csv`

Régénérer ce livrable par le traitement corrigé ; aucune valeur de portefeuille n’est ajustée à la main.

Avant : `9c78f7e7cbed463582db829fdfb8c72459bcaa129a93d2270f12ca67baf2f64e`. Après : `234b1e3011345dbbe028a535de7e22043f854a60a84d0af1b4a2a7659ef6f27e`.

Lignes physiques : 6710 avant, 6710 après.

Après : 6709 enregistrements. Colonnes : `date`, `P1_reeq`, `P1_cons`, `P10_reeq`, `P10_cons`, `P2_reeq`, `P2_cons`, `P3_reeq`, `P3_cons`, `P4_reeq`, `P4_cons`, `P5_reeq`, `P5_cons`, `P6_reeq`, `P6_cons`, `P7_reeq`, `P7_cons`, `P8_reeq`, `P8_cons`, `P9_reeq`, `P9_cons`.

Avant : 6709 enregistrements. La plage de données commence à la ligne 2 ; les colonnes de prix, rendements, poids ou diagnostics sont recalculées selon les règles du fichier producteur.

### `data/review/comptabilite_controle_manifest.json`

Horodater le nouveau rejeu du contrôle comptable ; empreintes, nombres et résultats sont inchangés.

Avant : `02de6c5d74cd9c4ce15efedb1b70ef7c76af6e4e2671627f9d6af3ef95a59194`. Après : `079d5eacd834d89746f3707f1360aad8bc7e93bf3c203df41f65305fd35bb095`.

Lignes physiques : 29 avant, 29 après.

Champs modifiés ou ajoutés : `produit_le`.

### `data/review/regles_historiques_prix.csv`

Exclure uniquement les segments GOOG, DELL et VRT qui précèdent le titre ou l’activité visée, avec dates et sources, sans changer les bruts.

Avant : fichier absent. Après : `6fad7152cfa03bd27edcbe93402bbdd5c68d7444086dec9bd755a5c7411f1307`.

Lignes physiques : 0 avant, 4 après.

Les repères `@@` indiquent les lignes avant et après. `-` contient le texte retiré, `+` le texte retenu.

<details>
<summary>Contenu exact des changements</summary>

```diff
--- data/review/regles_historiques_prix.csv avant
+++ data/review/regles_historiques_prix.csv après
@@ -0,0 +1,4 @@
+titre,debut_admissible,motif,source,decision_le
+GOOG,2014-04-03,"La classe C ne cote sous GOOG en marché régulier qu'à partir de cette date. L'historique antérieur sous ce symbole ne constitue pas une deuxième classe négociable.",https://www.nasdaqtrader.com/TraderNews.aspx?id=ETA2014-24,2026-09-08
+DELL,2018-12-26,"Début des échanges sous condition de la classe C, puis marché régulier le 28 décembre. Le segment antérieur n'est pas assimilé à cette action.",https://www.dell.com/en-us/dt/corporate/newsroom/20181228.htm,2026-09-08
+VRT,2020-02-10,"Début de cotation de Vertiv après la fusion. L'historique antérieur appartient au véhicule d'acquisition GSAH et ne décrit pas l'entreprise industrielle.",https://www.vertiv.com/en-emea/about/news-and-events/news-releases/2020/vertiv-lists-on-the-new-york-stock-exchange/,2026-09-08
```

</details>

### `outputs/01a0708c-acb3-72c2-885a-9b76b6070a14/apercus/Par_canal.png`

Régénérer l’export courant à 113 entreprises avec CMS, puis ses vues et son inspection. Les anciens classeurs archivés restent intacts.

Avant : `84010aad0eada50fd81ceff285b6f7cf786449a6886fa373c167cc197a12980d`. Après : `5accb05c5b654295c860dbd793f86eaee201ee2c6d28e0343894e4ecafecfdbf`.

Aperçu régénéré du classeur corrigé ; les lignes, effectifs ou noms visibles reflètent l’export courant.

### `outputs/01a0708c-acb3-72c2-885a-9b76b6070a14/apercus/Par_secteur.png`

Régénérer l’export courant à 113 entreprises avec CMS, puis ses vues et son inspection. Les anciens classeurs archivés restent intacts.

Avant : `deadb63018b387e7eff06b8f8b85298b714fea87d5d51ea7a5a26a15f92642d1`. Après : `9430815268ea63ade48449fea552a08b0005d3990d5d9879d5b4835a1ef8dce5`.

Aperçu régénéré du classeur corrigé ; les lignes, effectifs ou noms visibles reflètent l’export courant.

### `outputs/01a0708c-acb3-72c2-885a-9b76b6070a14/apercus/Recapitulatif.png`

Régénérer l’export courant à 113 entreprises avec CMS, puis ses vues et son inspection. Les anciens classeurs archivés restent intacts.

Avant : `60cd87160333818ba89a262b1d54c5447716ab1cfda397141975c18235676bf4`. Après : `a1296c9e9d2ebad1f7bf5b337af646a5adc0ac3be0463ab10a932a6cd81b15fe`.

Aperçu régénéré du classeur corrigé ; les lignes, effectifs ou noms visibles reflètent l’export courant.

### `outputs/01a0708c-acb3-72c2-885a-9b76b6070a14/univers_retenu.json`

Régénérer l’export courant à 113 entreprises avec CMS, puis ses vues et son inspection. Les anciens classeurs archivés restent intacts.

Avant : `1b6bac065652edd759d889aab887ac6d8de129c16ec1079926b1880114a50bab`. Après : `0a7cb049c4ec11e1c8e0b0ecd02b4cff799035c86fdb25753f79982fe9ba54aa`.

Lignes physiques : 9508 avant, 9593 après.

Fichier de données ou inspection régénéré avec l’export ; son empreinte identifie précisément l’état avant et après.

### `outputs/01a0708c-acb3-72c2-885a-9b76b6070a14/univers_retenu.xlsx`

Régénérer l’export courant à 113 entreprises avec CMS, puis ses vues et son inspection. Les anciens classeurs archivés restent intacts.

Avant : `a44881ea990a3fc86c70e95a5ba0895f6ea3f6e0e476ce6027772fc56470da6f`. Après : `2a06e2ad69afa9c19fd9189e253c90298a595c5ac7694ea351804295676b5a2d`.

Cellules et plages concernées : ligne CMS ajoutée dans les trois vues `Par anciennete`, `Par secteur`, `Par canal` ; leurs tableaux et formules étendus à la ligne 114. `Recapitulatif!B3` passe de 112 à 113, les catégories Utilities, fournit, engagement et couverture partielle sont actualisées. Le titre identifie le registre courant. Les cellules de noms des classes d’Alphabet utilisent désormais le nom d’entreprise.

### `outputs/01a0708c-acb3-72c2-885a-9b76b6070a14/univers_retenu.xlsx.inspect.ndjson`

Régénérer l’export courant à 113 entreprises avec CMS, puis ses vues et son inspection. Les anciens classeurs archivés restent intacts.

Avant : `3ef651733d064239873d9f0c5f67e2bb23a3238418929cf8788130966cc54f78`. Après : `15210e8bf2f78d795e257f5eba9f51a097e2ee5362683d7f7b31cd532eec75e3`.

Lignes physiques : 8371 avant, 8437 après.

Fichier de données ou inspection régénéré avec l’export ; son empreinte identifie précisément l’état avant et après.

### `outputs/01a0708c-acb3-72c2-885a-9b76b6070a14/verification_livraison.json`

Rattacher le reçu au classeur courant après rapprochement de 8 814 cellules ; conserver la vérification précédente dans un champ historique.

Avant : `3c41421a381e37c4123489f4c1049bb3c85cfc52ba2c38edd131bd3f83e25409`. Après : `5e8c3a02c97edc75776d19297a77994667ddade055dcf0e20df004d0ac64ec5c`.

Lignes physiques : 21 avant, 42 après.

Champs modifiés ou ajoutés : `archive`, `controle_precedent_du_2026_09_05`, `excel`, `limite`, `pipeline`, `tests_unittest_reussis`, `verifie_le`.

```json
{
  "verifie_le": "2026-09-08T06:35:58.934263+00:00",
  "tests_unittest_reussis": 92,
  "commande_tests": "python -B -m unittest discover -s tests -v",
  "pipeline": "Recalculs locaux et contrôles des empreintes des deux étapes réussis.",
  "excel": {
    "feuilles": 5,
    "entreprises_par_vue": 113,
    "cellules_rapprochees_aux_entrees": 8814,
    "cms_present_dans": [
      "Par anciennete",
      "Par secteur",
      "Par canal"
    ],
    "total_recapitulatif": 113,
    "erreurs_excel": 0,
    "cik": "texte de 10 chiffres",
    "sha256": "2a06e2ad69afa9c19fd9189e253c90298a595c5ac7694ea351804295676b5a2d"
  },
  "controle_precedent_du_2026_09_05": {
    "verifie_le": "2026-09-05T09:55:48.673026+00:00",
    "tests_unittest_reussis": 51,
    "commande_tests": "python -B -m unittest discover -s tests -v",
    "pipeline": "recalcul complet réussi ; --check-only réussi",
    "excel": {
      "feuilles": 5,
      "entreprises_par_vue": 112,
      "cellules_rapprochees_aux_entrees": 8736,
      "formules_synthese": "totaux rapprochés",
      "erreurs_excel": 0,
      "cik": "texte de 10 chiffres",
      "volets": "C2 dans les trois vues",
      "sha256": "a44881ea990a3fc86c70e95a5ba0895f6ea3f6e0e476ce6027772fc56470da6f"
    },
    "archive": {
      "fichiers_verifies": 29,
      "integrite": "toutes les empreintes correspondent"
    },
    "limite": "Contrôles techniques et rapprochements déclarés, pas certification de toutes les données ni revue intégrale de tous les rapports."
  },
  "limite": "Le contrôle précédent est conservé comme historique ; son empreinte ne désigne plus le classeur courant. Les rapprochements techniques ne certifient ni toutes les données ni la lecture intégrale des rapports."
}
```


### `research/cas_de_test.md`

Corriger les cas de dividende et de raccordement quotidien ; distinguer régression, contre-exemple et intégration.

Avant : `b07d20c4e1be5fe83b8fa281de2b6ea62b9ac09411db736a57d783f14abb8283`. Après : `eb40aaf5ad2686405635ba916dd1d81fa9d81bf886a2be5838c46c0fa432d334`.

Lignes physiques : 49 avant, 59 après.

Les repères `@@` indiquent les lignes avant et après. `-` contient le texte retiré, `+` le texte retenu.

<details>
<summary>Contenu exact des changements</summary>

```diff
--- research/cas_de_test.md avant
+++ research/cas_de_test.md après
@@ -5,7 +5,7 @@
 Ce document propose les cas qui doivent faire échouer le code. Il ne contient pas les tests eux mêmes, qui relèvent de la tâche 50.
 
-Chaque cas vient d'une erreur réellement commise pendant le projet. Un test qui n'a jamais rien attrapé ne prouve rien ; un test qui reproduit un défaut passé garantit qu'il ne revient pas. La colonne d'origine dit où l'erreur a été trouvée et par qui.
+Les cas couvrent des défauts déjà rencontrés et des échecs possibles. Un test de régression protège le cas qu'il reproduit ; il ne garantit pas toutes les variantes du défaut. Un contre-exemple utile n'a pas besoin d'avoir déjà causé une erreur dans les données réelles.
 
-Les données d'entrée sont minuscules et écrites à la main, trois à cinq lignes, pour que la réponse attendue se vérifie de tête. Aucun test ne doit lire les fichiers du dépôt : un test qui dépend de la donnée réelle échoue le jour où la donnée change, pour de mauvaises raisons.
+Les tests unitaires utilisent des données courtes, dont la réponse attendue peut être calculée indépendamment. Ils sont complétés par des contrôles d'intégration sur des fixtures et par le replay des fichiers du dépôt : ces contrôles vérifient d'autres propriétés, notamment les raccordements et la reproductibilité.
 
 ## I. Ce que le calcul des rendements doit refuser
@@ -19,5 +19,5 @@
 ## II. Ce que la convention de dividende doit produire
 
-**Cas 4, le détachement.** Un cours de 100 la veille, un dividende de 10 détaché, un cours de 95 le jour même. Le rendement total attendu suit la convention multiplicative, soit 95 divisé par 90 moins un, et non la convention additive qui donnerait 105 sur 100 moins un. Origine : la tâche 15, où la formule additive s'écartait jusqu'à 8 % sur `JCI` et la multiplicative restait sous 5 × 10⁻⁵ sur les 118 fichiers.
+**Cas 4, le détachement.** Un cours de 100 la veille, un dividende de 10 et un cours de 95 donnent une richesse de 105 pour une action détenue, soit un rendement de 5 %. La formule Yahoo multiplicative donne 95/90 − 1, soit environ 5,56 % : elle décrit un ajustement de série, pas le compte espèces du moteur. Le test appelle réellement le moteur. Un cours stable ou en hausse le jour du détachement reste possible.
 
 **Cas 5, la trésorerie.** Un portefeuille de deux titres, un dividende détaché en mars, aucun rééquilibrage avant janvier suivant. La trésorerie attendue reste constante de mars à décembre, ne rapporte rien, et est réinvestie à la première séance de janvier. Origine : la tâche 28.
@@ -29,7 +29,7 @@
 **Cas 7, l'entrée d'un titre.** Un portefeuille de deux titres auquel un troisième s'ajoute en cours de période. Le poids attendu du nouveau est celui d'un tiers, les deux autres sont réduits proportionnellement, et la valeur totale ne bouge pas, hors frais. Aucun poids ne lui est attribué avant sa première cotation. Origine : tâches 27 et 45.
 
-**Cas 8, l'encadrement.** Un portefeuille dont tous les titres montent. Son rendement ne peut pas être inférieur au plus faible ni supérieur au plus fort. La règle ne s'applique pas les jours de rééquilibrage, où la valeur bouge aussi par la trésorerie et les frais. Origine : tâche 46, où la première version du test relevait 25 violations qui tombaient toutes sur une date de rééquilibrage.
+**Cas 8, le raccordement quotidien.** Le rendement avant frais est la somme des rendements de prix et des dividendes, pondérée par les positions de la veille ; la trésorerie a un rendement nul. Les frais sont ensuite déduits. Cette identité vaut aussi à un rééquilibrage, car le réinvestissement ne crée pas de valeur. Une borne entre le meilleur et le pire rendement doit inclure les dividendes et les espèces ; les frais peuvent placer le net sous la borne brute.
 
-**Cas 9, l'identité d'agrégation.** Un univers de quatre titres, un portefeuille complet et deux sous portefeuilles de deux titres. Sans frais, le mélange des deux moitiés dans les proportions de leurs effectifs reproduit le portefeuille complet à la précision de la machine. Origine : tâche 47, le contrôle le plus fort du projet.
+**Cas 9, l'identité d'agrégation.** Sans frais, avec les mêmes dates d'investissement, des poids initiaux égaux et aucune opération divergente ensuite, le mélange des sous-groupes selon leurs effectifs reproduit l'univers complet. Le test protège ce cas restreint. Les entrées différées, les frais et les rééquilibrages propres aux groupes empêchent d'en faire une preuve générale de la simulation.
 
 **Cas 10, l'entreprise à deux classes d'actions.** Une entreprise cotée sous deux symboles dans un portefeuille de trois entreprises. Le poids attendu de l'entreprise est un tiers, réparti par moitié entre ses deux lignes, et non deux tiers. Origine : Alphabet, `GOOG` et `GOOGL`.
@@ -39,5 +39,5 @@
 **Cas 11, la réponse vide.** Une source qui renvoie un dictionnaire vide sans lever d'erreur. Le code doit compter un échec, pas un succès. Origine : la première version de la tâche 18, qui annonçait 118 titres décrits pour 117 réels parce que `BRK.B` interrogé au lieu de `BRK-B` renvoyait un dictionnaire vide.
 
-**Cas 12, la réponse hors sujet.** Une source qui renvoie une description complète mais sans date de première transaction. Le code doit compter un échec. Origine : `^RSP` et `^SPY`, indices d'options homonymes des fonds, décrits par la source mais sans historique de prix.
+**Cas 12, la réponse hors sujet.** Une description complète peut désigner un instrument différent. Il faut vérifier le symbole, le type attendu, la devise et le raccordement au fichier ; une date de première transaction seule ne prouve pas l'identité. Le contrôle local attend ETF pour SPY et RSP, INDEX pour les trois indices, EQUITY pour les actions.
 
 **Cas 13, le filtre appliqué à la mauvaise population.** Un indice dont toutes les séances portent un volume nul. Le filtre de remplissage ne doit pas s'y appliquer et la série doit survivre entière. Origine : la première version de la tâche 41, qui effaçait `^SP500TR` et `^SPXEW` en totalité, la première disparaissant du tableau sans message.
@@ -48,2 +48,12 @@
 
 Un test de collecte ne doit donc jamais s'écrire « aucune erreur n'a été levée ». Il doit s'écrire « le résultat contient ce qu'il doit contenir ».
+
+## VI. Les contre-exemples ajoutés lors de l'audit
+
+Je vérifie l'entrée en cours d'année dans les deux versions, le financement des achats par les ventes et les espèces, le coût des deux côtés, et le partage d'une entreprise entre classes. Une perte totale ne doit jamais être suivie d'une remise à un de la valeur sans apport. Une cible négative, absente, non finie ou désalignée doit être refusée, tout comme un rendement inconnu sur une position détenue.
+
+Je distingue un rendement observé manquant d'une valorisation portée. Sur des cours 100, absent, 121, 133,1, le trou ne doit pas faire perdre le mouvement de 100 à 121 ; aucun cours n'est cependant porté avant une introduction. Un volume nul avec des prix variables n'est pas assimilé au même cas qu'un segment plat. Les indices à volume nul gardent leur historique.
+
+Les identités de richesse et de frais sont vérifiées dans le journal quotidien de chaque série. Un calcul séparé en nombres de parts reproduit SPY ; une variante conserve les créances jusqu'au paiement officiel pour mesurer la limite du réinvestissement au détachement. Cette sensibilité ne remplace pas la collecte des dates de paiement des actions.
+
+Les acquisitions réseau ne sont pas rejouées sur le cliché protégé. Le carnet de collecte bloque une collecte ordinaire quand le manifeste existe, et sa cellule qui supprimait les CSV a été retirée. Ce verrou ne transforme pas le carnet historique en un collecteur de production entièrement testé.
```

</details>

### `research/controle_donnees_prix.md`

Actualiser les totaux et distinguer détection, rapprochement externe, convention de source et erreur prouvée.

Avant : `500cc1a4a4289df732d0dfe242b87011aec89f152419901543f42567fb1d6e8e`. Après : `797764d2c67ec1042781aa671f88e72190f1e638b5ce5ed65fcca1dbaab6d68f`.

Lignes physiques : 79 avant, 93 après.

Les repères `@@` indiquent les lignes avant et après. `-` contient le texte retiré, `+` le texte retenu.

<details>
<summary>Contenu exact des changements</summary>

```diff
--- research/controle_donnees_prix.md avant
+++ research/controle_donnees_prix.md après
@@ -1,79 +1,93 @@
 # Contrôle des données de prix
 
-*AI Concentration Risk Research. Phase 2 de l'étape 2. 7 septembre 2026.*
+*AI Concentration Risk Research. Phase 2 de l'étape 2. Mise à jour du 8 septembre 2026 après audit.*
 
-## I. Ce que je cherche, et ce que je ne cherche pas
+## I. Ce que je cherche
 
-Je n'analyse rien ici. Je n'ai regardé aucune volatilité, aucune corrélation, aucune performance. Je cherche à savoir si les séries que j'ai collectées méritent qu'on calcule quoi que ce soit dessus.
+Je cherche à distinguer une propriété du marché d'un défaut de fichier. Ce contrôle précède l'interprétation des risques ; les mesures descriptives utilisées pendant l'audit ne constituent pas les résultats de l'étape 3. Une série plausible ne devient pas exacte parce qu'elle passe des tests internes.
 
-La question est celle de l'instrument, pas du phénomène. Le jour où une volatilité sortira à 45 %, je veux pouvoir dire si c'est le marché ou un défaut de fichier. Ce document existe pour que cette réponse soit disponible sans avoir à recommencer.
+## II. Le périmètre et la méthode
 
-## II. Le périmètre
+Le cliché contient 114 fichiers d'actions pour 113 entreprises et cinq séries de comparaison, soit 119 fichiers et 1 057 439 lignes quotidiennes. Les empreintes sont dans `data/raw/prix_manifest.json`. Les preuves brutes ont été conservées intactes pendant l'audit.
 
-Cent treize fichiers d'actions et cinq séries de comparaison, deux fonds et trois indices, soit **1 043 940 lignes de prix quotidiens**. La source est Yahoo Finance, interrogée par `yfinance`, et les fichiers portent chacun leur empreinte dans `data/raw/prix_manifest.json`.
+`src/controler_prix.ipynb` appelle `src/controle_prix.py`. Il n'effectue plus d'acquisition de métadonnées ou de prix. Le traitement rejoue l'ensemble des contrôles et écrit `controle_prix.csv`, `resume_controle_prix.csv`, `controle_divisions_sec.csv` et `couverture_controle_prix.json` dans `data/processed/`.
 
-Les tests sont écrits dans `src/controler_prix.ipynb`. Chaque bloc réécrit ses propres résultats et laisse intacts ceux des autres, de sorte qu'on peut le relancer seul. Toutes les anomalies aboutissent dans un fichier unique, `data/processed/controle_prix.csv`, une ligne par cas, avec le fichier, le test, la date et un détail.
+La couverture indique les fichiers et les comparaisons réellement calculables. Les gardes structurelles refusent les fichiers vides, les colonnes manquantes, les dates impossibles ou désordonnées, les valeurs infinies et les événements ou volumes inconnus. Une absence de prix reste une anomalie explicite, pas un zéro. Un ajustement sans comparaison calculable ne peut pas donner un faux succès.
 
-## III. Vingt-trois tests, huit mille six cent soixante-dix anomalies
+Le calendrier contient 8 458 séances depuis le 29 janvier 1993. Un recalcul séparé des jours ouvrés, jours fériés et fermetures exceptionnelles ne trouve aucun écart sur cette période. Ce contrôle n'étend pas le calendrier avant 1993 et ne valide pas les cours présents à ces dates.
 
-| Test | Cas | Tâche |
-|---|---|---|
-| Date en double | 0 | 13 |
-| Antériorité au calendrier | 59 | 13 |
-| Séance absente | 14 | 13 |
-| Date hors calendrier | 0 | 13 |
-| Variation quotidienne extrême | 126 | 14 |
-| Barre incohérente | 1 | 14 |
-| Prix nul ou négatif | 0 | 14 |
-| Valeur manquante | 1 | 14 |
-| Ajustement incohérent | 0 | 15 |
-| Division non confirmée | 20 | 16 |
-| Référence de cotation absente | 37 | 17 |
-| Première cotation discordante | 0 | 17 |
-| Historique tronqué | 19 | 17 |
-| Métadonnées absentes | 0 | 18 |
-| Devise non USD | 0 | 18 |
-| Fuseau inattendu | 0 | 18 |
-| Type inattendu | 0 | 18 |
-| Décalage horaire inattendu | 0 | 18 |
-| Première transaction discordante | 0 | 18 |
-| Fin de série anticipée | 0 | 19 |
-| Dénomination divergente | 6 | 19 |
-| Séance sans transaction | 115 | 19 |
-| Prix figé | 8 272 | 19 |
+## III. Les résultats recalculés
 
-Cent fichiers sur cent dix-huit portent au moins une anomalie. Les zéros comptent autant que le reste : ils disent qu'un test a bien été exécuté et n'a rien relevé.
+Les vingt-trois contrôles historiques produisent 8 674 signalements sur 101 fichiers. Les nombres précédents, 8 670 signalements sur 100 fichiers et 1 043 940 lignes, n'avaient pas été mis à jour après l'ajout de CMS. Les fichiers dérivés étaient déjà à jour ; c'était leur description qui ne l'était pas.
 
-## IV. Cinq résultats qui changent la suite
+| Test | Cas |
+|---|---:|
+| Date en double | 0 |
+| Antériorité au calendrier | 60 |
+| Séance absente | 14 |
+| Date hors calendrier | 0 |
+| Variation quotidienne extrême | 127 |
+| Barre incohérente | 1 |
+| Prix nul ou négatif | 0 |
+| Valeur manquante | 1 |
+| Ajustement incohérent | 0 |
+| Division non confirmée par ce rapprochement | 20 |
+| Référence de cotation absente | 37 |
+| Première cotation discordante avec la référence | 0 |
+| Historique tronqué | 20 |
+| Métadonnées absentes | 0 |
+| Devise non USD | 0 |
+| Fuseau inattendu | 0 |
+| Type inattendu | 0 |
+| Décalage horaire inattendu | 0 |
+| Première transaction discordante | 0 |
+| Fin de série anticipée | 0 |
+| Dénomination divergente | 6 |
+| Séance sans transaction, hors prix figé | 115 |
+| Prix figé à volume nul | 8 273 |
 
-**Les lignes de remplissage.** Huit mille deux cent soixante-douze lignes portent un volume nul et quatre cours identiques, égaux à la clôture de la veille. Elles ne décrivent aucune séance. `HUBB` en compte 5 561, soit 41 % de son historique ; `CRH` 1 718, soit 18 %. Elles produiraient des rendements nuls et abaisseraient artificiellement toute volatilité calculée sur les périodes anciennes. Je les ai découvertes en cherchant à comprendre la plus forte variation de la liste, `HUBB` au 31 octobre 1994, à +885,9 %, qui n'est pas un mouvement de marché mais la soudure entre le segment fabriqué et le début des vraies cotations.
+Un zéro indique l'absence de détection parmi les observations calculables, pas une certification. Les quatorze séances absentes concernent `SPXEW`. La barre incohérente est celle de HUBB au 5 mai 2021, et les prix manquants ceux du 8 août 1977.
 
-**La convention d'ajustement.** Le prix ajusté de Yahoo se reconstruit à partir du prix de clôture et des dividendes selon une formule multiplicative, le dividende étant retiré du prix de départ et non ajouté au prix d'arrivée. La formule additive s'écarte jusqu'à 8 % sur `JCI` ; la multiplicative reste sous 5 × 10⁻⁵ sur les 118 fichiers, et tous les écarts de la formule additive tombent sur des jours de détachement. Je sais donc reconstruire la série ajustée à la cinquième décimale.
+## IV. Ce que ces contrôles changent
 
-**Deux natures d'événements dans une même colonne.** La colonne `Stock Splits` mélange les divisions d'actions véritables et les facteurs d'ajustement de prix consécutifs à une scission. Sur 56 divisions déclarées depuis 2010, la SEC en confirme 27 et n'en confirme pas 20. Dans ces vingt cas, le nombre d'actions ne bouge pas de plus de 0,1 % : `MMM` en avril 2024 pour Solventum, `IBM` en novembre 2021 pour Kyndryl. Le facteur cumulé des divisions ne peut donc pas être lu directement dans cette colonne, ce qui concerne la reconstruction des capitalisations.
+**Les cours figés.** Sur HUBB, 5 510 lignes portent un volume nul et quatre prix identiques, égaux à la clôture précédente. Le nombre de 5 561 concernait tous les volumes nuls, pas ce critère strict. Un long segment sans volume suivi d'une rupture, comme celle du 31 octobre 1994, ne doit pas être utilisé comme un historique ordinaire de rendements. Je ne peux cependant pas prouver avec ces seuls champs que toute séance isolée sans volume est fabriquée. Le filtre courant distingue les segments initiaux, les prix intérieurs figés et les prix variables à volume nul.
 
-**Les dates de début ne sont pas des premières cotations.** Douze séries commencent exactement le 17 mars 1980, neuf le 21 février 1973, huit le 2 janvier 1962. Aucune entreprise n'introduit ses actions le même matin que onze autres. Ce sont les strates de départ de la base de Yahoo. Dix-neuf entreprises étaient d'ailleurs déjà dans le S&P 500 avant la première ligne de prix disponible. Une date de début dit à partir de quand Yahoo parle du titre, pas quand le titre a commencé d'exister.
+Après les restrictions d'identité sur GOOG, DELL et VRT, 18 observations sont portées sur la période de construction. Le mouvement cumulé est pris à la reprise ; les rendements observés restent manquants autour du trou. La liste est dans `qualite_valorisation.csv`. Estimer une volatilité ou une corrélation en traitant ces valeurs portées comme des observations ordinaires demanderait une réserve supplémentaire.
 
-**Le reste des variations extrêmes est du marché.** Sur les 126 variations ajustées de plus de 30 %, soixante-seize tombent dans les années 2000, dont vingt-quatre en 2002 et seize en 2001, et six en 1987. La concentration correspond aux épisodes connus. Je ne les écarte pas.
+**L'ajustement Yahoo.** La formule `Close_t / (Close_precedent − Dividends_t) − 1` retrouve la variation de `Adj Close` avec un écart maximal inférieur à 5 × 10⁻⁵ dans le cliché. Le seuil d'alerte du programme est 10⁻⁴. La formule additive peut s'écarter sensiblement sur un détachement exceptionnel. Cela confirme la convention du fournisseur, pas sa supériorité pour représenter un compte de titres et d'espèces. Une action passant de 100 à 95 avec 10 de dividende donne 105 de richesse, soit 5 %, quelle que soit la variation de sa série ajustée Yahoo.
 
-## V. Ce que ce contrôle ne couvre pas
+**Les événements dans `Stock Splits`.** Sur 56 événements depuis 2010, 9 ne sont pas encadrés par les observations SEC disponibles, 20 ne correspondent pas à un rapport d'actions égal au facteur annoncé, et 27 sont compatibles avec la tolérance de 2 %. Les dates de mesure et de dépôt encadrantes sont conservées. Un dépôt postérieur à l'événement ne suffit pas si la mesure qu'il contient lui est antérieure.
 
-Aucune source externe automatisable n'a pu être mobilisée. Stooq, qui servait des fichiers de cours sans inscription, les protège désormais derrière une vérification anti-robot, et les autres fournisseurs gratuits exigent un compte. Le seul recoupement indépendant obtenu est celui des divisions d'actions contre les dépôts SEC. Le niveau manuel du protocole, un échantillon relevé à la main sur un site public, reste à exécuter.
+Les vingt cas ne signifient pas tous que le nombre d'actions est inchangé à 0,1 % près. Une scission, une acquisition, une émission, un rachat ou une différence de classes peut modifier ce rapport. Le contrôle est une alerte de rapprochement, pas la confirmation juridique de chaque événement. Il ne valide pas une multiplication cours fois nombre d'actions. Aucun portefeuille courant n'utilise une capitalisation reconstruite.
 
-Le biais du survivant n'est pas mesuré par le test des fins de série. Aucun de nos titres n'a été retiré de la cote, mais c'est une tautologie : la liste des composants est un cliché de 2026, donc une entreprise sortie de l'indice en 2018 n'a jamais eu de fichier.
+**Les débuts d'historique.** Trente-sept titres n'ont pas de référence dans `premieres_cotations.csv`. Les 77 concordances restantes utilisent la même source que les prix et ne constituent donc pas une seconde source. Vingt titres ont une date d'entrée dans l'indice antérieure à leur première ligne Yahoo. Les débuts partagés par plusieurs séries suggèrent aussi des limites de couverture, sans démontrer que des introductions simultanées seraient impossibles.
 
-Un changement de symbole à l'intérieur d'un historique reste invisible. Yahoo sert toute la série sous le symbole d'aujourd'hui, sans marque de rupture.
+L'audit a vérifié séparément trois identités : GOOG classe C à partir du 3 avril 2014, DELL classe C à partir du 26 décembre 2018 en cotation conditionnelle, VRT industriel à partir du 10 février 2020 après le véhicule GSAH. Les sources et les règles sont dans `regles_historiques_prix.csv`. Ces raccordements ne sont pas détectés par une simple concordance de dates Yahoo.
 
-Les prix ajustés de Yahoo sont réécrits rétroactivement à chaque dividende et chaque division. Une nouvelle collecte ne redonnera pas les mêmes valeurs. Les fichiers conservés et leurs empreintes fixent un cliché daté ; les calculs faits à partir de ce cliché restent reproductibles, la collecte non.
+**Les variations extrêmes.** Leur concentration dans des épisodes de marché connus est un contrôle de plausibilité. Elle ne prouve pas que chacune des 127 variations ajustées de plus de 30 % est exacte. Les alertes restent visibles ; aucune n'est effacée au seul motif qu'elle ressemble à une crise.
 
-Enfin, `data/raw/premieres_cotations.csv` ne couvre que 76 des 113 titres. Il date de l'époque où l'univers en comptait 82 et n'a pas été régénéré.
+## V. Le recoupement externe effectué
 
-## VI. Une leçon de méthode
+Le contrôle SEC porte sur des actions en circulation, pas sur les cours. L'affirmation selon laquelle aucun recoupement public supplémentaire n'était possible était trop générale. L'audit a consulté le fichier de [distributions historiques de State Street](https://www.ssga.com/library-content/products/fund-data/etfs/us/spdr-etf-historical-distributions.xlsx).
 
-Trois tests ont d'abord échoué de la même façon, et je le consigne parce que le défaut est reproductible.
+Les 135 dates de distribution de SPY depuis 1993 concordent. Sur les 107 distributions de la période de construction, une différence dépasse l'arrondi au millième : le 17 décembre 2021, Yahoo porte 1,633 dollar et State Street 1,636431 dollar. Je conserve les deux valeurs dans le constat, sans réécrire la preuve brute. Remplacer les montants par ceux de State Street dans un calcul séparé modifie l'annualisation de SPY d'environ 0,01 point de base. Avant 2000, d'autres divergences existent et ne concernent pas la fenêtre de construction.
 
-Le test des prix négatifs comparait chaque valeur à zéro, et laissait passer la ligne de `HUBB` du 8 août 1977 où tous les prix sont absents : une valeur manquante ne satisfait aucune comparaison. La collecte des métadonnées traitait toute absence d'exception comme un succès, et enregistrait un dictionnaire vide comme une fiche valide. Sa deuxième version traitait toute réponse non vide comme un succès, et a accepté la description d'indices d'options homonymes des fonds `RSP` et `SPY`.
+La [page officielle de SPY](https://www.ssga.com/us/en/individual/etfs/state-street-spdr-sp-500-etf-trust-spy) donne une clôture de 773,17 dollars au 3 septembre 2026 ; le fichier Yahoo contient 773,1699829101562. Ce point concorde à l'arrondi. Les volumes de place et les volumes consolidés n'ont pas le même périmètre ; leur différence ne constitue pas à elle seule une erreur. Un cours et des distributions de SPY ne valident pas les historiques des 114 actions.
 
-À chaque fois, je vérifiais l'absence de l'échec que j'imaginais au lieu de vérifier la présence du succès attendu. La règle retenue est la seconde.
+Le calendrier de distribution officiel révèle une autre limite : les 26 dividendes de décembre inclus depuis 2000 sont payés fin janvier suivant. Notre modèle les assimile à une poche disponible au détachement et peut donc les réinvestir avant paiement. En conservant les mêmes cours et montants Yahoo mais en attendant les paiements officiels, avec la même unique date annuelle de réinvestissement, l'annualisation de SPY diminue de 4,10 points de base. Les créances impayées restent dans la richesse ; elles ne sont pas supprimées. Cette sensibilité mesure une approximation d'exécution, pas un défaut de conservation de valeur.
 
-Un quatrième défaut portait sur la reproductibilité. Le contrôle des divisions donnait deux résultats différents sur deux machines, parce que soixante-six couples entreprise et date de mesure portent deux déclarations distinctes et que le tri par défaut de pandas n'est pas stable entre ex aequo. Corrigé en triant sur la date de dépôt, seule date qui situe une déclaration par rapport à un événement.
+La dernière passe ajoute quatre clôtures de Sandisk, du 31 août au 3 septembre 2026, publiées sur sa [page investisseurs alimentée par LSEG](https://investor.sandisk.com/stock-information/historical-price-lookup). Elles concordent à l'arrondi avec le cliché : 1 566,70, 1 536,87, 1 553,40 et 1 554,99 dollars. Ce rapprochement porte sur des prix récents, pas sur toute la hausse depuis la séparation. Une sensibilité déplaçant la seule entrée de SNDK de sa cotation conditionnelle du 13 février 2025 à sa cotation ordinaire du 24 février réduit l'annualisation de P5 conservé de 64,21 points de base. Le rapport d'audit détaille ce choix d'exécution, dont l'effet est plus grand que celui des frais testés.
+
+## VI. Ce qui reste ouvert
+
+Les dates de paiement des actions, les identités historiques des autres titres, les opérations sur titres et un échantillon de cours de plusieurs entreprises demandent encore un rapprochement externe. Une scission peut être incorporée dans un cours retraité sans que le moteur reconstruise les titres distribués. La version conservée reste donc une simulation sur séries retraitées, pas un registre certifié de titres détenus.
+
+Le test des fins de série ne mesure pas le biais du survivant. La composition de l'indice et les rapports sont récents, les entreprises sorties du périmètre n'ont pas été recherchées systématiquement. Les niveaux et classements rétrospectifs ne constituent pas une stratégie connue à l'époque.
+
+Yahoo peut réviser son historique lors d'une nouvelle collecte. Les CSV et empreintes fixent un cliché dont les traitements sont reproductibles ; ils ne figent pas la réponse future du fournisseur. Le carnet de collecte est conservé comme trace de démarche, séparément du programme de reconstruction.
+
+## VII. La leçon de méthode conservée
+
+Les premiers contrôles avaient laissé passer des prix absents, une réponse descriptive vide et des instruments homonymes. Je conserve la règle qui en est sortie : vérifier que le résultat attendu est présent, pas seulement qu'une exception n'a pas été levée.
+
+Cette règle vaut aussi pour l'audit. Un moteur qui conserve la richesse peut utiliser le mauvais titre ou le mauvais calendrier de paiement. Un rapprochement SEC stable peut comparer les mauvaises dates de mesure. Un chiffre ancien peut rester dans une note alors que le fichier a changé. Les preuves, les corrections et les limites doivent donc rester attachées aux résultats.
```

</details>

### `research/master_context.md`

Mettre le point de reprise à l’étape 2 tout en conservant les sections pédagogiques antérieures.

Avant : `5ebc4a4b237f91dedf2c914bbfb0b671b8356d9819580ee8b42d5ed539415707`. Après : `89f5d14bbd566c782f28abdea4fcb18e2af9371603e282525b2ad92f66b688d0`.

Lignes physiques : 930 avant, 930 après.

Les repères `@@` indiquent les lignes avant et après. `-` contient le texte retiré, `+` le texte retenu.

<details>
<summary>Contenu exact des changements</summary>

```diff
--- research/master_context.md avant
+++ research/master_context.md après
@@ -14,5 +14,5 @@
 ## 0. OÙ J'EN SUIS MAINTENANT
 
-Je construis un univers documenté d'entreprises du S&P 500 exposées à la chaîne des infrastructures de calcul liées à l'IA. Cet univers servira ensuite à construire et comparer plusieurs portefeuilles. Il n'oblige pas à détenir toutes les entreprises retenues et il ne fixe aucune pondération.
+L'univers exploratoire de l'étape 1 contient 113 entreprises, 114 titres avec les classes d'Alphabet. L'étape 2 construit dix groupes dans deux modes de gestion. La reconstruction locale et les tests ont été repris le 8 septembre 2026 ; cette étape reste ouverte sur les réserves de données, de paiement des dividendes et d'interprétation décrites dans `research/audit_etape_2.md`. Les règles courantes sont dans `research/portefeuilles.md`, la progression dans `research/plan_projet.md`. Les options pédagogiques anciennes ne remplacent pas ces décisions datées.
 
 La règle actuelle est la version III de `research/selection_rule.md`. Les résultats se trouvent dans `research/univers_selection.md`, les corrections expliquées dans `research/corrections_2026-09-05.md`, et les chiffres recalculés dans `data/processed/etat_projet.json`.
```

</details>

### `research/plan_projet.md`

Conserver le cheminement en datant les anciens résultats, corriger les chiffres et les conclusions, et remettre l’avancement en accord avec les réserves ouvertes.

Avant : `a8fe80ddb11e56cb553a974ca9d78437e687497e4ee34ddda6b1befcdd8b52af`. Après : `210671ddcaffb4d63d583ad8574d59c74beca8219609b03ef55ab9f79bfb1b16`.

Lignes physiques : 302 avant, 310 après.

Les repères `@@` indiquent les lignes avant et après. `-` contient le texte retiré, `+` le texte retenu.

<details>
<summary>Contenu exact des changements</summary>

```diff
--- research/plan_projet.md avant
+++ research/plan_projet.md après
@@ -1,5 +1,5 @@
 # Plan du projet et état d'avancement
 
-*AI Concentration Risk Research. 7 septembre 2026.*
+*AI Concentration Risk Research. Mise à jour du 8 septembre 2026 après audit.*
 
 Ce document dit où en est le projet, selon quel découpage, et à quelles conditions une étape est considérée comme close. Il existe parce qu'un audit externe a constaté que ce découpage n'apparaissait dans aucun fichier du dépôt : il ne vivait que dans les échanges de travail.
@@ -12,5 +12,5 @@
 |---|---|---|
 | 1 | Construire un univers d'entreprises exposées à la chaîne des infrastructures de calcul | **close**, version exploratoire |
-| 2 | Construire les portefeuilles à partir de cet univers | en cours, phase 1 sur 8 close |
+| 2 | Construire les portefeuilles à partir de cet univers | en cours, construction rejouée ; réserves de données et de méthode ouvertes |
 | 3 | Mesurer le risque, ses sources et son comportement en crise | non commencée |
 | 4 | Étudier la couverture et la diversification | non commencée |
@@ -27,5 +27,5 @@
 Huit phases, cinquante-cinq tâches. La répartition indique qui produit quoi : **A** pour l'auteur, **C** pour l'assistant.
 
-### Phase 0 — Décisions avant collecte — **close**
+### Phase 0 : Décisions avant collecte : **close**
 
 | | Tâche | | État |
@@ -37,56 +37,58 @@
 Les deux benchmarks retenus sont `SPY`, réplique du S&P 500 pondéré par capitalisation, et `RSP`, réplique de sa version équipondérée. Trois indices sont collectés en complément pour le contexte et le contrôle.
 
-### Phase 1 — Collecte — **close**
+### Phase 1 : Cliché de prix collecté, couverture auxiliaire partielle
 
 | | Tâche | | État |
 |---|---|---|---|
 | 4 | Correspondance CIK vers symbole | C | faite, `BRK.B` interrogé sous `BRK-B` |
-| 5 | Cours quotidiens bruts | A | 113 séries |
+| 5 | Cours quotidiens bruts | A | 114 séries pour 113 entreprises |
 | 6 | Cours quotidiens ajustés | A | mêmes fichiers |
 | 7 | Dividendes | A | mêmes fichiers |
 | 8 | Divisions d'actions | A | mêmes fichiers |
-| 9 | Nombre d'actions en circulation | A | 8 987 lignes, 112 entreprises |
+| 9 | Nombre d'actions en circulation | A | 8 987 lignes de notions différentes, CMS absent |
 | 10 | Séries de comparaison | A | 2 fonds et 3 indices |
 | 11 | Calendrier de bourse | A | 8 458 séances depuis 1993 |
 | 12 | Manifeste de collecte | A | empreintes et limites écrites |
 
-### Phase 2 — Contrôle de la donnée brute — **close**
-
-Les résultats sont écrits dans `data/processed/controle_prix.csv`, une ligne par anomalie, avec le fichier, le test, la date et un détail. Chaque bloc de `src/controler_prix.ipynb` réécrit ses propres tests et laisse les autres intacts, de sorte qu'on peut le relancer seul.
-
-| | Tâche | | État |
-|---|---|---|---|
-| 13 | Trous dans les séries et séances absentes | A | 73 anomalies |
-| 14 | Variations quotidiennes aberrantes | A | 128 anomalies |
+Le fichier auxiliaire des actions contient 6 444 observations `actions` pour 109 entreprises, 172 observations `actions_bilan` pour deux entreprises, 302 moyennes pondérées pour trois entreprises et 2 069 mesures de flottant en dollars. Ces notions ne sont pas interchangeables. CMS n'y figure pas ; Meta n'a pas de nombre instantané dans ce fichier, et Alphabet et Dell n'ont que les notions alternatives indiquées. Cette couverture suffit aux contrôles partiels décrits, pas à une capitalisation exhaustive. Les portefeuilles équipondérés n'utilisent aucune de ces notions comme poids.
+
+### Phase 2 : Contrôle de la donnée brute, réserves ouvertes
+
+Les résultats sont écrits dans `data/processed/controle_prix.csv`. Le notebook appelle maintenant `src/controle_prix.py`, qui rejoue tous les contrôles locaux sans acquisition. Le résumé conserve les tests à zéro. Le manifeste atteste les entrées du calcul, pas la validation économique de toutes les anomalies.
+
+| | Tâche | | État |
+|---|---|---|---|
+| 13 | Trous dans les séries et séances absentes | A | 74 anomalies |
+| 14 | Variations quotidiennes aberrantes | A | 129 anomalies |
 | 15 | Cohérence de l'ajustement | A | aucune anomalie |
 | 16 | Vérification contre une seconde source | A | 20 divisions non confirmées |
-| 17 | Cohérence des dates de première cotation | A | 56 anomalies |
+| 17 | Cohérence des dates de première cotation | A | 57 anomalies |
 | 18 | Devise et place de cotation | A | aucune anomalie |
-| 19 | Retraits de cote et changements de symbole | A | 8 393 anomalies |
+| 19 | Retraits de cote et changements de symbole | A | 8 394 anomalies |
 | 20 | Remise du rapport de contrôle intégral | A | `research/controle_donnees_prix.md` |
 
-**Tâche 13.** Quatorze séances absentes de `SPXEW` entre 2015 et 2019, et cinquante-neuf séries antérieures au calendrier de bourse, ce dernier ne remontant qu'à 1993.
-
-**Tâche 14.** Cent vingt-six variations ajustées de plus de 30 %, une barre incohérente sur `HUBB` au 5 mai 2021 où l'ouverture est inférieure au minimum, et une ligne sans aucun prix sur `HUBB` au 8 août 1977. Cette dernière n'était pas détectée par le test des prix négatifs : une valeur manquante ne satisfait aucune comparaison. Un test explicite a été ajouté.
-
-**Tâche 15.** Le prix ajusté de Yahoo se reconstruit à partir du prix de clôture et des dividendes selon une convention multiplicative, le dividende étant retiré du prix de départ et non ajouté au prix d'arrivée. La formule additive s'écarte jusqu'à 8 % sur `JCI` ; la formule multiplicative reste sous 5 × 10⁻⁵ sur les 118 fichiers. Tous les écarts de la formule additive tombent sur des jours de détachement, aucun ailleurs.
-
-**Tâche 16.** Aucune source externe automatisable n'a été trouvée sans compte : Stooq sert désormais ses fichiers derrière une vérification anti-robot. Le contrôle retenu confronte les divisions d'actions déclarées par Yahoo au nombre d'actions déposé à la SEC au trimestre suivant, deux collectes d'origines indépendantes. Sur 56 divisions depuis 2010, 9 ne sont pas encadrées par des dépôts et 20 ne sont pas confirmées.
-
-Ces vingt cas ne sont pas des erreurs de collecte. La colonne `Stock Splits` de Yahoo contient deux natures d'événements : les divisions véritables, que la SEC confirme, et les facteurs d'ajustement de prix consécutifs à une scission, où le nombre d'actions ne bouge pas. `MMM` en avril 2024 pour Solventum, `IBM` en novembre 2021 pour Kyndryl. **Conséquence pour la tâche 34** : le facteur cumulé des divisions ne peut pas être lu directement dans cette colonne.
+**Tâche 13.** Quatorze séances absentes de `SPXEW` entre 2015 et 2019, et soixante séries antérieures au calendrier de bourse, ce dernier ne remontant qu'à 1993.
+
+**Tâche 14.** Cent vingt-sept variations ajustées de plus de 30 %, une barre incohérente sur `HUBB` au 5 mai 2021 où l'ouverture est inférieure au minimum, et une ligne sans aucun prix sur `HUBB` au 8 août 1977. Cette dernière n'était pas détectée par le test des prix négatifs : une valeur manquante ne satisfait aucune comparaison. Un test explicite a été ajouté.
+
+**Tâche 15.** Le prix ajusté de Yahoo se reconstruit à partir du prix de clôture et des dividendes selon une convention multiplicative, le dividende étant retiré du prix de départ et non ajouté au prix d'arrivée. La formule additive s'écarte jusqu'à 8 % sur `JCI` ; la formule multiplicative reste sous 5 × 10⁻⁵ sur les 119 fichiers. Tous les écarts additifs dépassant le seuil de 10⁻⁴ tombent sur des jours de détachement. Il subsiste ailleurs de petits écarts numériques, jusqu'à 4,83 × 10⁻⁶ : écrire « aucun écart » aurait été trop fort.
+
+**Tâche 16.** Le rapprochement des divisions avec les comptes SEC couvre 56 événements depuis 2010 : 9 sans encadrement exploitable, 20 incompatibles avec un simple rapport d'actions égal au facteur Yahoo, 27 compatibles dans la tolérance de 2 %. Je vérifie les dates de mesure et de dépôt des observations encadrantes. Ce contrôle n'est ni une validation indépendante des cours ni une preuve exacte de chaque division. L'audit du 8 septembre ajoute le rapprochement de 135 distributions de SPY avec State Street et un cours de clôture public, détaillés dans le rapport de contrôle.
+
+Ces vingt cas ne suffisent pas à qualifier une erreur de collecte. `Stock Splits` contient aussi des facteurs liés aux scissions ; acquisitions, émissions, rachats et classes d'actions modifient également le rapport SEC. Je ne peux donc ni dire que le nombre d'actions est inchangé dans tous les cas ni multiplier aveuglément cette colonne pour reconstituer une capitalisation.
 
 **Tâche 19.** Aucune série ne s'arrête avant la dernière séance du calendrier, ce qui ne prouve rien : la liste des composants étant un cliché de 2026, une entreprise retirée de la cote n'a jamais eu de fichier. Six dénominations divergent entre Yahoo et le S&P 500, toutes des variantes d'écriture sauf Schlumberger, devenu SLB N.V.
 
-En cherchant l'origine de la plus forte variation de la liste, `HUBB` au 31 octobre 1994 à +885,9 %, j'ai trouvé un défaut que le plan n'avait pas prévu de tester. Ce n'est pas un mouvement de marché mais la soudure entre un segment fabriqué et le début des vraies cotations. **Huit mille deux cent soixante-douze lignes portent un volume nul et quatre cours identiques, égaux à la clôture de la veille**, réparties sur 44 fichiers, dont 41 % de l'historique de `HUBB` et 18 % de celui de `CRH`. Elles produiraient des rendements nuls et abaisseraient toute volatilité calculée sur les périodes anciennes. Deux tests ajoutés, séance sans transaction et prix figé.
-
-**Tâche 20.** Rapport intégral dans `research/controle_donnees_prix.md` : vingt-trois tests, huit mille six cent soixante-dix anomalies sur 1 043 940 lignes, cent fichiers concernés sur cent dix-huit. Le rapport liste aussi les tests restés à zéro, que le fichier de contrôle ne peut pas montrer.
-
-**Tâche 17.** Trente-sept fichiers de prix n'ont aucune entrée dans `data/raw/premieres_cotations.csv`, construit du temps où l'univers comptait 82 entreprises et jamais régénéré depuis. Sur les 76 restants les dates concordent, mais ce zéro ne prouve rien : les deux fichiers viennent de la même source.
-
-Le résultat utile vient de la contrainte logique inverse. Dix-neuf entreprises sont entrées dans le S&P 500 avant la première ligne de prix que Yahoo nous donne. Douze séries commencent exactement le 17 mars 1980, neuf le 21 février 1973, huit le 2 janvier 1962. Aucune entreprise n'introduit ses actions le même matin que onze autres : ce sont les strates de départ de la base de Yahoo. **Une date de début de série ne dit pas quand le titre a commencé d'exister, elle dit à partir de quand Yahoo en parle.** À retenir pour les tâches 21 et 27.
-
-**Tâche 18.** Les 118 fichiers sont libellés en dollars, sur des places américaines, avec les seuls décalages horaires de New York. Les métadonnées descriptives sont collectées dans `data/raw/metadonnees_titres.csv`. Aucune anomalie après correction.
-
-Trois versions ont été nécessaires, et les trois échecs relèvent du même défaut de conception. La première interrogeait Yahoo avec la valeur de la colonne `symbole`, qui vaut `BRK.B` dans le fichier de Berkshire alors que la donnée avait été collectée sous `BRK-B` ; Yahoo répond un dictionnaire vide sans lever d'erreur, et le compteur annonçait 118 succès pour 117. La deuxième traitait toute réponse non vide comme un succès ; interrogée avec `^RSP` et `^SPY`, elle a reçu la description d'indices d'options homonymes, réels mais sans historique de prix. La troisième exige une date de première transaction, seule preuve qu'il s'agit d'un instrument négociable.
+En cherchant l'origine de la plus forte variation de la liste, `HUBB` au 31 octobre 1994 à +885,9 %, j'ai repéré la transition entre un segment sans volume et une série négociée. Le contrôle relève 8 273 lignes de prix figés à volume nul. Pour HUBB, 5 510 lignes satisfont ce critère strict ; 5 561 ont un volume nul, ce qui est une autre grandeur. Ces motifs justifient un traitement prudent, pas la certitude que chaque séance sans volume est fictive. Le filtre courant et les cours portés sont décrits dans `portefeuilles.md`.
+
+**Tâche 20.** Le rapport est dans `research/controle_donnees_prix.md`. Le cliché contient 1 057 439 lignes dans 119 fichiers. Les contrôles historiques produisent 8 674 signalements sur 101 fichiers ; un signalement n'est pas une erreur confirmée. Les vérifications structurelles supplémentaires et leur couverture sont indiquées dans le rapport d'audit.
+
+**Tâche 17.** Trente-sept fichiers de prix n'ont aucune entrée dans `data/raw/premieres_cotations.csv`, construit du temps où l'univers comptait 82 entreprises et jamais régénéré depuis. Sur les 77 restants les dates concordent, mais ce zéro ne prouve rien : les deux fichiers viennent de la même source.
+
+Le résultat utile vient de la contrainte logique inverse. Vingt entreprises ont une date d'entrée dans le S&P 500 antérieure à la première ligne de prix fournie. Des débuts communs, douze séries au 17 mars 1980, neuf au 21 février 1973 et huit au 2 janvier 1962, suggèrent des limites de couverture de Yahoo. Plusieurs introductions le même jour ne seraient pas impossibles ; ce motif n'en est pas une preuve. Une date de début disponible n'est pas une date d'IPO vérifiée.
+
+**Tâche 18.** Les 119 fichiers sont libellés en dollars, sur des places américaines, avec les seuls décalages horaires de New York. Les métadonnées descriptives sont collectées dans `data/raw/metadonnees_titres.csv`. Aucune anomalie après correction.
+
+Trois versions de la collecte descriptive ont été nécessaires : une réponse vide avait été comptée comme un succès, puis des indices d'options homonymes avaient été acceptés pour `SPY` et `RSP`. Une date de première transaction est nécessaire mais ne prouve pas à elle seule l'identité. Je contrôle aussi le symbole demandé, le type attendu, la devise et le raccordement au fichier.
 
 **La règle qui en sort : vérifier la présence du succès attendu, jamais l'absence de l'échec imaginé.** Le même défaut avait produit la valeur manquante non détectée de la tâche 14.
@@ -94,11 +96,11 @@
 La colonne `symbole` de `BRK-B.csv` conserve `BRK.B` alors que la collecte s'est faite sous `BRK-B`. Le fichier de prix est correct, son étiquette de provenance ne l'est pas. Écart documenté plutôt que corrigé, pour ne pas invalider l'empreinte du manifeste.
 
-Une première version de ce contrôle donnait deux résultats différents sur deux machines pour `DUK` au 3 juillet 2012. Cause : soixante-six couples entreprise et date de mesure portent deux déclarations distinctes, l'entreprise réexprimant une date déjà publiée après un regroupement, et le tri par défaut de pandas n'est pas stable entre ex aequo. Corrigé en triant explicitement sur la date de dépôt plutôt que sur la date de mesure, une déclaration ne pouvant refléter une division que si elle a été écrite après. Les deux exécutions concordent désormais à la sixième décimale.
+Une première version du contrôle SEC dépendait du tri entre déclarations ex aequo. Le tri est désormais explicite et stable. L'audit ajoute une condition omise : la date de mesure doit elle aussi encadrer l'événement, pas seulement la date de dépôt. Un dépôt postérieur peut encore rapporter un nombre d'actions antérieur. Les observations encadrantes sont enregistrées pour rendre ce choix vérifiable.
 
 `DUK` reste non confirmé pour une raison réelle : le regroupement de juillet 2012 est simultané à l'absorption de Progress Energy, deux événements que le nombre d'actions ne permet pas de séparer.
 
-Un point reste ouvert sur cette phase : le niveau manuel du protocole de seconde source, un échantillon relevé à la main sur un site public, n'a pas encore été exécuté.
-
-### Phase 3 — Décisions en voyant les données — **close**
+Le recoupement externe reste partiel : les distributions de SPY, une de ses clôtures et quatre clôtures de Sandisk ont été rapprochées, mais les historiques des 114 actions et les opérations sur titres ne sont pas tous corroborés. Je garde cette phase ouverte sur cette réserve au lieu d'assimiler présence de contrôles et validation de toute la donnée.
+
+### Phase 3 : Décisions en voyant les données : **close**
 
 | | Tâche | | État |
@@ -115,25 +117,25 @@
 | 30 | Portefeuilles par canal d'exposition | A | faite dans la tâche 24 |
 
-**Tâche 21.** Période retenue : **du 1er janvier 2000 au 4 septembre 2026**, chaque titre entrant à sa première cotation réelle, celle qui suit ses éventuelles lignes de remplissage.
-
-Quatre-vingts titres sont présents dès le premier jour, trente-trois arrivent ensuite, jamais plus de cinq la même année. La composition évolue donc, comme celle de l'indice auquel elle sera comparée.
-
-Trois raisons. La période traverse quatre régimes de tension de natures différentes, 2000-2002, 2008, mars 2020 et 2022, là où un départ en 2007 n'en aurait offert que trois. L'éclatement des valeurs technologiques de 2000 est un épisode de concentration technologique qui a mal fini, ce qui le rend directement pertinent pour un sujet portant sur la concentration technologique. Et seules trente lignes de remplissage subsistent après 2000, dans sept fichiers, toutes identifiées dans `data/processed/controle_prix.csv` et donc écartables ligne à ligne plutôt qu'en tronquant une période entière.
-
-Exiger que les 113 titres soient présents sur toute la période aurait ramené l'étude à dix mois, puisque `GEV` et `CEG`, nées de scissions récentes, ne cotent que depuis 2024 et 2022. Ce sont précisément des entreprises que le sujet vise.
+**Tâche 21.** Période retenue : **de la clôture du 3 janvier 2000 à celle du 4 septembre 2026**, chaque titre entrant à sa première observation admissible selon les règles d'identité et de qualité écrites dans `portefeuilles.md`.
+
+Quatre-vingt-une entreprises et autant de titres sont présents au départ. Trente-trois titres sont ensuite admis, dont une seconde classe d'Alphabet : cela fait trente-deux entreprises supplémentaires. Les dates admissibles tiennent compte des corrections GOOG, DELL et VRT. La composition ne reproduit pas un indice historique, elle ajoute les survivants de l'univers actuel lorsqu'un historique utilisable apparaît.
+
+Trois raisons avaient conduit au départ en 2000 : observer l'éclatement technologique, la crise financière, mars 2020 et 2022 ; conserver un historique long ; traiter séparément les données suspectes. L'audit retient 18 cours portés après les corrections d'identité, au lieu d'effacer le rendement du jour de reprise. La présence de ces épisodes ne constitue pas encore leur définition statistique, qui appartient à l'étape 3.
+
+Exiger que les 113 entreprises soient présentes aurait ramené l'étude à la fenêtre débutant le 27 octobre 2025, première observation de Qnity. GEV et CEG, issues de scissions en 2024 et 2022, illustrent aussi les historiques courts, mais ne déterminent pas la date de départ commune la plus tardive.
 
 **Tâche 22.** Rendements **quotidiens**, soit environ 6 700 observations sur la période.
 
-Le quotidien est retenu parce qu'il se laisse agréger et que l'inverse est impossible : on passe du jour à la semaine ou au mois, jamais du mois au jour. Il donne aussi le nombre d'observations nécessaire pour parler d'événements rares, alors qu'une base mensuelle n'en offrirait que 320 et qu'un krach d'une journée y disparaîtrait.
-
-Sa faiblesse est connue et sera dite : à l'échelle du jour, une part du mouvement relève de la mécanique de marché plutôt que de l'information, et les corrélations quotidiennes sont mécaniquement plus basses que les corrélations réelles. Les résultats principaux seront donc rapportés en quotidien et en mensuel. S'ils divergent, la divergence sera expliquée et non arbitrée.
-
-**Tâche 23.** **Rendement total**, donc la colonne `Adj Close`, pour tous les calculs de performance et de risque. Les deux fonds de comparaison seront pris de la même façon ; `^GSPC`, qui est un indice de prix, ne servira que de repère de contexte et n'entrera dans aucune comparaison de performance.
-
-L'écart entre les deux mesures atteint deux points de rendement annuel en moyenne sur les 112 titres disponibles depuis 2000, six points sur Realty Income, cinq sur Southern, Duke et CenterPoint. Sur Southern, dix mille placés en janvier 2000 deviennent soixante-trois mille au cours seul et deux cent onze mille dividendes réinvestis : les deux tiers du gain sont dans les dividendes.
-
-La raison n'est pas la propreté de la mesure mais l'orientation de son erreur. L'univers contient deux populations, des fabricants de puces qui ne distribuent presque rien et des producteurs d'électricité et des foncières qui distribuent l'essentiel de leur résultat. Un portefeuille pondéré par capitalisation est dominé par les premiers et perdrait peu à ignorer les dividendes ; un portefeuille équipondéré, où les seconds pèsent autant et sont nombreux, en perdrait beaucoup. Mesurer sans les dividendes handicaperait donc systématiquement l'équipondéré, c'est à dire précisément le terme de comparaison qui sert à tester si la concentration ajoute du risque. **Le biais pointerait droit vers la conclusion recherchée.**
-
-Réserve : le rendement total suppose des dividendes réinvestis dans le titre le jour du détachement, sans impôt ni frais. Aucun investisseur n'obtient exactement cela. C'est la convention standard, comparable d'un titre à l'autre, et celle de `^SP500TR`.
+Le quotidien est retenu parce qu'il se laisse agréger et que l'inverse est impossible : on passe du jour à la semaine ou au mois, jamais du mois au jour. Il donne davantage d'observations pour étudier les événements rares, alors qu'une base mensuelle n'en offrirait qu'environ 320 et pourrait masquer un krach suivi d'une reprise dans le même mois. Cela ne garantit pas un nombre suffisant d'extrêmes indépendants pour estimer précisément les queues de distribution.
+
+Sa faiblesse est connue : des cotations non synchrones et la microstructure peuvent déformer les corrélations quotidiennes. Il n'existe pas une corrélation « réelle » nécessairement supérieure. Les rendements portés doivent être signalés et les résultats comparés en quotidien et en mensuel, sans choisir la fréquence qui confirme l'intuition.
+
+**Tâche 23.** Je retiens une richesse incluant les dividendes. La décision initiale d'utiliser `Adj Close` a été remplacée par la tâche 28 : `Close` et `Dividends`, créance au détachement puis réinvestissement annuel, dans les portefeuilles et dans SPY/RSP. Les séries Yahoo ajustées restent séparées pour le contrôle. La formule multiplicative qui reproduit Yahoo ne remplace pas l'identité additive d'un compte de titres et d'espèces.
+
+L'écart moyen entre annualisation Yahoo ajustée et annualisation de prix vaut 2,05 points sur les 114 titres, chacun sur sa fenêtre disponible depuis 2000. Seulement 81 titres couvrent toute la période : ce n'est pas une moyenne de 112 historiques complets. Sur Southern, 10 000 deviennent 63 398 au cours seul et 211 679 selon Yahoo ajusté. La différence représente environ 73,5 % du gain ajusté au-dessus de la mise initiale ; elle mêle distributions et convention de réinvestissement, pas une attribution causale de la performance.
+
+Ignorer les dividendes défavorise les titres distributeurs. Cela peut modifier différemment les paniers selon leurs poids en utilities, immobilier ou technologie. La direction et l'ampleur de l'effet doivent être calculées sur les portefeuilles effectivement comparés ; elles ne se déduisent pas universellement de l'étiquette équipondérée ou pondérée par capitalisation.
+
+Réserve : les rendements totaux publiés et notre convention annuelle ne sont pas identiques. Même les deux formules de détachement, richesse additive et ajustement Yahoo multiplicatif, diffèrent. Les impôts et les délais effectifs de paiement restent hors du modèle principal. Ces choix sont écrits dans `portefeuilles.md` et mesurés séparément lorsqu'une source permet le rapprochement.
 
 **Réserve écrite avant tout calcul.** Les benchmarks équipondérés ne couvrent pas le début de la période : `RSP` commence en mai 2003, `^SPXEW` en décembre 2006. Toute comparaison exigeant l'un d'eux sera restreinte à la sous-période correspondante et le dira. Ces séries ne seront pas prolongées ni reconstruites.
@@ -141,17 +143,17 @@
 Une première version de cette décision fixait le départ à janvier 2007 pour disposer des deux benchmarks dès le premier jour. L'auteur a objecté que l'indisponibilité d'une seule comparaison ne justifiait pas de tronquer toute l'étude. L'objection est retenue.
 
-**Tâche 25, sans objet.** Le portefeuille concentré n'a pas à être défini séparément : les sept maillons de la tâche 24 couvrent la gamme, de six titres pour les acheteurs à trente-deux pour les vendeurs.
-
-**Tâche 27.** Chaque titre entre à sa **première séance réelle**, sans délai d'observation préalable.
-
-Un délai minimum aurait été justifié si les premières semaines de cotation étaient anormalement agitées. La mesure dit le contraire : sur les trente-trois titres entrant après 2000, la volatilité des soixante premières séances vaut 1,04 fois celle de la suite en médiane, et un seul titre présente une séance sans transaction dans ses deux premiers mois. Les rares cas élevés tiennent à la date d'entrée et non à la nouveauté, `CARR` arrivant le 19 mars 2020 en plein krach et `EQIX` en août 2000 pendant l'éclatement des valeurs technologiques.
+**Tâche 25, sans objet.** Le portefeuille concentré n'a pas à être défini séparément : les sept maillons de la tâche 24 couvrent la gamme, de six entreprises pour les acheteurs à trente-deux pour les vendeurs. Les acheteurs ont sept titres, puisque les deux classes d'Alphabet représentent une entreprise.
+
+**Tâche 27.** Chaque titre entre à sa **première observation admissible**, sans délai d'observation préalable, sous réserve du report d'une opération quand un cours nécessaire manque.
+
+La mesure initiale comparait la volatilité des soixante premières séances à celle de la suite. Elle ne permet pas d'attribuer les écarts à la nouveauté plutôt qu'au régime de marché, ni de prouver l'absence d'un effet d'introduction. Le départ immédiat est une convention exploratoire de disponibilité, à tester plus tard avec un délai fixé à l'avance. Les cotations conditionnelles et les raccordements historiques demandent une vérification d'identité distincte.
 
 **Tâche 30, faite dans la tâche 24.** Les sept maillons de chaîne sont les portefeuilles par canal d'exposition.
 
-**Tâche 29.** **Dix points de base sur le montant échangé**, soit 0,10 %, appliqués à la seule part du portefeuille réellement mouvementée lors d'un rééquilibrage ou de l'entrée d'un titre. La version conservée ne supporte de coût qu'à l'entrée d'un nouveau titre.
-
-Le taux couvre la commission et l'écart entre prix acheteur et prix vendeur. Sur des grandes capitalisations américaines très liquides cet écart vaut aujourd'hui un à cinq points de base et était plus large en 2000 ; dix points de base est une hypothèse prudente.
-
-Un rééquilibrage annuel déplaçant typiquement dix à vingt pour cent du portefeuille, le coût annuel attendu tourne autour de un à deux points de base. S'il se confirme négligeable, l'argument selon lequel le rééquilibrage coûterait trop cher tombe, et l'arbitrage entre les deux versions se joue alors sur le seul risque, ce qui est un résultat en soi.
+**Tâche 29.** Je conserve dix points de base sur le montant réellement échangé. L'audit applique ce coût aux achats et aux ventes, y compris le financement des entrées et les achats de réinvestissement des dividendes. La version conservée supporte donc aussi des frais de réinvestissement. La rotation est annualisée sur la durée observée et compte les deux côtés de chaque opération.
+
+Le taux représente globalement commission et écart acheteur-vendeur. Il n'est pas estimé titre par titre et ne couvre pas de façon démontrée l'impact de marché, les cotations conditionnelles ou la liquidité de toute la période. Je le garde comme hypothèse constante, sans le qualifier de prudent sur toutes les observations.
+
+La mesure des frais doit être comparée aux effets sur la performance et sur le risque. Un coût faible dans ce modèle n'annule ni les autres contraintes d'exécution ni l'arbitrage de rendement. Je ne peux pas conclure que le choix entre conserver et rééquilibrer se joue sur le seul risque.
 
 Deux limites. Le taux est une hypothèse et non une mesure, et il est tenu constant alors que les coûts réels ont fortement baissé depuis 2000. La conclusion sera testée à cinq et à vingt-cinq points de base.
@@ -159,41 +161,41 @@
 **Tâche 28.** Aucune poche de liquidités permanente. Les dividendes sont **accumulés en trésorerie puis réinvestis à la date annuelle**, répartis selon les poids cibles dans la version rééquilibrée et réinvestis dans le titre qui les a versés dans la version conservée.
 
-Le rendement du dividende de l'univers vaut 1,81 % par an en moyenne depuis 2000, médiane 1,57 %, avec 29 titres au-dessus de 3 %. La trésorerie représente donc environ 0,9 % du portefeuille en moyenne, ce qui est négligeable pour la mesure du risque.
-
-Les deux autres options ont été écartées. Le réinvestissement immédiat, qui était la lecture littérale de la tâche 23, suppose une opération à la seconde qu'aucun investisseur ne réalise. La mise de côté définitive aurait laissé dormir près de la moitié du capital initial au bout de vingt-six ans, abaissant la volatilité pour une raison étrangère au thème et faussant la comparaison avec des fonds intégralement investis.
-
-**Conséquence sur la tâche 23.** La colonne `Adj Close` réinvestit les dividendes le jour du détachement et ne peut donc plus servir pour les portefeuilles. Leurs rendements seront calculés à partir de `Close` et de `Dividends`, selon la convention identifiée à la tâche 15. `Adj Close` reste utilisé pour les benchmarks, qui sont des fonds où le réinvestissement est interne.
-
-**Tâche 26.** Chaque portefeuille est calculé en **deux versions**, l'une rééquilibrée à la première séance de janvier, l'autre jamais rééquilibrée. Vingt séries au lieu de dix.
-
-Ce n'est pas un réglage technique mais le dispositif central de l'étude. Sans rééquilibrage, les titres qui montent prennent seuls une place croissante et le portefeuille se concentre de lui-même, ce qui est précisément le phénomène observé sur le S&P 500 : sa concentration dans les valeurs liées à l'IA n'a été décidée par personne. La version rééquilibrée sert de témoin, le même thème et les mêmes entreprises mais sans laisser la concentration s'installer. L'écart entre les deux mesure ce que la concentration apporte et ce qu'elle coûte en risque.
-
-La fréquence annuelle est retenue parce qu'elle maintient les poids proches de l'égalité tout en limitant les transactions à vingt-six opérations sur la période, contre cent quatre en trimestriel. La fréquence trimestrielle, celle de `RSP`, sera testée en contrôle de robustesse ; si les deux conclusions coïncident, le choix sera déclaré sans effet, sinon la divergence sera expliquée.
-
-Dans la version non rééquilibrée, une entreprise entrant en cours de période reçoit le poids moyen des titres déjà présents, financé par une réduction proportionnelle des autres.
-
-**Tâche 24, décidée.** Composition complète dans `research/portefeuilles.md`, entreprise par entreprise. Onze portefeuilles, tous équipondérés : `P1` les 113 comme thermomètre du thème, `P2` et `P3` qui le recomposent selon le niveau de maturité, `P4` à `P10` qui décomposent la chaîne en sept maillons sommant exactement à 113, et `P11` laissé vide.
-
-Le découpage en maillons suit le champ `canal` de la sélection de l'étape 1 et non la classification GICS. Une première version reposait sur les secteurs boursiers et envoyait Alphabet, Meta, Amazon et Tesla dans un groupe résiduel, la classification GICS les rangeant hors du secteur technologique. C'est le défaut que la section 41 du contexte maître signalait déjà.
+La moyenne des rendements annuels de dividendes calculés titre par titre sur leurs fenêtres disponibles vaut 1,84 %, la médiane 1,62 %, et 30 titres dépassent 3 %. Ces fenêtres ne sont pas toutes identiques. La poche de créances et espèces des vingt séries corrigées représente 0,92 % en moyenne des photographies mensuelles, et 5,64 % au maximum ; ce sont des observations du modèle, pas la preuve d'un effet nul sur le risque.
+
+Le réinvestissement immédiat et l'accumulation définitive des distributions sont deux conventions alternatives. La première ne demande pas littéralement une opération « à la seconde » ; elle constitue une convention de rendement. La seconde introduit une poche croissante non rémunérée. Je retiens l'annuel pour les comparer de manière homogène, avec la réserve explicite sur les dates de paiement manquantes.
+
+**Conséquence sur la tâche 23.** `Close` et `Dividends` servent au compte de richesse, dans les portefeuilles et les deux fonds. `Adj Close` reste une série de contrôle du fournisseur. SPY et RSP distribuent leurs dividendes, ils ne les réinvestissent pas à la place du porteur.
+
+**Tâche 26.** Chaque portefeuille est calculé en **deux versions**, l'une remise à égalité à la date annuelle de janvier, l'autre sans remise à égalité annuelle. Les entrées et le réinvestissement des dividendes donnent lieu à des transactions dans les deux versions. Vingt séries au lieu de dix.
+
+Les deux versions permettent de suivre la dérive des poids et l'effet de la remise à égalité. Leur différence inclut aussi les transactions, les entrées, les facteurs de marché et les coûts : elle n'est pas un estimateur causal pur du coût de la concentration. La version annuelle ne supprime pas toute concentration entre deux janvier.
+
+La fréquence annuelle limite les remises à égalité, mais il faut y ajouter les entrées en cours d'année. Les dates effectives peuvent être reportées faute de cours. Une sensibilité trimestrielle reste à faire, avec les mêmes règles de dividendes et de coûts. L'accord de deux résultats ne prouverait pas que le choix de fréquence n'a aucun effet.
+
+Dans les deux versions, une entreprise entrant entre deux janvier reçoit un poids moyen par entreprise, financé par une réduction proportionnelle des positions et des espèces existantes. Une seconde classe d'actions partage le poids de son entreprise ; elle ne compte pas comme une entreprise nouvelle.
+
+**Tâche 24, décidée.** Composition complète dans `research/portefeuilles.md`, entreprise par entreprise. Dix portefeuilles construits dans deux modes de gestion, avec équipondération des entreprises à la constitution : `P1` le thème complet, `P2` et `P3` sa partition par maturité, `P4` à `P10` sa partition par canal puis secteur. `P11` est réservé et laissé vide. Les poids ne restent pas égaux entre deux opérations.
+
+Le découpage donne priorité au canal de l'étape 1 pour les acheteurs et vendeurs, puis utilise GICS pour subdiviser les fournisseurs. C'est donc une règle hybride. Les groupes immobilier et fournisseurs technologiques débordent respectivement les seules foncières de centres de données et les seuls fabricants d'outils pour puces. Leurs définitions exactes sont dans `portefeuilles.md`.
 
 Alphabet compte pour une ligne, les poids de ses deux classes d'actions étant additionnés.
 
-`P11`, dit portefeuille d'avenir, est réservé. Il sera constitué à la fin du projet, une fois les résultats connus, et présenté comme le seul portefeuille construit en connaissance de cause, distinct des dix autres définis à l'aveugle.
-
-Sept portefeuilles comptent moins de vingt-cinq titres et `P4` n'en compte que six. Ils seront mécaniquement plus volatils que `P1`, et cet effet de petit nombre devra être isolé à chaque comparaison.
+`P11`, dit portefeuille d'avenir, est réservé à une exploration fondée sur les résultats futurs du projet. Les dix autres groupes ont des règles antérieures à leur construction ; je ne dispose pas pour autant d'un protocole préenregistré prouvant qu'ils ont été choisis à l'aveugle.
+
+Sept groupes comptent moins de vingt-cinq entreprises. Cela réduit une possibilité de diversification à risques individuels et dépendances donnés, mais ne les rend pas nécessairement plus volatils que `P1`. L'étape 3 devra séparer la taille, les secteurs, les facteurs et les dépendances.
 
 Deux constats matériels ont conduit à cette forme.
 
-Le premier est matériel. Les nombres d'actions déclarés à la SEC commencent le 24 février 2009 et ne couvrent que 54 entreprises cette année-là. Reconstruire une capitalisation quotidienne depuis 2000 est donc impossible avec les données du dépôt, et non pas seulement difficile. Toute pondération par capitalisation portant sur nos propres portefeuilles est écartée sur la majeure partie de la période ; l'effet des poids reste mesuré par `SPY` contre `RSP`, deux fonds réels dont il n'y a rien à reconstruire.
-
-Le second est méthodologique. Une règle de sélection par la taille serait une règle de marché, étrangère au travail de l'étape 1, et elle empilerait un second anachronisme sur le premier : le dix premières capitalisations de 2000 ne contiennent pas les acteurs du calcul IA. La piste retenue construit les portefeuilles sur la classification établie à l'étape 1, canal d'exposition et niveau de maturité, qui ne demande aucun chiffre de marché et reste applicable du premier au dernier jour.
-
-Sept portefeuilles équipondérés sont à l'étude, non validés : les 113 comme thermomètre du thème, les 95 à exposition établie, les 18 à engagement documenté, puis quatre portefeuilles par maillon de chaîne, technologie, industrie, services aux collectivités et immobilier. La concentration s'y mesure par le nombre de titres détenus plutôt que par le poids, ce qui est plus proche de la question posée : un investisseur exposé au thème en détient dix ou vingt, pas cinq cents.
-
-**Discussion ouverte sur le biais de connaissance a posteriori.** L'univers est établi avec des rapports de 2026 et appliqué à des prix antérieurs. Raccourcir la période ne corrige rien, le biais tenant à la sélection et non à la longueur de l'historique. Trois issues ont été posées : commencer en 2026 et attendre, ce qui laisse zéro observation ; conserver l'historique en s'interdisant toute affirmation de performance réalisable et en ne traitant que la structure du risque ; ou refaire la sélection sur un millésime ancien, l'exercice 2018 par exemple, pour tester hors échantillon sur 2019-2026, ce qui règle le problème au prix d'une nouvelle collecte SEC complète. La deuxième issue est proposée pour maintenant, la troisième réservée pour plus tard. **Rien n'est tranché.**
-
-### Phase 4 — Construction — **close**
-
-Tout est produit par `src/construire_portefeuille.ipynb`.
+Le premier est matériel. Les nombres d'actions instantanés déclarés à la SEC commencent le 24 février 2009 et ne couvrent que 54 entreprises cette année-là. Reconstruire une capitalisation quotidienne depuis 2000 est donc impossible avec les données du dépôt, et non pas seulement difficile. Toute pondération par capitalisation portant sur nos propres portefeuilles est écartée sur la majeure partie de la période. `SPY` et `RSP` apportent deux références de pondération, mais leurs différences ne mesurent pas le seul effet des poids ; le compte du porteur est reconstruit selon notre convention commune de dividendes et de frais.
+
+Le second est méthodologique. Je choisis les groupes issus de la classification de l'étape 1 pour comparer les canaux et la maturité de l'exposition. Une pondération fondée sur des capitalisations connues à chaque date serait une autre comparaison pertinente ; elle ne serait pas anachronique du seul fait d'utiliser la taille. Employer des tailles actuelles dans le passé poserait en revanche ce problème. La classification retenue ne demande pas de capitalisation historique, mais elle reste elle-même fondée sur des informations récentes. Je ne transforme pas cette solution au manque de données en preuve de supériorité méthodologique.
+
+La proposition initiale de sept groupes était une piste de travail. Elle est remplacée par les dix groupes et leurs deux modes de gestion dans `portefeuilles.md`. Le nombre de lignes et la concentration des poids ne suffisent pas à décrire la concentration du risque, qui demande les dépendances entre titres.
+
+**Décision sur la connaissance a posteriori, précisée le 8 septembre.** Je conserve l'exercice rétrospectif sur l'univers actuel, avec interdiction d'en tirer une performance historiquement réalisable ou une attribution causale à l'IA. Les mesures relatives de risque ne sont pas immunisées contre ce biais. Une sélection datée sur un millésime ancien, puis testée sur des données ultérieures, reste une extension nécessaire pour une conclusion prédictive.
+
+### Phase 4 : Construction : **close**
+
+La reconstruction locale est `python -B -m src.construire_portefeuilles`. `src/construire_portefeuille.ipynb` appelle ce même traitement. Les sorties et leurs empreintes sont vérifiées après la construction ; le notebook ne redéfinit plus un second moteur.
 
 | | Tâche | | État |
@@ -201,5 +203,5 @@
 | 31 | Rendements individuels | A | `rendements_prix.csv`, `dividendes.csv` |
 | 32 | Alignement des dates | A | 6 709 séances, zéro écart |
-| 33 | Traitement des valeurs manquantes | A | 59 trous internes |
+| 33 | Traitement des valeurs manquantes | A | 18 cours portés, signalés séparément |
 | 34 | Reconstruction des capitalisations | A | sans objet, voir tâche 24 |
 | 35 | Poids cibles aux dates de rééquilibrage | A | `poids_cibles.csv` |
@@ -214,59 +216,59 @@
 **Le moteur.** Il suit des montants et non des poids, ce qui rend la dérive automatique et supprime toute renormalisation. Chaque jour, le montant d'un titre est multiplié par un plus son rendement de prix ; le dividende versé alimente une trésorerie attachée à ce titre, réinvestie à la première séance de janvier. Le rendement du portefeuille est la variation de la somme des montants et des trésoreries. Vingt séries en sortent, dix portefeuilles en version rééquilibrée et conservée.
 
-**Validation du moteur.** Appliqué à `SPY` avec la même logique, il donne ×8,299 contre ×8,451 pour le rendement total publié par Yahoo. L'écart de 1,81 % sur vingt-six ans, soit sept centièmes de point par an, correspond au réinvestissement différé à janvier voulu par la tâche 28. Second contrôle indépendant : `SPY` ressort neuf centièmes de point par an derrière `SP500TR`, ce qui correspond aux frais de gestion annoncés du fonds. Le pipeline reproduit donc spontanément un écart connu qu'il n'a pas cherché.
-
-**Coûts de transaction, mesure.** La rotation annuelle vaut 23 % pour `P1` rééquilibré et le coût correspondant 2,7 centièmes de point par an. La prévision de la tâche 29 annonçait un à deux centièmes, la mesure en donne deux à trois. **L'arbitrage entre rééquilibrer et conserver ne se joue donc pas sur les frais mais sur le seul risque**, ce qui était l'hypothèse à vérifier.
+**Validation du moteur.** Les identités de richesse et de frais sont contrôlées chaque jour, y compris les opérations, et un calcul indépendant en nombres de parts reproduit SPY. L'écart avec Yahoo ajusté mélange le calendrier de réinvestissement, la formule de détachement et les coûts ; il ne peut pas être attribué entièrement au délai jusqu'à janvier. Le rapprochement avec un indice publié reste un contrôle de plausibilité, pas une certification de tous les cours.
+
+**Coûts de transaction, mesure corrigée.** La rotation annualisée de `P1` rééquilibré vaut 24,24 % et la perte d'annualisation par rapport au même moteur sans frais vaut 2,87 points de base. Les vingt mesures sont dans `mesures_portefeuilles.csv`. Les sensibilités du rapport d'audit comparent la même construction à différents taux ; leur portée reste celle d'un modèle sans impact de marché.
 
 **Un défaut corrigé.** La première version des séries de comparaison appliquait aux indices le filtre de volume nul conçu pour les actions. Un indice ne s'échange pas et Yahoo lui attribue un volume nul sur toutes ses séances : le filtre effaçait l'intégralité de `^SP500TR` et de `^SPXEW`, et la première disparaissait du tableau sans message. Corrigé en n'appliquant le filtre qu'aux titres dont le champ `type` des métadonnées n'est pas `INDEX`. C'est le même défaut de conception que les trois de la phase 2 : une règle validée sur une population, appliquée sans examen à une autre.
 
-**Premier signal, à ne pas confondre avec un résultat.** Sur leur fenêtre commune de mai 2003 à septembre 2026, `SPY` rend 11,56 % par an pour une volatilité de 18,49 % et un repli maximal de 55,2 %, tandis que `RSP` rend 11,36 % pour une volatilité de 19,73 % et un repli de 59,9 %. Les mêmes cinq cents entreprises, la seule différence étant le poids : supprimer la concentration des poids n'a pas réduit le risque sur cette fenêtre, il l'a augmenté. L'analyse appartient à l'étape 3 et rien n'est conclu ici.
-
-**Rappel contraignant.** Les portefeuilles ressortent entre 11,0 % et 21,7 % par an quand `SPY` fait 8,35 %. Cet écart n'est pas un résultat sur l'IA, c'est la taille du biais de connaissance a posteriori : l'univers a été établi avec des rapports de 2026 puis appliqué à des prix antérieurs. Aucune affirmation de performance réalisable ne sera tirée de ces niveaux. Seules les grandeurs relatives sont exploitables.
-
-### Phase 5 — Contrôle des résultats — **close**
-
-| | Tâche | | État |
-|---|---|---|---|
-| 43 | Somme des poids égale à 1 | A | écart maximal 4 × 10⁻¹⁶ |
+**Comparaison descriptive, à ne pas confondre avec une attribution.** Les chiffres de 11,56 % et 11,36 % par an pour SPY et RSP concernaient les séries Yahoo ajustées sur leur fenêtre commune depuis mai 2003. Les références principales ont maintenant la convention annuelle commune aux portefeuilles ; leurs résultats sont dans l'audit. Les différences de poids, de rééquilibrage et de frais internes empêchent d'attribuer à la seule concentration l'écart entre les fonds.
+
+**Rappel contraignant.** L'écart entre les portefeuilles et SPY n'est pas une mesure de la taille du biais de connaissance a posteriori. Il combine la sélection, les secteurs, la pondération, les entrées et d'autres effets. Les mesures absolues comme relatives décrivent des paniers choisis aujourd'hui ; leur robustesse et leurs facteurs restent à étudier.
+
+### Phase 5 : Contrôle des résultats, identités vérifiées et interprétation réservée
+
+| | Tâche | | État |
+|---|---|---|---|
+| 43 | Somme des poids égale à 1 | A | écart maximal 4,45 × 10⁻¹⁶ |
 | 44 | Aucun poids négatif ni aberrant | A | aucun cas |
 | 45 | Nombre de titres présents par date | A | aucun cas |
 | 46 | Plausibilité des rendements cumulés | A | aucun cas |
-| 47 | Cohérence de l'agrégation | A | écart maximal 3 × 10⁻¹⁵ |
-| 48 | Reconstruction comparée aux indices publiés | A | trois écarts retrouvés |
-
-Les poids sont photographiés en fin de mois, soit 321 relevés et 196 110 lignes dans `data/processed/poids_mensuels.csv`. La fréquence mensuelle a été préférée à l'annuelle parce qu'une photo annuelle serait prise juste après un rééquilibrage, donc au moment où la dérive est nulle, et parce que cette série servira à l'étape 3 pour suivre la formation de la concentration.
-
-**Tâche 47, l'identité qui valide le moteur.** Si `P1` attribue 1/113 à chaque entreprise et `P2` 1/95 aux siennes, alors mélanger `P2` et `P3` dans les proportions de leurs effectifs doit redonner `P1` exactement. L'écart mesuré vaut 3 × 10⁻¹⁵ sur 6 709 jours, et 1 × 10⁻¹⁵ pour le mélange des sept maillons. Le moteur est algébriquement correct.
-
-**Tâche 48, trois écarts connus retrouvés.** `SPY` ressort 9,0 points de base par an derrière `SP500TR`, contre 9,45 annoncés par le fonds. `^GSPC` ressort 1,97 point derrière `SP500TR`, ce qui est la contribution des dividendes. Aucun de ces chiffres n'a été cherché ; ils sortent du calcul.
-
-**Une erreur de description corrigée.** Le troisième écart, `RSP` devant `^SPXEW` de 1,69 point par an, est impossible pour un fonds face à son indice. Explication : **`^SPXEW` est un indice de prix**, sans dividendes, et non la référence en rendement total de `RSP`. Il est l'équivalent équipondéré de `^GSPC`, pas de `^SP500TR`. Le seul benchmark équipondéré en rendement total est donc `RSP`, à partir de mai 2003 ; `^SPXEW` ne sert que de contrôle en prix. Le contrôle a révélé cette erreur en produisant un résultat impossible.
-
-**Une erreur de test corrigée.** La première version du contrôle 46 relevait 25 violations de l'encadrement du rendement du portefeuille par le pire et le meilleur de ses titres. Les 25 tombaient sur une date de rééquilibrage, où la valeur bouge aussi par le réinvestissement de la trésorerie et le prélèvement des frais. L'encadrement ne s'y applique pas ; le test exclut désormais ces 27 dates.
-
-**Replis maximaux mesurés**, cohérents avec l'histoire des marchés : `P9`, l'amont des puces, à −83 % lors de l'effondrement de 2001, `P6`, l'électricité, à −45 %, `P1` à −54 % contre −55 % pour `SPY`.
-
-**Résultat majeur de la phase.** Au 4 septembre 2026, la version conservée de `P1` porte 24,8 % sur Nvidia, contre un poids cible de 0,885 %. Dans `P5` conservé, Nvidia atteint 42,9 % ; dans `P4` conservé, Tesla atteint 59,5 %. Le poids maximal jamais atteint par un titre vaut 76,7 % dans `P4` conservé, contre 4,2 % pour le plus gros poids de `P1` rééquilibré au dernier relevé. **La concentration ne résulte d'aucune décision : elle résulte de l'absence de décision.**
-
-### Phase 6 — Tests — **close**
+| 47 | Cohérence de l'agrégation | A | identité quotidienne, écart inférieur à 10⁻¹² |
+| 48 | Reconstruction comparée aux indices publiés | A | contrôles de convention et oracle SPY, couverture externe partielle |
+
+Les poids sont photographiés à la dernière séance disponible de chaque mois, soit 321 relevés et 225 984 lignes, y compris les poids nuls, dans `data/processed/poids_mensuels.csv`. Le dernier relevé est au 4 septembre, fin du cliché et non fin du mois civil. La fréquence mensuelle permet de suivre la dérive entre les opérations ; une photographie annuelle n'aurait une dérive nulle que si elle était prise immédiatement après une remise à égalité.
+
+**Tâche 47, portée du contrôle.** La partition des entreprises permet une identité de mélange à poids initiaux égaux, sans frais et sans opérations différentes entre les sous-groupes. Cette identité ne certifie pas la trajectoire complète avec entrées et rééquilibrages. Le contrôle décisif porte maintenant chaque jour sur la richesse avant opérations, les rendements, les dividendes et les frais réellement facturés.
+
+**Tâche 48.** L'écart d'environ neuf points de base entre SPY ajusté et `SP500TR` est proche des frais internes annoncés du fonds, sans les identifier exactement : conventions, suivi de l'indice et fenêtres interviennent aussi. L'écart entre `^GSPC` et `SP500TR` est celui de deux conventions d'indice. Il ne se transpose pas automatiquement à la contribution des dividendes d'un compte espèces.
+
+**Une erreur de description corrigée.** `^SPXEW` est un indice de prix, sans dividendes. Que RSP, dividendes inclus, le dépasse n'a donc rien d'impossible ; c'était une comparaison de conventions différentes. Il reste un contrôle en prix, et RSP la référence équipondérée avec distributions à partir de mai 2003.
+
+**Une erreur de test corrigée par cet audit.** Exclure les dates de rééquilibrage du contrôle masquait une faiblesse. Réinvestir des espèces ne crée pas de richesse. Le rendement avant frais doit se raccorder à la moyenne des rendements totaux des positions, espèces à rendement nul incluses ; les frais expliquent ensuite la différence. Ce contrôle s'applique aussi les jours d'opération, sans leur donner une exemption.
+
+**Replis maximaux mesurés.** Les ordres de grandeur des séries corrigées sont de −83 % pour `P9` conservé, −45 % pour `P6`, −54 % pour `P1` et −55 % pour SPY reconstruit. Leurs dates, les deux modes de gestion et les fenêtres doivent accompagner une comparaison ; leur plausibilité historique ne prouve pas l'exactitude de toutes les observations.
+
+**Concentration, résultats mis à jour.** Les chiffres précédents, 24,8 % sur Nvidia dans `P1` conservé et 59,5 % sur Tesla dans `P4` conservé, correspondaient bien aux poids des fichiers avant cet audit. Les nouvelles règles d'entrée et d'identité ont changé les trajectoires : les mesures actuelles figurent dans le rapport d'audit. La dérive vient des rendements sous une règle de gestion choisie ; l'absence de remise à égalité est elle-même une décision, pas l'absence de toute décision.
+
+### Phase 6 : Tests : **close**
 
 | | Tâche | | État |
 |---|---|---|---|
 | 49 | Proposition des cas qui doivent faire échouer le code | C | `research/cas_de_test.md`, treize cas |
-| 50 | Écriture des tests | C | `tests/test_portefeuille.py`, douze tests |
-
-Chaque cas reproduit une erreur réellement commise pendant le projet ; un test qui n'a jamais rien attrapé ne prouve rien. Les données sont écrites à la main, trois à cinq lignes, pour que la réponse attendue se vérifie de tête, et aucun test ne lit les fichiers du dépôt.
+| 50 | Écriture des tests | C | 41 tests de l'étape 2, 92 tests dans l'ensemble du dépôt |
+
+Les tests combinent des défauts déjà rencontrés et des contre-exemples construits pour mettre les règles en difficulté. Les exemples courts vérifient la mécanique ; les replays sur le cliché vérifient l'intégration. Aucun ensemble de tests ne garantit l'absence de toute erreur. Les cas et leur couverture sont dans `research/cas_de_test.md`.
 
 Écrire les tests a d'abord exigé de sortir le moteur du notebook vers `src/portefeuille.py` : `import` sait lire un fichier `.py` et non un `.ipynb`. Le notebook importe désormais ses fonctions au lieu de les définir. Le partage du travail est acté à partir de là : les fichiers `.py` reviennent à l'assistant, les notebooks à l'auteur.
 
-**Le test a trouvé un défaut réel du moteur, et il changeait une conclusion.** Dans la version conservée, un titre entrant en cours de période recevait son montant sans que les titres déjà détenus soient réduits en face : le portefeuille créait de la valeur à chaque nouvelle cotation, trente-trois fois sur la période. La tâche 26 énonçait pourtant la bonne règle, une entrée financée par une réduction proportionnelle des autres ; le code en appliquait une autre.
-
-Corrigé, `P1` conservé passe de 12 464 à 8 978 en base 100, soit de 19,87 % à 18,40 % par an, et `P5` conservé de 30 266 à 18 501. **La lecture s'inverse** : avant correction, conserver l'emportait sur rééquilibrer presque partout ; après, le rééquilibrage l'emporte dans sept portefeuilles sur dix, et parfois largement, `P8` à 17,21 % contre 12,86 %. Les dix séries rééquilibrées ne sont pas touchées, le défaut ne concernait que la branche conservée.
-
-Les mesures de concentration tiennent, elles portent sur des poids relatifs et non sur des niveaux.
-
-Un second échec de test venait de la donnée d'essai et non du moteur : un titre y détachait un dividende de dix pour cent sans que son cours baisse, ce qu'aucun marché ne fait. Le moteur avait raison, l'exemple était incohérent.
-
-### Phase 7 — Documentation et clôture — en cours, 4 tâches sur 5
+**Le test a trouvé un défaut réel du moteur, et il changeait une conclusion.** Dans la version conservée, un titre entrant en cours de période recevait son montant sans que les titres déjà détenus soient réduits en face : le portefeuille créait de la valeur à chaque nouvelle cotation, lors des admissions effectuées par cette ancienne version. La tâche 26 énonçait pourtant la bonne règle, une entrée financée par une réduction proportionnelle des autres ; le code en appliquait une autre.
+
+Lors de cette correction antérieure à l'audit du 8 septembre, `P1` conservé était passé de 12 464 à 8 978 en base 100 et `P5` conservé de 30 266 à 18 501. Les fichiers présents au début de l'audit donnaient un avantage de performance à la version rééquilibrée dans six groupes sur dix, et non sept comme je l'avais écrit. Ces niveaux sont historiques : les corrections d'entrée, d'identité et de coûts de cet audit changent aussi les séries rééquilibrées. Les vingt résultats courants et leur comparaison avec ce cliché précédent sont publiés dans l'audit.
+
+Les poids relatifs du fichier précédent ont été recalculés et concordaient avec les chiffres du journal. Cela ne prouve pas qu'une correction d'entrée préserve toujours la concentration : les nouvelles dates et le financement des entrées peuvent la modifier.
+
+Un second échec de test avait été attribué à un dividende sans baisse de cours. Cette justification était fausse : une hausse de marché peut compenser le détachement. Le test doit accepter un dividende avec un cours stable ou en hausse et vérifier la richesse correspondante, sans imposer une baisse mécanique observée.
+
+### Phase 7 : Documentation et clôture : en cours, 4 tâches sur 5
 
 | | Tâche | |
@@ -275,5 +277,5 @@
 | 52 | Écriture des limites | A | **faite**, section IV et `portefeuilles.md` |
 | 53 | Mise à jour des notes | A | **faite** |
-| 54 | Intégration au pipeline | C | **faite**, `data/processed/pipeline_portefeuilles.json` |
+| 54 | Intégration au pipeline | C | **faite**, `data/processed/pipeline_portefeuilles.json`, commande locale documentée |
 | 55 | Commit | A | à faire |
 
@@ -284,7 +286,7 @@
 **Les capitalisations, tâche 34.** Les prix de Yahoo sont retraités des divisions d'actions ; les nombres d'actions déclarés à la SEC ne le sont pas. Les multiplier tels quels donnerait une capitalisation fausse d'un facteur égal au cumul des divisions. Aucun calcul du dépôt ne fait aujourd'hui cette multiplication. Le contrôle sera simple : une division d'actions ne doit produire aucun saut dans la série de capitalisation.
 
-**Les historiques courts, tâches 21 et 27.** Sur les 113 séries, la plus courte compte 216 séances, depuis le 27 octobre 2025. Exiger les 113 simultanément réduirait la période à dix mois.
-
-Cette fenêtre n'est pas calme pour autant. Le S&P 500 y enregistre un repli maximal de 8,89 %, entre le sommet du 27 janvier 2026 et le creux du 30 mars 2026. L'argument contre une période aussi courte n'est donc pas l'absence de tension, mais le manque de profondeur et de diversité des régimes de marché traversés. Les seuils définissant un épisode de stress restent à établir, et ils le seront avant toute comparaison.
+**Les historiques courts, tâches 21 et 27.** Sur les 114 séries pour 113 entreprises, la plus courte compte 216 séances, depuis le 27 octobre 2025. Exiger les 113 simultanément réduirait la période à dix mois.
+
+Cette fenêtre n'est pas dépourvue de mouvement : `^GSPC`, indice de prix, y présente un repli maximal de 9,10 %, tandis que `^SP500TR`, dividendes inclus, donne 8,89 %. Le chiffre précédent était défendable en rendement total mais ne précisait pas la série. Une fenêtre aussi courte manque surtout de profondeur et de diversité de régimes ; les épisodes de stress seront définis avant leur comparaison à l'étape 3.
 
 Le benchmark équipondéré `RSP` ne remonte par ailleurs qu'à 2003.
@@ -301,2 +303,8 @@
 
 **Univers provisoire.** Soixante-seize dossiers restent à examiner. La composition peut donc encore changer.
+
+## V. État après l'audit du 8 septembre 2026
+
+L'étape 2 n'est pas déclarée close. Le moteur, ses règles, ses tests et sa reconstruction locale ont été corrigés et rejoués. Les erreurs corrigées, les valeurs actuelles et les preuves sont dans `research/audit_etape_2.md` ; ce rapport prime sur les mesures historiques explicitement datées de ce journal.
+
+Restent ouverts le recoupement des prix et des opérations sur titres au-delà de l'échantillon, la disponibilité effective des dividendes à leur paiement, et la décision de sensibilité aux entrées et à la fréquence de gestion. Les risques, facteurs, stress, diversification et couvertures relèvent des étapes suivantes ; leur absence n'est pas une erreur de construction. Le commit reste une opération de l'auteur, séparée de la validation scientifique.
```

</details>

### `research/portefeuilles.md`

Raccorder chaque règle au moteur, préciser les identités, la disponibilité des prix, la convention synthétique des dividendes et les limites d’interprétation.

Avant : `cf6391c23dbff7de05da47764a74ab2fb7b3394a1367a014efa1e74f36c3b940`. Après : `4d2311a229c72710340df221447be43cd4aeb6bc413b77ca0574d74222de11d1`.

Lignes physiques : 147 avant, 159 après.

Les repères `@@` indiquent les lignes avant et après. `-` contient le texte retiré, `+` le texte retenu.

<details>
<summary>Contenu exact des changements</summary>

```diff
--- research/portefeuilles.md avant
+++ research/portefeuilles.md après
@@ -1,41 +1,53 @@
 # Portefeuilles de l'étude
 
-*AI Concentration Risk Research. Tâche 24 de la phase 3. 8 septembre 2026.*
+*AI Concentration Risk Research. Tâche 24 de la phase 3. Mise à jour du 8 septembre 2026 après audit.*
 
-Ce document fixe la composition des portefeuilles avant tout calcul. Il est écrit pour qu'aucune décision de construction ne puisse être révisée après avoir vu un résultat. Si une composition change, la modification sera datée et motivée ici même.
+Ce document fixe la composition et les règles courantes. Les premières règles ont été écrites avant la construction, mais les données avaient déjà été consultées. Je ne présente donc pas ce document comme un protocole préenregistré à l'aveugle. Les corrections de l'audit sont datées ici et détaillées dans `research/audit_etape_2.md`.
 
-## Règles communes
+## I. Règles communes
 
-Tous les portefeuilles sont **équipondérés**. Aucun ne demande de capitalisation boursière, ce qui les rend calculables sur toute la période : les nombres d'actions déclarés à la SEC ne commencent qu'en février 2009.
+Je construis dix portefeuilles, chacun dans deux versions. L'équipondération porte sur les entreprises, identifiées par CIK, à la constitution et aux rééquilibrages de la version annuelle. Les poids dérivent entre ces dates. La version conservée n'est pas remise à égalité chaque année.
 
-Chaque entreprise entre le jour de sa **première cotation réelle**, celle qui suit ses éventuelles lignes de remplissage. La composition grandit donc au cours du temps, comme celle de l'indice auquel elle est comparée. `P1` compte 81 titres au 3 janvier 2000 et 113 au 27 octobre 2025.
+La période va de la clôture du 3 janvier 2000 à celle du 4 septembre 2026. Elle contient 6 709 niveaux et 6 708 rendements. L'annualisation conventionnelle utilise 252 séances par an. Le départ est une base nette de constitution : je n'impute pas les frais de la mise initiale, ni ceux d'une liquidation finale. Les rendements sont nominaux, en dollars, avant fiscalité. Les fractions de titres sont autorisées, sans contrainte de taille ni d'impact de marché.
 
-**Alphabet compte pour une ligne.** Ses deux classes d'actions, `GOOG` et `GOOGL`, occupent deux fichiers de prix ; leurs poids sont additionnés et l'entreprise pèse comme n'importe quelle autre.
+Une entreprise entre à la clôture de sa première observation admissible ; son rendement commence à compter à la séance suivante. C'est une règle de disponibilité dans les données, pas la preuve d'une date d'IPO. La composition grandit, de 81 entreprises et 81 titres à 113 entreprises et 114 titres. Elle ne reproduit pas les entrées et sorties historiques du S&P 500.
 
-Les rendements sont **quotidiens** et **totaux**, dividendes réinvestis, colonne `Adj Close`.
+Alphabet compte pour une entreprise. `GOOGL` désigne la classe A et `GOOG` la classe C. Je retiens la classe C seulement à partir du 3 avril 2014, son historique Yahoo antérieur reprenant celui de la classe A. L'apparition d'une seconde classe partage le montant investi dans l'entreprise entre ses classes disponibles, sans lui attribuer le poids d'une nouvelle entreprise. Les listes ci-dessous nomment l'entreprise ; `appartenance.csv` conserve ses deux titres.
 
-Les termes de comparaison sont `SPY`, réplique du S&P 500 pondéré par capitalisation, et `RSP`, réplique de sa version équipondérée, tous deux en rendement total. Toute comparaison exigeant `RSP` commence en mai 2003.
+Deux autres limites d'historique sont fixées dans `data/review/regles_historiques_prix.csv`, avec leurs sources : `DELL` commence le 26 décembre 2018 pour la classe C, en cotation conditionnelle avant la cotation ordinaire du 28 décembre ; `VRT` commence le 10 février 2020 après le rapprochement de Vertiv et du véhicule coté GSAH. Les segments antérieurs restent dans les fichiers bruts mais ne servent pas à ces portefeuilles. Ces corrections portent sur l'identité du titre ou de l'activité, pas sur les performances obtenues.
 
-Les trois indices collectés servent de contrôle et non de terme de comparaison. `^SP500TR` est le seul en rendement total ; `^GSPC` et `^SPXEW` sont des indices de prix, sans dividendes, et ne peuvent donc pas être comparés directement aux portefeuilles.
+Les autres cotations conditionnelles, dites « when-issued », ne sont pas exclues au seul motif qu'elles précèdent la distribution juridique d'une action. Elles peuvent être réelles. Leur négociabilité, leur liquidité et leur coût d'exécution restent une limite du modèle ; le premier cours Yahoo ne prouve pas qu'une opération de n'importe quelle taille était réalisable.
 
-## Les quatre règles de gestion
+Je sépare les rendements observés, dans `rendements_prix.csv`, de ceux utilisés pour valoriser, dans `rendements_valorisation.csv`. Les séquences initiales sans volume sont exclues. À l'intérieur de l'historique, un cours identique à la veille, avec volume nul et quatre prix identiques, est traité comme suspect. Un volume nul avec des prix variables n'est pas automatiquement effacé. Pendant un trou, je porte le dernier cours connu puis je prends le mouvement cumulé à la reprise. Les 18 observations portées sont signalées dans `qualite_valorisation.csv` : ce ne sont pas des observations de rendement nul utilisables sans réserve pour estimer le risque. Aucun prix n'est porté avant la première observation admissible.
 
-**Rééquilibrage.** Chaque portefeuille existe en deux versions, l'une remise aux poids cibles à la première séance de janvier, l'autre jamais rééquilibrée. L'écart entre les deux mesure ce que la concentration apporte et ce qu'elle coûte, puisqu'elle se forme d'elle-même dès qu'on ne fait rien.
+## II. Les règles de gestion et de comparaison
 
-**Dividendes.** Ils alimentent une trésorerie attachée au titre qui les verse, ne rapportent rien, et sont réinvestis à la date annuelle : selon les poids cibles dans la version rééquilibrée, dans le titre payeur dans la version conservée. La trésorerie représente 0,98 % du portefeuille en moyenne et 5,64 % au maximum.
+**Rééquilibrage.** La version annuelle est remise aux poids égaux par entreprise à la première séance de janvier. La version conservée réinvestit seulement les dividendes dans le titre payeur à cette date. Les entrées ont lieu en cours d'année dans les deux versions. Si un titre déjà admis n'a pas de cours utilisable le jour d'une opération, je reporte toute l'opération à la première séance où tous les titres admis sont négociables. Trois reports concernent `P1`, `P2` et `P5`, du 2 au 5 janvier 2015, à cause de la cotation absente d'AMD. Je ne liquide plus implicitement AMD pour toute l'année.
 
-**Coûts.** Dix points de base sur le montant échangé, à chaque rééquilibrage et à chaque entrée de titre. Mesurés : deux à trois centièmes de point par an pour une rotation annuelle de 23 %. Négligeables, donc l'arbitrage entre les deux versions se joue sur le risque et non sur les frais.
+**Entrées.** Une nouvelle entreprise reçoit, après financement, un poids égal à un divisé par le nombre d'entreprises alors détenues, nouvelle comprise. Si plusieurs entrent ensemble, chacune reçoit ce poids. Le financement réduit proportionnellement les positions existantes et leur trésorerie ; hors frais, il ne crée aucune valeur. Les anciens poids conservent leur dérive. Une entrée hors janvier n'est donc pas un rééquilibrage général. Les cibles enregistrées hors janvier sont une référence d'égalité pour l'admission, pas la photographie des poids effectivement détenus.
 
-**Entrées.** Un titre entre à sa première séance réelle, sans délai d'observation. Dans la version conservée, il reçoit le poids moyen des titres déjà détenus, **financé par une réduction proportionnelle de ceux-ci**, de sorte que la valeur du portefeuille ne bouge pas. Cette dernière condition n'était pas respectée par la première version du moteur ; le défaut a été trouvé par un test et corrigé.
+**Dividendes.** J'utilise `Close` et `Dividends`, pas `Adj Close`, pour les portefeuilles. Sur une position déjà détenue, le rendement de richesse avant frais est la variation du cours plus le dividende, rapportés au cours précédent. Le montant du dividende est comptabilisé au détachement dans une poche attachée au titre et non rémunérée. Il est réinvesti à la date annuelle : suivant les poids cibles dans la version rééquilibrée, dans le titre payeur dans la version conservée.
 
-## Avertissement sur le nombre de titres
+Cette poche assimile une créance de dividende à des espèces disponibles. Les dates de paiement des actions n'ont pas été collectées. La différence est réelle : les dividendes de décembre de SPY sont payés fin janvier, après notre date de réinvestissement. Je conserve une convention synthétique commune aux portefeuilles et aux fonds de comparaison, mais je ne la présente pas comme un compte espèces strictement réalisable. Un contrôle séparé sur SPY mesure cette approximation dans le rapport d'audit. Il reste à traiter la disponibilité effective des paiements avant de revendiquer une exécution réelle.
 
-Sept portefeuilles comptent moins de vingt-cinq titres et `P4` n'en compte que six. Ils seront **mécaniquement plus volatils** que `P1`, indépendamment de tout effet lié à l'IA.
+**Coûts.** Le coût vaut dix points de base sur la somme des achats et des ventes effectivement exécutés, y compris les ventes qui financent une entrée et les achats de réinvestissement des dividendes. Les frais sont financés par le portefeuille ; les cibles sont réduites pour que les achats, ventes, espèces et frais se raccordent exactement. La rotation publiée est la somme de ces montants échangés rapportés à la valeur avant chaque opération, divisée par la durée en années de 252 séances. Elle compte les deux côtés des transactions. Ce taux constant est une hypothèse, pas une mesure de spread ou une garantie de prudence pour toute la période. Les sensibilités à cinq et vingt-cinq points de base figurent dans l'audit.
 
-La volatilité d'un portefeuille équipondéré de n titres de volatilité σ et de corrélation moyenne ρ vaut σ multiplié par la racine de ρ plus (1 − ρ)/n. Quand n passe de 113 à 6, le second terme explose. Cet effet devra être isolé à chaque comparaison, faute de quoi on attribuera à la concentration thématique ce qui vient du simple petit nombre.
+**Comparaisons.** `SPY` et `RSP` distribuent des dividendes ; leur réinvestissement n'est pas interne au fonds pour le porteur. Je les reconstruis donc avec la même convention de créance, de réinvestissement annuel et de frais que les portefeuilles. Les séries Yahoo ajustées restent séparées dans `valeurs_comparaisons_yahoo.csv`, pour contrôler l'écart de convention. Toute comparaison exigeant `RSP` commence le 1er mai 2003 et utilise une fenêtre commune, sans prolongement antérieur.
 
-## Le thème et ses deux moitiés
+Les trois indices collectés servent au contexte et au contrôle. `^SP500TR` est en rendement total ; `^GSPC` et `^SPXEW` sont des indices de prix, sans dividendes. Le dernier comporte des séances absentes. Ils ne doivent pas entrer sans adaptation dans une comparaison de performance totale. Les frais internes et les règles de suivi de SPY et RSP restent différents : leur écart n'identifie pas à lui seul l'effet causal de la concentration.
 
-`P2` et `P3` se recomposent exactement en `P1`.
+**Divisions et scissions.** Les cours Yahoo sont déjà retraités des divisions. Je ne multiplie jamais une seconde fois les positions par `Stock Splits`. Cette colonne contient aussi des facteurs de scission. Le moteur suit des montants sur des cours retraités et ne reconstitue pas un registre juridique de parts, de titres distribués, d'échanges et de ventes de droits. C'est une limite de l'interprétation de la version « conservée », à rapprocher des opérations sur titres avant une affirmation d'investissabilité.
+
+## III. Ce que les comparaisons permettent de dire
+
+Les dix portefeuilles sont sélectionnés aujourd'hui avec des informations récentes puis projetés sur le passé. Leur performance absolue, leur classement relatif et leurs mesures de risque peuvent tous être affectés par la connaissance a posteriori et par la sélection des survivants. L'écart avec SPY ne mesure pas la taille de ce biais. Je décris la trajectoire historique de paniers actuels, sans conclure qu'ils étaient identifiables ou investissables à l'époque.
+
+La différence entre rééquilibrer et conserver combine la dérive des poids, les ventes des gagnants, les achats des perdants, les entrées et les coûts. Elle sert à étudier ces mécanismes ; elle n'isole pas un effet causal pur de la concentration. Cette séparation, les facteurs de marché et les épisodes de crise relèvent de l'étape 3. La comparaison trimestrielle reste à faire.
+
+Sept portefeuilles comptent moins de vingt-cinq entreprises et `P4` en compte six. À volatilités individuelles égales et corrélation moyenne donnée, la volatilité d'un portefeuille équipondéré vaut σ multiplié par la racine de ρ + (1 − ρ)/n. Réduire n augmente alors la part non diversifiée. Nos groupes n'ont ni les mêmes volatilités ni les mêmes corrélations : leur petit effectif ne prouve donc pas qu'ils seront plus volatils que `P1`. L'effet de taille devra être distingué des secteurs et des dépendances observées.
+
+## IV. Le thème et ses deux composantes
+
+Les entreprises de `P2` et `P3` forment une partition de celles de `P1`. Cette identité d'appartenance n'implique pas qu'un mélange fixe de leurs séries reproduise `P1` en présence d'entrées, de rééquilibrages et de frais.
 
 ### P1. Le thème entier
@@ -49,5 +61,5 @@
 ### P2. Exposition établie
 
-**Règle.** Les entreprises dont le rapport annuel documente une activité IA déjà réelle.
+**Règle.** Les entreprises classées `etablie` dans le registre de sélection : une activité liée à la chaîne de calcul est documentée. Cela ne mesure ni une part de revenus IA ni une intensité homogène d'exposition.
 
 **Question.** Restreindre aux expositions avérées change-t-il le risque, ou le thème emporte-t-il tout.
@@ -55,11 +67,11 @@
 **95 entreprises**, dont 64 disponibles dès le 3 janvier 2000.
 
-3M (MMM), AES Corporation (AES), Advanced Micro Devices (AMD), Akamai Technologies (AKAM), Alliant Energy (LNT), Alphabet Inc. (Class A) (GOOG), Amazon (AMZN), American Tower (AMT), Ametek (AME), Amphenol (APH), Analog Devices (ADI), Applied Materials (AMAT), Ares Management (ARES), Arista Networks (ANET), Baker Hughes (BKR), Berkshire Hathaway (BRK-B), Broadcom (AVGO), CBRE Group (CBRE), CDW Corporation (CDW), CRH plc (CRH), Cadence Design Systems (CDNS), Carrier Global (CARR), Caterpillar Inc. (CAT), Ciena (CIEN), Cisco (CSCO), Coherent Corp. (COHR), Comfort Systems USA (FIX), Constellation Energy (CEG), Corning Inc. (GLW), Cummins (CMI), Dell Technologies (DELL), Digital Realty (DLR), Dominion Energy (D), Dover Corporation (DOV), Dow Inc. (DOW), Duke Energy (DUK), Eaton Corporation (ETN), Ecolab (ECL), Emcor (EME), Equinix (EQIX), Fastenal (FAST), FirstEnergy (FE), Flex Ltd. (FLEX), GE Vernova (GEV), Generac (GNRC), General Dynamics (GD), Hewlett Packard Enterprise (HPE), Howmet Aerospace (HWM), Hubbell Incorporated (HUBB), IBM (IBM), IDEX Corporation (IEX), Intel (INTC), Iron Mountain (IRM), Jabil (JBL), Johnson Controls (JCI), KLA Corporation (KLAC), Keysight Technologies (KEYS), Lam Research (LRCX), Lennox International (LII), Lumentum (LITE), Martin Marietta Materials (MLM), Marvell Technology (MRVL), Meta Platforms (META), Microchip Technology (MCHP), Micron Technology (MU), Microsoft (MSFT), Monolithic Power Systems (MPWR), NRG Energy (NRG), NetApp (NTAP), Nucor (NUE), Nvidia (NVDA), ON Semiconductor (ON), Oracle Corporation (ORCL), Pinnacle West Capital (PNW), Prologis (PLD), Qnity Electronics (Q), Quanta Services (PWR), Sandisk (SNDK), Schlumberger (SLB), Seagate Technology (STX), Skyworks Solutions (SWKS), Steel Dynamics (STLD), Supermicro (SMCI), Synopsys (SNPS), TE Connectivity (TEL), Teledyne Technologies (TDY), Teradyne (TER), Tesla, Inc. (TSLA), Texas Instruments (TXN), Trane Technologies (TT), Vertiv (VRT), Vulcan Materials Company (VMC), Western Digital (WDC), Xcel Energy (XEL), Xylem Inc. (XYL)
+3M (MMM), AES Corporation (AES), Advanced Micro Devices (AMD), Akamai Technologies (AKAM), Alliant Energy (LNT), Alphabet (GOOGL classe A, GOOG classe C), Amazon (AMZN), American Tower (AMT), Ametek (AME), Amphenol (APH), Analog Devices (ADI), Applied Materials (AMAT), Ares Management (ARES), Arista Networks (ANET), Baker Hughes (BKR), Berkshire Hathaway (BRK-B), Broadcom (AVGO), CBRE Group (CBRE), CDW Corporation (CDW), CRH plc (CRH), Cadence Design Systems (CDNS), Carrier Global (CARR), Caterpillar Inc. (CAT), Ciena (CIEN), Cisco (CSCO), Coherent Corp. (COHR), Comfort Systems USA (FIX), Constellation Energy (CEG), Corning Inc. (GLW), Cummins (CMI), Dell Technologies (DELL), Digital Realty (DLR), Dominion Energy (D), Dover Corporation (DOV), Dow Inc. (DOW), Duke Energy (DUK), Eaton Corporation (ETN), Ecolab (ECL), Emcor (EME), Equinix (EQIX), Fastenal (FAST), FirstEnergy (FE), Flex Ltd. (FLEX), GE Vernova (GEV), Generac (GNRC), General Dynamics (GD), Hewlett Packard Enterprise (HPE), Howmet Aerospace (HWM), Hubbell Incorporated (HUBB), IBM (IBM), IDEX Corporation (IEX), Intel (INTC), Iron Mountain (IRM), Jabil (JBL), Johnson Controls (JCI), KLA Corporation (KLAC), Keysight Technologies (KEYS), Lam Research (LRCX), Lennox International (LII), Lumentum (LITE), Martin Marietta Materials (MLM), Marvell Technology (MRVL), Meta Platforms (META), Microchip Technology (MCHP), Micron Technology (MU), Microsoft (MSFT), Monolithic Power Systems (MPWR), NRG Energy (NRG), NetApp (NTAP), Nucor (NUE), Nvidia (NVDA), ON Semiconductor (ON), Oracle Corporation (ORCL), Pinnacle West Capital (PNW), Prologis (PLD), Qnity Electronics (Q), Quanta Services (PWR), Sandisk (SNDK), Schlumberger (SLB), Seagate Technology (STX), Skyworks Solutions (SWKS), Steel Dynamics (STLD), Supermicro (SMCI), Synopsys (SNPS), TE Connectivity (TEL), Teledyne Technologies (TDY), Teradyne (TER), Tesla, Inc. (TSLA), Texas Instruments (TXN), Trane Technologies (TT), Vertiv (VRT), Vulcan Materials Company (VMC), Western Digital (WDC), Xcel Energy (XEL), Xylem Inc. (XYL)
 
 ### P3. Engagement documenté
 
-**Règle.** Les entreprises ayant annoncé un engagement sans l'avoir encore réalisé.
+**Règle.** Les entreprises classées `engagement_ou_developpement_documente`. La preuve porte sur un engagement ou un développement ; elle ne permet pas de réduire toutes ces entreprises à une promesse entièrement irréalisée.
 
-**Question.** Le marché traite-t-il une promesse comme une réalité.
+**Question.** La maturité de l'exposition documentée est-elle associée à un comportement boursier différent.
 
 **18 entreprises**, dont 17 disponibles dès le 3 janvier 2000.
@@ -67,7 +79,7 @@
 Ameren (AEE), American Electric Power (AEP), CMS Energy (CMS), CenterPoint Energy (CNP), Chevron Corporation (CVX), DTE Energy (DTE), Entergy (ETR), Evergy (EVRG), Halliburton (HAL), NiSource (NI), PPL Corporation (PPL), Realty Income (O), Sempra (SRE), Southern Company (SO), Texas Pacific Land Corporation (TPL), Vistra Corp. (VST), WEC Energy Group (WEC), Williams Companies (WMB)
 
-## La chaîne, sept maillons
+## V. La chaîne, sept maillons
 
-Les sept maillons somment exactement à 113. Le découpage suit le champ `canal` de la sélection de l'étape 1, et non la classification sectorielle GICS : celle-ci range Alphabet et Meta dans les services de communication et Amazon dans la consommation discrétionnaire, ce qui disperserait les acteurs les plus centraux dans un groupe résiduel.
+Les sept groupes somment exactement à 113. Je donne priorité au champ `canal` : dépenses vers `P4`, ventes vers `P5`. Pour le canal `fournit`, je subdivise ensuite selon le secteur GICS, vers `P6` à `P10`. Ce découpage hybride garde les grands acheteurs ensemble, mais ses groupes restent hétérogènes ; leurs noms ne constituent pas une classification économique indépendante.
 
 ### P4. Les acheteurs
@@ -79,5 +91,5 @@
 **6 entreprises**, dont 3 disponibles dès le 3 janvier 2000.
 
-Alphabet Inc. (Class A) (GOOG), Amazon (AMZN), Meta Platforms (META), Microsoft (MSFT), Oracle Corporation (ORCL), Tesla, Inc. (TSLA)
+Alphabet (GOOGL classe A, GOOG classe C), Amazon (AMZN), Meta Platforms (META), Microsoft (MSFT), Oracle Corporation (ORCL), Tesla, Inc. (TSLA)
 
 ### P5. Les vendeurs
@@ -93,5 +105,5 @@
 ### P6. L'électricité
 
-**Règle.** Canal fournit, secteur Utilities : les producteurs qui alimentent les centres de données.
+**Règle.** Canal fournit, secteur Utilities : les services aux collectivités dont l'activité ou l'engagement envers la chaîne de calcul est documenté.
 
 **Question.** L'exposition IA d'un service public se comporte-t-elle comme celle d'un fabricant de puces.
@@ -113,5 +125,5 @@
 ### P8. L'immobilier
 
-**Règle.** Canal fournit, secteur Real Estate : les foncières de centres de données.
+**Règle.** Canal fournit, secteur Real Estate : immobilier et services immobiliers, dont les centres de données. Toutes les entreprises de ce groupe ne sont pas des foncières spécialisées dans ces centres.
 
 **Question.** Un actif immobilier adossé à l'IA reste-t-il un actif immobilier.
@@ -121,7 +133,7 @@
 American Tower (AMT), CBRE Group (CBRE), Digital Realty (DLR), Equinix (EQIX), Iron Mountain (IRM), Prologis (PLD), Realty Income (O)
 
-### P9. L'amont des puces
+### P9. Les fournisseurs technologiques
 
-**Règle.** Canal fournit, secteur Information Technology : les outils qui fabriquent les puces.
+**Règle.** Canal fournit, secteur Information Technology : équipements, conception, test, assemblage et distribution. CDW, Flex et Jabil montrent que ce groupe déborde les seuls outils de fabrication des puces.
 
 **Question.** L'amont amplifie-t-il ou amortit-il les mouvements de l'aval.
@@ -141,7 +153,7 @@
 Ares Management (ARES), Baker Hughes (BKR), Berkshire Hathaway (BRK-B), CRH plc (CRH), Chevron Corporation (CVX), Halliburton (HAL), Martin Marietta Materials (MLM), Nucor (NUE), Schlumberger (SLB), Steel Dynamics (STLD), Texas Pacific Land Corporation (TPL), Vulcan Materials Company (VMC), Williams Companies (WMB)
 
-## P11. Portefeuille d'avenir
+## VI. P11. Portefeuille d'avenir
 
 Réservé. Il sera constitué à la fin du projet, une fois les mesures de risque, de couverture et de coût établies. Rien n'y est inscrit aujourd'hui, et rien ne doit y être inscrit avant que les résultats soient connus.
 
-Sa vocation est d'être le seul portefeuille du document construit **en connaissance des résultats**, et il sera présenté comme tel, distinct des dix autres qui sont définis à l'aveugle.
+Sa construction utilisera explicitement les résultats déjà obtenus. Je le présenterai comme une exploration après observation, à valider sur de nouvelles données. Les dix autres portefeuilles ont des règles antérieures à leur construction, ce qui ne suffit pas à certifier un choix à l'aveugle.
```

</details>

### `research/univers_selection.md`

Mettre à jour CMS et les effectifs associés, conserver l’historique à 112 et expliquer que P1 utilise désormais le vivier complet.

Avant : `ad4bcac2b195659d8d4f2349c8aa545d16392b6b4f2a6533e825749259daed9c`. Après : `5dfad8f2a9af193e5bed41089bba67e474d6e623f1300726591bb844663de6e0`.

Lignes physiques : 174 avant, 174 après.

Les repères `@@` indiquent les lignes avant et après. `-` contient le texte retiré, `+` le texte retenu.

<details>
<summary>Contenu exact des changements</summary>

```diff
--- research/univers_selection.md avant
+++ research/univers_selection.md après
@@ -2,5 +2,5 @@
 
 *AI Concentration Risk Research. 5 septembre 2026.*
-*Application de la règle version III, après les corrections documentaires et comptables.*
+*Règle version III. Effectifs actualisés le 8 septembre 2026, historique des décisions conservé.*
 
 ## I. Ce que j'ai fait
@@ -17,11 +17,11 @@
 |---|---:|
 | A_EXAMINER | 76 |
-| DOUTEUX | 39 |
-| ENTRE | 112 |
+| DOUTEUX | 38 |
+| ENTRE | 113 |
 | SORT | 273 |
 
-**Les 112 entreprises retenues ont toutes une preuve retrouvée dans le corpus.** Il s'agit de l'univers utilisable à ce stade, pas d'une liste définitive pour toute la suite du projet.
+**Les 113 entreprises retenues ont toutes une preuve retrouvée dans le corpus.** Il s'agit de l'univers utilisable à ce stade, pas d'une liste définitive pour toute la suite du projet.
 
-Les 273 exclusions sont provisoires et motivées par les passages examinés. Les 39 cas douteux signalent une frontière ou une preuve insuffisante. Les 76 dossiers à examiner ne sont pas assimilés à des exclusions ; ils peuvent demander une lecture plus large, une preuve différente ou un rapport disponible.
+Les 273 exclusions sont provisoires et motivées par les passages examinés. Les 38 cas douteux signalent une frontière ou une preuve insuffisante. Les 76 dossiers à examiner ne sont pas assimilés à des exclusions ; ils peuvent demander une lecture plus large, une preuve différente ou un rapport disponible.
 
 Une citation retrouvée prouve sa traçabilité. Elle ne remplace pas la discussion du jugement économique que j'en tire.
@@ -29,13 +29,13 @@
 ### Cet univers est un vivier, pas un portefeuille
 
-Ces 112 entreprises ne forment pas un portefeuille et ne sont pas destinées à être détenues ensemble. Elles constituent l'ensemble des candidats dans lequel plusieurs portefeuilles différents seront construits.
+Ces 113 entreprises constituent un vivier de recherche. L'étape 2 en construit plusieurs groupes et inclut un panier complet `P1` comme thermomètre du thème ; cela n'en fait pas une recommandation de détenir l'ensemble.
 
 La distinction est nécessaire pour la suite, parce que le sujet du projet est la concentration. Et il faut ici séparer deux notions que j'avais confondues dans une version précédente de ce document.
 
-**La concentration des poids** décrit la répartition du capital entre les lignes. Elle se calcule directement à partir des pondérations, sans aucune donnée de marché. Un portefeuille bâti sur une poignée de très grandes capitalisations affiche une concentration des poids élevée ; un portefeuille équipondéré sur les 112 affiche une concentration des poids faible.
+**La concentration des poids** décrit la répartition du capital entre les lignes. Elle se calcule directement à partir des pondérations, sans aucune donnée de marché. Un portefeuille bâti sur une poignée de très grandes capitalisations affiche une concentration des poids élevée ; un portefeuille équipondéré sur les 113 affiche une concentration des poids faible.
 
 **La concentration du risque** décrit la part de la variabilité du portefeuille attribuable à un petit nombre de sources. Elle dépend des volatilités et surtout des dépendances entre titres. Elle ne se déduit pas des poids.
 
-Les deux ne coïncident pas. Un portefeuille de 112 lignes équipondérées dont les titres évoluent ensemble se comporte comme un portefeuille beaucoup plus étroit. Avec une volatilité individuelle de 30 % et une corrélation uniforme, la volatilité du portefeuille vaut 2,8 % si la corrélation est nulle, et 28,5 % si elle vaut 0,9. Les poids et leur indice de concentration sont identiques dans les deux cas. Ces valeurs illustrent le mécanisme, elles ne décrivent pas les entreprises retenues.
+Les deux ne coïncident pas. Un portefeuille de 113 lignes équipondérées dont les titres évoluent ensemble se comporte comme un portefeuille beaucoup plus étroit. Avec une volatilité individuelle de 30 % et une corrélation uniforme, la volatilité du portefeuille vaut 2,8 % si la corrélation est nulle, et 28,5 % si elle vaut 0,9. Les poids et leur indice de concentration sont identiques dans les deux cas. Ces valeurs illustrent le mécanisme, elles ne décrivent pas les entreprises retenues.
 
 **Je ne peux donc pas écrire qu'un portefeuille équipondéré serait diversifié.** Ce serait affirmer par avance ce que l'analyse de risque doit établir. Ce que je peux dire à ce stade : les portefeuilles issus de ce vivier différeront par leur concentration des poids, et la comparaison de leurs risques réels est l'objet de l'étape suivante.
@@ -45,5 +45,5 @@
 ## III. Pourquoi l'univers a changé
 
-L'ancienne sélection retenait 82 entreprises. La nouvelle en ajoute 36 et place 6 anciennes entrées en doute, soit 112 retenues. Je ne cherche pas à conserver l'ancien effectif : ce nombre doit être le résultat de la règle.
+L'ancienne sélection retenait 82 entreprises. La nouvelle en ajoute 36 et place 6 anciennes entrées en doute, soit 112 retenues à cette date. La révision ultérieure du dossier CMS Energy ajoute une entreprise, portant le total courant à 113. Je ne cherche pas à conserver l'ancien effectif : ce nombre doit être le résultat de la règle.
 
 Les nouveaux cas comprennent Applied Materials, Amphenol, Trane, Carrier, Monolithic Power Systems, CDW et plusieurs fournisseurs industriels. Ils montrent pourquoi un rang faible ou un secteur autre que la technologie ne justifiait pas une exclusion automatique.
@@ -51,5 +51,5 @@
 Berkshire Hathaway et Ares Management entrent sur des activités opérationnelles de filiales ou de plateformes décrites dans leurs dossiers. Leur présence ne signifie pas qu'une simple participation financière suffirait à qualifier tout gestionnaire d'actifs.
 
-NextEra Energy, Public Service Enterprise Group, CMS Energy, PG&E, Oneok et Consolidated Edison passent en `DOUTEUX`. Les preuves examinées ne satisfont pas assez précisément la distinction entre activité ou engagement concret et perspective générale. Ce changement ne vient pas de leurs multiples comptables.
+Le 5 septembre, NextEra Energy, Public Service Enterprise Group, CMS Energy, PG&E, Oneok et Consolidated Edison sont passées en `DOUTEUX`. CMS a depuis été retenue après réexamen documenté dans le registre courant. Les preuves alors examinées ne satisfaisaient pas assez précisément la distinction entre activité ou engagement concret et perspective générale. Ce changement ne vient pas de leurs multiples comptables.
 
 First Solar reste douteuse lorsque le passage ne décrit que des acheteurs potentiels. Adobe, ServiceNow et AppLovin restent des cas de frontière entre investissement applicatif et capacité d'infrastructure identifiable. Je ne les exclus pas simplement parce que leur métier est le logiciel.
@@ -63,10 +63,10 @@
 | depense | 2 |
 | depense et vend | 4 |
-| fournit | 74 |
+| fournit | 75 |
 | vend | 32 |
 
-L'activité est établie dans 95 dossiers ; 17 reposent sur un engagement ou un développement documenté.
+L'activité est établie dans 95 dossiers ; 18 reposent sur un engagement ou un développement documenté.
 
-La part précisément attribuable à l'IA n'est pas isolée de manière suffisamment homogène. Le degré est donc `non_quantifie` pour les 112 entreprises. Cela ne veut pas dire qu'elles ont toutes la même exposition. Cela empêche de transformer un adjectif non étayé en mesure de risque ou en poids de portefeuille.
+La part précisément attribuable à l'IA n'est pas isolée de manière suffisamment homogène. Le degré est donc `non_quantifie` pour les 113 entreprises. Cela ne veut pas dire qu'elles ont toutes la même exposition. Cela empêche de transformer un adjectif non étayé en mesure de risque ou en poids de portefeuille.
 
 Les centres de données servent aussi des usages autres que l'IA. Cette limite reste attachée à la preuve et à l'interprétation.
@@ -84,9 +84,9 @@
 | Materials | 7 |
 | Real Estate | 7 |
-| Utilities | 21 |
+| Utilities | 22 |
 
-L'univers couvre 9 secteurs du fichier. 69 entreprises retenues se trouvent hors de l'Information Technology.
+L'univers couvre 9 secteurs du fichier. 70 entreprises retenues se trouvent hors de l'Information Technology.
 
-Cela décrit la différence entre une classification sectorielle et le mécanisme que je cherche. Cela ne démontre pas que ces secteurs se comporteront de la même façon en bourse, ni que les 112 entreprises offrent 112 risques indépendants.
+Cela décrit la différence entre une classification sectorielle et le mécanisme que je cherche. Cela ne démontre pas que ces secteurs se comporteront de la même façon en bourse, ni que les 113 entreprises offrent 113 risques indépendants.
 
 La composition reste celle du fichier local, source secondaire à rapprocher d'une composition officielle datée. Le périmètre S&P 500 n'est pas synonyme de toutes les entreprises cotées aux États-Unis.
@@ -96,5 +96,5 @@
 La base contient 16 722 lignes brutes et 5 707 périodes traitées pour 496 entreprises. Une clôture identifie l'exercice ; deux périodes ne sont pas fusionnées parce qu'elles partagent l'année civile majoritaire.
 
-La description des 112 entreprises retenues donne :
+La description des 113 entreprises retenues donne :
 
 | Mouvement des mesures disponibles | Nombre |
@@ -102,5 +102,5 @@
 | doublement observe | 50 |
 | non evaluable | 6 |
-| progression inferieure au seuil | 55 |
+| progression inferieure au seuil | 56 |
 | recul des mesures disponibles | 1 |
 
@@ -110,5 +110,5 @@
 |---|---:|
 | aucune comparaison | 6 |
-| observation partielle | 48 |
+| observation partielle | 49 |
 | trois mesures comparables | 58 |
 
@@ -145,5 +145,5 @@
 Je ne peux donc plus présenter tous les services aux collectivités comme uniquement exposés à une croissance future. Je ne peux pas non plus déduire la nature de cette exposition d'une hausse du chiffre d'affaires total.
 
-Les 21 entreprises retenues dans ce secteur ne définissent pas un poids de portefeuille. La comparaison des situations économiques, de la régulation et des dépendances boursières viendra avant toute pondération.
+Les 22 entreprises retenues dans ce secteur ne définissent pas un poids de portefeuille. La comparaison des situations économiques, de la régulation et des dépendances boursières viendra avant toute pondération.
 
 ## IX. Ce qui reste à vérifier
@@ -155,5 +155,5 @@
 L'exposition économique n'est pas encore une exposition boursière mesurée. Les derniers rapports, la composition locale actuelle et les comptes retraités ne forment pas un historique de stratégie sans anticipation.
 
-La prochaine étape est de relire les décisions et les comparaisons, puis de définir les portefeuilles, les périodes, les benchmarks et les hypothèses à tester.
+La construction des portefeuilles est maintenant engagée. Ses règles sont dans `research/portefeuilles.md`, son avancement dans `research/plan_projet.md`, et les réserves du contrôle dans `research/audit_etape_2.md`.
 
 ## X. Où retrouver les résultats
@@ -164,5 +164,5 @@
 | `data/processed/classement_texte.csv` | Ordre de lecture reproductible |
 | `data/processed/classification_manuelle.csv` | Verdicts appliqués et preuves vérifiées |
-| `data/processed/univers_retenu.csv` | Les 112 entreprises actuellement retenues |
+| `data/processed/univers_retenu.csv` | Les 113 entreprises actuellement retenues |
 | `data/processed/base_selection.csv` | Les 5 707 périodes et statuts par mesure |
 | `data/processed/corroboration_details.csv` | Références exactes et sources des multiples |
```

</details>

### `src/collecter_prix.ipynb`

Bloquer le rejeu ordinaire d’une collecte sur un cliché existant et retirer la suppression finale des CSV bruts. Les sorties stockées ont été effacées pour ne pas suggérer une nouvelle collecte.

Avant : `0ff4d06f1638cc6c2f36d073404d2fad8fc171bc205ad58c07f80b7d60e7165f`. Après : `124bda73d9df4f3ec626ee99af2e7bf2d5f109c69234ce7098e090e8d2e0af37`.

Lignes physiques : 696 avant, 470 après.

Cellules : 25 avant, 26 après ; cellules avec sorties enregistrées : 10 avant, 0 après. Les identifiants de cellules sont uniques ; les carnets de reconstruction n’annoncent plus un ancien Python dans leurs métadonnées.

<details>
<summary>Sources des cellules avant et après</summary>

```diff
--- src/collecter_prix.ipynb avant
+++ src/collecter_prix.ipynb après
@@ -1,7 +1,12 @@
-CELLULE 0, code
+CELLULE 0, markdown
+# Démarche de collecte initiale
+
+Ce carnet conserve le raisonnement de collecte. Il s'arrête si un manifeste existe déjà, afin de protéger le cliché daté. Le rejeu des calculs se fait dans `construire_portefeuille.ipynb`, sans réseau. Une collecte nouvelle exige un dossier distinct et une publication complète, contrôlée avant remplacement d'une version.
+
+CELLULE 1, code
 from pathlib import Path
 import yfinance as yf
 
-CELLULE 1, code
+CELLULE 2, code
 RACINE = next (d for d in [Path.cwd(), *Path.cwd().parents] if (d / ".git").exists())
 DOSSIER = RACINE /"data"/ "raw" / "prix"
@@ -9,35 +14,37 @@
 
 COLONNES = ["Open" , "High", "Low", "Close", "Adj Close", "Volume", "Dividends", "Stock Splits"]
-
-CELLULE 2, code
+if (RACINE / "data/raw/prix_manifest.json").exists():
+    raise FileExistsError("Le cliché de collecte existe. Pour recalculer, utiliser le carnet de construction ; une nouvelle collecte doit avoir un dossier daté distinct.")
+
+CELLULE 3, code
 histo = yf.Ticker(SYMBOLE).history(period = "max" , auto_adjust =False)
 histo = histo[COLONNES]
 
-CELLULE 3, code
+CELLULE 4, code
 histo.index.name = "date"
 histo["symbole"]= SYMBOLE
 
-CELLULE 4, code
+CELLULE 5, code
 DOSSIER.mkdir(parents = True, exist_ok = True)
 chemin = DOSSIER / f"{SYMBOLE}.csv"
 
-CELLULE 5, code
+CELLULE 6, code
 histo.to_csv(chemin, encoding = "utf-8")
 print(len(histo), "lignes ecrites dans" , chemin)
 histo.tail(3)
 
-CELLULE 6, markdown
+CELLULE 7, markdown
 ### lanncement et imporatations des base de données yahoo finance
 
-CELLULE 7, code
+CELLULE 8, code
 import time
 import pandas as pd
 
-CELLULE 8, code
+CELLULE 9, code
 univers = pd.read_csv(RACINE / "data" / "processed" / "univers_retenu.csv")
 symboles = sorted({s for ligne in univers["symboles"] for s in ligne.split("|")})
 print(len(symboles), "symboles a collecter")
 
-CELLULE 9, code
+CELLULE 10, code
 echecs = []
 
@@ -66,5 +73,5 @@
     print(" -", symbole, ":", message[:80])
 
-CELLULE 10, code
+CELLULE 11, code
 symbole = "BRK.B"
 requete = symbole.replace(".", "-")
@@ -80,8 +87,8 @@
 print(len(histo), "lignes", chemin.name)
 
-CELLULE 11, markdown
+CELLULE 12, markdown
 ### benchmark
 
-CELLULE 12, code
+CELLULE 13, code
 BENCH = RACINE / "data" / "raw" / "benchmarks"
 BENCH.mkdir(parents=True, exist_ok=True)
@@ -89,5 +96,5 @@
 REFERENCES = ["SPY", "RSP", "^GSPC", "^SP500TR", "^SPXEW"]
 
-CELLULE 13, code
+CELLULE 14, code
 for symbole in REFERENCES:
     fichier = symbole.replace("^", "") + ".csv"
@@ -103,5 +110,5 @@
     time.sleep(0.3)
 
-CELLULE 14, code
+CELLULE 15, code
 CALENDRIER = RACINE / "data" / "raw" / "calendrier_bourse.csv"
 
@@ -117,8 +124,8 @@
 print(manquantes[:10])
 
-CELLULE 15, markdown
+CELLULE 16, markdown
 ### cas simple NVDA
 
-CELLULE 16, code
+CELLULE 17, code
 import requests
 
@@ -140,8 +147,8 @@
     print(v)
 
-CELLULE 17, markdown
+CELLULE 18, markdown
 ### cas général
 
-CELLULE 18, code
+CELLULE 19, code
 import time
 
@@ -185,8 +192,8 @@
     print(" -", nom, ":", message[:70])
 
-CELLULE 19, markdown
+CELLULE 20, markdown
 ### correction
 
-CELLULE 20, code
+CELLULE 21, code
 SUBSTITUTS = [
     ("us-gaap", "CommonStockSharesOutstanding", "shares", "actions_bilan"),
@@ -225,8 +232,8 @@
 print(actions.groupby("notion").cik.nunique().to_string())
 
-CELLULE 21, code
-
-
 CELLULE 22, code
+
+
+CELLULE 23, code
 import hashlib
 import json
@@ -265,17 +272,9 @@
 print(len(manifeste["prix"]), "fichiers de prix |", len(manifeste["benchmarks"]), "benchmarks")
 
-CELLULE 23, code
-
-
 CELLULE 24, code
-for fichier in sorted(DOSSIER.glob("*.csv")):
-    d = pd.read_csv(fichier)
-    d.to_csv(fichier.with_suffix(".csv.gz"), index=False, compression="gzip")
-    fichier.unlink()
-
-for fichier in sorted(BENCH.glob("*.csv")):
-    d = pd.read_csv(fichier)
-    d.to_csv(fichier.with_suffix(".csv.gz"), index=False, compression="gzip")
-    fichier.unlink()
-
-print("compresse")
+
+
+CELLULE 25, markdown
+## Conservation des preuves
+
+La dernière cellule proposait de compresser les CSV puis de supprimer les originaux. Je l'ai retirée le 8 septembre 2026 : elle aurait détruit les chemins et les empreintes attendus par les contrôles. La collecte conservée est un cliché, sa compression éventuelle doit produire une archive séparée.
```

</details>

### `src/construire_portefeuille.ipynb`

Retirer les définitions successives et appeler le même moteur et les mêmes contrôles que la commande locale.

Avant : `4a1d9637dc7324f15fd54d5a4dd4cb013976307562e78320713239195abde3d4`. Après : `848cd476b1e8643e8228d9d7974dafbd5bbaff087007514f8a97244b58b8b24e`.

Lignes physiques : 797 avant, 127 après.

Cellules : 18 avant, 8 après ; cellules avec sorties enregistrées : 10 avant, 0 après. Les identifiants de cellules sont uniques ; les carnets de reconstruction n’annoncent plus un ancien Python dans leurs métadonnées.

<details>
<summary>Sources des cellules avant et après</summary>

```diff
--- src/construire_portefeuille.ipynb avant
+++ src/construire_portefeuille.ipynb après
@@ -1,487 +1,54 @@
-CELLULE 0, code
+CELLULE 0, markdown
+# Construction des portefeuilles
+
+## I. Les règles et le moteur
+
+Je garde ici le déroulé du calcul. Les fonctions sont dans `src/portefeuille.py` et la reconstruction complète dans `src/construire_portefeuilles.py`. Une seule version du moteur produit les valeurs, les poids et les contrôles. Les décisions corrigées le 8 septembre sont datées dans `research/portefeuilles.md`.
+
+CELLULE 1, code
 from pathlib import Path
+import sys
+import importlib
 import pandas as pd
 
-RACINE = next(d for d in [Path.cwd(), *Path.cwd().parents] if (d / ".git").exists())
-DOSSIER = RACINE / "data" / "raw" / "prix"
-BENCH = RACINE / "data" / "raw" / "benchmarks"
+RACINE = next(d for d in [Path.cwd(), *Path.cwd().parents]
+              if (d / "src" / "portefeuille.py").exists())
+if str(RACINE) not in sys.path:
+    sys.path.insert(0, str(RACINE))
 SORTIE = RACINE / "data" / "processed"
 
-DEBUT = "2000-01-03"
+CELLULE 2, markdown
+## II. Recalculer depuis le cliché conservé
 
-CELLULE 1, code
-prix, dividendes = {}, {}
-
-for fichier in sorted(DOSSIER.glob("*.csv")):
-    d = pd.read_csv(fichier, usecols=["date", "Close", "Volume", "Dividends"])
-    d["j"] = d["date"].str[:10]
-    d = d.set_index("j")
-
-    cloture = d.Close.astype("Float64").mask(d.Volume == 0)
-
-    prix[fichier.stem] = cloture.pct_change(fill_method=None).loc[DEBUT:]
-    dividendes[fichier.stem] = (d.Dividends / cloture.shift()).loc[DEBUT:]
-
-rendements = pd.DataFrame(prix)
-detachements = pd.DataFrame(dividendes)
-
-rendements.to_csv(SORTIE / "rendements_prix.csv", encoding="utf-8")
-detachements.to_csv(SORTIE / "dividendes.csv", encoding="utf-8")
-
-print(rendements.shape, "dates x titres")
-print("valeurs renseignees :", int(rendements.notna().sum().sum()),
-      "| manquantes :", int(rendements.isna().sum().sum()))
-print("titres au premier jour :", int(rendements.iloc[0].notna().sum()),
-      "| au dernier :", int(rendements.iloc[-1].notna().sum()))
-print("rendement maximal :", f"{rendements.max().max():+.1%}",
-      "| minimal :", f"{rendements.min().min():+.1%}")
-print("detachements de dividende :", int((detachements > 0).sum().sum()))
-
-CELLULE 2, code
-calendrier = pd.read_csv(RACINE / "data" / "raw" / "calendrier_bourse.csv")["date"].astype(str)
-seances = set(calendrier[(calendrier >= rendements.index.min())
-                         & (calendrier <= rendements.index.max())])
-lignes = set(rendements.index.astype(str))
-
-if lignes - seances:
-    raise ValueError(f"{len(lignes - seances)} dates hors calendrier de bourse")
-if seances - lignes:
-    raise ValueError(f"{len(seances - lignes)} seances absentes de la matrice")
-
-print(len(lignes), "seances alignees sur le calendrier de bourse")
-print("titres renseignes par seance : min", int(rendements.notna().sum(axis=1).min()),
-      "| max", int(rendements.notna().sum(axis=1).max()))
+Je vérifie les empreintes des sources avant de calculer. Le traitement n'interroge aucun fournisseur et ne modifie aucun fichier brut. Il distingue les rendements observés des valeurs portées lors d'un cours manquant, finance les entrées, prélève les frais sur les achats et ventes et contrôle les sorties avant publication.
 
 CELLULE 3, code
-decisions = pd.read_csv(RACINE / "data" / "review" / "decisions_selection.csv", dtype=str)
-retenues = decisions[decisions.verdict == "ENTRE"].copy()
-retenues["titres"] = retenues.symboles.str.replace(".", "-", regex=False).str.split("|")
+import src.controle_prix as controle_module
+import src.portefeuille as moteur
+import src.construire_portefeuilles as construction
+importlib.reload(controle_module)
+importlib.reload(moteur)
+importlib.reload(construction)
+resultat = construction.construire(RACINE, SORTIE)
+print(resultat)
 
-def maillon(r):
-    if r.canal in ("depense", "depense et vend"): return "P4"
-    if r.canal == "vend": return "P5"
-    if r.secteur == "Utilities": return "P6"
-    if r.secteur == "Industrials": return "P7"
-    if r.secteur == "Real Estate": return "P8"
-    if r.secteur == "Information Technology": return "P9"
-    return "P10"
+CELLULE 4, markdown
+## III. Lire les résultats contrôlés
 
-lignes = []
-for r in retenues.itertuples():
-    for p in ["P1", "P2" if r.maturite_exposition == "etablie" else "P3", maillon(r)]:
-        for titre in r.titres:
-            lignes.append({"portefeuille": p, "entreprise": r.nom, "cik": r.cik,
-                           "titre": titre, "classes": len(r.titres)})
-
-appartenance = pd.DataFrame(lignes)
-appartenance.to_csv(SORTIE / "appartenance.csv", index=False, encoding="utf-8")
-
-manquants = set(appartenance.titre) - set(rendements.columns)
-if manquants:
-    raise ValueError(f"titres sans serie de rendement : {sorted(manquants)}")
-
-effectifs = appartenance.groupby("portefeuille").entreprise.nunique()
-if effectifs["P2"] + effectifs["P3"] != effectifs["P1"]:
-    raise ValueError("P2 et P3 ne recomposent pas P1")
-if effectifs[[f"P{i}" for i in range(4, 11)]].sum() != effectifs["P1"]:
-    raise ValueError("les sept maillons ne somment pas a P1")
-
-print(effectifs.to_string())
-print("\ntitres :", appartenance.titre.nunique(), "| entreprises :", appartenance.entreprise.nunique())
-
-CELLULE 4, code
-dates = pd.Series(rendements.index.astype(str))
-reequilibrages = dates.groupby(dates.str[:4]).min().tolist()
-
-present = rendements.notna()
-lignes = []
-
-for p, groupe in appartenance.groupby("portefeuille"):
-    for j in reequilibrages:
-        presents = groupe[[present.at[j, t] for t in groupe.titre]]
-        if presents.empty:
-            continue
-        n = presents.entreprise.nunique()
-        classes = presents.groupby("entreprise").titre.transform("size")
-        for r, k in zip(presents.itertuples(), classes):
-            lignes.append({"portefeuille": p, "date": j, "titre": r.titre,
-                           "entreprise": r.entreprise, "poids": 1 / (n * k)})
-
-poids_cibles = pd.DataFrame(lignes)
-poids_cibles.to_csv(SORTIE / "poids_cibles.csv", index=False, encoding="utf-8")
-
-sommes = poids_cibles.groupby(["portefeuille", "date"]).poids.sum()
-if not sommes.round(12).eq(1).all():
-    raise ValueError("des poids cibles ne somment pas a 1")
-
-effectifs = (poids_cibles.groupby(["date", "portefeuille"]).entreprise.nunique()
-             .unstack()[[f"P{i}" for i in range(1, 11)]])
-
-print(len(poids_cibles), "lignes de poids |", len(reequilibrages), "dates de reequilibrage")
-print(effectifs.iloc[[0, 5, 10, 15, 20, 26]].to_string())
+Ces chiffres décrivent rétrospectivement l'univers constitué en 2026. Ils ne mesurent ni une performance réalisable à l'époque ni la part de risque causée par l'IA. La trésorerie et les frais expliquent chaque variation de valeur dans le journal quotidien.
 
 CELLULE 5, code
-import numpy as np
+mesures = pd.read_csv(SORTIE / "mesures_portefeuilles.csv")
+print(mesures.to_string(index=False))
+print(pd.read_csv(SORTIE / "operations_reportees.csv").to_string(index=False))
 
-COUT = 0.0010
+CELLULE 6, markdown
+## IV. Les références et les empreintes
 
-dates = rendements.index.astype(str).tolist()
-jours_reeq = set(poids_cibles.date.unique())
-detachements = detachements.reindex(columns=rendements.columns)
-
-
-def simuler(portefeuille, reequilibrer, cout=COUT):
-    membres = appartenance[appartenance.portefeuille == portefeuille]
-    titres = membres.titre.tolist()
-
-    r = rendements[titres].astype("float64").to_numpy()
-    d = detachements[titres].astype("float64").fillna(0).to_numpy()
-    cote = ~np.isnan(r)
-    cible = (poids_cibles[poids_cibles.portefeuille == portefeuille]
-             .pivot(index="date", columns="titre", values="poids")
-             .reindex(columns=titres))
-
-    montant = np.zeros(len(titres))
-    tresorerie = np.zeros(len(titres))
-    valeurs, rotations = [], []
-
-    for i, jour in enumerate(dates):
-        vivant = cote[i]
-
-        if i > 0:
-            tresorerie += montant * np.where(vivant, d[i], 0.0)
-            montant = montant * (1 + np.where(vivant, np.nan_to_num(r[i]), 0.0))
-
-        valeur = montant.sum() + tresorerie.sum()
-
-        if jour in jours_reeq:
-            w = np.nan_to_num(cible.loc[jour].to_numpy(dtype=float))
-
-            if valeur == 0:
-                montant = w.copy()
-                tresorerie[:] = 0.0
-
-            elif reequilibrer:
-                vise = valeur * w
-                echange = np.abs(vise - montant).sum()
-                rotations.append(echange / valeur)
-                frais = cout * echange
-                montant = vise * (1 - frais / valeur)
-                tresorerie[:] = 0.0
-
-            else:
-                montant = montant + tresorerie
-                tresorerie[:] = 0.0
-                entrants = vivant & (montant == 0) & (w > 0)
-                if entrants.any():
-                    presents = int((montant > 0).sum())
-                    part = montant.sum() / (presents + entrants.sum())
-                    montant[entrants] = part
-                    echange = part * entrants.sum()
-                    rotations.append(echange / montant.sum())
-                    frais = cout * echange
-                    montant *= (montant.sum() - frais) / montant.sum()
-
-            valeur = montant.sum() + tresorerie.sum()
-
-        valeurs.append(valeur)
-
-    return pd.Series(valeurs, index=dates), float(np.mean(rotations)) if rotations else 0.0
-
-
-series, resume = {}, []
-annees = len(dates) / 252
-
-for pf in [f"P{i}" for i in range(1, 11)]:
-    for reeq in [True, False]:
-        nom = f"{pf}_{'reeq' if reeq else 'cons'}"
-        v, rotation = simuler(pf, reeq)
-        v = v / v.iloc[0] * 100
-        sans, _ = simuler(pf, reeq, cout=0.0)
-        sans = sans / sans.iloc[0] * 100
-        series[nom] = v
-        resume.append({"serie": nom, "base100": v.iloc[-1],
-                       "annualise": (v.iloc[-1] / 100) ** (1 / annees) - 1,
-                       "rotation": rotation,
-                       "cout_pb": ((sans.iloc[-1] / 100) ** (1 / annees)
-                                   - (v.iloc[-1] / 100) ** (1 / annees)) * 10000})
-
-valeurs = pd.DataFrame(series)
-valeurs.to_csv(SORTIE / "valeurs_portefeuilles.csv", encoding="utf-8")
-
-resume = pd.DataFrame(resume).set_index("serie")
-print(valeurs.shape, "seances x series")
-print(resume.to_string(float_format=lambda x: f"{x:,.4f}"))
-
-CELLULE 6, code
-meta = pd.read_csv(RACINE / "data" / "raw" / "metadonnees_titres.csv")
-nature = dict(zip(meta.fichier, meta.type))
-
-comparaisons = {}
-
-for fichier in sorted(BENCH.glob("*.csv")):
-    d = pd.read_csv(fichier, usecols=["date", "Adj Close", "Volume"])
-    d["j"] = d["date"].str[:10]
-    d = d.set_index("j")
-
-    serie = d["Adj Close"].astype("float64")
-    if nature[fichier.name] != "INDEX":
-        serie = serie.mask(d.Volume == 0)
-
-    serie = serie.loc[DEBUT:].reindex(valeurs.index)
-    comparaisons[fichier.stem] = serie / serie.dropna().iloc[0] * 100
-
-comparaisons = pd.DataFrame(comparaisons)
-comparaisons.to_csv(SORTIE / "valeurs_comparaisons.csv", encoding="utf-8")
-
-annees_dispo = comparaisons.notna().sum() / 252
-print(pd.DataFrame({"debut": comparaisons.apply(lambda s: s.first_valid_index()),
-                    "seances": comparaisons.notna().sum(),
-                    "base100_finale": comparaisons.iloc[-1],
-                    "annualise": (comparaisons.iloc[-1] / 100) ** (1 / annees_dispo) - 1}
-                   ).to_string(float_format=lambda x: f"{x:,.4f}"))
+SPY et RSP sont calculés avec la même convention de créances assimilées à des espèces et de réinvestissement annuel que les portefeuilles. Les séries ajustées de Yahoo sont conservées séparément pour retrouver l'ancien repère. Les indices de prix restent des contrôles descriptifs.
 
 CELLULE 7, code
-mois = pd.Series(dates)
-fins_de_mois = set(mois.groupby(mois.str[:7]).max())
-
-
-def simuler(portefeuille, reequilibrer, cout=COUT):
-    membres = appartenance[appartenance.portefeuille == portefeuille]
-    titres = membres.titre.tolist()
-
-    r = rendements[titres].astype("float64").to_numpy()
-    d = detachements[titres].astype("float64").fillna(0).to_numpy()
-    cote = ~np.isnan(r)
-    cible = (poids_cibles[poids_cibles.portefeuille == portefeuille]
-             .pivot(index="date", columns="titre", values="poids")
-             .reindex(columns=titres))
-
-    montant = np.zeros(len(titres))
-    tresorerie = np.zeros(len(titres))
-    valeurs, rotations, photos = [], [], []
-
-    for i, jour in enumerate(dates):
-        vivant = cote[i]
-
-        if i > 0:
-            tresorerie += montant * np.where(vivant, d[i], 0.0)
-            montant = montant * (1 + np.where(vivant, np.nan_to_num(r[i]), 0.0))
-
-        valeur = montant.sum() + tresorerie.sum()
-
-        if jour in jours_reeq:
-            w = np.nan_to_num(cible.loc[jour].to_numpy(dtype=float))
-
-            if valeur == 0:
-                montant = w.copy()
-                tresorerie[:] = 0.0
-
-            elif reequilibrer:
-                vise = valeur * w
-                echange = np.abs(vise - montant).sum()
-                rotations.append(echange / valeur)
-                frais = cout * echange
-                montant = vise * (1 - frais / valeur)
-                tresorerie[:] = 0.0
-
-            else:
-                montant = montant + tresorerie
-                tresorerie[:] = 0.0
-                entrants = vivant & (montant == 0) & (w > 0)
-                if entrants.any():
-                    presents = int((montant > 0).sum())
-                    part = montant.sum() / (presents + entrants.sum())
-                    montant[entrants] = part
-                    echange = part * entrants.sum()
-                    rotations.append(echange / montant.sum())
-                    frais = cout * echange
-                    montant *= (montant.sum() - frais) / montant.sum()
-
-            valeur = montant.sum() + tresorerie.sum()
-
-        valeurs.append(valeur)
-
-        if jour in fins_de_mois and valeur > 0:
-            photo = pd.Series(montant / valeur, index=titres, name=jour)
-            photo["_tresorerie"] = tresorerie.sum() / valeur
-            photos.append(photo)
-
-    rotation = float(np.mean(rotations)) if rotations else 0.0
-    return pd.Series(valeurs, index=dates), rotation, pd.DataFrame(photos)
-
-
-morceaux = []
-for pf in [f"P{i}" for i in range(1, 11)]:
-    for reeq in [True, False]:
-        nom = f"{pf}_{'reeq' if reeq else 'cons'}"
-        _, _, photos = simuler(pf, reeq)
-        p = photos.stack().rename("poids").reset_index()
-        p.columns = ["date", "titre", "poids"]
-        p.insert(0, "serie", nom)
-        morceaux.append(p[p.poids != 0])
-
-poids_mensuels = pd.concat(morceaux, ignore_index=True)
-poids_mensuels.to_csv(SORTIE / "poids_mensuels.csv", index=False, encoding="utf-8")
-
-print(f"{len(poids_mensuels):,} lignes | {poids_mensuels.date.nunique()} mois | "
-      f"{poids_mensuels.serie.nunique()} series")
-
-CELLULE 8, code
-
-
-CELLULE 9, code
-controles = []
-
-sommes = poids_mensuels.groupby(["serie", "date"]).poids.sum()
-ecart = (sommes - 1).abs().max()
-controles.append({"tache": 43, "test": "somme des poids egale a 1",
-                  "cas": int((sommes - 1).abs().gt(1e-9).sum()),
-                  "detail": f"ecart maximal {ecart:.2e} sur {len(sommes)} couples"})
-
-actions = poids_mensuels[poids_mensuels.titre != "_tresorerie"]
-tresorerie = poids_mensuels[poids_mensuels.titre == "_tresorerie"]
-controles.append({"tache": 44, "test": "poids negatif", "cas": int((actions.poids < 0).sum()),
-                  "detail": ""})
-controles.append({"tache": 44, "test": "poids superieur a 1", "cas": int((actions.poids > 1).sum()),
-                  "detail": ""})
-controles.append({"tache": 44, "test": "tresorerie negative",
-                  "cas": int((tresorerie.poids < 0).sum()),
-                  "detail": f"moyenne {tresorerie.poids.mean():.2%}, maximum {tresorerie.poids.max():.2%}"})
-
-premiere = {c: rendements[c].astype("float64").first_valid_index() for c in rendements.columns}
-avant = actions[actions.date < actions.titre.map(premiere)]
-controles.append({"tache": 45, "test": "poids avant la premiere cotation",
-                  "cas": len(avant), "detail": ""})
-
-membres = appartenance.groupby("portefeuille").titre.apply(set).to_dict()
-hors = actions[[t not in membres[s.split("_")[0]]
-                for t, s in zip(actions.titre, actions.serie)]]
-controles.append({"tache": 45, "test": "titre hors appartenance", "cas": len(hors), "detail": ""})
-
-controles = pd.DataFrame(controles)
-print(controles.to_string(index=False))
-
-if controles.cas.sum():
-    raise ValueError(f"{int(controles.cas.sum())} anomalies de construction")
-print("\nles six controles passent")
-
-CELLULE 10, code
-hors_reeq = ~valeurs.index.astype(str).isin(jours_reeq)
-cas_46 = 0
-for s in valeurs.columns:
-    titres = appartenance[appartenance.portefeuille == s.split("_")[0]].titre.tolist()
-    r = valeurs[s].pct_change()
-    sous = rendements[titres].astype("float64")
-    dehors = (r < sous.min(axis=1) - 1e-9) | (r > sous.max(axis=1) + 1e-9)
-    cas_46 += int((dehors & sous.notna().any(axis=1) & hors_reeq).sum())
-
-brut = {pf: simuler(pf, True, cout=0.0)[0] for pf in [f"P{i}" for i in range(1, 11)]}
-effectifs = poids_cibles.groupby(["portefeuille", "date"]).entreprise.nunique().unstack(0)
-jalons = sorted(jours_reeq)
-bornes = list(zip(jalons, jalons[1:] + [dates[-1]]))
-position = {j: i for i, j in enumerate(dates)}
-
-def melanger(parts):
-    serie = pd.Series(index=dates, dtype=float)
-    courant = 1.0
-    for a, b in bornes:
-        n = effectifs.loc[a, parts].astype(float)
-        w = (n / n.sum()).to_dict()
-        segment = dates[position[a]:position[b] + 1]
-        serie.loc[segment] = courant * sum(w[p] * (brut[p].loc[segment] / brut[p].loc[a])
-                                           for p in parts)
-        courant = serie.loc[b]
-    return serie
-
-reference = brut["P1"] / brut["P1"].iloc[0]
-ecart_moities = (melanger(["P2", "P3"]) / reference - 1).abs().max()
-ecart_maillons = (melanger([f"P{i}" for i in range(4, 11)]) / reference - 1).abs().max()
-
-annualise = lambda s: (s.iloc[-1] / s.iloc[0]) ** (252 / len(s)) - 1
-spy = comparaisons[["SPY", "SP500TR"]].dropna()
-rsp = comparaisons[["RSP", "SPXEW"]].dropna()
-gspc = comparaisons[["GSPC", "SP500TR"]].dropna()
-
-print("46. rendements hors de l'encadrement par les titres :", cas_46)
-print(f"47. P2 + P3 reconstituent P1      ecart maximal {ecart_moities:.2e}")
-print(f"    les 7 maillons reconstituent P1 ecart maximal {ecart_maillons:.2e}")
-print(f"48. SPY {annualise(spy.SPY):.2%} contre SP500TR {annualise(spy.SP500TR):.2%}"
-      f"  ->  {(annualise(spy.SP500TR) - annualise(spy.SPY)) * 10000:.1f} pb de frais")
-print(f"    GSPC {annualise(gspc.GSPC):.2%} contre SP500TR {annualise(gspc.SP500TR):.2%}"
-      f"  ->  {(annualise(gspc.SP500TR) - annualise(gspc.GSPC)) * 100:.2f} pt de dividendes")
-print(f"    RSP {annualise(rsp.RSP):.2%} contre SPXEW {annualise(rsp.SPXEW):.2%}"
-      f"  ->  {(annualise(rsp.RSP) - annualise(rsp.SPXEW)) * 100:.2f} pt, SPXEW est un indice de prix")
-
-if cas_46 or ecart_moities > 1e-10 or ecart_maillons > 1e-10:
-    raise ValueError("incoherence de construction")
-print("\nles trois controles passent")
-
-CELLULE 11, code
-import sys
-from pathlib import Path
-import numpy as np
-import pandas as pd
-
-RACINE = next(d for d in [Path.cwd(), *Path.cwd().parents] if (d / ".git").exists())
-if str(RACINE) not in sys.path:
-    sys.path.insert(0, str(RACINE))
-
-from src.portefeuille import simuler, rendements_et_dividendes
-
-DOSSIER = RACINE / "data" / "raw" / "prix"
-BENCH = RACINE / "data" / "raw" / "benchmarks"
-SORTIE = RACINE / "data" / "processed"
-DEBUT = "2000-01-03"
-COUT = 0.0010
-
-CELLULE 12, code
-mois = pd.Series(dates)
-fins_de_mois = set(mois.groupby(mois.str[:7]).max())
-
-morceaux, series, resume = [], {}, []
-annees = len(dates) / 252
-
-for pf in [f"P{i}" for i in range(1, 11)]:
-    titres = appartenance[appartenance.portefeuille == pf].titre.tolist()
-    cibles = (poids_cibles[poids_cibles.portefeuille == pf]
-              .pivot(index="date", columns="titre", values="poids")
-              .reindex(columns=titres))
-
-    for reeq in [True, False]:
-        nom = f"{pf}_{'reeq' if reeq else 'cons'}"
-        v, rotation, photos = simuler(rendements, detachements, titres, cibles,
-                                      dates, jours_reeq, reeq, COUT, fins_de_mois)
-        v = v / v.iloc[0] * 100
-        series[nom] = v
-
-        p = photos.stack().rename("poids").reset_index()
-        p.columns = ["date", "titre", "poids"]
-        p.insert(0, "serie", nom)
-        morceaux.append(p[p.poids != 0])
-
-        resume.append({"serie": nom, "base100": v.iloc[-1],
-                       "annualise": (v.iloc[-1] / 100) ** (1 / annees) - 1,
-                       "rotation": rotation})
-
-valeurs = pd.DataFrame(series)
-valeurs.to_csv(SORTIE / "valeurs_portefeuilles.csv", encoding="utf-8")
-pd.concat(morceaux, ignore_index=True).to_csv(SORTIE / "poids_mensuels.csv",
-                                              index=False, encoding="utf-8")
-
-print(valeurs.shape)
-print(pd.DataFrame(resume).set_index("serie").to_string(float_format=lambda x: f"{x:,.4f}"))
-
-CELLULE 13, code
-
-
-CELLULE 14, code
-
-
-CELLULE 15, code
-
-
-CELLULE 16, code
-
-
-CELLULE 17, code
+comparaisons = pd.read_csv(SORTIE / "valeurs_comparaisons.csv", index_col=0)
+print(comparaisons.tail())
+construction.verifier(SORTIE, RACINE)
+print("Empreintes vérifiées après les calculs et les contrôles.")
```

</details>

### `src/construire_portefeuilles.py`

Créer une reconstruction locale unique, des contrôles avant publication et un manifeste des dépendances et résultats.

Avant : fichier absent. Après : `aebcf04b0e086ca5874be0d1cbf6021de30a01864cd3a8a30b87c51eca13863c`.

Lignes physiques : 0 avant, 308 après.

Les repères `@@` indiquent les lignes avant et après. `-` contient le texte retiré, `+` le texte retenu.

<details>
<summary>Contenu exact des changements</summary>

```diff
--- src/construire_portefeuilles.py avant
+++ src/construire_portefeuilles.py après
@@ -0,0 +1,308 @@
+"""Reconstruction locale de l'étape 2, sans collecte ni modification des preuves.
+
+Exécution : python -m src.construire_portefeuilles
+Contrôle des empreintes : python -m src.construire_portefeuilles --check-only
+"""
+from pathlib import Path
+import argparse
+import hashlib
+import importlib.metadata
+import json
+import re
+import shutil
+import sys
+import tempfile
+from datetime import datetime, timezone
+
+import numpy as np
+import pandas as pd
+
+from src.portefeuille import COUT, poids_cibles, preparer_prix, simuler
+
+RACINE = Path(__file__).resolve().parents[1]
+DEBUT = "2000-01-03"
+
+
+def empreinte(path):
+    return hashlib.sha256(path.read_bytes()).hexdigest()
+
+
+def ecrire_json(path, contenu):
+    path.write_text(json.dumps(contenu, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
+
+
+def verifier_bruts(racine):
+    raw = racine / "data/raw"
+    m = json.loads((raw / "prix_manifest.json").read_text(encoding="utf-8"))
+    sources = [raw / "prix_manifest.json"]
+    for groupe in ("prix", "benchmarks"):
+        attendus = {e["fichier"] for e in m[groupe]}
+        if attendus != {p.name for p in (raw / groupe).glob("*.csv")}:
+            raise ValueError(f"Inventaire brut différent du manifeste : {groupe}")
+        if len(attendus) != len(m[groupe]):
+            raise ValueError(f"Fichier répété dans le manifeste : {groupe}")
+        for e in m[groupe]:
+            p = raw / groupe / e["fichier"]
+            if p.parent.resolve() != (raw / groupe).resolve() or empreinte(p) != e["sha256"]:
+                raise ValueError(f"Empreinte brute invalide : {p.name}")
+            sources.append(p)
+    for groupe in ("calendrier", "actions", "metadonnees"):
+        e = m[groupe]
+        p = raw / e["fichier"]
+        if p.parent.resolve() != raw.resolve() or empreinte(p) != e["sha256"]:
+            raise ValueError(f"Empreinte invalide : {groupe}")
+        sources.append(p)
+    return sources
+
+
+def lire_prix(path):
+    df = pd.read_csv(path)
+    df.index = pd.Index(df.date.str[:10], name="date")
+    if df.empty or not df.index.is_unique or not df.index.is_monotonic_increasing:
+        raise ValueError(f"Historique vide, dupliqué ou désordonné : {path.name}")
+    return df
+
+
+def appartenance(decisions):
+    retenues = decisions[decisions.verdict == "ENTRE"]
+    if retenues.cik.duplicated().any() or retenues.cik.isna().any():
+        raise ValueError("CIK retenu absent ou dupliqué.")
+    lignes = []
+    for r in retenues.itertuples():
+        if r.maturite_exposition not in {"etablie", "engagement_ou_developpement_documente"}:
+            raise ValueError(f"Maturité inconnue : {r.cik}, {r.maturite_exposition}")
+        if r.canal in {"depense", "depense et vend"}:
+            maillon = "P4"
+        elif r.canal == "vend":
+            maillon = "P5"
+        elif r.canal == "fournit":
+            maillon = {"Utilities": "P6", "Industrials": "P7", "Real Estate": "P8",
+                       "Information Technology": "P9"}.get(r.secteur, "P10")
+        else:
+            raise ValueError(f"Canal inconnu : {r.cik}, {r.canal}")
+        titres = r.symboles.replace(".", "-").split("|")
+        if not all(titres) or len(set(titres)) != len(titres):
+            raise ValueError(f"Symboles invalides : {r.cik}")
+        for pf in ["P1", "P2" if r.maturite_exposition == "etablie" else "P3", maillon]:
+            for titre in titres:
+                nom = re.sub(r"\s*\(Class [A-Z]\)$", "", r.nom) if len(titres) > 1 else r.nom
+                lignes.append({"portefeuille": pf, "entreprise": nom, "cik": r.cik,
+                               "titre": titre, "classes": len(titres)})
+    membres = pd.DataFrame(lignes)
+    if membres.duplicated(["portefeuille", "titre"]).any():
+        raise ValueError("Un symbole appartient à plusieurs entreprises.")
+    return membres
+
+
+def annualise(valeurs):
+    """252 séances par an ; N niveaux contiennent N-1 rendements."""
+    v = valeurs.dropna()
+    return float((v.iloc[-1] / v.iloc[0]) ** (252 / (len(v) - 1)) - 1) if len(v) > 1 else None
+
+
+def construire(racine=RACINE, sortie=None, cout=COUT, controles_prix=True):
+    racine = Path(racine).resolve()
+    sortie = Path(sortie or racine / "data/processed").resolve()
+    if sortie.is_relative_to(racine / "data/raw"):
+        raise ValueError("Une reconstruction ne peut jamais écrire dans les données brutes.")
+    sources = verifier_bruts(racine)
+    raw = racine / "data/raw"
+    dates = pd.Index(pd.read_csv(raw / "calendrier_bourse.csv").date.astype(str), name="date")
+    dates = dates[dates >= DEBUT]
+    if not len(dates) or dates[0] != DEBUT or not dates.is_unique or not dates.is_monotonic_increasing:
+        raise ValueError("Calendrier invalide.")
+    annuel = set(pd.Series(dates).groupby(pd.Series(dates).str[:4]).min())
+    fins = set(pd.Series(dates).groupby(pd.Series(dates).str[:7]).max())
+    decisions = pd.read_csv(racine / "data/review/decisions_selection.csv", dtype=str)
+    membres = appartenance(decisions)
+    prix = {p.stem: lire_prix(p) for p in sorted((raw / "prix").glob("*.csv"))}
+    if set(membres.titre) != set(prix):
+        raise ValueError("Les fichiers de prix et les symboles retenus diffèrent.")
+    for titre, p in prix.items():
+        requis = dates[(dates >= p.index[0]) & (dates <= p.index[-1])]
+        if not set(requis) <= set(p.index) or p.index[-1] != dates[-1]:
+            raise ValueError(f"Séance brute absente ou historique arrêté : {titre}")
+    regles = pd.read_csv(racine / "data/review/regles_historiques_prix.csv", dtype=str)
+    if regles.titre.duplicated().any() or not set(regles.titre) <= set(prix):
+        raise ValueError("Règles d'historique dupliquées ou hors univers.")
+    for regle in regles.itertuples():
+        prix[regle.titre] = prix[regle.titre].loc[regle.debut_admissible:]
+    prepares = {t: preparer_prix(p).reindex(dates) for t, p in prix.items()}
+    matrices = {champ: pd.DataFrame({t: p[champ] for t, p in prepares.items()}, index=dates)
+                for champ in ["rendement_observe", "rendement_valorisation", "dividende", "disponible", "cours_porte"]}
+    r, d = matrices["rendement_valorisation"], matrices["dividende"]
+    dispo = matrices["disponible"].fillna(False).astype(bool)
+    # La présence commence au premier cours utilisable, pas au premier rendement.
+    premiers = {t: dispo.index[dispo[t]][0] for t in dispo}
+    cibles_lignes, valeurs, photos, journaux, resumes, reports = [], {}, [], [], [], []
+    for pf, groupe in membres.groupby("portefeuille", sort=True):
+        titres = sorted(groupe.titre)
+        entreprises = groupe.set_index("titre").cik.to_dict()
+        evenements, annuel_effectif = set(), set()
+        for demande in sorted(annuel | {premiers[t] for t in titres}):
+            # Je ne vends pas un titre à un cours absent. Toute l'opération est
+            # reportée à la première séance où les positions sont négociables.
+            effectif = None
+            for jour in dates[dates >= demande]:
+                admis = [t for t in titres if premiers[t] <= jour]
+                if dispo.loc[jour, admis].all():
+                    effectif = jour
+                    break
+            if effectif is None:
+                raise ValueError(f"Opération impossible avant la fin de série : {pf}, {demande}")
+            evenements.add(effectif)
+            if demande in annuel:
+                annuel_effectif.add(effectif)
+            if effectif != demande:
+                reports.append({"portefeuille": pf, "date_prevue": demande, "date_effective": effectif,
+                                "motif": "cotation absente, aucune opération au cours porté"})
+        evenements = sorted(evenements)
+        cibles = []
+        for jour in evenements:
+            admis = [t for t in titres if premiers[t] <= jour]
+            if not dispo.loc[jour, admis].all():
+                raise ValueError(f"Cotation absente lors d'une opération : {pf}, {jour}")
+            w = poids_cibles(groupe, admis)
+            if not w:
+                raise ValueError(f"Portefeuille sans titre initial : {pf}")
+            cibles.append({t: w.get(t, 0.0) for t in titres})
+            for t, poids in w.items():
+                cibles_lignes.append({"portefeuille": pf, "date": jour, "titre": t,
+                    "entreprise": groupe.set_index("titre").at[t, "entreprise"],
+                    "poids": poids, "motif": "annuel" if jour in annuel_effectif else "entree"})
+        cible = pd.DataFrame(cibles, index=evenements, columns=titres)
+        for reeq, suffixe in [(True, "reeq"), (False, "cons")]:
+            nom = pf + "_" + suffixe
+            journal = []
+            v, rotation, photo = simuler(r, d, titres, cible, dates, annuel_effectif, reeq, cout,
+                fins_de_mois=fins, disponibilite=dispo, entreprises=entreprises, journal=journal)
+            valeurs[nom] = 100 * v / v.iloc[0]
+            ph = photo.rename_axis("date").reset_index().melt("date", var_name="titre", value_name="poids")
+            ph["serie"] = nom
+            photos.append(ph[["date", "serie", "titre", "poids"]])
+            j = pd.DataFrame(journal)
+            j["serie"] = nom
+            journaux.append(j)
+            brut, _, _ = simuler(r, d, titres, cible, dates, annuel_effectif, reeq, 0,
+                disponibilite=dispo, entreprises=entreprises)
+            resumes.append({"serie": nom, "base100": valeurs[nom].iloc[-1],
+                "annualise": annualise(v), "rotation_annuelle": rotation,
+                "cout_annualise_pb": 10000 * (annualise(brut) - annualise(v)),
+                "repli_maximal": float((v / v.cummax() - 1).min())})
+    valeurs = pd.DataFrame(valeurs, index=dates)
+    photos, journal = pd.concat(photos, ignore_index=True), pd.concat(journaux, ignore_index=True)
+    sommes = photos.groupby(["date", "serie"]).poids.sum()
+    if not np.allclose(sommes, 1, rtol=0, atol=1e-12) or photos.poids.lt(0).any():
+        raise ArithmeticError("Les poids produits sont invalides.")
+    j = journal[journal.valeur_avant > 0]
+    ecart = (j.valeur / j.valeur_avant - 1 - j.rendement_attendu_avant_frais + j.frais / j.valeur_avant).abs()
+    if not np.isfinite(ecart).all() or ecart.max() > 1e-12:
+        raise ArithmeticError("La valeur n'est pas expliquée par les positions, dividendes et frais.")
+    if not np.allclose(j.frais, cout * j.echange, rtol=1e-10, atol=1e-14):
+        raise ArithmeticError("La facture ne correspond pas aux transactions.")
+    # Références homogènes : dividendes du fonds en espèces, réinvestis en janvier.
+    # Les valeurs ajustées du fournisseur restent disponibles séparément.
+    comparaisons, yahoo = {}, {}
+    for fichier in sorted((raw / "benchmarks").glob("*.csv")):
+        t = fichier.stem
+        p = lire_prix(fichier)
+        if not np.isfinite(p['Adj Close']).all() or p['Adj Close'].le(0).any():
+            raise ValueError(f"Cours ajusté de comparaison invalide : {t}")
+        adj = p['Adj Close'].reindex(dates)
+        yahoo[t] = adj / adj.dropna().iloc[0] * 100
+        if t not in {"SPY", "RSP"}:
+            comparaisons[t] = yahoo[t]
+            continue
+        ds = dates[dates >= p.index[0]]
+        pp = preparer_prix(p).reindex(ds)
+        if not pp.disponible.all():
+            raise ValueError(f"Observation manquante dans le fonds de comparaison : {t}")
+        ja = set(pd.Series(ds).groupby(pd.Series(ds).str[:4]).min())
+        cible = pd.DataFrame({t: 1.0}, index=sorted(ja))
+        v, _, _ = simuler(pp[["rendement_valorisation"]].rename(columns={"rendement_valorisation": t}),
+            pp[["dividende"]].rename(columns={"dividende": t}), [t], cible, ds, ja, False, cout,
+            disponibilite=pp[["disponible"]].rename(columns={"disponible": t}))
+        comparaisons[t] = v / v.iloc[0] * 100
+    qualite = []
+    for t, pp in prepares.items():
+        for jour in pp.index[pp.cours_porte.fillna(False)]:
+            qualite.append({"titre": t, "date": jour, "motif": "dernier cours connu porté",
+                "reprise": pp.index[(pp.index > jour) & pp.disponible.fillna(False)].min()})
+    resume_controles = {"seances": len(dates), "titres": len(prix), "entreprises": membres.cik.nunique(),
+        "series": len(valeurs.columns), "releves_mensuels": len(fins), "lignes_poids": len(photos),
+        "ecart_somme_poids": float((sommes - 1).abs().max()), "ecart_identite_quotidienne": float(ecart.max()),
+        "cours_portes": len(qualite), "cout": cout,
+        "limite": "Identités comptables contrôlées, exactitude des prix non garantie par ces identités."}
+    sortie.mkdir(parents=True, exist_ok=True)
+    # Les résultats complets sont contrôlés en mémoire avant leur publication.
+    with tempfile.TemporaryDirectory(prefix="portefeuilles_") as tmp:
+        stage = Path(tmp).resolve()
+        tables = {"appartenance.csv": (membres, False), "poids_cibles.csv": (pd.DataFrame(cibles_lignes), False),
+            "rendements_prix.csv": (matrices["rendement_observe"], True),
+            "rendements_valorisation.csv": (r, True), "dividendes.csv": (d, True),
+            "valeurs_portefeuilles.csv": (valeurs, True), "poids_mensuels.csv": (photos, False),
+            "journal_portefeuilles.csv": (journal, False), "mesures_portefeuilles.csv": (pd.DataFrame(resumes), False),
+            "qualite_valorisation.csv": (pd.DataFrame(qualite, columns=["titre", "date", "motif", "reprise"]), False),
+            "operations_reportees.csv": (pd.DataFrame(reports, columns=["portefeuille", "date_prevue", "date_effective", "motif"]), False),
+            "valeurs_comparaisons.csv": (pd.DataFrame(comparaisons, index=dates), True),
+            "valeurs_comparaisons_yahoo.csv": (pd.DataFrame(yahoo, index=dates), True)}
+        for nom, (df, index) in tables.items():
+            df.to_csv(stage / nom, index=index, encoding="utf-8")
+        ecrire_json(stage / "controles_portefeuilles.json", resume_controles)
+        if controles_prix:
+            from src.controle_prix import controler
+            controler(racine, stage)
+        sources += [racine / p for p in ["data/review/decisions_selection.csv", "data/review/regles_historiques_prix.csv", "data/raw/sp500_constituents.csv",
+            "data/raw/premieres_cotations.csv", "requirements.txt", "src/portefeuille.py", "src/construire_portefeuilles.py",
+            "src/controle_prix.py", "src/construire_portefeuille.ipynb", "src/controler_prix.ipynb",
+            "tests/test_portefeuille.py", "tests/test_audit_portefeuilles.py", "research/portefeuilles.md"]]
+        sources += sorted((racine / "tests").glob("test_pipeline_portefeuilles.py"))
+        fichiers = sorted(stage.iterdir())
+        manifeste = {"statut": "termine", "produit_le": datetime.now(timezone.utc).isoformat(),
+            "python": sys.version.split()[0], "bibliotheques": {p: importlib.metadata.version(p) for p in ["pandas", "numpy"]},
+            "commande": "python -m src.construire_portefeuilles", "regles": resume_controles,
+            "entrees_sha256": {str(p.relative_to(racine)).replace('\\', '/'): empreinte(p) for p in sources},
+            "sorties_sha256": {p.name: empreinte(p) for p in fichiers}}
+        for p in fichiers:
+            shutil.copyfile(p, sortie / p.name)
+        ecrire_json(sortie / "pipeline_portefeuilles.json", manifeste)
+    return resume_controles
+
+
+def verifier(sortie, racine=RACINE):
+    sortie, racine = Path(sortie).resolve(), Path(racine).resolve()
+    verifier_bruts(racine)
+    manifeste = json.loads((sortie / "pipeline_portefeuilles.json").read_text(encoding="utf-8"))
+    if manifeste.get("statut") != "termine":
+        raise ValueError("Reconstruction non terminée.")
+    obligatoires = {"valeurs_portefeuilles.csv", "poids_mensuels.csv", "appartenance.csv",
+                   "valeurs_comparaisons.csv", "rendements_valorisation.csv", "journal_portefeuilles.csv",
+                   "mesures_portefeuilles.csv", "controles_portefeuilles.json"}
+    if not obligatoires <= set(manifeste.get("sorties_sha256", {})) or not manifeste.get("entrees_sha256"):
+        raise ValueError("Manifeste incomplet.")
+    for nom, attendu in manifeste["entrees_sha256"].items():
+        p = (racine / nom).resolve()
+        if not p.is_relative_to(racine.resolve()) or empreinte(p) != attendu:
+            raise ValueError(f"Entrée modifiée depuis le calcul : {nom}")
+    for nom, attendu in manifeste["sorties_sha256"].items():
+        p = (sortie / nom).resolve()
+        if p.parent != sortie.resolve() or empreinte(p) != attendu:
+            raise ValueError(f"Sortie modifiée depuis le calcul : {nom}")
+    return True
+
+
+def main():
+    parser = argparse.ArgumentParser(description=__doc__)
+    parser.add_argument("--check-only", action="store_true")
+    parser.add_argument("--output", type=Path, default=RACINE / "data/processed")
+    parser.add_argument("--cout", type=float, default=COUT)
+    args = parser.parse_args()
+    if args.check_only:
+        verifier(args.output)
+        print("Empreintes de l'étape 2 vérifiées.")
+    else:
+        print(json.dumps(construire(sortie=args.output, cout=args.cout), ensure_ascii=False, indent=2))
+
+
+if __name__ == "__main__":
+    main()
```

</details>

### `src/controle_prix.py`

Séparer contrôle et acquisition, conserver la couverture calculable et corriger l’encadrement SEC par dates de mesure et de dépôt.

Avant : fichier absent. Après : `1a8ae25d030ccb7b4b156462c47a2358da218088aa8b9943071c729747d8394b`.

Lignes physiques : 0 avant, 426 après.

Les repères `@@` indiquent les lignes avant et après. `-` contient le texte retiré, `+` le texte retenu.

<details>
<summary>Contenu exact des changements</summary>

```diff
--- src/controle_prix.py avant
+++ src/controle_prix.py après
@@ -0,0 +1,426 @@
+"""Contrôles locaux des prix, extraits du notebook le 8 septembre 2026.
+
+Les acquisitions sont séparées des contrôles : ce module ne touche jamais
+aux preuves brutes. Les comptes SEC ne prouvent pas le prix du titre.
+"""
+from pathlib import Path
+import numpy as np
+import pandas as pd
+
+
+def verifier_structure_prix(d, nom):
+    """Refuse les échecs qui rendraient les comparaisons silencieusement vides.
+
+    Les prix manquants restent des anomalies à examiner. Un événement ou un
+    volume inconnu n'est jamais assimilé à zéro, ni une infinité à un prix.
+    """
+    requis = {"date", "Open", "High", "Low", "Close", "Adj Close", "Volume", "Dividends", "Stock Splits"}
+    if d.empty or not requis <= set(d.columns):
+        raise ValueError(f"Fichier vide ou colonnes manquantes : {nom}")
+    if d.date.isna().any():
+        raise ValueError(f"Date absente : {nom}")
+    jours = d.date.str[:10]
+    # Le suffixe de fuseau est contrôlé dans le rapport, la date doit exister.
+    pd.to_datetime(jours, format="%Y-%m-%d", errors="raise")
+    if not jours.is_monotonic_increasing:
+        raise ValueError(f"Dates désordonnées : {nom}")
+    nombres = d[list(requis - {"date"})].apply(pd.to_numeric, errors="raise")
+    if np.isinf(nombres).any().any():
+        raise ValueError(f"Valeur infinie : {nom}")
+    evenements = nombres[["Dividends", "Stock Splits", "Volume"]]
+    if evenements.isna().any().any() or evenements.lt(0).any().any():
+        raise ValueError(f"Événement ou volume absent ou négatif : {nom}")
+    if not d.Close.notna().any() or not d['Adj Close'].notna().any():
+        raise ValueError(f"Aucun prix calculable : {nom}")
+
+
+def controler(racine, sortie):
+    RACINE, SORTIE = Path(racine), Path(sortie)
+    SORTIE.mkdir(parents=True, exist_ok=True)
+    DOSSIER, BENCH = RACINE / "data/raw/prix", RACINE / "data/raw/benchmarks"
+    fichiers = sorted(list(DOSSIER.glob("*.csv")) + list(BENCH.glob("*.csv")))
+    if not fichiers:
+        raise ValueError("Aucun fichier de prix à contrôler.")
+    couverture = []
+    for fichier in fichiers:
+        d = pd.read_csv(fichier)
+        verifier_structure_prix(d, fichier.name)
+        couverture.append({"fichier": fichier.name, "lignes": len(d),
+                           "structure_verifiee": True})
+    # Tâche, cellule historique 1.
+    CONTROLE = SORTIE / "controle_prix.csv"
+
+    seances = set(pd.read_csv(RACINE / "data" / "raw" / "calendrier_bourse.csv")["date"].astype(str))
+    debut_cal, fin_cal = min(seances), max(seances)
+
+    # Tâche, cellule historique 2.
+    anomalies = []
+
+    for fichier in sorted(list(DOSSIER.glob("*.csv")) + list(BENCH.glob("*.csv"))):
+        dates = pd.read_csv(fichier, usecols=["date"])["date"].str[:10]
+        debut, fin = dates.iloc[0], dates.iloc[-1]
+
+        for j in dates[dates.duplicated()].unique():
+            anomalies.append({"fichier": fichier.name, "test": "date en double",
+                              "date": j, "detail": ""})
+
+        avant = int((dates < debut_cal).sum())
+        if avant:
+            anomalies.append({"fichier": fichier.name, "test": "anteriorite au calendrier",
+                              "date": debut, "detail": f"{avant} seances avant {debut_cal}"})
+
+        bas, haut = max(debut, debut_cal), min(fin, fin_cal)
+        couvertes = set(dates[(dates >= bas) & (dates <= haut)])
+        attendues = {j for j in seances if bas <= j <= haut}
+
+        for j in sorted(attendues - couvertes):
+            anomalies.append({"fichier": fichier.name, "test": "seance absente",
+                              "date": j, "detail": ""})
+        for j in sorted(couvertes - seances):
+            anomalies.append({"fichier": fichier.name, "test": "date hors calendrier",
+                              "date": j, "detail": ""})
+
+    controle = pd.DataFrame(anomalies, columns=["fichier", "test", "date", "detail"])
+    controle.to_csv(CONTROLE, index=False, encoding="utf-8")
+
+    print(len(controle), "anomalies")
+    if len(controle):
+        print(controle.test.value_counts().to_string())
+        print()
+        print(controle[controle.test == "seance absente"].fichier.value_counts().head(10).to_string())
+
+    # Tâche, cellule historique 3.
+    SEUIL = 0.30
+    TESTS = ["variation quotidienne extreme", "barre incoherente",
+             "prix nul ou negatif", "valeur manquante"]
+    COLS = ["Open", "High", "Low", "Close", "Adj Close"]
+
+    # Tâche, cellule historique 4.
+    anomalies = []
+
+    for fichier in sorted(list(DOSSIER.glob("*.csv")) + list(BENCH.glob("*.csv"))):
+        d = pd.read_csv(fichier, usecols=["date"] + COLS)
+        d["j"] = d["date"].str[:10]
+
+        var = d["Adj Close"].pct_change(fill_method=None)
+        for i in var[var.abs() > SEUIL].index:
+            anomalies.append({"fichier": fichier.name, "test": "variation quotidienne extreme",
+                              "date": d.j[i], "detail": f"{var[i] * 100:+.1f} %"})
+
+        incoherent = ((d.Low > d.High) | (d.Open < d.Low) | (d.Open > d.High)
+                      | (d.Close < d.Low) | (d.Close > d.High))
+        for i in d.index[incoherent]:
+            r = d.loc[i]
+            anomalies.append({"fichier": fichier.name, "test": "barre incoherente", "date": r.j,
+                              "detail": f"O={r.Open:.2f} H={r.High:.2f} L={r.Low:.2f} C={r.Close:.2f}"})
+
+        for i in d.index[(d[COLS] <= 0).any(axis=1)]:
+            anomalies.append({"fichier": fichier.name, "test": "prix nul ou negatif",
+                              "date": d.j[i], "detail": ""})
+
+        for i in d.index[d[COLS].isna().any(axis=1)]:
+            anomalies.append({"fichier": fichier.name, "test": "valeur manquante",
+                              "date": d.j[i], "detail": ""})
+
+    ancien = pd.read_csv(CONTROLE)
+    ancien = ancien[~ancien.test.isin(TESTS)]
+    controle = pd.concat([ancien, pd.DataFrame(anomalies, columns=["fichier", "test", "date", "detail"])], ignore_index=True)
+    controle.to_csv(CONTROLE, index=False, encoding="utf-8")
+
+    print(len(anomalies), "nouvelles anomalies |", len(controle), "au total")
+    print(pd.DataFrame(anomalies, columns=["fichier", "test", "date", "detail"]).test.value_counts().to_string())
+
+    # Tâche, cellule historique 5.
+    TOL = 1e-4
+    TESTS_15 = ["ajustement incoherent"]
+
+    # Tâche, cellule historique 6.
+    anomalies, ecarts = [], []
+
+    for fichier in sorted(list(DOSSIER.glob("*.csv")) + list(BENCH.glob("*.csv"))):
+        d = pd.read_csv(fichier, usecols=["date", "Close", "Adj Close", "Dividends", "Stock Splits"])
+        d["j"] = d["date"].str[:10]
+
+        r_ajuste = d["Adj Close"].pct_change(fill_method=None)
+        r_additif = (d["Close"] + d["Dividends"]) / d["Close"].shift() - 1
+        r_multiplicatif = d["Close"] / (d["Close"].shift() - d["Dividends"]) - 1
+
+        e_add = (r_ajuste - r_additif).abs()
+        e_mul = (r_ajuste - r_multiplicatif).abs()
+        if not e_mul.notna().any() or np.isinf(e_mul).any():
+            raise ValueError(f"Ajustement non calculable : {fichier.name}")
+        ecarts.append({"fichier": fichier.name, "additif": e_add.max(),
+                       "multiplicatif": e_mul.max(), "comparaisons": int(e_mul.notna().sum())})
+
+        for i in e_mul[e_mul > TOL].index:
+            anomalies.append({"fichier": fichier.name, "test": "ajustement incoherent",
+                              "date": d.j[i], "detail": f"ecart {e_mul[i]:.2e}"})
+
+    ecarts = pd.DataFrame(ecarts)
+
+    ancien = pd.read_csv(CONTROLE)
+    ancien = ancien[~ancien.test.isin(TESTS_15)]
+    controle = pd.concat([ancien, pd.DataFrame(anomalies, columns=["fichier", "test", "date", "detail"])], ignore_index=True)
+    controle.to_csv(CONTROLE, index=False, encoding="utf-8")
+
+    print("ecart maximal, tous fichiers confondus")
+    print(ecarts[["additif", "multiplicatif"]].max().to_string())
+    print()
+    print(ecarts.sort_values("additif", ascending=False).head(8).to_string(index=False))
+    print()
+    print(len(anomalies), "ajustements incoherents |", len(controle), "au total")
+
+    # Tâche, cellule historique 7.
+    TESTS_16 = ["division non confirmee"]
+    DEBUT_SEC = "2010-01-01"
+    TOL_SPLIT = 0.02
+
+    # Tâche, cellule historique 8.
+    sp500 = pd.read_csv(RACINE / "data/raw/sp500_constituents.csv", dtype=str)
+    correspondance = sp500[["CIK", "Symbol"]].rename(columns={"CIK": "cik", "Symbol": "symbole"})
+    correspondance["symbole"] = correspondance.symbole.str.replace(".", "-", regex=False)
+    actions = pd.read_csv(RACINE / "data/raw/actions_en_circulation.csv", dtype={"cik": str})
+    actions = actions[actions.notion == "actions"].merge(correspondance, on="cik", validate="many_to_many")
+    actions = actions.sort_values(["depose_le", "fin", "valeur", "depot"], kind="stable")
+
+
+    # Tâche, cellule historique 9.
+    anomalies, mesures = [], []
+
+    for fichier in sorted(DOSSIER.glob("*.csv")):
+        d = pd.read_csv(fichier, usecols=["date", "Stock Splits"]).rename(
+            columns={"Stock Splits": "division"})
+        d["j"] = d["date"].str[:10]
+        divisions = d[(d.division > 0) & (d.j >= DEBUT_SEC)]
+        if divisions.empty:
+            continue
+
+        serie = actions[actions.symbole == fichier.stem]
+
+        for r in divisions.itertuples():
+            avant = serie[(serie.depose_le < r.j) & (serie.fin < r.j)].sort_values(["fin", "depose_le", "valeur", "depot"], kind="stable").tail(1)
+            apres = serie[(serie.depose_le > r.j) & (serie.fin >= r.j)].sort_values(["fin", "depose_le", "valeur", "depot"], kind="stable").head(1)
+            if avant.empty or apres.empty:
+                mesures.append({"symbole": fichier.stem, "date": r.j, "annonce": r.division,
+                                "mesure": None, "ecart": None, "avant_fin": None, "apres_fin": None})
+                continue
+
+            mesure = apres.valeur.iloc[0] / avant.valeur.iloc[0]
+            ecart = abs(mesure / r.division - 1)
+            mesures.append({"symbole": fichier.stem, "date": r.j, "annonce": r.division,
+                            "mesure": mesure, "ecart": ecart, "avant_fin": avant.fin.iloc[0], "apres_fin": apres.fin.iloc[0], "avant_depose": avant.depose_le.iloc[0], "apres_depose": apres.depose_le.iloc[0]})
+
+            if ecart > TOL_SPLIT:
+                anomalies.append({"fichier": fichier.name, "test": "division non confirmee",
+                                  "date": r.j,
+                                  "detail": f"annonce {r.division:g}, mesure {mesure:.3f}"})
+
+    mesures = pd.DataFrame(mesures, columns=["symbole", "date", "annonce", "mesure", "ecart", "avant_fin", "apres_fin", "avant_depose", "apres_depose"])
+    mesures.to_csv(SORTIE / "controle_divisions_sec.csv", index=False)
+
+    ancien = pd.read_csv(CONTROLE)
+    ancien = ancien[~ancien.test.isin(TESTS_16)]
+    controle = pd.concat([ancien, pd.DataFrame(anomalies, columns=["fichier", "test", "date", "detail"])], ignore_index=True)
+    controle.to_csv(CONTROLE, index=False, encoding="utf-8")
+
+    print(len(mesures), "divisions depuis", DEBUT_SEC)
+    print(int(mesures.mesure.isna().sum()), "sans encadrement SEC")
+    print(len(anomalies), "non confirmees |", len(controle), "au total")
+    print()
+    print(mesures.dropna(subset=["ecart"]).sort_values("ecart", ascending=False)
+          .head(24).to_string(index=False))
+
+    # Tâche, cellule historique 10.
+    TESTS_17 = ["reference de cotation absente", "premiere cotation discordante",
+                "historique tronque"]
+
+    composants = pd.read_csv(RACINE / "data" / "raw" / "sp500_constituents.csv", dtype=str)
+    entree = dict(zip(composants.Symbol.str.replace(".", "-", regex=False),
+                      composants["Date added"]))
+
+    reference = pd.read_csv(RACINE / "data" / "raw" / "premieres_cotations.csv")
+    premiere = dict(zip(reference.ticker, reference.premiere_cotation))
+
+    # Tâche, cellule historique 11.
+    anomalies, debuts = [], []
+
+    for fichier in sorted(DOSSIER.glob("*.csv")):
+        debut = pd.read_csv(fichier, usecols=["date"], nrows=1).date.iloc[0][:10]
+        ref = premiere.get(fichier.stem)
+        ajout = entree.get(fichier.stem)
+        debuts.append({"symbole": fichier.stem, "prix": debut, "reference": ref, "indice": ajout})
+
+        if ref is None:
+            anomalies.append({"fichier": fichier.name, "test": "reference de cotation absente",
+                              "date": debut, "detail": ""})
+        elif ref != debut:
+            anomalies.append({"fichier": fichier.name, "test": "premiere cotation discordante",
+                              "date": debut, "detail": f"reference {ref}"})
+
+        if ajout is not None and ajout < debut:
+            anomalies.append({"fichier": fichier.name, "test": "historique tronque",
+                              "date": debut, "detail": f"entree dans l'indice le {ajout}"})
+
+    debuts = pd.DataFrame(debuts)
+
+    ancien = pd.read_csv(CONTROLE)
+    ancien = ancien[~ancien.test.isin(TESTS_17)]
+    controle = pd.concat([ancien, pd.DataFrame(anomalies, columns=["fichier", "test", "date", "detail"])], ignore_index=True)
+    controle.to_csv(CONTROLE, index=False, encoding="utf-8")
+
+    print(len(anomalies), "anomalies |", len(controle), "au total")
+    print(pd.DataFrame(anomalies, columns=["fichier", "test", "date", "detail"]).test.value_counts().to_string())
+    print()
+    print("dates de debut partagees par plusieurs titres")
+    compte = debuts.prix.value_counts()
+    print(compte[compte > 1].to_string())
+
+    # Tâche, cellule historique 13.
+    TESTS_18 = ["metadonnees absentes", "devise non usd", "fuseau inattendu", "type inattendu",
+                "decalage horaire inattendu", "premiere transaction discordante"]
+
+    FUSEAUX = {"EST", "EDT"}
+    DECALAGES = {"-05:00", "-04:00"}
+
+    meta = pd.read_csv(RACINE / "data" / "raw" / "metadonnees_titres.csv")
+    attendu = {r.fichier: r.premiere_transaction for r in meta.itertuples()
+               if isinstance(r.premiere_transaction, str)}
+    decrits = set(meta.fichier)
+    if meta.fichier.duplicated().any():
+        raise ValueError("Métadonnées dupliquées.")
+    anomalies = []
+
+    for r in meta.itertuples():
+        if r.devise != "USD":
+            anomalies.append({"fichier": r.fichier, "test": "devise non usd",
+                              "date": "", "detail": str(r.devise)})
+        if r.fuseau not in FUSEAUX:
+            anomalies.append({"fichier": r.fichier, "test": "fuseau inattendu",
+                              "date": "", "detail": str(r.fuseau)})
+
+        attendus = {"EQUITY"} if (DOSSIER / r.fichier).exists() else ({"ETF"} if r.fichier in {"SPY.csv", "RSP.csv"} else {"INDEX"})
+        if r.type not in attendus:
+            anomalies.append({"fichier": r.fichier, "test": "type inattendu",
+                              "date": "", "detail": str(r.type)})
+
+    for fichier in fichiers:
+        if fichier.name not in decrits:
+            anomalies.append({"fichier": fichier.name, "test": "metadonnees absentes",
+                              "date": "", "detail": ""})
+
+        d = pd.read_csv(fichier, usecols=["date"])
+        for x in sorted(set(d.date.str[-6:]) - DECALAGES):
+            anomalies.append({"fichier": fichier.name, "test": "decalage horaire inattendu",
+                              "date": "", "detail": x})
+
+        debut = d.date.iloc[0][:10]
+        declaree = attendu.get(fichier.name)
+        if declaree and declaree != debut:
+            anomalies.append({"fichier": fichier.name, "test": "premiere transaction discordante",
+                              "date": debut, "detail": f"declaree {declaree}"})
+
+    ancien = pd.read_csv(CONTROLE)
+    ancien = ancien[~ancien.test.isin(TESTS_18)]
+    controle = pd.concat([ancien, pd.DataFrame(anomalies, columns=["fichier", "test", "date", "detail"])], ignore_index=True)
+    controle.to_csv(CONTROLE, index=False, encoding="utf-8")
+
+    print(len(anomalies), "anomalies |", len(controle), "au total")
+    if anomalies:
+        print(pd.DataFrame(anomalies, columns=["fichier", "test", "date", "detail"]).test.value_counts().to_string())
+
+    # Tâche, cellule historique 14.
+    TESTS_19 = ["fin de serie anticipee", "denomination divergente"]
+
+    import re
+
+    def normaliser(nom):
+        n = str(nom).lower()
+        for mot in [" incorporated", " corporation", " companies", " company", " holdings",
+                    " group", " inc", " corp", " plc", " ltd", " the", " co",
+                    " & ", " and ", ".", ",", "'", "-"]:
+            n = n.replace(mot, " ")
+        return re.sub(r"\s+", " ", n).strip()
+
+    calendrier = pd.read_csv(RACINE / "data" / "raw" / "calendrier_bourse.csv")["date"].astype(str)
+    derniere = calendrier.max()
+
+    meta = pd.read_csv(RACINE / "data" / "raw" / "metadonnees_titres.csv")
+    composants = pd.read_csv(RACINE / "data" / "raw" / "sp500_constituents.csv", dtype=str)
+    nom_indice = dict(zip(composants.Symbol.str.replace(".", "-", regex=False), composants.Security))
+
+    anomalies = []
+
+    for fichier in fichiers:
+        fin = pd.read_csv(fichier, usecols=["date"]).date.iloc[-1][:10]
+        if fin < derniere:
+            anomalies.append({"fichier": fichier.name, "test": "fin de serie anticipee",
+                              "date": fin, "detail": f"derniere seance {derniere}"})
+
+    for r in meta.itertuples():
+        reference = nom_indice.get(r.symbole)
+        if reference is None:
+            continue
+        a, b = normaliser(r.nom), normaliser(reference)
+        if not (a.startswith(b[:8]) or b.startswith(a[:8])):
+            anomalies.append({"fichier": r.fichier, "test": "denomination divergente",
+                              "date": "", "detail": f"{r.nom} contre {reference}"})
+
+    ancien = pd.read_csv(CONTROLE)
+    ancien = ancien[~ancien.test.isin(TESTS_19)]
+    controle = pd.concat([ancien, pd.DataFrame(anomalies, columns=["fichier", "test", "date", "detail"])], ignore_index=True)
+    controle.to_csv(CONTROLE, index=False, encoding="utf-8")
+
+    print(len(anomalies), "anomalies |", len(controle), "au total")
+    if anomalies:
+        print(pd.DataFrame(anomalies, columns=["fichier", "test", "date", "detail"]).test.value_counts().to_string())
+        print()
+        print(pd.DataFrame(anomalies, columns=["fichier", "test", "date", "detail"])[["fichier", "detail"]].to_string(index=False))
+
+    # Tâche, cellule historique 15.
+    TESTS_19B = ["seance sans transaction", "prix fige"]
+
+    anomalies = []
+    resume = []
+
+    for fichier in sorted(DOSSIER.glob("*.csv")):
+        d = pd.read_csv(fichier, usecols=["date", "Open", "High", "Low", "Close", "Volume"])
+        d["j"] = d["date"].str[:10]
+
+        sans_volume = d.Volume == 0
+        fige = (sans_volume
+                & (d.Open == d.High) & (d.High == d.Low) & (d.Low == d.Close)
+                & (d.Close == d.Close.shift()))
+
+        if sans_volume.any():
+            resume.append({"symbole": fichier.stem, "lignes": len(d),
+                           "sans_volume": int(sans_volume.sum()), "fige": int(fige.sum()),
+                           "part": int(sans_volume.sum()) / len(d)})
+
+        for i in d.index[sans_volume & ~fige]:
+            anomalies.append({"fichier": fichier.name, "test": "seance sans transaction",
+                              "date": d.j[i], "detail": ""})
+        for i in d.index[fige]:
+            anomalies.append({"fichier": fichier.name, "test": "prix fige",
+                              "date": d.j[i], "detail": f"{d.Close[i]:.4f}"})
+
+    resume = pd.DataFrame(resume, columns=["symbole", "lignes", "sans_volume", "fige", "part"]).sort_values("sans_volume", ascending=False)
+
+    ancien = pd.read_csv(CONTROLE)
+    ancien = ancien[~ancien.test.isin(TESTS_19B)]
+    controle = pd.concat([ancien, pd.DataFrame(anomalies, columns=["fichier", "test", "date", "detail"])], ignore_index=True)
+    controle.to_csv(CONTROLE, index=False, encoding="utf-8")
+
+    print(len(anomalies), "anomalies |", len(controle), "au total")
+    print(pd.DataFrame(anomalies, columns=["fichier", "test", "date", "detail"]).test.value_counts().to_string())
+    print()
+    print(resume.head(12).to_string(index=False, formatters={"part": "{:.1%}".format}))
+    tests = list(dict.fromkeys(["date en double", "anteriorite au calendrier", "seance absente", "date hors calendrier"] + TESTS + TESTS_15 + TESTS_16 + TESTS_17 + TESTS_18 + TESTS_19 + ["seance sans transaction", "prix fige"]))
+    counts = controle.test.value_counts().reindex(tests, fill_value=0)
+    counts.rename_axis("test").rename("cas").to_csv(SORTIE / "resume_controle_prix.csv")
+    import json
+    detail = {"fichiers": couverture, "comparaisons_ajustement": ecarts.to_dict("records"),
+              "tests": counts.to_dict(), "signalements": len(controle),
+              "limite": "Un zéro signifie absence de détection sur les comparaisons calculables, pas validation externe."}
+    (SORTIE / "couverture_controle_prix.json").write_text(
+        json.dumps(detail, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
+    return controle
```

</details>

### `src/controler_prix.ipynb`

Remplacer les cellules hétérogènes, dont des collectes, par l’appel au contrôle local sans réseau.

Avant : `dc009f854cc7c264b34c9bdba1530644a54dc38c8c2668e6c52fd113e43c5c2d`. Après : `d1989ee9e77dd061d6b0f3f06f29a3d84e0e3a88e9f82ae77d350ea1dfbd41b1`.

Lignes physiques : 823 avant, 91 après.

Cellules : 22 avant, 5 après ; cellules avec sorties enregistrées : 10 avant, 0 après. Les identifiants de cellules sont uniques ; les carnets de reconstruction n’annoncent plus un ancien Python dans leurs métadonnées.

<details>
<summary>Sources des cellules avant et après</summary>

```diff
--- src/controler_prix.ipynb avant
+++ src/controler_prix.ipynb après
@@ -1,461 +1,35 @@
-CELLULE 0, code
+CELLULE 0, markdown
+# Contrôle des prix conservés
+
+## I. Le contrôle est distinct de la collecte
+
+Je peux relancer ce carnet sans télécharger ni écraser une preuve. Les anciens blocs de collecte de métadonnées et de CMS ne font plus partie du contrôle. Le calcul est dans `src/controle_prix.py` ; ses résultats, y compris les tests sans anomalie, sont enregistrés ensemble.
+
+CELLULE 1, code
 from pathlib import Path
+import sys
+import importlib
 import pandas as pd
 
-RACINE = next(d for d in [Path.cwd(), *Path.cwd().parents] if (d / ".git").exists())
-DOSSIER = RACINE / "data" / "raw" / "prix"
-BENCH = RACINE / "data" / "raw" / "benchmarks"
-
-CELLULE 1, code
-CONTROLE = RACINE / "data" / "processed" / "controle_prix.csv"
-
-seances = set(pd.read_csv(RACINE / "data" / "raw" / "calendrier_bourse.csv")["date"].astype(str))
-debut_cal, fin_cal = min(seances), max(seances)
+RACINE = next(d for d in [Path.cwd(), *Path.cwd().parents]
+              if (d / "src" / "portefeuille.py").exists())
+if str(RACINE) not in sys.path:
+    sys.path.insert(0, str(RACINE))
+SORTIE = RACINE / "data" / "processed"
 
 CELLULE 2, code
-anomalies = []
+from src.construire_portefeuilles import verifier_bruts
+import src.controle_prix as controle_module
+importlib.reload(controle_module)
+verifier_bruts(RACINE)
+controle = controle_module.controler(RACINE, SORTIE)
 
-for fichier in sorted(list(DOSSIER.glob("*.csv")) + list(BENCH.glob("*.csv"))):
-    dates = pd.read_csv(fichier, usecols=["date"])["date"].str[:10]
-    debut, fin = dates.iloc[0], dates.iloc[-1]
+CELLULE 3, markdown
+## II. Ce que les résultats établissent
 
-    for j in dates[dates.duplicated()].unique():
-        anomalies.append({"fichier": fichier.name, "test": "date en double",
-                          "date": j, "detail": ""})
-
-    avant = int((dates < debut_cal).sum())
-    if avant:
-        anomalies.append({"fichier": fichier.name, "test": "anteriorite au calendrier",
-                          "date": debut, "detail": f"{avant} seances avant {debut_cal}"})
-
-    bas, haut = max(debut, debut_cal), min(fin, fin_cal)
-    couvertes = set(dates[(dates >= bas) & (dates <= haut)])
-    attendues = {j for j in seances if bas <= j <= haut}
-
-    for j in sorted(attendues - couvertes):
-        anomalies.append({"fichier": fichier.name, "test": "seance absente",
-                          "date": j, "detail": ""})
-    for j in sorted(couvertes - seances):
-        anomalies.append({"fichier": fichier.name, "test": "date hors calendrier",
-                          "date": j, "detail": ""})
-
-controle = pd.DataFrame(anomalies)
-controle.to_csv(CONTROLE, index=False, encoding="utf-8")
-
-print(len(controle), "anomalies")
-if len(controle):
-    print(controle.test.value_counts().to_string())
-    print()
-    print(controle[controle.test == "seance absente"].fichier.value_counts().head(10).to_string())
-
-CELLULE 3, code
-SEUIL = 0.30
-TESTS = ["variation quotidienne extreme", "barre incoherente",
-         "prix nul ou negatif", "valeur manquante"]
-COLS = ["Open", "High", "Low", "Close", "Adj Close"]
+Une anomalie demande un examen ; elle ne prouve pas à elle seule une erreur. Une concordance entre nombre d'actions SEC et facteur Yahoo reste un contrôle indirect, sensible aux rachats, émissions, classes et opérations simultanées. Le rapport distingue ces limites de l'identité arithmétique des calculs.
 
 CELLULE 4, code
-anomalies = []
-
-for fichier in sorted(list(DOSSIER.glob("*.csv")) + list(BENCH.glob("*.csv"))):
-    d = pd.read_csv(fichier, usecols=["date"] + COLS)
-    d["j"] = d["date"].str[:10]
-
-    var = d["Adj Close"].pct_change(fill_method=None)
-    for i in var[var.abs() > SEUIL].index:
-        anomalies.append({"fichier": fichier.name, "test": "variation quotidienne extreme",
-                          "date": d.j[i], "detail": f"{var[i] * 100:+.1f} %"})
-
-    incoherent = ((d.Low > d.High) | (d.Open < d.Low) | (d.Open > d.High)
-                  | (d.Close < d.Low) | (d.Close > d.High))
-    for i in d.index[incoherent]:
-        r = d.loc[i]
-        anomalies.append({"fichier": fichier.name, "test": "barre incoherente", "date": r.j,
-                          "detail": f"O={r.Open:.2f} H={r.High:.2f} L={r.Low:.2f} C={r.Close:.2f}"})
-
-    for i in d.index[(d[COLS] <= 0).any(axis=1)]:
-        anomalies.append({"fichier": fichier.name, "test": "prix nul ou negatif",
-                          "date": d.j[i], "detail": ""})
-
-    for i in d.index[d[COLS].isna().any(axis=1)]:
-        anomalies.append({"fichier": fichier.name, "test": "valeur manquante",
-                          "date": d.j[i], "detail": ""})
-
-ancien = pd.read_csv(CONTROLE)
-ancien = ancien[~ancien.test.isin(TESTS)]
-controle = pd.concat([ancien, pd.DataFrame(anomalies)], ignore_index=True)
-controle.to_csv(CONTROLE, index=False, encoding="utf-8")
-
-print(len(anomalies), "nouvelles anomalies |", len(controle), "au total")
-print(pd.DataFrame(anomalies).test.value_counts().to_string())
-
-CELLULE 5, code
-TOL = 1e-4
-TESTS_15 = ["ajustement incoherent"]
-
-CELLULE 6, code
-anomalies, ecarts = [], []
-
-for fichier in sorted(list(DOSSIER.glob("*.csv")) + list(BENCH.glob("*.csv"))):
-    d = pd.read_csv(fichier, usecols=["date", "Close", "Adj Close", "Dividends", "Stock Splits"])
-    d["j"] = d["date"].str[:10]
-
-    r_ajuste = d["Adj Close"].pct_change(fill_method=None)
-    r_additif = (d["Close"] + d["Dividends"]) / d["Close"].shift() - 1
-    r_multiplicatif = d["Close"] / (d["Close"].shift() - d["Dividends"]) - 1
-
-    e_add = (r_ajuste - r_additif).abs()
-    e_mul = (r_ajuste - r_multiplicatif).abs()
-    ecarts.append({"fichier": fichier.name, "additif": e_add.max(),
-                   "multiplicatif": e_mul.max()})
-
-    for i in e_mul[e_mul > TOL].index:
-        anomalies.append({"fichier": fichier.name, "test": "ajustement incoherent",
-                          "date": d.j[i], "detail": f"ecart {e_mul[i]:.2e}"})
-
-ecarts = pd.DataFrame(ecarts)
-
-ancien = pd.read_csv(CONTROLE)
-ancien = ancien[~ancien.test.isin(TESTS_15)]
-controle = pd.concat([ancien, pd.DataFrame(anomalies)], ignore_index=True)
-controle.to_csv(CONTROLE, index=False, encoding="utf-8")
-
-print("ecart maximal, tous fichiers confondus")
-print(ecarts[["additif", "multiplicatif"]].max().to_string())
-print()
-print(ecarts.sort_values("additif", ascending=False).head(8).to_string(index=False))
-print()
-print(len(anomalies), "ajustements incoherents |", len(controle), "au total")
-
-CELLULE 7, code
-TESTS_16 = ["division non confirmee"]
-DEBUT_SEC = "2010-01-01"
-TOL_SPLIT = 0.02
-
-CELLULE 8, code
-sp500 = pd.read_csv(RACINE / "data" / "raw" / "sp500_constituents.csv", dtype=str)
-symbole = dict(zip(sp500.CIK, sp500.Symbol.str.replace(".", "-", regex=False)))
-
-actions = pd.read_csv(RACINE / "data" / "raw" / "actions_en_circulation.csv", dtype={"cik": str})
-actions = actions[actions.notion == "actions"].copy()
-actions["symbole"] = actions.cik.map(symbole)
-actions = actions.dropna(subset=["symbole"])
-actions = actions.sort_values(["depose_le", "fin", "valeur"], kind="stable")
-
-CELLULE 9, code
-anomalies, mesures = [], []
-
-for fichier in sorted(DOSSIER.glob("*.csv")):
-    d = pd.read_csv(fichier, usecols=["date", "Stock Splits"]).rename(
-        columns={"Stock Splits": "division"})
-    d["j"] = d["date"].str[:10]
-    divisions = d[(d.division > 0) & (d.j >= DEBUT_SEC)]
-    if divisions.empty:
-        continue
-
-    serie = actions[actions.symbole == fichier.stem]
-
-    for r in divisions.itertuples():
-        avant = serie[serie.depose_le < r.j].tail(1)
-        apres = serie[serie.depose_le > r.j].head(1)
-        if avant.empty or apres.empty:
-            mesures.append({"symbole": fichier.stem, "date": r.j, "annonce": r.division,
-                            "mesure": None, "ecart": None})
-            continue
-
-        mesure = apres.valeur.iloc[0] / avant.valeur.iloc[0]
-        ecart = abs(mesure / r.division - 1)
-        mesures.append({"symbole": fichier.stem, "date": r.j, "annonce": r.division,
-                        "mesure": mesure, "ecart": ecart})
-
-        if ecart > TOL_SPLIT:
-            anomalies.append({"fichier": fichier.name, "test": "division non confirmee",
-                              "date": r.j,
-                              "detail": f"annonce {r.division:g}, mesure {mesure:.3f}"})
-
-mesures = pd.DataFrame(mesures)
-
-ancien = pd.read_csv(CONTROLE)
-ancien = ancien[~ancien.test.isin(TESTS_16)]
-controle = pd.concat([ancien, pd.DataFrame(anomalies)], ignore_index=True)
-controle.to_csv(CONTROLE, index=False, encoding="utf-8")
-
-print(len(mesures), "divisions depuis", DEBUT_SEC)
-print(int(mesures.mesure.isna().sum()), "sans encadrement SEC")
-print(len(anomalies), "non confirmees |", len(controle), "au total")
-print()
-print(mesures.dropna(subset=["ecart"]).sort_values("ecart", ascending=False)
-      .head(24).to_string(index=False))
-
-CELLULE 10, code
-TESTS_17 = ["reference de cotation absente", "premiere cotation discordante",
-            "historique tronque"]
-
-composants = pd.read_csv(RACINE / "data" / "raw" / "sp500_constituents.csv", dtype=str)
-entree = dict(zip(composants.Symbol.str.replace(".", "-", regex=False),
-                  composants["Date added"]))
-
-reference = pd.read_csv(RACINE / "data" / "raw" / "premieres_cotations.csv")
-premiere = dict(zip(reference.ticker, reference.premiere_cotation))
-
-CELLULE 11, code
-anomalies, debuts = [], []
-
-for fichier in sorted(DOSSIER.glob("*.csv")):
-    debut = pd.read_csv(fichier, usecols=["date"], nrows=1).date.iloc[0][:10]
-    ref = premiere.get(fichier.stem)
-    ajout = entree.get(fichier.stem)
-    debuts.append({"symbole": fichier.stem, "prix": debut, "reference": ref, "indice": ajout})
-
-    if ref is None:
-        anomalies.append({"fichier": fichier.name, "test": "reference de cotation absente",
-                          "date": debut, "detail": ""})
-    elif ref != debut:
-        anomalies.append({"fichier": fichier.name, "test": "premiere cotation discordante",
-                          "date": debut, "detail": f"reference {ref}"})
-
-    if ajout is not None and ajout < debut:
-        anomalies.append({"fichier": fichier.name, "test": "historique tronque",
-                          "date": debut, "detail": f"entree dans l'indice le {ajout}"})
-
-debuts = pd.DataFrame(debuts)
-
-ancien = pd.read_csv(CONTROLE)
-ancien = ancien[~ancien.test.isin(TESTS_17)]
-controle = pd.concat([ancien, pd.DataFrame(anomalies)], ignore_index=True)
-controle.to_csv(CONTROLE, index=False, encoding="utf-8")
-
-print(len(anomalies), "anomalies |", len(controle), "au total")
-print(pd.DataFrame(anomalies).test.value_counts().to_string())
-print()
-print("dates de debut partagees par plusieurs titres")
-compte = debuts.prix.value_counts()
-print(compte[compte > 1].to_string())
-
-CELLULE 12, code
-import time
-import yfinance as yf
-
-META = RACINE / "data" / "raw" / "metadonnees_titres.csv"
-
-fichiers = sorted(DOSSIER.glob("*.csv")) + sorted(BENCH.glob("*.csv"))
-lignes, echecs = [], []
-
-for fichier in fichiers:
-    declare = pd.read_csv(fichier, usecols=["symbole"], nrows=1).symbole.iloc[0]
-    interroge = declare.replace(".", "-")
-
-    try:
-        m = yf.Ticker(interroge).history_metadata
-    except Exception as erreur:
-        echecs.append((interroge, type(erreur).__name__))
-        continue
-
-    ts = m.get("firstTradeDate")
-    if not ts:
-        echecs.append((interroge, "aucune premiere transaction declaree"))
-        continue
-
-    lignes.append({
-        "fichier": fichier.name,
-        "symbole": interroge,
-        "symbole_declare": declare,
-        "devise": m.get("currency"),
-        "place": m.get("fullExchangeName"),
-        "type": m.get("instrumentType"),
-        "fuseau": m.get("timezone"),
-        "nom": m.get("longName") or m.get("shortName"),
-        "premiere_transaction": str(pd.to_datetime(ts, unit="s", utc=True).date()),
-    })
-    time.sleep(0.2)
-
-meta = pd.DataFrame(lignes)
-meta["collecte_le"] = pd.Timestamp.utcnow().strftime("%Y-%m-%d")
-meta.to_csv(META, index=False, encoding="utf-8")
-
-print(len(meta), "titres decrits |", len(echecs), "echecs")
-if echecs:
-    print(echecs)
-print()
-print(meta.devise.value_counts().to_string())
-print(meta.type.value_counts().to_string())
-print(meta.place.value_counts().to_string())
-print()
-divergents = meta[meta.symbole != meta.symbole_declare]
-print(len(divergents), "fichiers ou le symbole declare differe de celui interroge")
-if len(divergents):
-    print(divergents[["fichier", "symbole", "symbole_declare"]].to_string(index=False))
-
-CELLULE 13, code
-TESTS_18 = ["metadonnees absentes", "devise non usd", "fuseau inattendu", "type inattendu",
-            "decalage horaire inattendu", "premiere transaction discordante"]
-
-FUSEAUX = {"EST", "EDT"}
-DECALAGES = {"-05:00", "-04:00"}
-
-meta = pd.read_csv(RACINE / "data" / "raw" / "metadonnees_titres.csv")
-attendu = {r.fichier: r.premiere_transaction for r in meta.itertuples()
-           if isinstance(r.premiere_transaction, str)}
-decrits = set(meta.fichier)
-anomalies = []
-
-for r in meta.itertuples():
-    if r.devise != "USD":
-        anomalies.append({"fichier": r.fichier, "test": "devise non usd",
-                          "date": "", "detail": str(r.devise)})
-    if r.fuseau not in FUSEAUX:
-        anomalies.append({"fichier": r.fichier, "test": "fuseau inattendu",
-                          "date": "", "detail": str(r.fuseau)})
-
-    attendus = {"EQUITY"} if (DOSSIER / r.fichier).exists() else {"ETF", "INDEX"}
-    if r.type not in attendus:
-        anomalies.append({"fichier": r.fichier, "test": "type inattendu",
-                          "date": "", "detail": str(r.type)})
-
-for fichier in fichiers:
-    if fichier.name not in decrits:
-        anomalies.append({"fichier": fichier.name, "test": "metadonnees absentes",
-                          "date": "", "detail": ""})
-
-    d = pd.read_csv(fichier, usecols=["date"])
-    for x in sorted(set(d.date.str[-6:]) - DECALAGES):
-        anomalies.append({"fichier": fichier.name, "test": "decalage horaire inattendu",
-                          "date": "", "detail": x})
-
-    debut = d.date.iloc[0][:10]
-    declaree = attendu.get(fichier.name)
-    if declaree and declaree != debut:
-        anomalies.append({"fichier": fichier.name, "test": "premiere transaction discordante",
-                          "date": debut, "detail": f"declaree {declaree}"})
-
-ancien = pd.read_csv(CONTROLE)
-ancien = ancien[~ancien.test.isin(TESTS_18)]
-controle = pd.concat([ancien, pd.DataFrame(anomalies)], ignore_index=True)
-controle.to_csv(CONTROLE, index=False, encoding="utf-8")
-
-print(len(anomalies), "anomalies |", len(controle), "au total")
-if anomalies:
-    print(pd.DataFrame(anomalies).test.value_counts().to_string())
-
-CELLULE 14, code
-TESTS_19 = ["fin de serie anticipee", "denomination divergente"]
-
-import re
-
-def normaliser(nom):
-    n = str(nom).lower()
-    for mot in [" incorporated", " corporation", " companies", " company", " holdings",
-                " group", " inc", " corp", " plc", " ltd", " the", " co",
-                " & ", " and ", ".", ",", "'", "-"]:
-        n = n.replace(mot, " ")
-    return re.sub(r"\s+", " ", n).strip()
-
-calendrier = pd.read_csv(RACINE / "data" / "raw" / "calendrier_bourse.csv")["date"].astype(str)
-derniere = calendrier.max()
-
-meta = pd.read_csv(RACINE / "data" / "raw" / "metadonnees_titres.csv")
-composants = pd.read_csv(RACINE / "data" / "raw" / "sp500_constituents.csv", dtype=str)
-nom_indice = dict(zip(composants.Symbol.str.replace(".", "-", regex=False), composants.Security))
-
-anomalies = []
-
-for fichier in fichiers:
-    fin = pd.read_csv(fichier, usecols=["date"]).date.iloc[-1][:10]
-    if fin < derniere:
-        anomalies.append({"fichier": fichier.name, "test": "fin de serie anticipee",
-                          "date": fin, "detail": f"derniere seance {derniere}"})
-
-for r in meta.itertuples():
-    reference = nom_indice.get(r.symbole)
-    if reference is None:
-        continue
-    a, b = normaliser(r.nom), normaliser(reference)
-    if not (a.startswith(b[:8]) or b.startswith(a[:8])):
-        anomalies.append({"fichier": r.fichier, "test": "denomination divergente",
-                          "date": "", "detail": f"{r.nom} contre {reference}"})
-
-ancien = pd.read_csv(CONTROLE)
-ancien = ancien[~ancien.test.isin(TESTS_19)]
-controle = pd.concat([ancien, pd.DataFrame(anomalies)], ignore_index=True)
-controle.to_csv(CONTROLE, index=False, encoding="utf-8")
-
-print(len(anomalies), "anomalies |", len(controle), "au total")
-if anomalies:
-    print(pd.DataFrame(anomalies).test.value_counts().to_string())
-    print()
-    print(pd.DataFrame(anomalies)[["fichier", "detail"]].to_string(index=False))
-
-CELLULE 15, code
-TESTS_19B = ["seance sans transaction", "prix fige"]
-
-anomalies = []
-resume = []
-
-for fichier in sorted(DOSSIER.glob("*.csv")):
-    d = pd.read_csv(fichier, usecols=["date", "Open", "High", "Low", "Close", "Volume"])
-    d["j"] = d["date"].str[:10]
-
-    sans_volume = d.Volume == 0
-    fige = (sans_volume
-            & (d.Open == d.High) & (d.High == d.Low) & (d.Low == d.Close)
-            & (d.Close == d.Close.shift()))
-
-    if sans_volume.any():
-        resume.append({"symbole": fichier.stem, "lignes": len(d),
-                       "sans_volume": int(sans_volume.sum()), "fige": int(fige.sum()),
-                       "part": int(sans_volume.sum()) / len(d)})
-
-    for i in d.index[sans_volume & ~fige]:
-        anomalies.append({"fichier": fichier.name, "test": "seance sans transaction",
-                          "date": d.j[i], "detail": ""})
-    for i in d.index[fige]:
-        anomalies.append({"fichier": fichier.name, "test": "prix fige",
-                          "date": d.j[i], "detail": f"{d.Close[i]:.4f}"})
-
-resume = pd.DataFrame(resume).sort_values("sans_volume", ascending=False)
-
-ancien = pd.read_csv(CONTROLE)
-ancien = ancien[~ancien.test.isin(TESTS_19B)]
-controle = pd.concat([ancien, pd.DataFrame(anomalies)], ignore_index=True)
-controle.to_csv(CONTROLE, index=False, encoding="utf-8")
-
-print(len(anomalies), "anomalies |", len(controle), "au total")
-print(pd.DataFrame(anomalies).test.value_counts().to_string())
-print()
-print(resume.head(12).to_string(index=False, formatters={"part": "{:.1%}".format}))
-
-CELLULE 16, code
-import yfinance as yf
-
-SYMBOLE = "CMS"
-CIBLE = DOSSIER / f"{SYMBOLE}.csv"
-
-if CIBLE.exists():
-    raise FileExistsError(f"{CIBLE} existe deja, collecte refusee")
-
-h = yf.Ticker(SYMBOLE).history(period="max", auto_adjust=False, actions=True)
-if h.empty:
-    raise ValueError(f"aucune donnee pour {SYMBOLE}")
-
-h.index.name = "date"
-h["symbole"] = SYMBOLE
-h = h[["Open", "High", "Low", "Close", "Adj Close", "Volume",
-       "Dividends", "Stock Splits", "symbole"]]
-h.to_csv(CIBLE, encoding="utf-8")
-
-print(len(h), "lignes ecrites dans", CIBLE)
-print(h.index[0].date(), "->", h.index[-1].date())
-
-CELLULE 17, code
-
-
-CELLULE 18, code
-
-
-CELLULE 19, code
-
-
-CELLULE 20, code
-
-
-CELLULE 21, code
+resume = pd.read_csv(SORTIE / "resume_controle_prix.csv")
+print(resume.to_string(index=False))
+print(pd.read_csv(SORTIE / "controle_divisions_sec.csv").to_string(index=False))
```

</details>

### `src/export_univers_excel.py`

Rattacher l’export au registre courant et retirer la classe A du nom générique de l’entreprise à plusieurs classes.

Avant : `3602890e5d28af5b0ad96cdc9f9664533fe0005cd902ce0abb1bc8529b1e52ad`. Après : `8a6cce29b762e6f027d63dbe02d67409c4c5fed6723152b0455a2447ddeef044`.

Lignes physiques : 100 avant, 106 après.

Les repères `@@` indiquent les lignes avant et après. `-` contient le texte retiré, `+` le texte retenu.

<details>
<summary>Contenu exact des changements</summary>

```diff
--- src/export_univers_excel.py avant
+++ src/export_univers_excel.py après
@@ -8,4 +8,5 @@
 from pathlib import Path
 import argparse
+import hashlib
 import json
 import os
@@ -32,4 +33,6 @@
     t = univers.merge(infos, on="cik", how="left", validate="one_to_one")
     t = t.merge(corro.reindex(columns=colonnes_comptes), on="cik", how="left", validate="one_to_one")
+    plusieurs = t.symboles.str.contains("|", regex=False)
+    t.loc[plusieurs, "nom"] = t.loc[plusieurs, "nom"].str.replace(r"\s*\(Class [A-Z]\)$", "", regex=True)
     t["ticker"] = t.symboles.str.split("|", regex=False).str[0]
     dates = lire("data/raw/premieres_cotations.csv")
@@ -75,7 +78,10 @@
         tri = t.sort_values(cles, ascending=nom != "Par anciennete", na_position="last")
         sheets[nom] = json.loads(tri.to_json(orient="values", force_ascii=False))
+    registre = RACINE / "data/review/decisions_selection.csv"
+    sha_registre = hashlib.sha256(registre.read_bytes()).hexdigest()
     return {"columns": list(t.columns), "sheets": sheets,
             "summary": json.loads((RACINE / "data/processed/etat_projet.json").read_text(encoding="utf-8")),
-            "snapshot": "2026-09-05", "input_workbook": str(RACINE / "univers_82.xlsx")}
+            "snapshot": "registre " + sha_registre[:12], "registre_sha256": sha_registre,
+            "input_workbook": str(RACINE / "univers_82.xlsx")}
```

</details>

### `src/portefeuille.py`

Appliquer les dates d’entrée, les entreprises par CIK, la valorisation des trous et les frais réellement exécutés ; refuser les états invalides et la réinitialisation après perte totale.

Avant : `d045efe0a43f25fb45d576c681af18450e0c99ab0deecf3edc677f5be309b9b9`. Après : `84a7b06ce4da16d7c376011b1ef2cea8204e099622f064c0dd308387f42854c3`.

Lignes physiques : 116 avant, 197 après.

Les repères `@@` indiquent les lignes avant et après. `-` contient le texte retiré, `+` le texte retenu.

<details>
<summary>Contenu exact des changements</summary>

```diff
--- src/portefeuille.py avant
+++ src/portefeuille.py après
@@ -1,8 +1,3 @@
-"""Construction des portefeuilles equiponderes de l'etude.
-
-Les regles appliquees ici sont fixees dans research/portefeuilles.md et
-research/plan_projet.md, phase 3. Elles ne doivent pas etre modifiees sans
-que la modification soit datee et motivee dans ces documents.
-"""
+"""Moteur en montants. Les décisions sont datées dans research/portefeuilles.md."""
 import numpy as np
 import pandas as pd
@@ -11,106 +6,192 @@
 
 
-def rendements_et_dividendes(prix):
-    """Rendement de prix et dividende rapporte au cours de la veille.
+def preparer_prix(prix, indice=False):
+    """Sépare observation et valorisation au dernier cours connu.
 
-    prix : DataFrame indexe par date, colonnes Close, Volume, Dividends.
+    Les cours Yahoo sont déjà retraités des divisions : Stock Splits ne
+    multiplie jamais une seconde fois les montants. Une valeur portée pendant
+    un trou n'est pas une observation de marché sans réserve pour le risque.
+    """
+    if not prix.index.is_unique or not prix.index.is_monotonic_increasing:
+        raise ValueError("Dates dupliquées ou non ordonnées.")
+    close, div = prix.Close.astype(float), prix.Dividends.astype(float)
+    if np.isinf(close).any() or close.dropna().le(0).any():
+        raise ValueError("Prix non fini, nul ou négatif.")
+    if np.isinf(div).any() or div.dropna().lt(0).any():
+        raise ValueError("Dividende négatif ou non fini.")
+    suspect = pd.Series(False, index=prix.index)
+    if not indice:
+        volume = prix.Volume.astype(float)
+        if volume.isna().any() or volume.lt(0).any() or np.isinf(volume).any():
+            raise ValueError("Volume absent, négatif ou non fini.")
+        avant = ~volume.gt(0).cummax()
+        if {"Open", "High", "Low"} <= set(prix.columns):
+            plat = prix[["Open", "High", "Low"]].eq(close, axis=0).all(axis=1)
+            suspect = volume.eq(0) & (avant | (plat & close.eq(close.shift())))
+        else:
+            suspect = volume.eq(0)
+    observe = close.mask(suspect)
+    valeur = observe.ffill()
+    if (div.isna() & valeur.notna()).any():
+        raise ValueError("Dividende absent pendant l'historique valorisé.")
+    return pd.DataFrame({
+        "rendement_observe": observe.pct_change(fill_method=None),
+        "rendement_valorisation": valeur.pct_change(fill_method=None),
+        "dividende": div / valeur.shift(), "disponible": observe.notna(),
+        "cours_porte": observe.isna() & valeur.notna(),
+        "volume_nul": False if indice else prix.Volume.eq(0)}, index=prix.index)
 
-    Une seance a volume nul n'est pas une seance : c'est une ligne de
-    remplissage servie par la source faute de cotation reelle. Son cours est
-    traite comme inconnu, ce qui annule le rendement du jour et celui du
-    lendemain, lequel a besoin de la veille.
-    """
-    cloture = prix.Close.astype("float64").mask(prix.Volume == 0)
-    return cloture.pct_change(fill_method=None), prix.Dividends / cloture.shift()
+
+def rendements_et_dividendes(prix, indice=False):
+    """Rendement observé et détachement en espèces rapporté au cours précédent."""
+    p = preparer_prix(prix, indice)
+    return p.rendement_observe, p.dividende
 
 
 def poids_cibles(membres, presents):
-    """Poids d'equiponderation par titre, a une date.
-
-    membres : DataFrame de colonnes entreprise et titre.
-    presents : titres cotes ce jour la.
-
-    Chaque entreprise presente pese 1/n. Une entreprise cotee sous plusieurs
-    classes d'actions partage ce poids entre elles a parts egales : elle ne
-    pese pas davantage parce qu'elle a deux lignes.
-    """
+    """Équipondère les entreprises puis partage entre classes disponibles."""
+    if membres.titre.duplicated().any():
+        raise ValueError("Titre dupliqué dans l'appartenance.")
+    cle = "cik" if "cik" in membres else "entreprise"
+    if membres[cle].isna().any():
+        raise ValueError("Identité d'entreprise absente.")
     vivants = membres[membres.titre.isin(presents)]
     if vivants.empty:
         return {}
-    n = vivants.entreprise.nunique()
-    classes = vivants.groupby("entreprise").titre.transform("size")
+    n = vivants[cle].nunique()
+    classes = vivants.groupby(cle).titre.transform("size")
     return {r.titre: 1.0 / (n * k) for r, k in zip(vivants.itertuples(), classes)}
 
 
+def _executer(montant, vise, cash_vise, cout):
+    """Finance les frais sur les achats et ventes réellement exécutés.
+
+    La cible complète, trésorerie comprise, est réduite proportionnellement.
+    Je résous frais = coût * somme(abs(cible après frais - positions avant)).
+    """
+    valeur = float(vise.sum() + cash_vise.sum())
+    if valeur <= 0:
+        return vise.copy(), cash_vise.copy(), 0.0, 0.0
+    if np.array_equal(montant, vise):
+        return vise.copy(), cash_vise.copy(), 0.0, 0.0
+    bas, haut = 0.0, valeur
+    for _ in range(55):
+        frais = (bas + haut) / 2
+        facture = cout * np.abs(vise * (1 - frais / valeur) - montant).sum()
+        if frais < facture:
+            bas = frais
+        else:
+            haut = frais
+    frais = (bas + haut) / 2 if cout else 0.0
+    nouveau = vise * (1 - frais / valeur)
+    cash = cash_vise * (1 - frais / valeur)
+    return nouveau, cash, float(frais), float(np.abs(nouveau - montant).sum())
+
+
 def simuler(rendements, detachements, titres, cibles, dates, jours_reeq,
-            reequilibrer, cout=COUT, fins_de_mois=frozenset()):
-    """Simule un portefeuille et renvoie (valeurs, rotation moyenne, photos des poids).
+            reequilibrer, cout=COUT, fins_de_mois=frozenset(), *,
+            disponibilite=None, entreprises=None, journal=None):
+    """Renvoie valeurs, rotation annualisée et photographies des poids.
 
-    Le suivi porte sur des montants et non sur des poids : la derive entre deux
-    reequilibrages est alors automatique et aucune renormalisation n'intervient.
-    Le dividende verse par un titre alimente une tresorerie attachee a ce titre,
-    qui ne rapporte rien jusqu'a son reinvestissement en janvier.
-
-    cibles : DataFrame indexe par date de reequilibrage, colonnes = titres.
+    Une cible hors janvier est un événement d'entrée, jamais un rééquilibrage
+    général. L'achat est à la clôture ; le nouveau titre ne rapporte que dès
+    la séance suivante. La mise initiale est une base nette de sa constitution.
+    Aucun apport n'est autorisé ensuite, même après une perte totale.
     """
-    r = rendements[titres].astype("float64").to_numpy()
-    d = detachements[titres].astype("float64").fillna(0).to_numpy()
-    cote = ~np.isnan(r)
-
-    montant = np.zeros(len(titres))
-    tresorerie = np.zeros(len(titres))
+    dates = pd.Index(dates)
+    if (not len(dates) or not dates.is_unique or not dates.is_monotonic_increasing
+            or len(set(titres)) != len(titres) or not titres):
+        raise ValueError("Dates ou liste de titres invalides.")
+    if not np.isfinite(cout) or not 0 <= cout < 1:
+        raise ValueError("Coût invalide.")
+    for df in (rendements, detachements):
+        if not df.index.equals(dates) or not df.columns.is_unique:
+            raise ValueError("Dates désalignées ou colonnes dupliquées.")
+    if not cibles.index.is_unique or not set(cibles.index) <= set(dates):
+        raise ValueError("Dates de cibles invalides.")
+    if not set(titres) <= set(cibles.columns):
+        raise ValueError("Cibles incomplètes.")
+    if dates[0] not in cibles.index or not set(jours_reeq) <= set(cibles.index):
+        raise ValueError("Cible initiale ou annuelle absente.")
+    r = rendements[titres].to_numpy(dtype=float)
+    d = detachements[titres].to_numpy(dtype=float)
+    if np.isinf(r).any() or np.isinf(d).any() or (r < -1).any() or (d < 0).any():
+        raise ValueError("Rendement ou détachement invalide.")
+    if disponibilite is None:
+        cote = ~np.isnan(r)
+    else:
+        if not disponibilite.index.equals(dates) or disponibilite[titres].isna().any().any():
+            raise ValueError("Disponibilités désalignées ou inconnues.")
+        if not all(pd.api.types.is_bool_dtype(disponibilite[t].dtype) for t in titres):
+            raise ValueError("Une disponibilité doit être un booléen, pas un texte ou un nombre.")
+        cote = disponibilite[titres].to_numpy(dtype=bool)
+    wc = cibles.loc[:, titres].to_numpy(dtype=float)
+    if not np.isfinite(wc).all() or (wc < 0).any() or not np.allclose(wc.sum(axis=1), 1, rtol=0, atol=1e-12):
+        raise ValueError("Poids cibles non finis, négatifs ou de somme différente de un.")
+    groupes = np.array([entreprises[t] if entreprises is not None else t for t in titres])
+    montant, tresorerie = np.zeros(len(titres)), np.zeros(len(titres))
+    deja_entre = np.zeros(len(titres), dtype=bool)
     valeurs, rotations, photos = [], [], []
-
     for i, jour in enumerate(dates):
-        vivant = cote[i]
-
+        precedent = float(montant.sum() + tresorerie.sum())
+        poids_avant = montant / precedent if precedent else montant.copy()
         if i > 0:
-            tresorerie += montant * np.where(vivant, d[i], 0.0)
-            montant = montant * (1 + np.where(vivant, np.nan_to_num(r[i]), 0.0))
-
-        valeur = montant.sum() + tresorerie.sum()
-
-        if jour in jours_reeq:
-            w = np.nan_to_num(cibles.loc[jour].to_numpy(dtype=float))
-
-            if valeur == 0:
+            detenus = montant > 0
+            if (detenus & (~np.isfinite(r[i]) | ~np.isfinite(d[i]))).any():
+                raise ValueError(f"Rendement ou dividende inconnu sur une position détenue : {jour}")
+            tresorerie += montant * np.nan_to_num(d[i], nan=0)
+            montant *= 1 + np.nan_to_num(r[i], nan=0)
+        avant_operation = float(montant.sum() + tresorerie.sum())
+        frais = echange = 0.0
+        if jour in cibles.index:
+            w = cibles.loc[jour, titres].to_numpy(dtype=float)
+            if ((w > 0) & ~cote[i]).any():
+                raise ValueError(f"Cible sur un titre sans cotation : {jour}")
+            if i == 0:
                 montant = w.copy()
-                tresorerie[:] = 0.0
-
-            elif reequilibrer:
-                vise = valeur * w
-                echange = np.abs(vise - montant).sum()
-                rotations.append(echange / valeur)
-                frais = cout * echange
-                montant = vise * (1 - frais / valeur)
-                tresorerie[:] = 0.0
-
-            else:
-                montant = montant + tresorerie
-                tresorerie[:] = 0.0
-                entrants = vivant & (montant == 0) & (w > 0)
-                if entrants.any():
-                    presents = int((montant > 0).sum())
-                    nouveaux = int(entrants.sum())
-                    avant = montant.sum()
-                    # l'entrant prend 1/(n+k) du total ; les titres deja detenus
-                    # sont reduits en proportion pour financer son entree, de
-                    # sorte que la valeur du portefeuille ne bouge pas.
-                    montant *= presents / (presents + nouveaux)
-                    montant[entrants] = avant / (presents + nouveaux)
-                    echange = avant * nouveaux / (presents + nouveaux)
-                    rotations.append(echange / avant)
-                    frais = cout * echange
-                    montant *= (avant - frais) / montant.sum()
-
-            valeur = montant.sum() + tresorerie.sum()
-
+                deja_entre = w > 0
+            elif avant_operation > 0:
+                annuel = jour in jours_reeq
+                nouveaux = (w > 0) & ~deja_entre
+                vise, cash_vise = montant.copy(), tresorerie.copy()
+                if annuel and reequilibrer:
+                    vise, cash_vise = avant_operation * w, np.zeros(len(titres))
+                else:
+                    if annuel:
+                        vise += cash_vise
+                        cash_vise[:] = 0
+                    if nouveaux.any():
+                        anciens = set(groupes[(montant + tresorerie) > 0])
+                        nouveaux_groupes = set(groupes[nouveaux]) - anciens
+                        n, k = len(anciens), len(nouveaux_groupes)
+                        vise *= n / (n + k)
+                        cash_vise *= n / (n + k)
+                        for groupe in sorted(set(groupes[nouveaux])):
+                            selection = (groupes == groupe) & (deja_entre | nouveaux)
+                            if groupe in nouveaux_groupes:
+                                vise[selection] = avant_operation / (n + k) / selection.sum()
+                            else:
+                                # Une deuxième classe ne crée pas une entreprise.
+                                vise[selection] = vise[selection].sum() / selection.sum()
+                montant, tresorerie, frais, echange = _executer(montant, vise, cash_vise, cout)
+                rotations.append(echange / avant_operation)
+                deja_entre |= nouveaux
+        valeur = float(montant.sum() + tresorerie.sum())
+        if not np.isfinite(valeur) or (montant < -1e-13).any() or (tresorerie < -1e-13).any():
+            raise ValueError(f"État de portefeuille invalide : {jour}")
+        if i and abs(valeur + frais - avant_operation) > 1e-10 * max(1, avant_operation):
+            raise ArithmeticError(f"L'opération crée ou détruit de la valeur : {jour}")
+        if journal is not None:
+            attendu = float(np.dot(poids_avant, np.nan_to_num(r[i] + d[i], nan=0))) if i else 0.0
+            journal.append({"date": jour, "valeur_avant": precedent,
+                            "valeur_avant_operation": avant_operation, "valeur": valeur,
+                            "frais": frais, "echange": echange,
+                            "rendement_attendu_avant_frais": attendu,
+                            "tresorerie": float(tresorerie.sum())})
         valeurs.append(valeur)
-
         if jour in fins_de_mois and valeur > 0:
             photo = pd.Series(montant / valeur, index=titres, name=jour)
             photo["_tresorerie"] = tresorerie.sum() / valeur
             photos.append(photo)
-
-    rotation = float(np.mean(rotations)) if rotations else 0.0
-    return pd.Series(valeurs, index=dates), rotation, pd.DataFrame(photos)
+    annees = max((len(dates) - 1) / 252, 1 / 252)
+    return pd.Series(valeurs, index=dates), float(sum(rotations) / annees), pd.DataFrame(photos)
```

</details>

### `src/run_pipeline.py`

Limiter les dépendances de l’étape 1 à ses propres traitements, puis régénérer son manifeste sans modifier les résultats économiques.

Avant : `5c160865c06297d8f339c9e1e3ab010dc56648031bb15d0bb95e97960cbd05cb`. Après : `db86ed6fa7dd8bc62d176beafd01931729a87a8d3f921c4cf3754f427ea627a2`.

Lignes physiques : 221 avant, 222 après.

Les repères `@@` indiquent les lignes avant et après. `-` contient le texte retiré, `+` le texte retenu.

<details>
<summary>Contenu exact des changements</summary>

```diff
--- src/run_pipeline.py avant
+++ src/run_pipeline.py après
@@ -197,6 +197,7 @@
         inputs += sorted((RACINE / "data/review").glob("decisions*.csv"))
         inputs += sorted((RACINE / "data/review").glob("comptabilite_exceptions*.json"))
-        inputs += [p for p in sorted((RACINE / "src").glob("*.py"))
-                   if not p.name.startswith("export_")]
+        # L'étape 1 dépend de ses traitements, pas des moteurs de l'étape 2.
+        inputs += [RACINE / "src" / nom for nom in (*ETAPES, "run_pipeline.py")]
+        inputs += [RACINE / "requirements.txt"]
         inputs += [RACINE / "data/raw/filings_manifest.json"]
         outputs = [PROCESSED / nom for nom in SORTIES]
```

</details>

### `tests/test_audit_portefeuilles.py`

Ajouter les contre-exemples sur entrées, coûts, classes, dividendes, trous, données invalides et perte totale.

Avant : fichier absent. Après : `432e35e3323bbd20062849fc15cd60791d6dc16de8cbe24954de33093bbb8608`.

Lignes physiques : 0 avant, 135 après.

Les repères `@@` indiquent les lignes avant et après. `-` contient le texte retiré, `+` le texte retenu.

<details>
<summary>Contenu exact des changements</summary>

```diff
--- tests/test_audit_portefeuilles.py avant
+++ tests/test_audit_portefeuilles.py après
@@ -0,0 +1,135 @@
+"""Contre-exemples de l'audit du 8 septembre, calculables indépendamment du moteur."""
+import unittest
+import numpy as np
+import pandas as pd
+from src.portefeuille import preparer_prix, simuler, poids_cibles
+
+
+class AuditMoteurTests(unittest.TestCase):
+    def run_case(self, r, w, *, reeq=False, cout=0, d=None, entreprises=None, annuel=None):
+        r = pd.DataFrame(r)
+        r.index = [f"2020-01-{i+1:02d}" for i in range(len(r))]
+        d = pd.DataFrame(0., index=r.index, columns=r.columns) if d is None else pd.DataFrame(d, index=r.index)
+        c = pd.DataFrame(w, columns=r.columns)
+        c.index = r.index[[0, len(r)-1]] if len(c)==2 else r.index[:1]
+        journal=[]
+        result = simuler(r,d,list(r),c,r.index,set(annuel or [r.index[0]]),reeq,cout,
+                         fins_de_mois=set(r.index),entreprises=entreprises,journal=journal)
+        return (*result,journal)
+
+    def test_entree_hors_janvier_financee_dans_les_deux_versions(self):
+        for reeq in [False,True]:
+            v,_,w,_=self.run_case({'A':[0,0],'B':[np.nan,0]},[[1,0],[.5,.5]],reeq=reeq)
+            self.assertAlmostEqual(v.iloc[-1],1)
+            self.assertAlmostEqual(w.B.iloc[-1],.5)
+
+    def test_achats_et_ventes_factures(self):
+        v,_,_,j=self.run_case({'A':[0,0],'B':[np.nan,0]},[[1,0],[.5,.5]],cout=.001)
+        self.assertAlmostEqual(v.iloc[-1],.999,places=12)
+        self.assertAlmostEqual(j[-1]['echange'],1,places=12)
+        self.assertAlmostEqual(j[-1]['frais'],.001,places=12)
+
+    def test_frais_reinvestissement_dividende_conserve(self):
+        v,_,_,j=self.run_case({'A':[0,-.1]},[[1],[1]],d={'A':[0,.1]},cout=.001,
+                              annuel=['2020-01-01','2020-01-02'])
+        self.assertAlmostEqual(j[-1]['frais'],.0001/1.001,places=12)
+        self.assertAlmostEqual(v.iloc[-1],1-.0001/1.001,places=12)
+
+    def test_faillite_ne_recree_pas_de_mise(self):
+        v,_,_,_=self.run_case({'A':[0,-1,0]},[[1],[1]],annuel=['2020-01-01','2020-01-03'])
+        self.assertEqual(v.tolist(),[1.,0.,0.])
+
+    def test_deuxieme_classe_ne_dilue_pas_une_autre_entreprise(self):
+        v,_,w,_=self.run_case({'A1':[0,0],'B':[0,0],'A2':[np.nan,0]},
+            [[.5,.5,0],[.25,.5,.25]],entreprises={'A1':'1','A2':'1','B':'2'})
+        self.assertAlmostEqual(w.B.iloc[-1],.5)
+        self.assertAlmostEqual(w.A1.iloc[-1]+w.A2.iloc[-1],.5)
+        self.assertAlmostEqual(v.iloc[-1],1)
+
+    def test_nouvelle_entreprise_comptee_par_cik(self):
+        _,_,w,_=self.run_case({'A1':[0,0],'A2':[0,0],'B':[0,0],'C':[np.nan,0]},
+            [[.25,.25,.5,0],[1/6,1/6,1/3,1/3]],entreprises={'A1':'1','A2':'1','B':'2','C':'3'})
+        self.assertAlmostEqual(w.C.iloc[-1],1/3)
+
+    def test_dividende_sans_baisse_du_prix_est_possible(self):
+        v,_,_,_=self.run_case({'A':[0,0]},[[1]],d={'A':[0,.1]})
+        self.assertAlmostEqual(v.iloc[-1],1.1)
+
+    def test_manquant_sur_position_refuse(self):
+        with self.assertRaisesRegex(ValueError,'inconnu'):
+            self.run_case({'A':[0,np.nan]},[[1]])
+
+    def test_infini_et_rendement_inferieur_a_moins_un_refuses(self):
+        for valeur in [np.inf,-np.inf,-1.01]:
+            with self.assertRaises(ValueError):
+                self.run_case({'A':[0,valeur]},[[1]])
+
+    def test_cibles_invalides_refusees(self):
+        for w in [[np.nan],[np.inf],[-1],[.9],[1.1]]:
+            with self.assertRaises(ValueError):
+                self.run_case({'A':[0,0]},[w])
+
+    def test_dates_desalignees_refusees(self):
+        r=pd.DataFrame({'A':[0,0]},index=['2020-01-01','2020-01-02'])
+        with self.assertRaises(ValueError):
+            simuler(r,r.iloc[::-1],['A'],pd.DataFrame({'A':[1]},index=r.index[:1]),r.index,{r.index[0]},False)
+
+    def test_cibles_reordonnees_par_symbole(self):
+        r=pd.DataFrame({'A':[0,.2],'B':[0,0]},index=['2020-01-01','2020-01-02'])
+        w=pd.DataFrame({'B':[.2],'A':[.8]},index=r.index[:1])
+        v,_,_=simuler(r,r*0,['A','B'],w,r.index,{r.index[0]},False,cout=0)
+        self.assertAlmostEqual(v.iloc[-1],1.16)
+
+    def test_encadrement_inclut_cash_dividendes_et_frais(self):
+        v,_,_,j=self.run_case({'A':[0,-.1,0],'B':[0,0,.2]},[[.5,.5],[.5,.5]],
+             d={'A':[0,.1,0],'B':[0,0,0]},cout=.001,reeq=True,
+             annuel=['2020-01-01','2020-01-03'])
+        for i in range(1,len(v)):
+            actual=v.iloc[i]/v.iloc[i-1]-1
+            self.assertAlmostEqual(actual,j[i]['rendement_attendu_avant_frais']-j[i]['frais']/j[i]['valeur_avant'])
+
+
+class AuditPrixTests(unittest.TestCase):
+    def prix(self,close,volume=None):
+        return pd.DataFrame({'Close':close,'Open':close,'High':close,'Low':close,
+            'Volume':volume if volume is not None else [100]*len(close),'Dividends':[0]*len(close)})
+
+    def test_reprise_recupere_tout_le_mouvement(self):
+        p=preparer_prix(self.prix([100,np.nan,121,133.1]))
+        self.assertTrue(p.rendement_observe.iloc[1:3].isna().all())
+        self.assertAlmostEqual((1+p.rendement_valorisation.iloc[1:]).prod(),1.331)
+        self.assertEqual(p.cours_porte.tolist(),[False,True,False,False])
+
+    def test_pas_de_prolongement_avant_le_premier_cours(self):
+        p=preparer_prix(self.prix([np.nan,np.nan,100,110]))
+        self.assertTrue(p.rendement_valorisation.iloc[:3].isna().all())
+
+    def test_volume_nul_variable_ne_signifie_pas_prix_fabrique(self):
+        p=preparer_prix(self.prix([100,101,102],[100,0,100]))
+        self.assertTrue(p.disponible.all())
+
+    def test_prix_fige_suspect_est_porte_puis_raccorde(self):
+        p=preparer_prix(self.prix([100,100,110],[100,0,100]))
+        self.assertFalse(p.disponible.iloc[1])
+        self.assertAlmostEqual(p.rendement_valorisation.iloc[2],.1)
+
+    def test_indice_volume_zero_reste_entier(self):
+        p=preparer_prix(self.prix([100,101,102],[0,0,0]),indice=True)
+        self.assertTrue(p.disponible.all())
+
+    def test_division_deja_retraitee_n_est_pas_appliquee_deux_fois(self):
+        prix=self.prix([50,51,52]);prix['Stock Splits']=[0,2,0]
+        p=preparer_prix(prix)
+        self.assertAlmostEqual((1+p.rendement_valorisation.dropna()).prod(),52/50)
+
+    def test_dividende_absent_apres_debut_refuse(self):
+        p=self.prix([100,101]);p.loc[1,'Dividends']=np.nan
+        with self.assertRaises(ValueError):preparer_prix(p)
+
+    def test_cik_prioritaire_sur_nom(self):
+        membres=pd.DataFrame({'titre':['A1','A2','B'],'entreprise':['ancien nom','nouveau nom','autre'],'cik':['1','1','2']})
+        w=poids_cibles(membres,list(membres.titre))
+        self.assertEqual(w,{'A1':.25,'A2':.25,'B':.5})
+
+
+if __name__=='__main__':unittest.main()
```

</details>

### `tests/test_pipeline_portefeuilles.py`

Contrôler des fichiers invalides, un manifeste vide ou altéré et un oracle en nombres de parts sur 80 scénarios de gestion.

Avant : fichier absent. Après : `f1f545e3b34198a61c7db365fe89e30cb63435692c67f56a3a85d7c0cf514f0a`.

Lignes physiques : 0 avant, 115 après.

Les repères `@@` indiquent les lignes avant et après. `-` contient le texte retiré, `+` le texte retenu.

<details>
<summary>Contenu exact des changements</summary>

```diff
--- tests/test_pipeline_portefeuilles.py avant
+++ tests/test_pipeline_portefeuilles.py après
@@ -0,0 +1,115 @@
+"""Échecs de fichier et oracle de compte de parts, indépendants du replay réel."""
+import json
+from pathlib import Path
+import tempfile
+import unittest
+from unittest.mock import patch
+
+import numpy as np
+import pandas as pd
+
+from src.controle_prix import verifier_structure_prix
+from src.construire_portefeuilles import appartenance, verifier, verifier_bruts
+from src.portefeuille import preparer_prix, simuler
+
+
+class ContratsDonneesTests(unittest.TestCase):
+    def prix(self):
+        return pd.DataFrame({'date':['2020-01-02','2020-01-03'],
+            'Open':[100.,101.], 'High':[100.,101.], 'Low':[100.,101.],
+            'Close':[100.,101.], 'Adj Close':[100.,101.],
+            'Volume':[100.,100.], 'Dividends':[0.,0.], 'Stock Splits':[0.,0.]})
+
+    def test_prix_infinis_et_evenements_inconnus_refuses(self):
+        for col,val in [('Open',np.inf),('Adj Close',np.inf),('Dividends',np.nan),
+                        ('Stock Splits',-2.),('Volume',np.nan),('Close','texte')]:
+            with self.subTest(col=col,val=val):
+                p=self.prix();p[col]=p[col].astype(object);p.loc[1,col]=val
+                with self.assertRaises((ValueError,TypeError)):
+                    verifier_structure_prix(p,'essai.csv')
+
+    def test_absence_prix_reste_identifiable_sans_faux_zero(self):
+        p=self.prix();p.loc[1,['Open','High','Low','Close','Adj Close']]=np.nan
+        verifier_structure_prix(p,'essai.csv')
+        prepare=preparer_prix(p)
+        self.assertTrue(prepare.cours_porte.iloc[1])
+        self.assertTrue(np.isnan(prepare.rendement_observe.iloc[1]))
+
+    def test_fichier_vide_ou_dates_impossibles_refuses(self):
+        with self.assertRaises(ValueError):verifier_structure_prix(self.prix().iloc[:0],'vide.csv')
+        p=self.prix();p.loc[1,'date']='2020-02-31'
+        with self.assertRaises(ValueError):verifier_structure_prix(p,'date.csv')
+
+    def test_disponibilite_texte_ne_devient_pas_vrai(self):
+        r=pd.DataFrame({'A':[0.,.1]},index=['2020-01-02','2020-01-03'])
+        c=pd.DataFrame({'A':[1.]},index=r.index[:1])
+        dispo=pd.DataFrame({'A':['False','False']},index=r.index)
+        with self.assertRaisesRegex(ValueError,'booléen'):
+            simuler(r,r*0,['A'],c,r.index,{r.index[0]},False,disponibilite=dispo)
+
+    def test_manifeste_vide_ne_vaut_pas_validation(self):
+        with tempfile.TemporaryDirectory() as tmp:
+            path=Path(tmp)
+            (path/'pipeline_portefeuilles.json').write_text(json.dumps(
+                {'statut':'termine','entrees_sha256':{},'sorties_sha256':{}}))
+            with patch('src.construire_portefeuilles.verifier_bruts',return_value=[]):
+                with self.assertRaisesRegex(ValueError,'incomplet'):verifier(path,path)
+
+    def test_brut_modifie_refuse_avant_calcul(self):
+        with tempfile.TemporaryDirectory() as tmp:
+            root=Path(tmp);raw=root/'data/raw';(raw/'prix').mkdir(parents=True);(raw/'benchmarks').mkdir()
+            (raw/'prix/A.csv').write_text('modification')
+            (raw/'prix_manifest.json').write_text(json.dumps({'prix':[{'fichier':'A.csv','sha256':'0'*64}], 'benchmarks':[]}))
+            with self.assertRaisesRegex(ValueError,'Empreinte'):verifier_bruts(root)
+
+    def test_registre_hors_regle_refuse(self):
+        d=pd.DataFrame([{'verdict':'ENTRE','cik':'1','maturite_exposition':'inconnue',
+                         'canal':'vend','secteur':'Information Technology','symboles':'A','nom':'A'}])
+        with self.assertRaisesRegex(ValueError,'Maturité'):appartenance(d)
+        d.loc[0,'maturite_exposition']='etablie';d.loc[0,'canal']='autre'
+        with self.assertRaisesRegex(ValueError,'Canal'):appartenance(d)
+
+
+class OraclePartsTests(unittest.TestCase):
+    def test_comptes_de_parts_aleatoires_entree_dividendes_et_frais(self):
+        """Deux titres au départ, un entrant, puis janvier : 40 scénarios fixés.
+
+        L'oracle tient des quantités de parts et des créances nominales. Les
+        frais sont obtenus par point fixe, pas par le solveur du moteur.
+        """
+        rng=np.random.default_rng(8092026)
+        dates=pd.Index(['2020-12-28','2020-12-29','2020-12-30','2020-12-31','2021-01-04','2021-01-05'])
+        for scenario in range(40):
+            prices=100*np.exp(np.cumsum(rng.normal(0,.1,(6,3)),axis=0))
+            div=rng.uniform(0,2,(6,3));div[0]=0;div[:3,2]=0
+            returns=np.vstack([np.zeros(3),prices[1:]/prices[:-1]-1]);returns[:3,2]=np.nan
+            det=np.vstack([np.zeros(3),div[1:]/prices[:-1]])
+            targets=pd.DataFrame([[.5,.5,0],[1/3]*3,[1/3]*3],index=dates[[0,3,4]],columns=['A','B','C'])
+            for reeq in [False,True]:
+                rate=float(rng.uniform(0,.02))
+                units=np.array([.5/prices[0,0],.5/prices[0,1],0.]);cash=np.zeros(3);expected=[]
+                for i in range(6):
+                    if i:cash+=units*div[i]
+                    old=units*prices[i];value=old.sum()+cash.sum()
+                    if i==3:
+                        target=old*(2/3);reserve=cash*(2/3);target[2]=value/3
+                    elif i==4:
+                        target=np.full(3,value/3) if reeq else old+cash
+                        reserve=np.zeros(3)
+                    else:
+                        expected.append(value);continue
+                    fee=0.
+                    for _ in range(100):
+                        next_fee=rate*np.abs(target*(1-fee/value)-old).sum()
+                        if abs(next_fee-fee)<1e-15:fee=next_fee;break
+                        fee=next_fee
+                    units=target*(1-fee/value)/prices[i];cash=reserve*(1-fee/value)
+                    expected.append((units*prices[i]).sum()+cash.sum())
+                r=pd.DataFrame(returns,index=dates,columns=targets.columns)
+                d=pd.DataFrame(det,index=dates,columns=targets.columns)
+                actual,_,_=simuler(r,d,list(r),targets,dates,{dates[0],dates[4]},reeq,rate)
+                np.testing.assert_allclose(actual,expected,rtol=0,atol=2e-14,
+                                           err_msg=f'scenario={scenario},reeq={reeq}')
+
+
+if __name__=='__main__':unittest.main()
```

</details>

### `tests/test_portefeuille.py`

Faire appeler le moteur au cas de dividende ; vérifier 105 de richesse pour 100 de mise, et non la formule Yahoo recopiée dans le test.

Avant : `12159b1e59de9e91065790ba138a6cc4a523596d1b13aee5e645bb6751895fe2`. Après : `8c69ad6f7f03d3c4f4bd8e9d3b64701cb22a2bb5ba1e1eeeb2a3aa487db8d758`.

Lignes physiques : 167 avant, 170 après.

Les repères `@@` indiquent les lignes avant et après. `-` contient le texte retiré, `+` le texte retenu.

<details>
<summary>Contenu exact des changements</summary>

```diff
--- tests/test_portefeuille.py avant
+++ tests/test_portefeuille.py après
@@ -12,5 +12,5 @@
 import pandas as pd
 
-from src.portefeuille import rendements_et_dividendes, poids_cibles, simuler
+from src.portefeuille import rendements_et_dividendes, poids_cibles, simuler, preparer_prix
 
 
@@ -62,10 +62,13 @@
                         "une division retraitee ne doit pas creer de rendement aberrant")
 
-    def test_cas_4_convention_multiplicative_et_non_additive(self):
+    def test_cas_4_dividende_en_especes_dans_le_moteur(self):
         p = prix([100.0, 95.0], dividendes=[0.0, 10.0])
         r, d = rendements_et_dividendes(p)
-        total = (1 + r.iloc[1]) / (1 - d.iloc[1]) - 1
-        self.assertAlmostEqual(total, 95 / 90 - 1, places=12)
-        self.assertNotAlmostEqual(total, 105 / 100 - 1, places=3)
+        r.iloc[0], d.iloc[0] = 0, 0
+        cible = pd.DataFrame({"A": [1.]}, index=[p.index[0]])
+        v, _, _ = simuler(r.to_frame("A"), d.to_frame("A"), ["A"], cible,
+                          p.index, set(cible.index), False, cout=0)
+        self.assertAlmostEqual(v.iloc[-1], 1.05, places=12)
+        self.assertNotAlmostEqual(v.iloc[-1], 95 / 90, places=3)
```

</details>

### `research/audit_etape_2.md`

Création du présent diagnostic, des résultats recalculés, de la couverture et de ce journal. Avant : aucun rapport de cet audit dans le cliché initial. Après : les sections I à VI constituent le livrable. Son propre contenu ne reçoit pas une empreinte à l’intérieur de lui-même.

<!-- JOURNAL_END -->

## VI. Vérification finale et durée

Les 92 tests du dépôt passent, dont 41 pour l'étape 2 et 51 pour les dépendances de l'étape 1. L'oracle en nombres de parts comporte quarante jeux de données dans chacun des deux modes de gestion, soit quatre-vingts scénarios. Ces tests ne remplacent pas les replays du cliché réel.

Les dix-huit sorties du traitement courant sont identiques octet par octet entre le dépôt, la reconstruction sous Python 3.12.14 et celle sous Python 3.13.9. Les versions de pandas et NumPy sont respectivement 3.0.0 et 2.4.1. Les deux environnements sont sur cette même machine Windows : ce résultat n'est pas un essai sur toutes les plateformes. Les manifestes conservent normalement des heures et versions d'environnement différentes.

Les cellules de code des notebooks de contrôle et de construction ont été exécutées dans leur ordre, en déroutant seulement leur dossier de sortie vers l'annexe. Leurs dix-huit résultats sont aussi identiques aux sorties publiées. Il s'agit d'une exécution des sources de cellules par Python, pas d'un test de l'interface Jupyter. Le collecteur est arrêté par son verrou avant la première acquisition ; ses requêtes réseau n'ont pas été exécutées.

Les 134 180 lignes du journal quotidien et les 225 984 lignes de poids ont été relues depuis les CSV. L'identité des rendements, les frais, les annualisations, les replis et les rotations concordent. En mémoire, le plus grand écart de somme des poids vaut 4,44089 × 10⁻¹⁶ et celui de l'identité quotidienne 7,55472 × 10⁻¹⁶. Après lecture des CSV, ces maxima sont respectivement 6,55032 × 10⁻¹⁵ et 9,00321 × 10⁻¹⁶, toujours sous 10⁻¹² ; la conversion décimale explique la différence de précision. Rejouer les vingt séries depuis les matrices CSV en inversant l'ordre des titres donne un écart relatif maximal de 1,60151 × 10⁻¹³ par rapport aux valeurs publiées. Les effectifs des dix groupes, leurs effectifs initiaux et l'égalité des cibles par entreprise ont été rapprochés du document de composition.

Le classeur courant compte 113 entreprises dans chacune de ses trois vues. Les 8 814 cellules de données correspondent à l'entrée d'export, les CIK restent du texte à dix chiffres et aucune cellule ne porte une erreur Excel. Les vues affectées ont été inspectées visuellement. Le reçu courant conserve la vérification antérieure comme historique.

Les empreintes finales des 2 646 fichiers protégés sont identiques à celles du début de l'audit, sans ajout ni suppression dans ce périmètre. Tous les résultats économiques couverts par le manifeste initial de l'étape 1 sont également inchangés. Le relevé différentiel compte 34 fichiers modifiés et 16 créés, soit 50 fichiers, rapport compris. Les changements déjà présents avant l'audit ne sont pas attribués à ce travail : la comparaison utilise le cliché local initial, pas le seul écart avec Git.

Les commandes `python -B src/run_pipeline.py --check-only` et `python -B -m src.construire_portefeuilles --check-only` réussissent sur les sorties courantes. `git diff --check` ne relève pas d'erreur de différence. Aucun commit ni envoi GitHub n'a été effectué pendant cet audit.

Le contrôle a commencé le 8 septembre 2026 à 04:44:17 UTC, soit 06:44:17 à Paris. La clôture du diagnostic est enregistrée à 2026-09-08 06:44:40 UTC. La durée écoulée est de 2 h 00 min 23 s. Elle comprend les lectures, recalculs, recherches ciblées, corrections, replays et contre-vérifications décrits ici. Cette durée ne constitue pas une garantie d'absence de toute erreur.

Les corrections rendent le calcul conforme aux règles précisées et sa reconstruction contrôlable. Elles ne ferment pas les réserves de données, d'exécution et d'interprétation exposées dans la partie IV. L'étape 2 reste donc en cours.
