# Contrôle des données de prix

*Cliché arrêté au 4 septembre 2026 ; revue de finition du 8 septembre 2026.*

## I. Couverture réelle

Le cliché final contient 1241185 lignes dans 140 fichiers : 135 actions, deux fonds et trois indices. Les 17 actions ajoutées lors de la finition, puis les 4 ajoutées sous A-08, ont été acquises avec yfinance sans ajustement automatique, événements inclus, même date de fin. Le symbole, la devise USD, le type EQUITY et la date de première transaction ont été vérifiés. Les anciennes séries sont inchangées. Les ajouts et les métadonnées figurent dans les révisions de `prix_manifest.json`.

## II. Contrôles locaux

Les 23 contrôles existants produisent 9098 signalements. Ils portent sur le brut complet, y compris avant 2000 ; un signalement n'est pas une erreur confirmée. Les tests à zéro restent visibles.

| Contrôle local | Signalements |
| --- | --- |
| date en double | 0 |
| anteriorite au calendrier | 72 |
| seance absente | 14 |
| date hors calendrier | 0 |
| variation quotidienne extreme | 146 |
| barre incoherente | 1 |
| prix nul ou negatif | 0 |
| valeur manquante | 1 |
| ajustement incoherent | 0 |
| division non confirmee | 20 |
| reference de cotation absente | 56 |
| premiere cotation discordante | 0 |
| historique tronque | 22 |
| metadonnees absentes | 0 |
| devise non usd | 0 |
| fuseau inattendu | 0 |
| type inattendu | 0 |
| decalage horaire inattendu | 0 |
| premiere transaction discordante | 0 |
| fin de serie anticipee | 0 |
| denomination divergente | 7 |
| seance sans transaction | 117 |
| prix fige | 8642 |



Les séances absentes concernent SPXEW ; les valeurs nulles de volume ne sont pas appliquées comme un filtre aux indices. Les prix figés et les bornes d'identité sont traités séparément en construction. Après ce traitement, 38 valorisations sont portées, sans créer d'observations de rendement nul.

| Titre | Cours portés |
| --- | --- |
| AMD | 1 |
| BKR | 1 |
| NDAQ | 19 |
| NRG | 1 |
| SBAC | 1 |
| TPL | 13 |
| VST | 1 |
| XEL | 1 |



## III. Distributions et seconde source

Les nouvelles distributions exceptionnelles LDOS sont monétaires selon les dépôts de l'émetteur. APD distribue Versum, et LDOS sépare le nouveau SAIC : leurs facteurs de scission restent documentés sans certification. Le dividende HD répété au 28 novembre 2001 est retiré en mémoire ; le versement officiel du 27 novembre reste présent. Le registre comporte 40 événements et six corrections applicables, dont une hors de l'historique JCI désormais admis.

Nasdaq apporte 155046 clôtures communes de 64 titres. Les 31 écarts de rendement supérieurs à dix points de base se répartissent ainsi :

| Traitement | Écarts |
| --- | --- |
| convention_scission_ou_veille_documentee | 13 |
| non_arbitree | 9 |
| hors_historique_admissible | 5 |
| cours_nasdaq_fige_documente_audit_precedent | 2 |
| cours_yahoo_porte_et_reprise_cumulee | 2 |



L'écart EQT du 13 novembre 2018 est rattaché à la distribution Equitrans, sans certification du facteur Yahoo de 1,837. Les deux écarts SBAC encadrent un cours figé déjà porté par le moteur ; le mouvement cumulé reste pris à la reprise. Le nouvel écart APD correspond à Versum. Les neuf divergences non arbitrées de la vérification précédente restent une limite finie, pas une invitation à recommencer un audit général.

Le brut contient 111 extrêmes depuis 2000, dont 8 hors de la portion admissible. Les 103 autres se répartissent entre 21 concordances de prix et 82 non corroborés. Les listes complètes figurent dans `variations_finition_2026-09-08.csv` et `divergences_finition_2026-09-08.csv`.

## IV. Limites conservées

L'univers est choisi sur les informations récentes de 2026, puis projeté sur le passé. Il comporte un biais de connaissance a posteriori et de survivance. Les résultats décrivent des paniers actuels ; ils ne prouvent ni une stratégie identifiable à l'époque, ni un risque causé par l'IA. La règle III admet des activités générales de la chaîne : centres de données hors IA, semi-conducteurs, énergie, logistique et équipements. Les 134 degrés restent non quantifiés. La maturité distingue une activité établie d'un engagement, sans mesurer leur intensité.

Yahoo est une source secondaire. Close est déjà retraité des divisions, et Adj Close dépend d'ajustements rétroactifs. Le cliché conservé, ses dividendes et ses facteurs sont reproductibles localement ; une nouvelle collecte ne promet pas les mêmes valeurs. Ce ne sont pas des cours historiques totalement non ajustés. Les nombres d'actions SEC ne doivent pas être multipliés par ces cours sans harmoniser dates, classes et divisions.

Le rapprochement Nasdaq porte maintenant sur 64 titres et 155 046 clôtures, soit 154 982 rendements comparables. L'essentiel de cette couverture commence en septembre 2016. Sur les 103 variations extrêmes du brut situées dans un historique admissible, 82 restent non corroborées et 21 concordent en rendement de prix. Les neuf divergences anciennes non arbitrées restent exactement recensées dans `data/review/divergences_finition_2026-09-08.csv`. Les coefficients de scission ne sont pas certifiés. Toute conclusion de risque appuyée sur ces extrêmes devra expliciter cette réserve. Une identité comptable correcte ne certifie pas les prix.

Les dividendes sont des créances assimilées à des espèces au détachement, réinvesties en janvier. Les dates de paiement des actions ne sont pas collectées. L'ancien contrôle SPY situe l'effet du paiement tardif de décembre à environ 0,04 point par an sur ce fonds ; il ne mesure pas l'effet sur le nouvel univers. Les distributions de titres sont réinvesties synthétiquement dans le parent, sans frais propres à la scission. Il n'existe pas de registre exhaustif des opérations sur titres ni de reproduction d'un compte réellement conservé.

Le fichier auxiliaire `premieres_cotations.csv` couvre 79 entreprises et 79 titres parmi les 134 entreprises et 135 titres retenus. Il n'a pas été réécrit. Les métadonnées des nouveaux prix contiennent leur première transaction, ce qui ne certifie pas toutes les anciennes dates d'IPO. Les cas de collecte 11 à 13 restent sans tests d'acquisition importables. Le dernier relevé mensuel est la clôture du 4 septembre 2026, pas une fin de mois. L'étape 2 conserve sa commande séparée de `src/run_pipeline.py`.

La cotation conditionnelle de SNDK au 13 février 2025 reste retenue. L'ancienne sensibilité d'environ 0,29 point par an sur P1 conservé concernait l'univers précédent et n'est pas une mesure du portefeuille actuel. La liquidité et le coût d'une transaction en cotation conditionnelle ne sont pas démontrés. Aucune de ces limites n'est transformée en chantier supplémentaire dans cette finition.
