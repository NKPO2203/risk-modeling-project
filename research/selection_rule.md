# Règle de sélection de l'univers de recherche

*AI Concentration Risk Research. Version III, 5 septembre 2026.*
*Les versions précédentes sont conservées dans `research/archive/2026-09-05_avant_corrections/`.*

## I. Pourquoi j'ai repris la règle

Je voulais repérer des entreprises exposées à un même mécanisme économique. Ma première tentative partait de l'intensité d'investissement. Elle mesurait surtout à quel point un métier consomme du capital. Une entreprise qui entretient un réseau d'eau pouvait remonter devant un fournisseur de matériel de calcul, sans être plus exposée à l'IA.

J'ai donc commencé à lire ce que les entreprises disent de leurs investissements et de leurs débouchés. Ce déplacement reste justifié. Mais il ne suffisait pas à rendre toute la méthode correcte. La lecture n'avait pas été menée de façon uniforme, certaines exclusions étaient attribuées par défaut et plusieurs comparaisons comptables mélangeaient des périodes ou des activités différentes.

Cette troisième version corrige ces problèmes. Je conserve le raisonnement économique, mais je précise ce qui permet de retenir une entreprise, ce que les comptes permettent d'observer et ce qui reste à démontrer.

## II. Ce que je construis à ce stade

Je construis un univers de recherche à partir de la composition du S&P 500 enregistrée dans le dépôt. J'y cherche les entreprises ayant une activité ou un engagement concret dans la chaîne des infrastructures de calcul liées à l'IA : capacités de calcul, équipements, composants, énergie, refroidissement, construction et immobilier nécessaires à cette chaîne.

Cet univers est un ensemble d'entreprises dans lequel je pourrai ensuite construire et comparer plusieurs portefeuilles. Il ne fixe ni le nombre de lignes d'un futur portefeuille, ni ses poids, ni une promesse de performance. Il ne prétend pas recenser toutes les entreprises qui développent ou utilisent de l'IA.

Le périmètre est l'appartenance à l'indice dans le fichier utilisé. Ce n'est ni une définition de la nationalité, ni la liste de toutes les entreprises cotées aux États-Unis. La composition locale provient d'une source secondaire ; sa concordance complète avec une composition officielle datée reste à établir.

## III. La question économique et la règle observable

Ma question de départ était : « Si l'investissement en IA s'arrêtait demain, cette entreprise perdrait-elle de l'argent ? »

Cette question aide à réfléchir, mais elle ne constitue pas une observation. Un arrêt des nouvelles commandes, une annulation de contrats et une baisse d'utilisation des installations existantes ne sont pas le même choc. Les effets dépendent aussi des contrats, de la régulation, du financement et des autres activités de l'entreprise.

Je retiens donc une entreprise lorsque son rapport documente au moins l'un des deux éléments suivants :

- une activité existante dans la chaîne : produits vendus, services fournis, installations exploitées, clients ou commandes identifiés ;
- un engagement concret : investissement engagé, chantier identifié ou accord documenté portant sur cette chaîne.

Une simple intention de se positionner, une opportunité de marché générale ou la présence du mot « IA » ne suffit pas. Si le texte ne permet pas de distinguer une activité réelle d'une possibilité, le cas reste douteux.

Le lien avec l'IA peut être explicite ou passer par les infrastructures de calcul. Dans ce second cas, je signale la limite : un centre de données accueille aussi des usages qui ne relèvent pas de l'IA. Je ne transforme pas son chiffre d'affaires total en chiffre d'affaires IA.

La même exigence s'applique aux industriels, aux producteurs d'électricité, aux équipementiers et aux entreprises technologiques. Le secteur n'allège pas le niveau de preuve.

## IV. Les décisions possibles

**ENTRE.** Une pièce documentaire permet d'établir une activité ou un engagement répondant au périmètre.

**SORT.** Les passages examinés documentent un usage interne, une offre située hors du périmètre technique retenu ou un autre motif explicite d'exclusion. Cette conclusion reste limitée au dossier examiné ; elle ne prouve pas l'absence universelle de tout lien à l'IA.

**DOUTEUX.** Le lien est plausible, mais sa nature, sa maturité ou son rapport à l'infrastructure n'est pas suffisamment établi.

**A_EXAMINER.** Le rapport manque, la revue manque ou la preuve ne correspond plus au corpus utilisé.

L'absence de décision ne devient jamais une exclusion. L'absence de mot repéré ne devient pas non plus une preuve d'absence d'exposition.

## V. Le canal, la maturité et le degré

Le canal décrit le rôle de l'entreprise : elle dépense, elle vend, elle dépense et vend, ou elle fournit la chaîne. Ce classement aide à expliquer le mécanisme ; il ne prédit pas un rendement.

Je distingue ensuite une activité déjà présente d'un engagement et d'une exposition seulement prospective. Cette maturité ne doit pas être confondue avec la taille de l'exposition.

