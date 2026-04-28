import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Configuration pour la reproductibilité
np.random.seed(42)

# Génération de 50 âges fictifs (entre 18 et 65 ans)
ages = np.random.normal(loc=38, scale=10, size=50)
ages = np.clip(ages, 18, 65).astype(int)

# Création du DataFrame
df = pd.DataFrame({'Age': ages})

# Sauvegarde en CSV
df.to_csv('donnees-ages.csv', index=False)

print("Le fichier 'donnees-ages.csv' a été généré avec succès.")

# 1. Charger les données
df = pd.read_csv('donnees-ages.csv')

# 2. Créer la visualisation
plt.figure(figsize=(10, 6))
sns.set_palette("pastel")
sns.set_theme(style="whitegrid")
sns.histplot(df['Age'], kde=True, color='skyblue', bins=15)


# 3. Personnalisation
plt.title('Distribution des âges des employés avec courbe KDE', fontsize=14)
plt.xlabel('Âge', fontsize=12)
plt.ylabel('Fréquence', fontsize=12)


# Affichage
plt.show()

# Pourquoi utiliser le KDE ? #
# L'histogramme est utile pour voir le comptage brut par tranches d'âge (les "bins"),
# mais la courbe KDE (Kernel Density Estimation) permet de lisser les variations pour voir la "forme" réelle de ta population.
# Elle aide à répondre à des questions comme :
# "L'entreprise a-t-elle un pic de recrutement chez les jeunes ou une population vieillissante ?"