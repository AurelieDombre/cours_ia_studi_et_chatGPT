
---

# Résumé détaillé – Fondamentaux de l'optimisation des modèles d'IA

## Introduction : pourquoi optimiser un modèle d'IA ?

Créer un modèle d'IA performant ne suffit pas. En entreprise, un modèle doit également :

* être rapide ;
* être fiable ;
* respecter les contraintes réglementaires ;
* répondre à un besoin métier.

Autrement dit, **un excellent modèle est un modèle qui apporte de la valeur à l'entreprise**, pas seulement celui qui obtient les meilleures statistiques.

Le cours insiste sur une idée essentielle :

> L'optimisation ne consiste pas seulement à améliorer des performances techniques, mais à améliorer les résultats concrets de l'entreprise. 

---

# I. Les différents types de modèles d'IA

Avant d'optimiser un modèle, il faut savoir de quel type il s'agit.

## 1. Les modèles supervisés

Ils apprennent grâce à des données **étiquetées**.

Exemple :

On montre au modèle :

* photo → chat
* photo → chien
* photo → voiture

Le modèle apprend à reconnaître chaque catégorie.

### Objectif

Faire des prédictions les plus justes possibles.

Les principales métriques sont :

* précision
* rappel
* F1-score

---

## 2. Les modèles non supervisés

Cette fois, il n'y a **pas de réponse connue**.

Le modèle doit découvrir seul des groupes.

Exemple :

Une entreprise possède 100 000 clients.

Personne ne connaît les profils.

Le modèle crée automatiquement des groupes :

* jeunes acheteurs
* gros consommateurs
* clients occasionnels

Le problème :

Impossible de dire immédiatement si ces groupes sont "bons".

On utilise alors :

* indice de silhouette
* inertie intra-cluster
* validation métier

C'est-à-dire :

> Les groupes créés sont-ils réellement utiles pour l'entreprise ? 

---

## 3. L'apprentissage par renforcement

Le modèle apprend grâce à un système :

* récompense
* punition

Comme un enfant qui apprend.

Exemple :

Un robot reçoit :

+10 points lorsqu'il atteint son objectif

−5 points lorsqu'il échoue.

Petit à petit, il apprend la meilleure stratégie.

---

# II. Les grands problèmes des modèles

Le cours insiste énormément sur deux notions.

## Le surajustement (Overfitting)

Le modèle apprend **par cœur** les données d'entraînement.

Résultat :

* excellent sur les anciennes données
* mauvais sur de nouvelles données

C'est comme un étudiant qui récite un sujet sans comprendre.

---

## Le sous-ajustement (Underfitting)

À l'inverse,

le modèle est trop simple.

Il n'apprend même pas correctement les données d'entraînement.

C'est comme un élève qui révise seulement 10 % du cours.

Le but est donc de trouver un équilibre entre les deux. 

---

# III. Les architectures de modèles

Le cours compare principalement deux familles.

## Les arbres de décision

Avantages :

* faciles à comprendre
* très explicables

Inconvénient :

* surajustement fréquent.

Solution :

→ élagage (pruning).

---

## Les réseaux de neurones

Ils sont beaucoup plus puissants.

Mais :

* difficiles à interpréter ;
* demandent beaucoup de calcul ;
* risquent le surajustement.

On utilise alors :

* régularisation
* réglage des hyperparamètres
* transfert d'apprentissage (Transfer Learning). 

---

# IV. L'objectif métier est plus important que la technique

Le cours insiste énormément sur cette idée.

Prenons un exemple.

Une banque veut détecter les fraudes.

L'objectif métier :

> détecter un maximum de fraudes.

Le modèle, lui, doit être optimisé selon cet objectif.

Cela signifie que les indicateurs techniques doivent être choisis en fonction du besoin réel.

Même chose dans le retail :

L'objectif n'est pas :

> avoir un modèle avec 99 % de précision.

Mais :

> mieux gérer les stocks.

Les performances techniques doivent donc être reliées aux performances économiques. 

---

