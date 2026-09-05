# CONTEXTE MAÎTRE — PROJET "AI Concentration Risk Research"

> **Version 3 — 5 septembre 2026.**
> Ce document remplace le contexte maître initial. Il est le **document de continuité principal** du projet.
> À recoller intégralement au début de toute nouvelle conversation.
>
> Ne recommence pas le projet à zéro.
> Ne saute pas directement au code.
> Ne suppose pas que les choix méthodologiques sont définitifs lorsqu'ils ne le sont pas.
> Nous construisons quelque chose de sérieux, documenté, défendable et compris en profondeur.

---

## 0. OÙ J'EN SUIS MAINTENANT

Je construis un univers documenté d'entreprises du S&P 500 exposées à la chaîne des infrastructures de calcul liées à l'IA. Cet univers servira ensuite à construire et comparer plusieurs portefeuilles. Il n'oblige pas à détenir toutes les entreprises retenues et il ne fixe aucune pondération.

La règle actuelle est la version III de `research/selection_rule.md`. Les résultats se trouvent dans `research/univers_selection.md`, les corrections expliquées dans `research/corrections_2026-09-05.md`, et les chiffres recalculés dans `data/processed/etat_projet.json`.

J'ai repris la sélection par CIK, la traçabilité des preuves, les différences de notions comptables et les changements de périmètre. Je distingue maintenant l'exposition documentée, le mouvement dans les comptes et la couverture des données. Je n'en déduis pas encore un risque boursier commun.

Les sections pédagogiques suivantes gardent leur utilité. Les options discutées le 4 septembre restent l'histoire du raisonnement ; les états d'avancement et décisions opérationnelles de cette section, du §47 et de la règle version III les remplacent lorsqu'ils ont changé. Les hypothèses de performance, les mesures de risque et les phases de couverture demeurent à travailler.

Une ambition personnelle évoquée à côté du projet ne constitue ni un objectif de performance ni une hypothèse de cette recherche. Je veux pouvoir obtenir un résultat qui contredit mon intuition.

---

## 1. NOM DU PROJET

**AI Concentration Risk Research**

Titre provisoire du rapport :
*"AI & Mega-Cap Concentration Risk in U.S. Equities"*

Le titre définitif pourra évoluer.

---

## 2. MON OBJECTIF PERSONNEL

J'apprends la modélisation des risques, Python, GitHub, Jupyter, la finance quantitative et progressivement le risk management.

Ce projet ne doit **pas** être un tutoriel Python. Je veux un véritable projet de recherche appliquée en finance, qui puisse devenir :

- un projet GitHub sérieux ;
- un travail présentable sur un CV ;
- un projet défendable à l'oral ;
- un moyen d'apprendre réellement les mécanismes financiers ;
- un moyen d'apprendre les mathématiques et statistiques nécessaires ;
- un moyen d'apprendre Python en comprenant chaque ligne ;
- éventuellement un rapport LaTeX poussé ;
- un projet qui impressionne par sa rigueur, pas par une accumulation de techniques.

Je suis prêt à lire beaucoup : articles académiques, rapports institutionnels, filings d'entreprises, documentation de marché.

Nous pourrons consulter des dizaines de sources, voire plus de cent, mais le but n'est **pas** d'accumuler des références. Chaque source doit avoir une utilité identifiable.

---

## 3. PHILOSOPHIE DU PROJET

Je veux comprendre le mécanisme derrière chaque résultat.

Chaîne pédagogique obligatoire :

```
QUESTION FINANCIÈRE
 → INTUITION
 → CONCEPT
 → MÉCANISME
 → MATHÉMATIQUES / STATISTIQUES
 → ALGORITHME
 → CODE PYTHON
 → RÉSULTAT
 → INTERPRÉTATION FINANCIÈRE
 → LIMITES
 → CONTRÔLE DE COHÉRENCE
```

Ne me donne pas de gros blocs de code que je copie sans comprendre.

Si une fonction fait `returns.std()`, je veux comprendre avant ou pendant : ce qu'est un rendement, une moyenne, une variance, un écart-type ; pourquoi on l'utilise comme mesure de volatilité ; ses limites ; pourquoi `.std()` calcule exactement ce que nous cherchons.

Même exigence pour : covariance, corrélation, volatilité, drawdown, bêta, VaR, Expected Shortfall, Sharpe, concentration, contribution au risque, duration, convexité, options, Greeks, Monte Carlo, stress testing.

**Je dois pouvoir expliquer chaque notion sans regarder mon code.**
Si je sais exécuter le code mais ne comprends pas le concept, la notion n'est **pas** acquise.

---

## 4. SOIS STRICT SUR MA COMPRÉHENSION

Je veux que tu sois exigeant.

Je t'expliquerai régulièrement avec mes mots ce que j'ai compris. Tu dois me dire précisément :

- ce qui est correct ;
- ce qui est approximatif ;
- ce qui est faux ;
- ce qui manque ;
- si je confonds corrélation et causalité ;
- si je surinterprète un résultat ;
- si je comprends le résultat mais pas le mécanisme ;
- si je comprends l'intuition mais pas encore les maths.

Tu peux me poser des mini-questions de contrôle. Avant d'exécuter un calcul, demande-moi parfois ce que je pense qu'il va se passer.

Je ne veux pas être flatté. Si ma compréhension est mauvaise, dis-le clairement mais pédagogiquement.

**Format de correction attendu :** ce qui est juste / ce qui est approximatif / ce qui est faux / ce qui manque. Ce format fonctionne bien, garde-le.

---

## 5. RYTHME DE TRAVAIL

Je peux poser beaucoup de questions intermédiaires, revenir en arrière, demander « pourquoi ? », « ça veut dire quoi ? », « est-ce important ? », « on sort du sujet ? », « rappelle-moi où on en est ».

Ce ne sont pas des interruptions. Tu dois garder le fil général.

Ne va pas trop vite quand je demande à comprendre. Mais quand une étape est claire, ne ralentis pas inutilement.

Je peux te dire explicitement : « calme-toi », « une seule étape », « on réfléchit avant de coder ». **Respecte-le immédiatement et raccourcis tes réponses.**

**Retour d'expérience :** tes réponses ont tendance à être trop longues. Une correction dense de 15 lignes vaut mieux qu'un cours de 100 lignes. Va à l'essentiel, propose une seule question à la fois quand je sature.

---

## 6. PROBLÈME DE RECHERCHE — CADRAGE DE TRAVAIL

Mon point de départ était la concentration du marché actions américain autour de très grandes entreprises, dont plusieurs occupent une place importante dans l'écosystème de l'IA. Le travail actuel construit plus précisément un univers économique lié aux infrastructures de calcul. La concentration de l'indice reste un contexte possible ; elle ne définit pas à elle seule les futurs portefeuilles.

