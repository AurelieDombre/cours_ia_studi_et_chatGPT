
---

# Résumé très détaillé - Tests de robustesse et sécurité des modèles IA

# I. Pourquoi ce cours est important ?

Créer un modèle d'IA qui fonctionne en laboratoire n'est pas suffisant.

Le vrai défi est de savoir s'il fonctionnera **dans la vraie vie**, où les données sont rarement parfaites.

Imagine un étudiant :

* il obtient 20/20 uniquement lorsqu'on lui pose exactement les questions qu'il a apprises → il n'est pas très intelligent.
* il réussit même lorsque les questions sont formulées différemment → il est robuste.

C'est exactement le même principe pour une IA.

---

# Les deux objectifs du cours

Le cours répond à deux questions.

## 1. Le modèle est-il robuste ?

Autrement dit :

> Continue-t-il à bien fonctionner lorsque les données changent un peu ?

## 2. Le modèle est-il sécurisé ?

Autrement dit :

> Peut-on tromper ou attaquer le modèle ?

Ces deux notions sont différentes mais complémentaires. 

---

# II. La robustesse

## Définition

La robustesse est :

> La capacité d'un modèle IA à continuer de donner de bons résultats même lorsque les données sont différentes de celles utilisées pendant son entraînement. 

En résumé :

**Un modèle robuste = un modèle qui résiste aux perturbations.**

---

## Exemple très simple

Tu entraînes une IA à reconnaître des chats.

Pendant l'entraînement :

* toutes les photos sont lumineuses
* les chats sont toujours de face
* les photos sont nettes

L'IA obtient 99 % de réussite.

Puis tu la mets sur Internet.

Les utilisateurs envoient :

* des photos floues
* des chats de dos
* des chats dans le noir
* des chats cachés derrière un meuble

Si l'IA ne reconnaît plus les chats...

➡ elle est performante...

mais PAS robuste.

---

# III. Performance ≠ Robustesse

C'est LA différence la plus importante du cours.

## Performance

La performance mesure :

> Les résultats obtenus dans des conditions parfaites.

On utilise des données propres.

Exemple :

94 % de précision.

Tout semble parfait.

---

## Robustesse

La robustesse mesure :

> Ce qui se passe lorsque les conditions deviennent difficiles.

Exemple :

Photo normale :

→ 94 %

Photo un peu floue :

→ 92 %

Photo sombre :

→ 91 %

Photo bruitée :

→ 90 %

Le modèle est robuste.

Autre cas :

Photo normale :

→ 94 %

Photo floue :

→ 50 %

Le modèle n'est pas robuste.

**À retenir :**

Performance = qualité en laboratoire.

Robustesse = qualité dans la vraie vie. 

---

# IV. Pourquoi tester la robustesse ?

Parce que les données réelles ne ressemblent jamais exactement aux données d'entraînement.

Exemples :

En médecine :

Scanner différent.

En banque :

Format de dossier différent.

En industrie :

Capteur défectueux.

En voiture autonome :

Pluie.

Brouillard.

Reflets.

Le modèle doit continuer à fonctionner malgré tout. 

---

# V. Les perturbations à tester

Une perturbation est :

> Une modification volontaire des données pour voir si l'IA résiste.

Le cours distingue plusieurs catégories.

## 1. Bruit aléatoire

Définition :

Ajout de petites erreurs dans les données.

Exemples :

* image avec du bruit
* enregistrement audio parasité
* erreur de saisie

---

## 2. Déformations

On modifie légèrement les données.

Exemples :

Images :

* rotation
* flou
* compression

Audio :

* changement de fréquence

Tableaux :

* colonnes déplacées

---

## 3. Données incomplètes

Il manque des informations.

Exemples :

* une ligne vide
* une page absente
* un texte coupé
* un capteur hors service

---

## 4. Valeurs extrêmes

Ce sont des cas rares.

Exemple :

Un client avec un revenu extrêmement élevé.

Une température inhabituelle.