# V. Les contraintes d'utilisation

Un même modèle peut être utilisé dans plusieurs contextes.

Le cours distingue notamment :

## Temps réel

Exemple :

Détection de fraude bancaire.

Le modèle doit répondre en moins de 100 ms.

Ici, la priorité est :

→ réduire la latence.

---

## Traitement Batch

Exemple :

Analyse des ventes pendant la nuit.

Le temps importe moins.

On cherche surtout :

→ une meilleure précision.

---

## Edge Computing

Exemple :

Drone.

Le processeur est limité.

Le modèle doit être :

* léger ;
* peu gourmand en énergie.

On utilise :

* compression
* quantification. 

---

# VI. Les métriques de performance

Le cours explique qu'il n'existe pas UNE seule métrique.

Tout dépend du problème.

---

## Exactitude (Accuracy)

Pourcentage de bonnes réponses.

Simple mais parfois trompeur.

---

## Précision

Question :

> Quand le modèle dit "Oui", a-t-il raison ?

Très importante lorsqu'un faux positif coûte cher.

Exemple :

Bloquer une carte bancaire sans raison.

---

## Rappel

La précision répond à la question :

> **Parmi toutes les prédictions positives du modèle, combien sont réellement correctes ?**

Question :

> Parmi tous les vrais cas positifs, combien ont été détectés ?

Très important en médecine.

Mieux vaut détecter presque tous les cancers, même si quelques personnes sont alertées à tort.

### Formule

[
\text{Précision} = \frac{\text{Vrais positifs}}{\text{Vrais positifs}+\text{Faux positifs}}
]

### Exemple

Un modèle détecte des e-mails comme étant du spam.

Il classe **100 e-mails** comme spam.

En réalité :

* 90 sont bien du spam ✅
* 10 sont des e-mails normaux ❌

La précision est donc :

90 / 100 = **90 %**

👉 Une **précision élevée** signifie que le modèle fait **peu de fausses alertes (faux positifs)**. 

---


## F1-score

Le **F1-Score** est un compromis entre :

* la précision ;
* le rappel.

Il est utilisé lorsque l'on souhaite équilibrer les deux, notamment si les classes sont déséquilibrées.

### Exemple

| Métrique  | Valeur |
| --------- | -----: |
| Précision |   90 % |
| Rappel    |   90 % |
| F1-score  | ≈ 90 % |

En revanche :

| Métrique  | Valeur |
| --------- | -----: |
| Précision |  100 % |
| Rappel    |   20 % |
| F1-score  | faible |

Même si la précision est excellente, le F1-score baisse car le modèle manque beaucoup de vrais cas.

👉 Le F1-score est donc utile lorsque l'on veut **un bon équilibre entre précision et rappel**. 

---

# Différence entre précision et rappel

Imagine un détecteur de fraude bancaire.

### Si on privilégie la précision :

* Peu de clients honnêtes sont bloqués.
* Mais certaines fraudes peuvent passer.

### Si on privilégie le rappel :

* Presque toutes les fraudes sont détectées.
* Mais davantage de clients honnêtes peuvent être bloqués.

👉 Tout dépend donc du contexte métier. 

---

## AUC-ROC


L'AUC-ROC mesure la capacité globale du modèle à distinguer les deux classes (par exemple : fraude / pas fraude, malade / sain).

La valeur varie entre **0 et 1**.

* **1** → modèle parfait ✅
* **0,9** → excellent
* **0,8** → bon
* **0,7** → correct
* **0,5** → le modèle fait aussi bien qu'un tirage au sort ❌

Le cours précise que l'AUC-ROC est particulièrement intéressante car elle reste pertinente même lorsque les classes sont déséquilibrées. 

### Exemple

Deux modèles détectent une fraude.

* Modèle A : AUC = **0,97**
* Modèle B : AUC = **0,75**

➡️ Le modèle A sépare beaucoup mieux les transactions frauduleuses des transactions normales.

---

## Régression

La **régression** est utilisée lorsque le modèle prédit une **valeur numérique** et non une catégorie.

