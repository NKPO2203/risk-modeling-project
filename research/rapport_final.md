# AI & Mega-Cap Concentration Risk in U.S. Equities

*Rapport final de l'AI Concentration Risk Research. Version du 28 septembre 2026.*

*Ce rapport suit la table des matières de la section 24 du contexte maître. Il rassemble des résultats établis dans les documents de chaque étape, qui en donnent le détail et les calculs : `research/portefeuilles.md` pour la construction, `research/resultats_risque.md` pour le risque, `research/resultats_couverture.md` pour la diversification et la couverture, `research/resultats_strategies.md` pour la comparaison des stratégies. Chaque chiffre est produit par une cellule d'un carnet de `src/`, cité à la fin de chaque chapitre. Les étapes 4 et 5 et le portefeuille P11 ont été menés en un seul tour de travail, sur des décisions que l'auteur m'avait déléguées ; elles sont écrites comme des propositions qu'il pourra renverser.*

## I. Introduction

**Contexte.** Le FMI situe l'indice de concentration de Herfindahl et Hirschman des actions américaines au 97,7e percentile de son historique depuis 1990, et rattache cette concentration à l'optimisme des investisseurs sur les technologies liées à l'intelligence artificielle (*Global Financial Stability Report*, avril 2026, chapitre 1, figure 1.7). Au même moment, des entreprises de métiers très différents, semi-conducteurs, équipements, électricité, immobilier de centres de données, déclarent dans leurs rapports annuels une activité dans la chaîne des infrastructures de calcul.

**Motivation et problématique.** Ces deux constats ne disent rien, à eux seuls, du risque d'un investisseur. Une relation économique documentée n'implique ni que les cours bougent ensemble, ni qu'un portefeuille qui les rassemble soit plus risqué. Je voulais savoir ce que coûte, en risque, le fait de concentrer un portefeuille sur cette chaîne, et ce qu'on peut faire contre ce risque.

**Question de recherche.** Dans quelle mesure un portefeuille d'entreprises du S&P 500 exposées à la chaîne des infrastructures de calcul liées à l'IA porte-t-il un risque différent du reste du marché, d'où vient ce risque, et dans quelle mesure la diversification et la couverture permettent-elles de le réduire, à quel coût ?

**Hypothèses de départ.** Trois intuitions ont été écrites avant l'analyse, sans être tenues pour des conclusions. Hypothèse A, la concentration est dangereuse parce que ces entreprises partagent des facteurs communs. Hypothèse B, la concentration n'est pas forcément mauvaise, ces entreprises étant solides. Hypothèse C, le problème apparaît surtout en crise, quand la diversification s'efface.

**Contributions.** Je construis un univers de 134 entreprises à partir d'une règle de preuve documentaire appliquée aux 500 membres de l'indice, et non d'une liste de noms célèbres. J'en tire dix portefeuilles et vingt séries, puis je mesure leur risque contre le marché et contre un groupe témoin construit de la même façon avec les 366 entreprises écartées. Je compare ensuite douze stratégies de diversification et de couverture à risque égal. Les décisions de méthode de chaque étape ont été écrites avant les calculs, et chaque écart est daté.

**Structure.** Les chapitres II et III posent la littérature et les concepts, IV et V les données et la méthode, VI à X les résultats, XI la discussion, XII la conclusion.

## II. Revue de littérature

Je dois être net sur ce point : la revue de littérature n'a pas été faite. La matrice prévue à la section 19 du contexte maître est vide. Une seule source institutionnelle est vérifiée sur document primaire : le rapport du FMI d'avril 2026. Il fournit le constat de concentration, deux canaux de propagation d'une correction, et l'érosion de la relation de couverture entre actions et obligations depuis la pandémie, qui a servi à fixer avant calcul la coupure de 2022 de l'étape 4.

Les méthodes employées renvoient à des travaux connus dont je n'ai pas relu les textes originaux : la déviation à la baisse de Sortino, le test de couverture de Kupiec pour la VaR, la correction de corrélation de Forbes et Rigobon (2002), la formule d'évaluation des options de Black et Scholes. Elles sont décrites dans le code et ses tests, pas discutées contre leur littérature. Le positionnement de ce travail par rapport aux études existantes sur la concentration et la diversification reste donc à écrire. C'est la première limite de ce rapport, et le premier chantier d'une version suivante.

## III. Cadre conceptuel

**Rendement.** Rendement total, dividendes réinvestis, annualisé géométriquement à partir de la valeur finale. La moyenne arithmétique multipliée par 252 flatterait les séries les plus volatiles, et n'est jamais présentée comme un rendement.