Nous ne commençons **pas** avec la conclusion « la concentration IA est dangereuse ». La question reste ouverte.

Formulation de départ, à reformuler après la construction de l'univers :

> « Dans quelle mesure la concentration d'un portefeuille dans les grandes entreprises liées à l'IA améliore-t-elle ou détériore-t-elle la rentabilité ajustée du risque de l'investisseur, et dans quelle mesure ce risque peut-il être maîtrisé par des stratégies de diversification et de couverture ? »

Formulation complémentaire :

> « How does the concentration of U.S. equity markets in AI-related mega-cap companies affect portfolio risk, diversification and risk-adjusted returns? »

Chaîne analysée :

```
CONCENTRATION → RENTABILITÉ → RISQUE → RAPPORT RENDEMENT/RISQUE
 → DIVERSIFICATION → COUVERTURE → RISQUE RÉSIDUEL
```

---

## 7. BUT DE RECHERCHE — VERSION DE TRAVAIL

Version de travail :

> « Ce projet vise à analyser les conséquences de la concentration des portefeuilles dans les entreprises exposées aux infrastructures de calcul liées à l'intelligence artificielle sur la performance et le risque de l'investisseur.
>
> Il cherchera à déterminer si les rendements obtenus sont cohérents avec les risques supportés, à identifier la nature et les sources de ces risques, puis à évaluer dans quelle mesure différentes stratégies de diversification et de couverture permettent de les réduire.
>
> L'analyse examinera également les coûts, les limites et les nouveaux risques éventuellement introduits par ces stratégies. »

Important mais **pas encore définitif**.

---

## 8. GRANDES QUESTIONS DU PROJET

1. La concentration dans les entreprises liées à l'IA apporte-t-elle réellement un supplément de rendement ?
2. Quel risque faut-il supporter pour obtenir ce rendement ?
3. Le rendement supplémentaire compense-t-il raisonnablement le risque supplémentaire ?
4. Que devient ce portefeuille dans les situations de marché défavorables ?
5. Peut-on réduire ces risques par diversification ou couverture sans détruire l'intérêt économique du portefeuille ?
6. Existe-t-il des risques qui ne peuvent pas être éliminés et doivent être compris, surveillés et acceptés ?

À affiner.

---

## 9. HYPOTHÈSES — ATTENTION AUX BIAIS

Nous avons une intuition, nous ne construisons pas l'analyse pour la confirmer.

**HYPOTHÈSE A — Concentration dangereuse.**
Ces entreprises sont exposées à des facteurs communs. Un choc commun produirait : corrélations élevées → pertes simultanées → diversification moins efficace → tail risk plus important.

**HYPOTHÈSE B — Concentration mais entreprises fondamentalement solides.**
Fortes marges, trésorerie abondante, positions dominantes, activités diversifiées, croissance. Une forte concentration ne signifie pas nécessairement un mauvais portefeuille.

**HYPOTHÈSE C — Le problème apparaît surtout en crise.**
En régime normal, diversification apparemment correcte ; en stress, corrélations en hausse, diversification qui s'efface, pertes extrêmes accrues.

Nous devons toujours pouvoir répondre : **« Qu'est-ce qui montrerait que notre hypothèse est fausse ? »**
Un résultat contraire à notre intuition doit être accepté et publié.

**RÈGLE :** nous avons le droit d'avoir une intuition avant de regarder les données. Nous n'avons pas le droit d'avoir une conclusion avant d'avoir fait l'analyse.

---

## 10. DISTINCTION SCIENTIFIQUE À RESPECTER

Toujours séparer :

| | Définition |
|---|---|
| **CE QUE NOUS SAVONS** | appuyé par théorie, données ou source |
| **CE QUE NOUS SUPPOSONS** | hypothèse non testée |
| **CE QUE NOUS OBSERVONS** | résultat empirique obtenu |
| **CE QUE NOUS INTERPRÉTONS** | explication possible du résultat |

Ne jamais transformer « j'observe X » en « Y cause X ». Corrélation ≠ causalité.

---

## 11. CONCEPTS CENTRAUX À DÉFINIR AVANT LA MÉTHODOLOGIE

Définitions **non encore verrouillées** :

rentabilité · rendement · risque · volatilité · concentration · diversification · couverture · rendement ajusté du risque · risque systématique · risque idiosyncratique · risque extrême · portefeuille « AI-related » · benchmark.

**Règle absolue :** dire « cette action est risquée » ne suffit jamais. Toujours demander **quel type de risque** : volatilité, drawdown, perte extrême, concentration, taux, liquidité, systématique, idiosyncratique, valorisation.

---

## 12. SÉLECTION DES ENTREPRISES — RÈGLE ACTUELLE

Je ne choisis pas une entreprise parce qu'elle est célèbre, parce que son action a monté ou parce qu'elle appartient à la technologie.

La sélection repose désormais sur une activité ou un engagement concret documenté dans la chaîne des infrastructures de calcul. Le CIK identifie l'entreprise ; les classes d'actions sont regroupées pour la revue économique. Le secteur et les symboles restent conservés.

Le classement de vocabulaire aide à lire les dossiers ; il ne décide pas des entrées. Une décision absente ou une preuve introuvable donne `A_EXAMINER`, jamais une exclusion automatique. Une exposition seulement possible reste `DOUTEUX`.

Les comptes décrivent l'évolution de l'entreprise à périmètre comparable. Ils ne prouvent pas que cette évolution vient de l'IA et ne servent pas de second filtre.

La version III de `research/selection_rule.md` définit les cas, les preuves, la maturité de l'exposition et les limites. La question de la sélection est donc opérationnelle ; celle de la construction des portefeuilles reste ouverte.

---

## 13. IMPORTANCE DES BENCHMARKS

Un chiffre de risque seul n'a pas de sens. « Volatilité = 22 % » → comparée à quoi ?

Comparaisons envisagées :

- S&P 500 market-cap weighted ;
- S&P 500 Equal Weight ;
- portefeuille AI / mega-cap concentré ;
- portefeuille diversifié ;
- éventuellement portefeuille actions + obligations ;
- éventuellement portefeuille couvert.

Benchmarks **non verrouillés**. Chacun devra avoir une justification scientifique (ex. : l'equal-weight isole l'effet de la pondération par capitalisation).

**Précision acquise :** le S&P 500 Equal Weight est un **benchmark de comparaison**, pas l'indice servant à décrire le phénomène. Ne pas confondre les deux rôles.

---

## 14. EXTENSION : OBLIGATIONS

Aller au-delà du 100 % actions, mais **seulement après** avoir compris le risque du portefeuille actions.

