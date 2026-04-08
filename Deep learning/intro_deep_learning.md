# 🧠 Introduction simplifiée au Deep Learning

Vidéo explicative sur la chaine youtude de 
AI for you - Morgan Gautherot  https://www.youtube.com/@AIforyouMorganGautherot

## 1. C’est quoi un réseau de neurones ?

Un réseau de neurones est une machine qui apprend à partir d’exemples.

### Exemple :

- On montre des images de chats 🐱
- Le modèle apprend à reconnaître un chat

---

## 2. Structure d’un réseau

Un réseau est composé de couches :

- **Entrée** → les données (image, texte…)
- **Couches cachées** → traitement
- **Sortie** → résultat (prédiction)

---

## 3. Comment apprend le modèle ?

### Étapes :

1. **Prédiction (forward)**
   - Le modèle donne une réponse

2. **Erreur (loss)**
   - On compare avec la vraie réponse

3. **Correction (backward)**
   - Le modèle ajuste ses paramètres

👉 Il répète ça plusieurs fois pour s’améliorer

---

## 4. Accuracy et Loss

### Accuracy (précision)

- % de bonnes réponses
- Plus c’est élevé → mieux c’est

### Loss (erreur)

- Mesure à quel point il se trompe
- Plus c’est bas → mieux c’est

---

## 5. Comprendre les résultats

### Exemple :

#### Train :
- Epoch 1 → 38.6%
- Epoch 5 → 64.0%

#### Test :
- Epoch 1 → 52.5%
- Epoch 5 → 68.2%

👉 Interprétation :
- Le modèle s’améliore (accuracy ↑)
- L’erreur diminue (loss ↓)
- Train et test sont proches → bon signe

---

## 6. Overfitting (à éviter)

### Mauvais cas :
- Train = 95%
- Test = 60%

👉 Le modèle a appris par cœur ❌

### Bon cas :
- Train ≈ Test

👉 Le modèle généralise bien ✅

---

## 7. Epoch, Batch, Iteration

### Epoch
👉 1 passage complet sur toutes les données

---

### Batch
👉 Un petit groupe de données

Exemple :
- 1000 images
- batch size = 100
→ 10 batches

---

### Iteration
👉 1 apprentissage sur 1 batch

---

## 8. Relation entre les 3

👉 Formule :
Nombre d’iterations = nombre de batches par epoch


---

## 9. Exemple concret

- 1000 images
- batch size = 100

👉 Calcul :
- 10 batches
- 10 iterations
- 1 epoch = 10 iterations

---

## 10. Analogie simple

- Epoch → lire tout un livre 📘
- Batch → lire un chapitre 📄
- Iteration → apprendre un chapitre 🔁

---

## 11. Schéma d’apprentissage

### Début (Epoch 1)
- Accuracy faible ❌
- Loss élevée 🔴

### Milieu
- Accuracy augmente 📈
- Loss diminue 🟠

### Fin (Epoch 5)
- Accuracy bonne 👍
- Loss faible 🟢

---

## 12. Résumé final

- Le modèle apprend en répétant (epochs)
- Il progresse progressivement
- Il faut surveiller :
  - accuracy ↑
  - loss ↓
  - train ≈ test

---

## 13. À retenir absolument

Batch = petit groupe de données
Iteration = 1 apprentissage sur un batch
Epoch = tout le dataset parcouru