Le degré décrit la part concernée seulement si la preuve permet de l'étayer. Une mention du marché des centres de données ne permet pas de conclure à une exposition « forte ». Lorsque cette part n'est pas isolée, je note `non_quantifie`. Je ne fabrique pas un pourcentage ni un poids de portefeuille à partir d'un adjectif.

Une banque qui finance un projet, un gestionnaire qui détient des participations et une filiale qui construit effectivement ses équipements ne jouent pas le même rôle. Une simple exposition financière n'entre pas automatiquement dans le périmètre technique défini ici.

## VI. Ce que le texte permet et ne permet pas

Le filet de recherche inclut le vocabulaire des métiers : centres de données, hyperscale, processeurs graphiques, calcul accéléré, apprentissage automatique, refroidissement et infrastructure cloud. La liste exacte est conservée dans le code.

Les occurrences servent à organiser le travail. Le classement est reproductible : nombre de termes actifs, puis occurrences, puis densité, puis CIK pour départager les égalités. Le sigle isolé « AI » reste extrait mais n'ordonne pas le classement, car il produit des ambiguïtés.

Je ne sélectionne pas les premiers rangs. Tous les CIK du fichier de composition restent dans la table de revue, y compris ceux sans rapport ou sans décision.

L'extraction conserve le contexte et ne s'arrête plus après quarante passages. Les rapports archivés, leurs identifiants, les textes extraits et les empreintes permettent de revenir à la pièce utilisée. Une erreur de téléchargement demeure une erreur visible ; elle ne doit pas produire un fichier donnant l'impression d'être complet.

Lire les passages repérés n'est pas lire intégralement cinq cents rapports. Le registre indique le périmètre de la revue et ses limites. Un cas ambigu appelle une lecture plus large du rapport, pas une affirmation plus catégorique.

## VII. Une décision doit pouvoir être retrouvée

Le CIK identifie l'entreprise. Le rang textuel est seulement un ordre de lecture : s'il change, la décision ne doit pas passer à une autre entreprise.

Le registre `data/review/decisions_selection.csv` conserve le verdict, le canal, la maturité, le degré, le motif, la phrase décisive, le dépôt SEC, son URL et les limites de la preuve.

Le programme vérifie que la citation appartient au bon CIK et au dépôt indiqué dans le corpus courant. Si cette preuve n'est plus retrouvée après une actualisation, la décision initiale reste visible, mais le statut appliqué redevient `A_EXAMINER`. Une actualisation documentaire peut donc réduire temporairement l'univers utilisable : c'est une demande de revue, pas un changement économique démontré.

## VIII. Pourquoi les comptes viennent ensuite

Le texte documente le mécanisme. Les comptes décrivent l'évolution de l'entreprise, sous réserve de leur comparabilité.

J'avais écrit que les chiffres confirmaient l'exposition à l'IA. C'était trop fort. Une hausse des ventes, des investissements ou de la recherche peut venir des prix, d'une acquisition, d'une activité différente ou du cycle économique. Elle ne mesure pas la contribution propre de l'IA.

La corroboration conserve son nom de fichier pour la continuité du projet, mais elle devient une **description comptable**, indépendante du verdict de sélection. Une croissance ne fait pas entrer une entreprise. Une baisse ne la fait pas sortir. Des données absentes n'annulent pas une exposition documentée.

## IX. Comment je rends les comptes comparables

Je conserve les valeurs brutes et leurs étiquettes. Le traitement choisit une notion et enregistre sa source, sa période, son statut de qualité et son périmètre.

Deux étiquettes ne deviennent pas équivalentes parce que l'une donne un chiffre plus élevé ou parce que leurs montants sont proches. Une dépense de construction et une acquisition d'installations sont deux notions différentes. Les divergences non rapprochées sont signalées ; elles ne servent pas à fabriquer un multiple. La tolérance numérique est de 0,01 dollar, pour éviter un écart de représentation informatique. Le seuil de 5 % conservé dans un contrôle d'alerte ne valide aucune équivalence comptable.

Un exercice est identifié par ses dates réelles. L'année affichée correspond à l'année civile contenant le plus de jours de la période ; elle ne remplace jamais les dates de début et de fin. Deux clôtures distinctes peuvent recevoir la même année majoritaire. Je conserve donc une ligne par CIK et date de clôture, au lieu d'écraser l'un des deux exercices. Le champ d'année du dépôt SEC ne suffit pas à dater les chiffres comparatifs qu'il contient.

Je privilégie les valeurs publiées les plus récemment dans le jeu de données. Cela peut intégrer des retraitements postérieurs : c'est approprié pour cette description actuelle, mais cela ne reconstitue pas l'information connue à une date historique.

Les scissions et acquisitions sont traitées mesure par mesure. Des ventes retraitées sur les activités poursuivies ne rendent pas automatiquement les anciens flux d'investissement comparables. Chaque exception doit être sourcée dans `data/review/`.

Une valeur manquante reste manquante. Un complément trouvé dans un document officiel est permis, avec son montant, son libellé, sa période et sa source ; ce n'est pas une estimation. Les données `companyfacts` ne couvrent pas tous les faits personnalisés ou ventilés des rapports. Voir la [documentation de la SEC](https://www.sec.gov/search-filings/edgar-application-programming-interfaces).

