import pandas as pd
import plotly.express as px

# Charge le fichier CSV dans un DataFrame pandas.
data = pd.read_csv("dataset/dataset_cours.csv")

# Affiche les 5 premieres lignes pour verifier que les donnees sont bien chargees.
print(data.head())

# La courbe de tendance "ols" demande la bibliotheque statsmodels.
# Si elle n'est pas installee, on affiche quand meme le graphique sans trendline.
try:
    import statsmodels.api as sm  # noqa: F401
    trendline_value = "ols"
except ModuleNotFoundError:
    trendline_value = None

# Cree un graphique en nuage de points.
# x = prix moyen
# y = nombre d'utilisateurs
# hover_data = informations affichees au survol
# size = taille des points selon la note
fig = px.scatter(
    data,
    x="Prix moyen",
    y="Nombre d'utilisateurs",
    trendline=trendline_value,
    hover_data=["Plateforme"],
    size="Note sur 10",
)

# Affiche le graphique dans le navigateur.
fig.show()

# Export en html
with open('plotly_graph.html', 'w') as f:
    f.write(fig.to_html(include_plotlyjs='cdn'))