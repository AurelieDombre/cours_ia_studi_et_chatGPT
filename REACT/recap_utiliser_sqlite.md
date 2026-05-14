# Récapitulatif ultra pédagogique — SQLite avec React Native

## 1. Pourquoi utiliser SQLite ?

Quand une application mobile se ferme, redémarre ou passe en arrière-plan, les données stockées dans les variables (`state`) disparaissent.

Exemple :

* une liste de tâches,
* un panier,
* des favoris.

👉 SQLite permet de **sauvegarder les données directement dans le téléphone** pour les retrouver plus tard. 

---

# 2. SQLite, c’est quoi exactement ?

SQLite est :

* une **base de données relationnelle**,
* légère,
* stockée dans un fichier local,
* utilisable directement dans React Native avec Expo. 

## Base de données relationnelle = ?

Les données sont organisées en :

* **tables**
* **colonnes**
* **lignes**

Comme un tableau Excel intelligent.

---

# 3. Comprendre les tables SQL

## Exemple simple

### Table Users

| id | prénom  | nom      |
| -- | ------- | -------- |
| 1  | Andréas | HANSS    |
| 2  | Claude  | Delatour |

### Table Tasks

| id | owner | tâche             | done  |
| -- | ----- | ----------------- | ----- |
| 1  | 1     | Faire un cours RN | false |

Ici :

* `owner = 1`
* signifie que la tâche appartient à l’utilisateur ayant `id = 1`.

---

# 4. Les notions SUPER importantes

## A. Clé primaire (PRIMARY KEY)

C’est l’identifiant unique d’une ligne.

Exemple :

```sql
id INTEGER PRIMARY KEY
```

👉 Chaque utilisateur possède un id différent.

### À retenir :

* unique
* identifie une ligne
* souvent un entier

---

## B. Clé étrangère (FOREIGN KEY)

Elle relie une table à une autre.

Exemple :

```sql
FOREIGN KEY (owner_id) REFERENCES Users(id)
```

👉 Cela signifie :
“owner_id doit correspondre à un utilisateur existant”.

---

## C. NOT NULL

Champ obligatoire.

```sql
prenom TEXT NOT NULL
```

👉 Impossible d’ajouter un utilisateur sans prénom.

---

## D. UNIQUE

Empêche les doublons.

Exemple :

```sql
email TEXT UNIQUE
```

👉 Deux utilisateurs ne peuvent pas avoir le même email.

---

# 5. Création d’une table

Exemple :

```sql
CREATE TABLE Users (
 id INTEGER PRIMARY KEY,
 prenom TEXT NOT NULL,
 nom TEXT NOT NULL
);
```

## Traduction humaine

* CREATE TABLE → créer une table
* Users → nom de la table
* id → identifiant unique
* TEXT → texte
* NOT NULL → obligatoire

---

# 6. Les types de données SQLite

| Type    | Signification    |
| ------- | ---------------- |
| INTEGER | nombre entier    |
| REAL    | nombre décimal   |
| TEXT    | texte            |
| NULL    | valeur vide      |
| BLOB    | données binaires |

⚠️ Important :
SQLite n’a PAS de type `DATE`. 

👉 On utilise donc un timestamp :

```js
Date.now()
```

---

# 7. Les transactions (TRÈS IMPORTANT)

## Le problème sans transaction

Imagine un transfert bancaire :

1. on retire 50€
2. l’application plante
3. on n’ajoute jamais les 50€ à l’autre compte

💥 Données incohérentes.

---

## Solution : les transactions

Une transaction garantit :

* soit TOUT fonctionne,
* soit RIEN n’est validé.

En React Native :

```js
db.transaction((tx) => {
   // requêtes SQL
})
```

👉 `tx` représente la transaction en cours.

---

# 8. Installer SQLite dans Expo

Commande :

```bash
expo install expo-sqlite
```

Puis :

```js
import * as SQLite from 'expo-sqlite';
```

---

# 9. Ouvrir une base de données

```js
const db = SQLite.openDatabase("test.db");
```

