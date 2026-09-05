# Pourquoi j'ai corrigé cette étape du projet

*AI Concentration Risk Research. 5 septembre 2026.*
*Ce document explique les problèmes rencontrés et les décisions prises. Les résultats courants sont dans `univers_selection.md` ; les versions antérieures restent archivées avec leurs empreintes.*

## I. Le problème de départ : je mesurais le capital, pas sa destination

J'étais parti de l'idée qu'une entreprise investissant beaucoup devait être intéressante pour mon sujet. Le classement faisait pourtant remonter des métiers qui investissent structurellement beaucoup, indépendamment de l'IA.

Le problème ne venait pas seulement d'un seuil mal choisi. Le ratio ne répondait pas à la question posée. J'ai donc conservé les données d'investissement comme description et déplacé la sélection vers les activités et engagements documentés dans la chaîne de calcul.

Cela ne veut pas dire que l'investissement est inutile. Cela veut dire qu'il faut d'abord savoir ce qu'il finance.

## II. Ma question économique était plus affirmative que mes preuves

« Perdre de l'argent si l'investissement IA s'arrête » décrivait un scénario. Je l'utilisais presque comme si j'avais déjà observé sa réalisation.

J'ai remplacé cette réponse hypothétique par une preuve observable : activité actuelle, commandes, installations, contrat ou investissement concret. Une perspective générale reste douteuse.

J'ai aussi retiré l'affirmation selon laquelle toutes les actions retenues plongeraient ensemble. Ce comportement est précisément ce que l'analyse de risque devra tester. La sélection décrit un mécanisme possible de concentration, elle n'en démontre pas encore l'effet boursier.

L'univers reste un ensemble de candidats pour plusieurs portefeuilles possibles. Je ne l'assimile pas à un portefeuille qui détiendrait nécessairement toutes les entreprises.

## III. Certaines exclusions ne correspondaient à aucune décision écrite

L'ancien classement comportait des exclusions attribuées par défaut. Le balayage complémentaire de certains secteurs avait rattrapé des entreprises, mais il n'offrait pas la même chance d'examen à toutes.

Applied Materials et Amphenol montrent le problème : des liens avec la demande d'équipements ou de composants pour les infrastructures étaient présents dans les sources, alors que les entreprises restaient écartées. Leurs [rapports Applied Materials 2025](https://www.sec.gov/Archives/edgar/data/6951/000162828025056742/amat-20251026.htm) et [Amphenol 2025](https://www.sec.gov/Archives/edgar/data/820313/000110465926013549/aph-20251231x10k.htm) permettent de revenir au raisonnement.

Je conserve maintenant les cinq cents CIK dans un registre explicite. Une décision manquante devient `A_EXAMINER`. Une pièce insuffisante devient `DOUTEUX`. La revue a été étendue aux passages repérés pour chaque entreprise, avec des lectures complémentaires pour les cas litigieux.

Cette correction ne m'autorise pas à prétendre avoir audité intégralement cinq cents rapports. Le registre indique la limite de la lecture réellement menée.

## IV. Le rang ne pouvait pas servir d'identifiant

Les premières décisions étaient liées au rang d'un classement. Une nouvelle extraction pouvait modifier ce rang et faire passer la décision à une autre entreprise sans changer le code de classification.

Le CIK est désormais la clé. Le rang reste un ordre de lecture reproductible. Le contrôle de preuve vérifie le CIK, le dépôt et la citation dans le corpus associé. Si une actualisation rend la preuve introuvable, la décision ancienne reste conservée mais n'est plus appliquée comme acquise.

## V. L'extraction ne pouvait pas soutenir une promesse de lecture complète

L'ancien extracteur s'arrêtait après quarante passages et écartait certaines phrases selon leur longueur. Cela pouvait supprimer la partie utile d'un rapport, notamment les tableaux ou les paragraphes longs.

L'extraction actuelle conserve tous les passages déclenchés par les motifs déclarés, leur contexte, leur position et leur dépôt. Les HTML et les textes sont archivés avec leurs empreintes. Les CSV et leur manifeste doivent correspondre avant d'être utilisés.

Le corpus corrigé contient 499 rapports complets et 12 836 passages pour une composition de 500 entreprises. Honeywell Aerospace reste sans 10-K exploitable au CIK concerné. Pour Exxon Mobil, le rapport du prédécesseur n'a été utilisé qu'après vérification d'une continuité juridique explicite, documentée dans le [dépôt du 1er juillet 2026](https://www.sec.gov/Archives/edgar/data/2115436/000119312526291990/d71068d8k12b.htm).

