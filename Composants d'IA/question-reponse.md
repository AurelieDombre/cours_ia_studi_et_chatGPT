

# 🔹 Réponses détaillées (partie entretien)

## ✅ Question 1

**Différence entre corrélation et causalité + comment la prouver**

La **corrélation** désigne une relation statistique entre deux variables : lorsqu’une variable évolue, l’autre a tendance à évoluer aussi, dans le même sens ou en sens inverse. Cependant, cette relation ne signifie pas qu’il existe un lien de cause à effet.

La **causalité**, en revanche, implique qu’une variable influence directement une autre. Autrement dit, un changement dans la variable A entraîne un changement dans la variable B.

👉 Exemple simple :

* Corrélation : ventes de glaces ↔ nombre de noyades
* Causalité réelle : chaleur (variable cachée) influence les deux

👉 Pour prouver la causalité :

* Mettre en place une **expérience contrôlée (A/B test)**
* Isoler les variables (toutes choses égales par ailleurs)
* Utiliser des méthodes statistiques avancées (modèles causaux)

💡 En entretien, tu peux dire :

> “La corrélation est un signal, la causalité est une preuve.”

---

## ✅ Question 2

**Biais vs Variance (explication simple)**

Le compromis biais/variance est fondamental en machine learning.

* **Biais** : erreur due à un modèle trop simple
  → Il ne capture pas la complexité des données
  → Résultat : sous-apprentissage (underfitting)

* **Variance** : erreur due à un modèle trop complexe
  → Il apprend “par cœur” les données d’entraînement
  → Résultat : surapprentissage (overfitting)

👉 Exemple :

* Modèle simple → mauvaises performances partout → biais élevé
* Modèle trop complexe → parfait en train, nul en test → variance élevée

💡 Bonne phrase :

> “Le biais mesure l’erreur d’approximation, la variance mesure la sensibilité aux données.”

---

## ✅ Question 3

**Fuite de données (data leakage)**

La fuite de données se produit lorsque des informations du futur ou du jeu de test sont utilisées dans l’entraînement.

👉 Exemples courants :

* Normaliser les données **avant** le split train/test
* Utiliser une variable qui contient indirectement la cible
* Mélanger données futures et passées (cas temporel)

👉 Pourquoi c’est grave ?

* Le modèle semble très performant… mais échoue en production

👉 Comment l’éviter :

* Toujours faire le **split AVANT preprocessing**
* Utiliser des **pipelines propres**
* Vérifier les variables suspectes

💡 Phrase forte :

> “La fuite de données donne une illusion de performance.”

---

## ✅ Question 4

**Gestion des données manquantes**

👉 Variables catégorielles :

* Remplacer par la **modalité la plus fréquente**
* Ou créer une catégorie “inconnue”

👉 Variables numériques :

* Moyenne / médiane
* Modèles prédictifs (imputation avancée)

👉 Important :

* Certains modèles comme les **arbres** gèrent naturellement les valeurs manquantes

💡 À dire :

> “Le choix dépend du modèle et de la distribution des données.”

---

## ✅ Question 5

**Quand le scaling n’est pas nécessaire**

Le scaling n’est pas nécessaire pour les modèles basés sur des arbres :

* Arbres de décision
* Random Forest

👉 Pourquoi ?
Parce qu’ils utilisent des **seuils** (ex: x > 10), pas des distances.

👉 En revanche, il est essentiel pour :

* Régression logistique
* SVM
* KNN

💡 Phrase simple :

> “Le scaling est crucial pour les modèles basés sur la distance, inutile pour les arbres.”

---

## ✅ Question 6

**Multicolinéarité**

La multicolinéarité apparaît lorsque plusieurs variables sont fortement corrélées entre elles.

👉 Problèmes :

* Instabilité des modèles linéaires
* Difficulté d’interprétation

👉 Détection :

* Matrice de corrélation (> 0.8)
* VIF (Variance Inflation Factor)

👉 Solutions :

* Supprimer une variable
* Combiner
* Utiliser PCA

💡 À dire :

> “La multicolinéarité ajoute du bruit sans ajouter d’information.”

---

## ✅ Question 7

**Régression logistique vs Random Forest**

👉 Régression logistique :

* Simple
* Interprétable
* Rapide
* Adaptée aux relations linéaires

👉 Random Forest :

* Plus performante sur données complexes
* Gère interactions non linéaires
* Moins interprétable

👉 Choix métier :

* Besoin d’explication → régression logistique
* Besoin de performance → Random Forest

💡 Phrase clé :

> “C’est un compromis entre interprétabilité et performance.”

---

## ✅ Question 8

**ROC & AUC**


* **ROC** = courbe qui montre la performance d’un modèle de classification
* **AUC** = aire sous cette courbe → mesure globale de performance


### 💡 Explication simple

La courbe ROC représente le compromis entre :

