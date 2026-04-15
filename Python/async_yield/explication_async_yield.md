# Les coroutines
---

# 🧠 Ce que fait ton code (en une phrase)

👉 Il produit des valeurs **une par une**, en attendant 1 seconde entre chaque.

---

# 🔍 Décomposition du code

## 1. 🔹 Le générateur asynchrone

```python
import asyncio

async def generator_coroutine():
    for i in range(3):
        await asyncio.sleep(1)
        yield 1
```

### 💡 Ce qu’il se passe :

* `async def` → fonction **asynchrone**
* `await asyncio.sleep(1)` → pause **non bloquante** de 1 seconde
* `yield` → renvoie une valeur **petit à petit**

👉 Donc :

* attend 1 seconde
* renvoie `1`
* attend 1 seconde
* renvoie `1`
* etc. (3 fois)

---

## ⚠️ Différence importante

* `yield` normal → générateur classique
* `async + yield` → **générateur asynchrone**

➡️ Du coup, tu dois utiliser :

```python
async for
```

et pas `for`

---

## 2. 🔹 La fonction principale

```python
async def main():
    async for value in generator_coroutine():
        print(value)
```

👉 `async for` :

* récupère les valeurs **au fur et à mesure**
* attend automatiquement les `await`

---

## 3. 🔹 Lancement du programme

```python
asyncio.run(main())
```

👉 Lance la boucle asynchrone (event loop)

---

# ⏱️ Ce que tu verras concrètement

Sortie dans le terminal :

```
(après 1 seconde) → 1
(après 1 seconde) → 1
(après 1 seconde) → 1
```

---

# 🧠 Image mentale

Imagine un robinet :

* `yield` → tu ouvres un peu → 💧
* `await` → tu attends avant la prochaine goutte
* `async for` → tu récupères chaque goutte quand elle arrive

---

# 🔥 Pourquoi c’est utile ?

## 1. 📡 Données qui arrivent dans le temps

Exemple :

* messages réseau
* streaming
* API en continu

---

## 2. ⚡ Ne pas bloquer le programme

👉 `await asyncio.sleep(1)` :

* n’arrête pas tout le programme
* laisse faire autre chose en parallèle

---

## 3. 🔄 Pipeline de données

Tu peux traiter des données **au fur et à mesure qu’elles arrivent**

---

# ⚠️ Petit détail dans ton code

```python
yield 1
```

👉 Tu renvoies toujours `1`
➡️ plus logique serait :

```python
yield i
```

---

# ✅ Version améliorée

```python
import asyncio

async def generator_coroutine():
    for i in range(3):
        await asyncio.sleep(1)
        yield i

async def main():
    async for value in generator_coroutine():
        print(value)

asyncio.run(main())
```

---

# 🧠 Résumé simple

* `async` → fonction non bloquante
* `await` → attendre intelligemment
* `yield` → envoyer des valeurs une par une
* `async for` → lire ces valeurs

---