« Extraction complète » signifie complète pour le vocabulaire déclaré, pas détection certaine de toutes les expositions économiques.

## VI. Une série d'investissement mélangeait deux notions

American Electric Power semblait avoir multiplié son investissement par environ onze. Ce nombre était calculable avec l'ancien fichier, mais les postes rapprochés ne décrivaient pas la même dépense.

Le tableau de flux 2025 distingue **3,453 milliards de dollars d'acquisitions de centrales** et **8,453 milliards de dépenses de construction**. J'ai retenu une série homogène de construction. Je ne l'appelle pas pour autant investissement total de toutes les acquisitions. La distinction est visible dans le [rapport AEP 2025](https://www.sec.gov/Archives/edgar/data/4904/000000490426000013/aep-20251231.htm).

Cette correction change aussi la règle générale : choisir le plus grand poste disponible ne constitue pas un rapprochement comptable. Quand une divergence n'est pas résolue, la valeur reste visible avec un statut de revue et le multiple n'est pas utilisé. J'ai étendu ce contrôle aux différences inférieures à 5 % : un faible écart ne prouve pas que deux notions sont équivalentes.

## VII. Je comparais parfois des entreprises dont le périmètre avait changé

J'avais présenté Howmet et Western Digital comme deux contradictions entre le discours et les comptes. Mais certains anciens montants incluaient des activités sorties du groupe.

Pour **Howmet**, les ventes et la recherche retraitées ne suivent pas automatiquement la même histoire que les flux d'investissement. Les comptes de résultat comparatifs de 2018 et 2019 sont utilisables sur les activités poursuivies ; les anciens flux ne sont pas raccordés sans rapprochement. Le [rapport Howmet 2020](https://www.sec.gov/Archives/edgar/data/4281/000000428121000049/arnc-20201231.htm) explique cette différence.

Pour **Western Digital**, la séparation de Sandisk modifie le périmètre. Les flux des activités abandonnées restent inclus dans certains tableaux consolidés. J'ai conservé les rapprochements explicites : 821 − 219 = 602 millions en 2023, 487 − 166 = 321 millions en 2024, 412 − 139 = 273 millions en 2025. Ce sont des soustractions documentées, pas des montants inventés pour améliorer le résultat. Voir le [rapport WDC 2025, note sur les activités abandonnées](https://www.sec.gov/Archives/edgar/data/106040/000010604025000038/wdc-20250627.htm).

