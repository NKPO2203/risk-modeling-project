# Contrôle des données de prix

*AI Concentration Risk Research. Phase 2 de l'étape 2. Mise à jour du 8 septembre 2026 après audit.*

## I. La question du contrôle

Une forte variation peut venir du marché, d'une opération sur titres ou d'un défaut de fichier. Le contrôle doit les distinguer. Ce contrôle précède l'interprétation des risques ; les mesures descriptives utilisées pendant l'audit ne constituent pas les résultats de l'étape 3. Une série plausible ne devient pas exacte parce qu'elle passe des tests internes.

## II. Le périmètre et la méthode

Le cliché contient 114 fichiers d'actions pour 113 entreprises et cinq séries de comparaison, soit 119 fichiers et 1 057 439 lignes quotidiennes. Les empreintes sont dans `data/raw/prix_manifest.json`. Les preuves brutes ont été conservées intactes pendant l'audit.

`src/controler_prix.ipynb` appelle `src/controle_prix.py`. Il n'effectue plus d'acquisition de métadonnées ou de prix. Le traitement rejoue l'ensemble des contrôles et écrit `controle_prix.csv`, `resume_controle_prix.csv`, `controle_divisions_sec.csv` et `couverture_controle_prix.json` dans `data/processed/`.

La couverture indique les fichiers et les comparaisons réellement calculables. Les gardes structurelles refusent les fichiers vides, les colonnes manquantes, les dates impossibles ou désordonnées, les valeurs infinies et les événements ou volumes inconnus. Une absence de prix reste une anomalie explicite, pas un zéro. Un ajustement sans comparaison calculable ne peut pas donner un faux succès.

Le calendrier contient 8 458 séances depuis le 29 janvier 1993. Un recalcul séparé des jours ouvrés, jours fériés et fermetures exceptionnelles ne trouve aucun écart sur cette période. Ce contrôle n'étend pas le calendrier avant 1993 et ne valide pas les cours présents à ces dates.

## III. Les résultats recalculés

Les vingt-trois contrôles historiques produisent 8 674 signalements sur 101 fichiers. Les nombres précédents, 8 670 signalements sur 100 fichiers et 1 043 940 lignes, n'avaient pas été mis à jour après l'ajout de CMS. Les fichiers dérivés étaient déjà à jour ; c'était leur description qui ne l'était pas.

| Test | Cas |
|---|---:|
| Date en double | 0 |
| Antériorité au calendrier | 60 |
| Séance absente | 14 |
| Date hors calendrier | 0 |
| Variation quotidienne extrême | 127 |
| Barre incohérente | 1 |
| Prix nul ou négatif | 0 |
| Valeur manquante | 1 |
| Ajustement incohérent | 0 |
| Division non confirmée par ce rapprochement | 20 |
| Référence de cotation absente | 37 |
| Première cotation discordante avec la référence | 0 |
| Historique tronqué | 20 |
| Métadonnées absentes | 0 |
| Devise non USD | 0 |
| Fuseau inattendu | 0 |
| Type inattendu | 0 |
| Décalage horaire inattendu | 0 |
| Première transaction discordante | 0 |
| Fin de série anticipée | 0 |
| Dénomination divergente | 6 |
| Séance sans transaction, hors prix figé | 115 |
| Prix figé à volume nul | 8 273 |

Un zéro indique l'absence de détection parmi les observations calculables, pas une certification. Les quatorze séances absentes concernent `SPXEW`. La barre incohérente est celle de HUBB au 5 mai 2021, et les prix manquants ceux du 8 août 1977.

## IV. Ce que ces contrôles changent

**Les cours figés.** Sur HUBB, 5 510 lignes portent un volume nul et quatre prix identiques, égaux à la clôture précédente. Le nombre de 5 561 concernait tous les volumes nuls, pas ce critère strict. Un long segment sans volume suivi d'une rupture, comme celle du 31 octobre 1994, ne doit pas être utilisé comme un historique ordinaire de rendements. Ces seuls champs ne prouvent cependant pas que toute séance isolée sans volume est fabriquée. Le filtre courant distingue les segments initiaux, les prix intérieurs figés et les prix variables à volume nul.

Après les restrictions d'identité sur GOOG, DELL et VRT, 18 observations sont portées sur la période de construction. Le mouvement cumulé est pris à la reprise ; les rendements observés restent manquants autour du trou. La liste est dans `qualite_valorisation.csv`. Estimer une volatilité ou une corrélation en traitant ces valeurs portées comme des observations ordinaires demanderait une réserve supplémentaire.