Vraie question de portfolio management : « Ajouter des obligations réduit-il réellement le risque du portefeuille concentré ? »

Comparaisons : 100 % actions vs 80/20 vs 60/40.

« Obligations = moins de risque » n'est **pas** une vérité automatique.

À apprendre : prix d'une obligation, yield, duration, convexité, risque de taux, éventuellement risque de crédit, corrélation actions-obligations, changement de régime de corrélation.

**Note issue d'une source primaire (FMI, avril 2026) :** l'institution documente une érosion de la relation de couverture actions-obligations sur la période post-pandémie, liée à des chocs d'offre plus fréquents, et un risque de désendettement simultané sur les deux classes d'actifs. Ce point renforce la pertinence du chapitre 7 : la corrélation actions-obligations n'est pas une constante.

---

## 15. EXTENSION : PRODUITS DÉRIVÉS / HEDGING

Question économique : « Si l'investisseur veut conserver son exposition IA mais limiter une forte baisse, peut-il transférer une partie du risque ? »

À étudier plus tard : puts, protective put, futures, éventuellement collars.

Chaque dérivé n'est introduit que s'il répond à une vraie question.

**Principe :** une couverture ne fait pas disparaître le risque. Elle le transfère, modifie le profil de payoff, coûte une prime, réduit certaines pertes et introduit d'autres risques.

Comparaison SANS HEDGE vs AVEC HEDGE : coût du hedge, réduction du drawdown, réduction de la VaR, réduction de l'ES, impact sur le rendement, risque résiduel, comportement selon les scénarios.

Comprendre aussi pourquoi un future est essentiellement linéaire et une option non linéaire. Cela pourra mener à : payoff, Black-Scholes si pertinent, volatilité implicite, delta, gamma, theta, vega — **seulement si le problème nous y conduit.**

---

## 16. GRAND CHEMIN ANALYTIQUE

```
PHASE A — Comprendre le portefeuille actions concentré
   ↓
PHASE B — Diversification, éventuellement ajout d'obligations
   ↓
PHASE C — Couverture par dérivés
   ↓
PHASE D — Comparaison des stratégies
   ↓
QUESTION FINALE : quelle stratégie offre quel profil rendement/risque,
à quel coût, dans quelles conditions, et quels risques restent non maîtrisables ?
```

---

## 17. MESURES POUVANT ÊTRE ÉTUDIÉES

Liste non définitive. Chaque mesure doit répondre à une question — ne pas tout utiliser automatiquement.

**Performance** — simple returns, log returns, cumulative returns, CAGR.

**Risque** — variance, écart-type, volatilité annualisée, downside volatility, maximum drawdown, VaR, Expected Shortfall, tail risk.

**Dépendance** — covariance, corrélation, évolution temporelle des corrélations, corrélations en période de stress.

**Concentration** — poids individuels, top-N concentration, HHI, effective number of holdings.

**Portfolio risk** — variance du portefeuille, matrice de covariance, marginal contribution to risk, component contribution to risk, risk budgeting.

**Rendement ajusté du risque** — Sharpe, Sortino, Calmar.

**Stress** — stress tests historiques, scénarios hypothétiques, choc technologique, choc de taux, choc de volatilité, chocs combinés.

**Simulation** — Monte Carlo, modèles de volatilité avancés plus tard.

---

## 18. PRINCIPES MATHÉMATIQUES

Je veux comprendre les formules en profondeur.

Exemple central — variance d'un portefeuille :

$$\sigma_p^2 = \mathbf{w}' \Sigma \mathbf{w}$$

Je veux comprendre : ce qu'est $\mathbf{w}$, ce qu'est $\Sigma$, ce qu'est une matrice de covariance, pourquoi les poids apparaissent, pourquoi les covariances apparaissent, comment la formule découle de la variance d'une somme, son intuition économique, et sa dérivation complète en annexe.

Trois niveaux :

| Niveau | Traitement |
|---|---|
| **Formule utilisée** | comprendre son sens |
| **Formule centrale** | comprendre profondément + dérivation |
| **Formule avancée** | annexe, si elle sert réellement le projet |

Ne jamais ajouter une équation pour « faire quantitatif ».

---

## 19. REVUE DE LITTÉRATURE

Pour chaque source, savoir répondre :

- Quelle question pose l'auteur ?
- Quelle est sa thèse ?
- Quelles données ? Quelle méthode ? Quelle période ?
- Quels résultats ? Quelles hypothèses ? Quelles limites ?
- Est-ce causal ou corrélationnel ?
- Quel intérêt pour notre projet ?
- Soutient-il, nuance-t-il ou contredit-il notre intuition ?

**Literature Matrix** — colonnes :

```
Source | Question | Méthode | Données | Période | Résultat | Limites | Utilité | Citation/notes
```

Ne pas lire passivement. Je raconterai parfois avec mes mots ce que j'ai compris d'un article ; tu corriges strictement.

---

## 20. TYPES DE SOURCES À PRIVILÉGIER

**Institutionnelles** — FMI, BIS, Federal Reserve, BCE, SEC, OCDE, Bank of England.

**Indices / marché** — S&P Dow Jones Indices, MSCI, Nasdaq.

**Entreprises** — 10-K, 10-Q, rapports annuels, investor relations, filings SEC.

**Académique** — articles peer-reviewed, NBER, SSRN avec prudence, working papers crédibles, littérature classique.

**Données** — sources fiables et reproductibles.

Toute information actuelle doit être vérifiée avec une source récente. Ne jamais réutiliser une ancienne affirmation si elle a pu changer.

---

## 21. DISCIPLINE SUR LES SOURCES

Toute décision importante doit avoir une justification écrite :

pourquoi 5 ans ? pourquoi 10 ans ? pourquoi daily ? pourquoi monthly ? pourquoi VaR 95 % ? pourquoi 99 % ? pourquoi telle entreprise ? pourquoi tel benchmark ? pourquoi tel ETF obligataire ? pourquoi tel dérivé ? pourquoi telle maturité ? pourquoi telle période de stress ?

Je dois pouvoir répondre à tout cela dans le rapport.

Ne jamais choisir un paramètre parce qu'il est « standard » sans expliquer pourquoi il est approprié **ici**.

---

## 22. BIAIS ET LIMITES À SURVEILLER

data snooping · look-ahead bias · survivorship bias · **selection bias** · confirmation bias · période historique choisie · changement de régime · estimation error · corrélation ≠ causalité · overfitting · biais introduits par la définition « AI-related » · biais de composition d'indice · changements de constituants · corporate actions · ajustements de prix · qualité des données · limites de la VaR · hypothèses de distribution · stabilité des corrélations · coûts de transaction · coût réel du hedging · liquidité · bid-ask spreads · fiscalité si pertinent.

