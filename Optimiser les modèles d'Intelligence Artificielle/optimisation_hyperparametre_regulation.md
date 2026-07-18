

---

# Résumé détaillé – Optimisation des hyperparamètres et techniques de généralisation

## Objectif du cours

Lorsque l'on entraîne un modèle d'IA, il ne suffit pas de choisir un algorithme.

Il faut aussi déterminer **comment le modèle va apprendre**.

Pour cela, on règle des **hyperparamètres**.

Même avec un excellent modèle et de bonnes données, de mauvais hyperparamètres peuvent produire :

* un modèle qui apprend trop lentement ;
* un modèle qui ne converge jamais ;
* un modèle qui mémorise les données (surapprentissage) ;
* un modèle qui apprend mal (sous-apprentissage). 

Le but du cours est donc de répondre à deux questions :

> **Comment trouver les meilleurs hyperparamètres ?**

et

> **Comment éviter que le modèle surapprenne ?**

---

# I. Paramètres et hyperparamètres : quelle différence ?

C'est la première notion à bien comprendre.

## Les paramètres

Les paramètres sont **appris automatiquement** pendant l'entraînement.

Exemple :

Dans un réseau de neurones, les **poids** et les **biais** sont calculés par le modèle.

On ne les choisit pas.

Le modèle les modifie lui-même.

---

## Les hyperparamètres

Les hyperparamètres sont choisis **avant** l'entraînement.

Ils contrôlent **la manière dont le modèle apprend**.

Exemples :

