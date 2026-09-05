"""
Classification manuelle des entreprises, rangs 1 a 120 du classement textuel.

Chaque verdict resulte de la lecture des phrases extraites du dernier rapport
annuel de l'entreprise, et de la question posee dans la regle de selection :
si l'investissement en intelligence artificielle s'arretait demain, cette
entreprise perdrait-elle de l'argent ?

Le motif est la raison retenue, tiree du texte de l'entreprise elle-meme.
"""

from pathlib import Path

import pandas as pd

RACINE = Path(__file__).resolve().parents[1]
ENTREE = RACINE / "data" / "processed" / "classement_texte.csv"
SORTIE = RACINE / "data" / "processed" / "classification_manuelle.csv"

# rang : (verdict, canal, degre, motif)
VERDICTS = {
    1: ("ENTRE", "vend", "quasi total", "plateformes de calcul accelere vendues aux fournisseurs cloud et aux createurs de modeles"),
    2: ("ENTRE", "vend", "fort", "demande forte pour les accelerateurs IA deployes par les clients hyperscale"),
    3: ("ENTRE", "depense et vend", "fort", "infrastructure cloud passee de 35 a 53 pourcent des revenus cloud ; premiere du classement investissement"),
    4: ("ENTRE", "vend", "partiel", "services d infrastructure cloud declares comme axe strategique ; inference en peripherie de reseau"),
    5: ("ENTRE", "vend", "fort", "demande de calcul accrue pour les systemes GPU tiree par les charges d IA generative"),
    6: ("ENTRE", "vend", "quasi total", "transformation declaree en fournisseur complet d infrastructure de centres de donnees"),
    7: ("ENTRE", "fournit", "quasi total", "location d espace et de puissance electrique dans ses centres de donnees"),
    8: ("ENTRE", "depense et vend", "fort", "116 milliards d investissement, Azure, centres de donnees"),
    9: ("ENTRE", "vend", "fort", "accelerateurs sur mesure pour hyperscalers et createurs de modeles de pointe"),
    10: ("ENTRE", "vend", "fort", "le centre de donnees est l un de ses deux marches finaux declares"),
    11: ("ENTRE", "fournit", "fort", "outils de conception achetes par les fabricants de puces IA"),
    12: ("ENTRE", "vend", "fort", "division entiere dediee a la memoire pour clients hyperscale"),
    13: ("SORT", "utilise", "", "met de l IA dans ses produits ; un arret lui ferait economiser des couts"),
    14: ("ENTRE", "fournit", "partiel", "segment dedie au calcul, a l alimentation et au refroidissement pour centres de donnees"),
    15: ("ENTRE", "fournit", "quasi total", "alimentation et refroidissement ; les centres de donnees sont son marche final numero un"),
    16: ("ENTRE", "depense et vend", "fort", "augmentation significative annoncee de l investissement en infrastructure technique"),
    17: ("ENTRE", "vend", "partiel", "stockage pour charges IA, integre aux trois grands hyperscalers"),
    18: ("ENTRE", "vend", "partiel", "centres de donnees prets pour l IA, clients hyperscalers"),
    19: ("SORT", "utilise", "", "IA dans le produit ; centres de donnees mentionnes comme fournisseurs et risques"),
    20: ("ENTRE", "vend", "fort", "serveurs IA et commutateurs de centres de donnees"),
    21: ("SORT", "utilise", "", "cybersecurite ; centres de donnees = ses propres locaux et lieux de deploiement"),
    22: ("ENTRE", "fournit", "partiel", "1340 megawatts de capacite, location aux clients hyperscale"),
    23: ("SORT", "utilise", "", "surveille les infrastructures cloud sans rien fournir a la chaine"),
    24: ("SORT", "utilise", "", "hebergement ; les centres de donnees sont un cout pour elle"),
    25: ("ENTRE", "vend", "fort", "reseau pour IA, cloud et centres de donnees, coeur de metier declare"),
    26: ("SORT", "utilise", "", "activite centres de donnees naissante, non materielle a ce jour"),
    27: ("ENTRE", "vend", "fort", "composants optiques fournis aux exploitants de centres de donnees et aux fournisseurs d infrastructure IA"),
    28: ("SORT", "utilise", "", "centres de donnees mentionnes comme charge d hebergement"),
    29: ("SORT", "utilise", "", "cybersecurite ; heberge chez AWS"),
    30: ("ENTRE", "depense", "fort", "investissements massifs en centres de donnees et infrastructure technique"),
    31: ("SORT", "utilise", "", "logiciel d entreprise ; centres de donnees = cout"),
    32: ("ENTRE", "vend", "fort", "disques haute capacite pour centres de donnees cloud"),
    33: ("ENTRE", "vend", "fort", "marche final declare Datacenter"),
    34: ("ENTRE", "fournit", "partiel", "quatre acquisitions ciblees centres de donnees ; marche final declare"),
    35: ("DOUTEUX", "fournit", "?", "climatisation ; refroidissement de centres de donnees non demontre par les passages"),
    36: ("DOUTEUX", "vend", "faible", "licence de donnees pour l entrainement de modeles ; faible face a la publicite"),
    37: ("SORT", "utilise", "", "IA pour efficacite interne"),
    38: ("SORT", "utilise", "", "analytique et scoring ; IA dans le produit"),
    39: ("SORT", "utilise", "", "cybersecurite ; centres de donnees = cout"),
    40: ("ENTRE", "vend", "partiel", "forte demande de fibre a l interieur et entre les centres de donnees"),
    41: ("ENTRE", "fournit", "quasi total", "310 centres de donnees"),
    42: ("ENTRE", "fournit", "partiel", "demande accrue de refroidissement liquide pour l infrastructure de centres de donnees"),
    43: ("DOUTEUX", "fournit", "faible", "developpement de centres de donnees en interne, une strategie parmi beaucoup d autres"),
    44: ("SORT", "utilise", "", "revendeur informatique aux entreprises, pas a la chaine d infrastructure"),
    45: ("ENTRE", "fournit", "partiel", "segment centres de donnees declare mais minoritaire"),
    46: ("ENTRE", "vend", "fort", "un de ses deux segments declares s appelle Datacenter et Communications"),
    47: ("ENTRE", "fournit", "fort", "outils de conception de puces, meme logique que Cadence"),
    48: ("ENTRE", "depense et vend", "fort", "AWS et investissement massif"),
    49: ("ENTRE", "fournit", "fort", "equipements de fabrication de puces, demande tiree par l IA et le cloud"),
    50: ("ENTRE", "fournit", "fort", "croissance du segment test tiree par une demande robuste des applications IA"),
    51: ("ENTRE", "fournit", "partiel", "tres grand marche pour l alimentation de secours cree par l investissement en centres de donnees"),
    52: ("ENTRE", "vend", "fort", "Data Center est l un de ses deux marches finaux principaux"),
    53: ("SORT", "utilise", "", "centres de donnees = lieu de deploiement de ses produits"),
    54: ("SORT", "utilise", "", "donnees de credit ; IA dans le produit"),
    55: ("SORT", "menace", "", "l IA generative pourrait abaisser la barriere a l entree de concurrents"),
    56: ("SORT", "utilise", "", "IA dans le produit ; centres de donnees = infrastructure propre"),
    57: ("SORT", "utilise", "", "paiements ; plateforme IA interne"),
    58: ("DOUTEUX", "fournit", "faible", "activite Data Center Solutions declaree en forte croissance mais minime face au parapetrolier"),
    59: ("DOUTEUX", "vend", "faible", "croissance du sous marche filaire tiree par l infrastructure de centres de donnees"),
    60: ("SORT", "menace", "", "l IA pourrait modifier le marche de ses offres et reduire la demande de ses clients"),
    61: ("SORT", "utilise", "", "IA dans les services de sante"),
    62: ("ENTRE", "vend", "fort", "clients fournisseurs cloud hyperscale ; strategie declaree autour du centre de donnees"),
    63: ("SORT", "utilise", "", "colocation boursiere sans lien avec l IA"),
    64: ("SORT", "utilise", "", "IA interne pour la logistique"),
    65: ("ENTRE", "vend", "fort", "segment ISG, serveurs et infrastructure IA"),
    66: ("SORT", "utilise", "", "logiciel de sante heberge chez un tiers"),
    67: ("ENTRE", "fournit", "partiel", "contrat de fourniture a Microsoft pour ses centres de donnees ; expansion tiree par les hyperscalers"),
    68: ("SORT", "utilise", "", "donnees financieres ; IA dans le produit"),
    69: ("DOUTEUX", "vend", "faible", "composants de puissance, lien avec les centres de donnees non demontre par les passages"),
    70: ("SORT", "utilise", "", "IA pour le service client"),
    71: ("SORT", "menace", "", "l IA pourrait alterer le marche de ses produits et reduire la demande"),
    72: ("ENTRE", "vend", "partiel", "portefeuille declare incluant le centre de donnees ; controleurs pour centres de donnees IA"),
    73: ("SORT", "utilise", "", "cybersecurite grand public"),
    74: ("SORT", "utilise", "", "editeur de logiciel dont l IA est le produit, meme famille que Salesforce et Adobe"),
    75: ("SORT", "utilise", "", "IA pour le service client"),
    76: ("ENTRE", "fournit", "partiel", "segment Intelligent Infrastructure dedie a l infrastructure IA"),
    77: ("SORT", "utilise", "", "IA embarquee dans les machines agricoles"),
    78: ("SORT", "utilise", "", "IA dans les processus de paie"),
    79: ("SORT", "utilise", "", "IA dans le produit ; centres de donnees = risque operationnel"),
    80: ("SORT", "menace", "", "l IA generative pourrait reduire les barrieres a la concurrence"),
    81: ("SORT", "utilise", "", "modeles d apprentissage pour le credit"),
    82: ("SORT", "utilise", "", "IA pour la fraude et le risque"),
    83: ("ENTRE", "fournit", "partiel", "developpe des moyens de production dedies a ses clients centres de donnees"),
    84: ("SORT", "utilise", "", "indices financiers ; cloud utilise pour reduire ses propres risques de centres de donnees"),
    85: ("DOUTEUX", "fournit", "faible", "les centres de donnees figurent parmi les classes d actifs en croissance de son courtage"),
    86: ("ENTRE", "vend", "partiel", "reseaux de donnees numeriques, 28 pourcent des ventes du segment industriel"),
    87: ("SORT", "utilise", "", "robotique chirurgicale, IA dans le produit"),
    88: ("SORT", "utilise", "", "IA comme tendance affectant ses clients"),
    89: ("SORT", "utilise", "", "modeles d apprentissage pour le marketing"),
    90: ("SORT", "utilise", "", "centres de donnees = hebergement propre"),
    91: ("SORT", "utilise", "", "IA dans les solutions parapetrolieres"),
    92: ("SORT", "utilise", "", "IA pour la place de marche"),
    93: ("SORT", "utilise", "", "IA pour la protection des paiements"),
    94: ("DOUTEUX", "fournit", "faible", "investissements immobiliers en centres de donnees, une classe d actifs parmi d autres"),
    95: ("SORT", "utilise", "", "IA dans les produits de securite publique"),
    96: ("SORT", "utilise", "", "IA pour l efficacite operationnelle"),
    97: ("SORT", "utilise", "", "logiciel public heberge chez AWS"),
    98: ("ENTRE", "fournit", "partiel", "hors tres gros clients centres de donnees les volumes seraient plats ; discussions de fourniture en cours"),
    99: ("SORT", "utilise", "", "centres de donnees = risque operationnel de la bourse"),
    100: ("SORT", "utilise", "", "IA pour l automatisation de ses flux"),
    101: ("SORT", "utilise", "", "investit dans son hebergement pour ses propres capacites IA"),
    102: ("SORT", "utilise", "", "mentions limitees aux risques juridiques des fonctions IA"),
    103: ("ENTRE", "fournit", "fort", "materiaux et composants pour l IA et le calcul haute performance, gestion thermique"),
    104: ("SORT", "utilise", "", "conseil et logiciel ; cinq mentions seulement dans tout le document"),
    105: ("SORT", "utilise", "", "centres de donnees = locaux operationnels"),
    106: ("ENTRE", "fournit", "partiel", "contrat de fourniture d un campus de centres de donnees ou AWS est implique"),
    107: ("ENTRE", "depense", "partiel", "plus de 20 milliards d investissement en 2026 tires par les initiatives IA, infrastructure de calcul et centres de donnees"),
    108: ("SORT", "utilise", "", "notation et donnees ; IA dans le produit"),
    109: ("SORT", "utilise", "", "IA pour la gestion des couts de sante"),
    110: ("SORT", "utilise", "", "centres de donnees = installations propres"),
    111: ("ENTRE", "fournit", "partiel", "demande croissante des centres de donnees parmi ses gros clients"),
    112: ("DOUTEUX", "fournit", "?", "mentions limitees aux risques de l IA, exposition non demontree par les passages"),
    113: ("SORT", "utilise", "", "moteur publicitaire fonde sur l IA"),
    114: ("SORT", "utilise", "", "IA pour le support et la fraude"),
    115: ("SORT", "utilise", "", "IA pour l analyse de donnees medicales"),
    116: ("ENTRE", "fournit", "partiel", "solutions pour accroitre l efficacite des grappes de calcul IA et les interconnexions"),
    117: ("DOUTEUX", "fournit", "faible", "refroidissement de centres de donnees cite dans une enumeration"),
    118: ("ENTRE", "fournit", "partiel", "clients hyperscalers ; demande de transport d electricite tiree par les centres de donnees"),
    119: ("DOUTEUX", "fournit", "faible", "investissements en centres de donnees, nouvelle classe d actifs pour une fonciere de commerce"),
    120: ("SORT", "utilise", "", "IA comme tendance reglementaire et concurrentielle"),
}


