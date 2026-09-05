# Règle de sélection de l'univers d'investissement

*AI Concentration Risk Research. Version II, 4 septembre 2026.*
*Remplace la version I du même jour, dont le journal des amendements figure en partie XII.*

---

## I. Pourquoi une deuxième version

La première version reposait sur une idée simple : les entreprises engagées dans l'IA investissent beaucoup, donc je classe les cinq cents entreprises de l'indice par intensité d'investissement et je retiens les plus élevées.

Cette idée ne fonctionne pas, pour deux raisons que j'expose ici parce qu'elles expliquent tout le reste du document.

**Première raison : un chiffre ne dit pas à quoi sert l'argent.** American Water Works investit 61 % de son chiffre d'affaires. C'est pour des canalisations d'eau potable. Microsoft en investit 35 %, et c'est pour des centres de données. Le classement par intensité d'investissement met la compagnie des eaux devant. Il mesure à quel point un métier est gourmand en capital, ce qui est une caractéristique permanente des services aux collectivités, des foncières et des chemins de fer. Il ne mesure pas l'intelligence artificielle.

**Deuxième raison : l'investissement n'est qu'un canal d'exposition parmi plusieurs.** Une entreprise peut être exposée parce qu'elle dépense, parce qu'elle vend, ou parce qu'elle fournit ceux qui vendent. En ne retenant que la dépense, je fabriquais un univers d'acheteurs et je laissais dehors toute la chaîne d'approvisionnement.

La finalité de l'argent n'est pas dans les comptes. Elle est dans le texte du rapport annuel, où les entreprises écrivent elles mêmes pourquoi elles investissent et de quoi dépend leur activité. C'est cette information que la version I n'utilisait pas.

---

## II. Ce que je cherche

Une liste d'entreprises du S&P 500 dont l'activité dépend du fait que l'argent continue d'affluer vers l'infrastructure de calcul liée à l'intelligence artificielle.

Pour chacune, je veux son rôle dans cette chaîne, la part de son activité réellement concernée, et la phrase de son propre rapport annuel qui justifie sa présence.

---

## III. Le critère unique

Toute la sélection repose sur une seule question, posée à chaque entreprise :

> **Si l'investissement en intelligence artificielle s'arrêtait demain, cette entreprise perdrait-elle de l'argent ?**

Si la réponse est oui, elle entre. Sinon, elle sort.

Ce critère a trois qualités qui m'ont fait l'adopter.

Il absorbe l'exposition directe et l'exposition indirecte sans distinction artificielle. Peu importe qu'une entreprise construise, vende ou fournisse : ce qui compte est qu'elle soit du même côté du choc.

Il exclut proprement les entreprises qui se contentent d'utiliser l'IA comme outil interne. Une banque qui déploie un assistant automatique ne perdrait rien si l'investissement s'arrêtait, elle économiserait même des dépenses.

Et surtout, il correspond exactement à l'objet de la recherche. Ce que je veux étudier, c'est un portefeuille dont toutes les lignes plongeraient ensemble pour la même raison. Le critère sélectionne donc directement sur ce qui fait la concentration du risque.

---

## IV. Les quatre canaux d'exposition

**Elle dépense.** Elle construit des capacités de calcul et immobilise du capital aujourd'hui contre des revenus espérés demain. Grandes plateformes cloud. Elle perdrait du capital engagé pour rien. **Elle entre.**

**Elle vend.** Ses produits sont achetés parce que d'autres investissent. Semi-conducteurs, serveurs, équipements réseau. Elle perdrait son chiffre d'affaires. **Elle entre.**

**Elle fournit la chaîne.** Elle ne vend pas d'IA mais elle vend à ceux qui en vendent, ou elle fournit ce sans quoi rien ne fonctionne : l'électricité, le refroidissement, la construction des sites, les composants électriques, l'immobilier des centres de données. Même choc, avec un cran de décalage. **Elle entre.**

**Elle utilise, ou elle est menacée.** Elle déploie l'IA en interne, ou son métier risque d'être remplacé par elle. Ces deux situations sont différentes l'une de l'autre, mais elles ont un point commun décisif : ces entreprises ne perdraient rien si l'investissement s'arrêtait. Les secondes y gagneraient un sursis. **Elles sortent.**

---

## V. Pourquoi le texte d'abord et les chiffres ensuite

Le texte dit le **pourquoi**. Les chiffres disent le **combien**.

Le texte seul ne suffit pas, parce que déclarer n'est pas faire. Une entreprise peut annoncer une ambition en intelligence artificielle sans que rien ne bouge dans ses comptes.