Nous ne prétendons pas que notre modèle représente parfaitement la réalité.

---

## 23. EXPLORATION VERSUS VALIDATION

Distinguer **hypothèse prédéfinie** et **résultat exploratoire**.

Si nous découvrons dans les données quelque chose que nous n'avions pas prévu, nous pouvons l'analyser — mais il faut l'appeler *exploratory finding* et ne pas faire croire que nous l'avions prédit.

---

## 24. ARCHITECTURE DU RAPPORT LATEX — PROVISOIRE

1. **Introduction** — 1.1 Contexte · 1.2 Motivation · 1.3 Problématique · 1.4 Question de recherche · 1.5 Hypothèses · 1.6 Contributions · 1.7 Structure
2. **Revue de littérature** — 2.1 Concentration des marchés actions · 2.2 Essor de l'écosystème IA · 2.3 Concentration et diversification · 2.4 Risque et rendement · 2.5 Gestion du risque · 2.6 Lacunes et positionnement
3. **Cadre conceptuel** — 3.1 Rendement · 3.2 Risque · 3.3 Concentration · 3.4 Diversification · 3.5 Corrélation et covariance · 3.6 Risque systématique/idiosyncratique · 3.7 Rendement ajusté du risque · 3.8 Couverture
4. **Données** — 4.1 Univers d'investissement · 4.2 Définition d'une entreprise liée à l'IA · 4.3 Critères de sélection · 4.4 Sources · 4.5 Période d'étude · 4.6 Traitement · 4.7 Limites et biais
5. **Méthodologie** — 5.1 Construction des portefeuilles · 5.2 Mesures de concentration · 5.3 Performance · 5.4 Volatilité · 5.5 Covariance et corrélations · 5.6 Drawdown · 5.7 VaR · 5.8 Expected Shortfall · 5.9 Contribution au risque · 5.10 Performance ajustée du risque
6. **Analyse du portefeuille actions** — 6.1 Performance historique · 6.2 Concentration · 6.3 Sources du risque · 6.4 Dépendance entre entreprises · 6.5 Risques extrêmes
7. **Diversification par classes d'actifs** — 7.1 Pourquoi les obligations ? · 7.2 Risque de taux · 7.3 Portefeuilles mixtes · 7.4 Résultats · 7.5 Limites
8. **Couverture par dérivés** — 8.1 Objectif économique · 8.2 Instruments · 8.3 Options · 8.4 Coût de la protection · 8.5 Effet sur le profil rendement-risque · 8.6 Nouveaux risques
9. **Stress tests et scénarios** — 9.1 Choc technologique · 9.2 Choc de taux · 9.3 Choc de volatilité · 9.4 Chocs combinés · 9.5 Pertes extrêmes
10. **Comparaison des stratégies** — 10.1 Concentré · 10.2 Diversifié · 10.3 Couvert · 10.4 Coût vs réduction du risque · 10.5 Robustesse
11. **Discussion** — 11.1 Interprétation économique · 11.2 Hypothèses confirmées ou rejetées · 11.3 Implications pour l'investisseur · 11.4 Limites · 11.5 Recherche future
12. **Conclusion**

Cette table des matières est une carte, pas une prison.

---

## 25. ANNEXES ENVISAGÉES

- **A** — Fondements statistiques
- **B** — Dérivation de la variance d'un portefeuille
- **C** — Mesures de concentration
- **D** — Théorie de la VaR et de l'Expected Shortfall
- **E** — Fixed income : duration et convexité
- **F** — Théorie des options
- **G** — Modèles de volatilité
- **H** — Tests de robustesse
- **I** — Résultats supplémentaires

Contenu possible : démonstrations, formules, tests supplémentaires, tableaux complets, diagnostics, méthodologies alternatives, robustesse.

---

## 26. RÈGLE CONTRE LE DOCUMENT DE 600 PAGES INUTILES

> **Une notion entre dans le rapport principal uniquement si elle aide directement à répondre à une question de recherche.**

Sinon : annexe, notebook, notes de recherche, ou document d'apprentissage séparé.

Profondeur ≠ dispersion.

---

## 27. ARCHITECTURE GITHUB CIBLE

```
risk-modeling-project/
├── report/
│   ├── main.tex
│   ├── sections/
│   │   ├── 01_introduction.tex
│   │   ├── 02_literature_review.tex
│   │   ├── 03_conceptual_framework.tex
│   │   ├── 04_data.tex
│   │   ├── 05_methodology.tex
│   │   ├── 06_equity_analysis.tex
│   │   ├── 07_diversification.tex
│   │   ├── 08_hedging.tex
│   │   ├── 09_stress_testing.tex
│   │   ├── 10_results.tex
│   │   ├── 11_discussion.tex
│   │   └── 12_conclusion.tex
│   ├── appendices/
│   ├── figures/
│   └── tables/
├── notebooks/
│   ├── 01_data_collection.ipynb
│   ├── 02_exploratory_analysis.ipynb
│   ├── 03_concentration.ipynb
│   ├── 04_portfolio_risk.ipynb
│   ├── 05_bonds.ipynb
│   ├── 06_derivatives.ipynb
│   └── 07_stress_tests.ipynb
├── data/
│   ├── raw/
│   └── processed/
├── research/
│   ├── master_context.md        ← CE DOCUMENT
│   ├── research_charter.md
│   ├── project_state.md
│   ├── literature_matrix.csv
│   ├── methodology_log.md
│   └── decision_log.md
├── references/
│   └── references.bib
├── src/
├── README.md
└── .gitignore
```

**État au 5 septembre 2026 :** l'arborescence ci-dessus reste une cible, pas une liste de livrables existants. Le dépôt contient désormais les collectes, le classement textuel, le registre de sélection, le traitement comptable, les contrôles et la description des comptes dans `src/`, `data/` et `tests/`. Le README décrit les commandes réellement disponibles. Le rapport LaTeX et les modules de portefeuille restent à construire.

---

## 28. DOCUMENTS DE MÉMOIRE DU PROJET

Le projet ne doit pas dépendre de la mémoire d'un assistant.

| Fichier | Contenu |
|---|---|
| `master_context.md` | **ce document** — contexte complet, à recoller en début de conversation |
| `research_charter.md` | phénomène, problème, question, hypothèses, principes scientifiques |
| `project_state.md` | où nous en sommes, décisions, tâches faites, prochaine tâche, questions ouvertes |
| `literature_matrix.csv` | synthèse structurée des sources |
| `methodology_log.md` | pourquoi chaque choix méthodologique a été fait |
| `decision_log.md` | décisions importantes, alternatives, motifs de rejet |

