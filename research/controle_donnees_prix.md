# Contrôle des données de prix

*AI Concentration Risk Research. Phase 2 de l'étape 2. 7 septembre 2026.*

## I. Ce que je cherche, et ce que je ne cherche pas

Je n'analyse rien ici. Je n'ai regardé aucune volatilité, aucune corrélation, aucune performance. Je cherche à savoir si les séries que j'ai collectées méritent qu'on calcule quoi que ce soit dessus.

La question est celle de l'instrument, pas du phénomène. Le jour où une volatilité sortira à 45 %, je veux pouvoir dire si c'est le marché ou un défaut de fichier. Ce document existe pour que cette réponse soit disponible sans avoir à recommencer.

## II. Le périmètre

Cent treize fichiers d'actions et cinq séries de comparaison, deux fonds et trois indices, soit **1 043 940 lignes de prix quotidiens**. La source est Yahoo Finance, interrogée par `yfinance`, et les fichiers portent chacun leur empreinte dans `data/raw/prix_manifest.json`.

Les tests sont écrits dans `src/controler_prix.ipynb`. Chaque bloc réécrit ses propres résultats et laisse intacts ceux des autres, de sorte qu'on peut le relancer seul. Toutes les anomalies aboutissent dans un fichier unique, `data/processed/controle_prix.csv`, une ligne par cas, avec le fichier, le test, la date et un détail.

## III. Vingt-trois tests, huit mille six cent soixante-dix anomalies

| Test | Cas | Tâche |
|---|---|---|
| Date en double | 0 | 13 |
| Antériorité au calendrier | 59 | 13 |
| Séance absente | 14 | 13 |
| Date hors calendrier | 0 | 13 |
| Variation quotidienne extrême | 126 | 14 |
| Barre incohérente | 1 | 14 |
| Prix nul ou négatif | 0 | 14 |
| Valeur manquante | 1 | 14 |
| Ajustement incohérent | 0 | 15 |
| Division non confirmée | 20 | 16 |
| Référence de cotation absente | 37 | 17 |
| Première cotation discordante | 0 | 17 |
| Historique tronqué | 19 | 17 |
| Métadonnées absentes | 0 | 18 |
| Devise non USD | 0 | 18 |
| Fuseau inattendu | 0 | 18 |
| Type inattendu | 0 | 18 |
| Décalage horaire inattendu | 0 | 18 |
| Première transaction discordante | 0 | 18 |
| Fin de série anticipée | 0 | 19 |
| Dénomination divergente | 6 | 19 |
| Séance sans transaction | 115 | 19 |
| Prix figé | 8 272 | 19 |

Cent fichiers sur cent dix-huit portent au moins une anomalie. Les zéros comptent autant que le reste : ils disent qu'un test a bien été exécuté et n'a rien relevé.

## IV. Cinq résultats qui changent la suite

**Les lignes de remplissage.** Huit mille deux cent soixante-douze lignes portent un volume nul et quatre cours identiques, égaux à la clôture de la veille. Elles ne décrivent aucune séance. `HUBB` en compte 5 561, soit 41 % de son historique ; `CRH` 1 718, soit 18 %. Elles produiraient des rendements nuls et abaisseraient artificiellement toute volatilité calculée sur les périodes anciennes. Je les ai découvertes en cherchant à comprendre la plus forte variation de la liste, `HUBB` au 31 octobre 1994, à +885,9 %, qui n'est pas un mouvement de marché mais la soudure entre le segment fabriqué et le début des vraies cotations.

**La convention d'ajustement.** Le prix ajusté de Yahoo se reconstruit à partir du prix de clôture et des dividendes selon une formule multiplicative, le dividende étant retiré du prix de départ et non ajouté au prix d'arrivée. La formule additive s'écarte jusqu'à 8 % sur `JCI` ; la multiplicative reste sous 5 × 10⁻⁵ sur les 118 fichiers, et tous les écarts de la formule additive tombent sur des jours de détachement. Je sais donc reconstruire la série ajustée à la cinquième décimale.