👉 Si la base n’existe pas :
SQLite la crée automatiquement.

---

# 10. Les requêtes SQL essentielles

## A. SELECT → récupérer des données

```sql
SELECT * FROM Products;
```

👉 récupère tous les produits.

---

## B. INSERT → ajouter des données

```sql
INSERT INTO Products (title, quantity)
VALUES ('Produit 1', 100);
```

👉 ajoute un produit.

---

## C. UPDATE → modifier

```sql
UPDATE Products
SET title = 'Super Produit'
WHERE id = 1;
```

👉 modifie le produit 1.

---

## D. DELETE → supprimer

```sql
DELETE FROM Products
WHERE id = 1;
```

👉 supprime le produit 1.

---

# 11. Pourquoi utiliser les `?` dans les requêtes ?

Exemple :

```js
tx.executeSql(
 "DELETE FROM Products WHERE id = ?;",
 [toDeleteId]
)
```

Les `?` servent à :

* injecter des valeurs facilement,
* éviter les injections SQL,
* sécuriser les requêtes. 

---

# 12. Structure d’une requête React Native SQLite

```js
tx.executeSql(
   "SELECT * FROM Products",
   [],
   (_, result) => {
      console.log(result.rows._array)
   },
   (error) => console.warn(error)
)
```

## Explication

### Paramètre 1

La requête SQL.

### Paramètre 2

Les arguments des `?`.

### Paramètre 3

Fonction appelée si succès.

### Paramètre 4

Fonction appelée si erreur.

---

# 13. useEffect + SQLite

Le cours utilise souvent :

```js
useEffect(() => {
   // requêtes SQL
}, [])
```

👉 Cela permet :

* de créer les tables au démarrage,
* de charger les données automatiquement.

---

# 14. Le hook personnalisé `useFetch`

Le cours explique aussi les hooks personnalisés.

## Pourquoi ?

Pour éviter de répéter le même code `fetch`.

---

## Sans hook personnalisé

On répète :

* useState
* useEffect
* fetch
* gestion erreurs

à chaque composant.

---

## Avec `useFetch`

On factorise :

```js
const [items] = useFetch(url)
```

👉 beaucoup plus propre.

---

# 15. Exemple global du projet du cours

Le projet crée :

## Tables :

* Users
* Products
* WishLists
* WishList_Products

---

## Fonctionnement :

* création de produits,
* ajout dans une wishlist,
* suppression,
* récupération des données,
* affichage dans React Native.

---

# 16. Le point LE PLUS IMPORTANT du cours

👉 SQLite sert à rendre les données persistantes.

Sans SQLite :

* les données disparaissent quand l’application se ferme.

Avec SQLite :

* elles restent enregistrées dans le téléphone.

---

# 17. Ce qu’il faut ABSOLUMENT retenir pour l’examen

## À connaître par cœur

### SQLite est :

✅ une base relationnelle

---

### Installation :

```bash
expo install expo-sqlite
```

---

### Ouvrir la base :

```js
SQLite.openDatabase("test.db")
```

---

### Requêtes SQL :

```sql
SELECT
INSERT
UPDATE
DELETE
```

---

### Clé primaire :

* identifiant unique

---

### Clé étrangère :

* relation entre tables

---

### Transaction :

* garantit l’intégrité des données

---

### `?` dans SQL :

* sécurité
* paramètres dynamiques

---

### SQLite n’a pas de type DATE

👉 utiliser un timestamp.

---

# 18. Résumé ultra simple en 30 secondes

SQLite = une mini base de données stockée dans le téléphone.

Elle permet :

* de sauvegarder les données,
* de faire des requêtes SQL,
* de garder les données même après fermeture de l’application.

On utilise :

* des tables,
* des clés primaires,
* des clés étrangères,
* des transactions.

Dans React Native :

```js
db.transaction((tx) => {
   tx.executeSql(...)
})
```

Et les principales requêtes sont :

```sql
SELECT
INSERT
UPDATE
DELETE
```
