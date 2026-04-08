# Gradient Descent (Descente de gradient)

Vidéo explicative sur : https://youtube.com/playlist?list=PLmBLgNjbSiTF0cl2UgKdyYcJ-AbzbvcsY&si=uC1YFfJE6X85hoVm

## 🎯 Objectif

Trouver les paramètres (a, b) qui minimisent l’erreur.

🔥 1. Le problème à résoudre en ML
On a vu que :

- modèle :

y = ax + b

- erreur (moindres carrés) :
  Erreur = Σ (y_réel - y_prédit)²

👉 Donc le but du machine learning :

trouver a et b qui minimisent l’erreur

---

## 🧠 Pourquoi on a besoin du gradient descent ?

👉 Problème :

On ne peut pas tester toutes les valeurs possibles de a et b
(il y en a une infinité)

👉 Solution :

On utilise une méthode intelligente pour descendre vers la meilleure solution

---

## ⛰️ Image mentale (super importante)

Imagine :

- une montagne

- en haut → erreur énorme ❌

- en bas → erreur minimale ✅

👉 Ton modèle est “quelque part” sur cette montagne

🎯 Objectif : descendre tout en bas

---

## ⚙️ Comment ça marche ?

1. On commence avec des valeurs au hasard (a, b)
2. On calcule l’erreur
3. On regarde dans quelle direction descendre
4. On fait un petit pas
5. On recommence

👉 encore et encore jusqu’au minimum

---
## 📉 Le mot “gradient” (important mais simple)

👉 Le gradient, c’est :

➡️ la direction dans laquelle l’erreur augmente le plus

Donc :

👉 on fait l’inverse pour descendre

---

## 🔁 Mise à jour des paramètres

À chaque étape :

a = a - learning_rate × dérivée
b = b - learning_rate × dérivée

👉 learning_rate = taille du pas

---

## ⚠️ Importance du learning rate

- trop grand ❌ → tu sautes partout, tu ne converges pas

- trop petit ❌ → trop lent

👉 il faut un bon équilibre

---

## 🔄 Boucle d’apprentissage

Répéter :

- prédire
- calculer erreur
- ajuster paramètres

👉 jusqu’à ce que l’erreur soit minimale

---

## 🤖 Lien avec le Machine Learning

Gradient descent =
👉 la méthode utilisée pour apprendre

Moindres carrés =
👉 ce qu’on cherche à minimiser

---

## 🔥 Ce que fait concrètement sklearn

Quand tu fais :

```python
model.fit(X, Y)
```

👉 en réalité :

-il calcule l’erreur

-il ajuste les paramètres

-il répète

👉 souvent avec une version optimisée du gradient descent

## 🧠 Résumé ultra clair

👉 Moindres carrés
= mesurer l’erreur

👉 Gradient descent
= réduire l’erreur

👉 Ensemble = cœur du machine learning