Format du Decision Log :

```
Decision D-007
Décision    : Utiliser un benchmark equal-weighted.
Raison      : Isoler l'effet de la pondération par capitalisation.
Alternative : S&P 500 classique uniquement.
Rejet       : Ne permet pas d'isoler l'effet de concentration.
Date        : ...
```

---

## 29. LATEX VERSUS NOTEBOOKS

Le **rapport LaTeX** explique : pourquoi, théorie, méthode, résultats, interprétation.
Les **notebooks** montrent : calculs, données, implémentation, visualisations, tests.

Ne pas mettre chaque ligne de Python dans le rapport. Le rapport doit être lisible ; GitHub rend l'analyse reproductible.

---

## 30. JUPYTER / PYTHON / GITHUB — ÉTAT ACTUEL

Déjà en place : GitHub, Git local, Anaconda, Jupyter, Python. Dépôt `risk-modeling-project` créé et fonctionnel.

Workflow maîtrisé :

```
Jupyter → Ctrl+S → PowerShell → git add . → git commit -m "message" → git push → GitHub
```

Je comprends : repository, commit, push, README, `git clone`, `git status`, branche `main`.

**Ne recommence pas à m'expliquer Git comme si je n'avais jamais vu Git.**

Déjà fait et poussé : `risk_analysis.ipynb`, et un exercice minimal de workflow :

```python
initial_value = 1000
final_value = 900

loss = initial_value - final_value
loss_percentage = (loss / initial_value) * 100

print("Perte :", loss)
print("Perte en % :", loss_percentage)
```

Ce n'était **pas** le vrai projet de recherche, uniquement le workflow.

---

## 31. CODE

Le code de collecte et de préparation de l'univers existe maintenant. La commande `python -B src/run_pipeline.py` reconstruit les résultats locaux sans réseau ; les collectes restent séparées. Les tests portent sur les erreurs qui changeraient les décisions ou les comparaisons.

Le notebook initial et `main.py` restent des exercices de workflow. Ils ne calculent pas le risque de cet univers.

L'étape suivante ne consiste pas à ajouter immédiatement des modèles. Je dois d'abord relire les corrections, comprendre les cas douteux et préciser les portefeuilles, les périodes et les hypothèses que je veux comparer.

---

## 32. SOURCES WEB ET ACTUALITÉ

Le sujet est très actuel. Pour tout ce qui concerne la concentration actuelle du S&P 500, les poids, les entreprises IA, le capex IA, les valorisations, les conditions de marché, la composition d'indices : **cherche des sources web récentes et fiables**, ne te fie pas à ta mémoire.

Les affirmations évoquées dans les conversations précédentes (FMI, S&P 500, BIS) ne sont **pas** automatiquement validées. Vérifier les documents originaux avant usage dans le rapport.

**Distinction à respecter :** un résumé de moteur de recherche, un article de presse ou un site agrégateur ne sont **pas** des sources primaires. Ils servent à localiser le document original ; c'est le document original que l'on cite.

---

## 33. STYLE DE RECHERCHE

Le projet doit être défendable. Donc :

- pas de chiffres sans source ;
- pas d'entreprise sélectionnée arbitrairement ;
- pas de période arbitraire ;
- pas de conclusion avant les résultats ;
- pas de formule décorative ;
- pas de jargon inutile ;
- pas de modèle avancé pour impressionner.

Je préfère **un modèle simple parfaitement compris** à un modèle complexe copié sans compréhension. Mais si un modèle avancé devient pertinent, je veux pouvoir aller très loin.

**Corollaire acquis :** aucun texte n'est validé parce qu'il est bien écrit — ni celui d'un assistant, ni le mien. Tout ce qui entre dans le charter passe les trois tests du §39.

---

## 34. PROFONDEUR POTENTIELLE

```
STATISTIQUES (moyenne, variance, écart-type, covariance, corrélation,
distributions, moments, estimation, tests)
   ↓
PORTFOLIO THEORY (Markowitz, diversification, efficient frontier,
matrice de covariance, risk contribution)
   ↓
ASSET PRICING (bêta, CAPM, facteurs)
   ↓
RISK MANAGEMENT (VaR, ES, drawdown, stress testing, tail risk)
   ↓
FIXED INCOME (obligations, yields, duration, convexité, rate risk)
   ↓
DERIVATIVES (forwards, futures, options, payoff, Greeks, IV, hedging)
   ↓
ÉCONOMÉTRIE (rolling windows, changement de régime, GARCH,
simulations, modèles de dépendance)
```

Aucune de ces notions n'est ajoutée artificiellement.

---

## 35. CE QUE NOUS AVONS DÉCIDÉ SUR LA « CONCENTRATION »

Idée conceptuelle centrale :

> Un portefeuille peut contenir de nombreuses actions et être économiquement peu diversifié.

NVIDIA, Microsoft, Amazon, Meta, Alphabet : cinq entreprises, mais expositions potentiellement communes — IA, technologie, valorisations, taux, croissance, cloud, data centers, capex, semi-conducteurs, sentiment de marché.

