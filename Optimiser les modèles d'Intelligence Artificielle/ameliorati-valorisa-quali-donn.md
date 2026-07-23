Oui. Ce cours est beaucoup plus simple qu'il n'y paraît. En réalité, il répond à une seule question :

> **Comment obtenir un jeu de données (dataset) de qualité pour entraîner une intelligence artificielle ?**

Le message principal du cours est le suivant :

> **Une bonne IA dépend davantage de la qualité des données que de la complexité de l'algorithme.** 

Je vais te réexpliquer le cours comme si tu n'avais jamais fait d'IA.

---

# Avant de commencer : comment fonctionne une IA ?

Imagine que tu veuilles apprendre à un enfant à reconnaître un chien.

Tu lui montres 10 000 photos.

Si les photos sont :

* nettes ✅
* correctement étiquetées ("chien", "chat"...)
* variées (petits chiens, gros chiens, noirs, blancs...)

alors l'enfant apprendra correctement.

Maintenant imagine que :

* certaines photos sont floues
* d'autres sont mal étiquetées
* il manque des photos de certaines races
* certaines photos sont vieilles ou incomplètes

L'enfant va apprendre de mauvaises choses.

Pour une IA, c'est exactement pareil.

Les photos représentent ce qu'on appelle un **jeu de données**.

---

# Qu'est-ce qu'un dataset ?

## Définition

Un **dataset** (jeu de données) est un ensemble de données utilisé pour entraîner une intelligence artificielle.

Exemple :

On veut créer une IA qui prédit si un client va acheter une voiture.

Le dataset pourrait être :

| Âge | Salaire | Ville    | Achat |
| --- | ------- | -------- | ----- |
| 25  | 25000   | Paris    | Oui   |
| 54  | 52000   | Lyon     | Non   |
| 39  | 41000   | Toulouse | Oui   |

Chaque ligne représente un client.

Chaque colonne représente une information.

Le but est que l'IA découvre toute seule les relations entre ces informations.

---

# Pourquoi la qualité des données est-elle si importante ?

Imagine que tu cuisines.

Tu peux être le meilleur cuisinier du monde.

Si tes ingrédients sont périmés...

Le plat sera mauvais.

En IA :

* le cuisinier = l'algorithme
* les ingrédients = les données

Donc :

> **Mauvaises données = mauvaise IA**

C'est l'idée centrale de tout le cours. 

---

# Les 6 dimensions de la qualité des données

Le cours explique qu'un dataset est de qualité seulement s'il respecte **6 critères**. 

Je vais les détailler.

---

# 1. La complétude

## Définition

La complétude signifie :

> Les informations importantes sont présentes. Il n'y a pas de valeurs manquantes sur les variables essentielles. 

Exemple :

| Nom   | Âge | Salaire |
| ----- | --- | ------- |
| Paul  | 25  | 25000   |
| Julie |     | 32000   |
| Lucas | 40  |         |

Ici :

* Julie n'a pas d'âge.
* Lucas n'a pas de salaire.

Le dataset est incomplet.

### Pourquoi est-ce un problème ?

L'IA ne sait plus quoi apprendre.

Elle doit soit :

* deviner
* supprimer la ligne
* remplacer les valeurs

---

### À retenir

Complétude = **pas de données importantes manquantes**.

Attention : un dataset peut être complet mais rester de mauvaise qualité s'il est biaisé ou incorrect. 

---

# 2. L'exactitude

## Définition

L'exactitude signifie :

> Les données correspondent à la réalité.

Exemple :

Si une personne mesure :

1,75 m

mais que la base indique :

17,5 m

La donnée est fausse.

Autre exemple :

Un patient est enregistré comme ayant 250 ans.

Impossible.

L'information est incorrecte.

---

### À retenir

Exactitude = **les données sont vraies**.

---

# 3. La cohérence

## Définition

La cohérence signifie :

> Les données ne se contredisent pas.

Exemple :

| Date de naissance | Âge |
| ----------------- | --- |
| 2010              | 45  |

Impossible.

Autre exemple :

Une commande est enregistrée comme livrée...

avant d'avoir été expédiée.

Les informations se contredisent.

Le dataset est incohérent.

---

### À retenir

Cohérence = **aucune contradiction entre les données**.

---

# 4. L'actualité

## Définition

L'actualité (ou fraîcheur) signifie :

