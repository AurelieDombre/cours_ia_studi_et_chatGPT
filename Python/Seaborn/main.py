import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Création d'un DataFrame de démonstration
data = pd.DataFrame({
   'age': [23, 45, 56, 78, 21, 34, 49, 50, 20, 31, 73, 24, 58, 46, 35, 62]
})

# Tracé de l'histogramme avec estimation de la densité
sns.histplot(data['age'], kde=True)
plt.title('Distribution des âges')
plt.show()