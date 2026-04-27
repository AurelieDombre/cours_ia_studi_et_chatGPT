import pandas as pd
import plotly.express as px

# Associe chaque annee au vrai nom du fichier CSV present dans le dossier dataset.
files = {
    "1994": "Lillehammer 1994 Olympics Nations Medals.csv",
    "1996": "Atlanta 1996 Olympics Nations Medals.csv",
    "1998": "Nagano 1998 Olympics Nations Medals.csv",
    "2000": "Sydney 2000 Olympics Nations Medals.csv",
    "2002": "SaltLakeCity 2002 Olympics Nations Medals.csv",
    "2004": "Athens 2004 Olympics Nations Medals.csv",
    "2006": "Torino 2006 Olympics Nations Medals.csv",
    "2008": "Beijing_2008_ Olympics_Nations_Medals.csv",
    "2010": "Vancouver 2010 Olympics Nations Medals.csv",
    "2012": "London 2012 Olympics Nations Medals.csv",
    "2014": "Sochi 2014 Olympics Nations Medals.csv",
    "2016": "Rio 2016 Olympics Nations Medals.csv",
    "2018": "PyeongChang 2018 Olympics Nations Medals.csv",
    "2020": "Tokyo 2020 Olympics Nations Medals.csv",
    "2022": "beijing_2022_Olympics_Nations_Medals.csv",
    "2024": "Paris 2024 Olympics_Nations Medals.csv",
}

# Liste des annees. Elle servira aussi pour l'axe horizontal du graphique.
dates = list(files.keys())

# Dictionnaire qui stockera chaque DataFrame charge.
data = {}

# Charge tous les fichiers CSV un par un.
for date in dates:
    data[date] = pd.read_csv("dataset/" + files[date])

    # Affiche un apercu du fichier charge pour verifier que tout fonctionne.
    print(f"\nApercu du fichier {date} :")
    print(data[date].head())

# Listes contenant le nombre de medailles d'or pour les USA et le Japon.
gold_array_usa = []
gold_array_jpn = []

# Pour chaque annee, on filtre la ligne du pays puis on recupere la valeur Gold.
for date in dates:
    gold_usa = data[date][data[date]["NOC"] == "USA"]["Gold"].item()
    gold_jpn = data[date][data[date]["NOC"] == "JPN"]["Gold"].item()

    gold_array_usa.append(gold_usa)
    gold_array_jpn.append(gold_jpn)

# Cree un graphique en lignes avec les deux series.
fig = px.line(
    x=dates,
    y=[gold_array_usa, gold_array_jpn],
    range_y=[0, 50],
    title="Evolution des medailles d'or : USA vs JPN",
    labels={"x": "Annee", "value": "Nombre de medailles d'or"},
)

# Renomme les courbes pour avoir une legende claire.
trace_names = ["USA", "JPN"]
for i, trace in enumerate(fig.data):
    trace.update(name=trace_names[i])

# Ajoute les titres des axes.
fig.update_layout(
    xaxis_title="Annee",
    yaxis_title="Nombre de medailles d'or",
)

# Affiche le graphique.
fig.show()
