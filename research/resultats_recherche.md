# Résultats de la recherche systématique de règles de construction

*AI Concentration Risk Research. 29 septembre 2026.*

*Décisions écrites et commitées avant tout calcul, section IX de `research/plan_projet.md`. Calculs dans `src/recherche_regles.ipynb` et `src/synthese_regles.ipynb`, fonctions dans `src/regles.py` et leurs tests dans `tests/test_regles.py`, sorties `regles_*` et `aleatoires_*` dans `data/processed/`. Toutes les comparaisons se font à l'intérieur d'un univers choisi avec les rapports de 2026 : aucune performance citée ici n'était réalisable.*

## I. Ce qui a été fait

L'auteur voulait essayer toutes les combinaisons possibles. Elles sont trop nombreuses pour être calculées, et la meilleure serait un gagnant choisi après coup. J'ai donc fait trois choses.

1. **Neuf cents règles construites.** Quatre sélections : toutes les entreprises, ou trois sélections selon une note fondamentale. Neuf pondérations, de l'équipondération à la variance minimale. Vingt-cinq protections : aucune, pilotage de la volatilité, mélanges avec obligations et liquidités, ou options au prix réel de l'indice CBOE `PPUT`. Chaque règle n'utilise à chaque date que l'information disponible la veille. Les chiffres comptables ne servent qu'après leur dépôt à la SEC.
2. **Cent mille portefeuilles tirés au hasard** parmi les mêmes entreprises, pour savoir ce que produit le hasard dans cet univers.
3. **Le gagnant soumis à trois contrôles fixés d'avance**, pour savoir s'il se distingue vraiment.

La fenêtre commune va du 3 janvier 2011 au 4 septembre 2026, car les données comptables XBRL de la SEC commencent avec les dépôts de 2010.

Le moteur a été contrôlé contre `P1` rééquilibré de l'étape 2, sur 2001 à 2026 : la corrélation quotidienne est de 0,9987. L'écart de rendement, 18,13 % contre 18,94 % par an, vient des conventions plus prudentes de cette version : un titre n'entre qu'en janvier, et seulement avec un an d'historique.

## II. La réponse à la question du bloc 3

La question adoptée demande si l'on peut garder l'essentiel de la hausse tout en limitant les pertes en crise, et à quel coût. Une règle est acceptable si elle ne fait pire que le témoin `T1S` sur aucun des trois critères : repli maximal, perte moyenne au-delà de la VaR à 99 %, rendement annualisé.

**Sur 2011 à 2026, la réponse est oui : 102 règles sur 900 sont acceptables.** Le critère qui trie est le rendement. Presque toutes les règles battent `T1S` sur le repli et sur la perte extrême, 875 et 884 sur 900, mais seules 118 font au moins aussi bien que ses 16,09 % par an. Protéger est facile ; protéger sans perdre de rendement est rare. Parmi les portefeuilles aléatoires, sans protection, seuls 1,3 % satisfont les trois critères.

**La règle au meilleur Sharpe parmi les acceptables** combine trois choses :
- toutes les entreprises ;
- des contributions au risque égales entre les sept groupes de la chaîne, estimées sur deux ans ;
- un pilotage de la volatilité visant 15 %, mesuré sur un mois, avec le reste placé en obligations du Trésor.

Face à `T1S` :

| | Rendement annualisé | Volatilité | Repli maximal | Perte au-delà de la VaR 99 % | Sharpe |
|---|---|---|---|---|---|
| Règle gagnante | 17,00 % | 14,53 % | −27,7 % | 3,49 % | 1,05 |
| `T1S` | 16,09 % | 17,33 % | −38,2 % | 4,42 % | 0,86 |

Son bêta au marché vaut 0,77. Les quinze meilleures règles acceptables se ressemblent : presque toutes répartissent le risque entre groupes, et toutes ajoutent une protection. La protection est soit un pilotage de la volatilité, soit des puts réels sur la moitié du bêta, soit un mélange à 80 % d'actions.

