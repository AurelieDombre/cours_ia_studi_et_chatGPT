


---

# Fiche de révision – IA : Explicabilité, Débogage et Optimisation

---

# 1. SHAP et LIME

## Pourquoi utiliser SHAP et LIME ?

Les modèles d'IA, notamment les réseaux de neurones, sont souvent appelés des **boîtes noires** (*Black Box*).

Ils donnent une prédiction, mais il est difficile de comprendre **pourquoi** ils ont pris cette décision.

Exemple :

Un modèle refuse un prêt bancaire.

Il indique seulement :

```text
Refus du prêt
```

Mais il ne précise pas si cette décision est due :

* au salaire,
* à l'âge,
* aux revenus,
* aux dettes,
* ou à un autre critère.

SHAP et LIME servent à **expliquer les décisions du modèle**.

---

## LIME (Local Interpretable Model-agnostic Explanations)

### Définition

LIME explique **une seule prédiction**.

Il cherche à répondre à la question :

> Pourquoi le modèle a-t-il pris cette décision pour cet individu précis ?

### Fonctionnement

1. On choisit une observation.
2. LIME crée plusieurs versions légèrement modifiées de cette observation.
3. Il observe comment les prédictions changent.
4. Il construit un modèle simple (souvent linéaire) pour expliquer la décision.

### Exemple

Une banque refuse un prêt.

LIME indique :

* Revenus faibles : **-30 %**
* Dettes importantes : **-45 %**
* Ancienneté élevée : **+15 %**

On comprend alors pourquoi le prêt a été refusé.

### Avantages

* Rapide.
* Facile à comprendre.
* Fonctionne avec presque tous les modèles.

### Inconvénients

* Explique uniquement un cas.
* Deux explications proches peuvent être différentes.

---

## SHAP (SHapley Additive exPlanations)

### Définition

SHAP mesure la contribution de chaque variable à la prédiction en utilisant la théorie des jeux.

Il répond à la question :

> Quelle est la part de responsabilité de chaque variable dans la décision ?

### Fonctionnement

SHAP imagine que chaque variable est un joueur d'une équipe.

Chaque joueur participe au résultat final.

SHAP calcule précisément la contribution de chacun.

### Exemple

Prédiction : risque de maladie = 80 %

SHAP indique :

| Variable     | Contribution |
| ------------ | -----------: |
| Âge          |        +25 % |
| Tabac        |        +30 % |
| Cholestérol  |        +20 % |
| Sport        |        -10 % |
| Alimentation |        +15 % |

On comprend précisément pourquoi le risque est élevé.

### Avantages

* Explications très fiables.
* Explications locales et globales.
* Basé sur une méthode mathématique solide.

### Inconvénients

* Plus lent.
* Plus coûteux en calcul.

---

## Différence entre SHAP et LIME

| LIME                           | SHAP                                                   |
| ------------------------------ | ------------------------------------------------------ |
| Explique une prédiction locale | Explique une prédiction locale et l'ensemble du modèle |
| Rapide                         | Plus lent                                              |
| Approximation                  | Théorie des jeux (valeurs de Shapley)                  |
| Plus simple                    | Plus précis                                            |

---

# 2. Débogage des modèles d'IA

## Pourquoi déboguer un modèle ?

Un modèle peut :

* donner de mauvaises prédictions ;
* apprendre très lentement ;
* ne jamais converger ;
* surapprendre.

Le débogage consiste à trouver la cause de ces problèmes.

---

## Le pipeline IA

```text
Données
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
```

Une erreur peut apparaître à n'importe quelle étape.

---

## Cycle de débogage

Toujours suivre les mêmes étapes :

1. Observer le problème.
2. Formuler des hypothèses.
3. Modifier une seule chose à la fois.
4. Tester.
5. Analyser les résultats.
6. Documenter les essais.

---

## Data Leakage

### Définition

Le modèle reçoit accidentellement une information qui contient déjà la réponse.

### Exemple

On veut prédire :

```text
Le client remboursera-t-il son prêt ?
```

Mais une variable indique déjà :

```text
Prêt remboursé : Oui
```

Le modèle n'apprend plus à prédire.

