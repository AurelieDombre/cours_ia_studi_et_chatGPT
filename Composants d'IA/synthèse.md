---

# 🧠 FICHE 1 — Modèles & Algorithmes clés (VERSION DÉTAILLÉE)

---

## 🌳 1. Arbre de décision

### 🧾 À retenir (version courte)

* Modèle basé sur des **règles de décision successives**
* Pas besoin de **scaling** ni de transformation lourde
* Gère les **valeurs manquantes et données imparfaites**
* Très **interprétable (explicable facilement)**

---

### 💡 Explication approfondie

Un arbre de décision fonctionne comme une suite de questions :

> “Si revenu > 2000€” → branche gauche
> “Sinon” → branche droite

Un arbre construit ses splits en choisissant la variable et le seuil qui **réduisent le plus l’impureté** :

👉 Gini :

* mesure l’hétérogénéité d’un nœud
* plus il est faible → plus le nœud est “pur”

👉 Entropie :

* mesure le désordre (inspiré de la théorie de l’information)

👉 Information Gain :

* gain obtenu après un split

👉 À la fin :
on arrive à une **feuille = prédiction**

---

### 🔍 Détails importants

* Les arbres peuvent gérer :

  * variables numériques **et** catégorielles
* Pas besoin de :

  * normalisation
  * transformation linéaire

👉 MAIS :

* biais vers variables avec beaucoup de modalités
* instabilité forte

---

### 🎯 Intuition

> “On découpe les données jusqu’à obtenir des groupes homogènes”

---

### ⚠️ Pièges classiques

* Trop profond → **overfitting (variance élevée)**
* Trop simple → **underfitting (biais élevé)**
* Sensible aux petites variations des données

---

### 🛠 Hyperparamètres clés

* `max_depth`
* `min_samples_split`
* `min_samples_leaf`
* `criterion` (gini / entropy)

---

### 🛠 Bonnes pratiques

* Limiter la profondeur (`max_depth`)
* Utiliser un ensemble (Random Forest)

---

## 🌲 2. Random Forest

### 🧾 À retenir

* Ensemble de **plusieurs arbres indépendants**
* Utilise le **bagging (bootstrap sampling)**
* Réduit la **variance**
* Très robuste au surapprentissage

---

### 💡 Explication approfondie

Principe :

1. On tire plusieurs **échantillons avec remise**
2. On entraîne un arbre sur chaque échantillon
3. On combine les résultats

👉 Classification → vote majoritaire
👉 Régression → moyenne

En plus du bagging :

👉 Random Forest ajoute :
➡️ **feature randomness**

À chaque split :
👉 on ne teste qu’un sous-ensemble de variables

➡️ Résultat :

* arbres **décorrélés**
* meilleure généralisation
  
---

### 🎯 Intuition

> “Un seul arbre peut se tromper, une forêt corrige les erreurs individuelles”

---

### ⚠️ Limites

* Peu performant sur :
  * données très haute dimension sparse (texte brut)
  * Moins bon que boosting sur problèmes complexes
  * Moins interprétable
  * Plus lourd en calcul
  * Peut sur-apprendre si mal réglé
  
---

### 🛠 Bonnes pratiques

* Ajuster `n_estimators`
* Limiter profondeur des arbres
* Utiliser feature importance

---


### 🆚 Bonus : Random Forest vs Gradient Boosting

| RF                  | Boosting                     |
| ------------------- | ---------------------------- |
| arbres indépendants | arbres séquentiels           |
| réduit variance     | réduit biais                 |
| robuste             | plus performant mais fragile |

---

## 📈 3. Régression logistique

### 🧾 À retenir

* Modèle **linéaire probabiliste**
* Sortie entre **0 et 1 (probabilité)**
* Très **interprétable**

---

### 💡 Explication approfondie

Elle modélise :

👉 probabilité d’appartenir à une classe

via une fonction **sigmoïde** :

* transforme une somme linéaire en probabilité

👉 Décision :

* seuil (souvent 0.5)

---

### 🔍 Détails importants

* Optimisation :

  * descente de gradient
  * minimise log-loss (cross-entropy)

* Interprétation :

  * coefficient = impact sur le log-odds

👉 exp(coef) = **odds ratio**

---

### 🎯 Intuition

> “On trace une frontière (ligne / plan) entre les classes”

---

### ⚠️ Limites

* Mauvaise performance sur relations complexes
* Sensible aux variables corrélées
* Nécessite du **scaling**

---

### 🛠 Bonnes pratiques

* Standardiser les données
* Vérifier multicolinéarité
* Régularisation (L1 / L2)

---

## ⚖️ 4. Random Forest vs Régression Logistique

| Critère        | Régression logistique | Random Forest       |
| -------------- | --------------------- | ------------------- |
| Interprétation | ✅ Très claire         | ❌ difficile         |
| Performance    | ⚠️ limitée            | ✅ souvent meilleure |
| Non-linéarité  | ❌                     | ✅                   |
| Robustesse     | ⚠️ moyenne            | ✅ forte             |