### Exemples

* prédire le prix d'une maison ;
* prévoir les ventes d'un magasin ;
* estimer la température de demain.

On utilise principalement deux métriques.

### MAE (Mean Absolute Error)

C'est **l'erreur moyenne** entre les prédictions et les vraies valeurs.

Exemple :

|  Réel | Prédit | Erreur |
| ----: | -----: | -----: |
| 100 € |  105 € |    5 € |
| 200 € |  190 € |   10 € |

MAE = (5 + 10) / 2 = **7,5 €**

👉 Plus la MAE est faible, meilleur est le modèle.

### RMSE (Root Mean Squared Error)

La RMSE fonctionne comme la MAE, mais **elle pénalise davantage les grosses erreurs**.

Exemple :

Deux modèles :

* Modèle A : erreurs de 2 €, 3 €, 2 €
* Modèle B : erreurs de 1 €, 1 €, 30 €

La MAE pourrait sembler proche, mais la RMSE sera beaucoup plus élevée pour le modèle B, car elle donne plus de poids à la très grosse erreur.

👉 On utilise souvent la RMSE lorsque les grosses erreurs sont particulièrement coûteuses. 

---

# Tableau récapitulatif

| Métrique      | À quoi sert-elle ?                                        | Quand l'utiliser ?                                          |
| ------------- | --------------------------------------------------------- | ----------------------------------------------------------- |
| **Précision** | Vérifie si les prédictions positives sont correctes       | Quand les faux positifs sont coûteux (fraude, spam)         |
| **Rappel**    | Vérifie si tous les vrais positifs sont détectés          | Quand les faux négatifs sont dangereux (médecine, sécurité) |
| **F1-Score**  | Équilibre entre précision et rappel                       | Quand on veut un compromis ou des classes déséquilibrées    |
| **AUC-ROC**   | Mesure la capacité globale à distinguer les classes       | Pour comparer des modèles de classification                 |
| **MAE**       | Mesure l'erreur moyenne d'une prédiction numérique        | Régression                                                  |
| **RMSE**      | Mesure l'erreur moyenne en pénalisant les grosses erreurs | Régression, lorsque les grosses erreurs sont critiques      |

---
### Astuce pour retenir

* 🎯 **Précision** = *Quand je dis "oui", ai-je raison ?*
* 🔍 **Rappel** = *Ai-je trouvé tous les vrais "oui" ?*
* ⚖️ **F1-score** = *Le meilleur compromis entre les deux.*
* 📈 **AUC-ROC** = *À quel point le modèle sépare bien les classes ?*
* 💶 **MAE / RMSE** = *De combien se trompe le modèle lorsqu'il prédit une valeur ?*
---

## Clustering

On utilise :

* indice de silhouette
* inertie.

---

## Modèles génératifs

Deux métriques apparaissent :

Perplexité

→ qualité d'un modèle de langage.

FID

→ qualité des images générées. 

---

# VII. Les métriques doivent être traduites en valeur business

C'est probablement **l'idée la plus importante du cours**.

Un directeur ne veut pas entendre :

> "Le F1-score a augmenté."

Il veut entendre :

> "Les pertes dues aux fraudes ont diminué de 20 %."

Autrement dit :

Chaque métrique technique doit être reliée à un indicateur économique :

* chiffre d'affaires ;
* satisfaction client ;
* réduction des coûts ;
* retour sur investissement (ROI). 

---

# VIII. La méthode DMAIC

Le cours présente une méthode très utilisée pour optimiser un modèle.

## D — Define

Définir :

* le problème ;
* les objectifs ;
* les contraintes.

---

## M — Measure

Mesurer les performances actuelles.

Créer une **baseline**.

C'est le point de départ.

---

## A — Analyze

Chercher les causes des mauvaises performances.

Exemple :

* données de mauvaise qualité ;
* mauvais hyperparamètres ;
* architecture inadaptée.

---

## I — Improve

Tester des solutions :

* nouvelles données ;
* réglages ;
* nouvelle architecture ;
* nouvelles fonctionnalités.