**Risque.** Je ne dis jamais qu'un portefeuille est risqué sans dire de quel risque. J'en mesure cinq formes : la volatilité, la dispersion à la baisse, le repli maximal et sa durée, la perte extrême par la VaR historique et la perte moyenne au-delà, et la sensibilité au marché par le bêta.

**Concentration.** Deux concentrations sont distinguées tout au long du rapport : celle de l'argent, mesurée par l'inverse de l'indice de Herfindahl des poids, et celle du risque, mesurée par l'inverse de l'indice des contributions au risque. L'écart entre les deux est l'un des résultats centraux.

**Diversification.** Mesurée par le nombre d'actifs indépendants équivalents, déduit de la corrélation moyenne entre titres. Un portefeuille n'est pas diversifié parce qu'il contient beaucoup de lignes.

**Risque systématique et risque propre.** La part de variance expliquée par le marché, et celle qu'il n'explique pas.

**Couverture.** Une couverture ne fait pas disparaître le risque : elle le transfère contre un coût. J'appelle valeur ajoutée d'une stratégie l'écart de rendement entre elle et un mélange du portefeuille et de liquidités qui a exactement le même risque.

## IV. Données

**Univers.** Les 500 entreprises de la composition du S&P 500 relevée en 2026 ont été examinées une à une, sur leurs rapports annuels. Une entreprise entre si une activité ou un engagement concret dans la chaîne des infrastructures de calcul est documenté ; la règle est écrite dans `research/selection_rule.md`. Résultat : 134 entreprises retenues, 135 titres avec les deux classes d'Alphabet, et 366 écartées.

**Sources.** Les cours viennent de Yahoo Finance, source secondaire, rapprochée de Nasdaq sur 64 titres. Le taux sans risque est le bon du Trésor à treize semaines. Pour l'étape 4 s'ajoutent deux fonds du Trésor américain, l'indice `VIX` et l'indice CBOE PutWrite. Chaque fichier brut est inscrit dans un manifeste avec son empreinte.

**Période.** Du 3 janvier 2000 au 4 septembre 2026 : 6 709 séances, six épisodes de tension.

**Limites et biais.** Le biais principal est connu et chiffré : l'univers a été choisi avec les informations de 2026 et appliqué depuis 2000. Il ne contient que des survivants. Les séries du thème font de 11,7 % à 26,1 % par an quand `SPY` fait 8,35 %. Mais le témoin des 366 entreprises écartées, construit de la même façon, fait déjà 16,07 %, ce qui montre que l'essentiel de cette avance n'a rien à voir avec l'IA. Par ailleurs, quatre-vingt-deux variations extrêmes de cours restent non corroborées par une seconde source, et neuf divergences entre fournisseurs ne sont pas arbitrées. Les 134 degrés d'exposition au thème ne sont pas quantifiés. Le manifeste de l'étape 1 est périmé et ne peut être régénéré qu'avec le corpus local de 2,5 Go, absent de l'environnement où les étapes 4 et 5 ont été menées.

## V. Méthodologie

**Construction.** Dix groupes, `P1` pour l'univers entier et `P2` à `P10` pour ses sous-ensembles et ses maillons, chacun en deux gestions : rééquilibrée à poids égaux chaque janvier, ou conservée, les poids dérivant avec les cours. Aucune pondération par capitalisation, par décision de l'auteur du 8 septembre 2026. Frais de 10 points de base sur les montants échangés.

**Mesures.** Les neuf mesures fixées avant calcul à l'étape 3 : volatilité aux deux fréquences, semi-volatilité au sens de Sortino, repli maximal avec sa durée et son temps de récupération, asymétrie et aplatissement, VaR historique à 95 % et 99 %, perte moyenne au-delà, ratios de Sharpe et de Sortino, bêta au marché. Les contributions au risque suivent la décomposition d'Euler de $\sigma_p^2 = \mathbf{w}'\Sigma\mathbf{w}$, dont les parts somment exactement à la volatilité.

**Épisodes de tension.** Un repli de `SPY` d'au moins 15 % depuis son plus haut, du sommet au creux, appliqué mécaniquement.

**Significativité.** Bootstrap circulaire par blocs d'un trimestre, 2 000 tirages, les séries comparées étant tirées aux mêmes dates.

**Groupe témoin.** Les 366 entreprises écartées, construites avec le même moteur, à poids égaux (`T1`) ou aux parts sectorielles de `P1` (`T1S`).