---

### 🎯 Règle simple

* Explication métier → **logistique**
* Données complexes → **Random Forest**

---

## 📊 5. K-Means (clustering)

### 🧾 À retenir

* Algorithme **non supervisé**
* Regroupe en **K clusters**
* Basé sur la **distance (euclidienne)**

---

### 💡 Fonctionnement détaillé

1. Initialisation de K centres (aléatoires)
2. Attribution de chaque point au centre le plus proche
3. Recalcul des centres
4. Répétition jusqu’à convergence

---

### ⚠️ Détails critiques

* Sensible à l’initialisation
  👉 utiliser **k-means++**

* Suppose :

  * clusters sphériques
  * taille similaire

---

---

### 📌 Alternatives importantes

* DBSCAN → clusters non sphériques
* Hierarchical clustering → structure arborescente

---

### 🎯 Intuition

> “Chaque point va vers le centre le plus proche”

---

### ⚠️ Pièges

* Mauvais choix de K
* Sensible au scaling
* Mauvais pour formes complexes

---

### 🛠 Bonnes pratiques

* Méthode du coude (Elbow)
* Standardisation des données
* Tester plusieurs K

---

## 📉 6. PCA (Réduction de dimension)

### 🧾 À retenir

* Réduit le nombre de variables
* Supprime la **redondance**
* Conserve la **variance maximale**
* Composantes triées par importance

---

### 💡 Explication approfondie

La PCA transforme les variables en :
👉 **nouvelles variables orthogonales (indépendantes)**

appelées :
👉 **composantes principales**

---

### 🎯 Intuition

> “On compresse l’information sans trop la perdre”

---

### ⚠️ Limites

* Perte d’interprétabilité
* Transformation abstraite

---

### ⚠️ Point critique

👉 PCA est **linéaire**

➡️ ne capture pas :

* relations non linéaires

---
### 🛠 Cas d’usage

* Visualisation (2D / 3D)
* Accélération des modèles
* Réduction du bruit

---

## 🤖 7. Supervisé vs Non supervisé

### 🧾 À retenir

| Type          | Données     | Objectif |
| ------------- | ----------- | -------- |
| Supervisé     | Avec labels | Prédire  |
| Non supervisé | Sans labels | Explorer |

---

### 💡 Explication approfondie

👉 Supervisé :

* apprend une relation entrée → sortie
* ex : classification spam

👉 Non supervisé :

* découvre des structures cachées
* ex : segmentation client

---

### 🎯 Différence clé

> “Supervisé = prédire, Non supervisé = comprendre”

---

# 🧠 FICHE 2 — Concepts fondamentaux (VERSION DÉTAILLÉE)

---

## 🎯 1. Biais vs Variance

### 🧾 À retenir

* Biais élevé → modèle trop simple
* Variance élevée → modèle trop complexe

---

### 🔍 Décomposition erreur

Erreur totale =

👉 biais² + variance + bruit irréductible

---

### 💡 Explication approfondie

👉 Biais :

* simplifie trop la réalité
* erreurs systématiques

👉 Variance :

* dépend trop des données
* instable

* modèles simples → biais élevé
* modèles complexes → variance élevée

👉 ex :

* arbre profond → variance
* régression → biais
---

### 🎯 Image mentale

* Biais → “je généralise trop”
* Variance → “je mémorise tout”

---

### ⚠️ Impact

| Cas             | Résultat     |
| --------------- | ------------ |
| Biais élevé     | underfitting |
| Variance élevée | overfitting  |

---

### 🎯 Objectif

👉 Trouver le **juste équilibre**

---

## 🔗 2. Corrélation vs Causalité

### 🧾 À retenir

* Corrélation ≠ causalité
* Peut être dû à une variable cachée

---

### 💡 Approfondissement

👉 Corrélation :

* relation statistique
* peut être accidentelle

👉 Causalité :

* lien direct cause → effet

---

### 🎯 Comment prouver ?

* A/B testing
* Expériences contrôlées
* Modèles causaux

---

### ⚠️ Piège classique

> “Les données seules ne prouvent pas la causalité”

---

## 📉 3. Overfitting (surapprentissage)

### 🧾 À retenir

* Apprend trop les données d’entraînement
* Mauvaise généralisation

---

### 💡 Détection

* Train score élevé
* Test score faible

---

### 🛠 Solutions

* Plus de données
* Cross-validation
* Régularisation
* Simplifier le modèle

---

### 🔍 Techniques avancées

* Early stopping
* Dropout (deep learning)
* Data augmentation

---

# 🧠 FICHE 3 — Préparation des données (VERSION DÉTAILLÉE)

---

## ⚠️ 1. Data Leakage

### 🧾 À retenir

* Fuite d’information du futur
* Résultats artificiellement bons
* * target encoding mal fait
* CV mal construite
* features temporelles mal alignées

---

### 💡 Exemples

* Scaling avant split
* Feature contenant la cible
* Mauvais pipeline

