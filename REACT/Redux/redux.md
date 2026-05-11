Redux est une bibliothèque JavaScript utilisée pour gérer l’état (“state”) d’une application, surtout dans les applications front-end comme React.

L’idée principale de Redux est simple :

> **Avoir une seule source de vérité pour les données de l’application, avec des règles très strictes pour les modifier.**

---

# Pourquoi Redux existe ?

Imaginons une application e-commerce :

* un panier
* un utilisateur connecté
* des produits favoris
* des filtres de recherche
* des notifications

Quand l’application grossit, ces données doivent être accessibles depuis plusieurs composants différents.

Sans organisation :

* les données se dupliquent
* les composants se passent des props partout
* les bugs deviennent fréquents
* on ne sait plus “qui modifie quoi”

Redux apporte :

* un stockage centralisé
* des modifications prévisibles
* un historique clair des changements

---

# L’analogie du supermarché

Imagine :

## Le Store = l’entrepôt central

Toutes les données de l’application sont stockées à un seul endroit.

Exemple :

```js
{
  user: { name: "Alice" },
  cart: ["Livre", "Clavier"],
  darkMode: true
}
```

---

## Les Components = les clients

Les composants React viennent :

* lire les données
* demander des modifications

Mais ils ne modifient jamais directement le stock.

---

## Les Actions = les formulaires de demande

Un composant dit :

```js
{
  type: "ADD_TO_CART",
  payload: "Souris"
}
```

C’est juste une description de ce qu’on veut faire.

---

## Les Reducers = les employés de l’entrepôt

Le reducer reçoit :

* l’état actuel
* l’action

Puis il décide du nouvel état.

Exemple :

```js
function cartReducer(state = [], action) {
  switch(action.type) {
    case "ADD_TO_CART":
      return [...state, action.payload]

    default:
      return state
  }
}
```

---

# Le flux Redux (TRÈS important)

Redux fonctionne toujours dans le même sens :

```text
Component
   ↓
dispatch(action)
   ↓
Reducer
   ↓
Nouveau state
   ↓
Interface mise à jour
```

C’est ce qu’on appelle un **flux unidirectionnel**.

---

# Les 3 principes fondamentaux

## 1. Single Source of Truth

Un seul store central.

```text
Toute l’application → un seul état global
```

---

## 2. State en lecture seule

On ne modifie jamais directement le state.

❌ Mauvais :

```js
state.cart.push("Livre")
```

✅ Correct :

```js
return [...state, "Livre"]
```

Redux adore l’immutabilité.

---

## 3. Modifications prévisibles

Toutes les modifications passent par :

* une action
* un reducer

Donc tout devient traçable.

---

# Exemple complet ultra simple

## Création du store

```js
import { createStore } from "redux"
```

---

## Reducer

```js
function counterReducer(state = 0, action) {

  switch(action.type) {

    case "INCREMENT":
      return state + 1

    case "DECREMENT":
      return state - 1

    default:
      return state
  }
}
```

---

## Store

```js
const store = createStore(counterReducer)
```

---

## Lire le state

```js
console.log(store.getState())
```

---

## Envoyer une action

```js
store.dispatch({ type: "INCREMENT" })
```

Résultat :

```js
1
```

---

# Avec React : comment ça se connecte ?

On utilise généralement :

* React Redux
* parfois Redux Toolkit (recommandé aujourd’hui)

---

## Hook useSelector

Pour lire le state :

```js
const count = useSelector(state => state.counter)
```

---

## Hook useDispatch

Pour envoyer une action :

```js
dispatch({ type: "INCREMENT" })
```

---

# Redux Toolkit (la version moderne)

Aujourd’hui, on utilise surtout :

Redux Toolkit

Parce que le Redux “historique” était très verbeux.

Redux Toolkit simplifie énormément :

Avant :

* actions séparées
* constantes
* switch
* boilerplate énorme

Maintenant :

```js
const counterSlice = createSlice({
  name: "counter",

  initialState: 0,

  reducers: {
    increment: state => state + 1,
    decrement: state => state - 1
  }
})
```

---

# Quand utiliser Redux ?

Redux est utile quand :

✅ Beaucoup de données globales
✅ Beaucoup de composants partagent les mêmes données
✅ Application complexe
✅ Besoin de debugging avancé
✅ État métier important

Exemples :

* dashboards
* SaaS
* e-commerce
* outils collaboratifs
* applications temps réel

---

# Quand Redux est excessif

Pour une petite app :

* formulaire
* todo simple
* mini portfolio

Redux peut être trop lourd.

Aujourd’hui beaucoup d’apps utilisent :

* Context API
* Zustand
* Jotai
* TanStack Query

à la place.

---

# La différence importante : local state vs global state

## Local state

```js
const [open, setOpen] = useState(false)
```

Utilisé seulement dans UN composant.

---

## Global state (Redux)

```js
user connecté
panier
thème
permissions
cache global
```

Accessible partout.

---

# Pourquoi le nom “Reducer” ?

Le terme vient de la programmation fonctionnelle :

```js
array.reduce(...)
```

Un reducer :

* prend un état précédent
* applique une opération
* retourne un nouvel état

Comme :

```js
nouvelEtat = reducer(ancienEtat, action)
```

---

# Ce qu’il faut retenir

Redux =

✅ un store central
✅ des actions pour décrire les changements
✅ des reducers pour modifier l’état
✅ un flux unidirectionnel
✅ des changements prévisibles et traçables

---

# Vision mentale simple

```text
STORE = base de données frontend

ACTION = demande de changement

REDUCER = logique métier

DISPATCH = envoyer la demande
```

---

# Pour apprendre Redux intelligemment

Ordre recommandé :

1. Comprendre :

   * state
   * props
   * useState

2. Comprendre :

   * immutabilité

3. Comprendre :

   * flux de données React

4. Puis :

   * Redux Toolkit
   * slices
   * async thunks

---

# Petit schéma final

```text
[UI]
  ↓ clique
dispatch(action)
  ↓
[Reducer]
  ↓
nouveau state
  ↓
[Store]
  ↓
UI re-render
```