> Les données sont récentes et correspondent encore à la réalité. 

Exemple :

Une banque entraîne une IA sur des fraudes datant de 2015.

En 2026 :

Les techniques des fraudeurs ont changé.

Le modèle ne reconnaît plus les nouvelles fraudes.

Le dataset est devenu obsolète.

---

### À retenir

Actualité = **les données sont encore valides aujourd'hui**.

---

# 5. La représentativité

C'est probablement la notion la plus importante du cours.

## Définition

La représentativité signifie :

> Le dataset représente correctement tous les cas réels que rencontrera le modèle. 

Exemple :

Tu crées une IA qui reconnaît les chiens.

Tu lui montres uniquement :

* des Labradors

Le jour où elle voit :

* un Chihuahua

Elle échoue.

Pourquoi ?

Parce que les Labradors représentaient 100 % du dataset.

Le dataset n'était pas représentatif.

---

### Autre exemple

Une entreprise possède :

* 90 % de clients adultes
* 10 % de jeunes

Mais son dataset contient :

* 99 % d'adultes
* 1 % de jeunes

L'IA sera excellente pour les adultes...

mais très mauvaise pour les jeunes.

---

### À retenir

Représentativité = **tous les profils importants sont suffisamment présents dans le dataset**.

---

# 6. La pertinence

## Définition

La pertinence signifie :

> Les informations disponibles sont utiles pour résoudre le problème. 

Exemple :

On veut prédire :

"Un client va-t-il acheter une voiture ?"

On enregistre :

* sa couleur préférée
* son plat préféré

Ces informations sont probablement inutiles.

En revanche :

* salaire
* âge
* nombre d'enfants

sont beaucoup plus pertinentes.

---

### À retenir

Pertinence = **les bonnes informations sont présentes**.

---

# Comment vérifier la qualité d'un dataset ?

Le cours explique qu'avant d'entraîner une IA, il faut réaliser un **audit**.

## Définition

Un audit est une analyse complète du jeu de données afin de détecter ses défauts. 

On regarde notamment :

* les valeurs manquantes ;
* les distributions des données ;
* les corrélations entre variables ;
* les valeurs aberrantes (outliers) ;
* la qualité des annotations ;
* les incohérences.

---

# Les valeurs aberrantes (Outliers)

## Définition

Les **outliers** sont des valeurs très éloignées des autres. 

Exemple :

Les salaires sont :

* 2 000 €
* 2 100 €
* 1 900 €
* 150 000 €

Le dernier est une valeur aberrante.

Mais attention :

Le cours insiste sur un point :

> Un outlier n'est pas forcément une erreur.

Il peut représenter un cas rare mais réel (par exemple un très gros client ou une panne exceptionnelle). Avant de le supprimer, il faut le valider avec un expert métier. 

---

# Les valeurs manquantes

Le cours déconseille de supprimer automatiquement toutes les lignes incomplètes.

Pourquoi ?

Parce qu'on risque de perdre beaucoup d'informations et même d'introduire un biais. Il faut d'abord comprendre **pourquoi** les données manquent. 

Exemple :

22 % des valeurs d'humidité manquent uniquement sur les sites tropicaux.

Ce n'est pas un hasard.

Cela révèle un problème de collecte.

---

# Qu'est-ce que l'imputation ?

## Définition

L'**imputation** consiste à remplacer une valeur manquante par une estimation.

Exemple :

| Température |
| ----------- |
| 20°C        |
| 22°C        |
| ?           |
| 21°C        |

On peut estimer la valeur manquante grâce à différentes méthodes.

Le cours recommande d'utiliser des méthodes intelligentes (comme la régression ou les k plus proches voisins) plutôt qu'une simple moyenne lorsque c'est possible, afin de préserver les relations entre les variables. 

---

# Pourquoi normaliser les données ?

## Définition

La **normalisation** consiste à mettre toutes les variables sur une échelle comparable. 

Exemple :

Une variable varie entre :

0 et 1

Une autre entre :

0 et 1 000 000

Sans normalisation, la seconde risque de dominer l'apprentissage.

---

# L'augmentation des données (Data Augmentation)

## Définition

L'augmentation des données consiste à créer de nouveaux exemples à partir des données existantes afin d'enrichir le dataset. 

Exemples :

Pour des images :