---

## 5. Données OOD (Out Of Distribution)

C'est une notion essentielle.

### Définition

Les données OOD sont :

> Des données très différentes de celles utilisées pendant l'entraînement. 

Exemples :

L'IA apprend sur :

* des scanners Canon

Puis elle reçoit :

* des scanners Epson

Les images sont correctes...

mais différentes.

Résultat :

Les performances chutent.

Ce sont des données OOD.

---

# VI. Comment tester la robustesse ?

Le principe est simple.

On modifie volontairement les données.

Puis on observe les résultats.

Exemple :

Image normale

↓

Image légèrement floue

↓

Image très floue

↓

Image très sombre

↓

Image avec bruit

À chaque étape :

on mesure la précision.

---

# VII. Les indicateurs de robustesse

Le cours présente quatre indicateurs principaux. 

## 1. Variance

Définition :

La variation des performances selon les scénarios.

Faible variance :

→ modèle stable.

Grande variance :

→ modèle fragile.

---

## 2. Courbe de dégradation

Définition :

Graphique montrant la baisse des performances lorsque les perturbations augmentent.

Exemple :

Aucune perturbation :

95 %

Peu de bruit :

93 %

Beaucoup de bruit :

88 %

Énormément de bruit :

40 %

La courbe montre à quel moment le modèle « s'effondre ».

---

## 3. Robustesse relative

Définition :

Comparaison entre la performance normale et la performance perturbée.

Formule :

Robustesse relative = Performance perturbée / Performance normale

Exemple :

Performance normale :

100 %

Performance perturbée :

80 %

Robustesse relative :

80 %

---

## 4. Sensibilité moyenne

Définition :

Mesure de la vitesse à laquelle les performances diminuent lorsque les perturbations augmentent.

Plus la sensibilité est élevée,

plus le modèle est fragile.

---

# VIII. Les tests simulés et réels

Le cours distingue deux approches.

## Tests simulés

On crée artificiellement des perturbations.

Exemple :

On ajoute du bruit sur une image.

Avantages :

* rapides
* peu coûteux
* nombreux scénarios

---

## Tests réels

On teste le modèle avec de vraies données.

Exemple :

Vraies photos prises sur le terrain.

Le cours explique qu'il faut combiner les deux méthodes, car certaines situations réelles ne peuvent pas être reproduites parfaitement en simulation. 

---

# IX. Les attaques contre une IA

La deuxième moitié du cours parle de sécurité.

Ici, le problème n'est plus :

"L'IA résiste-t-elle aux erreurs ?"

mais

"Peut-on volontairement la tromper ?"

---

# X. Les attaques adversariales

Définition :

Une attaque adversariale consiste à modifier très légèrement une donnée pour tromper volontairement l'IA. 

L'humain ne voit presque rien.

Mais l'IA se trompe complètement.

Exemple célèbre :

Un panneau STOP.

Quelques pixels sont modifiés.

L'humain lit toujours "STOP".

L'IA croit lire "80 km/h".

C'est extrêmement dangereux.

---

# XI. Les autres attaques

## 1. Data Poisoning

Définition :

Injection de mauvaises données pendant l'entraînement. 

Objectif :

Fausser le comportement futur du modèle.

Exemple :

On ajoute volontairement des images mal étiquetées.

Le modèle apprend de mauvaises choses.

---

## 2. Inversion de modèle

Définition :

Retrouver des informations confidentielles à partir des réponses du modèle. 

Exemple :

Le modèle médical révèle indirectement des données de patients.

---

## 3. Extraction de modèle

Définition :

Copier un modèle propriétaire en lui posant énormément de questions. 

L'attaquant recrée progressivement le fonctionnement du modèle.

---

# XII. Comment protéger une IA ?

Le cours propose plusieurs stratégies.

## Entraînement adversarial

On entraîne le modèle avec des données volontairement perturbées.

Ainsi, il apprend à résister.

---

## Filtrage des entrées