**Stratégies.** Douze stratégies fixées avant calcul : 80 % ou 60 % du portefeuille mêlés à des liquidités, des obligations du Trésor intermédiaires ou longues, ou des actions hors du thème ; vente de contrats à terme sur la moitié ou la totalité du bêta ; achat mensuel de puts sur le S&P 500 à 90 % ou 95 % du cours, évalués par Black et Scholes avec le `VIX`.

**Discipline.** Chaque étape a commencé par une phase de décisions écrites et commitées avant le premier chiffre, avec les hypothèses et ce qui les contredirait. Les écarts découverts en cours de route sont datés dans les documents.

## VI. Analyse du portefeuille actions

**Performance.** Le rendement brut ne distingue pas les deux gestions : la concentration laissée libre rapporte davantage dans six portefeuilles sur dix, et dans quatre seulement quand on exclut 2000 à 2004. Face au témoin aux mêmes secteurs, le supplément du thème vaut 2,5 points de rendement excédentaire par an, avec un intervalle de −1,0 à +6,1 points : il n'est pas significatif.

**Risque.** `P1` rééquilibré est 1,14 fois plus volatil que le marché, 21,73 % contre 19,11 %, et plus volatil que le témoin aux mêmes secteurs de 2,2 points. Cet écart est significatif. Ses maillons vont de 0,97 à 1,84 fois le marché. Aucune des vingt-cinq séries n'a une distribution normale, et une VaR gaussienne y sous-estime la perte de 13 % à 21,5 %.

**Concentration.** Elle s'est formée en six ans. Dans `P1` conservé, le nombre effectif de lignes reste entre 52 et 78 de 2000 à 2019, puis tombe à 11,6 en 2026, avec Nvidia à 19,4 %. La version rééquilibrée termine à 106,9 lignes effectives.

**Sources du risque.** Les semi-conducteurs détiennent 45 % de l'argent de `P1` rééquilibré et portent 77 % de son risque. L'électricité en détient 14 % et en porte 2 %. Dans les vingt séries, le risque est plus concentré que l'argent : `P1` rééquilibré répartit son argent comme sur 107 lignes et son risque comme sur 30.

**Dépendance.** Avec une corrélation moyenne de 0,338, les 135 lignes de `P1` valent 2,92 actifs indépendants. Le témoin de 368 titres en vaut 3,21 : la diversification par le nombre est épuisée pour l'ensemble des survivants de l'indice, et le thème n'y est qu'un peu plus exposé.

**Risques extrêmes.** La VaR à 99 % est dépassée 1,4 à 1,8 fois trop souvent, et le test de Kupiec la rejette sur les vingt-cinq séries, `SPY` compris. Les dépassements arrivent en paquets.

*Calculs : `src/mesurer_risque.ipynb`, `src/robustesse_statistique.ipynb`, `src/construire_temoin.py`.*

## VII. Diversification par classes d'actifs

**Pourquoi des actifs extérieurs.** Puisque ajouter des entreprises ne diversifie plus, tout gain devait venir d'actifs qui ne suivent pas les actions. Chaque diversifiant est comparé aux liquidités à part égale : sans cette comparaison, une baisse de risque obtenue en vendant des actions serait attribuée à l'actif acheté.

**Les obligations du Trésor.** Jusqu'en 2021, elles ont été un vrai diversifiant. Leur corrélation avec `P1` vaut −0,33, elle devient plus négative en tension, et elles font mieux que les liquidités sur les vingt séries. En 2008, `P1` perd 50,0 % ; mêlé à 40 % d'obligations longues, il perd 25,9 %. Depuis 2022, la corrélation vaut +0,09, et le mélange obligataire est plus volatil que le mélange de liquidités sur les vingt séries. En 2022, `P1` avec 40 % d'obligations longues perd 23,1 %, davantage que `P1` seul, qui perd 19,7 %.

**Le risque de taux.** Il explique ce renversement. Les obligations longues amortissent le mieux une baisse des taux en crise, et souffrent le plus d'une hausse. Les obligations ont rapporté 3,97 % par an, deux points de plus que les bons du Trésor, pendant une période où le taux court est passé de plus de 6 % à presque zéro. Cet avantage ne peut pas se répéter depuis un niveau bas.

**Les actions hors du thème.** Elles ne protègent presque pas. À 40 % du portefeuille, elles réduisent la volatilité de 7,4 %, contre 41,0 % pour des liquidités. Leur corrélation avec `P1` vaut 0,90, et 0,92 en tension.

**Limites.** La sous-période depuis 2022 ne compte que 4,7 ans et un seul épisode de hausse des taux. L'or n'a pas été mesuré, faute de série couvrant toute la période.

*Calculs : `src/couvrir_diversifier.ipynb`, sections 5 à 9.*

