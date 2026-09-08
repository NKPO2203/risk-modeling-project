"""Contrôles locaux des prix, extraits du notebook le 8 septembre 2026.

Les acquisitions sont séparées des contrôles : ce module ne touche jamais
aux preuves brutes. Les comptes SEC ne prouvent pas le prix du titre.
"""
from pathlib import Path
import numpy as np
import pandas as pd


def verifier_structure_prix(d, nom):
    """Refuse les échecs qui rendraient les comparaisons silencieusement vides.

    Les prix manquants restent des anomalies à examiner. Un événement ou un
    volume inconnu n'est jamais assimilé à zéro, ni une infinité à un prix.
    """
    requis = {"date", "Open", "High", "Low", "Close", "Adj Close", "Volume", "Dividends", "Stock Splits"}
    if d.empty or not requis <= set(d.columns):
        raise ValueError(f"Fichier vide ou colonnes manquantes : {nom}")
    if d.date.isna().any():
        raise ValueError(f"Date absente : {nom}")
    jours = d.date.str[:10]
    # Le suffixe de fuseau est contrôlé dans le rapport, la date doit exister.
    pd.to_datetime(jours, format="%Y-%m-%d", errors="raise")
    if not jours.is_monotonic_increasing:
        raise ValueError(f"Dates désordonnées : {nom}")
    nombres = d[list(requis - {"date"})].apply(pd.to_numeric, errors="raise")
    if np.isinf(nombres).any().any():
        raise ValueError(f"Valeur infinie : {nom}")
    evenements = nombres[["Dividends", "Stock Splits", "Volume"]]
    if evenements.isna().any().any() or evenements.lt(0).any().any():
        raise ValueError(f"Événement ou volume absent ou négatif : {nom}")
    if not d.Close.notna().any() or not d['Adj Close'].notna().any():
        raise ValueError(f"Aucun prix calculable : {nom}")