---

## C — Control

Surveiller le modèle après son déploiement.

Pourquoi ?

Parce qu'un modèle peut se dégrader avec le temps.

On parle alors de **Concept Drift**.

Il faut donc :

* surveiller les métriques ;
* déclencher des alertes ;
* réentraîner le modèle si nécessaire. 

---

# IX. La préparation d'une optimisation

Le cours conseille de toujours commencer par :

## 1. Faire un audit

Mesurer :

* précision ;
* rappel ;
* latence ;
* consommation mémoire ;
* robustesse.

---

## 2. Étudier les données

Vérifier :

* biais ;
* données manquantes ;
* déséquilibre.

---

## 3. Construire un environnement reproductible

Même version :

* Python ;
* bibliothèques ;
* données ;
* hyperparamètres.

Le but :

obtenir exactement les mêmes résultats.

---

## 4. Utiliser le versioning

Le cours recommande des outils comme :

* MLflow
* Weights & Biases

pour enregistrer :

* modèles ;
* métriques ;
* jeux de données ;
* hyperparamètres. 

---

# X. Les réglementations

Deux réglementations sont citées.

## RGPD

Protège les données personnelles.

---

## AI Act

Nouvelle réglementation européenne.

Elle classe les IA selon leur niveau de risque et impose davantage d'exigences pour les applications sensibles. 

---

# Les 10 idées à retenir absolument

1. **Chaque type de modèle (supervisé, non supervisé, renforcement) s'optimise différemment.**
2. **Éviter le surajustement et le sous-ajustement est essentiel.**
3. **Les métriques doivent être choisies selon le contexte métier.**
4. **Précision, rappel et F1-score sont les métriques clés de la classification.**
5. **La latence est cruciale pour les applications en temps réel.**
6. **L'optimisation doit toujours servir un objectif business, pas seulement améliorer un chiffre technique.**
7. **Le framework DMAIC (Define, Measure, Analyze, Improve, Control) est la méthode de référence pour améliorer un modèle de façon structurée.**
8. **Les expérimentations doivent être reproductibles grâce au versioning, à un environnement de test stable et à une bonne documentation.**
9. **Les contraintes réglementaires (RGPD, AI Act) et l'explicabilité doivent être intégrées dès la conception.**
10. **Une optimisation réussie est un équilibre entre performance, rapidité, coût, robustesse et valeur métier.** 

**Conseil pour l'examen :** si tu maîtrises ces 10 idées et que tu sais expliquer pourquoi on choisit une métrique plutôt qu'une autre (par exemple, le rappel en médecine ou la précision en détection de fraude), tu auras compris l'essentiel du cours.


Avec plaisir ! Cet exercice est **très représentatif de ce que l'on peut te demander en examen**. Il ne s'agit pas seulement de connaître le cours, mais surtout de **savoir appliquer les notions (DMAIC, métriques, optimisation, indicateurs business, etc.)** à un cas concret. 

Je vais te l'expliquer comme si nous étions en cours.

---

# 1. Comprendre la situation

## L'entreprise

L'entreprise s'appelle **FashionLine**.

C'est un site de e-commerce qui vend des vêtements.

Elle possède :

* 2,5 millions de visiteurs par mois ;
* 45 000 produits.

Pour aider les clients à acheter, elle utilise un **modèle d'IA de recommandation**.

Exemple :

> Tu regardes un jean.

Le modèle recommande :

* une ceinture ;
* une chemise ;
* une veste.

L'objectif est de faire acheter davantage.

---

## Le problème

Le modèle fonctionne depuis **18 mois**, mais il commence à poser des problèmes.

On en observe **deux principaux** :

### Problème n°1 : les recommandations ne sont plus pertinentes

Les clients se plaignent.

Pourquoi ?

Parce que le modèle recommande :

* des vêtements hors saison ;
* des tailles indisponibles ;
* toujours les mêmes produits.

Les plaintes ont augmenté de **23 %**. 

---

