# Résumé pédagogique – Optimisation des modèles d'IA

> **Objectif :** comprendre pourquoi on optimise un modèle d'intelligence artificielle, quelles sont les principales techniques utilisées et dans quels cas les appliquer.

---

# Plan

1. Pourquoi optimiser un modèle ?
2. Diagnostiquer les performances
3. Les techniques de compression
4. Optimisation de l'inférence
5. Déploiement des modèles
6. MLOps
7. Méthodologie pour les exercices
8. Fiche de révision

---

D'après votre cours, cette leçon explique comment rendre un modèle d’IA plus rapide, plus léger et moins coûteux sans trop perdre en qualité. L’idée centrale est simple : un modèle peut être très performant, mais s’il consomme trop de mémoire, d’énergie ou de temps de calcul, il devient difficile à déployer, surtout sur mobile, en edge ou dans des environnements contraints comme l’hôpital ou l’industrie.

1. D’abord, mesurer avant d’optimiser
Le cours insiste sur le profilage : on ne regarde pas seulement la précision, mais aussi la latence, le débit, la mémoire utilisée, le CPU ou GPU mobilisé, et les transferts de données. Cela permet d’identifier les goulots d’étranglement. Par exemple, pour votre futur métier dans le développement d’une solution digitale avec IA, un modèle peut sembler bon en test, mais être trop lent en production sur un matériel moins puissant.

2. Ensuite, compresser le modèle
Le cours présente trois grandes techniques :

Distillation : un petit modèle apprend d’un grand modèle.
Pruning : on supprime les poids ou blocs les moins utiles.
Quantification : on réduit la précision numérique, par exemple vers INT8.
Ces méthodes visent à alléger le modèle tout en gardant un bon niveau de performance.

3. Enfin, optimiser l’exécution et le déploiement
Le cours montre aussi qu’on peut gagner en efficacité en :

fusionnant des opérations,
optimisant le graphe d’exécution,
accélérant le pipeline de données,
choisissant une infrastructure adaptée : cloud, edge, hybride ou local.
À retenir
Le message principal est : on n’optimise pas seulement le modèle, on optimise tout le système. Dans une logique de MLOps, cela devient un travail continu, mesuré, testé et adapté au contexte réel de déploiement.


# 1. Pourquoi optimiser un modèle ?

## Définition

Après son entraînement, un modèle d'IA peut être très performant, mais cela ne signifie pas qu'il est prêt à être utilisé en production.

Un modèle peut être :

- trop lent ;
- trop volumineux ;
- trop gourmand en mémoire ;
- trop énergivore.

L'objectif de l'optimisation est donc de **conserver les meilleures performances possibles tout en réduisant les ressources nécessaires**.

---

## Exemple

Imaginons un modèle de reconnaissance d'images.

Avant optimisation :

- Temps de réponse : **2 secondes**
- Taille : **500 Mo**

Après optimisation :

- Temps de réponse : **200 ms**
- Taille : **80 Mo**
- Précision presque identique.

L'utilisateur ne remarque quasiment aucune différence de qualité, mais l'application est beaucoup plus rapide.

---

# 2. Diagnostiquer les performances

Avant de modifier un modèle, il faut comprendre **où se situe le problème**.

On mesure plusieurs indicateurs.

## Latence

Temps nécessaire pour produire une seule prédiction.

**Objectif :** obtenir une latence la plus faible possible.

---

## Throughput

Nombre de prédictions réalisées par seconde.

Plus le throughput est élevé, plus le modèle peut traiter de données.

---

## Utilisation mémoire

Quantité de mémoire RAM ou GPU utilisée pendant l'exécution.

---

## Utilisation CPU/GPU

Permet de savoir si le processeur ou la carte graphique est utilisé efficacement.

---

## Benchmarking

Le benchmarking consiste à comparer plusieurs modèles ou plusieurs versions d'un même modèle dans les mêmes conditions.

Cela permet de choisir objectivement la meilleure solution.

---

# 3. Les techniques de compression

## Distillation

### Définition

La distillation consiste à entraîner un petit modèle grâce à un modèle beaucoup plus grand.

Le grand modèle est appelé :

**Teacher (professeur)**

Le petit modèle est appelé :

**Student (élève)**

Le professeur transmet ses connaissances à l'élève.

### Avantages

- modèle plus petit ;
- plus rapide ;
- faible perte de précision.

### Exemple