Avant que les données arrivent au modèle :

on vérifie qu'elles ne sont pas suspectes.

---

## Normalisation renforcée

On standardise les données.

Exemple :

Toutes les images ont :

* la même taille
* le même contraste
* la même orientation

Ainsi, les variations gênent moins le modèle.

---

## Sécuriser tout le pipeline IA

Il ne faut pas protéger uniquement le modèle.

Il faut aussi sécuriser :

* les données
* les accès
* les API
* le stockage
* le chiffrement
* la journalisation
* les mises à jour

On parle de **sécurisation de bout en bout** (end-to-end). 

---

# XIII. La surveillance continue

Une IA n'est jamais définitivement sécurisée.

Pourquoi ?

Parce que :

* les données évoluent ;
* de nouvelles attaques apparaissent ;
* le modèle est mis à jour.

Il faut donc :

* surveiller les performances ;
* détecter les anomalies ;
* faire des audits réguliers ;
* réévaluer la robustesse après chaque mise à jour. 

---

# Tableau récapitulatif des définitions à connaître

| Terme                         | Définition simple                                                                                       |
| ----------------------------- | ------------------------------------------------------------------------------------------------------- |
| **Robustesse**                | Capacité d'un modèle à conserver de bonnes performances malgré des perturbations.                       |
| **Performance**               | Résultat obtenu dans des conditions idéales.                                                            |
| **OOD (Out Of Distribution)** | Données très différentes de celles vues pendant l'entraînement.                                         |
| **Perturbation**              | Modification volontaire des données pour tester la résistance du modèle.                                |
| **Variance**                  | Variation des performances entre plusieurs scénarios de test.                                           |
| **Courbe de dégradation**     | Évolution des performances lorsque les perturbations augmentent.                                        |
| **Robustesse relative**       | Rapport entre la performance perturbée et la performance normale.                                       |
| **Sensibilité moyenne**       | Vitesse à laquelle les performances diminuent face aux perturbations.                                   |
| **Attaque adversariale**      | Modification presque invisible des données pour tromper le modèle.                                      |
| **Data poisoning**            | Injection de données malveillantes pendant l'entraînement.                                              |
| **Inversion de modèle**       | Tentative de retrouver les données d'origine grâce aux réponses du modèle.                              |
| **Extraction de modèle**      | Tentative de copier un modèle en l'interrogeant de nombreuses fois.                                     |
| **Entraînement adversarial**  | Entraîner le modèle avec des exemples perturbés pour le rendre plus résistant.                          |
| **Filtrage d'entrée**         | Vérification des données avant leur traitement par le modèle.                                           |
| **Pipeline IA**               | Ensemble des étapes d'un système IA : collecte, entraînement, déploiement, utilisation et surveillance. |

---

# Les 10 points essentiels à retenir pour un examen

1. **Performance ≠ Robustesse** : un modèle performant n'est pas forcément robuste.
2. **La robustesse** mesure la capacité d'un modèle à résister aux perturbations.
3. Il faut tester le modèle avec du **bruit**, des **déformations**, des **données incomplètes**, des **valeurs extrêmes** et des **données OOD**.
4. Les principaux indicateurs sont : **variance**, **courbe de dégradation**, **robustesse relative** et **sensibilité moyenne**.
5. Les **tests simulés** sont utiles mais doivent être complétés par des **tests en conditions réelles**.
6. Une **attaque adversariale** modifie très légèrement une entrée pour tromper l'IA.
7. Le **data poisoning** attaque la phase d'entraînement en injectant des données malveillantes.
8. L'**inversion de modèle** cherche à retrouver des données sensibles et l'**extraction de modèle** vise à copier un modèle.
9. Les meilleures défenses sont **l'entraînement adversarial**, le **filtrage des entrées**, la **normalisation renforcée** et une **défense multicouche**.
10. La sécurité d'un modèle IA est un **processus continu** : surveillance, audits et réévaluation sont indispensables après le déploiement.