**L'ajustement Yahoo.** La formule `Close_t / (Close_precedent − Dividends_t) − 1` retrouve la variation de `Adj Close` avec un écart maximal inférieur à 5 × 10⁻⁵ dans le cliché. Le seuil d'alerte du programme est 10⁻⁴. La formule additive peut s'écarter sensiblement sur un détachement exceptionnel. Cela confirme la convention du fournisseur, pas sa supériorité pour représenter un compte de titres et d'espèces. Une action passant de 100 à 95 avec 10 de dividende donne 105 de richesse, soit 5 %, quelle que soit la variation de sa série ajustée Yahoo.

**Les événements dans `Stock Splits`.** Sur 56 événements depuis 2010, 9 ne sont pas encadrés par les observations SEC disponibles, 20 ne correspondent pas à un rapport d'actions égal au facteur annoncé, et 27 sont compatibles avec la tolérance de 2 %. Les dates de mesure et de dépôt encadrantes sont conservées. Un dépôt postérieur à l'événement ne suffit pas si la mesure qu'il contient lui est antérieure.

Les vingt cas ne signifient pas tous que le nombre d'actions est inchangé à 0,1 % près. Une scission, une acquisition, une émission, un rachat ou une différence de classes peut modifier ce rapport. Le contrôle est une alerte de rapprochement, pas la confirmation juridique de chaque événement. Il ne valide pas une multiplication cours fois nombre d'actions. Aucun portefeuille courant n'utilise une capitalisation reconstruite.

**Les débuts d'historique.** Trente-sept titres n'ont pas de référence dans `premieres_cotations.csv`. Les 77 concordances restantes utilisent la même source que les prix et ne constituent donc pas une seconde source. Vingt titres ont une date d'entrée dans l'indice antérieure à leur première ligne Yahoo. Les débuts partagés par plusieurs séries suggèrent aussi des limites de couverture, sans démontrer que des introductions simultanées seraient impossibles.

L'audit a vérifié séparément trois identités : GOOG classe C à partir du 3 avril 2014, DELL classe C à partir du 26 décembre 2018 en cotation conditionnelle, VRT industriel à partir du 10 février 2020 après le véhicule GSAH. Les sources et les règles sont dans `regles_historiques_prix.csv`. Ces raccordements ne sont pas détectés par une simple concordance de dates Yahoo.

**Les variations extrêmes.** Leur concentration dans des épisodes de marché connus est un contrôle de plausibilité. Elle ne prouve pas que chacune des 127 variations ajustées de plus de 30 % est exacte. Les alertes restent visibles ; aucune n'est effacée au seul motif qu'elle ressemble à une crise.

## V. Le recoupement externe effectué

Le contrôle SEC porte sur des actions en circulation, pas sur les cours. L'affirmation selon laquelle aucun recoupement public supplémentaire n'était possible était trop générale. L'audit a consulté le fichier de [distributions historiques de State Street](https://www.ssga.com/library-content/products/fund-data/etfs/us/spdr-etf-historical-distributions.xlsx).

Les 135 dates de distribution de SPY depuis 1993 concordent. Sur les 107 distributions de la période de construction, une différence dépasse l'arrondi au millième : le 17 décembre 2021, Yahoo porte 1,633 dollar et State Street 1,636431 dollar. Les deux valeurs restent consignées ; la preuve brute est conservée. Remplacer les montants par ceux de State Street dans un calcul séparé modifie l'annualisation de SPY d'environ 0,01 point de base. Avant 2000, d'autres divergences existent et ne concernent pas la fenêtre de construction.