Les chiffres seuls ne suffisent pas, c'est la leçon de la version I.

Une entreprise entre donc si les deux concordent : elle déclare une dépendance à l'infrastructure de calcul, et ses comptes montrent que quelque chose a effectivement bougé. Quand les deux se contredisent, le cas est signalé et tranché à la main, avec la justification écrite.

---

## VI. Le filet de termes, et pourquoi le mot évident est le pire

Le repérage se fait sur une liste de termes cherchés dans le texte intégral du dernier rapport annuel.

Le terme le plus évident, « intelligence artificielle », est aussi le plus trompeur, et j'en ai la démonstration.

Eaton, fabricant d'équipements électriques, mentionne quatre fois l'intelligence artificielle dans son rapport. Les quatre mentions parlent d'efficacité interne et de risques juridiques liés à l'IA générative. Ce sont des mentions du quatrième canal, celles qui font sortir une entreprise.

Le même rapport mentionne vingt-quatre fois les centres de données, et décrit quatre acquisitions faites pour ce marché : des modules électriques, du refroidissement liquide, des transformateurs, des solutions modulaires pour clients hyperscale. Eaton est fortement exposée, et c'est le vocabulaire du métier qui le révèle, pas le mot à la mode.

Chercher « intelligence artificielle » seul m'aurait fait exclure Eaton pour la mauvaise raison.

Le filet doit donc contenir le vocabulaire opérationnel : centre de données sous ses différentes orthographes, hyperscale, calcul accéléré, apprentissage automatique, processeur graphique, refroidissement, infrastructure cloud, calcul haute performance. Ce sont les mots de ceux qui construisent, pas de ceux qui commentent.

La liste exacte est dans le code, et elle peut être complétée si un cas montre qu'elle laisse passer quelque chose. Toute modification est datée.

---

## VII. La procédure

**Première étape.** Pour chacune des cinq cents entreprises, je récupère le texte intégral de son dernier rapport annuel et je compte les occurrences de chaque terme du filet.

**Deuxième étape.** Les entreprises n'affichant aucune occurrence sur aucun terme sortent définitivement. American Water Works, première du classement d'investissement de la version I, affiche zéro partout. Cette étape est mécanique et ne demande aucun jugement.

**Troisième étape.** Pour les autres, j'extrais les phrases contenant ces termes, avec leur contexte. Une page de phrases par entreprise, au lieu d'un document de quatre cents pages.

C'est cette étape qui rend le reste possible. Promettre de lire quarante rapports annuels serait une promesse creuse. Lire quarante pages de phrases extraites ne l'est pas.

**Quatrième étape.** Lecture de ces phrases, et réponse à la question de la partie III. Le cas Eaton montre que quatorze phrases suffisent à trancher, et à trancher mieux qu'une lecture rapide du document entier.

**Cinquième étape.** Corroboration par les comptes déjà collectés. L'investissement ou la recherche ont-ils réellement bougé par rapport au passé de l'entreprise elle même. Le passé de chaque entreprise sert de référence à elle même : la compagnie des eaux se compare à la compagnie des eaux, pas à Microsoft.

**Sixième étape.** Consignation, entreprise par entreprise, de la décision et de son motif.

---

## VIII. Ce que je consigne pour chaque entreprise retenue

Le canal d'exposition parmi les quatre. Le degré, activité entièrement ou partiellement concernée. La phrase du rapport qui a emporté la décision, avec la référence du dépôt. Le mouvement observé dans les comptes, ou l'absence de mouvement. Le secteur officiel, à titre descriptif uniquement.

Le degré ne sert pas à exclure. Il servira à expliquer les résultats, quand deux entreprises du même canal ne réagiront pas de la même façon à un même choc.

---

## IX. Conventions de données

Ces règles ont été établies en construisant la collecte, et plusieurs viennent d'erreurs constatées.

**Rattachement des exercices.** Toutes les entreprises ne clôturent pas au 31 décembre. Sur les cinq cents, cent trente ne le font pas. Un exercice est rattaché à l'année civile où il a passé le plus de temps, donc une clôture entre janvier et mai est rattachée à l'année précédente. Comparer des années civiles sans regarder les dates fausserait un quart de l'indice sans qu'aucune erreur n'apparaisse.

**Datation des valeurs.** Les champs d'exercice de la base SEC désignent l'année du rapport où une valeur figure, non l'année à laquelle elle se rapporte, puisqu'un rapport annuel contient les exercices précédents en comparatif. On se fie uniquement à la date de clôture réelle de la période.

