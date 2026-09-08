# Journal de vérification et de correction : finition

*État historique de la finition avant l'amendement A-08 : les chiffres ci-dessous décrivent l'univers alors validé de 130 entreprises. L’[ajout du 8 septembre 2026](decisions_auteur_2026-09-08.md) consigne les décisions désormais tranchées et le recalcul courant sur 134 entreprises. Les anciennes options ci-dessous ne sont plus réservées.*

*8 septembre 2026. Le journal antérieur est conservé intégralement dans `archive/2026-09-08_avant_finition/journal_verification_etape_2.md`.*

## I. Ordre des travaux

Fermeture des 114 dossiers, acquisition des 17 nouveaux historiques, instruction des distributions et continuités, reconstruction, exécution propre du carnet, rédaction à partir des données, vérification transversale et commit. Les notes de travail sont hors dépôt. Le registre de sélection et les sorties reconstruites portent 130 ENTRE et 370 SORT, sans dossier en attente.

Les jugements préexistants sont conservés ; quatre nouvelles bornes s'ajoutent aux trois déjà écrites. La seule nouvelle correction de versement concerne HD. La correction JCI 2007 reste contrôlée mais n'est plus utilisée dans la période admissible. Le rapport `finition_etapes_1_et_2.md` expose les pièces et les raisons, sans rouvrir les corrections closes.

## II. Résultats vérifiés

Les 500 empreintes et positions de citation sont vérifiées, les 386 anciennes décisions sont identiques cellule par cellule, les 2 647 éléments protégés sont inchangés. Les 103 tests réussissent. Les quatre cellules du carnet sous Python 3.12.14 retrouvent les 18 sorties de la commande sous Python 3.13.9. Les vingt identités de richesse quotidiennes et les frais se raccordent à la tolérance de 10⁻¹². Les deux partitions d'entreprises sont exactes.

| Groupe | Entreprises initiales | Entreprises finales | Titres finaux |
| --- | --- | --- | --- |
| P1 | 87 | 130 | 131 |
| P2 | 68 | 109 | 110 |
| P3 | 19 | 21 | 21 |
| P4 | 4 | 10 | 11 |
| P5 | 19 | 34 | 34 |
| P6 | 20 | 23 | 23 |
| P7 | 20 | 28 | 28 |
| P8 | 3 | 7 | 7 |
| P9 | 8 | 13 | 13 |
| P10 | 13 | 15 | 15 |


| Série | Base 100 finale | Annualisé | Rotation annuelle | Effet des frais, pb/an | Repli maximal |
| --- | --- | --- | --- | --- | --- |
| P1_reeq | 9 991,06 | 18,88 % | 25,07 % | 2,98 | -51,69 % |
| P1_cons | 10 018,86 | 18,90 % | 4,60 % | 0,55 | -53,07 % |
| P10_reeq | 3 662,96 | 14,49 % | 18,41 % | 2,11 | -56,82 % |
| P10_cons | 5 626,77 | 16,35 % | 2,64 % | 0,31 | -62,18 % |
| P2_reeq | 10 990,93 | 19,31 % | 25,97 % | 3,10 | -55,54 % |
| P2_cons | 10 903,34 | 19,27 % | 4,81 % | 0,57 | -55,10 % |
| P3_reeq | 3 917,48 | 14,77 % | 17,27 % | 1,98 | -44,82 % |
| P3_cons | 4 357,12 | 15,23 % | 3,45 % | 0,40 | -51,54 % |
| P4_reeq | 47 977,33 | 26,10 % | 36,25 % | 4,57 | -70,60 % |
| P4_cons | 5 902,89 | 16,56 % | 7,02 % | 0,82 | -86,53 % |
| P5_reeq | 15 476,45 | 20,85 % | 30,49 % | 3,69 | -72,64 % |
| P5_cons | 25 576,60 | 23,16 % | 4,91 % | 0,60 | -73,08 % |
| P6_reeq | 2 032,55 | 11,98 % | 13,06 % | 1,46 | -44,99 % |
| P6_cons | 1 923,69 | 11,75 % | 4,33 % | 0,48 | -44,62 % |
| P7_reeq | 7 656,17 | 17,70 % | 17,21 % | 2,03 | -54,02 % |
| P7_cons | 7 419,05 | 17,56 % | 3,82 % | 0,45 | -53,75 % |
| P8_reeq | 6 731,43 | 17,13 % | 25,63 % | 3,00 | -64,52 % |
| P8_cons | 2 588,94 | 13,00 % | 8,56 % | 0,97 | -59,65 % |
| P9_reeq | 5 007,99 | 15,84 % | 23,51 % | 2,72 | -72,34 % |
| P9_cons | 2 284,38 | 12,47 % | 4,19 % | 0,47 | -73,13 % |