**Deux natures d'événements dans une même colonne.** La colonne `Stock Splits` mélange les divisions d'actions véritables et les facteurs d'ajustement de prix consécutifs à une scission. Sur 56 divisions déclarées depuis 2010, la SEC en confirme 27 et n'en confirme pas 20. Dans ces vingt cas, le nombre d'actions ne bouge pas de plus de 0,1 % : `MMM` en avril 2024 pour Solventum, `IBM` en novembre 2021 pour Kyndryl. Le facteur cumulé des divisions ne peut donc pas être lu directement dans cette colonne, ce qui concerne la reconstruction des capitalisations.

**Les dates de début ne sont pas des premières cotations.** Douze séries commencent exactement le 17 mars 1980, neuf le 21 février 1973, huit le 2 janvier 1962. Aucune entreprise n'introduit ses actions le même matin que onze autres. Ce sont les strates de départ de la base de Yahoo. Dix-neuf entreprises étaient d'ailleurs déjà dans le S&P 500 avant la première ligne de prix disponible. Une date de début dit à partir de quand Yahoo parle du titre, pas quand le titre a commencé d'exister.

**Le reste des variations extrêmes est du marché.** Sur les 126 variations ajustées de plus de 30 %, soixante-seize tombent dans les années 2000, dont vingt-quatre en 2002 et seize en 2001, et six en 1987. La concentration correspond aux épisodes connus. Je ne les écarte pas.

## V. Ce que ce contrôle ne couvre pas

Aucune source externe automatisable n'a pu être mobilisée. Stooq, qui servait des fichiers de cours sans inscription, les protège désormais derrière une vérification anti-robot, et les autres fournisseurs gratuits exigent un compte. Le seul recoupement indépendant obtenu est celui des divisions d'actions contre les dépôts SEC. Le niveau manuel du protocole, un échantillon relevé à la main sur un site public, reste à exécuter.

Le biais du survivant n'est pas mesuré par le test des fins de série. Aucun de nos titres n'a été retiré de la cote, mais c'est une tautologie : la liste des composants est un cliché de 2026, donc une entreprise sortie de l'indice en 2018 n'a jamais eu de fichier.

Un changement de symbole à l'intérieur d'un historique reste invisible. Yahoo sert toute la série sous le symbole d'aujourd'hui, sans marque de rupture.

Les prix ajustés de Yahoo sont réécrits rétroactivement à chaque dividende et chaque division. Une nouvelle collecte ne redonnera pas les mêmes valeurs. Les fichiers conservés et leurs empreintes fixent un cliché daté ; les calculs faits à partir de ce cliché restent reproductibles, la collecte non.

Enfin, `data/raw/premieres_cotations.csv` ne couvre que 76 des 113 titres. Il date de l'époque où l'univers en comptait 82 et n'a pas été régénéré.

## VI. Une leçon de méthode

Trois tests ont d'abord échoué de la même façon, et je le consigne parce que le défaut est reproductible.

Le test des prix négatifs comparait chaque valeur à zéro, et laissait passer la ligne de `HUBB` du 8 août 1977 où tous les prix sont absents : une valeur manquante ne satisfait aucune comparaison. La collecte des métadonnées traitait toute absence d'exception comme un succès, et enregistrait un dictionnaire vide comme une fiche valide. Sa deuxième version traitait toute réponse non vide comme un succès, et a accepté la description d'indices d'options homonymes des fonds `RSP` et `SPY`.

À chaque fois, je vérifiais l'absence de l'échec que j'imaginais au lieu de vérifier la présence du succès attendu. La règle retenue est la seconde.

Un quatrième défaut portait sur la reproductibilité. Le contrôle des divisions donnait deux résultats différents sur deux machines, parce que soixante-six couples entreprise et date de mesure portent deux déclarations distinctes et que le tri par défaut de pandas n'est pas stable entre ex aequo. Corrigé en triant sur la date de dépôt, seule date qui situe une déclaration par rapport à un événement.
