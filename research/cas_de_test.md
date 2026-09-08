# Cas de test

*AI Concentration Risk Research. Tâche 49 de la phase 6. 8 septembre 2026.*

Ce document propose les cas qui doivent faire échouer le code. Il ne contient pas les tests eux mêmes, qui relèvent de la tâche 50.

Les cas couvrent des défauts déjà rencontrés et des échecs possibles. Un test de régression protège le cas qu'il reproduit ; il ne garantit pas toutes les variantes du défaut. Un contre-exemple utile n'a pas besoin d'avoir déjà causé une erreur dans les données réelles.

Les tests unitaires utilisent des données courtes, dont la réponse attendue peut être calculée indépendamment. Ils sont complétés par des contrôles d'intégration sur des fixtures et par le replay des fichiers du dépôt : ces contrôles vérifient d'autres propriétés, notamment les raccordements et la reproductibilité.

## I. Ce que le calcul des rendements doit refuser

**Cas 1, la ligne de remplissage.** Trois séances à volume nul dont les quatre cours sont identiques et égaux à la veille, suivies d'une séance réelle. Le rendement attendu est manquant sur les quatre lignes, et non nul sur les trois premières puis énorme sur la quatrième. Origine : `HUBB` au 31 octobre 1994, où le rendement calculé valait +885,9 %, découvert en cherchant l'origine de la plus forte variation du contrôle.

**Cas 2, la valeur absente.** Une séance dont tous les cours sont vides, entourée de séances normales. Le rendement attendu est manquant ce jour là et le lendemain, puisque le lendemain a besoin de la veille. Origine : `HUBB` au 8 août 1977, non détectée parce que le test d'origine comparait les prix à zéro et qu'une valeur manquante ne satisfait aucune comparaison.

**Cas 3, la division d'actions.** Deux séances encadrant une division de deux pour un, avec des cours déjà retraités par la source. Le rendement attendu est celui du marché, sans saut de facteur deux. Origine : le piège annoncé de la tâche 34, écarté avant d'avoir nui.

## II. Ce que la convention de dividende doit produire

**Cas 4, le détachement.** Un cours de 100 la veille, un dividende de 10 et un cours de 95 donnent une richesse de 105 pour une action détenue, soit un rendement de 5 %. La formule Yahoo multiplicative donne 95/90 − 1, soit environ 5,56 % : elle décrit un ajustement de série, pas le compte espèces du moteur. Le test appelle réellement le moteur. Un cours stable ou en hausse le jour du détachement reste possible.

**Cas 5, la trésorerie.** Un portefeuille de deux titres, un dividende détaché en mars, aucun rééquilibrage avant janvier suivant. La trésorerie attendue reste constante de mars à décembre, ne rapporte rien, et est réinvestie à la première séance de janvier. Origine : la tâche 28.

## III. Ce que la construction du portefeuille doit garantir

**Cas 6, la somme des poids.** Un portefeuille de trois titres après une dérive quelconque. La somme des poids des titres et de la trésorerie vaut un, à la précision de la machine. Origine : tâche 43.

**Cas 7, l'entrée d'un titre.** Un portefeuille de deux titres auquel un troisième s'ajoute en cours de période. Le poids attendu du nouveau est celui d'un tiers, les deux autres sont réduits proportionnellement, et la valeur totale ne bouge pas, hors frais. Aucun poids ne lui est attribué avant sa première cotation. Origine : tâches 27 et 45.

**Cas 8, le raccordement quotidien.** Le rendement avant frais est la somme des rendements de prix et des dividendes, pondérée par les positions de la veille ; la trésorerie a un rendement nul. Les frais sont ensuite déduits. Cette identité vaut aussi à un rééquilibrage, car le réinvestissement ne crée pas de valeur. Une borne entre le meilleur et le pire rendement doit inclure les dividendes et les espèces ; les frais peuvent placer le net sous la borne brute.

**Cas 9, l'identité d'agrégation.** Sans frais, avec les mêmes dates d'investissement, des poids initiaux égaux et aucune opération divergente ensuite, le mélange des sous-groupes selon leurs effectifs reproduit l'univers complet. Le test protège ce cas restreint. Les entrées différées, les frais et les rééquilibrages propres aux groupes empêchent d'en faire une preuve générale de la simulation.

**Cas 10, l'entreprise à deux classes d'actions.** Une entreprise cotée sous deux symboles dans un portefeuille de trois entreprises. Le poids attendu de l'entreprise est un tiers, réparti par moitié entre ses deux lignes, et non deux tiers. Origine : Alphabet, `GOOG` et `GOOGL`.

## IV. Ce que la collecte doit refuser

**Cas 11, la réponse vide.** Une source qui renvoie un dictionnaire vide sans lever d'erreur. Le code doit compter un échec, pas un succès. Origine : la première version de la tâche 18, qui annonçait 118 titres décrits pour 117 réels parce que `BRK.B` interrogé au lieu de `BRK-B` renvoyait un dictionnaire vide.

**Cas 12, la réponse hors sujet.** Une description complète peut désigner un instrument différent. Il faut vérifier le symbole, le type attendu, la devise et le raccordement au fichier ; une date de première transaction seule ne prouve pas l'identité. Le contrôle local attend ETF pour SPY et RSP, INDEX pour les trois indices, EQUITY pour les actions.

**Cas 13, le filtre appliqué à la mauvaise population.** Un indice dont toutes les séances portent un volume nul. Le filtre de remplissage ne doit pas s'y appliquer et la série doit survivre entière. Origine : la première version de la tâche 41, qui effaçait `^SP500TR` et `^SPXEW` en totalité, la première disparaissant du tableau sans message.

## V. La règle qui traverse les cas 11, 12 et 13

Les trois viennent du même défaut de conception : **vérifier l'absence de l'échec imaginé au lieu de vérifier la présence du succès attendu.** Le cas 2 en est la version sur les données.

Un test de collecte ne doit donc jamais s'écrire « aucune erreur n'a été levée ». Il doit s'écrire « le résultat contient ce qu'il doit contenir ».

## VI. Les contre-exemples ajoutés lors de l'audit

Je vérifie l'entrée en cours d'année dans les deux versions, le financement des achats par les ventes et les espèces, le coût des deux côtés, et le partage d'une entreprise entre classes. Une perte totale ne doit jamais être suivie d'une remise à un de la valeur sans apport. Une cible négative, absente, non finie ou désalignée doit être refusée, tout comme un rendement inconnu sur une position détenue.

Je distingue un rendement observé manquant d'une valorisation portée. Sur des cours 100, absent, 121, 133,1, le trou ne doit pas faire perdre le mouvement de 100 à 121 ; aucun cours n'est cependant porté avant une introduction. Un volume nul avec des prix variables n'est pas assimilé au même cas qu'un segment plat. Les indices à volume nul gardent leur historique.

Les identités de richesse et de frais sont vérifiées dans le journal quotidien de chaque série. Un calcul séparé en nombres de parts reproduit SPY ; une variante conserve les créances jusqu'au paiement officiel pour mesurer la limite du réinvestissement au détachement. Cette sensibilité ne remplace pas la collecte des dates de paiement des actions.

Les acquisitions réseau ne sont pas rejouées sur le cliché protégé. Le carnet de collecte bloque une collecte ordinaire quand le manifeste existe, et sa cellule qui supprimait les CSV a été retirée. Ce verrou ne transforme pas le carnet historique en un collecteur de production entièrement testé.
