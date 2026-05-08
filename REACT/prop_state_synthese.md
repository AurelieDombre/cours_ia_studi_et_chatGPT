# Les Props et le State en React Native — version simple

## 1. À quoi servent les composants ?

En React Native, une application est découpée en **composants**.

Exemple :

* un composant `Header`
* un composant `Button`
* un composant `TaskItem`

Chaque composant peut :

* **recevoir des données** → avec les **props**
* **gérer ses propres données** → avec le **state**

---

# 2. Les Props

## Définition simple

Les **props** servent à **envoyer des données d’un composant parent vers un composant enfant**.

👉 Les props sont **en lecture seule** :
le composant enfant ne peut pas les modifier.

---

## Exemple simple

### Composant enfant

```jsx
const Greeting = (props) => {
  return <Text>Bonjour {props.name}</Text>;
};
```

Ici :

* `name` est une prop
* le composant affiche la valeur reçue

---

### Composant parent

```jsx
<Greeting name="Marie" />
<Greeting name="Pierre" />
```

Résultat :

```txt
Bonjour Marie
Bonjour Pierre
```

---

# Important à retenir

## Props = données envoyées du parent vers l’enfant

Schéma :

```txt
Parent → Enfant
```

---

# 3. Le destructuring (important)

Au lieu d’écrire :

```jsx
const Greeting = (props) => {
  return <Text>{props.name}</Text>;
};
```

on peut écrire :

```jsx
const Greeting = ({ name }) => {
  return <Text>{name}</Text>;
};
```

👉 C’est plus propre et plus lisible.

---

# 4. Le State

## Définition simple

Le **state** sert à stocker des données qui peuvent changer dans le composant.

Exemples :

* compteur
* formulaire
* liste de tâches
* menu ouvert/fermé

Contrairement aux props :

* le state peut être modifié

---

# 5. useState

Pour créer un state, on utilise le hook :

```jsx
useState()
```

---

## Exemple simple : compteur

```jsx
const Counter = () => {
  const [count, setCount] = useState(0);

  return (
    <View>
      <Text>{count}</Text>

      <Button
        title="Ajouter"
        onPress={() => setCount(count + 1)}
      />
    </View>
  );
};
```

---

# Explication ligne par ligne

```jsx
const [count, setCount] = useState(0);
```

* `count` = valeur actuelle
* `setCount` = fonction pour modifier la valeur
* `0` = valeur initiale

---

Quand on clique :

```jsx
setCount(count + 1)
```

➡ le compteur augmente.

---

# À retenir

## Props vs State

| Props           | State                  |
| --------------- | ---------------------- |
| données reçues  | données internes       |
| immuables       | modifiables            |
| parent → enfant | géré dans le composant |

---

# 6. useEffect

## À quoi sert useEffect ?

`useEffect` sert à exécuter du code :

* quand le composant apparaît
* quand une donnée change
* quand le composant se met à jour

---

## Exemple simple

```jsx
useEffect(() => {
  console.log("Composant chargé");
}, []);
```

Le `[]` signifie :
👉 exécuter une seule fois au chargement.

---

# Exemple avec dépendance

```jsx
useEffect(() => {
  console.log("Le compteur a changé");
}, [count]);
```

👉 L’effet se lance chaque fois que `count` change.

---

# 7. Cycle de vie simplifié

Un composant peut :

1. apparaître → montage
2. se mettre à jour
3. disparaître → démontage

Avec les composants fonctionnels, on gère ça avec :

* `useEffect`

---

# 8. PropTypes

## Pourquoi utiliser PropTypes ?

PropTypes permet de vérifier que les props ont le bon type.

Exemple :

* texte → string
* nombre → number
* booléen → bool

---

## Exemple

```jsx
Greeting.propTypes = {
  name: PropTypes.string.isRequired,
  age: PropTypes.number.isRequired,
};
```

---

# Explication

* `string` → texte
* `number` → nombre
* `isRequired` → obligatoire

Si le type est mauvais :
➡ React affiche une erreur.

---

# 9. Communication entre composants

---

# Parent → Enfant

On utilise :

## les props

```txt
Parent → props → Enfant
```

---

# Enfant → Parent

Un enfant ne peut pas modifier directement le parent.

👉 On utilise une fonction callback.

---

# Exemple simple

## Parent

```jsx
const Parent = () => {
  const [message, setMessage] = useState("");

  const handleMessage = (text) => {
    setMessage(text);
  };

  return (
    <Child onSendMessage={handleMessage} />
  );
};
```

---

## Enfant

```jsx
const Child = ({ onSendMessage }) => {
  return (
    <Button
      title="Envoyer"
      onPress={() => onSendMessage("Bonjour")}
    />
  );
};
```

---

# Ce qu’il se passe

1. Le parent envoie une fonction à l’enfant
2. L’enfant appelle cette fonction
3. Le parent récupère les données

---

# Schéma global

```txt
Parent → props → Enfant
Enfant → callback → Parent
```

---

# 10. Les hooks à connaître

| Hook       | Rôle                          |
| ---------- | ----------------------------- |
| useState   | gérer les données             |
| useEffect  | gérer le cycle de vie         |
| useContext | partager des données globales |

---

# 11. Résumé ultra simple

## Props

➡ servent à transmettre des données

## State

➡ sert à stocker des données modifiables

## useState

➡ crée un state

## useEffect

➡ exécute du code lors des changements

## PropTypes

➡ vérifie les types des props

## Callback

➡ permet à l’enfant de parler au parent

---

# Astuce pour retenir

## Props = paramètres

Comme les paramètres d’une fonction.

---

## State = mémoire du composant

Le composant “se souvient” d’une valeur.

---

# Mini fiche mémoire

```txt
Props :
- parent → enfant
- lecture seule

State :
- données internes
- modifiable

useState :
- crée un state

useEffect :
- effets / cycle de vie

Callback :
- enfant → parent
```
