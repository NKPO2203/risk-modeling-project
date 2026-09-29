# Revue de littérature : ce qu'elle apprend sur mes résultats et ce qu'elle dit de la stratégie

*AI Concentration Risk Research. 29 septembre 2026.*

*Les documents reçus sont conservés dans `research/sources_revue_2026-09-29/`. La vérification des références est produite par `python -m src.verifier_bibliographie`, qui écrit `data/review/bibliographie_verification.csv`. La question de recherche est celle adoptée le 29 septembre au bloc 3 du Research Charter : peut-on construire, à partir du thème, un portefeuille qui garde l'essentiel de son potentiel de hausse tout en limitant ses pertes en crise, et à quel coût ?*

## I. Ce que vaut la revue comme source

La revue est une synthèse produite par un outil de recherche automatisée, en deux versions qui ne citent pas exactement les mêmes articles. Les soixante références des deux versions existent toutes. Sept DOI sur quarante-huit de la version A étaient faux, dont deux qui menaient à un autre article ; les bons sont dans le fichier de vérification. Les cinquante fiches annoncées, qui auraient donné pour chaque article sa question, sa méthode et ses limites, n'ont pas été transmises. Ce que je rapporte ci-dessous du contenu des articles est donc ce qu'en dit la revue. Je ne l'ai confronté au texte que pour les deux prépublications de 2026, dont les résumés confirment les chiffres cités.

Deux reprises de mon propre travail y sont fausses, parce qu'elles datent d'avant les corrections du 29 septembre. La revue lit l'écart de 7,6 points entre le témoin et `SPY` comme une mesure du biais de survie : l'écart vaut 7,8 points avec `SPY` à 8,27 %, et il n'est pas une mesure de ce biais. Elle appelle aussi « puces » les groupes `P5` et `P9`, qui mêlent semi-conducteurs, réseau, stockage, serveurs, services et chimie. Toutes ses recommandations sur « le maillon puces » portent donc sur un périmètre qui n'existe pas encore : le définir est l'un des choix en attente de la section VI bis du plan.

## II. Ce qu'elle apprend sur les résultats de l'étape 3

**Pourquoi 135 titres valent environ trois actifs indépendants.** Evans et Archer (1968), puis Elton et Gruber (1977), montrent que le gain d'un titre supplémentaire devient vite marginal quand les titres partagent les mêmes facteurs. Mon résultat n'est pas une curiosité : c'est la prédiction classique appliquée à un univers très corrélé. Il en découle la conséquence stratégique la plus importante de la revue : **la protection ne viendra pas du nombre de titres.** Elle viendra de la répartition du risque entre groupes, de la gestion de l'exposition, ou d'actifs extérieurs.

**Pourquoi la corrélation de crise se lit avec prudence.** Forbes et Rigobon (2002) montrent qu'une hausse de variance du marché suffit à faire monter la corrélation mesurée. La revue conclut comme la réserve déjà écrite : absence de hausse après correction, pas preuve d'absence de contagion.

**Ce que le témoin mesure et ne mesure pas.** Brown, Goetzmann, Ibbotson et Ross (1992) établissent que l'exclusion des disparus fausse les performances. Le témoin répond à « parmi les survivants, le thème se distingue-t-il ? », pas à « qu'aurait gagné un investisseur ? ». C'est la formulation adoptée le 29 septembre.

**Ce qui n'est pas encore nouveau.** Ante et Saggu (2025) définissent déjà une exposition à l'IA à partir des rapports 10-K. Ce qui reste propre à ce projet, dans le corpus examiné, est la preuve d'une activité dans la chaîne physique du calcul et la décomposition du risque par groupe de cette chaîne.

## III. Ce qu'elle dit de la stratégie à construire

La question adoptée cherche une protection qui garde la hausse. La littérature citée par la revue classe les candidates ainsi.

**Réduire l'exposition quand la volatilité monte.** Fleming, Kirby et Ostdiek (2001), Moreira et Muir (2017), puis Harvey et ses coauteurs (2018) trouvent que ce pilotage améliore le rendement ajusté du risque sur les actions et atténue certaines pertes extrêmes. C'est la candidate la mieux soutenue. Sa faiblesse connue est de rater une partie des rebonds rapides, ce que le troisième critère du bloc 3, un rendement au moins égal à celui de `T1S`, mettra à l'épreuve. Une version sans levier, dont l'exposition ne dépasse jamais 100 %, correspond à l'objectif défensif.

