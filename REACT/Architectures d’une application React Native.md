
---

# Synthèse — Architectures d’une application React Native

## Pourquoi une bonne architecture est importante ?

Dans une application React Native, l’architecture sert à :

* rendre le code **maintenable**
* faciliter le travail en équipe
* améliorer la **scalabilité**
* réduire les erreurs
* organiser clairement les responsabilités

React Native utilise une approche orientée **composants**, contrairement aux architectures web plus classiques séparant fortement frontend/backend.

Le cours présente principalement deux architectures :

1. **Feature-based**
2. **Layer-based**

---

# 1. Architecture Feature-Based

## Principe

L’organisation du projet est centrée sur les **fonctionnalités métier**.

Chaque fonctionnalité possède son propre dossier contenant :

* composants
* logique métier
* styles
* modèles
* contrôleurs
* hooks éventuels

👉 On regroupe tout ce qui concerne une fonctionnalité au même endroit.

---

## Exemple de structure

```txt
/src
  /features
    /Panier
      PanierView.js
      PanierController.js
      PanierModel.js

    /ListeDeProduits
      ListeDeProduitsView.js
      ListeDeProduitsController.js
      ListeDeProduitsModel.js

  /components
    /Button
    /Header

  /shared
    /utils
    /hooks
    /api
```

---

## Fonctionnement

Exemple avec `ListeDeProduits` :

### Model

Contient :

* données
* logique métier
* appels API
* manipulation des produits

Exemple :

```js
addProduct()
deleteProduct()
getProducts()
```

---

### View

Contient :

* affichage UI
* JSX
* rendu des listes

Exemple :

```jsx
<ProductCard />
```

---

### Controller

Fait le lien entre :

* la vue
* le modèle

Il traite :

* les actions utilisateur
* les événements
* les mises à jour du state

---

# Avantages du Feature-Based

## ✅ Points forts

### Cohésion

Tout le code d’une feature est regroupé.

### Très pratique pour les grosses équipes

Chaque équipe peut travailler sur une feature différente.

### Scalabilité

Ajouter une fonctionnalité = ajouter un dossier.

### Lisibilité métier

On comprend rapidement :

* où est le code
* quelle feature il concerne

---

## ❌ Inconvénients

### Duplication possible

Plusieurs features peuvent répéter certaines logiques.

### Complexité sur très gros projets

Quand il y a énormément de features :

* navigation plus difficile
* dépendances plus complexes

---

# 2. Architecture Layer-Based (architecture en couches)

## Principe

Le projet est organisé selon les **responsabilités techniques**.

Chaque couche a un rôle précis.

---

## Structure typique

```txt
/src
  /presentation
    /components
    /views

  /businessLogic
    /services
    /controllers
    /rules

  /dataAccess
    /models
    /repositories
    /database
```

---

# Les différentes couches

## 1. Présentation

Contient :

* UI
* écrans
* composants React Native
* styles

Rôle :
➡️ afficher les données

---

## 2. Business Logic

Contient :

* logique métier
* règles de validation
* traitements

Rôle :
➡️ prendre les décisions

Exemples :

* validation formulaire
* calculs métier
* gestion panier

---

## 3. Data Access

Contient :

* accès API
* base de données
* repositories

Rôle :
➡️ récupérer/stocker les données

---

# Communication entre couches

Une couche communique uniquement avec :

* la couche juste au-dessus
* ou juste en dessous

Exemple :

```txt
Présentation
    ↓
Business Logic
    ↓
Data Access
```

---

# Avantages du Layer-Based

## ✅ Points forts

### Séparation claire des responsabilités

Chaque couche a un rôle unique.

### Maintenance facilitée

Modifier la base de données impacte peu l’UI.

### Réutilisation plus simple

Les services métier peuvent être réutilisés.

---

## ❌ Inconvénients

### Navigation plus compliquée

Pour modifier une feature :

* il faut parcourir plusieurs couches

### Plus rigide

Certaines évolutions sont moins naturelles.

---

# Comparaison rapide

| Feature-Based                             | Layer-Based                                 |
| ----------------------------------------- | ------------------------------------------- |
| Organisation par fonctionnalités          | Organisation par responsabilités techniques |
| Très adapté au frontend moderne           | Très utilisé dans architectures classiques  |
| Facile pour travailler par équipe feature | Bonne séparation technique                  |
| Plus intuitif côté métier                 | Plus rigoureux techniquement                |
| Peut créer des duplications               | Peut devenir rigide                         |

---

# Quel choix utiliser ?

## Utiliser Feature-Based si :

* application React Native moderne
* équipe frontend importante
* développement rapide
* nombreuses fonctionnalités indépendantes

👉 C’est souvent le choix préféré en React Native.

---

## Utiliser Layer-Based si :

* logique métier complexe
* architecture très stricte
* gros système technique
* forte séparation des responsabilités

---

# Ce qu’il faut retenir

## Architecture Feature-Based

➡️ Organisation par fonctionnalités métier.

Très adaptée à React Native.

---

## Architecture Layer-Based

➡️ Organisation par couches techniques.

Très bonne séparation des responsabilités.

---

## MVC dans React Native

Le cours montre aussi que certaines features peuvent utiliser le pattern MVC :

* **Model** → données + logique
* **View** → interface utilisateur
* **Controller** → interactions et coordination

---

# Conclusion importante du cours

Une bonne architecture permet :

* une meilleure qualité du code
* une maintenance plus simple
* un travail d’équipe efficace
* une application évolutive

Et elle doit être accompagnée d’outils de qualité :

* ESLint
* Prettier
* SonarLint
* JSDoc
* Git