## VIII. Couverture par dérivés

**Objectif économique.** Garder l'exposition au thème en transférant une partie de la perte.

**Contrats à terme sur l'indice.** Couvrir le bêta entier ramène celui de `P1` à 0,01 et sa volatilité de 21,73 % à 8,34 %, pour 0,19 point par an de frais. Les 8,34 % restants sont le risque que le marché n'explique pas. L'hypothèse que j'avais écrite, une mauvaise protection en 2000 à 2002, est contredite : `P1` y perd moins que le marché, 37,6 % contre 47,3 %, et la couverture termine l'épisode en gain. Son meilleur Sharpe mesure surtout l'écart entre l'univers de survivants et le marché, c'est-à-dire le biais de l'univers.

**Options de vente.** Les puts mensuels protègent des chutes rapides : en 2020, `P1` perd 17,7 % au lieu de 36,8 % avec des puts à 95 %. Ils ne protègent pas des baisses lentes. En 2000 à 2002, la perte passe de 37,6 % à 40,9 %, et le put à 90 % aggrave le repli maximal sur onze séries sur vingt.

**Coût de la protection.** C'est la question que je ne peux pas trancher. Un contrôle contre l'indice CBOE PutWrite montre que mon modèle surévalue les puts à la monnaie d'environ 3,8 points de volatilité, à rebours de ce que j'avais annoncé avant calcul. Pour `P1` avec des puts à 95 %, le coût annuel va de 7,3 points dans la base à 2,1 points dans la variante calibrée, et le Sharpe de 0,60 à 0,91.

**Nouveaux risques.** Les puts ajoutent un risque de base : ils protègent l'indice, pas le thème. Ils portent aussi un risque de prix, puisque leur coût dépend d'une volatilité implicite qui monte précisément en crise. Les contrats à terme ajoutent un risque de base et des appels de marge, non modélisés ici.

*Calculs : `src/couvrir_diversifier.ipynb`, sections 2 à 4, 8, 11 et le contrôle PutWrite.*

## IX. Stress tests et scénarios

Je n'ai pas construit de scénarios hypothétiques. Les six épisodes historiques en tiennent lieu, traités un par un, sans moyenne, parce qu'ils ne sont pas comparables.

**Choc technologique, 2000 à 2002.** Les maillons des puces y connaissent leur repli maximal, de 65 à 87 %. `P1`, qui mêle puces, électricité et énergie, perd 37,6 %, moins que le marché. L'électricité gagne 4,3 % quand le marché perd 47,3 %.

**Crise financière, 2007 à 2009.** C'est le pire épisode de presque toutes les stratégies. `P1` perd 50,0 %. Les obligations sont alors la meilleure protection parmi les actifs extérieurs.

**Choc de taux, 2022.** Actions et obligations tombent ensemble. Pour `P1` rééquilibré, c'est le seul des six épisodes où les liquidités protègent mieux que les obligations, et où les obligations longues aggravent la perte.

**Choc de volatilité, mars 2020.** Une chute d'un mois, du 19 février au 23 mars. C'est le cas où les puts mensuels jouent pleinement leur rôle.

**Pertes extrêmes.** Si la première ligne de `P1` rééquilibré perdait la moitié de sa valeur, le portefeuille perdrait 8,2 %, soit quatre fois et demie son exposition directe de 3,7 %, parce que les autres lignes bougeraient avec elle. Ce chiffre est un minorant, les bêtas venant d'une période normale.

*Calculs : `src/mesurer_risque.ipynb` et `src/couvrir_diversifier.ipynb`, section 8.*

## X. Comparaison des stratégies

**Concentré, diversifié, couvert.** À risque égal, c'est-à-dire face à un mélange de `P1` et de liquidités qui a exactement le même risque, seules les obligations du Trésor intermédiaires ajoutent de la valeur de façon robuste. Elles sont supérieures sur quatorze à dix-huit séries sur vingt, pour 0,7 point par an environ. Leur avantage s'amenuise d'une moitié de la période à l'autre, et s'inverse depuis 2022. La couverture complète par contrats à terme n'est supérieure sur aucune série, et sa valeur ajoutée médiane vaut −3,0 points. Les puts sont inférieurs sur les vingt séries dans la base, et jamais inférieurs dans la variante calibrée : leur verdict dépend d'un prix que je n'observe pas.

**Coût contre réduction du risque.** Par point de rendement abandonné, les obligations achètent 11 à 15 % de réduction de la perte extrême, les liquidités 8 à 9 %, les contrats à terme et les puts de la base 4 à 8 %. Je ne convertis pas ces rapports en classement unique.

