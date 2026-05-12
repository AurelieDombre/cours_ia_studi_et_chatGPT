import * as React from 'react';
import { Text, View, StyleSheet } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createMaterialTopTabNavigator } from '@react-navigation/material-top-tabs';


// Notre premier écran
function HomeScreen() {
  return (
    <View style={styles.containers}>
      <Text>Home</Text>
    </View>
  );
}

// Notre deuxième écran
function ProfileScreen() {
  return (
    <View style={styles.containers}>
      <Text>Profile</Text>
    </View>
  );
}

// Notre troisième écran
function AboutScreen() {
  return (
    <View style={styles.containers}>
      <Text>A</Text>
    </View>
  );
}

// Des styles communs pour l'affichage
const styles = StyleSheet.create({
  containers: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
});

// Notre navigateur en tables
const Tab = createMaterialTopTabNavigator();

// Et notre application ainsi que la définition des écrans
export default function App() {
  return (
    <NavigationContainer>
      <Tab.Navigator>
        <Tab.Screen name="Home" component={HomeScreen} />
        <Tab.Screen name="Profile" component={ProfileScreen} />
        <Tab.Screen name="About" component={AboutScreen} />
      </Tab.Navigator>
    </NavigationContainer>
  );
}