$$\text{nombre d'actions} \neq \text{nombre de risques indépendants}$$

C'est une idée centrale **à tester**, pas à supposer.

**Formulation renforcée (acquise) :** un investisseur détenant un fonds indiciel large est *réputé* diversifié. Si les poids de l'indice se concentrent, cet investisseur devient concentré **sans avoir pris aucune décision**. C'est ce qui rend le phénomène non trivial : ce n'est pas un pari assumé, c'est le contenu du portefeuille « prudent » par défaut qui a changé.

---

## 36. RENDEMENT AJUSTÉ DU RISQUE

Question centrale : **« Le rendement obtenu est-il cohérent avec le risque pris ? »**

| | Rendement | Volatilité |
|---|---|---|
| Portefeuille A | 18 % | 32 % |
| Portefeuille B | 11 % | 14 % |

Le fait que A gagne plus ne suffit pas à dire qu'il est meilleur. Il faut regarder : rendement, volatilité, drawdown, tail risk, performance ajustée du risque, comportement en crise.

---

## 37. RÈGLE DE GESTION DU RISQUE

Le but du risk management n'est **pas** d'éliminer tout risque. Un portefeuille sans risque n'est pas l'objectif.

Les vraies questions : quel risque prenons-nous ? pourquoi ? quelle rémunération espérons-nous ? quels risques pouvons-nous diversifier ? lesquels couvrir ? à quel coût ? lesquels devons-nous accepter ? quel risque résiduel reste ?

---

# ═══ ACQUIS MÉTHODOLOGIQUES (nouveaux — session du 4 sept. 2026) ═══

---

## 38. LES TROIS BLOCS DU RESEARCH CHARTER

| Bloc | Nature | Contenu |
|---|---|---|
| 1. **Phenomenon of Interest** | fait observable | ce qui se passe dans le monde, indépendamment de moi |
| 2. **Research Problem** | difficulté intellectuelle | pourquoi ce fait pose un problème non résolu |
| 3. **Research Question** | question testable | ce que l'analyse cherchera à établir empiriquement |

Erreur la plus fréquente : écrire le phénomène + la question + le plan de travail en une seule phrase. Tant que le bloc 1 contient déjà la question, on ne peut pas vérifier que la question est fondée sur un fait.

**Règle :** le bloc 1 ne contient **aucun verbe d'investigation** (*savoir si, déterminer, analyser, impacter*) et **aucun mot de jugement** (*dangereux, excessif, risqué, insoutenable*). Uniquement des verbes de constat : *a augmenté, représente, s'élève à, est passé de… à…*.

---

## 39. LES TROIS TESTS DU PHÉNOMÈNE

Tout énoncé candidat au bloc 1 doit passer les trois :

**Test 1 — Neutralité.** Supprimer tous les mots de jugement. Si la phrase ne survit pas, ce n'était pas un phénomène mais une conclusion.

**Test 2 — Adversaire.** Un défenseur de l'hypothèse B doit pouvoir lire le paragraphe et dire « c'est factuellement exact ». Les hypothèses A, B, C s'opposent sur les *conséquences* ; elles doivent s'accorder sur le *phénomène*. Si l'adversaire conteste déjà le phénomène, une thèse s'y est glissée.

**Test 3 — Graphique.** Pour chaque affirmation, pouvoir dire : « je pourrais tracer ceci, avec cette donnée, sur cette période ». Pas le faire — pouvoir le dire.

---

## 40. CRITÈRE DE SÉPARATION PHÉNOMÈNE / RÉSULTAT

Critère opérationnel, à appliquer systématiquement :

> **Deux analystes honnêtes, partant des mêmes données brutes, obtiendraient-ils nécessairement le même chiffre ?**
> **Oui** → candidat pour le phénomène.
> **Non, cela dépend de choix méthodologiques** → c'est un résultat de l'analyse.

Formulation équivalente : **le phénomène existait avant que j'ouvre Python ; le résultat, c'est Python qui le produit.**

Un poids d'indice se **lit** (publié par S&P). Une corrélation se **fabrique** : il faut choisir la fréquence (quotidienne / hebdomadaire / mensuelle), la fenêtre (1 an / 3 ans / 10 ans), fixe ou glissante, l'estimateur. Chaque choix change le chiffre.

**Classement établi :**

| Élément | Statut |
|---|---|
| Poids des N premières composantes, daté | **Phénomène** |
| Nombre de sociétés dans l'indice | **Phénomène** |
| Capex déclaré dans un 10-K | **Phénomène** |
| Volatilité d'un portefeuille construit | **Résultat** |
| Max drawdown d'un portefeuille construit | **Résultat** |
| Part du rendement de l'indice attribuable au top-10 | **Résultat** (cas limite) |
| Corrélations entre les titres | **Résultat** — jamais dans le bloc 1 |

**Pourquoi les corrélations ne peuvent pas entrer dans le bloc 1 — trois raisons :**
1. elles sont calculées, pas observées (voir critère ci-dessus) ;
2. « les corrélations sont élevées » **est** l'hypothèse A : la poser en prémisse truque le match, et le Test 2 échoue ;
3. cela viderait le projet — si la conclusion figure dans le point de départ, les chapitres 6.4 et 6.5 ne feraient que redire la prémisse. Ce n'est plus une recherche, c'est une plaidoirie.

**Cas limite à surveiller :** « la part du rendement de l'indice attribuable aux 10 plus grosses composantes » ressemble à un fait publié, mais c'est le produit d'une méthode d'attribution (poids de début de période ou rebalancés ? *price return* ou *total return* ? les 10 plus grosses à quelle date ?). Choisir les 10 plus grosses en fin de période introduit en plus un look-ahead. À traiter comme contexte, pas comme cœur du phénomène.

---

## 41. PIÈGE DE CIRCULARITÉ SUR LA DÉFINITION « AI-RELATED »

**Le risque :** si l'on définit « entreprise IA » a posteriori, en partant de celles dont le cours a le plus monté, puis que l'on observe que « les entreprises IA ont beaucoup monté », on n'a rien observé. C'est une sélection sur la variable dépendante — un *selection bias*, et probablement la critique la plus dure qu'un professionnel adresserait au projet en soutenance.

**La parade retenue :** scinder le phénomène en deux composantes séparément vérifiables.

1. **La concentration par capitalisation** — mesurable sans définir quoi que ce soit ; les poids d'indice sont publiés et ne dépendent d'aucun jugement.
2. **Le lien avec l'IA** — documenté par les **fondamentaux** (capex, chiffre d'affaires, axes stratégiques déclarés dans les 10-K et 10-Q), **jamais par la performance boursière**.

Le lien IA devient ainsi quelque chose que l'on *documente*, pas quelque chose que l'on *présuppose*.

**Alternative envisagée puis mise en réserve :** partir d'un univers « IA » défini a priori par une source externe (ex. : un indice thématique de fournisseur). Défendable, mais rend le projet dépendant de la méthodologie d'un tiers, qu'il faudrait alors auditer et exposer.

---

## 42. PIÈGE DE LA CLASSIFICATION SECTORIELLE (GICS)

Dans le fichier local de composition, dont le rapprochement avec une source primaire datée reste à faire :

- **Alphabet** et **Meta** ne sont **pas** dans le secteur *Information Technology* → ils relèvent de *Communication Services* ;
- **Amazon** non plus → *Consumer Discretionary*.

**Conséquence :** mesurer le phénomène par « le poids du secteur technologique » **exclut mécaniquement trois des entreprises les plus centrales**. Le secteur officiel ne découpe pas le monde comme notre question de recherche.

C'est la raison de fond pour laquelle le §12 exige une règle de sélection documentée plutôt qu'un secteur tout fait : sans elle, on mesure autre chose que ce que l'on croit mesurer.

---

## 43. TRAITEMENT DES PÉRIODES

Je distingue trois périodes parce qu'elles ne répondent pas à la même question.

| Période | Rôle | Point à justifier |
|---|---|---|
| Observation du phénomène | Décrire une évolution historique | Disponibilité et comparabilité des observations |
| Estimation | Estimer les rendements et leurs dépendances | Taille de l'échantillon et changements de régime |
| Stress | Examiner des épisodes ou scénarios définis | Nature du choc et critères de sélection |

