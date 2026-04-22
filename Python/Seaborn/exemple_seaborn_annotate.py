import matplotlib.pyplot as plt
import seaborn as sns


# On charge un dataset d'exemple fourni par Seaborn.
# "titanic" contient des informations sur les passagers du Titanic
# (âge, sexe, classe, survie, etc.).
titanic = sns.load_dataset("titanic")
# Le dataset Titanic contient des NaN dans la colonne age. Ça peut casser le modèle logistique.
titanic = titanic.dropna(subset=["age", "survived"])

# head() affiche les 5 premières lignes du tableau.
# C'est pratique pour voir rapidement à quoi ressemblent les données.
print(titanic.head())

# On définit des "tranches" d'âge.
# Ici, Seaborn va regrouper les âges autour de ces bornes
# pour rendre la visualisation plus lisible.
age_bins = [15, 30, 45, 60]


# Étape 1 : calculer les valeurs
age_min = titanic["age"].min()
age_max = titanic["age"].max()
age_mean = titanic["age"].mean()
survival_mean = titanic["survived"].mean()


# Étape 2 : ajouter les lignes + point

# Version basique
# fig = sns.regplot(
#     data=titanic,
#     x="age",
#     y="survived",
#     logistic=True
# )

# Version moderne
fig = sns.lmplot(
    data=titanic,
    x="age",
    y="survived",
    hue="sex",
    x_bins=age_bins,
    logistic=True,
    height=6,
    aspect=1.2
)

ax = fig.ax

# Lignes verticales (min / max / moyenne)
# Ajouter les éléments visuels

ax.axvline(age_min, linestyle="--", label="Âge min")
ax.axvline(age_max, linestyle="--", label="Âge max")
ax.axvline(age_mean, linestyle="-", linewidth=2, label="Âge moyen")

# Point pour la moyenne
ax.scatter(age_mean, survival_mean, s=100)

# Annotation
ax.annotate(
    "Moyenne survie",
    xy=(age_mean, survival_mean),
    xytext=(age_mean + 5, survival_mean + 0.1),
    arrowprops=dict(arrowstyle="->")
)
# Légende
ax.legend()

# On fixe les limites de l'axe des x entre 0 et 80 ans
# pour éviter que le graphique ne s'étende trop loin.
fig.set(xlim=(0, 80))

# Affiche le graphique final.
plt.show()

