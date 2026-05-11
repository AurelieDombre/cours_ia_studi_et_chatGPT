# Architecture moderne Tabs + Stack

C’est la structure la plus utilisée en production aujourd’hui.

Exemple :

```txt id="5v32t8"
NavigationContainer
└── Bottom Tabs
    ├── Home Stack
    │   ├── HomeScreen
    │   └── DetailsScreen
    │
    ├── Search Stack
    │   ├── SearchScreen
    │   └── ResultScreen
    │
    └── Profile Stack
        └── ProfileScreen
```

---

# Ce qu’on va construire

Une mini app avec :

## Tabs

* 🏠 Accueil
* 🔍 Recherche
* 👤 Profil

## Stack dans Home

Depuis l’accueil :

* on ouvre une fiche produit,
* avec navigation stack classique.

---

# Installation

## Créer le projet

```bash id="1g1tca"
npx create-expo-app my-tabs-stack-app
```

---

## Installer React Navigation

```bash id="bll8iq"
npx expo install @react-navigation/native
npx expo install react-native-screens react-native-safe-area-context
npm install @react-navigation/native-stack
npm install @react-navigation/bottom-tabs
```

---

# Structure conseillée

```txt id="jafqj0"
src/
 ├── navigation/
 │    ├── HomeStack.js
 │    └── TabNavigator.js
 │
 ├── screens/
 │    ├── HomeScreen.js
 │    ├── DetailsScreen.js
 │    ├── SearchScreen.js
 │    └── ProfileScreen.js
 │
 └── App.js
```

---

# 1. App.js

```jsx id="m4q4vh"
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

# 2. navigation/HomeStack.js

```jsx id="o4k5e0"
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
        options={{
          title: 'Accueil',
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
  );
}
```

---

# 3. navigation/TabNavigator.js

```jsx id="fl2o0g"
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';

import HomeStack from './HomeStack';

import SearchScreen from '../screens/SearchScreen';
import ProfileScreen from '../screens/ProfileScreen';

const Tab = createBottomTabNavigator();

export default function TabNavigator() {
  return (
    <Tab.Navigator
      screenOptions={{
        headerShown: false,
      }}
    >
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

# 4. screens/HomeScreen.js

```jsx id="q2whdn"
import {
  View,
  Text,
  TouchableOpacity,
  StyleSheet,
} from 'react-native';

const PRODUCTS = [
  { id: 1, name: 'iPhone 16' },
  { id: 2, name: 'MacBook Pro' },
  { id: 3, name: 'iPad Air' },
];

export default function HomeScreen({ navigation }) {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>
        Produits
      </Text>

      {PRODUCTS.map((product) => (
        <TouchableOpacity
          key={product.id}
          style={styles.card}
          onPress={() =>
            navigation.navigate('Details', {
              product,
            })
          }
        >
          <Text style={styles.cardTitle}>
            {product.name}
          </Text>
        </TouchableOpacity>
      ))}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: '#f3f4f6',
  },

  title: {
    fontSize: 32,
    fontWeight: 'bold',
    marginBottom: 20,
  },

  card: {
    backgroundColor: 'white',
    padding: 20,
    borderRadius: 12,
    marginBottom: 12,
  },

  cardTitle: {
    fontSize: 18,
  },
});
```

---

# 5. screens/DetailsScreen.js

```jsx id="m5w25v"
import {
  View,
  Text,
  Button,
  StyleSheet,
} from 'react-native';

export default function DetailsScreen({
  route,
  navigation,
}) {
  const { product } = route.params;

  return (
    <View style={styles.container}>
      <Text style={styles.title}>
        {product.name}
      </Text>

      <Text>ID : {product.id}</Text>

      <View style={{ height: 20 }} />

      <Button
        title="Ouvrir encore"
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

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#f3f4f6',
  },

  title: {
    fontSize: 28,
    fontWeight: 'bold',
    marginBottom: 10,
  },
});
```

---

# 6. screens/SearchScreen.js

```jsx id="sh9vgm"
import {
  View,
  Text,
  StyleSheet,
} from 'react-native';

export default function SearchScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>
        Recherche
      </Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#f3f4f6',
  },

  title: {
    fontSize: 28,
    fontWeight: 'bold',
  },
});
```

---

# 7. screens/ProfileScreen.js

```jsx id="8pr54q"
import {
  View,
  Text,
  StyleSheet,
} from 'react-native';

export default function ProfileScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>
        Profil
      </Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#f3f4f6',
  },

  title: {
    fontSize: 28,
    fontWeight: 'bold',
  },
});
```

---

# Ce que cette app t’apprend

## Bottom Tabs

```jsx id="2vbk1v"
createBottomTabNavigator()
```

---

## Stack imbriqué

```jsx id="uj5z6o"
HomeStack dans un Tab
```

---

## Navigation entre écrans

```jsx id="a2tq0q"
navigation.navigate()
navigation.push()
navigation.goBack()
```

---

## Paramètres

```jsx id="v0u22f"
route.params
```

---

# Pourquoi cette architecture est importante

Parce qu’elle est utilisée partout :

* Instagram
* Spotify
* Uber
* Airbnb
* LinkedIn

---

# Évolution naturelle ensuite

Tu pourras ajouter :

## Auth Stack

```txt id="5kq7z2"
Login
Register
ForgotPassword
```

---

## Protected Routes

Utilisateur connecté ou non.

---

## Drawer Navigation

Menu latéral.

---

## Deep Linking

Navigation via URL mobile.

---

# Bonus : ajouter des icônes dans les tabs

Installer :

```bash id="q8y0p4"
npx expo install @expo/vector-icons
```

Puis :

```jsx id="4sj8mc"
import Ionicons from '@expo/vector-icons/Ionicons';
```

Et :

```jsx id="90ypu5"
tabBarIcon: ({ color, size }) => (
  <Ionicons
    name="home"
    size={size}
    color={color}
  />
)
```

---

# Documentation officielle

* [Bottom Tabs Navigator](https://reactnavigation.org/docs/bottom-tab-navigator?utm_source=chatgpt.com)
* [Native Stack Navigator](https://reactnavigation.org/docs/native-stack-navigator?utm_source=chatgpt.com)
* [Nesting Navigators](https://reactnavigation.org/docs/nesting-navigators?utm_source=chatgpt.com)