**Le coût.** La même répartition par groupe, estimée sur un an et sans protection, rapporte 19,98 % par an pour un repli de −36,4 %. La protection du gagnant coûte donc environ trois points de rendement par an, pour neuf points de repli en moins. La jambe d'options du `PPUT` a coûté en moyenne 3,93 % par an par rapport au S&P 500 en rendement total sur la fenêtre : c'est le prix réel d'une assurance permanente par puts à 5 % hors de la monnaie.

## III. Les trois contrôles : aucune règle ne se distingue de façon établie

1. **L'écart de Sharpe avec `T1S`** vaut 0,19, avec un intervalle à 95 % de −0,05 à +0,40 (probabilité 0,13). L'intervalle contient zéro : le contrôle échoue.
2. **Le Deflated Sharpe Ratio** vaut 0,998 pour un seuil de 0,95 : le contrôle passe. Mais ce test demande seulement si le vrai Sharpe dépasse zéro après correction pour 900 essais, et zéro n'est pas le bon point de comparaison ici. Dans cet univers de survivants, les portefeuilles tirés au hasard ont un Sharpe médian de 0,98, et 93,1 % d'entre eux dépassent celui de `T1S`. Passer ce test ne dit donc rien de la valeur de la règle. Je l'avais choisi avant calcul sans voir cette limite, et je l'écris plutôt que de changer le test après coup.
3. **La probabilité de surapprentissage** vaut 0,59 sur 12 870 découpages de la fenêtre. La règle la meilleure sur une moitié des données finit plus souvent sous la médiane que dessus sur l'autre moitié. Le classement entre règles n'est pas stable.

Le test de White, calculé en complément, donne une probabilité de 0,46 que le meilleur écart de Sharpe avec `T1S` apparaisse sans aucun talent.

La règle fixée d'avance s'applique : le gagnant échoue au premier contrôle, donc **aucune règle ne se distingue de `T1S` de façon établie.** Des règles protégées font mieux que le témoin sur les trois critères, mais leur avance en Sharpe reste dans ce que le hasard et le choix parmi 900 essais peuvent produire. Le gagnant particulier n'est pas fiable. La famille qui revient en tête, répartition du risque par groupe plus protection, est un indice, pas une preuve.

## IV. Ce que les portefeuilles aléatoires apprennent

**L'univers compte plus que la règle.** Sur 2011 à 2026, un portefeuille tiré au hasard parmi les 134 entreprises a un Sharpe médian de 0,98 et rapporte 20,97 % par an. `T1S` n'est qu'au 7e centile de cette distribution. L'essentiel de ce qui sépare le thème du témoin sur cette fenêtre tient donc à l'univers lui-même, choisi en 2026, et non à la façon d'y construire un portefeuille.

**Les règles se situent au milieu du hasard, pas au-dessus.** L'équipondération simple sans protection est au 68e centile de Sharpe. La répartition du risque par groupe est au 72e centile ; elle réduit la volatilité mieux que 97 % des portefeuilles aléatoires. Le gagnant protégé dépasse 88,9 % d'entre eux en Sharpe. La variance minimale obtient la volatilité la plus basse, mais son Sharpe tombe entre le 1er et le 3e centile. Elle concentre alors la moitié de son risque sur l'électricité.

## V. La sélection fondamentale a fait moins bien que ne rien sélectionner

La note fondamentale tirée de la revue combine cinq critères notés dans chaque groupe : profitabilité, qualité des résultats, croissance de l'actif, rendement bénéficiaire, solidité du bilan. Je l'ai comparée à l'absence de sélection, à pondération et protection égales, sur 225 paires par sélection.

**Elle n'améliore le Sharpe dans aucune paire, et le dégrade significativement dans 47 à 123 paires sur 225 selon la sélection.** Garder la moitié la mieux notée de chaque groupe le dégrade dans 79 paires ; garder le tiers, dans 123. Le centile de Sharpe médian tombe de 0,38 sans sélection à 0,07 avec la sélection la plus stricte.