**Le risque résiduel.** Une fois le marché couvert, ce qui reste de `P1` est encore plus concentré dans les puces : leur part du risque monte de 77 % à 82 % en gestion rééquilibrée, et de 84 % à 90,5 % en gestion conservée. Aucun instrument sur l'indice ne couvre ce qui distingue le thème du marché.

**Robustesse.** Chaque verdict est confronté aux deux moitiés de la période et au bootstrap. Les verdicts qui n'y survivent pas sont écrits comme indécidables, et ils sont majoritaires.

**P11.** J'ai ajouté un onzième portefeuille, construit en connaissance de ces résultats et présenté comme tel. Il détient 60 % d'actions du thème, pondérées par maillon à l'inverse de leur volatilité, 20 % d'obligations intermédiaires et 20 % de liquidités. Il fait ce qu'il annonce : les puces ne portent plus que 43,6 % du risque de ses actions, contre 65,9 % à poids égaux par entreprise. Mais son historique ne bat pas le simple mélange obligataire, avec un Sharpe de 0,90 contre 0,93, et cet historique ne prouve rien puisque la règle a été écrite après avoir vu les données. Son test est prospectif. Trois prédictions sont enregistrées pour les 252 séances qui suivent le 4 septembre 2026 (`research/portefeuilles.md`, section VII).

*Calculs : `src/comparer_strategies.ipynb`, `src/portefeuille_avenir.ipynb`.*

## XI. Discussion

**Interprétation économique.** Le risque de ce thème est celui des semi-conducteurs. L'électricité, l'immobilier et les matériaux, qui en font aussi partie, n'y contribuent presque pas en risque : ils l'absorbent. Élargir l'univers a dilué les poids sans diluer le risque. C'est ce qui explique à la fois que le thème ait mieux résisté que le marché en 2000 à 2002, grâce à ses passagers non technologiques, et que la couverture par l'indice laisse intact le cœur de son risque.

**Hypothèses confirmées ou rejetées.** L'hypothèse A est confirmée dans sa forme faible : les titres partagent un facteur commun, la diversification par le nombre est épuisée, et le risque est plus concentré que l'argent. Mais elle vaut presque autant pour tout le S&P 500 survivant, et ne distingue donc pas le thème. L'hypothèse B n'est pas testable avec ces données : les rendements élevés sont ceux de survivants, et le témoin en a presque autant. L'hypothèse C est confirmée pour les corrélations brutes, qui montent en tension dans les dix portefeuilles. La correction de Forbes et Rigobon ne permet ni de l'attribuer à une contagion propre au thème, ni de l'exclure. Parmi les hypothèses de l'étape 4, deux sont confirmées et une contredite.

**Implications pour l'investisseur.** Je ne formule pas de recommandation. Trois constats seulement. Un portefeuille équipondéré de ce thème est, en risque, un portefeuille de semi-conducteurs. Le laisser dériver concentre encore davantage le risque que l'argent. Et les instruments sur l'indice ne couvrent pas ce risque-là : seule la réduction de la place des puces le réduit.

**Limites.** Six limites portent sur l'ensemble. L'univers est connu de 2026, donc aucune performance n'est réalisable, et le rendement ne peut porter aucune conclusion. La revue de littérature n'est pas faite. Les prix d'option sont des prix de modèle, dont le niveau est incertain. Le témoin contient des faux négatifs de la sélection. Les covariances des décompositions par maillon ne portent que sur la dernière année. Enfin, les étapes 4 et 5 et P11 reposent sur des décisions déléguées, que l'auteur doit relire.

**Recherche future.** Trois chantiers restent ouverts : la revue de littérature, la mesure des degrés d'exposition des 134 entreprises, et le test prospectif de P11 et de la question principale du bloc 3 du Research Charter.

## XII. Conclusion

J'ai cherché à savoir ce que coûte, en risque, la concentration d'un portefeuille sur la chaîne des infrastructures de calcul liées à l'IA, et ce qu'on peut faire contre ce risque. La réponse tient en quatre phrases. Ce portefeuille est plus volatil que le marché et que le reste de l'indice, de façon établie, sans que son rendement supplémentaire soit distinguable du hasard ni du biais de survie. Son risque vient des semi-conducteurs, qui en portent les trois quarts avec moins de la moitié de l'argent. Ajouter des entreprises ne le diversifie plus, et couvrir le marché laisse intact ce qui le distingue du marché. Le seul moyen robuste de réduire ce risque a été d'en détenir moins, et, jusqu'en 2021 seulement, de le remplacer par des obligations du Trésor.
