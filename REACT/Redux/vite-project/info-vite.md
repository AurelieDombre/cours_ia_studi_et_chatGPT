Cette erreur est normale dans le navigateur : Uncaught TypeError: Failed to resolve module specifier "redux". Relative references must start with either "/", "./", or "../".

Tu fais :

```js id="tq9dho"
import { createStore } from 'redux'
```

mais `"redux"` est un package npm, pas un fichier local.
Le navigateur seul ne sait pas résoudre ça.

Tu as 3 solutions.

---

# Solution recommandée : utiliser un bundler

Le plus propre pour Redux est d’utiliser :

* [Vite](https://vitejs.dev?utm_source=chatgpt.com)
* ou webpack

Avec Vite :

```bash id="j7om2j"
npm create vite@latest
npm install
npm install redux
npm run dev
```

Ensuite :

```js id="r72b8t"
import { createStore } from 'redux'
```

fonctionnera.

---

# Solution simple pour tester vite fait dans le navigateur

Importer Redux depuis un CDN ES Module.

Dans `store.js` :

```js id="6e5i9j"
import { createStore } from 'https://cdn.skypack.dev/redux'
import { counterReducer } from '../reducers/counterReducer.js'

export const store = createStore(counterReducer)
```

ou :

```js id="3grm42"
import { createStore } from 'https://esm.sh/redux'
```

Ça fonctionne directement sans npm.

---

# Pourquoi l’erreur arrive

Le navigateur comprend seulement :

```js id="b0b47s"
import x from './file.js'
import x from '../file.js'
import x from '/file.js'
```

mais pas :

```js id="8b4v3q"
import x from 'redux'
```

car ça nécessite :

* npm
* node_modules
* résolution de dépendances
* bundler

---

Pour apprendre Redux rapidement, le plus simple aujourd’hui est :

1. installer Node.js
2. utiliser [Vite](https://vitejs.dev?utm_source=chatgpt.com)
3. installer Redux via npm

C’est le workflow moderne standard.

---
Dans un projet [Vite](https://vitejs.dev?utm_source=chatgpt.com), tu lances le serveur avec :
---
```bash id="qkh7k7"
npm run dev
```

---

Workflow complet :

```bash id="d49m1x"
npm install
npm run dev
```

Vite va afficher quelque chose comme :

```txt id="mk3of4"
  VITE vX.X.X  ready in 300 ms

  ➜  Local:   http://localhost:5173/
```

Tu ouvres ensuite cette URL dans ton navigateur.

---

Important :
avec Vite tu n’utilises PLUS Live Server (`127.0.0.1:5500`).

Tu dois passer par le serveur Vite :

```txt id="i3n3m2"
http://localhost:5173
```

---

Et maintenant ceci fonctionnera :

```js id="l3o7q8"
import { createStore } from 'redux'
```

à condition d’avoir installé Redux :

```bash id="9p6xyx"
npm install redux
```