Il lit simplement la réponse.

---

## Déséquilibre de classes

Exemple :

```text
99 % chats

1 % chiens
```

Le modèle répond toujours :

```text
Chat
```

Il obtient :

```text
99 % de précision
```

mais il est incapable de reconnaître les chiens.

---

## Solutions

### SMOTE

Crée artificiellement de nouveaux exemples de la classe minoritaire.

➡️ On ajoute des données.

---

### Sous-échantillonnage

On retire une partie des exemples de la classe majoritaire.

➡️ On supprime des données.

---

### Pondération de la loss

On pénalise davantage les erreurs sur la classe rare.

➡️ Le modèle apprend à y faire plus attention.

---

### Algorithmes spécialisés

Utilisent des modèles capables de mieux gérer les classes déséquilibrées.

Exemple :

* Balanced Random Forest
* XGBoost avec pondération des classes

---

## Underfitting

Le modèle est trop simple.

Il ne comprend pas les données.

Performances faibles partout.

---

## Overfitting

Le modèle mémorise les données d'entraînement.

Il obtient d'excellents résultats sur les données d'entraînement,

mais échoue sur de nouvelles données.

---

# 3. Hyperparamètres

## Paramètres

Ils sont appris automatiquement.

Exemple :

* poids ;
* biais.

---

## Hyperparamètres

Ils sont choisis avant l'entraînement.

Ils contrôlent la façon dont le modèle apprend.

Exemples :

* Learning Rate ;
* Batch Size ;
* nombre de couches ;
* Dropout.

---

# 4. Learning Rate

## Définition

Le Learning Rate détermine **la taille des corrections** appliquées au modèle après chaque erreur.

### Trop grand

Le modèle dépasse constamment la bonne solution.

La loss oscille.

### Trop petit

Le modèle apprend très lentement.

### Bon Learning Rate

Compromis entre vitesse et stabilité.

---

# 5. Batch Size

Nombre d'exemples utilisés avant de mettre à jour les poids.

### Petit Batch

* meilleure généralisation ;
* apprentissage plus bruité.

### Grand Batch

* apprentissage plus stable ;
* nécessite plus de mémoire.

---

# 6. Méthodes de recherche des hyperparamètres

## Grid Search

Teste toutes les combinaisons possibles.

✔ Très fiable.

❌ Très lent.

---

## Random Search

Teste uniquement quelques combinaisons au hasard.

✔ Beaucoup plus rapide.

❌ Peut manquer la meilleure solution.

---

## Optimisation bayésienne (TPE)

Apprend des essais précédents.

Teste principalement autour des meilleures configurations.

✔ Très efficace.

---

## Hyperband

Entraîne beaucoup de modèles pendant quelques époques.

Supprime rapidement les moins bons.

Continue uniquement avec les meilleurs.

✔ Énorme gain de temps.

---

# 7. Techniques de régularisation

## L1 (Lasso)

Supprime automatiquement les variables peu importantes.

Les poids deviennent :

```text
0
```

➡️ Sélection automatique de variables.

---

## L2 (Weight Decay)

Réduit les poids sans les supprimer.

➡️ Limite le surapprentissage.

---

## Différence L1 / L2

| L1                     | L2                            |
| ---------------------- | ----------------------------- |
| Met certains poids à 0 | Réduit tous les poids         |
| Supprime des variables | Conserve toutes les variables |

---

## Dropout

Pendant l'entraînement, certains neurones sont désactivés aléatoirement.

Objectif :

Éviter que le réseau ne devienne trop dépendant de quelques neurones.

➡️ Réduit le surapprentissage.

---

## Early Stopping

On surveille les performances sur le jeu de validation.

Dès qu'elles cessent de s'améliorer,

on arrête l'entraînement.

➡️ Évite que le modèle ne commence à mémoriser les données.

---

## Data Augmentation

Crée artificiellement de nouvelles données.

Exemple :

Une image peut être :

* tournée ;
* agrandie ;
* éclaircie.

➡️ Le modèle apprend sur davantage d'exemples.

---

## Batch Normalization

Normalise les activations entre les couches.

Résultat :

