
---

# Résumé détaillé – Méthodologies de diagnostic des erreurs dans les modèles d'IA

## Objectif du cours

Un modèle d'IA peut très bien fonctionner pendant son entraînement puis commencer à faire des erreurs une fois utilisé en production.

Le but du diagnostic est de répondre à une question simple :

> **Pourquoi mon modèle fait-il des erreurs ?**

L'idée est de **chercher la vraie cause** avant de modifier le modèle.

Le diagnostic évite de perdre du temps à changer des paramètres alors que le problème vient parfois simplement des données. 

---

# I. Les trois grandes familles d'erreurs

Le cours explique que presque toutes les erreurs proviennent de **trois sources principales**.

## 1. Les données

C'est la première chose à vérifier.

Même un excellent algorithme donnera de mauvais résultats avec de mauvaises données.

Les problèmes peuvent être :

### Données manquantes

Certaines informations sont absentes.

Exemple :

Une colonne "âge" contient beaucoup de cellules vides.

Conséquence :

Le modèle apprend avec des informations incomplètes.

Solution :

* imputation (remplir les valeurs)
* suppression raisonnée
* récupération des données

---

### Données bruitées

Ce sont des données fausses ou aberrantes.

Exemple :

Un capteur indique

```
Température = 850°C
```

alors que la machine fonctionne normalement.

Ce n'est pas une donnée manquante.

C'est une donnée erronée.

Solution :

* détecter les valeurs aberrantes
* corriger
* filtrer

À retenir :

> **Donnée manquante = information absente**
>
> **Donnée bruitée = information fausse** 

---

### Données biaisées

Le modèle apprend les injustices présentes dans les données.

Exemple :

Dans un historique de recrutement :

* 90 % des personnes recrutées sont des hommes.

Le modèle peut apprendre :

> Homme = meilleur candidat

alors que c'est faux.

Les performances globales peuvent sembler bonnes, mais certaines catégories sont pénalisées.

Il faut donc vérifier les performances :

* selon le sexe
* selon l'âge
* selon la région
* selon les catégories métiers

On appelle cela **un audit d'équité**. 

---

### Data Drift (dérive de distribution)

Le monde change.

Les données changent.

Mais le modèle, lui, reste entraîné sur les anciennes données.

Exemple :

Pendant le COVID :

les achats en ligne explosent.

Le modèle entraîné avant le COVID continue de recommander les anciens produits.

Résultat :

beaucoup d'erreurs.

Le drift signifie :

> Les données de production ne ressemblent plus aux données d'entraînement.

Solution :

* surveiller les données
* réentraîner régulièrement le modèle. 

---

# 2. Les erreurs de modélisation

Même avec de bonnes données, on peut choisir un mauvais modèle.

Exemple :

On utilise une régression linéaire.

Mais le problème est très complexe.

Le modèle est incapable de comprendre les relations.

À l'inverse :

Utiliser un énorme réseau de neurones sur peu de données provoque souvent du surapprentissage.

Il faut donc toujours vérifier :

> Le modèle est-il adapté au problème ? 

---

# 3. Les erreurs d'implémentation

Le problème peut venir du code.

Exemples :

* bug Python
* erreur dans un script
* mauvais prétraitement
* erreur dans les variables

C'est la dernière chose à vérifier.

---

# II. Les problèmes pendant l'entraînement

Le cours présente plusieurs problèmes très fréquents.

---

## A. Le surapprentissage (Overfitting)

Le modèle apprend presque par cœur les données d'entraînement.

Il devient excellent sur ces données.

Mais dès qu'on lui montre de nouvelles données :

les performances chutent.

Sur les courbes :

* entraînement très bon
* validation mauvaise

C'est le signe classique du surapprentissage. 

---

## B. Le sous-apprentissage (Underfitting)

Cette fois :

le modèle est trop simple.

Il ne comprend pas le phénomène.

Les performances sont mauvaises :

* sur les données d'entraînement
* sur les données de validation

Les deux courbes restent faibles.

Solutions :

* modèle plus complexe
* meilleures variables
* plus de données pertinentes. 

---

## C. Les problèmes de convergence

Pendant l'entraînement :

la fonction de perte (loss)

ne diminue plus

ou devient instable.

Causes :

* taux d'apprentissage trop élevé
* mauvaise initialisation
* architecture mal conçue

Exemple :

Le gradient explose.

Le modèle n'apprend plus. 

---

# III. Les hyperparamètres

Les hyperparamètres contrôlent la façon dont le modèle apprend.

Exemples :

* learning rate
* batch size
* nombre de couches
* profondeur d'un arbre

Erreur classique :

Modifier plusieurs paramètres en même temps.

Le cours recommande :

> **Modifier un seul paramètre à la fois.**

Ainsi on sait exactement quel changement améliore (ou dégrade) le modèle. 