# --------------------------------------------------------------------------
# Balayage sectoriel au-dela du rang 120.
#
# Les entreprises retenues tardivement ont toutes le meme profil : elles
# fournissent la chaine sans employer souvent le vocabulaire. Un classement
# par frequence les enterre. On a donc balaye integralement les secteurs ou
# l'exposition indirecte se cache : services aux collectivites, industrie,
# immobilier, materiaux, energie.
#
# Sans ce balayage, Comfort Systems (rang 285, specialiste du CVC de centres
# de donnees) et Vistra (rang 291) auraient ete manquees.
# --------------------------------------------------------------------------

BALAYAGE = {
    127: ("ENTRE", "fournit", "partiel", "forte demande pour ses produits destines aux centres de donnees sur six a huit trimestres"),
    134: ("ENTRE", "fournit", "fort", "fournisseur de reference d energie renouvelable aux entreprises de centres de donnees"),
    135: ("ENTRE", "fournit", "fort", "commandes de raccordement et production electrique pour electrifier les centres de donnees"),
    138: ("ENTRE", "fournit", "partiel", "hausse de demande et reglementation sur l interconnexion des centres de donnees IA"),
    143: ("ENTRE", "fournit", "partiel", "ses plans d investissement dependent de la croissance et de la viabilite des centres de donnees"),
    147: ("ENTRE", "fournit", "partiel", "accord strategique pour developper des campus de centres de donnees sur ses terrains"),
    151: ("ENTRE", "fournit", "partiel", "ses plans d investissement dependent de la viabilite des centres de donnees raccordes"),
    158: ("ENTRE", "fournit", "partiel", "le centre de donnees figure parmi les marches finaux declares de son segment electrique"),
    167: ("ENTRE", "fournit", "partiel", "la demande de projets lies a l IA inclut les solutions d alimentation de centres de donnees"),
    177: ("ENTRE", "fournit", "partiel", "developpement selectif de centres de donnees dans sa strategie d infrastructure numerique"),
    185: ("ENTRE", "fournit", "faible", "hausse de charge anticipee et procedures d interconnexion des centres de donnees"),
    204: ("ENTRE", "fournit", "partiel", "facteur de risque dedie a la croissance de la demande des clients centres de donnees"),
    207: ("ENTRE", "fournit", "partiel", "croissance des ventes tiree par l usage des centres de donnees ; charges hyperscale"),
    224: ("ENTRE", "fournit", "partiel", "participation dans un fabricant d appareillage electrique utilise par les centres de donnees"),
    232: ("ENTRE", "fournit", "partiel", "croissance rapide alimentee par l IA et les centres de donnees"),
    238: ("ENTRE", "fournit", "partiel", "la demande liee a l expansion des centres de donnees pourrait avoir un effet significatif"),
    240: ("ENTRE", "fournit", "fort", "demande portee par l expansion des centres de donnees pour alimenter l IA et le cloud"),
    263: ("ENTRE", "fournit", "partiel", "croissance significative de la demande provenant principalement des centres de donnees"),
    285: ("ENTRE", "fournit", "fort", "demande particulierement forte pour les centres de donnees ; specialiste du CVC de centres de donnees"),
    291: ("ENTRE", "fournit", "partiel", "emergence de grandes charges de centres de donnees liees a l IA"),
    294: ("ENTRE", "fournit", "partiel", "cherche a servir les grands clients tels que les centres de donnees"),
    295: ("ENTRE", "fournit", "partiel", "forte croissance de charge attendue liee a l expansion des centres de donnees"),
    305: ("ENTRE", "fournit", "partiel", "investissements destines a la hausse de consommation portee par les grandes charges"),
    310: ("ENTRE", "fournit", "partiel", "projets de construction pour repondre aux besoins electriques crees par les centres de donnees"),
    323: ("ENTRE", "fournit", "faible", "turbines servant une demande electrique tiree par la construction de centres de donnees"),
    334: ("ENTRE", "fournit", "partiel", "contrats signes avec de nouveaux centres de donnees representant environ neuf gigawatts"),
    338: ("ENTRE", "fournit", "faible", "hausse de la demande de pointe due en partie aux centres de donnees"),
    346: ("ENTRE", "fournit", "partiel", "ses plans d investissement dependent de la croissance des centres de donnees raccordes"),
    358: ("ENTRE", "fournit", "partiel", "investissements de transport pour centres de donnees ; croissance de charge attendue"),
    364: ("ENTRE", "fournit", "partiel", "le developpement de centres de donnees doit entrainer une hausse rapide des investissements reseau"),
    374: ("ENTRE", "fournit", "partiel", "construction d installations de production pour desservir des centres de donnees"),
    399: ("ENTRE", "fournit", "partiel", "la demande croissante des centres de donnees la positionne pour de nouveaux projets"),

    145: ("DOUTEUX", "fournit", "faible", "commissionnaire de transport servant une clientele cloud, hyperscale et semi-conducteurs"),
    161: ("DOUTEUX", "fournit", "faible", "demande structurelle de gaz naturel tiree en partie par les centres de donnees"),
    193: ("DOUTEUX", "fournit", "faible", "exploration de l informatique en peripherie, au stade des intentions"),
    230: ("DOUTEUX", "vend", "faible", "fluide caloporteur pour refroidissement direct au processeur, produit reel mais marginal"),
    237: ("DOUTEUX", "fournit", "faible", "granulats cites parmi les usages incluant les centres de donnees"),
    241: ("DOUTEUX", "vend", "faible", "les centres de donnees figurent parmi ses marches enumeres"),
    250: ("DOUTEUX", "vend", "faible", "demande de cuivre soutenue entre autres par les centres de donnees"),
    267: ("DOUTEUX", "vend", "faible", "charpentes metalliques citees parmi des usages incluant les centres de donnees"),
    290: ("DOUTEUX", "fournit", "faible", "materiaux de construction cites pour la reindustrialisation et les centres de donnees"),
    300: ("DOUTEUX", "fournit", "faible", "premier projet electrique destine a des centres de donnees, au stade initial"),
    317: ("DOUTEUX", "fournit", "faible", "le centre de donnees figure dans une enumeration de marches servis"),
    329: ("DOUTEUX", "fournit", "?", "exposition aux groupes electrogenes de centres de donnees non demontree par les passages"),
    332: ("DOUTEUX", "vend", "faible", "stockage d energie soutenu par la hausse de demande electrique des centres de donnees"),
    350: ("DOUTEUX", "fournit", "faible", "les centres de donnees figurent parmi ses categories de clients"),
    370: ("DOUTEUX", "fournit", "faible", "granulats cites parmi les usages incluant les centres de donnees"),
    420: ("DOUTEUX", "fournit", "faible", "acier cite parmi des usages incluant les centres de donnees"),
    422: ("DOUTEUX", "fournit", "?", "nouvelles sources de demande evoquees sans precision exploitable"),
    426: ("DOUTEUX", "fournit", "?", "plan d investissement de 41 milliards sans attribution explicite"),
    451: ("DOUTEUX", "fournit", "faible", "developpement de centres de donnees cite parmi ses pistes de croissance"),
}


