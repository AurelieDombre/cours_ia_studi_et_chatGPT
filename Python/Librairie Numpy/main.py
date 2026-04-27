import numpy as np
import matplotlib.pyplot as plt

nu = 1 # moyenne
sigma = 0.2 # écart-type
nPoints = 10000 # nombre de points

# Génération de données aléatoires suivant une distribution normale
data = np.random.normal(nu, sigma, nPoints)

# Demande a numpy de calculer la moyenne et l'écart-type de nos données
mean = np.mean(data)
print("Moyenne calculée : ", mean)

stdDev = np.std(data)
print("Ecart-type calculé : ", stdDev)