---

# IV. La méthode de diagnostic

Le cours insiste énormément sur une méthode.

Toujours suivre le même ordre.

## Étape 1

Vérifier les données

↓

## Étape 2

Analyser le modèle

↓

## Étape 3

Vérifier les hyperparamètres

↓

## Étape 4

Chercher un bug dans le code

Ne jamais commencer directement par modifier le modèle.

C'est la méthode utilisée dans les entreprises. 

---

# V. Les outliers

Un **outlier** est une observation très différente des autres.

Exemple :

Tous les clients dépensent environ 100 €.

Un client dépense 20 000 €.

Ce cas est un outlier.

Pourquoi sont-ils importants ?

Parce qu'ils révèlent souvent les faiblesses du modèle.

Même s'ils sont rares,

ils permettent de comprendre pourquoi le modèle se trompe. 

---

# VI. Segmenter les erreurs

Regarder uniquement l'erreur moyenne est insuffisant.

Il faut découper les résultats.

Par exemple :

* par âge
* par région
* par produit
* par saison

On découvre parfois que :

Le modèle fonctionne très bien en été,

mais très mal pendant les soldes.

Sans segmentation,

on ne verrait jamais ce problème. 

---

# VII. Les outils de diagnostic

## Les courbes d'apprentissage

Elles permettent de savoir :

* si le modèle apprend correctement
* s'il surapprend
* s'il sous-apprend

---

## La matrice de confusion

Elle montre :

* vrais positifs
* faux positifs
* vrais négatifs
* faux négatifs

Très utile en :

* médecine
* fraude bancaire

Pourquoi ?

Parce que toutes les erreurs n'ont pas le même coût.

Exemple :

Ne pas détecter un cancer est beaucoup plus grave que déclencher une fausse alerte.

On parle de **coût d'erreur asymétrique**. 

---

## Analyse des résidus

Utilisée pour les modèles de régression.

Résidu :

```
Résidu = valeur réelle − valeur prédite
```

Les résidus permettent de détecter :

* un biais
* des variables oubliées
* une mauvaise modélisation

Si les erreurs deviennent très grandes pour les maisons de luxe,

cela signifie que le modèle ne comprend pas ce segment. 

---

## Test d'ablation

Principe :

On enlève une variable.

Puis on regarde si les performances changent.

Si elles chutent fortement,

la variable est importante.

Sinon,

elle est peut-être inutile. 

---

# VIII. Diagnostic selon le type de modèle

Le diagnostic dépend du modèle utilisé.

* **Classification (arbres, SVM, k-NN)** : on étudie les régions de décision et les variables importantes.
* **Régression** : on analyse les résidus.
* **Clustering** : on vérifie la stabilité des groupes (par exemple avec l'indice de silhouette).
* **Deep Learning** :

  * CNN : tester la robustesse aux changements d'images (rotation, éclairage, bruit).
  * RNN/Transformers : analyser les mécanismes d'attention et les dépendances dans les séquences.
  * Réseaux profonds : examiner les embeddings et les activations internes pour comprendre ce que le modèle a réellement appris. 

---

# La méthode à retenir pour l'examen

Tu peux mémoriser cette **check-list en 7 étapes** :

1. **Vérifier les données** (manquantes, bruitées, biaisées, drift).
2. **Vérifier que le modèle est adapté** au problème.
3. **Contrôler les hyperparamètres** (un seul changement à la fois).
4. **Observer les courbes d'apprentissage** (surapprentissage ou sous-apprentissage).
5. **Analyser les erreurs** (matrice de confusion, résidus, outliers).
6. **Segmenter les résultats** (par catégorie, région, saison, etc.).
7. **Contrôler l'implémentation** (prétraitements, scripts, bugs). Cette démarche correspond à la synthèse du cours. 

## Les notions indispensables à connaître

| Notion                   | Définition simple                                                     |
| ------------------------ | --------------------------------------------------------------------- |
| **Data Drift**           | Les données changent entre l'entraînement et la production.           |
| **Données bruitées**     | Données fausses ou aberrantes.                                        |
| **Données manquantes**   | Informations absentes.                                                |
| **Biais**                | Injustice héritée des données historiques.                            |
| **Surapprentissage**     | Le modèle mémorise les données d'entraînement et généralise mal.      |
| **Sous-apprentissage**   | Le modèle est trop simple et n'apprend pas suffisamment.              |
| **Outlier**              | Observation atypique qui révèle souvent une faiblesse du modèle.      |
| **Matrice de confusion** | Tableau qui décrit précisément les types d'erreurs d'un classifieur.  |
| **Résidu**               | Écart entre la valeur réelle et la valeur prédite.                    |
| **Test d'ablation**      | Suppression d'une variable ou d'un composant pour mesurer son impact. |