* apprentissage plus rapide ;
* entraînement plus stable ;
* meilleure convergence.

---

# 8. Concepts importants à connaître

| Notion                  | Définition                                                                 |
| ----------------------- | -------------------------------------------------------------------------- |
| **Pipeline IA**         | Ensemble des étapes d'un projet IA, des données au déploiement.            |
| **Black Box**           | Modèle dont les décisions sont difficiles à expliquer.                     |
| **LIME**                | Explique une prédiction locale en créant des exemples proches.             |
| **SHAP**                | Calcule la contribution de chaque variable à une prédiction.               |
| **Data Leakage**        | Fuite d'informations de la cible vers les données d'entrée.                |
| **SMOTE**               | Génère artificiellement de nouveaux exemples de la classe minoritaire.     |
| **Underfitting**        | Modèle trop simple qui n'apprend pas correctement.                         |
| **Overfitting**         | Modèle qui mémorise les données d'entraînement et généralise mal.          |
| **Learning Rate**       | Taille des corrections appliquées aux poids après chaque erreur.           |
| **Batch Size**          | Nombre d'exemples traités avant une mise à jour des poids.                 |
| **Grid Search**         | Teste toutes les combinaisons d'hyperparamètres.                           |
| **Random Search**       | Teste un sous-ensemble de combinaisons choisies au hasard.                 |
| **TPE**                 | Recherche intelligente des hyperparamètres à partir des essais précédents. |
| **Hyperband**           | Élimine rapidement les configurations peu prometteuses.                    |
| **L1**                  | Régularisation qui met certains poids à zéro.                              |
| **L2**                  | Régularisation qui réduit les poids.                                       |
| **Dropout**             | Désactive temporairement des neurones pendant l'entraînement.              |
| **Early Stopping**      | Arrête l'entraînement lorsque la validation ne s'améliore plus.            |
| **Data Augmentation**   | Crée artificiellement de nouvelles données.                                |
| **Batch Normalization** | Stabilise et accélère l'entraînement.                                      |

---

# ⭐ Les notions à connaître absolument pour l'examen

Si tu manques de temps, concentre-toi sur ces notions :

* ✔ Différence entre **paramètres** et **hyperparamètres**.
* ✔ Savoir expliquer **Learning Rate** et **Batch Size** avec un exemple.
* ✔ Connaître les différences entre **Grid Search**, **Random Search**, **TPE** et **Hyperband**.
* ✔ Comprendre **L1**, **L2**, **Dropout**, **Early Stopping** et **Data Augmentation**.
* ✔ Savoir distinguer **Underfitting** et **Overfitting**.
* ✔ Comprendre le **Data Leakage** et le **déséquilibre de classes** (SMOTE, sous-échantillonnage, pondération de la loss).
* ✔ Être capable d'expliquer simplement **LIME** et **SHAP**, leurs rôles et leurs différences.

💡 **Mon conseil pour tes révisions** : tu n'as pas besoin de retenir les formules mathématiques. En revanche, tu dois être capable de répondre à ces trois questions pour chaque notion :

1. **À quoi sert-elle ?**
2. **Comment fonctionne-t-elle ?**
3. **Dans quel cas l'utiliser ?**

Si tu sais répondre à ces trois questions avec un exemple simple, tu maîtriseras très bien les concepts abordés dans ces exercices.



À l'examen, si ton professeur te demande **"Expliquez le Dropout"**, il ne veut généralement pas une définition récitée par cœur. Il veut vérifier que tu as compris. Je répondrais donc toujours selon ce schéma :

> **1. À quoi ça sert ?** → l'objectif de la technique.
> **2. Comment ça fonctionne ?** → le principe.
> **3. Quand l'utiliser ?** → dans quelles situations.
> **4. Exemple concret** → pour montrer que tu as compris.

Je vais te montrer pour toutes les notions importantes.

---

# 1. Learning Rate

## À quoi sert-il ?

Le Learning Rate sert à **définir la vitesse à laquelle le modèle apprend**.

Il contrôle la taille des corrections apportées aux poids après chaque erreur.

---

## Comment fonctionne-t-il ?

Après chaque prédiction, le modèle calcule son erreur.

