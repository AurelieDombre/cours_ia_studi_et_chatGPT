
# 🧠 FICHE 1 — Modèles & Algorithmes clés

## 🌳 1. Arbre de décision

### 🧾 À retenir (version courte)

* Modèle basé sur des **règles de décision**
* Pas besoin de **scaling** ni d’encodage complexe
* Gère bien les **valeurs manquantes**
* Très **interprétable**

### 💡 Explication rapide

Un arbre découpe les données avec des questions du type :

> “Est-ce que l’âge > 30 ?”

Chaque nœud = une décision → on arrive à une prédiction.

### ⚠️ Piège classique

* Trop profond → **overfitting (variance élevée)**

---

## 🌲 2. Random Forest

### 🧾 À retenir

* Ensemble de plusieurs arbres
* Utilise le **bagging (échantillonnage avec remise)**
* Réduit la **variance**
* Plus robuste que 1 seul arbre

### 💡 Explication

On entraîne plusieurs arbres sur des subsets différents, puis :
👉 on **moyenne les prédictions**

### 🎯 Intuition

> “Plusieurs avis valent mieux qu’un seul”

---

## 📈 3. Régression logistique

### 🧾 À retenir

* Modèle **linéaire** pour classification
* Donne des **probabilités**
* Très **interprétable**

### 💡 Explication

Elle trace une frontière entre classes (souvent une droite).

### ⚠️ À savoir

* Sensible au **scaling**
* Mauvaise si relations **non linéaires**

---

## ⚖️ 4. Random Forest vs Régression Logistique

| Critère           | Régression logistique | Random Forest       |
| ----------------- | --------------------- | ------------------- |
| Interprétation    | ✅ Très claire         | ❌ difficile         |
| Performance       | ⚠️ limitée            | ✅ souvent meilleure |
| Données complexes | ❌                     | ✅                   |
| Scaling           | ✅ nécessaire          | ❌ inutile           |

### 🎯 Règle simple

* Besoin métier clair → **logistique**
* Performance → **Random Forest**

---

## 📊 5. K-Means (clustering)

### 🧾 À retenir

* Algorithme **non supervisé**
* Regroupe en **K clusters**
* Basé sur la **distance**

### 💡 Fonctionnement

1. On choisit K centres
2. On assigne les points
3. On recalcule les centres
4. On répète

### ⚠️ Pièges

* Il faut choisir **K**
* Sensible à l’échelle → scaling important

---

## 📉 6. PCA (Réduction de dimension)

### 🧾 À retenir

* Réduit le nombre de variables
* Supprime la **redondance**
* Conserve l’info principale (variance)

### 💡 Explication

Transforme les variables en nouvelles variables indépendantes :
👉 “composantes principales”

### 🎯 Pourquoi utile ?

* Accélère les modèles
* Améliore la visualisation

---

## 🤖 7. Supervisé vs Non supervisé

### 🧾 À retenir

| Type          | Données     | Objectif |
| ------------- | ----------- | -------- |
| Supervisé     | Avec labels | Prédire  |
| Non supervisé | Sans labels | Explorer |

### 💡 Exemples

* Supervisé → classification (spam)
* Non supervisé → clustering clients

---

# 🧠 FICHE 2 — Concepts fondamentaux

## 🎯 1. Biais vs Variance

### 🧾 À retenir

* **Biais élevé** → modèle trop simple (underfitting)
* **Variance élevée** → modèle trop complexe (overfitting)

### 💡 Image mentale

* Biais → “je simplifie trop”
* Variance → “je mémorise tout”

### 🎯 Objectif

👉 Trouver l’équilibre

---

## 🔗 2. Corrélation vs Causalité

### 🧾 À retenir

* Corrélation = lien statistique
* Causalité = relation de cause à effet

### 💡 Exemple

* Glaces ↑ → noyades ↑
  👉 corrélation (été), PAS causalité

### 🎯 Comment prouver la causalité ?

* Expériences (A/B test)
* Variables contrôlées

---

## 📉 3. Overfitting (surapprentissage)

### 🧾 À retenir

* Excellent sur train
* Mauvais sur test

### 💡 Détection

👉 Écart train vs test

### 🛠 Solutions

* Plus de données
* Régularisation
* Modèle plus simple

---

# 🧠 FICHE 3 — Préparation des données

## ⚠️ 1. Data Leakage (fuite de données)

### 🧾 À retenir

* Infos du test dans le train ❌
* Résultats faussés

### 💡 Exemple

* Scaling AVANT split

### ✅ Bonne pratique

👉 Split → puis preprocessing

---

## 🧩 2. Données manquantes

### 🧾 À retenir

* Catégorielles → mode / “inconnu”
* Numériques → moyenne / médiane

### ⚠️ Exception

* Arbres → gèrent naturellement

---

## 📏 3. Scaling (normalisation)

### 🧾 À retenir

* Important pour :

  * Régression logistique
  * SVM
  * K-Means

* Pas nécessaire pour :

  * Arbres
  * Random Forest

---

## 🔗 4. Multicolinéarité

### 🧾 À retenir

* Variables très corrélées (> 0.8)
* Problème pour modèles linéaires

### 🛠 Solutions

* Supprimer une variable
* PCA

---

# 🧠 FICHE 4 — Évaluation des modèles

## 📊 1. ROC & AUC

### 🧾 À retenir

* ROC = courbe TPR vs FPR
* AUC = performance globale

### 🎯 Interprétation

* 1 → parfait
* 0.5 → aléatoire

---

## ⚖️ 2. Dataset déséquilibré

### 🧾 À retenir

⚠️ Accuracy trompeuse

### ✅ Utiliser

* Précision
* Rappel
* F1-score
* ROC-AUC

---

# 🧠 FICHE 5 — Production & Data

## ⚙️ 1. Orchestrateur (Airflow)

### 🧾 À retenir

* Automatise les pipelines
* Planifie et surveille

---

## 🔄 2. Batch vs Temps réel

| Type       | Description         |
| ---------- | ------------------- |
| Batch      | Traitement par lots |
| Temps réel | Réponse instantanée |

---

## 📉 3. Data Drift

### 🧾 À retenir

* Données changent avec le temps

### 🛠 Solution

* Monitoring
* Réentraînement

---

# 🧠 FICHE 6 — Deep Learning & NLP

## 🔁 1. Backpropagation

### 🧾 À retenir

* Ajuste les poids selon l’erreur

---

## ⚡ 2. Fonction d’activation

### 🧾 À retenir

* Ajoute de la **non-linéarité**
* Indispensable

---

## 🧠 3. MLP vs CNN

| MLP                | CNN     |
| ------------------ | ------- |
| Données tabulaires | Images  |
| Pas spatial        | Spatial |

---

## 📝 4. TF-IDF vs Embedding

| TF-IDF    | Embedding  |
| --------- | ---------- |
| Fréquence | Sens       |
| Simple    | Contextuel |

---

# 🧠 FICHE 7 — Business & Expérimentation

## 🧪 1. A/B Testing

### 🧾 À retenir

* 2 groupes (A vs B)
* Comparaison statistique

---

## 💰 2. Expliquer un gain modèle

### 🧾 À retenir

👉 Toujours traduire en **impact métier**

### 💡 Exemple

> +10% précision = -10% erreurs = +X€

---


