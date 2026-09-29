# Research Charter — AI Concentration Risk Research

*Version 1 — 5 septembre 2026. Bloc 1 finalisé pour le cadrage actuel ; blocs 2 et 3 à construire.*

## Pourquoi je fixe cette formulation

Au départ, j'avais préparé un texte centré sur le poids des plus grandes entreprises du S&P 500. Il restait des chiffres à remplir et cette structure ne décrivait plus entièrement le travail réalisé : je documente aussi les entreprises qui fournissent les équipements, les composants et l'énergie nécessaires aux infrastructures de calcul.

Je pars donc de deux constats distincts : une concentration publiée à l'échelle du marché et des activités documentées dans cette chaîne. Leur présence simultanée ne suffit pas à établir un risque commun. C'est ce qui me permet de poser le phénomène sans écrire d'avance le résultat de la recherche.

## Bloc 1 — Phenomenon of Interest

Dans son rapport sur la stabilité financière d'avril 2026, le FMI situe la dernière observation de l'indice de concentration de Herfindahl–Hirschman (HHI) des actions américaines au **97,7e percentile de son historique depuis 1990**, dans la figure 1.7, panneau 4. Ce chiffre décrit la position historique de l'indicateur publié ; il ne représente pas la part du marché détenue par un groupe d'entreprises. [FMI, chapitre 1, p. 11](https://www.imf.org/-/media/files/publications/gfsr/2026/april/english/ch1.pdf).

Les rapports annuels 2025 documentent également des activités dans plusieurs métiers de la chaîne de calcul. Applied Materials décrit des équipements de fabrication de semi-conducteurs dont les débouchés comprennent les serveurs destinés à l'IA et aux centres de données. Amphenol rapporte une hausse de ses ventes au marché informatique et des communications de données, qu'elle rattache notamment à la demande de produits destinés aux applications liées à l'IA, ainsi qu'aux réseaux, aux serveurs et au stockage cloud. [Applied Materials, 10-K 2025, Item 1](https://www.sec.gov/Archives/edgar/data/6951/000162828025056742/amat-20251026.htm), [Amphenol, 10-K 2025, Item 7](https://www.sec.gov/Archives/edgar/data/820313/000110465926013549/aph-20251231x10k.htm).

Dans l'électricité, Dominion Energy indique que les centres de données représentent **28 % des ventes d'électricité de Virginia Power en 2025, contre 26 % en 2024**. Ce périmètre est celui de Virginia Power ; ces pourcentages ne mesurent pas une part de chiffre d'affaires IA du groupe Dominion Energy. Les centres de données accueillent aussi d'autres usages. [Dominion Energy, 10-K 2025, Item 1, présentation de Dominion Energy Virginia](https://www.sec.gov/Archives/edgar/data/715957/000119312526063120/d-20251231.htm).

## Comment je peux revenir aux faits

| Observation | Pièce et repère | Représentation possible |
|---|---|---|
| Concentration du marché américain | FMI, avril 2026, chapitre 1, figure 1.7, panneau 4 et sa note | Figure historique publiée depuis 1990, avec son indicateur et son périmètre conservés |
| Équipements et composants pour la chaîne de calcul | Applied Materials, exercice clos le 26 octobre 2025, Item 1 ; Amphenol, exercice clos le 31 décembre 2025, Item 7, comparaison 2025–2024 | Tableau daté des métiers, débouchés et déclarations ; les ventes au marché informatique ne deviennent pas des ventes exclusivement IA |
| Débouché électrique des centres de données | Dominion Energy, exercice clos le 31 décembre 2025, Item 1, passage sur Virginia Power | Deux barres pour les parts des ventes d'électricité en 2024 et 2025, sur le même périmètre |

Les rapports d'entreprises sont conservés dans le [corpus local](../data/raw/filings_text/). Le [registre des décisions](../data/review/decisions_selection.csv) permet de retrouver les dépôts et les passages associés à ces entreprises. Je paraphrase les déclarations dans le bloc 1 ; je ne les présente pas comme des mesures indépendantes de la contribution de l'IA.

J'applique les trois tests du contexte maître : les constats ne comportent pas de jugement sur un placement ; une personne qui conteste mon hypothèse de risque peut accepter ces faits ; chaque énoncé possède une source datée et une représentation identifiable. Les déclarations sur les métiers se présentent dans un tableau, sans leur inventer une série chiffrée. L'indicateur du FMI reste un constat publié selon sa méthode, pas un calcul de risque sur mes futurs portefeuilles.

## Ce que ce bloc fixe pour la suite

La concentration de marché constitue le contexte. L'univers construit à partir de la composition locale du S&P 500 décrit un périmètre économique plus large que quelques mégacapitalisations. Les exemples du bloc 1 illustrent des activités observées ; la règle de sélection et son application à l'ensemble des entreprises restent décrites dans les documents dédiés.

Le nombre d'entreprises retenues est un résultat de cette sélection, pas une preuve de concentration du risque. Les liens documentaires ne permettent pas encore de conclure que les cours réagissent ensemble, que la diversification échoue ou qu'un portefeuille aura de bonnes performances. L'univers pourra alimenter plusieurs portefeuilles, avec des compositions et des poids à définir.

Le bloc 1 est désormais rédigé et sourcé. La vérification de la composition locale de l'indice et les revues encore ouvertes restent des tâches concernant les données ; elles ne sont pas utilisées comme preuves dans ce paragraphe.

## Blocs 2 et 3

*Le bloc 3 est adopté par l'auteur le 29 septembre 2026. Le bloc 2 a été proposé le 28 septembre 2026, avant cette question ; il reste une proposition, à réécrire après la revue de littérature pour poser le problème de la question adoptée.*

### Bloc 2 — Research Problem

Le bloc 1 pose deux constats : la concentration du marché américain est historiquement élevée, et des entreprises de métiers très différents, semi-conducteurs, équipement, électricité, immobilier, déclarent une activité dans la chaîne des infrastructures de calcul.

La difficulté est que ces deux constats ne disent rien, à eux seuls, du risque d'un investisseur. Une exposition documentée dans un rapport annuel est une relation économique ; elle n'implique ni que les cours de ces entreprises bougent ensemble, ni qu'un portefeuille qui les rassemble soit plus risqué qu'un autre. Inversement, un portefeuille peut devenir concentré sans que personne n'ait choisi de le concentrer, par la seule dérive des poids. Trois obstacles empêchent de trancher par simple observation :

1. **Le biais de sélection.** Un univers défini avec les rapports de 2026 et appliqué depuis 2000 ne contient que des survivants. Toute performance mesurée mélange l'effet du thème et celui de la survie.
2. **La confusion entre thème, secteur et pondération.** Un portefeuille du thème est surpondéré en technologie et en services aux collectivités, et il est équipondéré. Comparé au marché, il diffère sur ces trois points à la fois.
3. **Le bruit d'échantillonnage.** Sur vingt-six ans de données quotidiennes, des écarts de ratio de Sharpe de l'ordre de 0,05 sont du même ordre que leur incertitude.

Le problème est donc d'isoler ce que l'exposition documentée à cette chaîne ajoute au risque, une fois neutralisés le biais de survie, le mélange sectoriel et la pondération, et de distinguer ce qui relève de la sélection des entreprises de ce qui relève de la gestion des poids.

### Bloc 3 — Research Question

**Question principale.** Peut-on construire, à partir des entreprises du S&P 500 exposées à la chaîne des infrastructures de calcul liées à l'IA, un portefeuille qui garde l'essentiel de leur potentiel de hausse tout en limitant ses pertes en crise, et à quel coût ?

**Trois sous-questions, dans l'ordre.**

1. **Le portefeuille nu est-il prometteur ?** Son rendement ajusté du risque dépasse-t-il celui du témoin `T1S`, qui porte le même biais de survie ?
2. **D'où vient son risque ?** Traitée à l'étape 3.
3. **Quelle protection réduit ce risque, à quel coût, et laquelle est la meilleure selon les critères ci-dessous ?**

**Critères, fixés avant tout calcul des étapes 4 et 5.** Une stratégie est acceptable si, sur la période rétrospective et frais de protection payés :

1. son pire drawdown n'est pas plus profond que celui de `T1S` ;
2. sa perte moyenne au-delà de la VaR à 99 % n'est pas plus forte que celle de `T1S` ;
3. son rendement annualisé n'est pas inférieur à celui de `T1S`.

Parmi les stratégies acceptables, la meilleure est celle dont le ratio de Sharpe est le plus élevé. Un écart ne compte que si l'intervalle à 95 % du bootstrap par blocs d'un trimestre exclut zéro. Si aucune stratégie n'est acceptable, c'est une réponse : on le dit, et on indique le critère qui échoue.

**Pourquoi la comparaison entre stratégies reste juste malgré le biais de survie.** La version protégée et la version nue contiennent les mêmes entreprises. Le biais de survie les touche toutes deux, et l'écart entre elles mesure la protection. Le rendement absolu reste flatté ; c'est pourquoi la sous-question 1 compare au témoin `T1S` et non au marché. Le témoin partage ce biais sans forcément en subir le même effet, et ses parts sectorielles sont celles de 2026 : la comparaison est descriptive (section XI de `research/resultats_risque.md`).

**Ce que la question ne demande pas.** Elle ne cherche pas à prédire quelle entreprise deviendra la prochaine grande gagnante : l'univers n'était pas connaissable en 2000, et aucune donnée du projet ne le permet. Elle ne porte pas sur la concentration de l'indice par capitalisation, que l'auteur a exclue le 8 septembre 2026 ; la concentration du bloc 1 reste un contexte.

**Un test prospectif ne commence qu'après la date où son protocole est figé.** Toute prédiction sur des séances futures sera écrite, datée et commitée avant la première séance qu'elle concerne.

*Adopté par l'auteur le 29 septembre 2026.*