def controler(racine, sortie):
    RACINE, SORTIE = Path(racine), Path(sortie)
    SORTIE.mkdir(parents=True, exist_ok=True)
    DOSSIER, BENCH = RACINE / "data/raw/prix", RACINE / "data/raw/benchmarks"
    fichiers = sorted(list(DOSSIER.glob("*.csv")) + list(BENCH.glob("*.csv")))
    if not fichiers:
        raise ValueError("Aucun fichier de prix à contrôler.")
    couverture = []
    for fichier in fichiers:
        d = pd.read_csv(fichier)
        verifier_structure_prix(d, fichier.name)
        couverture.append({"fichier": fichier.name, "lignes": len(d),
                           "structure_verifiee": True})
    # Tâche, cellule historique 1.
    CONTROLE = SORTIE / "controle_prix.csv"

    seances = set(pd.read_csv(RACINE / "data" / "raw" / "calendrier_bourse.csv")["date"].astype(str))
    debut_cal, fin_cal = min(seances), max(seances)

    # Tâche, cellule historique 2.
    anomalies = []

    for fichier in sorted(list(DOSSIER.glob("*.csv")) + list(BENCH.glob("*.csv"))):
        dates = pd.read_csv(fichier, usecols=["date"])["date"].str[:10]
        debut, fin = dates.iloc[0], dates.iloc[-1]

        for j in dates[dates.duplicated()].unique():
            anomalies.append({"fichier": fichier.name, "test": "date en double",
                              "date": j, "detail": ""})

        avant = int((dates < debut_cal).sum())
        if avant:
            anomalies.append({"fichier": fichier.name, "test": "anteriorite au calendrier",
                              "date": debut, "detail": f"{avant} seances avant {debut_cal}"})

        bas, haut = max(debut, debut_cal), min(fin, fin_cal)
        couvertes = set(dates[(dates >= bas) & (dates <= haut)])
        attendues = {j for j in seances if bas <= j <= haut}

        for j in sorted(attendues - couvertes):
            anomalies.append({"fichier": fichier.name, "test": "seance absente",
                              "date": j, "detail": ""})
        for j in sorted(couvertes - seances):
            anomalies.append({"fichier": fichier.name, "test": "date hors calendrier",
                              "date": j, "detail": ""})

    controle = pd.DataFrame(anomalies, columns=["fichier", "test", "date", "detail"])
    controle.to_csv(CONTROLE, index=False, encoding="utf-8")

    print(len(controle), "anomalies")
    if len(controle):
        print(controle.test.value_counts().to_string())
        print()
        print(controle[controle.test == "seance absente"].fichier.value_counts().head(10).to_string())

    # Tâche, cellule historique 3.
    SEUIL = 0.30
    TESTS = ["variation quotidienne extreme", "barre incoherente",
             "prix nul ou negatif", "valeur manquante"]
    COLS = ["Open", "High", "Low", "Close", "Adj Close"]

    # Tâche, cellule historique 4.
    anomalies = []

    for fichier in sorted(list(DOSSIER.glob("*.csv")) + list(BENCH.glob("*.csv"))):
        d = pd.read_csv(fichier, usecols=["date"] + COLS)
        d["j"] = d["date"].str[:10]

        var = d["Adj Close"].pct_change(fill_method=None)
        for i in var[var.abs() > SEUIL].index:
            anomalies.append({"fichier": fichier.name, "test": "variation quotidienne extreme",
                              "date": d.j[i], "detail": f"{var[i] * 100:+.1f} %"})

        incoherent = ((d.Low > d.High) | (d.Open < d.Low) | (d.Open > d.High)
                      | (d.Close < d.Low) | (d.Close > d.High))
        for i in d.index[incoherent]:
            r = d.loc[i]
            anomalies.append({"fichier": fichier.name, "test": "barre incoherente", "date": r.j,
                              "detail": f"O={r.Open:.2f} H={r.High:.2f} L={r.Low:.2f} C={r.Close:.2f}"})

        for i in d.index[(d[COLS] <= 0).any(axis=1)]:
            anomalies.append({"fichier": fichier.name, "test": "prix nul ou negatif",
                              "date": d.j[i], "detail": ""})

        for i in d.index[d[COLS].isna().any(axis=1)]:
            anomalies.append({"fichier": fichier.name, "test": "valeur manquante",
                              "date": d.j[i], "detail": ""})

    ancien = pd.read_csv(CONTROLE)
    ancien = ancien[~ancien.test.isin(TESTS)]
    controle = pd.concat([ancien, pd.DataFrame(anomalies, columns=["fichier", "test", "date", "detail"])], ignore_index=True)
    controle.to_csv(CONTROLE, index=False, encoding="utf-8")

    print(len(anomalies), "nouvelles anomalies |", len(controle), "au total")
    print(pd.DataFrame(anomalies, columns=["fichier", "test", "date", "detail"]).test.value_counts().to_string())

    # Tâche, cellule historique 5.
    TOL = 1e-4
    TESTS_15 = ["ajustement incoherent"]

    # Tâche, cellule historique 6.
    anomalies, ecarts = [], []

    for fichier in sorted(list(DOSSIER.glob("*.csv")) + list(BENCH.glob("*.csv"))):
        d = pd.read_csv(fichier, usecols=["date", "Close", "Adj Close", "Dividends", "Stock Splits"])
        d["j"] = d["date"].str[:10]

        r_ajuste = d["Adj Close"].pct_change(fill_method=None)
        r_additif = (d["Close"] + d["Dividends"]) / d["Close"].shift() - 1
        r_multiplicatif = d["Close"] / (d["Close"].shift() - d["Dividends"]) - 1

        e_add = (r_ajuste - r_additif).abs()
        e_mul = (r_ajuste - r_multiplicatif).abs()
        if not e_mul.notna().any() or np.isinf(e_mul).any():
            raise ValueError(f"Ajustement non calculable : {fichier.name}")
        ecarts.append({"fichier": fichier.name, "additif": e_add.max(),
                       "multiplicatif": e_mul.max(), "comparaisons": int(e_mul.notna().sum())})

        for i in e_mul[e_mul > TOL].index:
            anomalies.append({"fichier": fichier.name, "test": "ajustement incoherent",
                              "date": d.j[i], "detail": f"ecart {e_mul[i]:.2e}"})

    ecarts = pd.DataFrame(ecarts)

    ancien = pd.read_csv(CONTROLE)
    ancien = ancien[~ancien.test.isin(TESTS_15)]
    controle = pd.concat([ancien, pd.DataFrame(anomalies, columns=["fichier", "test", "date", "detail"])], ignore_index=True)
    controle.to_csv(CONTROLE, index=False, encoding="utf-8")

    print("ecart maximal, tous fichiers confondus")
    print(ecarts[["additif", "multiplicatif"]].max().to_string())
    print()
    print(ecarts.sort_values("additif", ascending=False).head(8).to_string(index=False))
    print()
    print(len(anomalies), "ajustements incoherents |", len(controle), "au total")

    # Tâche, cellule historique 7.
    TESTS_16 = ["division non confirmee"]
    DEBUT_SEC = "2010-01-01"
    TOL_SPLIT = 0.02

    # Tâche, cellule historique 8.
    sp500 = pd.read_csv(RACINE / "data/raw/sp500_constituents.csv", dtype=str)
    correspondance = sp500[["CIK", "Symbol"]].rename(columns={"CIK": "cik", "Symbol": "symbole"})
    correspondance["symbole"] = correspondance.symbole.str.replace(".", "-", regex=False)
    actions = pd.read_csv(RACINE / "data/raw/actions_en_circulation.csv", dtype={"cik": str})
    actions = actions[actions.notion == "actions"].merge(correspondance, on="cik", validate="many_to_many")
    actions = actions.sort_values(["depose_le", "fin", "valeur", "depot"], kind="stable")


    # Tâche, cellule historique 9.
    anomalies, mesures = [], []

    for fichier in sorted(DOSSIER.glob("*.csv")):
        d = pd.read_csv(fichier, usecols=["date", "Stock Splits"]).rename(
            columns={"Stock Splits": "division"})
        d["j"] = d["date"].str[:10]
        divisions = d[(d.division > 0) & (d.j >= DEBUT_SEC)]
        if divisions.empty:
            continue

        serie = actions[actions.symbole == fichier.stem]

        for r in divisions.itertuples():
            avant = serie[(serie.depose_le < r.j) & (serie.fin < r.j)].sort_values(["fin", "depose_le", "valeur", "depot"], kind="stable").tail(1)
            apres = serie[(serie.depose_le > r.j) & (serie.fin >= r.j)].sort_values(["fin", "depose_le", "valeur", "depot"], kind="stable").head(1)
            if avant.empty or apres.empty:
                mesures.append({"symbole": fichier.stem, "date": r.j, "annonce": r.division,
                                "mesure": None, "ecart": None, "avant_fin": None, "apres_fin": None})
                continue

            mesure = apres.valeur.iloc[0] / avant.valeur.iloc[0]
            ecart = abs(mesure / r.division - 1)
            mesures.append({"symbole": fichier.stem, "date": r.j, "annonce": r.division,
                            "mesure": mesure, "ecart": ecart, "avant_fin": avant.fin.iloc[0], "apres_fin": apres.fin.iloc[0], "avant_depose": avant.depose_le.iloc[0], "apres_depose": apres.depose_le.iloc[0]})

            if ecart > TOL_SPLIT:
                anomalies.append({"fichier": fichier.name, "test": "division non confirmee",
                                  "date": r.j,
                                  "detail": f"annonce {r.division:g}, mesure {mesure:.3f}"})

    mesures = pd.DataFrame(mesures, columns=["symbole", "date", "annonce", "mesure", "ecart", "avant_fin", "apres_fin", "avant_depose", "apres_depose"])
    mesures.to_csv(SORTIE / "controle_divisions_sec.csv", index=False)

    ancien = pd.read_csv(CONTROLE)
    ancien = ancien[~ancien.test.isin(TESTS_16)]
    controle = pd.concat([ancien, pd.DataFrame(anomalies, columns=["fichier", "test", "date", "detail"])], ignore_index=True)
    controle.to_csv(CONTROLE, index=False, encoding="utf-8")

    print(len(mesures), "divisions depuis", DEBUT_SEC)
    print(int(mesures.mesure.isna().sum()), "sans encadrement SEC")
    print(len(anomalies), "non confirmees |", len(controle), "au total")
    print()
    print(mesures.dropna(subset=["ecart"]).sort_values("ecart", ascending=False)
          .head(24).to_string(index=False))

    # Tâche, cellule historique 10.
    TESTS_17 = ["reference de cotation absente", "premiere cotation discordante",
                "historique tronque"]

    composants = pd.read_csv(RACINE / "data" / "raw" / "sp500_constituents.csv", dtype=str)
    entree = dict(zip(composants.Symbol.str.replace(".", "-", regex=False),
                      composants["Date added"]))

    reference = pd.read_csv(RACINE / "data" / "raw" / "premieres_cotations.csv")
    premiere = dict(zip(reference.ticker, reference.premiere_cotation))

    # Tâche, cellule historique 11.
    anomalies, debuts = [], []

    for fichier in sorted(DOSSIER.glob("*.csv")):
        debut = pd.read_csv(fichier, usecols=["date"], nrows=1).date.iloc[0][:10]
        ref = premiere.get(fichier.stem)
        ajout = entree.get(fichier.stem)
        debuts.append({"symbole": fichier.stem, "prix": debut, "reference": ref, "indice": ajout})

        if ref is None:
            anomalies.append({"fichier": fichier.name, "test": "reference de cotation absente",
                              "date": debut, "detail": ""})
        elif ref != debut:
            anomalies.append({"fichier": fichier.name, "test": "premiere cotation discordante",
                              "date": debut, "detail": f"reference {ref}"})

        if ajout is not None and ajout < debut:
            anomalies.append({"fichier": fichier.name, "test": "historique tronque",
                              "date": debut, "detail": f"entree dans l'indice le {ajout}"})

    debuts = pd.DataFrame(debuts)

    ancien = pd.read_csv(CONTROLE)
    ancien = ancien[~ancien.test.isin(TESTS_17)]
    controle = pd.concat([ancien, pd.DataFrame(anomalies, columns=["fichier", "test", "date", "detail"])], ignore_index=True)
    controle.to_csv(CONTROLE, index=False, encoding="utf-8")

    print(len(anomalies), "anomalies |", len(controle), "au total")
    print(pd.DataFrame(anomalies, columns=["fichier", "test", "date", "detail"]).test.value_counts().to_string())
    print()
    print("dates de debut partagees par plusieurs titres")
    compte = debuts.prix.value_counts()
    print(compte[compte > 1].to_string())

    # Tâche, cellule historique 13.
    TESTS_18 = ["metadonnees absentes", "devise non usd", "fuseau inattendu", "type inattendu",
                "decalage horaire inattendu", "premiere transaction discordante"]

    FUSEAUX = {"EST", "EDT"}
    DECALAGES = {"-05:00", "-04:00"}

    meta = pd.read_csv(RACINE / "data" / "raw" / "metadonnees_titres.csv")
    attendu = {r.fichier: r.premiere_transaction for r in meta.itertuples()
               if isinstance(r.premiere_transaction, str)}
    decrits = set(meta.fichier)
    if meta.fichier.duplicated().any():
        raise ValueError("Métadonnées dupliquées.")
    anomalies = []

    for r in meta.itertuples():
        if r.devise != "USD":
            anomalies.append({"fichier": r.fichier, "test": "devise non usd",
                              "date": "", "detail": str(r.devise)})
        if r.fuseau not in FUSEAUX:
            anomalies.append({"fichier": r.fichier, "test": "fuseau inattendu",
                              "date": "", "detail": str(r.fuseau)})

        attendus = {"EQUITY"} if (DOSSIER / r.fichier).exists() else ({"ETF"} if r.fichier in {"SPY.csv", "RSP.csv"} else {"INDEX"})
        if r.type not in attendus:
            anomalies.append({"fichier": r.fichier, "test": "type inattendu",
                              "date": "", "detail": str(r.type)})

    for fichier in fichiers:
        if fichier.name not in decrits:
            anomalies.append({"fichier": fichier.name, "test": "metadonnees absentes",
                              "date": "", "detail": ""})

        d = pd.read_csv(fichier, usecols=["date"])
        for x in sorted(set(d.date.str[-6:]) - DECALAGES):
            anomalies.append({"fichier": fichier.name, "test": "decalage horaire inattendu",
                              "date": "", "detail": x})

        debut = d.date.iloc[0][:10]
        declaree = attendu.get(fichier.name)
        if declaree and declaree != debut:
            anomalies.append({"fichier": fichier.name, "test": "premiere transaction discordante",
                              "date": debut, "detail": f"declaree {declaree}"})

    ancien = pd.read_csv(CONTROLE)
    ancien = ancien[~ancien.test.isin(TESTS_18)]
    controle = pd.concat([ancien, pd.DataFrame(anomalies, columns=["fichier", "test", "date", "detail"])], ignore_index=True)
    controle.to_csv(CONTROLE, index=False, encoding="utf-8")

    print(len(anomalies), "anomalies |", len(controle), "au total")
    if anomalies:
        print(pd.DataFrame(anomalies, columns=["fichier", "test", "date", "detail"]).test.value_counts().to_string())

    # Tâche, cellule historique 14.
    TESTS_19 = ["fin de serie anticipee", "denomination divergente"]

    import re

    def normaliser(nom):
        n = str(nom).lower()
        for mot in [" incorporated", " corporation", " companies", " company", " holdings",
                    " group", " inc", " corp", " plc", " ltd", " the", " co",
                    " & ", " and ", ".", ",", "'", "-"]:
            n = n.replace(mot, " ")
        return re.sub(r"\s+", " ", n).strip()

    calendrier = pd.read_csv(RACINE / "data" / "raw" / "calendrier_bourse.csv")["date"].astype(str)
    derniere = calendrier.max()

    meta = pd.read_csv(RACINE / "data" / "raw" / "metadonnees_titres.csv")
    composants = pd.read_csv(RACINE / "data" / "raw" / "sp500_constituents.csv", dtype=str)
    nom_indice = dict(zip(composants.Symbol.str.replace(".", "-", regex=False), composants.Security))

    anomalies = []

    for fichier in fichiers:
        fin = pd.read_csv(fichier, usecols=["date"]).date.iloc[-1][:10]
        if fin < derniere:
            anomalies.append({"fichier": fichier.name, "test": "fin de serie anticipee",
                              "date": fin, "detail": f"derniere seance {derniere}"})

    for r in meta.itertuples():
        reference = nom_indice.get(r.symbole)
        if reference is None:
            continue
        a, b = normaliser(r.nom), normaliser(reference)
        if not (a.startswith(b[:8]) or b.startswith(a[:8])):
            anomalies.append({"fichier": r.fichier, "test": "denomination divergente",
                              "date": "", "detail": f"{r.nom} contre {reference}"})

    ancien = pd.read_csv(CONTROLE)
    ancien = ancien[~ancien.test.isin(TESTS_19)]
    controle = pd.concat([ancien, pd.DataFrame(anomalies, columns=["fichier", "test", "date", "detail"])], ignore_index=True)
    controle.to_csv(CONTROLE, index=False, encoding="utf-8")

    print(len(anomalies), "anomalies |", len(controle), "au total")
    if anomalies:
        print(pd.DataFrame(anomalies, columns=["fichier", "test", "date", "detail"]).test.value_counts().to_string())
        print()
        print(pd.DataFrame(anomalies, columns=["fichier", "test", "date", "detail"])[["fichier", "detail"]].to_string(index=False))

    # Tâche, cellule historique 15.
    TESTS_19B = ["seance sans transaction", "prix fige"]

    anomalies = []
    resume = []

    for fichier in sorted(DOSSIER.glob("*.csv")):
        d = pd.read_csv(fichier, usecols=["date", "Open", "High", "Low", "Close", "Volume"])
        d["j"] = d["date"].str[:10]

        sans_volume = d.Volume == 0
        fige = (sans_volume
                & (d.Open == d.High) & (d.High == d.Low) & (d.Low == d.Close)
                & (d.Close == d.Close.shift()))

        if sans_volume.any():
            resume.append({"symbole": fichier.stem, "lignes": len(d),
                           "sans_volume": int(sans_volume.sum()), "fige": int(fige.sum()),
                           "part": int(sans_volume.sum()) / len(d)})

        for i in d.index[sans_volume & ~fige]:
            anomalies.append({"fichier": fichier.name, "test": "seance sans transaction",
                              "date": d.j[i], "detail": ""})
        for i in d.index[fige]:
            anomalies.append({"fichier": fichier.name, "test": "prix fige",
                              "date": d.j[i], "detail": f"{d.Close[i]:.4f}"})

    resume = pd.DataFrame(resume, columns=["symbole", "lignes", "sans_volume", "fige", "part"]).sort_values("sans_volume", ascending=False)

    ancien = pd.read_csv(CONTROLE)
    ancien = ancien[~ancien.test.isin(TESTS_19B)]
    controle = pd.concat([ancien, pd.DataFrame(anomalies, columns=["fichier", "test", "date", "detail"])], ignore_index=True)
    controle.to_csv(CONTROLE, index=False, encoding="utf-8")

    print(len(anomalies), "anomalies |", len(controle), "au total")
    print(pd.DataFrame(anomalies, columns=["fichier", "test", "date", "detail"]).test.value_counts().to_string())
    print()
    print(resume.head(12).to_string(index=False, formatters={"part": "{:.1%}".format}))
    tests = list(dict.fromkeys(["date en double", "anteriorite au calendrier", "seance absente", "date hors calendrier"] + TESTS + TESTS_15 + TESTS_16 + TESTS_17 + TESTS_18 + TESTS_19 + ["seance sans transaction", "prix fige"]))
    counts = controle.test.value_counts().reindex(tests, fill_value=0)
    counts.rename_axis("test").rename("cas").to_csv(SORTIE / "resume_controle_prix.csv")
    import json
    detail = {"fichiers": couverture, "comparaisons_ajustement": ecarts.to_dict("records"),
              "tests": counts.to_dict(), "signalements": len(controle),
              "limite": "Un zéro signifie absence de détection sur les comparaisons calculables, pas validation externe."}
    (SORTIE / "couverture_controle_prix.json").write_text(
        json.dumps(detail, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    return controle
