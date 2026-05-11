Oui 👍
Le PDF utilise une ancienne API de React Navigation (`@react-navigation/stack`) et certaines pratiques ne sont plus recommandées aujourd’hui.

Je vais te faire un **cours moderne React Navigation v7 + Expo SDK récent**, avec :

* les concepts importants,
* les différences avec l’ancien cours,
* les bonnes pratiques actuelles,
* une mini app complète à tester.

---

# Cours moderne — Navigation avec React Native

## 1. Pourquoi React Navigation ?

En React web, la navigation se base sur les URLs.

En React Native :

* il n’y a pas de navigateur web,
* donc pas de routes URL “naturelles”,
* il faut gérer un état de navigation.

La librairie principale aujourd’hui est :

[React Navigation](https://reactnavigation.org?utm_source=chatgpt.com)

---

# 2. Architecture moderne

Aujourd’hui, une app React Native ressemble souvent à ça :

```txt
NavigationContainer
└── Stack Navigator
    ├── HomeScreen
    ├── DetailsScreen
    └── ProfileScreen
```

---

# 3. Installation moderne (Expo)

## Nouveau système recommandé

Avec Expo :

```bash
npx expo install @react-navigation/native
npx expo install react-native-screens react-native-safe-area-context
npm install @react-navigation/native-stack
```

### Différence avec ton PDF

Le PDF utilise :

```bash
@react-navigation/stack
```

Aujourd’hui on préfère :

```bash
@react-navigation/native-stack
```

Pourquoi ?

* plus rapide,
* animations natives,
* meilleures performances,
* recommandé officiellement.

---

# 4. NavigationContainer

C’est le composant racine.

```jsx
import { NavigationContainer } from '@react-navigation/native';

export default function App() {
  return (
    <NavigationContainer>
      {/* navigateurs */}
    </NavigationContainer>
  );
}
```

Il contient :

* l’historique,
* l’état de navigation,
* les routes actives.

---

# 5. Créer un Stack Navigator

## API moderne

```jsx
import { createNativeStackNavigator } from '@react-navigation/native-stack';

const Stack = createNativeStackNavigator();
```

Puis :

```jsx
<Stack.Navigator>
  <Stack.Screen name="Home" component={HomeScreen} />
  <Stack.Screen name="Details" component={DetailsScreen} />
</Stack.Navigator>
```

---

# 6. Créer un écran

Un écran est juste un composant React.

```jsx
function HomeScreen() {
  return (
    <View>
      <Text>Accueil</Text>
    </View>
  );
}
```

---

# 7. Naviguer entre les écrans

## Avec `navigation.navigate`

```jsx
navigation.navigate('Details');
```

Exemple :

```jsx
<Button
  title="Voir les détails"
  onPress={() => navigation.navigate('Details')}
/>
```

---

# 8. Revenir en arrière

```jsx
navigation.goBack();
```

---

# 9. Passer des paramètres

## Envoi

```jsx
navigation.navigate('Details', {
  productId: 12,
});
```

## Réception

```jsx
function DetailsScreen({ route }) {
  const { productId } = route.params;

  return <Text>ID : {productId}</Text>;
}
```

---

# 10. navigate VS push

## navigate

Va vers un écran existant si déjà présent.

```jsx
navigation.navigate('Details')
```

## push

Ajoute TOUJOURS une nouvelle instance.

```jsx
navigation.push('Details')
```

Très utile pour :

* fiches produits,
* discussions,
* navigation récursive.

---

# 11. Personnaliser le header

## Titre

```jsx
<Stack.Screen
  name="Home"
  component={HomeScreen}
  options={{
    title: 'Accueil',
  }}
/>
```

---

## Style global

```jsx
<Stack.Navigator
  screenOptions={{
    headerStyle: {
      backgroundColor: '#222',
    },
    headerTintColor: '#fff',
  }}
>
```

---

# 12. Hook modernes

Aujourd’hui on utilise énormément les hooks.

## useNavigation

```jsx
import { useNavigation } from '@react-navigation/native';
```

## useRoute

```jsx
import { useRoute } from '@react-navigation/native';
```

---

# 13. Bonnes pratiques modernes

## ✅ Séparer les écrans

```txt
src/
 ├── screens/
 ├── navigation/
 ├── components/
```

---

## ✅ Utiliser TypeScript

Très recommandé avec React Navigation.

---

## ✅ Éviter les grosses stacks

Créer plusieurs navigateurs :

* Auth stack,
* Main stack,
* Tabs,
* Modals.

---

# 14. Nouveautés importantes par rapport au PDF

## ❌ Ancien

```jsx
@react-navigation/stack
```

## ✅ Moderne

```jsx
@react-navigation/native-stack
```

---

## ❌ Ancienne approche

Navigation dans un seul fichier énorme.

## ✅ Moderne

Architecture modulaire :

* `/screens`
* `/navigation`
* `/components`

---

## ❌ Ancien

Composants classe + props partout.

## ✅ Moderne

Hooks :

* `useNavigation`
* `useRoute`

---

# 15. Mini application moderne complète

Voici une petite app :

* accueil,
* liste de produits,
* détail produit,
* passage de paramètres,
* style moderne.

Tu peux la lancer directement avec Expo.

---

# App complète

## App.js

```jsx
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import {
  View,
  Text,
  Button,
  FlatList,
  TouchableOpacity,
  StyleSheet,
} from 'react-native';

const Stack = createNativeStackNavigator();

const PRODUCTS = [
  { id: 1, name: 'iPhone' },
  { id: 2, name: 'MacBook' },
  { id: 3, name: 'iPad' },
];

function HomeScreen({ navigation }) {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>Accueil</Text>

      <Button
        title="Voir les produits"
        onPress={() => navigation.navigate('Products')}
      />
    </View>
  );
}

function ProductsScreen({ navigation }) {
  return (
    <FlatList
      data={PRODUCTS}
      keyExtractor={(item) => item.id.toString()}
      contentContainerStyle={styles.list}
      renderItem={({ item }) => (
        <TouchableOpacity
          style={styles.card}
          onPress={() =>
            navigation.navigate('Details', {
              product: item,
            })
          }
        >
          <Text style={styles.cardTitle}>{item.name}</Text>
        </TouchableOpacity>
      )}
    />
  );
}

function DetailsScreen({ route, navigation }) {
  const { product } = route.params;

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Détail produit</Text>

      <Text style={styles.productName}>
        {product.name}
      </Text>

      <Text>ID : {product.id}</Text>

      <View style={{ height: 20 }} />

      <Button
        title="Ouvrir encore ce produit"
        onPress={() =>
          navigation.push('Details', {
            product,
          })
        }
      />

      <View style={{ height: 10 }} />

      <Button
        title="Retour"
        onPress={() => navigation.goBack()}
      />
    </View>
  );
}

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator
        screenOptions={{
          headerStyle: {
            backgroundColor: '#111827',
          },
          headerTintColor: '#fff',
          contentStyle: {
            backgroundColor: '#f3f4f6',
          },
        }}
      >
        <Stack.Screen
          name="Home"
          component={HomeScreen}
          options={{
            title: 'Accueil',
          }}
        />

        <Stack.Screen
          name="Products"
          component={ProductsScreen}
          options={{
            title: 'Produits',
          }}
        />

        <Stack.Screen
          name="Details"
          component={DetailsScreen}
          options={({ route }) => ({
            title: route.params.product.name,
          })}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    padding: 20,
  },

  title: {
    fontSize: 28,
    fontWeight: 'bold',
    marginBottom: 20,
  },

  list: {
    padding: 16,
  },

  card: {
    backgroundColor: 'white',
    padding: 20,
    borderRadius: 12,
    marginBottom: 12,
  },

  cardTitle: {
    fontSize: 18,
    fontWeight: '600',
  },

  productName: {
    fontSize: 24,
    marginBottom: 10,
  },
});
```

---

# 16. Comment tester

## Avec Expo

Créer le projet :

```bash
npx create-expo-app my-navigation-app
```

Installer React Navigation :

```bash
npx expo install @react-navigation/native
npx expo install react-native-screens react-native-safe-area-context
npm install @react-navigation/native-stack
```

Lancer :

```bash
npm start
```

---

# 17. Ce que tu devrais apprendre ensuite

Après Stack Navigator :

## Bottom Tabs

Navigation type Instagram.

```txt
Accueil | Recherche | Profil
```

---

## Drawer Navigation

Menu latéral.

---

## Nested Navigators

Navigateur dans navigateur.

Très utilisé en production.

---

# 18. Ce qui est utilisé en entreprise aujourd’hui

Le combo ultra classique :

```txt
NavigationContainer
 └── Stack Navigator
      └── Bottom Tabs
           ├── Home
           ├── Search
           └── Profile
```

---

# 19. Conseils pro

## Toujours :

* séparer les écrans,
* typer les routes,
* centraliser les noms de routes,
* éviter les chaînes hardcodées partout.

---

# 20. Documentation officielle moderne

* [Getting Started React Navigation](https://reactnavigation.org/docs/getting-started?utm_source=chatgpt.com)
* [Native Stack Navigator](https://reactnavigation.org/docs/native-stack-navigator?utm_source=chatgpt.com)
* [Navigation Hooks](https://reactnavigation.org/docs/use-navigation?utm_source=chatgpt.com)

---