La [page officielle de SPY](https://www.ssga.com/us/en/individual/etfs/state-street-spdr-sp-500-etf-trust-spy) donne une clôture de 773,17 dollars au 3 septembre 2026 ; le fichier Yahoo contient 773,1699829101562. Ce point concorde à l'arrondi. Les volumes de place et les volumes consolidés n'ont pas le même périmètre ; leur différence ne constitue pas à elle seule une erreur. Un cours et des distributions de SPY ne valident pas les historiques des 114 actions.

Le calendrier de distribution officiel révèle une autre limite : les 26 dividendes de décembre inclus depuis 2000 sont payés fin janvier suivant. Notre modèle les assimile à une poche disponible au détachement et peut donc les réinvestir avant paiement. En conservant les mêmes cours et montants Yahoo mais en attendant les paiements officiels, avec la même unique date annuelle de réinvestissement, l'annualisation de SPY diminue de 4,10 points de base. Les créances impayées restent dans la richesse ; elles ne sont pas supprimées. Cette sensibilité mesure une approximation d'exécution, pas un défaut de conservation de valeur.

L'audit initial avait rapproché quatre clôtures de Sandisk, du 31 août au 3 septembre 2026, publiées sur sa [page investisseurs alimentée par LSEG](https://investor.sandisk.com/stock-information/historical-price-lookup). Elles concordent à l'arrondi avec le cliché : 1 566,70, 1 536,87, 1 553,40 et 1 554,99 dollars. Le complément décrit ci-dessous couvre désormais les 392 clôtures de Sandisk depuis le 13 février 2025. Une sensibilité déplaçant la seule entrée de SNDK de sa cotation conditionnelle du 13 février 2025 à sa cotation ordinaire du 24 février réduit l'annualisation de P5 conservé de 64,21 points de base. Le rapport d'audit détaille ce choix d'exécution, dont l'effet est plus grand que celui des frais testés.

## VI. Vérification complémentaire du 8 septembre 2026

Le rapprochement Nasdaq porte sur 103 411 clôtures de 43 titres, dont deux fonds, et 103 368 paires quotidiennes comparables. La source reçue ne remonte généralement pas au-delà de septembre 2016. Les réponses, empreintes, dates couvertes et écarts sont conservés dans `data/review/sources_cloture_2026-09-08/`. La commande `python -m src.recouper_prix` rejoue le rapprochement sans réseau.

Les 392 clôtures de Sandisk concordent à l’arrondi. Parmi les 98 variations extrêmes signalées depuis 2000, 18 ont un rendement de prix concordant avec Nasdaq ; une correspond à la scission Tyco corrigée sur pièces SEC ; 79 restent non corroborées. Une absence de source ne valide ni ne réfute ces variations. Les résultats des contrôles bruts restent inchangés afin de conserver la trace des erreurs dans le cliché.

Le registre des opérations documente 34 événements : les 20 rapprochements SEC incompatibles, les 9 sans encadrement, et les 5 événements traités dans les corrections. Une scission ne se contrôle pas en exigeant que le nombre d’actions du parent augmente du facteur de prix. La nature juridique est documentée séparément de la précision du coefficient boursier.

Trois erreurs de richesse sont corrigées dans les traitements de JCI, ETN et CNP. Deux distributions non monétaires sont reclassées sans changer la richesse à leur date. Les calculs, les 27 écarts de rendement supérieurs à dix points de base entre fournisseurs et leur qualification figurent dans `research/verification_etape_2.md`. Les alertes non résolues ne sont pas déclarées validées.

## VII. Limites de la vérification

La couverture externe reste partielle, notamment sur 79 variations extrêmes anciennes et plusieurs différences de cours entre fournisseurs. Les dates de paiement relèvent d'une convention synthétique déjà écrite ; leur absence n'est pas assimilée à une erreur numérique du moteur. Une scission peut être incorporée dans un cours retraité sans que le moteur reconstruise les titres distribués. La version conservée reste donc une simulation sur séries retraitées, pas un registre certifié de titres détenus.

Le test des fins de série ne mesure pas le biais du survivant. La composition de l'indice et les rapports sont récents, les entreprises sorties du périmètre n'ont pas été recherchées systématiquement. Les niveaux et classements rétrospectifs ne constituent pas une stratégie connue à l'époque.

Yahoo peut réviser son historique lors d'une nouvelle collecte. Les CSV et empreintes fixent un cliché dont les traitements sont reproductibles ; ils ne figent pas la réponse future du fournisseur. Le carnet de collecte est conservé comme trace de démarche, séparément du programme de reconstruction.

## VIII. La leçon de méthode conservée

Les premiers contrôles avaient laissé passer des prix absents, une réponse descriptive vide et des instruments homonymes. La règle qui en est sortie reste utile : vérifier que le résultat attendu est présent, pas seulement qu'une exception n'a pas été levée.

Cette règle vaut aussi pour l'audit. Un moteur qui conserve la richesse peut utiliser le mauvais titre ou le mauvais calendrier de paiement. Un rapprochement SEC stable peut comparer les mauvaises dates de mesure. Un chiffre ancien peut rester dans une note alors que le fichier a changé. Les preuves, les corrections et les limites doivent donc rester attachées aux résultats.