### Problème n°2 : le modèle est trop lent

Aujourd'hui :

* temps moyen = **420 ms**
* objectif = **150 ms**

Pendant le Black Friday :

* plus de **800 ms**

Les clients attendent trop longtemps.

Certains quittent même le site.

➡️ C'est ce qu'on appelle un problème de **latence**. 

---

# 2. Les indicateurs montrent que le modèle est mauvais

Le tableau fournit plusieurs métriques.

Prenons-les une par une.

### Précision = 12 %

Objectif = 20 %

Cela signifie que lorsque le modèle recommande un produit :

> les utilisateurs cliquent seulement **12 fois sur 100**.

Les recommandations ne sont donc pas très pertinentes. 

---

### Rappel = 8 %

Le catalogue contient 45 000 produits.

Mais le modèle ne recommande qu'une très petite partie.

Autrement dit :

> il oublie énormément de produits.

Résultat :

Les recommandations sont répétitives.

Toujours les mêmes articles.

---

### F1-score = 0,42

L'objectif est 0,60.

Comme le F1-score combine :

* précision
* rappel

on comprend immédiatement que :

* la précision est faible ;
* le rappel est faible.

Le modèle est donc mauvais sur les deux aspects.

---

### Latence = 420 ms

Le site répond presque **3 fois plus lentement** que prévu.

Cela dégrade :

* le confort utilisateur ;
* les ventes.

---

### Conversion = 3,1 %

Seulement 3,1 % des recommandations provoquent un achat.

L'objectif est 5 %.

Donc le modèle rapporte moins d'argent qu'il ne devrait.

---

### Part du chiffre d'affaires

Seulement **11 %** du chiffre d'affaires vient des recommandations.

L'objectif est 18 %.

Encore une preuve que le modèle est peu performant.

---

### Abandon de panier

34 %

Quand une mauvaise recommandation apparaît,

beaucoup de clients abandonnent leur panier.

C'est une perte directe pour l'entreprise. 

---

# 3. Pourquoi le modèle fonctionne-t-il mal ?

Le sujet donne plusieurs indices.

## Premier indice

Le modèle n'a pas été ré-entraîné depuis **6 mois**.

Pourquoi est-ce un problème ?

Parce que la mode change.

En hiver :

on vend des manteaux.

En été :

des shorts.

Si le modèle apprend encore avec des données d'hiver,

il continuera à recommander des manteaux en juillet.

C'est ce qu'on appelle le **concept drift**.

---

## Deuxième indice

Les données ne distinguent pas :

* achat pour soi ;
* achat cadeau.

Exemple :

J'achète une robe pour offrir.

Le modèle croit que j'aime les robes.

La prochaine fois,

il me recommande encore des robes.

La recommandation est donc fausse.

---

## Troisième indice

Un seul serveur.

Aucun cache.

Conséquence :

À chaque visite,

le modèle recalcule toutes les recommandations.

C'est très lent.

Avec un cache,

les recommandations les plus fréquentes seraient déjà prêtes. 

---

# 4. Que faut-il faire ? → appliquer le DMAIC

Le sujet demande explicitement d'utiliser le DMAIC.

## D = Define

On définit précisément les problèmes.

Ici il y en a deux :

### Axe 1

La pertinence.

### Axe 2

La latence.

On identifie aussi les personnes concernées :

* service client ;
* équipe infrastructure ;
* marketing.

Puis on fixe des objectifs mesurables :

* précision 20 % ;
* F1-score 0,60 ;
* latence 150 ms. 

---

## M = Measure

On mesure précisément la situation actuelle.

On construit une **baseline**.

Cela signifie :

> on note les performances avant de modifier quoi que ce soit.

On mesure :

* précision ;
* rappel ;
* F1 ;
* latence.

Puis on découpe les résultats :

* selon les catégories ;
* selon les utilisateurs ;
* selon les périodes.

Pourquoi ?

Parce qu'on peut découvrir que le problème touche seulement certaines catégories (par exemple les vêtements d'hiver). 

---

## A = Analyze