Nasdaq couvre 60 titres et 144 990 clôtures. Les 30 écarts de rendement supérieurs à dix points de base se répartissent entre cinq hors historique admissible, douze liés à des conventions d'opération ou à leur veille, deux cours Nasdaq figés déjà documentés, deux rendements SBAC autour d'un cours porté et neuf non arbitrés. Sur 110 extrêmes du brut depuis 2000, 102 sont dans un historique admissible : vingt concordants et 82 non corroborés. Les listes finies ne sont pas effacées par la clôture.

## III. Modifications

- `.gitignore` : dépendance nécessaire aux livrables des deux premières étapes (travail antérieur conservé et intégré).
- `README.md` : état courant, résultats et limites réconciliés avec les données finales (modifié pendant la finition).
- `data/processed/appartenance.csv` : résultat dérivé ou manifeste reconstruit depuis les entrées finales (modifié pendant la finition).
- `data/processed/classification_manuelle.csv` : résultat dérivé ou manifeste reconstruit depuis les entrées finales (modifié pendant la finition).
- `data/processed/controle_divisions_sec.csv` : résultat dérivé ou manifeste reconstruit depuis les entrées finales (modifié pendant la finition).
- `data/processed/controle_prix.csv` : résultat dérivé ou manifeste reconstruit depuis les entrées finales (modifié pendant la finition).
- `data/processed/controles_portefeuilles.json` : résultat dérivé ou manifeste reconstruit depuis les entrées finales (modifié pendant la finition).
- `data/processed/corroboration.csv` : résultat dérivé ou manifeste reconstruit depuis les entrées finales (modifié pendant la finition).
- `data/processed/corroboration_details.csv` : résultat dérivé ou manifeste reconstruit depuis les entrées finales (modifié pendant la finition).
- `data/processed/corroboration_sensibilite.csv` : résultat dérivé ou manifeste reconstruit depuis les entrées finales (modifié pendant la finition).
- `data/processed/couverture_controle_prix.json` : résultat dérivé ou manifeste reconstruit depuis les entrées finales (modifié pendant la finition).
- `data/processed/dividendes.csv` : résultat dérivé ou manifeste reconstruit depuis les entrées finales (modifié pendant la finition).
- `data/processed/etat_projet.json` : résultat dérivé ou manifeste reconstruit depuis les entrées finales (modifié pendant la finition).
- `data/processed/journal_portefeuilles.csv` : résultat dérivé ou manifeste reconstruit depuis les entrées finales (modifié pendant la finition).
- `data/processed/mesures_portefeuilles.csv` : résultat dérivé ou manifeste reconstruit depuis les entrées finales (modifié pendant la finition).
- `data/processed/operations_reportees.csv` : résultat dérivé ou manifeste reconstruit depuis les entrées finales (travail antérieur conservé et intégré).
- `data/processed/pipeline_manifest.json` : résultat dérivé ou manifeste reconstruit depuis les entrées finales (modifié pendant la finition).
- `data/processed/pipeline_portefeuilles.json` : résultat dérivé ou manifeste reconstruit depuis les entrées finales (modifié pendant la finition).
- `data/processed/pipeline_status.json` : résultat dérivé ou manifeste reconstruit depuis les entrées finales (modifié pendant la finition).
- `data/processed/poids_cibles.csv` : résultat dérivé ou manifeste reconstruit depuis les entrées finales (modifié pendant la finition).
- `data/processed/poids_mensuels.csv` : résultat dérivé ou manifeste reconstruit depuis les entrées finales (modifié pendant la finition).
- `data/processed/qualite_valorisation.csv` : résultat dérivé ou manifeste reconstruit depuis les entrées finales (modifié pendant la finition).
- `data/processed/rendements_prix.csv` : résultat dérivé ou manifeste reconstruit depuis les entrées finales (modifié pendant la finition).
- `data/processed/rendements_valorisation.csv` : résultat dérivé ou manifeste reconstruit depuis les entrées finales (modifié pendant la finition).
- `data/processed/resume_controle_prix.csv` : résultat dérivé ou manifeste reconstruit depuis les entrées finales (modifié pendant la finition).
- `data/processed/synthese_resultats.md` : résultat dérivé ou manifeste reconstruit depuis les entrées finales (modifié pendant la finition).
- `data/processed/univers_retenu.csv` : résultat dérivé ou manifeste reconstruit depuis les entrées finales (modifié pendant la finition).
- `data/processed/valeurs_comparaisons.csv` : résultat dérivé ou manifeste reconstruit depuis les entrées finales (travail antérieur conservé et intégré).
- `data/processed/valeurs_comparaisons_yahoo.csv` : résultat dérivé ou manifeste reconstruit depuis les entrées finales (travail antérieur conservé et intégré).
- `data/processed/valeurs_portefeuilles.csv` : résultat dérivé ou manifeste reconstruit depuis les entrées finales (modifié pendant la finition).
- `data/raw/metadonnees_titres.csv` : 17 descriptions ajoutées, anciennes lignes conservées (modifié pendant la finition).
- `data/raw/prix/ACN.csv` : nouvelle série, acquisition sans écrasement et empreinte enregistrée (créé pendant la finition).
- `data/raw/prix/APD.csv` : nouvelle série, acquisition sans écrasement et empreinte enregistrée (créé pendant la finition).
- `data/raw/prix/APP.csv` : nouvelle série, acquisition sans écrasement et empreinte enregistrée (créé pendant la finition).
- `data/raw/prix/EMR.csv` : nouvelle série, acquisition sans écrasement et empreinte enregistrée (créé pendant la finition).
- `data/raw/prix/EXPD.csv` : nouvelle série, acquisition sans écrasement et empreinte enregistrée (créé pendant la finition).
- `data/raw/prix/FSLR.csv` : nouvelle série, acquisition sans écrasement et empreinte enregistrée (créé pendant la finition).
- `data/raw/prix/HD.csv` : nouvelle série, acquisition sans écrasement et empreinte enregistrée (créé pendant la finition).
- `data/raw/prix/ITW.csv` : nouvelle série, acquisition sans écrasement et empreinte enregistrée (créé pendant la finition).
- `data/raw/prix/LDOS.csv` : nouvelle série, acquisition sans écrasement et empreinte enregistrée (créé pendant la finition).
- `data/raw/prix/NDAQ.csv` : nouvelle série, acquisition sans écrasement et empreinte enregistrée (créé pendant la finition).
- `data/raw/prix/NDSN.csv` : nouvelle série, acquisition sans écrasement et empreinte enregistrée (créé pendant la finition).
- `data/raw/prix/NEE.csv` : nouvelle série, acquisition sans écrasement et empreinte enregistrée (créé pendant la finition).
- `data/raw/prix/NOW.csv` : nouvelle série, acquisition sans écrasement et empreinte enregistrée (créé pendant la finition).
- `data/raw/prix/NXPI.csv` : nouvelle série, acquisition sans écrasement et empreinte enregistrée (créé pendant la finition).
- `data/raw/prix/PH.csv` : nouvelle série, acquisition sans écrasement et empreinte enregistrée (créé pendant la finition).
- `data/raw/prix/QCOM.csv` : nouvelle série, acquisition sans écrasement et empreinte enregistrée (créé pendant la finition).
- `data/raw/prix/SBAC.csv` : nouvelle série, acquisition sans écrasement et empreinte enregistrée (créé pendant la finition).
- `data/raw/prix_manifest.json` : inventaire augmenté et révisions de collecte, anciennes empreintes conservées (modifié pendant la finition).
- `data/review/comptabilite_controle_manifest.json` : décision de revue, couverture ou vérification documentée (modifié pendant la finition).
- `data/review/continuite_examinee_2026-09-08.csv` : décision de revue, couverture ou vérification documentée (créé pendant la finition).
- `data/review/corrections_evenements_prix.json` : décision de revue, couverture ou vérification documentée (modifié pendant la finition).
- `data/review/couverture_selection_finition_2026-09-08.csv` : décision de revue, couverture ou vérification documentée (créé pendant la finition).
- `data/review/decisions_finition_2026-09-08.csv` : verdicts et preuves de sélection par CIK (créé pendant la finition).
- `data/review/decisions_selection.csv` : verdicts et preuves de sélection par CIK (modifié pendant la finition).
- `data/review/decisions_sources_complementaires.csv` : verdicts et preuves de sélection par CIK (créé pendant la finition).
- `data/review/divergences_finition_2026-09-08.csv` : décision de revue, couverture ou vérification documentée (créé pendant la finition).
- `data/review/evenements_prix_documentes.csv` : décision de revue, couverture ou vérification documentée (modifié pendant la finition).
- `data/review/finition_verifications_2026-09-08.json` : décision de revue, couverture ou vérification documentée (créé pendant la finition).
- `data/review/regles_historiques_prix.csv` : décision de revue, couverture ou vérification documentée (modifié pendant la finition).
- `data/review/sources_cloture_2026-09-08/bilan.json` : preuve ou résultat du rapprochement externe, conservé avec sa portée (modifié pendant la finition).
- `data/review/sources_cloture_2026-09-08/comparaison_cours.csv` : preuve ou résultat du rapprochement externe, conservé avec sa portée (modifié pendant la finition).
- `data/review/sources_cloture_2026-09-08/couverture.csv` : preuve ou résultat du rapprochement externe, conservé avec sa portée (modifié pendant la finition).
- `data/review/sources_cloture_2026-09-08/divergences.csv` : preuve ou résultat du rapprochement externe, conservé avec sa portée (modifié pendant la finition).
- `data/review/sources_cloture_2026-09-08/divergences_qualifiees.csv` : preuve ou résultat du rapprochement externe, conservé avec sa portée (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/impact_corrections.csv` : preuve ou résultat du rapprochement externe, conservé avec sa portée (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_ACN.json` : preuve de seconde source ou inventaire de ses empreintes (créé pendant la finition).
- `data/review/sources_cloture_2026-09-08/nasdaq_AES.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_AKAM.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_AMD.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_AMT.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_AMZN.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_APD.json` : preuve de seconde source ou inventaire de ses empreintes (créé pendant la finition).
- `data/review/sources_cloture_2026-09-08/nasdaq_APP.json` : preuve de seconde source ou inventaire de ses empreintes (créé pendant la finition).
- `data/review/sources_cloture_2026-09-08/nasdaq_CBRE.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_CDNS.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_CIEN.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_CNP.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_COHR.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_DELL.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_DTE.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_EMR.json` : preuve de seconde source ou inventaire de ses empreintes (créé pendant la finition).
- `data/review/sources_cloture_2026-09-08/nasdaq_EQIX.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_EXPD.json` : preuve de seconde source ou inventaire de ses empreintes (créé pendant la finition).
- `data/review/sources_cloture_2026-09-08/nasdaq_FIX.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_FLEX.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_FSLR.json` : preuve de seconde source ou inventaire de ses empreintes (créé pendant la finition).
- `data/review/sources_cloture_2026-09-08/nasdaq_GLW.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_HAL.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_HD.json` : preuve de seconde source ou inventaire de ses empreintes (créé pendant la finition).
- `data/review/sources_cloture_2026-09-08/nasdaq_HPE.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_IBM.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_ITW.json` : preuve de seconde source ou inventaire de ses empreintes (créé pendant la finition).
- `data/review/sources_cloture_2026-09-08/nasdaq_JBL.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_JCI.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_LDOS.json` : preuve de seconde source ou inventaire de ses empreintes (créé pendant la finition).
- `data/review/sources_cloture_2026-09-08/nasdaq_LITE.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_MMM.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_MRVL.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_NDAQ.json` : preuve de seconde source ou inventaire de ses empreintes (créé pendant la finition).
- `data/review/sources_cloture_2026-09-08/nasdaq_NDSN.json` : preuve de seconde source ou inventaire de ses empreintes (créé pendant la finition).
- `data/review/sources_cloture_2026-09-08/nasdaq_NEE.json` : preuve de seconde source ou inventaire de ses empreintes (créé pendant la finition).
- `data/review/sources_cloture_2026-09-08/nasdaq_NOW.json` : preuve de seconde source ou inventaire de ses empreintes (créé pendant la finition).
- `data/review/sources_cloture_2026-09-08/nasdaq_NTAP.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_NVDA.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_NXPI.json` : preuve de seconde source ou inventaire de ses empreintes (créé pendant la finition).
- `data/review/sources_cloture_2026-09-08/nasdaq_O.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_ON.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_ORCL.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_PH.json` : preuve de seconde source ou inventaire de ses empreintes (créé pendant la finition).
- `data/review/sources_cloture_2026-09-08/nasdaq_PLD.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_PWR.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_QCOM.json` : preuve de seconde source ou inventaire de ses empreintes (créé pendant la finition).
- `data/review/sources_cloture_2026-09-08/nasdaq_RSP.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_SBAC.json` : preuve de seconde source ou inventaire de ses empreintes (créé pendant la finition).
- `data/review/sources_cloture_2026-09-08/nasdaq_SMCI.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_SNDK.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_SNPS.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_SPY.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_SWKS.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_TDY.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_TSLA.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_VRT.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_WDC.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_WMB.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_XEL.json` : preuve de seconde source ou inventaire de ses empreintes (travail antérieur conservé et intégré).
- `data/review/sources_cloture_2026-09-08/nasdaq_manifest.json` : preuve de seconde source ou inventaire de ses empreintes (modifié pendant la finition).
- `data/review/sources_cloture_2026-09-08/variations_examines.csv` : preuve ou résultat du rapprochement externe, conservé avec sa portée (modifié pendant la finition).
- `data/review/sources_cloture_2026-09-08/verification_manifest.json` : preuve ou résultat du rapprochement externe, conservé avec sa portée (travail antérieur conservé et intégré).
- `data/review/sources_finition_2026-09-08/HONA.txt` : extrait complémentaire de la notice officielle de séparation, pas un rapport complet (créé pendant la finition).
- `data/review/variations_finition_2026-09-08.csv` : décision de revue, couverture ou vérification documentée (créé pendant la finition).
- `outputs/01a0708c-acb3-72c2-885a-9b76b6070a14/apercus/Lecture_et_sources.png` : export et contrôles de livraison actualisés sur 130 entreprises (modifié pendant la finition).
- `outputs/01a0708c-acb3-72c2-885a-9b76b6070a14/apercus/Par_canal.png` : export et contrôles de livraison actualisés sur 130 entreprises (modifié pendant la finition).
- `outputs/01a0708c-acb3-72c2-885a-9b76b6070a14/apercus/Par_secteur.png` : export et contrôles de livraison actualisés sur 130 entreprises (modifié pendant la finition).
- `outputs/01a0708c-acb3-72c2-885a-9b76b6070a14/apercus/Recapitulatif.png` : export et contrôles de livraison actualisés sur 130 entreprises (modifié pendant la finition).
- `outputs/01a0708c-acb3-72c2-885a-9b76b6070a14/univers_retenu.json` : export et contrôles de livraison actualisés sur 130 entreprises (modifié pendant la finition).
- `outputs/01a0708c-acb3-72c2-885a-9b76b6070a14/univers_retenu.xlsx` : export et contrôles de livraison actualisés sur 130 entreprises (modifié pendant la finition).
- `outputs/01a0708c-acb3-72c2-885a-9b76b6070a14/univers_retenu.xlsx.inspect.ndjson` : export et contrôles de livraison actualisés sur 130 entreprises (modifié pendant la finition).
- `outputs/01a0708c-acb3-72c2-885a-9b76b6070a14/verification_livraison.json` : export et contrôles de livraison actualisés sur 130 entreprises (modifié pendant la finition).
- `research/archive/2026-09-08_avant_finition/README.md` : état antérieur conservé pour distinguer ses chiffres des résultats courants (créé pendant la finition).
- `research/archive/2026-09-08_avant_finition/audit_etape_2.md` : état antérieur conservé pour distinguer ses chiffres des résultats courants (créé pendant la finition).
- `research/archive/2026-09-08_avant_finition/controle_donnees_prix.md` : état antérieur conservé pour distinguer ses chiffres des résultats courants (créé pendant la finition).
- `research/archive/2026-09-08_avant_finition/journal_verification_etape_2.md` : état antérieur conservé pour distinguer ses chiffres des résultats courants (créé pendant la finition).
- `research/archive/2026-09-08_avant_finition/master_context.md` : état antérieur conservé pour distinguer ses chiffres des résultats courants (créé pendant la finition).
- `research/archive/2026-09-08_avant_finition/plan_projet.md` : état antérieur conservé pour distinguer ses chiffres des résultats courants (créé pendant la finition).
- `research/archive/2026-09-08_avant_finition/portefeuilles.md` : état antérieur conservé pour distinguer ses chiffres des résultats courants (créé pendant la finition).
- `research/archive/2026-09-08_avant_finition/univers_selection.md` : état antérieur conservé pour distinguer ses chiffres des résultats courants (créé pendant la finition).
- `research/archive/2026-09-08_avant_finition/verification_etape_2.md` : état antérieur conservé pour distinguer ses chiffres des résultats courants (créé pendant la finition).
- `research/audit_etape_2.md` : état courant, résultats et limites réconciliés avec les données finales (modifié pendant la finition).
- `research/cas_de_test.md` : état courant, résultats et limites réconciliés avec les données finales (travail antérieur conservé et intégré).
- `research/controle_donnees_prix.md` : état courant, résultats et limites réconciliés avec les données finales (modifié pendant la finition).
- `research/finition_etapes_1_et_2.md` : état courant, résultats et limites réconciliés avec les données finales (rapport de finition).
- `research/journal_verification_etape_2.md` : état courant, résultats et limites réconciliés avec les données finales (rapport de finition).
- `research/master_context.md` : état courant, résultats et limites réconciliés avec les données finales (modifié pendant la finition).
- `research/plan_projet.md` : état courant, résultats et limites réconciliés avec les données finales (modifié pendant la finition).
- `research/portefeuilles.md` : état courant, résultats et limites réconciliés avec les données finales (modifié pendant la finition).
- `research/univers_selection.md` : état courant, résultats et limites réconciliés avec les données finales (modifié pendant la finition).
- `research/verification_etape_2.md` : état courant, résultats et limites réconciliés avec les données finales (modifié pendant la finition).
- `src/classification_manuelle.py` : chargement contrôlé du complément lorsque le corpus initial ne contient aucun rapport (modifié pendant la finition).
- `src/collecter_prix.ipynb` : traitement ou carnet de l’étape 2 issu des corrections précédentes et intégré au commit (travail antérieur conservé et intégré).
- `src/construire_portefeuille.ipynb` : quatre cellules exécutées dans un processus neuf, sorties et version Python enregistrées (modifié pendant la finition).
- `src/construire_portefeuilles.py` : corrections de preuve vérifiées avant la coupe des historiques admissibles (modifié pendant la finition).
- `src/controle_prix.py` : traitement ou carnet de l’étape 2 issu des corrections précédentes et intégré au commit (travail antérieur conservé et intégré).
- `src/controler_prix.ipynb` : traitement ou carnet de l’étape 2 issu des corrections précédentes et intégré au commit (travail antérieur conservé et intégré).
- `src/corrections_prix.py` : traitement ou carnet de l’étape 2 issu des corrections précédentes et intégré au commit (travail antérieur conservé et intégré).
- `src/export_univers_excel.mjs` : export courant conservant la structure existante et les sources (modifié pendant la finition).
- `src/export_univers_excel.py` : export courant conservant la structure existante et les sources (travail antérieur conservé et intégré).
- `src/portefeuille.py` : traitement ou carnet de l’étape 2 issu des corrections précédentes et intégré au commit (travail antérieur conservé et intégré).
- `src/recouper_prix.py` : traitement ou carnet de l’étape 2 issu des corrections précédentes et intégré au commit (travail antérieur conservé et intégré).
- `src/run_pipeline.py` : rattachement des sources complémentaires au manifeste de l’étape 1 (modifié pendant la finition).
- `tests/test_audit_portefeuilles.py` : régression protégeant les corrections ; suite complète réussie (travail antérieur conservé et intégré).
- `tests/test_complement_selection.py` : régression protégeant les corrections ; suite complète réussie (créé pendant la finition).
- `tests/test_corrections_prix.py` : régression protégeant les corrections ; suite complète réussie (modifié pendant la finition).
- `tests/test_pipeline_portefeuilles.py` : régression protégeant les corrections ; suite complète réussie (travail antérieur conservé et intégré).
- `tests/test_portefeuille.py` : régression protégeant les corrections ; suite complète réussie (travail antérieur conservé et intégré).

## IV. Portée de la livraison

Les résultats sont reproductibles avec le cliché et les caches conservés. Une nouvelle collecte ne garantit pas le même contenu. Les variantes pondérées par capitalisation et le départ retardé de P4 restent à décider par l'auteur ; aucune étape 3 n'est exécutée. Le rapport de finition et les annexes constituent l'état à reprendre pour la suite.