Une date de départ ne devient pas mauvaise uniquement parce qu'elle est récente, ni bonne parce qu'elle est ancienne. Elle doit correspondre à l'objet mesuré et être choisie pour une raison explicite. Une période récente offre moins de recul ; une période longue peut mélanger des entreprises et des régimes différents.

La fenêtre 2015–2026 reste une proposition de travail. Elle n'est pas encore un échantillon validé. Les épisodes de stress envisagés devront être datés, sourcés et sélectionnés selon des critères annoncés.

Le lancement public de ChatGPT avait été envisagé comme date de séparation. Cette date peut servir d'hypothèse de travail ; elle ne prouve pas à elle seule une rupture statistique. Il faudra distinguer un découpage motivé avant les tests d'une rupture découverte en cherchant celle qui produit le meilleur résultat.

Pour les comptes descriptifs déjà traités, la référence 2017–2019 et les éventuels replis sont propres à chaque mesure. Ces dates comptables ne fixent pas automatiquement les fenêtres de risque ou de performance.

Je prévois des variantes de fenêtre et je présenterai leur effet, y compris si elles fragilisent mon interprétation.

---

## 44. DÉCISIONS PROVISOIRES PRISES

**D-001 — Indice de référence pour décrire le phénomène : S&P 500.**
*Raison actuelle :* je pars d'un ensemble défini d'entreprises pour lequel les rapports réglementaires et la composition locale sont disponibles. Le S&P 500 pourra aussi servir de référence de marché pour des portefeuilles à définir. Sa détention ne garantit pas l'absence de concentration économique.
*Alternatives écartées :*
- **Nasdaq-100** — autre périmètre possible, avec des règles de composition différentes. Je ne peux pas l'écarter en supposant ce que pensent tous ses détenteurs ; il répondrait à une comparaison distincte à justifier.
- **Indice total market** (Russell 3000 / CRSP US Total Market) — argument sérieux (si la concentration persiste sur ~3000 titres, elle est plus difficile à attribuer à un artefact de sélection). Retenu comme **test de robustesse**, pas comme analyse principale.
- **S&P 500 Equal Weight** — n'est pas un candidat pour le bloc 1 : c'est un benchmark de comparaison (§13).
*Limite à assumer dans le rapport :* le S&P 500 n'est pas purement mécanique — un comité décide des inclusions selon des critères. Ce n'est pas disqualifiant, mais un lecteur exigeant le demandera ; on l'anticipe.
*Statut :* provisoire, à inscrire au `decision_log.md`.

**D-002 — Le lien IA sera documenté par les fondamentaux, pas par les cours.** Voir §41. *Statut :* acquis.

**D-003 — Les corrélations ne figurent pas dans le phénomène.** Voir §40. *Statut :* acquis.

---

## 45. SQUELETTE DU BLOC 1 (Phenomenon of Interest)

> **STATUT : PROPOSITION HISTORIQUE NON VALIDÉE.** Ce squelette porte sur la concentration de l'indice. Il devra être réécrit si je l'utilise dans le rapport, pour l'articuler avec l'univers économique actuellement construit. Il ne bloque plus la collecte et ne constitue pas une conclusion acquise. La valeur de N, la mesure de concentration, le point de comparaison historique et les chiffres restent à définir et à sourcer.

Structure envisagée : trois observations, chacune vérifiable séparément, aucune conclusion. Les crochets sont des trous à combler par des sources primaires.

> **Observation 1 — Concentration des poids.**
> Dans le S&P 500, la part de capitalisation représentée par les [N] plus grandes composantes est passée de [a] % en [date] à [b] % en [date]. *(Source : S&P Dow Jones Indices.)*
>
> **Observation 2 — Nature des entreprises concernées.**
> Ces entreprises déclarent dans leurs documents réglementaires des dépenses d'investissement en infrastructure de calcul en forte hausse sur la période, et identifient l'intelligence artificielle comme un axe stratégique. *(Source : 10-K, 10-Q.)*
>
> **Observation 3 — Conséquence mécanique pour l'investisseur passif.**
> Un investisseur détenant un fonds répliquant le S&P 500 voit son exposition à ce groupe d'entreprises passer de [a] % à [b] % sans avoir modifié son allocation.

Vérification : aucun mot de jugement ; un partisan de l'hypothèse B signe les trois lignes ; chaque ligne se trace ou se cite ; l'observation 2 documente le lien IA par les fondamentaux, pas par les cours.

**Ce que ce texte ne dit pas** — et ne doit pas dire : que c'est risqué, que les corrélations ont monté, que la diversification a disparu, qu'il faut se couvrir. Tout cela relève des chapitres 6 à 10.

---

## 46. SOURCES — ÉTAT DE VÉRIFICATION

### ✅ Vérifiée sur document primaire

**FMI — *Global Financial Stability Report*, avril 2026, chapitre 1.**
`https://www.imf.org/-/media/files/publications/gfsr/2026/april/english/ch1.pdf`

Éléments utilisables (lus dans le PDF, pages indiquées) :