def main():
    cl = pd.read_csv(ENTREE, dtype={"cik": str})
    sub = cl.copy()

    def attribuer(rang, i):
        if rang in VERDICTS:
            return VERDICTS[rang][i]
        if rang in BALAYAGE:
            return BALAYAGE[rang][i]
        return ("SORT", "", "", "non retenue : aucun element du rapport annuel n etablit une dependance a l investissement en IA")[i]

    for i, champ in enumerate(["verdict", "canal", "degre", "motif"]):
        sub[champ] = sub["rang"].map(lambda r, i=i: attribuer(r, i))

    colonnes = ["rang", "nom", "symboles", "secteur", "sous_secteur",
                "n_actifs", "total", "verdict", "canal", "degre", "motif"]
    sub[colonnes].to_csv(SORTIE, index=False, encoding="utf-8")
    sub[sub.verdict == "ENTRE"][colonnes].sort_values("rang").to_csv(
        SORTIE.parent / "univers_retenu.csv", index=False, encoding="utf-8")

    print(sub["verdict"].value_counts().to_string())
    print("\n--- ENTRE par secteur ---")
    print(sub[sub.verdict == "ENTRE"]["secteur"].value_counts().to_string())
    print("\n--- ENTRE par canal ---")
    print(sub[sub.verdict == "ENTRE"]["canal"].value_counts().to_string())
    print("\n--- densite des verdicts par tranche de 30 rangs ---")
    for a in (1, 31, 61, 91):
        t = sub[(sub.rang >= a) & (sub.rang < a + 30)]
        print(f"  rangs {a:3d}-{a+29:3d} : {(t.verdict=='ENTRE').sum():2d} entrent, "
              f"{(t.verdict=='DOUTEUX').sum()} douteux")


if __name__ == "__main__":
    main()