---

### 🛠 Solutions

* Pipeline strict
* Split avant preprocessing

---

## 🧩 2. Données manquantes

### 🧾 À retenir

| Type         | Solution          |
| ------------ | ----------------- |
| Catégorielle | mode / “inconnu”  |
| Numérique    | moyenne / médiane |

---

### 💡 Approfondissement

* Médiane → robuste aux outliers
* Modèles → imputation avancée

---

## 📏 3. Scaling

### 🧾 À retenir

* Nécessaire pour modèles basés sur distance

---

### 💡 Pourquoi ?

👉 variables sur même échelle
👉 sinon biais dans calculs

---

### ⚠️ Important

👉 inutile pour :

* arbres
* Random Forest

👉 crucial pour :

* KNN
* SVM
* K-Means
* régression logistique

---

## 🔗 4. Multicolinéarité

### 🔍 Détection

* VIF (Variance Inflation Factor)

---

### 🧾 À retenir

* Variables redondantes

---

### 💡 Impact

* instabilité
* coefficients incohérents

---

# 🧠 FICHE 4 — Évaluation des modèles (VERSION DÉTAILLÉE)

---

## 📊 1. ROC & AUC

### 🧾 À retenir

* ROC = compromis faux positifs / vrais positifs
* AUC = performance globale

---

### 🔍 Interprétation AUC

* 0.5 → aléatoire
* 0.7 → acceptable
* 0.8 → bon
* 0.9 → excellent

---

### 💡 Lecture

* proche coin haut gauche = bon modèle

---

## ⚖️ 2. Dataset déséquilibré

### 🧾 À retenir

⚠️ Accuracy trompeuse

---

### 💡 Exemple

95% classe A → modèle nul peut faire 95%

---

### ✅ Métriques clés

* précision
* rappel
* F1-score
* ROC-AUC

---

### ⚠️ Limite

ROC trompeur si dataset déséquilibré

👉 préférer :

* Precision-Recall curve

---

## ⚖️ 2. Dataset déséquilibré (complété)

### 🛠 Solutions

* Resampling :

  * oversampling (SMOTE)
  * undersampling

* Pondération des classes

---

# 🧠 FICHE 5 — Production & Data (VERSION DÉTAILLÉE)

---

## ⚙️ 1. Orchestrateur

### 🧾 À retenir

* Automatise pipelines
* Planifie tâches

---

### 💡 Exemple

Airflow :

* DAG
* monitoring
* retry

---

## 🔄 2. Batch vs Temps réel

### 💡 Différence clé


| Batch         | Temps réel     |
| ------------- | -------------- |
| volumineux    | faible latence |
| simple        | complexe       |
| moins coûteux | infra lourde   |


* Batch → différé
* Temps réel → instantané

---

## 📉 3. Data Drift

### 🧾 À retenir

* données évoluent → modèle devient obsolète

---

### 🛠 Solutions

* monitoring
* retrain
* alertes


---

# 🧠 FICHE 6 — Deep Learning & NLP (VERSION DÉTAILLÉE)

---

## 🔁 1. Backpropagation

### 🧾 À retenir

* calcule erreur
* ajuste poids

---

### 💡 Processus

1. prédiction
2. calcul erreur
3. mise à jour poids

---

## ⚡ 2. Fonction d’activation

### 🧾 À retenir

* introduit non-linéarité

---

### 💡 Pourquoi ?

Sans ça → modèle linéaire

---

### 🔍 Exemples

* ReLU :

  * rapide
  * évite gradient vanishing

* Sigmoid :

  * probabilités
  * mais saturation

---

## 🧠 3. MLP vs CNN

### 💡 Différence

* MLP → données tabulaires
* CNN → images
        * convolution → détection motifs
        * pooling → réduction dimension

---

## 📝 4. TF-IDF vs Embedding

### 💡 Différence

* TF-IDF → fréquence brute
* Embeddings (Word2Vec, BERT) :

  * capturent similarité sémantique
  * dimension dense

---

# 🧠 FICHE 7 — Business & Expérimentation (VERSION DÉTAILLÉE)

---

## 🧪 1. A/B Testing

### 🧾 À retenir

* comparaison de 2 groupes
* mesure impact réel

---

### 💡 Étapes

1. randomisation
2. test
3. analyse statistique

---

### 🔍 Concepts statistiques

* p-value
* intervalle de confiance
* puissance statistique

---

### ⚠️ Pièges

* biais de sélection
* durée trop courte
* effet saisonnier

---

## 💰 2. Expliquer un gain modèle

### 🧾 À retenir

👉 toujours traduire en business

---

### 💡 Exemple développé

> +10% précision
> → -10% erreurs
> → moins de coûts / plus de revenus

### 🔍 Approche structurée

1. Métrique ML
2. Impact opérationnel
3. Traduction business

---

### 🎯 Exemple enrichi

> +10% recall fraude
> → +10% fraudes détectées
> → économies directes
> → ROI mesurable

---