**Répartir le risque entre groupes plutôt qu'entre titres.** Maillard, Roncalli et Teïletche (2010) donnent les propriétés du portefeuille à contributions au risque égales. Les deux versions de la revue recommandent de le faire au niveau des groupes de la chaîne. C'est la réponse directe au constat que `P5` et `P9` portent 77 % du risque pour 45 % de l'argent. Anderson, Bianchi et Goldberg (2012) préviennent que ses résultats dépendent de la période. La covariance devra être estimée avec l'estimateur de Ledoit et Wolf (2004), puisque 135 titres sur 252 séances donnent une matrice bruitée. Le même estimateur servira à vérifier le 77 % lui-même.

**Acheter des puts.** Coval et Shumway (2001) et Bondarenko (2014) montrent que l'assurance par options coûte cher. Israelov (2019) trouve qu'acheter des puts en continu fait moins bien que réduire simplement l'exposition. La revue en fait la dernière étape, à ne tester que si les deux premières ne suffisent pas. L'historique PPUT du CBOE, ajouté au dépôt, donne le coût réel d'une telle protection sur l'indice. Une couverture ciblée sur les semi-conducteurs demanderait d'abord leur périmètre, puis un instrument dont je n'ai pas l'historique.

**Optimiser les poids.** DeMiguel, Garlappi et Uppal (2009) ne trouvent aucune des quatorze méthodes optimisées qui batte l'équipondération hors échantillon. Le portefeuille équipondéré reste donc la référence, et toute optimisation devra porter sur le risque, pas sur des rendements espérés estimés.

**Choisir la meilleure sans se tromper soi-même.** Le bloc 3 retient, parmi les stratégies acceptables, celle dont le Sharpe est le plus élevé. White (2000), Hansen (2005), Harvey, Liu et Zhu (2016), Bailey et López de Prado (2014) montrent que le meilleur de plusieurs essais est surestimé. Pour que ce choix tienne, trois règles s'imposent. Le nombre de stratégies est fixé et écrit avant calcul. Chaque essai est consigné. Le Sharpe du gagnant est corrigé du nombre d'essais, par le Deflated Sharpe Ratio ou le test de White.

**Contrôler le risque extrême proprement.** Christoffersen (1998) ajoute au test de Kupiec un test d'indépendance des dépassements, qui répond au regroupement des pertes déjà constaté. Il servira à juger si une stratégie protège vraiment en crise.

## IV. Ce que la revue laisse sans réponse

Elle ne dit pas comment faire suivre à `T1S` les parts sectorielles de `P1` dans le temps. La référence pertinente, hors de la revue, est celle des témoins par caractéristiques de Daniel, Grinblatt, Titman et Wermers (1997), vérifiée dans le même fichier. Elle ne propose aucun périmètre des semi-conducteurs, et ne dit rien des scénarios de choc ni de la vérification des prix extrêmes. Mesurer réellement le biais de survie et reclasser les entreprises avec les seuls rapports disponibles à chaque date exigeraient les compositions historiques de l'indice. Les bases CRSP et Compustat, qu'elle recommande, sont payantes.

## V. Ce que j'en retiens pour refaire les étapes 4 et 5

La nouvelle phase 0 peut s'appuyer sur la revue pour fixer, avant tout calcul, un petit nombre de stratégies. Les candidates, par ordre de soutien dans la littérature :
1. le pilotage de la volatilité, sans levier ;
2. la répartition du risque entre groupes de la chaîne, sur une covariance de Ledoit et Wolf ;
3. leur combinaison ;
4. les obligations et les liquidités, déjà mesurées dans le brouillon ;
5. en dernier, les puts, évalués sur le PPUT réel.

Chacune sera jugée sur les trois critères du bloc 3 face à `T1S`, et la meilleure sera choisie avec un Sharpe corrigé du nombre d'essais. Deux décisions restent à l'auteur avant cette phase 0 : le périmètre des semi-conducteurs, et le nombre de stratégies autorisées.