Ensuite, il modifie ses poids.

Le Learning Rate décide de l'importance de cette modification.

* grand LR → grosses corrections
* petit LR → petites corrections

---

## Quand l'utiliser ?

Toujours.

Tous les modèles entraînés avec la descente de gradient utilisent un Learning Rate.

On le règle lorsque :

* le modèle apprend trop lentement ;
* la loss ne diminue pas ;
* la loss oscille.

---

## Exemple

Imagine que tu apprends à lancer une balle dans un panier.

Si tu corriges énormément ton lancer à chaque essai, tu risques de lancer trop loin, puis trop près.

Si tu corriges très peu, tu progresseras très lentement.

Le Learning Rate correspond à **l'importance des corrections**.

---

# 2. Batch Size

## À quoi sert-il ?

Le Batch Size sert à définir **combien d'exemples sont utilisés avant de mettre à jour les poids du modèle**.

---

## Comment fonctionne-t-il ?

Le modèle ne regarde pas forcément toutes les données d'un coup.

Il les découpe en petits groupes appelés **batchs**.

Après chaque batch :

* il calcule la loss ;
* il met à jour les poids.

---

## Quand l'utiliser ?

Toujours.

Il faut choisir une valeur adaptée :

* petit batch → meilleure généralisation ;
* grand batch → entraînement plus stable.

---

## Exemple

Tu corriges 200 copies.

Tu peux :

* corriger les 200 avant de modifier ton barème ;
* ou corriger seulement 20 copies puis ajuster ton barème.

Le Batch Size correspond au nombre de copies corrigées avant de changer ta manière de noter.

---

# 3. Grid Search

## À quoi sert-il ?

À trouver les meilleurs hyperparamètres.

---

## Comment fonctionne-t-il ?

Il teste **toutes les combinaisons possibles**.

---

## Quand l'utiliser ?

Lorsque le nombre d'hyperparamètres est faible.

---

## Exemple

Tu cherches la meilleure recette de gâteau.

Tu testes :

* farine A ou B ;
* cuisson 20 ou 30 min ;
* sucre 50 ou 100 g.

Tu cuisines toutes les recettes possibles.

---

# 4. Random Search

## À quoi sert-il ?

Trouver rapidement de bons hyperparamètres.

---

## Comment fonctionne-t-il ?

Il choisit des combinaisons **au hasard**.

Il ne teste pas tout.

---

## Quand l'utiliser ?

Quand il y a énormément de combinaisons possibles.

---

## Exemple

Tu cherches un appartement.

Au lieu d'en visiter 500,

tu en visites seulement 30 choisis au hasard.

Tu peux quand même trouver un excellent appartement.

---

# 5. Optimisation bayésienne (TPE)

## À quoi sert-elle ?

Trouver les meilleurs hyperparamètres avec moins d'essais.

---

## Comment fonctionne-t-elle ?

Elle apprend des essais précédents.

Elle teste davantage autour des bonnes solutions.

---

## Quand l'utiliser ?

Lorsque l'entraînement est long ou coûteux.

---

## Exemple

Tu cherches un trésor.

Tu trouves quelques pièces d'or dans une zone.

Au lieu de repartir ailleurs,

tu continues à creuser autour.

---

# 6. Hyperband

## À quoi sert-il ?

Éviter de perdre du temps sur de mauvais modèles.

---

## Comment fonctionne-t-il ?

Tous les modèles commencent l'entraînement.

Les moins performants sont rapidement éliminés.

Seuls les meilleurs continuent.

---

## Quand l'utiliser ?

Quand chaque entraînement est très long.

---

## Exemple

Comme un tournoi de football.

Toutes les équipes commencent.

Les perdantes sont éliminées.

Seules les meilleures atteignent la finale.

---

# 7. L1

## À quoi sert-elle ?

Simplifier le modèle.

Supprimer les variables peu utiles.

---

## Comment fonctionne-t-elle ?

Elle ajoute une pénalité.

Les poids inutiles deviennent progressivement égaux à zéro.

---

## Quand l'utiliser ?

Lorsque certaines variables sont inutiles.

---

## Exemple