Le professeur obtient 98 % de précision.

L'élève atteint 97 % tout en étant quatre fois plus rapide.

---

## Pruning

### Définition

Le pruning consiste à supprimer les neurones ou connexions qui ont très peu d'influence sur les résultats.

### Objectif

Réduire :

- la taille ;
- la mémoire utilisée ;
- le temps d'inférence.

### Exemple

Comme lorsqu'on taille un arbre :

on retire les branches inutiles pour conserver uniquement les plus importantes.

---

## Quantification

### Définition

La quantification réduit la précision numérique des poids.

Exemple :

- Float32 → INT8

### Avantages

- moins de mémoire ;
- calculs plus rapides ;
- meilleure efficacité énergétique.

### Inconvénient

Une quantification trop importante peut diminuer la précision.

---

## Architectures légères

Certaines architectures sont conçues dès le départ pour être peu gourmandes.

Exemples :

- MobileNet
- EfficientNet
- ShuffleNet

Elles sont principalement utilisées sur :

- smartphones ;
- tablettes ;
- objets connectés.

---

# 4. Optimisation de l'inférence

L'inférence correspond au moment où le modèle réalise une prédiction.

Plusieurs outils permettent d'accélérer cette étape.

## TensorRT

Optimise automatiquement les réseaux de neurones pour les cartes NVIDIA.

---

## TVM

Optimise le modèle pour différents types de processeurs.

---

## XLA

Compilateur utilisé notamment avec TensorFlow.

Il fusionne certaines opérations afin de réduire le temps de calcul.

---

# 5. Déploiement des modèles

![Schéma](/compres-effica-optimi-comp-im1.png)

## Cloud

Le modèle est exécuté sur un serveur distant.

### Avantages

- forte puissance de calcul ;
- mise à l'échelle facile.

### Inconvénients

- dépendance au réseau ;
- coût.

---

## Edge Computing

Le modèle fonctionne directement sur l'appareil.

Exemples :

- téléphone ;
- caméra ;
- robot.

### Avantages

- très faible latence ;
- meilleure confidentialité.

### Inconvénients

- ressources limitées.

---

## Docker

Docker permet de regrouper :

- le modèle ;
- les bibliothèques ;
- les dépendances.

Ainsi, l'application fonctionne de la même manière sur tous les ordinateurs.

---

## Kubernetes

Kubernetes gère automatiquement plusieurs conteneurs Docker.

Il permet :

- le déploiement automatique ;
- la montée en charge ;
- le redémarrage des applications en cas de panne.

---

# 6. MLOps

Le MLOps correspond à l'ensemble des bonnes pratiques permettant de gérer le cycle de vie d'un modèle.

Il comprend notamment :

- le versionnage ;
- le déploiement continu (CI/CD) ;
- le monitoring ;
- le réentraînement automatique ;
- la maintenance.

---

# 7. Méthodologie des exercices

Lorsqu'un exercice demande de choisir une technique d'optimisation, suivre toujours cette méthode.

## Étape 1

Identifier le problème.

Exemples :

- modèle trop lent ;
- modèle trop gros ;
- manque de mémoire.

---

## Étape 2

Choisir la technique adaptée.

Exemple :

- modèle trop lourd → pruning ou quantification.

---

## Étape 3

Justifier le choix.

Toujours expliquer pourquoi cette technique répond au problème.

---

## Étape 4

Présenter les avantages.

Exemple :

- gain de mémoire ;
- accélération des calculs.

---

## Étape 5

Présenter les limites.

Exemple :

- légère perte de précision.

---

# 8. Fiche de révision