* **TPR (True Positive Rate)** → taux de vrais positifs (rappel)
* **FPR (False Positive Rate)** → taux de faux positifs

👉 On fait varier le **seuil de décision** du modèle
→ et on observe comment les performances changent

La courbe ROC montre la performance du modèle pour différents seuils :

* Axe X : faux positifs
* Axe Y : vrais positifs

👉 AUC :

* 1 = parfait
* 0.5 = aléatoire

👉 Interprétation :

* Plus la courbe est proche du coin supérieur gauche → meilleur modèle

---

### 📈 AUC (Area Under Curve)

👉 C’est la surface sous la courbe ROC

| Valeur | Signification    |
| ------ | ---------------- |
| 1      | Modèle parfait   |
| 0.5    | Modèle aléatoire |
| < 0.5  | Mauvais modèle   |

---

### 💡 Interprétation

* Plus l’AUC est élevée → meilleur modèle
* Une courbe proche du **coin haut gauche** = très bon modèle

---

### 🧠 Exemple

Un modèle avec AUC = 0.9
👉 a 90% de chances de classer correctement un positif vs un négatif

---

### 🎯 Phrase clé (entretien)

> “La ROC montre le compromis entre faux positifs et vrais positifs, et l’AUC mesure la capacité globale du modèle à distinguer les classes.”

---
💡 À dire :

> “L’AUC mesure la capacité du modèle à distinguer les classes.”

---

# 🔹 Question 9

**Comment savoir qu’un modèle surapprend sans regarder le code ?**

Un modèle surapprend lorsqu’il mémorise les données d’entraînement au lieu d’apprendre des patterns généralisables.

Le moyen le plus simple de le détecter est de comparer ses performances sur les données d’entraînement et sur les données de test.

👉 Si le modèle a :

* une très bonne performance sur le train (ex : 95–100%)
* mais une performance nettement plus faible sur le test

alors il est en **surapprentissage (overfitting)**.

Cela signifie qu’il a appris “par cœur” les données, mais qu’il ne sait pas généraliser.

💡 Exemple :
Un modèle qui prédit parfaitement les clients connus mais se trompe sur les nouveaux clients.

🎯 Phrase clé :

> “Un modèle qui surapprend est excellent en entraînement mais mauvais en généralisation.”

---

# 🔹 Question 10

**Comment concevoir un test A/B pour un changement de prix ?**

Un test A/B consiste à comparer deux versions pour mesurer un impact réel.

👉 Étapes :

1. Diviser aléatoirement les utilisateurs en deux groupes :

   * Groupe A (contrôle) → ancien prix
   * Groupe B (test) → nouveau prix

2. Exposer chaque groupe à une seule version

3. Mesurer des indicateurs clés :

   * taux de conversion
   * chiffre d’affaires
   * panier moyen

4. Comparer les résultats avec un test statistique

👉 Objectif :
isoler l’effet du changement de prix et établir une **relation causale**

⚠️ Important :

* randomisation obligatoire
* taille d’échantillon suffisante

🎯 Phrase clé :

> “Un A/B test permet de mesurer l’impact réel d’un changement en isolant une seule variable.”

---

# 🔹 Question 11

**Quelles métriques utiliser pour une classification déséquilibrée ?**

### 🧾 À retenir

* Pourcentage de **prédictions correctes**
* Métrique simple et intuitive

---

### 💡 Définition

L’accuracy mesure la proportion de bonnes prédictions parmi toutes les prédictions :

👉 fraction : Accurancy = nombre de bonnes prédictions sur nombre total de prédictions
---

Dans un dataset déséquilibré, l’accuracy devient trompeuse.

👉 Exemple :
95% classe A → modèle peut faire 95% accuracy sans rien apprendre.

Si ton modèle fait :

* 90 bonnes prédictions sur 100

👉 Accuracy = **90%**

👉 Il faut utiliser des métriques adaptées :

* **Précision** : parmi les prédictions positives, combien sont correctes
* **Rappel** : combien de vrais positifs sont détectés
* **F1-score** : équilibre précision / rappel
* **ROC-AUC** : capacité globale de discrimination
 
---

🎯 Intuition :

* précision → éviter les faux positifs
* rappel → éviter les faux négatifs
  
> “Sur 100 prédictions, combien sont justes ?”


---

### ⚠️ Limite importante

L’accuracy peut être **trompeuse** si les données sont déséquilibrées.

👉 Exemple :

* 95% classe A
* modèle prédit toujours A
  → Accuracy = 95% ❌ mais modèle inutile

---

### ✅ Quand l’utiliser ?

✔ Dataset équilibré
✔ Problèmes simples

---

### ❌ Quand éviter ?

⚠️ Classification déséquilibrée
⚠️ Cas critiques (fraude, médical…)

---
🎯 Phrase clé :

> “Quand les classes sont déséquilibrées, il faut regarder la qualité des erreurs, pas seulement le taux de bonnes réponses.”