* learning rate (taux d'apprentissage),
* batch size,
* nombre de couches,
* nombre de neurones,
* fonction d'activation,
* taux de dropout.

Le data scientist doit les choisir ou utiliser une méthode pour les optimiser.

---

### Exemple

Imagine que tu apprends à conduire.

Les **paramètres**, c'est ton expérience : elle s'améliore au fil du temps.

Les **hyperparamètres**, ce sont les conditions choisies avant de commencer :

* voiture automatique ou manuelle,
* vitesse autorisée,
* type de route.

Ils influencent ton apprentissage mais ne sont pas appris par toi.

---

## À retenir

> **Paramètres = appris par le modèle.**
>
> **Hyperparamètres = définis avant l'entraînement.**

---

# II. Les principaux hyperparamètres

Le cours distingue plusieurs catégories.

## 1. Le Learning Rate (taux d'apprentissage)

### Définition
Le Learning Rate (LR) est un hyperparamètre qui détermine l'importance des corrections apportées au modèle après chaque erreur.

À chaque fois que le modèle fait une prédiction, il compare :

- la valeur prédite ;
- la valeur réelle.

Il calcule ensuite une erreur (appelée loss) et modifie ses poids pour essayer de faire mieux au tour suivant.

Le Learning Rate décide de combien les poids seront modifiés.

### Comment fonctionne-t-il ?

Imagine que tu cherches la sortie d'un labyrinthe.

À chaque intersection, quelqu'un te dit :

> « Tu vas dans la bonne direction, continue ! »

Tu peux avancer :

par petits pas ;
ou par grands pas.

Le Learning Rate correspond à la taille de ces pas.

### Learning rate trop grand

Imaginons que le point idéal soit ici :    ↘
```
-------------------- X -------------------
                  minimum

```
Si tu avances avec de très grands pas :
```
←----------------------→
```

Tu dépasses constamment le minimum.

Le modèle fait alors :

- une correction trop importante ;
- puis une autre dans l'autre sens ;
- puis encore une autre...

La loss oscille sans jamais diminuer correctement.

Conséquences
- entraînement instable ;
- parfois divergence ;
- le modèle n'apprend pas.

---

### Learning rate trop petit

Cette fois, tu avances avec des pas minuscules.

```
. . . . . . . . . . .
```

Le modèle progresse.

Mais très lentement.

Il faudra parfois plusieurs milliers d'itérations pour obtenir un bon résultat.

***Conséquences***
- apprentissage très long ;
- consommation importante de ressources ;
- risque de rester bloqué dans un minimum local.

### Bon learning rate

***Cas idéal***

On cherche un compromis.

Les pas doivent être :

- suffisamment grands pour apprendre rapidement ;
- suffisamment petits pour rester stables.

---

***Exemple concret***

Tu entraînes un modèle qui reconnaît les chiffres manuscrits.

**LR = 1**

Après chaque erreur,

le modèle change complètement ses poids.

Résultat :

Accuracy

60 %

35 %

70 %

42 %

58 %

Les performances montent et descendent.

**LR = 0,000001**
60 %

60,2 %

60,3 %

60,5 %

Le modèle apprend...

mais presque pas.

**LR = 0,001**
60 %

68 %

79 %

90 %

96 %

L'apprentissage devient régulier.

Quand modifier le Learning Rate ?

Si :

la loss oscille fortement ;
le modèle ne converge pas ;

➡️ on diminue souvent le Learning Rate.

Si :

l'apprentissage est extrêmement lent ;

➡️ on peut l'augmenter légèrement.

Avantages

✔ contrôle directement la vitesse d'apprentissage

✔ très influent sur les performances

Inconvénients

❌ difficile à choisir

❌ une mauvaise valeur peut empêcher complètement l'apprentissage

À retenir

Le Learning Rate détermine la taille des corrections effectuées par le modèle après chaque erreur.

---

## 2. Le Batch Size

Le batch size représente **le nombre d'exemples utilisés avant une mise à jour des poids**.

Exemple :

Tu as 10 000 images.

Batch size = 100

Le modèle regarde 100 images,

calcule les erreurs,

puis met à jour ses poids.

Il recommence ensuite avec les 100 suivantes.

***Cas 1 : Batch Size = 10 000***

Le modèle regarde :

Image 1

Image 2

...

Image 10 000

Puis seulement après :

il modifie ses poids.

Il effectue donc une seule mise à jour.

***Cas 2 : Batch Size = 100***

Le modèle fait :

100 images

↓

Mise à jour

↓

100 images

↓

Mise à jour

↓

...

Les poids sont modifiés beaucoup plus souvent.

>Pourquoi utiliser des batchs ?
Si on utilisait toutes les données à chaque calcul :
- énormément de mémoire serait nécessaire ;
- l'entraînement serait très lent.

Les batchs permettent donc de découper les données.
---

### Petit batch

Avantages :

* moins de mémoire utilisée ;
* meilleure généralisation.

Inconvénients :

* apprentissage plus bruité ;
* plus lent.

---

### Grand batch

Avantages :

* entraînement plus stable ;
* calcul plus rapide sur GPU.

Inconvénients :

* nécessite plus de mémoire ;
* peut moins bien généraliser.

**Exemple concret**

Imagine que tu corriges :

100 copies d'examen.
Batch = 1

Tu corriges :

1 copie

↓

tu changes ton barème

↓

1 copie

↓

tu rechanges ton barème

Tu modifies constamment ta façon de noter.

Batch = 100

Tu corriges tout.

Puis seulement après,

tu modifies ton barème.

Les corrections sont beaucoup plus stables.

>À retenir
Le Batch Size répond à la question :
Combien d'exemples vais-je regarder avant de corriger mon modèle ?

---


## 3. Les hyperparamètres architecturaux

Ils définissent la structure du réseau.

Exemples :

* nombre de couches ;
* nombre de neurones ;
* fonction d'activation ;
* nombre de têtes d'attention (Transformers).

Plus le réseau est complexe,

plus il peut apprendre des relations difficiles...

mais plus le risque de surapprentissage augmente.

---


# III. Comment trouver les meilleurs hyperparamètres ?

Impossible de tout tester.

Imagine :

* 5 learning rates,
* 4 batch sizes,
* 6 valeurs de dropout,
* 5 valeurs de L2.

Cela donne :

```
5 × 4 × 6 × 5

=

600 essais
```

Et ce n'est qu'avec **4 hyperparamètres** !

On parle d'**explosion combinatoire**. 

---

# IV. Les méthodes d'optimisation

### Grid search

***Définition***

Le Grid Search est une méthode qui permet de trouver les meilleurs hyperparamètres.

Son principe est très simple :

Tester toutes les combinaisons possibles.

***Pourquoi en a-t-on besoin ?***

Supposons que tu ne connaisses pas les meilleurs paramètres.

Tu hésites entre :

Learning Rate
0.1

0.01

0.001
Batch Size
16

32

64

Tu ne sais pas quelle combinaison est la meilleure.

Le Grid Search va toutes les essayer.

0.1 +16

0.1 +32

0.1 +64

0.01 +16

0.01 +32

...

0.001 +64

À chaque essai :

le modèle est entraîné ;
les performances sont mesurées.

À la fin,

on garde la meilleure combinaison.

**Exemple concret**

Imagine que tu veux préparer un gâteau.

Tu ne connais pas la meilleure recette.

Tu testes :

farine A ou B ;
cuisson 20 ou 30 minutes ;
sucre 50 ou 100 g.

Le Grid Search cuisine toutes les recettes possibles.

Ensuite il garde la meilleure.

***Avantages***

✔ simple

✔ garantit qu'aucune combinaison n'est oubliée

***Inconvénients***

Le problème est qu'il devient vite énorme.

Imaginons :

Learning Rate

10 valeurs

Batch

10 valeurs

Dropout

10 valeurs

L2

10 valeurs

Le nombre d'essais devient :

10 ×10 ×10 ×10

=

10 000 entraînements

Or un seul entraînement peut durer plusieurs heures.

Le Grid Search devient donc rapidement inutilisable sur de gros modèles.

*** Quand l'utiliser ?***

✔ Peu d'hyperparamètres.

✔ Petit espace de recherche.

>À retenir
Le Grid Search est la méthode la plus exhaustive :
Il teste absolument toutes les combinaisons possibles, mais cela peut coûter énormément de temps de calcul.


---

## 2. Random Search

Le Random Search est une méthode d'optimisation des hyperparamètres qui consiste à tester des combinaisons choisies au hasard.
Contrairement au Grid Search, il ne teste pas toutes les possibilités.

Il en choisit seulement quelques-unes, de manière aléatoire.

***Pourquoi a-t-il été créé ?
Imaginons que tu veuilles régler :

| Hyperparamètre | Nombre de valeurs |
| -------------- | ----------------- |
| Learning Rate  | 10                |
| Batch Size     | 10                |
| Dropout        | 10                |
| L2             | 10                |

Le Grid Search devrait tester :
```
10 × 10 × 10 × 10

= 10 000 entraînements
```

Si un entraînement dure 30 minutes :
```
10 000 × 30 min

= 300 000 minutes

≈ 208 jours !
```
C'est beaucoup trop long.

Le Random Search propose donc une idée simple :

>Ne testons qu'une partie des combinaisons.

***Comment fonctionne-t-il ?***

Supposons que tu aies 10 000 combinaisons possibles.

Le Random Search peut décider d'en tester seulement :

100

ou

200

prises complètement au hasard.

Par exemple :
| Essai | Learning Rate | Batch | Dropout |
| ----- | ------------- | ----- | ------- |
| 1     | 0.01          | 32    | 0.2     |
| 2     | 0.0005        | 64    | 0.4     |
| 3     | 0.005         | 16    | 0.1     |


Chaque combinaison est entraînée puis évaluée.

À la fin, on garde la meilleure.

***Pourquoi cela fonctionne ?***

Tous les hyperparamètres n'ont pas la même importance.

Par exemple :

Imaginons :

le Learning Rate influence énormément les performances ;
le Batch Size influence peu.

Le Grid Search va perdre énormément de temps à tester toutes les valeurs de Batch Size.

Le Random Search, lui, explore davantage de valeurs de Learning Rate.

Il découvre souvent une bonne solution beaucoup plus rapidement.

**Exemple concret**

Imagine que tu cherches un restaurant dans une ville.

***Grid Search***

Tu décides de visiter tous les restaurants.

Tu finiras forcément par trouver le meilleur.

Mais cela prendra énormément de temps.

***Random Search***

Tu en visites seulement une vingtaine.

Tu as de très bonnes chances de trouver un excellent restaurant,

sans devoir tous les essayer.

***Avantages***

✅ beaucoup plus rapide que Grid Search

✅ très efficace quand il y a beaucoup d'hyperparamètres

✅ simple à mettre en œuvre

***Inconvénients***

❌ il ne garantit pas de trouver LA meilleure combinaison.

Il peut passer à côté.

***Quand l'utiliser ?***

✔ Beaucoup d'hyperparamètres

✔ Peu de temps de calcul

✔ Première recherche rapide

>À retenir
Random Search = tester seulement quelques combinaisons au hasard pour gagner énormément de temps.

---

## 3. Optimisation bayésienne (TPE)

L'optimisation bayésienne (comme TPE : Tree-structured Parzen Estimator) est une méthode beaucoup plus intelligente.

Contrairement au Random Search :

Elle apprend de ses essais précédents.

Elle devient de plus en plus efficace.

***Pourquoi utiliser cette méthode ?***

Imaginons que tu cherches un trésor.

Le Random Search fait ceci :

Creuser ici

Creuser là

Creuser encore ailleurs

Complètement au hasard.

Le TPE fait autre chose.

Après chaque essai,

il se demande :

  >Où ai-je eu les meilleurs résultats ?

Puis il continue à chercher autour de ces endroits.

***Comment fonctionne-t-il ?***

Premier essai :

- Learning Rate = 0.1

- Accuracy = 72 %

Deuxième :

- Learning Rate = 0.001

- Accuracy = 95 %

Le TPE comprend immédiatement que :

0.001

↓

Très intéressant

Les prochains essais seront donc :

0.0008

0.0011

0.0015

0.0009

Il concentre ses recherches autour des bonnes solutions.

***Exemple concret***

Imagine que tu cherches une station de ski.

Tu visites une première station.

Elle est moyenne.

Tu en visites une deuxième.

Elle est excellente.

***Que fais-tu ?***

Tu explores les stations voisines.

C'est exactement le principe du TPE.

***Avantages***

✅ beaucoup moins d'essais

✅ très performant

✅ apprend au fur et à mesure

Inconvénients

❌ plus compliqué à programmer

❌ nécessite quelques essais avant d'être efficace

***Quand l'utiliser ?***

✔ gros modèles

✔ beaucoup d'hyperparamètres

✔ peu de temps de calcul

>À retenir
Le TPE apprend des essais précédents et concentre ses recherches là où les performances sont les meilleures.

## 4. Algorithmes évolutionnaires

Inspirés de la sélection naturelle.

Chaque configuration est un "individu".

Les meilleures sont conservées,

croisées entre elles,

et légèrement modifiées (mutation).

Au fil des générations,

on obtient des configurations de plus en plus performantes.

Très utiles pour des problèmes complexes. 

---

## 5. Hyperband / Successive Halving

***Définition***
Le problème des méthodes précédentes est simple.
Même si une configuration est mauvaise,
il faut souvent attendre la fin de son entraînement pour le savoir.

Hyperband dit :

>Pourquoi entraîner complètement un mauvais modèle ?

Hyperband propose une idée simple :

1. entraîner beaucoup de modèles pendant quelques époques ;
2. supprimer rapidement les moins bons ;
3. continuer seulement avec les meilleurs.


***Comment fonctionne-t-il ?***

Imaginons :

Tu veux tester :

100 modèles

Chaque modèle doit normalement être entraîné pendant :

100 époques

Cela représente énormément de calcul.

Hyperband procède autrement.

***Étape 1***

Il entraîne tous les modèles seulement :

5 époques

Puis il regarde les résultats.

***Étape 2***

Les 50 moins bons sont supprimés.

***Étape 3***

Les 50 meilleurs continuent.

Puis on recommence.

100 modèles

↓

50

↓

25

↓

10

↓

3

↓

1 meilleur modèle
Pourquoi cette méthode est-elle rapide ?

Les mauvais modèles sont éliminés très tôt.

On ne gaspille donc pas de temps.

***Exemple concret***

Imagine un concours de chant.

Tu ne fais pas chanter chaque candidat pendant une heure.

Tu organises des éliminatoires.

Seuls les meilleurs continuent.

Hyperband fonctionne exactement comme cela.

***Avantages***

✅ énorme gain de temps

✅ très utilisé en Deep Learning

***Inconvénients***

❌ un modèle qui apprend lentement peut être éliminé trop tôt.

>À retenir
Hyperband élimine rapidement les mauvaises configurations afin de consacrer le temps de calcul uniquement aux meilleures.

---

# V. La régularisation : éviter le surapprentissage

Un modèle trop complexe peut **mémoriser** les données d'entraînement.

Il obtient de très bons résultats sur les données d'entraînement,

mais échoue sur de nouvelles données.

La régularisation sert à empêcher ce comportement. 

---

# VI. Les principales techniques de régularisation

## 1. L1 et L2

On ajoute une **pénalité** dans la fonction de coût.

L'objectif est d'éviter que les poids deviennent trop grands.

### L1

Favorise des modèles plus simples en mettant certains poids à zéro.
L1 est une technique de régularisation.

***Son objectif est :***

Simplifier le modèle.

Elle ajoute une pénalité dans la fonction de coût.

Les poids inutiles deviennent progressivement :

0

Le modèle supprime donc automatiquement certaines variables.
Pourquoi faire cela ?

Toutes les variables ne sont pas utiles.

***Exemple :***

Pour prédire le prix d'une maison :
| Variable            | Utile ? |
| ------------------- | ------- |
| Surface             | Oui     |
| Nombre de pièces    | Oui     |
| Quartier            | Oui     |
| Couleur de la porte | Non     |

***L1 va supprimer :***

```
Couleur de la porte

↓

Poids = 0
```

***Exemple concret***

Tu fais une randonnée.

Ton sac contient :

* eau
* nourriture
* carte
* trois paires de chaussures
* une télévision

Tu enlèves tout ce qui est inutile.

Le sac devient plus léger.

L1 fait exactement cela avec les variables.

***Avantages***

✅ modèle plus simple

✅ sélection automatique des variables

***Inconvénients***

❌ peut supprimer une variable qui était légèrement utile.

>À retenir
L1 sert à supprimer les variables peu importantes en mettant leurs poids à zéro.

### L2 (Weight Decay)

L2 est également une régularisation.

Mais contrairement à L1,

elle ne supprime pas les variables.

Elle réduit seulement leur influence.


***Comment fonctionne-t-elle ?***

Imaginons :

```
Avant :

Poids

28

35

42

Après L2 :

14

18

20
```
Les variables restent présentes.

Mais elles influencent moins les décisions.

***Pourquoi est-ce utile ?***

Lorsque certains poids deviennent énormes,

le modèle commence souvent à mémoriser les données.

L2 limite ce phénomène.

***Exemple concret***

Imagine une réunion.

Une seule personne parle tout le temps.

Le responsable demande :

"Tout le monde participe."

Cette personne continue à parler,

mais beaucoup moins.

L2 fait exactement cela avec les poids.

***Avantages***

✅ très efficace contre le surapprentissage

✅ améliore souvent la généralisation

***Inconvénients***

❌ ne réalise pas de sélection de variables.

>À retenir
L2 réduit la taille des poids afin que le modèle reste simple sans supprimer de variables.

---
#### Différence entre L1 et L2

| L1                                    | L2                            |
| ------------------------------------- | ----------------------------- |
| Met certains poids exactement à **0** | Réduit tous les poids         |
| Supprime des variables                | Conserve toutes les variables |
| Simplifie fortement le modèle         | Rend le modèle plus stable    |
| Sélection de variables                | Réduction des poids           |


À retenir :

* L1 = Éliminer → certaines variables disparaissent complètement.
* L2 = Limiter → toutes les variables restent, mais leur influence diminue.

---

## 2. Dropout

Le Dropout est une technique de régularisation qui consiste à désactiver aléatoirement certains neurones pendant l'entraînement.

Autrement dit, à chaque passage des données, une partie des neurones est temporairement "éteinte". Ils ne participent ni au calcul ni à l'apprentissage.

⚠️ Important : le Dropout est uniquement utilisé pendant l'entraînement. Lorsqu'on utilise le modèle pour faire des prédictions (phase de test ou de production), tous les neurones sont réactivés.

***Pourquoi utiliser le Dropout ?***

Imagine un réseau de neurones où certains neurones deviennent très importants.

Les autres neurones comptent tellement sur eux qu'ils n'apprennent presque plus.

Si ces neurones principaux se trompent, tout le réseau se trompe.

On dit que les neurones sont trop dépendants les uns des autres (co-adaptation).

Le Dropout oblige chaque neurone à apprendre à travailler sans pouvoir toujours compter sur les mêmes voisins.

***Comment fonctionne-t-il ?***

Imaginons un réseau très simple.

Sans Dropout :

```
Entrée

↓

● ● ● ● ●

↓

●

```


---

## 3. Early Stopping

On surveille les performances sur le jeu de validation.

Dès qu'elles cessent de s'améliorer,

on arrête l'entraînement.

Cela évite que le modèle continue à mémoriser les données.

---

## 4. Data Augmentation

On crée artificiellement de nouvelles données.

### Exemple en vision

Une photo peut être :

* tournée ;
* agrandie ;
* éclaircie ;
* légèrement bruitée.

### Exemple en NLP

Une phrase peut être :

* reformulée ;
* traduite puis retraduite (back-translation) ;
* enrichie avec des synonymes.

Le modèle voit davantage de situations et généralise mieux. 

---

## 5. Batch Normalization

Les activations sont normalisées entre les couches.

Résultat :

* apprentissage plus stable ;
* convergence plus rapide ;
* réseau plus robuste. 

---

# VII. Le compromis biais-variance

C'est une notion fondamentale.

Deux extrêmes sont à éviter :

## Modèle trop simple

* ne comprend pas les données ;
* mauvaises performances partout.

➡️ **Sous-apprentissage (biais élevé).**

---

## Modèle trop complexe

* apprend même le bruit ;
* excellent sur l'entraînement ;
* mauvais sur de nouvelles données.

➡️ **Surapprentissage (variance élevée).**

L'objectif est de trouver **un équilibre** entre ces deux situations.

---

# VIII. Bonnes pratiques d'optimisation

Le cours recommande une méthode rigoureuse :

1. Définir les objectifs (précision, F1-score, temps d'inférence…).
2. Choisir les hyperparamètres les plus influents.
3. Sélectionner une méthode de recherche adaptée.
4. Prévoir un budget de calcul.
5. Suivre toutes les expériences.
6. Garantir la reproductibilité (seeds, versions des bibliothèques).
7. Utiliser une validation rigoureuse et un jeu de test indépendant.

---

# IX. Outils et industrialisation

Dans un projet professionnel, on ne note pas les essais dans un cahier.

On utilise des outils dédiés :

* **MLflow** : enregistre les hyperparamètres, les métriques et les modèles.
* **Weights & Biases** : suit et compare les expériences.
* **DVC** : versionne les données.

Ces outils permettent de **retrouver, comparer et reproduire** facilement chaque expérience.

---

# X. Les notions indispensables à connaître

| Notion                            | Définition simple                                                                    |
| --------------------------------- | ------------------------------------------------------------------------------------ |
| **Hyperparamètre**                | Réglage choisi avant l'entraînement qui influence la façon d'apprendre.              |
| **Learning Rate**                 | Taille des pas réalisés par le modèle lors de l'apprentissage.                       |
| **Batch Size**                    | Nombre d'exemples utilisés avant de mettre à jour les poids.                         |
| **Grid Search**                   | Teste toutes les combinaisons possibles d'hyperparamètres.                           |
| **Random Search**                 | Teste des combinaisons choisies au hasard.                                           |
| **Optimisation bayésienne (TPE)** | Oriente les nouveaux essais à partir des résultats précédents.                       |
| **Hyperband**                     | Élimine rapidement les configurations peu prometteuses pour économiser du temps.     |
| **L1**                            | Pénalisation qui peut mettre certains poids à zéro (sélection de variables).         |
| **L2 (Weight Decay)**             | Pénalisation qui réduit la taille des poids pour limiter la complexité.              |
| **Dropout**                       | Désactive aléatoirement des neurones pendant l'entraînement.                         |
| **Early Stopping**                | Arrête l'entraînement lorsque la validation ne s'améliore plus.                      |
| **Data Augmentation**             | Crée de nouvelles données artificielles pour améliorer la généralisation.            |
| **Batch Normalization**           | Normalise les activations pour stabiliser et accélérer l'entraînement.               |
| **Compromis biais-variance**      | Équilibre entre un modèle trop simple (underfitting) et trop complexe (overfitting). |

---

# La méthode à retenir pour l'examen

Tu peux mémoriser cette démarche en **6 étapes** :

1. **Identifier les hyperparamètres les plus importants** (learning rate, batch size, architecture).
2. **Choisir une méthode d'optimisation adaptée** (Grid Search, Random Search, TPE, Hyperband…).
3. **Éviter l'explosion combinatoire** en ne testant pas tout.
4. **Appliquer des techniques de régularisation** (L1/L2, Dropout, Early Stopping, Data Augmentation…).
5. **Surveiller les courbes d'apprentissage** pour détecter le surapprentissage ou le sous-apprentissage.
6. **Documenter et rendre les expériences reproductibles** avec des outils comme MLflow, Weights & Biases ou DVC.

## 💡 Astuce pour réviser

Pour bien retenir ce cours, pense à le découper en **trois grandes idées** :

* **Optimiser** : trouver les meilleurs hyperparamètres (Grid Search, Random Search, TPE, Hyperband).
* **Régulariser** : empêcher le modèle de surapprendre (L1/L2, Dropout, Early Stopping, Data Augmentation…).
* **Industrialiser** : rendre les expériences fiables, traçables et reproductibles (MLflow, DVC, validation rigoureuse).