**Changements d'étiquette comptable.** Une entreprise peut déclarer la même notion sous des noms différents selon les années. Nvidia change de nom pour son chiffre d'affaires en 2021. Toutes les étiquettes sont donc fusionnées année par année.

**Choix du chiffre d'affaires.** Une entreprise peut publier plusieurs lignes de revenus dont l'une n'est qu'une partie de l'autre. C'est le cas de cent quarante-deux entreprises sur quatre cent quatre-vingt-seize. Une foncière encaisse des loyers et un assureur des primes, qui ne sont pas des ventes à des clients et n'apparaissent donc pas sous l'étiquette correspondante. La règle retenue est le maximum des étiquettes de revenu net, en écartant celle qui inclut les taxes collectées, sauf si c'est la seule disponible. Les justifications et les contre-exemples sont dans le code.

**Données manquantes.** Jamais estimées, jamais comblées. L'entreprise est marquée non évaluable et figure dans la liste des cas signalés.

**Classes d'actions multiples.** Une entreprise compte pour une entreprise. Trois sociétés de l'indice sont concernées : Alphabet, Fox et News Corp. Les lignes sont regroupées et les poids additionnés.

**Aucune décision dans les données brutes.** Le fichier brut conserve toutes les étiquettes trouvées. Les choix sont faits à l'étape de traitement, où ils sont visibles et documentés.

---

## X. Ce que je m'interdis

La performance boursière passée, sous toutes ses formes. Sélectionner les entreprises dont le cours a monté, puis observer qu'elles ont bien performé, ne démontrerait rien.

La capitalisation comme critère : elle mesure la taille.

Le secteur officiel comme filtre : trois des entreprises les plus concernées ne sont pas classées dans la technologie, et une partie de l'infrastructure de calcul relève de l'immobilier, des services aux collectivités et de l'industrie. Le secteur reste conservé comme information descriptive, et l'étalement de l'univers final sur plusieurs secteurs constituera un résultat.

La notoriété.

Une liste publiée par un tiers comme point de départ. Décision prise après examen : une telle liste contiendrait des sociétés étrangères, notamment taïwanaises et néerlandaises, alors que le périmètre retenu est strictement américain. Une liste institutionnelle pourra servir de comparaison en fin de parcours, jamais de source.

---

## XI. Les limites

**Le périmètre est amputé.** Partir du S&P 500 exclut des entreprises centrales dans la chaîne, en particulier en fabrication de semi-conducteurs et en équipement de gravure, qui ne sont pas cotées aux États-Unis. C'est une décision assumée, justifiée par le fait que l'investisseur étudié détient des actions américaines et par l'homogénéité des données. Elle doit être écrite dans le rapport, pas subie.

**La composition de l'indice change.** La liste utilisée est celle d'une date donnée, et les entreprises sorties de l'indice n'y figurent pas. Toute analyse rétrospective en portera la trace.

**Le chiffre d'affaires attribuable à l'intelligence artificielle n'existe pas comme donnée normalisée.** Aucune norme comptable ne l'impose ni ne le définit.

**La lecture comporte une part de jugement**, et cette part est irréductible. Elle est rendue contestable, et donc acceptable, par la consignation d'une phrase justificative par entreprise. Un lecteur en désaccord peut aller lire la même phrase.

**Le filet de termes peut laisser passer une entreprise** qui serait exposée sans employer aucun de ces mots. Le risque est réduit par l'usage du vocabulaire opérationnel plutôt que du seul mot à la mode, mais il n'est pas nul.

**L'exposition économique n'est pas l'exposition boursière.** Ce document sélectionne sur les faits économiques. La façon dont ces actions se comportent réellement en bourse sera mesurée ensuite, et séparément. Si une entreprise retenue ne se comporte pas comme les autres, ce ne sera pas un défaut de la sélection mais un résultat, et un résultat intéressant.

---

## XII. Journal des amendements

**A-01. Abandon du filtre par intensité d'investissement.**
La version I retenait le premier quintile d'intensité d'investissement, avec la croissance en condition secondaire. Motif de l'abandon : l'indicateur mesure le caractère capitalistique d'un métier, pas l'exposition à l'IA.
*Honnêteté requise : cet amendement a été décidé après avoir observé le haut du classement, qui était composé de compagnies des eaux, de gaz et d'électricité. Je n'étais donc plus aveugle. La justification tient toutefois sans les données, une compagnie des eaux investissant lourdement depuis toujours. Le lecteur peut juger lui-même si l'argument suffit.*

