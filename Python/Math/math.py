# Initialiser une matrice  [2 X 3] 2 lignes et 3 colonnes

import numpy as np

array = np.array([[1,2,3], [4,5,6]])

print(array)

# Affiche :
#[[1 2 3]
# [4 5 6]]

# Initialiser une matrice rempli de 1
arrayOnes = np.ones([4,5])
print(arrayOnes)
# Affiche
# [[1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]]


arrayZeros = np.zeros_like(arrayOnes)
print(arrayZeros)
# Affiche
# [[0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]
#  [0. 0. 0. 0. 0.]]

# Matrice diagonale
arrayEyes = np.eye(4,4)
print(arrayEyes)

# Affiche
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]