* rotation ;
* recadrage ;
* inversion miroir ;
* changement de couleur.

Pour du texte :

* remplacement par des synonymes ;
* traduction dans une autre langue puis retour au texte d'origine (*back-translation*).

Pour des séries temporelles :

* ajout d'un léger bruit (*jittering*).

Chaque type de donnée possède ses propres techniques d'augmentation. 

---

# Qu'est-ce que SMOTE ?

Imagine un modèle qui détecte la fraude bancaire.

Sur 10 000 opérations :

* 9 950 sont normales ;
* 50 sont frauduleuses.

Le modèle risque d'apprendre à répondre presque toujours "pas de fraude", car c'est la réponse la plus fréquente. 

## Définition

**SMOTE** (*Synthetic Minority Over-sampling Technique*) est une technique qui crée artificiellement de nouveaux exemples de la classe minoritaire afin de rééquilibrer le dataset. 

---

# Qu'est-ce qu'une Data Card ?

## Définition

Une **Data Card** est une fiche d'identité d'un jeu de données. Elle décrit :

* son origine ;
* son contenu ;
* ses limites ;
* les risques ;
* les transformations appliquées.

Elle permet d'assurer la transparence, la traçabilité et la reproductibilité des travaux. Le cours souligne que ce n'est pas une option réservée aux grandes entreprises. 

---

# La gouvernance des données

## Définition

La **gouvernance des données** est l'ensemble des règles qui garantissent que les données sont correctement collectées, documentées, contrôlées et suivies tout au long de leur cycle de vie. 

Cela inclut :

* des contrôles qualité ;
* la documentation ;
* la traçabilité ;
* un suivi continu ;
* des améliorations régulières.

---

# L'amélioration itérative

Le cours insiste sur une idée très importante :

> On n'améliore pas tout le dataset en même temps.

On regarde d'abord où le modèle se trompe.

Puis on améliore uniquement ces parties.

Exemple :

Une IA reconnaît :

* très bien les chiens ;
* très mal les chats noirs.

Au lieu de collecter des milliers de nouvelles photos de tous les animaux, on collecte surtout des photos de chats noirs. Cette approche ciblée est plus efficace et plus rentable. 

---

# Schéma mental du cours

```
Créer une IA
      │
      ▼
Avoir un dataset
      │
      ▼
Vérifier sa qualité
      │
      ├── Complétude
      ├── Exactitude
      ├── Cohérence
      ├── Actualité
      ├── Représentativité
      └── Pertinence
      │
      ▼
Faire un audit
      │
      ├── Valeurs manquantes
      ├── Outliers
      ├── Corrélations
      ├── Annotations
      └── Biais
      │
      ▼
Nettoyer les données
      │
      ├── Imputation
      ├── Traitement des outliers
      └── Normalisation
      │
      ▼
Améliorer le dataset
      │
      ├── Augmentation des données
      ├── SMOTE
      ├── Enrichissement
      └── Documentation (Data Card)
      │
      ▼
Entraîner une IA plus performante
```

## Les 15 définitions essentielles à connaître

* **Dataset** : ensemble de données utilisé pour entraîner une IA.
* **Qualité des données** : capacité d'un dataset à être complet, exact, cohérent, actuel, représentatif et pertinent.
* **Complétude** : absence de valeurs manquantes importantes.
* **Exactitude** : conformité des données à la réalité.
* **Cohérence** : absence de contradictions entre les données.
* **Actualité** : données suffisamment récentes.
* **Représentativité** : le dataset reflète la diversité réelle des cas.
* **Pertinence** : les variables sont utiles pour résoudre le problème.
* **Audit** : analyse méthodique de la qualité d'un dataset.
* **Outlier** : valeur très éloignée des autres observations.
* **Imputation** : remplacement d'une valeur manquante par une estimation.
* **Normalisation** : mise à l'échelle des variables numériques.
* **Augmentation des données** : création de nouveaux exemples à partir des données existantes.
* **SMOTE** : génération d'exemples synthétiques pour renforcer la classe minoritaire.
* **Data Card** : document décrivant un jeu de données (origine, limites, risques, transformations).

Si tu prépares un examen STUDI, ce sont ces notions qu'il faut maîtriser en priorité, car elles reviennent dans les exercices, le cas pratique TechnoMaint et les questions d'auto-évaluation. 
