
# Les composants React Native — version simplifiée

## 1. C’est quoi un composant ?

Un composant = un morceau d’interface réutilisable.

Par exemple :

* un bouton
* une carte produit
* un menu
* un texte
* une image

En React Native, toute l’application est construite avec des composants.

---

## 2. Les composants de base de React Native

Les plus utilisés :

| Composant | Sert à quoi                 |
| --------- | --------------------------- |
| `View`    | conteneur (comme une boîte) |
| `Text`    | afficher du texte           |
| `Image`   | afficher une image          |
| `Button`  | afficher un bouton          |

Exemple :

```jsx
import { View, Text } from 'react-native';

export default function App() {
  return (
    <View>
      <Text>Bonjour</Text>
    </View>
  );
}
```

Ici :

* `View` contient les éléments
* `Text` affiche le texte

---

# 3. JSX : la syntaxe bizarre avec les balises

Le JSX ressemble au HTML.

Exemple :

```jsx
<Text>Bonjour</Text>
```

ou

```jsx
<View>
  <Text>Salut</Text>
</View>
```

Mais derrière, c’est du JavaScript.

Le JSX sert juste à écrire l’interface plus facilement.

---

# 4. Parent / enfant

Quand un composant contient un autre composant :

```jsx
<View>
  <Text>Bonjour</Text>
</View>
```

Alors :

* `View` = parent
* `Text` = enfant

C’est exactement comme des boîtes imbriquées.

---

# 5. Les 2 façons de créer un composant

## A. Avec une fonction (la méthode moderne)

C’est la méthode la plus utilisée aujourd’hui.

```jsx
function Bonjour() {
  return <Text>Salut</Text>;
}
```

Puis on l’utilise comme ça :

```jsx
<Bonjour />
```

---

## B. Avec une classe (ancienne méthode)

```jsx
class Bonjour extends React.Component {
  render() {
    return <Text>Salut</Text>;
  }
}
```

Aujourd’hui :
👉 on préfère presque toujours les composants fonctionnels.

---

# 6. useState : stocker des données

Le hook `useState` permet de stocker une valeur.

Exemple :

```jsx
const [name, setName] = React.useState("Jean");
```

Ici :

* `name` = valeur actuelle
* `setName` = fonction pour modifier la valeur

---

## Exemple complet

```jsx
export default function App() {
  const [name, setName] = React.useState("Jean");

  return (
    <Text>Bonjour {name}</Text>
  );
}
```

Affiche :

```txt
Bonjour Jean
```

---

# 7. Le cycle de vie d’un composant

Un composant a plusieurs étapes de vie :

| Étape       | Signification         |
| ----------- | --------------------- |
| Montage     | le composant apparaît |
| Mise à jour | il change             |
| Démontage   | il disparaît          |

---

# 8. useEffect : réagir au cycle de vie

Le hook le plus important : `useEffect`.

Syntaxe :

```jsx
React.useEffect(() => {

}, []);
```

---

## A. Exécuter du code au démarrage

```jsx
React.useEffect(() => {
  console.log("Le composant apparaît");
}, []);
```

Le `[]` signifie :
👉 “fais-le une seule fois”.

---

## B. Exécuter du code quand le composant disparaît

```jsx
React.useEffect(() => {
  console.log("Apparition");

  return () => {
    console.log("Disparition");
  };
}, []);
```

Le `return` sert au nettoyage.

---

# 9. Exemple simple avec apparition/disparition

```jsx
function Coucou() {

  React.useEffect(() => {

    console.log("Je suis apparu");

    return () => {
      console.log("Je disparais");
    };

  }, []);

  return <Text>Coucou</Text>;
}
```

---

# 10. Fetch : récupérer des données d’une API

Exemple :

```jsx
React.useEffect(() => {

  fetch("https://jsonplaceholder.typicode.com/posts/1")
    .then((response) => response.json())
    .then((json) => console.log(json));

}, []);
```

---

## Ce qui se passe

### 1. `fetch(...)`

Envoie une requête internet.

---

### 2. `.then(...)`

Attend la réponse.

---

### 3. `response.json()`

Transforme la réponse en objet JavaScript.

---

### 4. `console.log(json)`

Affiche les données.

---

# 11. Les choses importantes à retenir

## JSX

Permet d’écrire l’interface avec des balises.

---

## View

Conteneur principal.

---

## Text

Affiche du texte.

---

## Composant

Bloc réutilisable.

---

## useState

Stocke des données.

---

## useEffect

Permet :

* de lancer du code au démarrage
* réagir aux changements
* nettoyer quand le composant disparaît

---

# 12. Différence importante

## Composant fonctionnel

```jsx
function App() {}
```

👉 moderne
👉 utilise les hooks

---

## Composant classe

```jsx
class App extends React.Component {}
```

👉 ancienne méthode

---

# 13. Petit résumé ultra-court

React Native fonctionne comme des LEGO :

* chaque composant = une pièce
* `View` = boîte
* `Text` = texte
* JSX = syntaxe avec balises
* `useState` = mémoire
* `useEffect` = actions automatiques

---

# Exemple final simple

```jsx
import * as React from 'react';
import { View, Text, Button } from 'react-native';

export default function App() {

  const [show, setShow] = React.useState(true);

  return (
    <View>

      <Button
        title="Changer"
        onPress={() => setShow(!show)}
      />

      {show ? <Text>Bonjour</Text> : null}

    </View>
  );
}
```

Ce code :

* affiche un bouton
* affiche “Bonjour”
* cache/affiche le texte quand on clique
