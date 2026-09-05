import fs from "node:fs/promises";
import path from "node:path";

// Le module peut être résolu depuis une installation locale ou un runtime
// existant explicitement fourni ; aucun chemin privé n'est codé dans le projet.
const spec = process.env.ARTIFACT_TOOL_MODULE || "@oai/artifact-tool";
const { Workbook, SpreadsheetFile } = await import(spec);
const [input, output] = process.argv.slice(2);
if (!input || !output) throw new Error("Usage : node src/export_univers_excel.mjs donnees.json sortie.xlsx");
const data = JSON.parse(await fs.readFile(input, "utf8"));
const wb = Workbook.create();
const names = [...Object.keys(data.sheets), "Recapitulatif", "Lecture et sources"];
for (const name of names) wb.worksheets.add(name);
const n = data.sheets["Par secteur"].length;
const libelles = {
  non_quantifie: "Non quantifié", etablie: "Activité établie",
  engagement_ou_developpement_documente: "Engagement documenté",
  depense: "Dépense", "depense et vend": "Dépense et vend", vend: "Vend", fournit: "Fournit",
  "doublement observe": "Doublement observé",
  "progression inferieure au seuil": "Progression sous le seuil",
  "non evaluable": "Non évaluable", "recul des mesures disponibles": "Recul des mesures disponibles",
  "trois mesures comparables": "Trois mesures comparables",
  "observation partielle": "Observation partielle", "aucune comparaison": "Aucune comparaison",
};
const alphabet = index => {
  let s = "";
  for (let x = index + 1; x > 0; x = Math.floor((x - 1) / 26)) s = String.fromCharCode(65 + (x - 1) % 26) + s;
  return s;
};
const header = r => {
  r.format.fill = "#1F3864";
  r.format.font = {bold:true, color:"#FFFFFF", name:"Calibri", size:11};
  r.format.wrapText = true;
  r.format.verticalAlignment = "center";
  r.format.rowHeight = 42;
};
for (const [name, rawRows] of Object.entries(data.sheets)) {
  const sheet = wb.worksheets.getItem(name);
  const rows = rawRows.map(row => row.map((v, c) => {
    if(c >= 5 && c <= 9 && typeof v === "string") return libelles[v] || v;
    if(c >= 23 && typeof v === "string") return v.trim() ? v.split(";").map(p => " " + p.replace("/", " → ")).join("\n") : null;
    if ((c === 10 || c === 13) && typeof v === "string" && /^\d{4}-\d{2}-\d{2}$/.test(v)) return new Date(v + "T00:00:00Z");
    // Une cellule commençant par "=" reste une citation littérale.
    if (typeof v === "string" && v.startsWith("=")) return "'" + v;
    return v;
  }));
  const full = sheet.getRangeByIndexes(0,0,n+1,data.columns.length);
  const entetes = [...data.columns];
  entetes[21] = "Multiple de\nl'investissement";
  entetes[22] = "Multiple de\nla recherche";
  full.values = [entetes,...rows];
  full.format.font = {name:"Calibri",size:11,color:"#17263C"};
  full.format.verticalAlignment = "center";
  full.format.rowHeight = 44;
  full.format.wrapText = true;
  sheet.showGridLines = false;
  sheet.freezePanes.freezeRows(1);
  sheet.freezePanes.freezeColumns(2);
  const widths = [11,17,32,30,36,19,17,26,29,25,23,34,20,22,92,15,29,66,85,66,20,25,25,48,48,48];
  widths.forEach((w,c) => sheet.getRangeByIndexes(0,c,n+1,1).format.columnWidth = w);
  header(sheet.getRangeByIndexes(0,0,1,data.columns.length));
  if(n) {
    sheet.getRange("K2:K"+(n+1)).setNumberFormat("yyyy-mm-dd");
    sheet.getRange("N2:N"+(n+1)).setNumberFormat("yyyy-mm-dd");
    sheet.getRange("U2:W"+(n+1)).setNumberFormat('0.00"x"');
    // Les valeurs restent des chaînes ; ce format conserve également les
    // zéros initiaux dans le rendu numérique de certains lecteurs.
    sheet.getRange("P2:P"+(n+1)).setNumberFormat("0000000000");
    for(let row=2;row<=n+1;row+=2) sheet.getRange("A"+row+":Z"+row).format.fill="#F1F5FA";
  }
  sheet.tables.add("A1:Z"+(n+1),true,name === "Par secteur" ? "UniversSecteur" : name === "Par canal" ? "UniversCanal" : "UniversAnciennete");
  if(n) sheet.getRangeByIndexes(1,0,n,data.columns.length).format.autofitRows();
}
const recap=wb.worksheets.getItem("Recapitulatif");
recap.showGridLines=false;
recap.getRange("A1:C1").merge();
recap.getRange("A1").values=[["Univers de recherche · "+data.snapshot]];
header(recap.getRange("A1:C1"));
recap.getRange("A3").values=[["Entreprises retenues"]];
recap.getRange("B3").formulas=[["=COUNTA('Par secteur'!A2:A"+Math.max(n+1,2)+")"]];
recap.getRange("A4").values=[["CIK examinés ou signalés"]];
recap.getRange("B4").values=[[data.summary.entreprises_composition]];
recap.getRange("A5").values=[["Rapports archivés"]];
recap.getRange("B5").values=[[data.summary.rapports_comptes]];
recap.getRange("A6:C7").merge();
recap.getRange("A6").values=[["Un univers pour de futurs portefeuilles. Le mouvement des comptes ne démontre ni une causalité IA ni une performance boursière."]];
recap.getRange("A6:C7").format.wrapText=true;
recap.getRange("A6:C7").format.fill="#FFF2D5";
let pos=9;
for (const [label,summaryKey,column] of [
  ["Secteur","secteurs_retenus","D"],["Canal","canaux_retenus","F"],
  ["Maturité","maturites_retenues","H"],["Mouvement comptable","mouvements_comptables","I"],
  ["Couverture comptable","couverture_comptable","J"]]) {
  recap.getRange("A"+pos+":B"+pos).values=[[label,"Nombre"]];
  header(recap.getRange("A"+pos+":B"+pos)); pos++;
  for(const key of Object.keys(data.summary[summaryKey])) {
    recap.getRange("A"+pos).values=[[libelles[key] || key]];
    recap.getRange("B"+pos).formulas=[["=COUNTIF('Par secteur'!"+column+"2:"+column+Math.max(n+1,2)+",A"+pos+")"]];
    pos++;
  }
  pos+=2;
}
recap.getRange("A1:A"+pos).format.columnWidth=46;
recap.getRange("B1:B"+pos).format.columnWidth=16;
recap.getRange("C1:C"+pos).format.columnWidth=24;
recap.getRange("A2:C"+pos).format.rowHeight=27;
recap.getRange("A2:C"+pos).format.verticalAlignment="center";
recap.getRange("B3:B"+pos).setNumberFormat("0");
recap.freezePanes.freezeRows(1);
const notes=wb.worksheets.getItem("Lecture et sources");
const lectures=[
["Point de lecture","Ce que je peux en déduire","Source ou contrôle"],
["Périmètre","Entreprises retenues sur leur activité ou leurs engagements dans la chaîne des infrastructures de calcul. Aucun poids de portefeuille n'est fixé.","research/selection_rule.md · version III"],
["Décision","Chaque CIK retenu a une preuve retrouvée. La revue porte sur les passages repérés et les lectures complémentaires consignées.","data/review/decisions_selection.csv ; colonnes Q à S des tableaux"],
["Degré non quantifié","La part d'activité liée à l'IA n'est pas isolée. Aucun pourcentage n'est déduit d'une mention.","Registre de sélection"],
["Mouvement comptable","Description nominale de mesures comparables. Une croissance peut avoir d'autres causes que l'IA.","data/processed/corroboration_details.csv"],
["Couverture","Une donnée absente ou non réconciliée ne vaut pas zéro. Un multiple absent reste vide.","data/processed/base_selection.csv"],
["Références","Les périodes sont propres à chaque mesure. Un repli peut porter sur deux exercices plus récents.","Colonnes X à Z ; corroboration_details.csv"],
["Date d'historique","Première date disponible dans le fichier Yahoo existant. Ce n'est pas une date d'IPO vérifiée. La date de collecte d'origine n'est pas documentée.","data/raw/premieres_cotations.csv ; Yahoo Finance, source secondaire"],
["Antériorité","Une date d'historique antérieure à la fondation indiquée appelle une vérification de continuité ; elle ne la prouve pas.","Comparaison des deux champs, sans rapprochement officiel"],
["Données d'indice","Fondation et entrée dans l'indice sont reprises du fichier de composition local, source secondaire à rapprocher.","data/raw/sp500_constituents.csv"],
["Photographie actuelle","Les dernières publications et les retraitements disponibles ne forment pas un historique investissable sans anticipation.","research/selection_rule.md"],
["Archives","L'ancien export univers_82.xlsx est conservé comme état antérieur. Ce classeur contient le nouvel univers.","research/archive/2026-09-05_avant_corrections/manifest.csv"],
];
notes.getRange("A1:C"+lectures.length).values=lectures;
notes.getRange("A1:C"+lectures.length).format.wrapText=true;
notes.getRange("A1:C"+lectures.length).format.verticalAlignment="center";
notes.getRange("A1:C"+lectures.length).format.rowHeight=68;
notes.getRange("A1:A"+lectures.length).format.columnWidth=27;
notes.getRange("B1:B"+lectures.length).format.columnWidth=85;
notes.getRange("C1:C"+lectures.length).format.columnWidth=66;
header(notes.getRange("A1:C1"));
notes.showGridLines=false;
notes.freezePanes.freezeRows(1);
const inspection=await wb.inspect({kind:"region",sheetId:"Recapitulatif",range:"A1:C18",maxChars:4500,tableMaxRows:18,tableMaxCols:3});
console.log(inspection.ndjson);
const values=recap.getRange("B3").values;
if (Number(values[0][0])!==n) throw new Error("Le total du récapitulatif ne correspond pas à l'univers.");
await fs.mkdir(path.dirname(output),{recursive:true});
const file=await SpreadsheetFile.exportXlsx(wb);
await file.save(output);
const previews=path.join(path.dirname(output),"apercus");
await fs.mkdir(previews,{recursive:true});
for(const name of names){
  const range=name==="Recapitulatif"?"A1:C20":name==="Lecture et sources"?"A1:C6":"A1:F7";
  const png=await wb.render({sheetName:name,range,scale:1.3,format:"png"});
  await fs.writeFile(path.join(previews,name.replaceAll(" ","_")+".png"),new Uint8Array(await png.arrayBuffer()));
}
console.log("Classeur exporté : "+n+" entreprises, "+names.length+" feuilles.");