L'explication la plus probable est celle de la période : de 2011 à 2026, les entreprises qui ont le plus monté sont celles que ces critères pénalisent, à forte croissance de l'actif et à faible rendement bénéficiaire. Ce résultat ne contredit pas la littérature, qui mesure des primes moyennes sur de nombreuses décennies et de nombreuses entreprises. Il dit que, dans cet univers et sur cette fenêtre, trier selon ces critères a écarté les gagnants.

Une réserve de données s'y ajoute. Le critère de profitabilité n'est disponible que pour 42 à 72 % des entreprises selon l'année, car les électriciens et les foncières ne publient pas de marge brute ; il vaut alors le milieu du groupe.

## VI. Les quatre attentes écrites avant calcul

1. *Aucune règle ne passera le Deflated Sharpe Ratio.* **Contredite**, mais pour une raison qui affaiblit le test plutôt que la règle (section III).
2. *La répartition du risque par groupe ramènera la part de `P5` et `P9` sous 50 %.* **Contredite de peu** : elle la ramène de 71,9 % avec l'équipondération à 50,7 % et 51,6 %, selon la fenêtre d'estimation.
3. *Les règles acceptables seront surtout protégées.* **Non contredite au sens du critère écrit** : 90 des 102 le sont. Mais en proportion, les règles sans protection sont plus souvent acceptables, 33 % contre 11 % pour le pilotage de la volatilité et 6 % pour les mélanges. Les douze règles acceptables sans protection sont toutes des pondérations à faible volatilité.
4. *La sélection fondamentale ne fera pas mieux que l'absence de sélection.* **Confirmée, et au-delà** : elle fait significativement moins bien dans de nombreuses paires (section V).

## VII. La lecture depuis 2001

Sur 2001 à 2026, pour les 225 règles sans sélection fondamentale, **aucune n'est acceptable**. `T1S` y rapporte 16,89 % par an, et aucune règle protégée ne l'égale en rendement. Les meilleures ont pourtant un Sharpe supérieur à 99,9 % des portefeuilles aléatoires non protégés. Par exemple, la répartition par groupe avec un pilotage à 10 % obtient 0,99 de Sharpe et −23,5 % de repli, pour 13,05 % par an. La réponse à la question du bloc 3 dépend donc de la fenêtre. Sur quinze ans de marché haussier, on a pu protéger sans perdre de rendement face au témoin ; sur vingt-cinq ans, crises de 2000 et 2008 comprises, la protection a toujours coûté du rendement.

## VIII. Ce que je retiens et ce que je m'interdis

Je retiens quatre énoncés, chacun sous sa réserve :
- On peut construire, dans cet univers, des portefeuilles qui battent le témoin sur les trois critères du bloc 3 sur 2011 à 2026, en répartissant le risque entre groupes et en ajoutant une protection. Mais aucune ne s'en distingue de façon statistiquement établie, et le classement entre règles n'est pas stable.
- L'univers lui-même explique davantage que la règle de construction.
- La sélection fondamentale fondée sur la littérature n'a rien apporté ici.
- Le Deflated Sharpe Ratio, appliqué contre un Sharpe nul, n'est pas le bon juge dans un univers de survivants ; la comparaison au témoin et aux portefeuilles aléatoires l'est.

Je m'interdis de présenter le gagnant comme une stratégie à suivre, de citer ses rendements comme réalisables, et d'oublier les 899 autres règles, toutes publiées dans `data/processed/regles_mesures.csv`.

**Limites propres à cette version.**
- La fenêtre n'est que de quinze ans et demi.
- Les options sont celles de l'indice S&P 500, pas du thème.
- Les dividendes sont réinvestis au détachement.
- Le témoin garde ses parts sectorielles de 2026.
- Aucun portefeuille aléatoire n'est protégé, ce qui rend la comparaison d'une règle protégée au hasard favorable à la règle.