Maintenant,

on cherche les causes.

Trois audits sont nécessaires.

### Audit des données

Chercher :

* données anciennes ;
* données manquantes ;
* biais.

---

### Audit du modèle

Vérifier :

* surajustement ;
* architecture adaptée ;
* réseau trop complexe ?

---

### Audit de l'infrastructure

Chercher :

* serveur saturé ;
* absence de cache ;
* problème matériel. 

---

# 5. Quelles métriques suivre ?

Le sujet insiste sur une idée importante :

Il faut distinguer **les métriques techniques** des **indicateurs business**.

## Les métriques techniques

Elles mesurent les performances de l'IA :

* précision ;
* rappel ;
* F1-score ;
* latence ;
* diversité des recommandations.

Elles intéressent surtout les développeurs et data scientists.

---

## Les indicateurs business

Ils intéressent les dirigeants.

Par exemple :

* taux de conversion ;
* chiffre d'affaires ;
* abandon panier ;
* plaintes clients.

Pourquoi ?

Parce qu'un directeur ne veut pas seulement savoir que le F1-score passe de 0,42 à 0,60.

Il veut surtout savoir :

> « Est-ce que cela augmente les ventes ? » 

---

# 6. Comment optimiser le modèle ?

Le corrigé propose trois grandes priorités.

## Priorité 1 : améliorer l'infrastructure

Pourquoi commencer ici ?

Parce que c'est rapide.

Actions :

* ajouter un cache ;
* répartir la charge sur plusieurs serveurs.

Résultat :

la latence diminue immédiatement.

---

## Priorité 2 : améliorer les données

Ensuite :

* ré-entraîner le modèle ;
* ajouter les nouvelles données ;
* distinguer cadeaux et achats personnels ;
* filtrer les produits indisponibles.

Cette étape améliore directement la qualité des recommandations.

---

## Priorité 3 : améliorer le modèle

Enfin :

* compresser le modèle ;
* ajouter davantage de diversité dans les recommandations ;
* vérifier les biais liés au genre.

Cette dernière étape est plus complexe, donc elle est réalisée après les gains rapides obtenus grâce aux deux premières. 

---

# 7. La phase Control

Une erreur fréquente est de croire que le projet est terminé après l'optimisation.

En réalité, il faut continuer à surveiller le modèle.

Le corrigé propose de :

* suivre automatiquement le F1-score ;
* surveiller la latence ;
* mesurer le taux de conversion ;
* créer des alertes si les performances baissent ;
* ré-entraîner régulièrement le modèle avec **MLflow**.

L'objectif est d'éviter que les mêmes problèmes réapparaissent dans quelques mois. 

---

# Ce qu'il faut retenir pour l'examen

Si tu dois répondre à un exercice comme celui-ci, pense toujours à cette méthode :

1. **Identifier les problèmes** (ici : pertinence et latence).
2. **Analyser les métriques** (précision, rappel, F1-score, latence, conversion...).
3. **Appliquer le DMAIC** :

   * **Define** : définir les problèmes et les objectifs.
   * **Measure** : mesurer les performances actuelles (baseline).
   * **Analyze** : rechercher les causes (données, modèle, infrastructure).
   * **Improve** : proposer des solutions concrètes (cache, ré-entraînement, optimisation du modèle).
   * **Control** : mettre en place un suivi continu avec des alertes et un ré-entraînement régulier.
4. **Toujours relier les améliorations techniques aux résultats business** (plus de ventes, moins de plaintes, meilleure satisfaction client).

💡 **Astuce d'examen :** dans ce type de cas pratique, les correcteurs attendent surtout que tu **justifies chaque proposition avec les données de l'énoncé**. Par exemple : *« Je propose un ré-entraînement car le modèle n'a pas été mis à jour depuis 6 mois »* ou *« Je mets en place un cache car l'infrastructure repose sur un serveur unique et la latence atteint 800 ms en période de pointe. »* C'est cette justification qui montre que tu sais appliquer le cours, et pas seulement le réciter.
