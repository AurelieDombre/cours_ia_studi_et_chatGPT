# Fonction sigmoïde (dans le Machine Learning)

## 🔥 1. Le problème en machine learning (classification)

En machine learning, il existe deux grands types de problèmes :

- Régression → prédire une valeur (ex : prix)
- Classification → prédire une catégorie (ex : spam / pas spam)

---

## ❌ 2. Problème avec un modèle simple

Avec un modèle linéaire :

y = ax + b

👉 on obtient des valeurs comme :
- -3
- 2.7
- 15

❌ Ces valeurs ne sont pas adaptées pour faire de la classification

---

## ✅ 3. La solution : la sigmoïde

On garde le modèle :

z = ax + b

Puis on applique la fonction sigmoïde :

y = σ(z)

Avec :

σ(x) = 1 / (1 + e^(-x))

---

## 🎯 4. Ce que ça change

👉 Le résultat est maintenant entre 0 et 1

Donc on peut interpréter la sortie comme une probabilité :

- 0.8 → 80% de chance que ce soit "oui"
- 0.2 → 20% de chance

---

## 🤖 5. En machine learning

Le modèle complet devient :

y = σ(ax + b)

👉 Cela s'appelle la **régression logistique**

---

## 🔗 6. Lien avec les autres concepts

- Le modèle linéaire calcule un score
- La sigmoïde transforme ce score en probabilité

👉 Régression linéaire :

y=ax+b

👉 Régression logistique (classification) :

y=σ(ax+b)

👉 donc :

- moindres carrés → pour la régression

- sigmoïde → pour la classification


---

## ⚙️ 7. Comment le modèle apprend ?

Même logique que pour la régression :

1. Le modèle prédit (une probabilité)
2. Il compare avec la vraie valeur (0 ou 1)
3. Il calcule une erreur
4. Il ajuste les paramètres (gradient descent)

---

## 🧠 8. Image mentale simple

👉 La sigmoïde = un filtre

- modèle linéaire → donne un score brut
- sigmoïde → transforme ce score en probabilité

---

## 🔥 9. Résumé

👉 La sigmoïde :

- transforme n’importe quel nombre en valeur entre 0 et 1
- permet de faire de la classification
- convertit un score en probabilité

---

## 🚀 Conclusion

👉 En machine learning :

- moindres carrés → mesurer l’erreur (régression)
- gradient descent → optimiser le modèle
- sigmoïde → permettre la classification

👉 Ces éléments forment la base de nombreux modèles (dont les réseaux de neurones)