| Notion | À retenir |
|---------|------------|
| Optimisation | Rendre le modèle plus rapide et moins gourmand. |
| Latence | Temps d'une prédiction. |
| Throughput | Nombre de prédictions par seconde. |
| Benchmarking | Comparaison de plusieurs modèles. |
| Distillation | Un grand modèle enseigne à un petit. |
|Distillation de connaissances|Entraînement d'un modèle compact à imiter les sorties probabilistes d'un modèle plus massif |
| Pruning | Suppression des connexions inutiles. |
|Pruning structuré|Suppression de blocs entiers (filtres, neurones, têtes d'attention) permettant des gains significatifs lors du déploiement matériel|
|Pruning non structuré| Retrait individuel de poids jugés négligeables, indépendamment de leur position dans la couche|
| Quantification | Réduction de la précision numérique. |
|Quantification-aware training| Apprentissage du modèle avec des contraintes de précision numérique réduite intégrées dès l'origine |
| MobileNet | Architecture légère pour appareils mobiles. |
| TensorRT | Optimisation des modèles pour GPU NVIDIA. |
| TVM | Optimisation multi-matériels. |
| XLA | Compilation et fusion d'opérations. |
| Cloud | Exécution sur serveur distant. |
| Edge | Exécution directement sur l'appareil. |
| Docker | Conteneur contenant l'application et ses dépendances. |
| Kubernetes | Gestion automatique des conteneurs. |
| MLOps | Gestion complète du cycle de vie d'un modèle. |
|Bande passante mémoire| Quantité maximale de données transférable entre mémoire et unités de calcul, dont la saturation crée un goulot matériel incompressible. Est la limite physique des transferts entre mémoire et calcul : aucune optimisation logicielle ne peut la compenser si elle est saturée|
|Baseline| Ensemble de mesures de référence permettant d'évaluer objectivement les gains ou pertes d'une optimisation|
|Heatmap ou graphe d'exécution| rendent visibles les nœuds critiques qui bloquent la chaîne.  Référentiel de mesures qui permet de juger objectivement l'impact de chaque modification.|

---

# Les points essentiels pour l'examen

Il faut être capable d'expliquer :

- Pourquoi on optimise un modèle.
- La différence entre **Cloud** et **Edge**.
- Le rôle de la **Distillation**, du **Pruning** et de la **Quantification**.
- À quoi servent **TensorRT**, **TVM** et **XLA**.
- Le rôle de **Docker** et **Kubernetes**.
- Ce qu'est le **MLOps**.
- La méthodologie pour choisir une technique d'optimisation.


# Synthèse cours 


### Comment identifier efficacement les goulots d'étranglement d'un modèle IA en production ?

Profiler le modèle dans l'environnement cible réel, pas uniquement sur machine de développement.

Utiliser des outils spécialisés (PyTorch Profiler, TensorFlow Profiler, NVIDIA Nsight) pour cartographier chaque opération. Analyse ligne à ligne des opérations et visualisation de la charge sur chaque composant matériel

Mesurer latence, débit, consommation mémoire et I/O sur plusieurs scénarios d'usage représentatifs.

Comparer les performances sur différentes plateformes (cloud, edge, GPU, CPU) pour anticiper les écarts de déploiement.

### Comment choisir entre distillation, pruning et quantification pour compresser un modèle ?

Évaluer la tolérance métier à la perte de précision et fixer un seuil de dégradation acceptable.

Privilégier la distillation si vous disposez d'un modèle teacher performant et de ressources d'entraînement.

Opter pour le pruning structuré si l'objectif est un gain matériel immédiat et une simplification du graphe.

Appliquer la quantification post-entraînement pour un déploiement rapide sur edge avec gains mémoire et vitesse.

### Comment intégrer l'optimisation computationnelle dans un pipeline MLOps existant ?

Automatiser le profilage et le benchmarking à chaque itération du cycle CI/CD.

Définir des seuils de performance (latence, débit, mémoire) comme critères de validation avant déploiement.

Générer automatiquement des versions optimisées (quantifiées, compilées) et les tester en parallèle.

Documenter chaque optimisation appliquée et capitaliser les retours d'expérience dans un référentiel partagé.

### Comment garantir la portabilité et la résilience d'un modèle IA déployé à grande échelle ?

Containeriser le modèle et ses dépendances avec Docker pour assurer reproductibilité sur tout environnement.

Orchestrer le déploiement avec Kubernetes pour gérer montée en charge, rollback et haute disponibilité.

Tester le modèle sur toutes les plateformes cibles avant mise en production pour détecter les régressions.

Mettre en place un monitoring continu des métriques de performance et déclencher des alertes en cas de dérive.

### Comment arbitrer entre performance, coût et impact environnemental lors du déploiement d'un modèle IA ?

Mesurer la consommation énergétique réelle du modèle sur l'infrastructure cible et la rapporter au coût opérationnel.

Comparer plusieurs scénarios de déploiement (cloud mutualisé, edge local, hybride) en intégrant critères RSE.

Privilégier les architectures légères et les optimisations compilateur pour réduire empreinte carbone sans sacrifier qualité.

Documenter les arbitrages et les communiquer aux parties prenantes pour aligner décisions techniques et engagements stratégiques.