- **Section « Contained Equity Market Correction amid High Concentration »** (p. 8-10) : la concentration est décrite comme élevée, un petit nombre d'entreprises pilotant de plus en plus les marchés actions ; l'optimisme des investisseurs sur les perspectives de long terme des technologies liées à l'IA en est un moteur clé.
- **Indice de Herfindahl–Hirschman** (p. 10) : pour deux des six grands marchés actions étudiés, le HHI dépasse actuellement son 95ᵉ percentile historique (Figure 1.7, panel 4).
- **Figure 1.7, panel 4 — « Concentration Risk Heat Map »** (p. 11) : z-score du HHI, données depuis 1990. Percentiles les plus récents : **USA 97,7** · KOR 99,7 · DEU 93,5 · GBR 78,8 · JPN 72,7 · FRA 55,9.
- **Deux canaux de risque distincts** (p. 10) : (i) une correction sur un petit nombre d'entreprises peut se propager à l'ensemble du marché ; (ii) le reste du monde est de plus en plus exposé aux actions américaines, ce qui propage le stress à travers les frontières par effets de richesse.
- **Note de la Figure 1.7** (p. 11) : définition retenue par le FMI du **Magnificent Seven** = Alphabet, Amazon, Apple, Meta, Microsoft, Nvidia, Tesla. Le **Bloomberg AI index** y est décrit comme suivant les 45 premières entreprises du cloud computing, des semi-conducteurs et du hardware orientés vers la prochaine génération de calcul. **→ Deux définitions institutionnelles d'univers exploitables pour le §12.**
- **Note de bas de page 9** (p. 10) : l'exposition des ménages américains aux actions représente environ 30 % de leurs actifs totaux. Le FMI rattache une grande partie de la hausse de cette exposition aux placements liés au S&P 500 ; cela ne signifie pas que la majorité du stock total de cette exposition soit détenue dans des véhicules passifs. Cette précision a été vérifiée dans le [chapitre 1 du GFSR d'avril 2026](https://www.imf.org/-/media/files/publications/gfsr/2026/april/english/ch1.pdf). **→ Appui pour l'Observation 3, sous cette formulation limitée.**
- **Note de bas de page 1** (p. 2) : définition des *hyperscalers* (fournisseurs de services cloud à grande échelle opérant de vastes infrastructures de data centers) ; certaines projections évoquent un investissement dépassant 3 400 milliards de dollars d'ici 2030.
- **Chapter 1 at a Glance** (p. 1) : des chocs d'offre plus fréquents ont érodé la relation de couverture actions-obligations, augmentant le risque de désendettement simultané sur les deux classes d'actifs. **→ Appui pour le chapitre 7.**

### ⚠ Non vérifiées — à confirmer sur source primaire avant tout usage

- Poids combiné des 10 premières composantes du S&P 500 (chiffres vus en source secondaire : ~38-40 % en 2025-2026 ; ~18-23 % entre 1990 et 2015). **La page S&P Dow Jones Indices renvoie une erreur 403 en accès automatisé** — il faudra récupérer le *factsheet* PDF mensuel manuellement, ou passer par une autre source primaire.
- Le chiffre « plus de 37 % » évoqué de mémoire : sans date ni définition, inutilisable. Préciser s'il s'agit du poids du secteur GICS *Information Technology*, du poids du top-10, ou d'un groupe défini par nous — ce sont trois grandeurs différentes.
- Affirmations issues des conversations précédentes concernant le FMI, la BIS et le S&P 500 : **non validées**, à revérifier une par une.

### À consulter ensuite

- S&P Dow Jones Indices — *factsheet* mensuel du S&P 500 et publications de recherche sur la concentration.
- BIS — *Quarterly Review*.
- Federal Reserve — *Financial Stability Report*.
- Bank of England — *Financial Stability Report* (juillet 2026 identifié).
- 10-K des entreprises retenues, pour le capex et les axes stratégiques.

---

## 47. ÉTAT EXACT DU PROJET (project_state)

**Date : 5 septembre 2026. Étape : univers économique documenté et description comptable, après correction méthodologique.**

J'ai dépassé le stade où aucune donnée et aucun code n'existaient. La composition locale de l'indice, les rapports SEC, leurs passages, les comptes et un registre de revue sont présents. La règle de sélection a été rendue explicite et ses erreurs connues sont corrigées ou signalées.

**Ce qui est fait :**

- sauvegarde des documents, scripts et données antérieurs, avec empreintes ;
- classement textuel reproductible et revue conservant tous les CIK ;
- décisions rattachées à une preuve documentaire, avec un statut lorsque la preuve manque ;
- retraitement des notions et périmètres comptables connus, sans remplir artificiellement les lacunes ;
- description des comptes avec dates de référence par mesure et couverture séparée ;
- contrôles automatiques, tests et manifeste reliant les résultats à leurs entrées ;
- documentation réécrite pour distinguer faits, choix exploratoires et hypothèses.

Les effectifs courants doivent être lus dans `data/processed/etat_projet.json` ou dans la note sur l'univers. Les anciens nombres ne sont plus les résultats de référence.

**Ce qui reste limité :**

La revue documentaire porte sur les passages extraits et les lectures complémentaires consignées, pas sur un audit intégral de tous les rapports. Les cas `DOUTEUX` et `A_EXAMINER` restent visibles. Les alertes comptables appellent une lecture ; leur présence ne signifie pas que toutes les valeurs sont fausses. La composition d'indice issue d'une source secondaire reste à rapprocher d'une source officielle datée.

La photographie actuelle n'est pas un univers historique disponible sans anticipation. Les comptes peuvent avoir été retraités après leur période. La contribution propre de l'IA et la réaction des cours ne sont pas encore mesurées.

**La question de cadrage a évolué :**

L'ancien choix entre « concentration des mégacapitalisations dans l'indice » et « portefeuille d'entreprises IA » n'est plus un blocage préalable à toute donnée. Le travail réalisé construit un univers économique lié à l'infrastructure, susceptible d'alimenter plusieurs portefeuilles. La concentration de l'indice peut servir de contexte ou de comparaison, mais elle ne remplace pas silencieusement cet objet.

Je ne suppose pas que toutes les entreprises de l'univers seront dans le même portefeuille. Je n'ai pas encore choisi la taille, les pondérations ni une méthode de simulation. Une éventuelle simulation Monte Carlo devra répondre à une question définie, avec des hypothèses contrôlées.

**La prochaine étape :**

Je relis les corrections et les décisions, notamment les changements de sélection et les comparaisons devenues non calculables. Ensuite je fixe la question empirique, les portefeuilles et les benchmarks. Avant un résultat historique de performance, il faudra définir les périodes, la disponibilité des informations, les règles de rebalancement et les données de prix.

**Ce qui n'a pas commencé :**

L'estimation du risque boursier de cet univers, la construction et l'optimisation des portefeuilles, la simulation de scénarios, l'évaluation des couvertures et le rapport LaTeX.

Le dépôt fait foi. Un assistant peut proposer et contrôler ; il ne doit pas présenter une hypothèse comme ma décision ni un calcul descriptif comme un résultat de portefeuille.

---

## 48. COMMENT REPRENDRE AVEC MOI

Ne me fais pas un résumé géant de ce document. Dis simplement que tu as compris où nous en sommes, puis reprends à la **tâche immédiate en attente** du §47.

Tu peux : proposer une formulation, me demander ce que je veux dire, me demander de reformuler avec mes mots, discuter des termes, identifier les présupposés, corriger mon raisonnement.

Le but est que **je** comprenne réellement ce que nous écrivons.

À la fin de chaque étape importante, aide-moi à mettre à jour le §47 : ce qui a été décidé, ce qui reste ouvert, la prochaine action. Si je demande « où on en est ? », utilise cette structure.

---

## 49. RÈGLE FINALE

Ce projet doit être :

**RIGOUREUX** mais pas artificiellement compliqué.
**PROFOND** mais pas dispersé.
**QUANTITATIF** mais économiquement interprétable.
**ACTUEL** mais historiquement contextualisé.
**DOCUMENTÉ** mais pas rempli de citations inutiles.
**REPRODUCTIBLE** mais pas réduit au code.
**AMBITIEUX** mais méthodologiquement honnête.

Et surtout : **je dois comprendre ce que je fais.**

Nous construisons un projet que je serais capable de défendre devant quelqu'un qui connaît réellement la finance.

**FIN DU CONTEXTE MAÎTRE.**
