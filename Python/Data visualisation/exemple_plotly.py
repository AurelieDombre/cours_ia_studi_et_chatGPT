import pandas as pd
import plotly.express as px

data = pd.read_csv("dataset/Paris 2024 Olympics_Nations Medals.csv")

print(data.head())

fig = px.bar(data, x="NOC", y="Gold", title="Médailles d'or par pays")
fig.show()