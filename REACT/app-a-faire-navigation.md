# Cours complet — React Navigation avec Tabs + Stack

On va construire une vraie architecture moderne React Native étape par étape.

Le but :

```txt id="y6nnn0"
Tabs
├── Accueil
│    └── Détails produit
├── Recherche
└── Profil
```

Cette architecture est utilisée dans énormément d’apps réelles.

---

# 1. Comprendre le problème

Dans une application web :

* le navigateur gère les pages,
* les URLs changent,
* l’historique existe déjà.

Exemple :

```txt id="c3on0w"
/home
/products
/profile
```

---

En React Native :

* il n’y a pas de navigateur web,
* pas d’URL par défaut,
* pas de système de pages.

Donc :
👉 React Navigation crée un système de navigation artificiel.

---

# 2. Les 3 concepts fondamentaux

## A. NavigationContainer

Le cerveau de la navigation.

Il :

* stocke l’historique,
* sait quel écran est affiché,
* gère les transitions.

---

## B. Navigator

Le système de navigation lui-même.

Exemples :

* Stack Navigator
* Bottom Tabs Navigator
* Drawer Navigator

---

## C. Screen

Un écran affiché dans l’application.

Exemple :

```jsx id="m9u3dr"
function HomeScreen() {
  return <Text>Accueil</Text>;
}
```

---

# 3. Les deux types de navigation qu’on va utiliser

---

# Stack Navigator

Fonctionne comme une pile.

```txt id="m5u3dg"
Home
  ↓
Details
  ↓
Payment
```

Quand on revient :

* le dernier écran disparaît.

👉 exactement comme l’historique du navigateur.

---

# Bottom Tabs Navigator

Navigation par onglets.

```txt id="w2uh1z"
Accueil | Recherche | Profil
```

Chaque onglet possède souvent sa propre stack.

C’est extrêmement important à comprendre.

---

# 4. Architecture finale

Notre app :

```txt id="2djbx3"
NavigationContainer
└── Tabs
    ├── Home Stack
    │   ├── HomeScreen
    │   └── DetailsScreen
    │
    ├── SearchScreen
    │
    └── ProfileScreen
```

---

# 5. Installation

## Création du projet

```bash id="v6z2t0"
npx create-expo-app my-navigation-app
```

Puis :

```bash id="yw2l3o"
cd my-navigation-app
```

---

# 6. Installer React Navigation

## Core

```bash id="4v5s74"
npx expo install @react-navigation/native
```

C’est la base de React Navigation.

---

## Dépendances natives

```bash id="y9s2pd"
npx expo install react-native-screens react-native-safe-area-context
```

### react-native-screens

Optimise les performances des écrans.

---

### react-native-safe-area-context

Gère les zones iPhone :

* notch,
* Dynamic Island,
* bordures.

---

# 7. Installer les navigateurs

## Stack moderne

```bash id="1cfu3e"
npm install @react-navigation/native-stack
```

---

## Bottom Tabs

```bash id="1qhv5z"
npm install @react-navigation/bottom-tabs
```

---

# 8. Organisation moderne du projet

On évite les énormes fichiers.

Bonne pratique :

```txt id="9h1r8i"
src/
 ├── navigation/
 ├── screens/
 └── components/
```

---

# 9. Créer App.js

## Pourquoi ?

C’est le point d’entrée.

---

## Code

```jsx id="y0kjv6"
import { NavigationContainer } from '@react-navigation/native';
import TabNavigator from './src/navigation/TabNavigator';

export default function App() {
  return (
    <NavigationContainer>
      <TabNavigator />
    </NavigationContainer>
  );
}
```

---

# 10. Comprendre NavigationContainer

```jsx id="8qq1iw"
<NavigationContainer>
```

Ce composant :

* mémorise la navigation,
* transmet le contexte,
* permet d’utiliser :

  * `navigation`
  * `route`
  * les hooks.

Sans lui :
❌ React Navigation ne fonctionne pas.

---

# 11. Créer le système Tabs

Créer :

```txt id="ukb9lb"
src/navigation/TabNavigator.js
```

---

# 12. Le Bottom Tab Navigator

## Code complet

```jsx id="dzzd7x"
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';

import HomeStack from './HomeStack';

import SearchScreen from '../screens/SearchScreen';
import ProfileScreen from '../screens/ProfileScreen';

const Tab = createBottomTabNavigator();

export default function TabNavigator() {
  return (
    <Tab.Navigator>
      <Tab.Screen
        name="HomeTab"
        component={HomeStack}
        options={{
          title: 'Accueil',
        }}
      />

      <Tab.Screen
        name="Search"
        component={SearchScreen}
        options={{
          title: 'Recherche',
        }}
      />

      <Tab.Screen
        name="Profile"
        component={ProfileScreen}
        options={{
          title: 'Profil',
        }}
      />
    </Tab.Navigator>
  );
}
```

---

# 13. Comprendre createBottomTabNavigator

```jsx id="n9w70n"
const Tab = createBottomTabNavigator();
```

Crée un objet contenant :

* `Tab.Navigator`
* `Tab.Screen`

---

# 14. Comprendre Tab.Navigator

```jsx id="ozujgx"
<Tab.Navigator>
```

C’est le conteneur des onglets.

Il :

* affiche la barre du bas,
* gère le changement d’onglet,
* garde les états des écrans.

---

# 15. Comprendre Tab.Screen

```jsx id="f6k1f5"
<Tab.Screen
  name="Search"
  component={SearchScreen}
/>
```

On déclare :

* le nom de route,
* le composant affiché.

---

# 16. Point TRÈS important

Regarde :

```jsx id="m4q4c9"
component={HomeStack}
```

Ce n’est PAS un écran.

C’est :
👉 un autre navigator.