Pour **Marvell**, l'histoire du nouveau CIK passe par l'acquisition d'Inphi et une réorganisation ; je ne la présente plus comme une simple scission. Les anciens comptes ne sont pas raccordés automatiquement. Voir le [dépôt Marvell d'avril 2021](https://investor.marvell.com/sec-filings/all-sec-filings/content/0001193125-21-122938/d136815d8k12b.htm).

Ces cas corrigés ne prouvent pas que toutes les acquisitions et cessions de toutes les entreprises ont été rapprochées. La limite reste écrite.

## VIII. L'année seule pouvait faire disparaître un exercice

La règle d'année majoritaire était auparavant approchée par le mois de clôture. En appliquant réellement le nombre de jours, j'ai découvert un autre problème : deux exercices distincts peuvent recevoir la même année civile majoritaire.

J'ai conservé les dates et une ligne par CIK et clôture. La base contient désormais 5 707 périodes pour 496 entreprises. Les débuts exacts restent propres à chaque mesure, même lorsque les postes clôturent le même jour.

La comparaison avec le passé utilise ces dates. Une référence ne peut ni inclure l'exercice récent, ni le chevaucher, ni compter deux fois la même clôture.

## IX. Les références ne portaient pas toutes sur les mêmes années

Le fichier pouvait afficher une référence générale 2017–2019 alors qu'une dépense utilisait des exercices beaucoup plus récents. Le cas Nvidia le rendait visible.

Chaque mesure conserve maintenant ses périodes de référence, ses montants, leurs dépôts et son éventuel repli. Si moins de deux exercices comparables précèdent la mesure récente, je ne calcule pas le multiple.

Pour les ventes de Nvidia, j'ai rapproché les deux étiquettes sur une preuve explicite : le rapport 2022 les utilise pour les mêmes contextes consolidés et les mêmes montants. Le [rapport 2020](https://www.sec.gov/Archives/edgar/data/1045810/000104581020000010/nvda-2020x10k.htm) et le [rapport 2022](https://www.sec.gov/Archives/edgar/data/1045810/000104581022000036/nvda-20220130.htm) permettent ainsi de conserver la référence 2017–2019. Cette équivalence est limitée à ce CIK, à ces deux étiquettes et aux périodes vérifiées ; elle n'autorise pas un raccordement général de tous les postes.

J'ai retiré l'idée qu'une base plus récente sous-estimerait nécessairement la croissance. Elle peut la réduire ou l'augmenter selon le parcours observé. La sensibilité aux références et à l'horizon reste une limite de cette description.

## X. Des données absentes devenaient une conclusion sur toute l'entreprise

Deux dépenses absentes ne permettent pas de conclure à une absence de mouvement. Inversement, une seule mesure qui baisse ne doit pas être classée en progression modérée au seul motif que les autres postes manquent.

Le fichier sépare désormais le mouvement observé et la couverture. Trois mesures comparables, une observation partielle et aucune comparaison sont des situations différentes.

Pour **CMS**, l'absence dans l'API ne signifiait pas que la dépense n'était publiée nulle part. Trois montants ont été retrouvés dans le 10-K sous une dimension XBRL : 2,407, 3,018 et 3,824 milliards de dollars pour 2023–2025. Le complément, sa définition et sa source sont consignés dans le registre. Voir le [rapport CMS 2025](https://www.sec.gov/Archives/edgar/data/811156/000081115626000004/cms-20251231.htm).

Pour **NextEra et DTE**, les lacunes non rapprochées demeurent. Je ne remplace pas le capex d'un groupe par celui d'une filiale ou par un agrégat d'une autre nature.

## XI. Les comptes ne démontrent pas la cause IA

L'ancienne rédaction transformait une croissance comptable générale en confirmation d'une exposition à l'IA. Ce lien ne peut pas être établi avec ces seules mesures.

J'ai retiré les conclusions selon lesquelles Intel ne capterait rien du marché, les logiciels gagneraient nécessairement à un arrêt des investissements, ou la progression des compagnies d'électricité confirmerait une exposition exclusivement future. Ces affirmations dépassaient les preuves.

La règle actuelle distingue activité existante, engagement et perspective. Le degré reste non quantifié lorsque la part d'activité n'est pas isolée. Les catégories de mouvement et leurs seuils sont descriptifs ; la sensibilité à 1,5, 2 et 2,5 reste visible.

Les méthodes ont été modifiées après observation des résultats. Je reconnais ce caractère exploratoire au lieu de le faire disparaître dans la rédaction.

## XII. Les documents et les sorties doivent raconter le même état du projet

Le contexte maître indiquait encore qu'aucun code et aucune collecte n'existaient. Les notes d'univers contenaient des effectifs anciens, des degrés additionnés incorrectement et des conclusions fondées sur les comparaisons désormais corrigées.

Le contexte maître et la règle ont été actualisés en conservant l'histoire et les principes pédagogiques. Le pipeline produit une synthèse recalculée et un manifeste. Le contrôle peut repérer une sortie, une source ou un script modifié depuis le calcul.

L'export Excel utilise les CIK pour ses jointures. La « première cotation » issue du fichier Yahoo existant est renommée comme première date d'historique disponible : sa date de collecte n'est pas documentée et elle n'est pas une date d'introduction en bourse vérifiée. Une antériorité par rapport à la fondation indiquée devient une demande de vérification, pas une preuve d'historique hérité.

## XIII. Ce que je dois encore vérifier

Le traitement corrige les erreurs identifiées et empêche plusieurs façons de les reproduire. Il n'offre pas une garantie générale d'absence d'erreur.

Les décisions douteuses ou non examinables restent visibles. Les 1 636 observations comptables marquées pour revue et les 3 724 alertes de contrôle couvrent notamment des divergences, des ruptures, des manques et des changements de postes ; ce ne sont pas 3 724 erreurs démontrées.

La composition locale de l'indice reste à rapprocher d'une source officielle datée. Les prix, les performances, les portefeuilles, leurs poids et leurs scénarios n'ont pas été ajoutés à cette étape.

Le prochain travail consiste à relire ces corrections et leurs preuves, puis à définir une question empirique et des portefeuilles que je pourrai réellement défendre.
