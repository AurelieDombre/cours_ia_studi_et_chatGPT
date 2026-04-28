import pandas as pd
import matplotlib.pyplot as plt

# Chargement
df = pd.read_csv('dataframe_visiteurs.csv', encoding='latin-1')

# Conversion des dates
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%y')

# Filtrage
df_filtered = df[df["Duree"] > 30]

# Tri par date
df_filtered = df_filtered.sort_values(by="Date")

# Moyennes
m_duree = df_filtered["Duree"].mean()
m_nb_click = df_filtered["Nombre de clicks"].mean()

print(f"Moyenne durée : {m_duree:.2f}")
print(f"Moyenne clicks : {m_nb_click:.2f}")

# Graphique (courbe)
plt.figure()

plt.plot(df_filtered["Date"], df_filtered["Duree"], marker='o')

plt.xlabel("Date")
plt.ylabel("Durée de visite")
plt.title("Évolution de la durée des visites")
plt.grid(True)

plt.xticks(rotation=45)  # meilleure lisibilité des dates
plt.tight_layout()

plt.show()