Donc :

* un navigator peut contenir un navigator.

C’est le principe du nesting.

---

# 17. Pourquoi imbriquer les navigateurs ?

Parce qu’on veut :

```txt id="6qrr3u"
Accueil
  ↓
Détails produit
```

SANS perdre :

* les tabs du bas,
* l’état des autres onglets.

---

# 18. Création du Stack Home

Créer :

```txt id="4bd3to"
src/navigation/HomeStack.js
```

---

# 19. Code du Stack

```jsx id="9a1qpn"
import { createNativeStackNavigator } from '@react-navigation/native-stack';

import HomeScreen from '../screens/HomeScreen';
import DetailsScreen from '../screens/DetailsScreen';

const Stack = createNativeStackNavigator();

export default function HomeStack() {
  return (
    <Stack.Navigator>
      <Stack.Screen
        name="HomeMain"
        component={HomeScreen}
      />

      <Stack.Screen
        name="Details"
        component={DetailsScreen}
      />
    </Stack.Navigator>
  );
}
```

---

# 20. Comprendre le Stack

Le stack :

* empile les écrans,
* anime les transitions,
* gère le bouton retour.

---

# 21. Pourquoi Native Stack ?

Ancienne API :

```jsx id="rl20l9"
@react-navigation/stack
```

Nouvelle API recommandée :

```jsx id="vymq7z"
@react-navigation/native-stack
```

Pourquoi ?

* plus rapide,
* utilise les transitions natives,
* meilleures performances.

---

# 22. Créer HomeScreen

Créer :

```txt id="ijr2cg"
src/screens/HomeScreen.js
```

---

# 23. Code HomeScreen

```jsx id="l2z76r"
import {
  View,
  Text,
  TouchableOpacity,
} from 'react-native';

const PRODUCTS = [
  { id: 1, name: 'iPhone' },
  { id: 2, name: 'MacBook' },
];

export default function HomeScreen({ navigation }) {
  return (
    <View>
      <Text>Produits</Text>

      {PRODUCTS.map((product) => (
        <TouchableOpacity
          key={product.id}
          onPress={() =>
            navigation.navigate('Details', {
              product,
            })
          }
        >
          <Text>{product.name}</Text>
        </TouchableOpacity>
      ))}
    </View>
  );
}
```

---

# 24. Comprendre navigation

Le screen reçoit automatiquement :

```jsx id="z9n01v"
{ navigation }
```

C’est une prop injectée par React Navigation.

---

# 25. navigation.navigate()

```jsx id="9f7qjq"
navigation.navigate('Details')
```

Permet :
👉 d’aller vers un autre écran.

---

# 26. Passer des paramètres

```jsx id="g9pc2n"
navigation.navigate('Details', {
  product,
})
```

Le second argument devient :

```jsx id="7zow4m"
route.params
```

dans l’écran cible.

---

# 27. Créer DetailsScreen

Créer :

```txt id="z4udx9"
src/screens/DetailsScreen.js
```

---

# 28. Code DetailsScreen

```jsx id="0l4o3r"
import {
  View,
  Text,
  Button,
} from 'react-native';

export default function DetailsScreen({
  route,
  navigation,
}) {
  const { product } = route.params;

  return (
    <View>
      <Text>{product.name}</Text>

      <Button
        title="Retour"
        onPress={() => navigation.goBack()}
      />
    </View>
  );
}
```

---

# 29. Comprendre route.params

```jsx id="8otfvi"
const { product } = route.params;
```

On récupère :

* les paramètres envoyés,
* depuis navigate().

---

# 30. navigation.goBack()

```jsx id="d8u6n6"
navigation.goBack()
```

Retire l’écran du dessus dans la stack.

---

# 31. Comprendre la pile

Avant :

```txt id="nifh9r"
Home
```

Après :

```txt id="lr9q14"
Home
Details
```

Puis :

```jsx id="7on9r8"
goBack()
```

revient à :

```txt id="qjlwm2"
Home
```

---

# 32. Ajouter SearchScreen

```jsx id="f6m3ma"
import { View, Text } from 'react-native';

export default function SearchScreen() {
  return (
    <View>
      <Text>Recherche</Text>
    </View>
  );
}
```

---

# 33. Ajouter ProfileScreen

```jsx id="s1fvhz"
import { View, Text } from 'react-native';

export default function ProfileScreen() {
  return (
    <View>
      <Text>Profil</Text>
    </View>
  );
}
```

---

# 34. Ce qu’il faut retenir

## NavigationContainer

Le cerveau.

---

## Tabs

Navigation principale.

---

## Stack

Navigation interne.

---

## Screen

Composant affiché.

---

## navigate()

Aller vers un écran.

---

## goBack()

Retour arrière.

---

## route.params

Récupérer les paramètres.

---

# 35. Architecture réelle utilisée en entreprise

Très souvent :

```txt id="2xq5a5"
Auth Stack
    ↓
Main Tabs
    ↓
Nested Stacks
```

Exemple :

```txt id="1mlik4"
Tabs
├── Feed Stack
├── Search Stack
├── Messages Stack
└── Profile Stack
```

---

# 36. Ce que tu peux apprendre ensuite

## Drawer Navigation

Menu latéral.

---

## Deep Linking

Ouvrir un écran via URL.

---

## Protected Routes

Accès selon login.

---

## TypeScript Navigation

Très utilisé en entreprise.

---

# 37. Documentation officielle

* [React Navigation](https://reactnavigation.org?utm_source=chatgpt.com)
* [Bottom Tabs](https://reactnavigation.org/docs/bottom-tab-navigator?utm_source=chatgpt.com)
* [Native Stack](https://reactnavigation.org/docs/native-stack-navigator?utm_source=chatgpt.com)