---

# 🔹 Question 12

**Comment gérer la dérive des données (data drift) après déploiement ?**

La dérive des données correspond au fait que les données évoluent dans le temps, ce qui peut dégrader les performances du modèle.

👉 Pour la gérer :

1. **Surveiller les performances**

   * précision
   * erreurs

2. **Analyser les distributions**

   * comparer données actuelles vs données d’entraînement

3. **Mettre en place des alertes**

   * seuil de performance

4. **Réentraîner le modèle**

   * avec des données récentes

🎯 Exemple :
Un modèle de fraude devient moins efficace car les comportements évoluent.

🎯 Phrase clé :

> “Un modèle en production doit être surveillé et mis à jour régulièrement.”

---

# 🔹 Question 13

**Différence entre pipeline batch et inférence temps réel**

👉 Pipeline batch :

* traitement par lots
* exécuté à intervalles réguliers (ex : chaque nuit)
* adapté aux gros volumes

👉 Inférence temps réel :

* réponse immédiate
* utilisée dans des systèmes interactifs

💡 Exemples :

* Batch → calcul des scores clients la nuit
* Temps réel → recommandation produit instantanée

🎯 Phrase clé :

> “Le batch analyse, le temps réel agit.”

---

# 🔹 Question 14

**Comment expliquer un gain de 10% de précision à un dirigeant non technique ?**

Un dirigeant ne s’intéresse pas à la précision, mais à l’impact business.

👉 Il faut traduire le gain technique en valeur concrète :

* +10% précision
  → -10% erreurs
  → moins de pertes / plus de ventes

💡 Exemple :

* moins de fraude non détectée
* meilleures recommandations → + revenus

🎯 Important :
parler en :

* euros
* performance métier
* impact client

🎯 Phrase clé :

> “Un gain technique n’a de valeur que s’il est traduit en impact business.”

---

# 🔹 Question 15

**Qu’est-ce que la PCA et pourquoi l’utiliser ?**

La PCA (Analyse en Composantes Principales) est une méthode de réduction de dimension.

👉 Elle transforme les variables initiales en nouvelles variables :

* indépendantes
* appelées composantes principales

👉 Objectif :

* réduire le nombre de variables
* conserver un maximum d’information (variance)

👉 Pourquoi l’utiliser :

* simplifier les données
* réduire le bruit
* accélérer les modèles
* faciliter la visualisation

🎯 Phrase clé :

> “La PCA compresse l’information tout en conservant l’essentiel.”

---

# 🔹 Question 16

**Différence entre supervisé et non supervisé**

👉 Apprentissage supervisé :

* données avec labels
* objectif : prédire une cible

👉 Apprentissage non supervisé :

* données sans labels
* objectif : découvrir des structures

💡 Exemples :

* supervisé → classification spam
* non supervisé → clustering clients

🎯 Phrase clé :

> “Le supervisé apprend à prédire, le non supervisé apprend à comprendre.”

---

# 🔹 Question 17

**Fonctionnement de K-Means**

K-Means est un algorithme de clustering.

👉 Fonctionnement :

1. Choisir K centres initiaux
2. Associer chaque point au centre le plus proche
3. Recalculer les centres
4. Répéter jusqu’à stabilisation

👉 Objectif :
minimiser la distance entre points et centre du cluster

🎯 Intuition :

> “Chaque point rejoint le groupe qui lui ressemble le plus.”

---

# 🔹 Question 18

**Différence entre MLP et CNN**

👉 MLP (Multi-Layer Perceptron) :

* traite des données tabulaires
* pas de notion spatiale

👉 CNN :

* conçu pour images
* détecte motifs (bords, formes)

🎯 Différence clé :

* MLP → données “plates”
* CNN → données structurées (images)

🎯 Phrase clé :

> “Le CNN comprend la structure, le MLP traite des variables.”

---

# 🔹 Question 19

**Qu’est-ce qu’une fonction d’activation et pourquoi indispensable ?**

Une fonction d’activation introduit de la non-linéarité dans un réseau de neurones.

👉 Sans elle :
le modèle serait une simple combinaison linéaire → limité

👉 Avec elle :
le réseau peut apprendre des relations complexes

👉 Exemples :

* ReLU
* Sigmoid
* Softmax

🎯 Phrase clé :

> “Sans fonction d’activation, un réseau de neurones n’est qu’une régression linéaire.”

---

# 🔹 Question 20

**Différence entre TF-IDF et Word Embedding**

👉 TF-IDF :

* basé sur fréquence des mots
* représentation simple
* ne capture pas le sens

👉 Word Embedding :

* vecteurs denses
* capture le contexte et la sémantique

💡 Exemple :

* TF-IDF → “chat” et “chien” = mots différents
* Embedding → mots proches sémantiquement

🎯 Phrase clé :

> “TF-IDF compte les mots, les embeddings comprennent leur sens.”

---

