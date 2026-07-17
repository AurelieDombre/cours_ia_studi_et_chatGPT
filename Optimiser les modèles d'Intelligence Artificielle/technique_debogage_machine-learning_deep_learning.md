# Résumé détaillé et pédagogique – Techniques de débogage pour les modèles de Machine Learning et Deep Learning

Ce cours explique **comment trouver et corriger les bugs dans un modèle d'IA** lorsqu'il produit de mauvais résultats. Contrairement à un programme classique, un modèle d'IA ne plante pas forcément : il continue souvent à fonctionner mais donne des prédictions erronées. 

---

# I. Pourquoi le débogage en IA est-il difficile ?

Dans un logiciel classique :

```text
Erreur -> message d'erreur -> correction
```

Dans l'IA :

```text
Erreur -> baisse de performance -> cause inconnue
```

Les erreurs peuvent venir de :

* données,
* prétraitement,
* architecture du modèle,
* hyperparamètres,
* environnement d'exécution. 

L'IA est aussi **stochastique** :

* initialisation aléatoire,
* batchs différents,
* augmentation de données,
* ordre de lecture variable.

Deux entraînements peuvent produire des résultats légèrement différents. 

---

# II. La règle d'or : raisonner comme un enquêteur

Le cours compare le data scientist à un enquêteur.

Quand un modèle se comporte mal, il faut considérer que :

> Toute la chaîne est suspecte.

On appelle cette chaîne le **pipeline IA** :

```text
Collecte des données
        ↓
Prétraitement
        ↓
Feature Engineering
        ↓
Entraînement
        ↓
Validation
        ↓
Déploiement
        ↓
Inférence
```

Une erreur peut apparaître à n'importe quel niveau. 

---

# III. Le cycle de débogage à connaître par cœur

C'est probablement la partie la plus importante du cours.

Le diagnostic suit toujours le même cycle :

## 1. Observation

On collecte tous les symptômes :

* baisse de précision,
* erreurs étranges,
* catégories mal prédites,
* perte de performance.

---

## 2. Hypothèses

On imagine plusieurs causes possibles.

Exemple :

* problème de données,
* bug dans le prétraitement,
* mauvais hyperparamètre.

---

## 3. Expérimentation

On modifie **une seule chose à la fois**.

C'est essentiel.

Sinon on ne sait pas ce qui a réellement provoqué le changement. 

---

## 4. Analyse

On mesure l'effet de la modification.

---

## 5. Itération

Si le problème persiste :

on recommence le cycle.

---

## 6. Documentation

On conserve l'historique de tous les essais. 

---

# IV. Les trois piliers d'un bon débogage

## A. Isolation

Tester chaque composant séparément.

Exemple :

```text
Données seules
Prétraitement seul
Modèle seul
```

Ainsi on trouve rapidement l'origine du problème. 

---

## B. Reproductibilité

Pouvoir refaire exactement une expérience.

Pour cela :

* fixer les seeds aléatoires,
* figer les versions des bibliothèques,
* conserver les données utilisées. 

---

## C. Traçabilité

Conserver :

* les paramètres,
* les métriques,
* les versions du modèle.

Des outils comme MLflow ou DVC sont souvent utilisés. 

---

# V. Les stratégies de débogage

## 1. Simplification progressive

Quand le système est trop complexe :

on enlève progressivement des éléments.

Exemple :

```text
10 couches
↓
8 couches
↓
6 couches
↓
4 couches
```

Si le bug disparaît à partir de 6 couches :

le problème est probablement lié aux couches supprimées. 

---

## 2. Ablation

L'ablation consiste à retirer :

* une variable,
* une couche,
* un module,

puis observer ce qui se passe.

Exemple :

On supprime la variable "âge".

Si les performances chutent :

→ elle était importante.

Si le bug disparaît :

→ elle était peut-être responsable du problème. 

---

## 3. Comparaison

Comparer :

* version qui fonctionne,
* version qui échoue.

Exemple :

```text
v2.2 : OK
v2.3 : Bug
```

On cherche ce qui a changé entre les deux versions. 

---

## 4. Tests unitaires

Tester chaque brique séparément :

```text
Lecture des données
✓

Encodage
✓

Normalisation
✓

Prédiction
✓
```

Cela permet de détecter les erreurs locales rapidement. 

---

# VI. Débogage des données

Le cours insiste énormément :

> La majorité des problèmes viennent des données.

Avant d'accuser le modèle :

toujours vérifier les données. 

---

## Anomalies de données

Chercher :

* valeurs aberrantes,
* incohérences,
* erreurs de saisie,
* données corrompues.

Outils :

* histogrammes,
* boxplots,
* scatter plots. 

---

## Outlier

Définition :

Observation très éloignée du comportement normal.

Exemple :

```text
Tous les clients : 50 €
Un client : 50 000 €
```

C'est un outlier.

Il peut révéler :

* une erreur,
* un événement exceptionnel,
* un bug. 

---

# VII. Débogage du prétraitement

Le prétraitement est souvent responsable de bugs invisibles.

Exemples :

## Mauvais encodage

```text
Rouge = 1
Bleu = 2
Vert = 3
```

Le modèle croit alors que :

```text
Vert > Bleu > Rouge
```

alors que ce n'est pas vrai.

---

## Data Leakage

Très important pour l'examen.

Le modèle reçoit accidentellement la réponse pendant l'entraînement.

Exemple :

Pour prédire :

```text
Va-t-il acheter ?
```

On lui donne indirectement une variable qui révèle déjà la réponse.

Résultat :

Performances artificiellement excellentes. 

---

## Bugs silencieux

Ce sont les plus dangereux.

