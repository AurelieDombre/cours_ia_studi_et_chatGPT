# Algorithmes classiques de Machine Learning

## 🌳 1. Arbres de décision (Decision Trees)

### 🧠 Idée
Un arbre de décision fonctionne comme une suite de questions (if/else).

Exemple :
- Surface > 80 ?
  - Oui → Prix élevé
  - Non → autre question

### 🎯 Fonctionnement
- Découpe les données en règles simples
- Crée des branches jusqu’à une décision finale

### ✅ Avantages
- Facile à comprendre
- Interprétable

### ❌ Inconvénients
- Risque d’overfitting (sur-apprentissage)

---

## 🌲🌲 2. Random Forest (Forêts aléatoires)

### 🧠 Idée
Utilise plusieurs arbres de décision.

- Chaque arbre apprend sur une partie des données
- Le modèle final combine leurs prédictions (vote ou moyenne)

### 🎯 Résultat
→ Modèle plus robuste et plus précis

### ✅ Avantages
- Très performant
- Réduit l’overfitting

### ❌ Inconvénients
- Moins interprétable
- Plus coûteux en calcul

---

## 👥 3. K plus proches voisins (KNN)

### 🧠 Idée
“Dis-moi qui sont tes voisins, je te dirai qui tu es”

- On regarde les K points les plus proches
- On prend la majorité

### 🎯 Exemple
- 5 voisins → 3 chats, 2 chiens → chat

### ✅ Avantages
- Très simple
- Pas de phase d’apprentissage

### ❌ Inconvénients
- Lent sur gros datasets
- Sensible au bruit

---

## 📊 4. Naive Bayes

### 🧠 Idée
Basé sur les probabilités.

Calcule :
P(classe | données)

Hypothèse :
→ les variables sont indépendantes

### 🎯 Exemple
- Classification de texte (spam)

### ✅ Avantages
- Très rapide
- Très efficace pour le texte

### ❌ Inconvénients
- Hypothèse d’indépendance souvent fausse

---

## ⚔️ 5. Support Vector Machine (SVM)

### 🧠 Idée
Trouver la meilleure frontière entre les classes.

- Sépare les données avec une ligne ou un plan
- Maximise la distance entre les classes

### 🎯 Cas complexe
- Utilisation de "kernel" pour séparer des données non linéaires

### ✅ Avantages
- Très performant
- Efficace en haute dimension

### ❌ Inconvénients
- Difficile à comprendre
- Coûteux en calcul

---

# ⚖️ Comparaison des algorithmes

| Algorithme        | Idée principale        | Facilité | Performance | Cas typique |
|------------------|----------------------|----------|-------------|------------|
| Arbre de décision | règles (if/else)     | ⭐⭐⭐⭐     | ⭐⭐          | simple, explicable |
| Random Forest     | plusieurs arbres     | ⭐⭐⭐      | ⭐⭐⭐⭐        | général, robuste |
| KNN               | voisins proches      | ⭐⭐⭐⭐     | ⭐⭐          | petits datasets |
| Naive Bayes       | probabilités         | ⭐⭐⭐⭐     | ⭐⭐⭐         | texte, spam |
| SVM               | frontière optimale   | ⭐⭐       | ⭐⭐⭐⭐        | données complexes |

---

# 🧠 Comment choisir ?

Le choix dépend de plusieurs facteurs :

### 📊 Taille des données
- < 10K → KNN, arbres
- < 100K → SVM, Random Forest
- > 100K → SGD (plus rapide)

### 🏷️ Type de problème
- Classification → SVM, Naive Bayes
- Régression → Ridge, Lasso, SVR
- Clustering → K-Means, MeanShift

### 📌 Cas pratiques
- Simple et explicable → Arbre de décision
- Bon choix général → Random Forest
- Petit dataset → KNN
- Texte → Naive Bayes
- Données complexes → SVM

---

# 🔥 Résumé

Tous ces algorithmes ont le même objectif :

👉 apprendre à prédire

Mais ils utilisent des stratégies différentes :

- Arbre → règles
- Random Forest → ensemble d’arbres
- KNN → proximité
- Naive Bayes → probabilités
- SVM → séparation optimale

---

# 🚀 Conclusion

👉 Il n’existe pas de meilleur algorithme universel

Le bon choix dépend :
- des données
- de leur taille
- du problème

👉 En pratique :
on teste plusieurs modèles et on compare leurs performances