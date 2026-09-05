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

## Blocs 2 et 3 — Prochaine étape

Je dois maintenant formuler le **Research Problem**, puis la **Research Question** testable. Le premier expliquera la difficulté que ces constats soulèvent ; la seconde précisera ce que les données et les comparaisons de portefeuilles permettront de trancher. Ces deux blocs ne sont pas encore finalisés.