Le statut « comparable » signifie que la mesure passe les règles de rapprochement déclarées dans ce traitement. Il ne signifie pas qu'un audit exhaustif de toutes les opérations de chaque entreprise a été réalisé.

## X. La comparaison avec le passé

Je prends le dernier exercice disponible de l'entreprise par date de clôture, sous réserve que cette clôture soit au moins en 2024, puis je traite séparément les ventes, l'investissement et la recherche. Je ne complète pas un poste récent absent avec un ancien exercice en le présentant comme actuel.

La référence proposée reste 2017–2019 selon l'année majoritaire, avec au moins deux exercices admissibles. Une observation doit se terminer avant le début de l'exercice récent, être utilisable et appartenir au même périmètre comptable.

Si cette référence n'est pas disponible, je prends les deux premiers exercices admissibles strictement antérieurs à l'exercice récent, sans chevauchement. Ce repli est signalé pour chaque mesure, avec les dates réellement utilisées et les sources. S'il reste moins de deux exercices, le multiple n'est pas calculé. Deux exercices restent deux observations même si leur étiquette d'année majoritaire est identique.

Une base nulle ou négative ne permet pas ce multiple de croissance. Une base plus tardive n'entraîne pas nécessairement un multiple plus faible : cela dépend du parcours de l'entreprise.

Les multiples sont nominaux. Des références différentes et des horizons différents empêchent de les lire comme un classement pur de vitesse de croissance.

## XI. Le mouvement et la couverture

Je conserve les trois multiples séparés. Le résumé indique si une mesure disponible a doublé, si une progression reste inférieure au seuil, ou si les mesures disponibles stagnent ou reculent.

À côté, une autre information décrit la couverture : trois mesures comparables, observation partielle ou aucune comparaison. Une seule mesure en recul ne permet pas d'écrire que toute l'entreprise recule ; deux dépenses absentes ne valent pas deux zéros.

Le doublement est une convention descriptive. Ce n'est pas un test statistique et ce n'est pas une preuve d'exposition. Le fichier de sensibilité montre aussi les seuils 1,5 et 2,5, sans choisir celui qui donnerait le résultat le plus favorable.

Les méthodes de corroboration ont changé après observation des résultats. La méthode actuelle est donc exploratoire. Je documente cette évolution au lieu d'écrire que des bornes fixées après exploration auraient supprimé le risque d'ajustement aux données.

## XII. Ce que je ne peux pas encore conclure

La sélection ne démontre pas que les cours baisseraient ensemble. C'est une hypothèse qui demandera des rendements, des portefeuilles définis et une analyse de dépendance.

Exclure un éditeur de logiciels du périmètre ne signifie pas qu'il bénéficierait d'un ralentissement de l'IA. Sa demande, ses coûts et sa valorisation pourraient réagir dans des directions différentes.

Le fichier actuel de composition, les derniers rapports et les comptes retraités ne forment pas un univers historique disponible sans anticipation. Une étude de performance passée devra traiter les entrées et sorties de l'indice, les dates de publication, les opérations sur titres, les devises et les prix ajustés avant de parler de stratégie investissable.

Je n'utilise ni la performance passée, ni la notoriété, ni le secteur comme critère d'entrée. Je n'interprète pas non plus le nombre d'entreprises retenues comme une mesure de diversification effective.

## XIII. Pourquoi les amendements restent visibles

A-01 à A-05 ont déplacé la sélection des ratios d'investissement vers les mécanismes documentés et le vocabulaire opérationnel.

A-06 et A-07 ont modifié la corroboration après observation de cas qui contredisaient les premiers classements. Il s'agit bien de plusieurs méthodes successives. Le passage à des catégories descriptives est lui-même une modification, même s'il cesse d'exclure des entreprises.

La version III ajoute une revue explicite par CIK, des preuves vérifiables, une extraction sans plafond arbitraire, des rapprochements comptables par notion et par périmètre, des références propres à chaque mesure et une séparation entre mouvement et couverture.

Le journal détaillé des erreurs constatées et des corrections se trouve dans `research/corrections_2026-09-05.md`. Les anciens documents et données sont archivés pour que l'évolution soit contrôlable.

## XIV. Les contrôles

Les tests vérifient notamment qu'un changement de rang ne transfère pas une décision, qu'une preuve manquante bloque son application et qu'une référence comptable n'inclut pas l'année qu'elle est censée comparer.

Les alertes de vraisemblance repèrent les ruptures, les lacunes et les ratios inhabituels. Investir davantage que ses ventes peut être réel : une alerte demande une explication, elle ne prouve pas une erreur.

Inversement, une valeur plausible peut être fausse. Les tests et les rapprochements connus ne garantissent pas l'absence de toute erreur. Je conserve donc les limites et les cas non résolus avec les résultats.

Ma règle demeure : un chiffre utilisé dans le rapport doit pouvoir être retrouvé dans un fichier et rattaché à une source.