Tu prédis le prix d'une maison.

La couleur des volets n'a presque aucune importance.

L1 la supprime automatiquement.

---

# 8. L2

## À quoi sert-elle ?

Limiter le surapprentissage.

---

## Comment fonctionne-t-elle ?

Elle réduit la valeur des poids.

Toutes les variables restent présentes,

mais elles influencent moins les décisions.

---

## Quand l'utiliser ?

Quand le modèle est trop complexe.

---

## Exemple

Dans une réunion,

une personne monopolise la parole.

L2 lui demande de parler moins,

sans la faire sortir de la réunion.

---

# 9. Dropout

## À quoi sert-il ?

Empêcher le réseau de mémoriser les données.

---

## Comment fonctionne-t-il ?

Pendant l'entraînement,

on désactive aléatoirement certains neurones.

Les autres doivent continuer à apprendre sans eux.

---

## Quand l'utiliser ?

Principalement avec les réseaux de neurones profonds.

---

## Exemple

Une équipe de football joue parfois sans certains titulaires.

Les remplaçants apprennent à jouer.

Ainsi, l'équipe ne dépend plus uniquement des meilleurs joueurs.

---

# 10. Early Stopping

## À quoi sert-il ?

Empêcher le surapprentissage.

---

## Comment fonctionne-t-il ?

On surveille les performances sur les données de validation.

Quand elles cessent de s'améliorer,

on arrête l'entraînement.

---

## Quand l'utiliser ?

Quand on constate que le modèle commence à mémoriser les données.

---

## Exemple

Tu révises un examen.

Au début, tes résultats progressent.

Puis tu commences à être fatigué et tu retiens moins bien.

Tu décides d'arrêter de réviser.

---

# 11. Data Augmentation

## À quoi sert-elle ?

Augmenter artificiellement le nombre de données.

---

## Comment fonctionne-t-elle ?

On crée de nouvelles données à partir des données existantes.

Par exemple :

* rotation d'image ;
* changement de luminosité ;
* zoom.

---

## Quand l'utiliser ?

Quand on possède peu de données.

---

## Exemple

Tu n'as que 100 photos de chiens.

Tu les retournes, les fais pivoter ou modifies leur luminosité.

Tu obtiens plusieurs centaines d'images différentes sans reprendre de nouvelles photos.

---

# 12. Batch Normalization

## À quoi sert-elle ?

Rendre l'entraînement plus rapide et plus stable.

---

## Comment fonctionne-t-elle ?

Elle normalise les valeurs produites par une couche avant de les transmettre à la suivante.

Ainsi, les données restent dans une plage de valeurs cohérente et le réseau apprend plus facilement.

---

## Quand l'utiliser ?

Dans les réseaux de neurones profonds pour accélérer l'apprentissage et améliorer la stabilité.

---

## Exemple

Imagine une classe où certains élèves parlent très fort et d'autres très doucement.

Le professeur demande à tout le monde de parler avec le même volume.

La communication devient plus fluide.

La Batch Normalization fait la même chose avec les valeurs qui circulent dans le réseau.

---

# ⭐ La méthode qui impressionne en examen

Pour **n'importe quelle notion**, tu peux répondre avec cette structure :

> **Définition :** ce que c'est.

> **Rôle :** pourquoi on l'utilise.

> **Fonctionnement :** comment elle agit sur le modèle.

> **Quand l'utiliser :** dans quelles situations.

> **Exemple :** un cas concret.

Par exemple, pour **Dropout**, une excellente réponse serait :

> *Le Dropout est une technique de régularisation utilisée pour limiter le surapprentissage dans les réseaux de neurones. Son rôle est d'empêcher le modèle de devenir trop dépendant de certains neurones. Pendant l'entraînement, il désactive aléatoirement une partie des neurones afin que les autres apprennent également à reconnaître les informations importantes. On l'utilise principalement avec les réseaux de neurones profonds lorsqu'on observe de l'overfitting. Par exemple, c'est comme une équipe de football qui s'entraîne parfois sans certains joueurs titulaires : les remplaçants développent aussi leurs compétences, ce qui rend l'équipe plus robuste.*