Exemples :

* normalisation appliquée deux fois,
* colonne renommée,
* changement de librairie.

Le modèle continue à fonctionner mais devient progressivement mauvais. 

---

# VIII. Déséquilibre de classes

Situation classique :

```text
99 % non-fraude
1 % fraude
```

Le modèle prédit toujours :

```text
Non fraude
```

et semble avoir :

```text
99 % de précision
```

alors qu'il est inutile.

Il faut analyser :

* précision,
* rappel,
* F1-score,
* matrice de confusion. 

---

## Solutions

* sur-échantillonnage,
* sous-échantillonnage,
* SMOTE,
* pondération de la loss. 

---

# IX. Débogage des algorithmes

## Sous-apprentissage (Underfitting)

Le modèle est trop simple.

Symptômes :

```text
Train faible
Validation faible
```

Le modèle ne comprend pas le problème. 

---

### Causes

* modèle trop simple,
* peu de données,
* mauvaises features. 

---

### Solutions

* modèle plus complexe,
* nouvelles variables,
* davantage de données. 

---

# X. Problèmes de convergence

Parfois la fonction de perte (loss) :

* oscille,
* stagne,
* ne diminue plus.

Causes possibles :

* learning rate mal réglé,
* mauvaise initialisation,
* données mal normalisées. 

---

# XI. Débogage des hyperparamètres

Les hyperparamètres influencent directement l'apprentissage.

Exemples :

* learning rate,
* batch size,
* profondeur,
* régularisation. 

---

## Règle essentielle

> Modifier un seul hyperparamètre à la fois. 

Sinon il devient impossible de savoir lequel est responsable de l'amélioration ou de la dégradation.

---

# XII. Débogage Deep Learning

Les réseaux profonds ont des problèmes spécifiques.

---

## A. Gradient Vanishing

Le gradient devient presque nul.

Les premières couches n'apprennent plus.

```text
Gradient ≈ 0
```

Conséquence :

Le réseau cesse d'apprendre correctement.

---

## B. Gradient Explosion

Le gradient devient énorme.

```text
Gradient = très grand
```

Conséquence :

* instabilité,
* divergence,
* loss qui explose.

---

## Solutions

* Batch Normalization,
* bonne initialisation (He, Xavier),
* ReLU ou Leaky ReLU. 

---

## C. Neurone mort

Un neurone renvoie toujours :

```text
0
```

Quelle que soit l'entrée.

Il ne participe plus à l'apprentissage. 

---

# XIII. Architecture trop simple ou trop complexe

## Réseau trop simple

```text
Faible apprentissage
```

→ Underfitting.

---

## Réseau trop complexe

```text
Apprend le bruit
```

→ Overfitting.

Le cours rappelle :

> Plus gros ≠ meilleur.

---

# XIV. RNN et Transformers

## RNN

Problème :

Ils oublient les dépendances longues.

---

## Transformers

Problème :

Attention mal répartie.

Exemple :

Le modèle se concentre sur certains mots et ignore les autres. 

---

# XV. Batch Size et Learning Rate

Deux hyperparamètres cruciaux.

## Learning Rate trop élevé

Symptômes :

```text
Loss instable
Oscillations
Divergence
```

---

## Batch trop petit

```text
Apprentissage bruité
```

---

## Batch trop grand

```text
Mauvaise généralisation
```

ou consommation mémoire excessive. 

---

# XVI. Régularisation

But :

Éviter le surapprentissage.

Techniques :

* Dropout,
* Early Stopping,
* L1,
* L2. 

Attention :

Trop de régularisation peut masquer le vrai problème. 

---

# XVII. Transfer Learning

Le modèle réutilise un modèle pré-entraîné.

Problème classique :

## Catastrophic Forgetting

Le modèle oublie ce qu'il savait avant.

Exemple :

BERT entraîné sur du texte général devient spécialiste du médical et perd ses connaissances générales. 

---

# Les notions indispensables à connaître

| Notion                  | Définition                                                    |
| ----------------------- | ------------------------------------------------------------- |
| Pipeline IA             | Chaîne complète de traitement.                                |
| Débogage stochastique   | Débogage soumis à l'aléatoire de l'apprentissage.             |
| Ablation                | Retrait progressif d'éléments pour trouver la cause d'un bug. |
| Outlier                 | Valeur extrême anormale.                                      |
| Data Leakage            | Fuite d'information de la cible dans les données.             |
| Underfitting            | Modèle trop simple.                                           |
| Gradient Vanishing      | Gradient qui devient nul.                                     |
| Gradient Explosion      | Gradient qui devient énorme.                                  |
| Neurone mort            | Neurone renvoyant toujours la même valeur.                    |
| Warm-up                 | Augmentation progressive du learning rate.                    |
| Catastrophic Forgetting | Oubli des connaissances pré-entraînées.                       |

---

# La méthode à retenir pour l'examen

Mémorise cette check-list :

1. **Observer les symptômes.**
2. **Formuler plusieurs hypothèses.**
3. **Modifier une seule chose à la fois.**
4. **Tester chaque composant séparément.**
5. **Vérifier les données avant le modèle.**
6. **Contrôler le prétraitement et le data leakage.**
7. **Analyser underfitting, convergence et hyperparamètres.**
8. **Pour le Deep Learning : surveiller gradients, batch size, learning rate et régularisation.**
9. **Documenter tous les essais.**

💡 Pour l'examen, les notions les plus souvent demandées sont : **pipeline IA, cycle de débogage, ablation, outlier, data leakage, déséquilibre de classes, underfitting, gradient vanishing/explosion et catastrophic forgetting**. Ce sont les concepts centraux du cours.