**A-02. Deux filtres au lieu d'un, puis abandon des deux.**
La version I avait déjà dû prévoir un critère distinct fondé sur la recherche, parce qu'une partie des fournisseurs ne possède pas d'usines et affiche donc un investissement faible. Ce correctif est devenu sans objet avec l'amendement A-01, mais le constat reste vrai et explique pourquoi les chiffres ne peuvent pas sélectionner seuls.

**A-03. Règle de choix du chiffre d'affaires.**
Ajoutée après un contrôle manuel qui a révélé un écart entre deux étiquettes chez Vistra. Le problème touchait cent quarante-deux entreprises, avec des écarts allant jusqu'à quatre-vingt-seize pour cent. Non corrigé, il aurait placé des foncières et des opérateurs de tours télécom en tête du classement.

**A-04. Le texte devient le critère principal.**
Motivé par une objection de fond : un ratio ne dit pas à quoi sert l'argent, et l'exposition ne se réduit pas à l'investissement.

**A-05. Le filet de termes ne repose pas sur le mot « intelligence artificielle ».**
Motivé par le cas Eaton, où ce mot conduit à la conclusion inverse de la réalité.

**A-06. Abandon du premier critère de corroboration. 5 septembre 2026.**
Le critère demandait si les dépenses avaient crû plus vite que l'activité, l'idée étant de neutraliser la croissance ordinaire. Il fonctionne pour les entreprises qui construisent : Oracle multiplie son investissement par 33 pendant que son chiffre d'affaires fait 1,7. Il échoue pour celles qui vendent : Nvidia, dont le chiffre d'affaires a été multiplié par vingt, ressortait « non confirmée » parce que ses ventes avaient crû plus vite encore que sa recherche. En divisant par la croissance du chiffre d'affaires, on efface le signal que l'on cherche. Un vendeur voit son exposition dans ses ventes, un constructeur dans ses dépenses engagées en avance.
*Amendement décidé après observation des résultats.*

**A-07. Abandon du second critère, et fin des ajustements. 5 septembre 2026.**
Le critère avait alors été rendu dépendant du canal d'exposition. Il classait Vertiv, qui a triplé son chiffre d'affaires et quadruplé son investissement, en « non confirmée », parce que le canal « fournit » mélange des vendeurs d'équipements, dont la preuve est le chiffre d'affaires, et des infrastructures régulées, dont la preuve est la dépense.

Une troisième correction aurait été défendable sur le fond. Elle n'a pas été faite, et c'est une décision de méthode : ajuster une règle jusqu'à ce que les entreprises auxquelles on croit la passent revient à fabriquer un résultat au lieu de le mesurer. C'est le biais que la partie I de ce document interdit.

La corroboration a donc cessé d'être un examen que l'on réussit ou que l'on rate, pour devenir une mesure à trois niveaux dont les bornes ne se négocient pas : aucun mouvement quand les deux multiples sont inférieurs ou égaux à 1, mouvement net quand l'un atteint 2, mouvement modéré entre les deux. Aucune entreprise n'est retirée de l'univers par cette étape. Le détail figure dans la note sur l'univers retenu.

---

## XIII. Contrôle de qualité

Deux contrôles distincts, qui ne servent pas à la même chose.

**Le contrôle manuel.** Trois entreprises tirées au sort, dont les valeurs sont comparées à leurs documents officiels. Il vérifie que la chaîne de récupération fonctionne. Il ne prouve rien sur les autres, et c'est précisément un tel contrôle qui a révélé l'erreur ayant conduit à l'amendement A-03.

**Le contrôle automatique.** Des tests appliqués aux cinq cents entreprises, portant sur ce que la réalité économique ne permet pas : investir plus que son chiffre d'affaires durablement, dépenser plus de la moitié de son chiffre d'affaires en recherche, voir son chiffre d'affaires tripler puis s'effondrer, avoir un trou au milieu de sa série.

Ces tests ne prouvent pas l'absence d'erreurs : une valeur fausse mais vraisemblable passe au travers. Ils garantissent seulement qu'il ne reste pas d'aberration. Une alerte n'est d'ailleurs pas une erreur, la plupart de celles constatées correspondaient à des faits économiques réels, l'effondrement du transport aérien et des croisières en 2020 par exemple.

**Règle générale du projet.** Un chiffre qui n'existe que dans une conversation n'existe pas. Seul un chiffre présent dans un fichier, accompagné de sa source, peut entrer dans le rapport.
