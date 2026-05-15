# Système CRUD complet avec Expo SQLite

## Structure recommandée

```txt
app/
 ├── index.tsx
 ├── users.tsx
 └── products.tsx

components/
 ├── UserCard.tsx
 └── ProductCard.tsx

services/
 ├── user.service.ts
 └── product.service.ts

 database/
 └── database.ts
```

---

# database/database.ts

```ts
import * as SQLite from "expo-sqlite";

export const db = SQLite.openDatabaseSync("boutique.db");

export async function initDatabase() {
  await db.execAsync(`
    PRAGMA foreign_keys = ON;

    CREATE TABLE IF NOT EXISTS Users (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      first_name TEXT NOT NULL,
      last_name TEXT NOT NULL,
      email TEXT NOT NULL UNIQUE
    );

    CREATE TABLE IF NOT EXISTS Products (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      title TEXT NOT NULL,
      description TEXT NOT NULL,
      quantity INTEGER DEFAULT 0
    );
  `);
}
```

---

# services/user.service.ts

```ts
import { db } from "@/database/database";

export type User = {
  id: number;
  first_name: string;
  last_name: string;
  email: string;
};

export async function getUsers() {
  return await db.getAllAsync<User>(`
    SELECT * FROM Users ORDER BY id DESC;
  `);
}

export async function createUser(
  firstName: string,
  lastName: string,
  email: string
) {
  await db.runAsync(
    `INSERT INTO Users (first_name, last_name, email)
     VALUES (?, ?, ?);`,
    [firstName, lastName, email]
  );
}

export async function updateUser(
  id: number,
  firstName: string,
  lastName: string,
  email: string
) {
  await db.runAsync(
    `UPDATE Users
     SET first_name = ?,
         last_name = ?,
         email = ?
     WHERE id = ?;`,
    [firstName, lastName, email, id]
  );
}

export async function deleteUser(id: number) {
  await db.runAsync(
    `DELETE FROM Users WHERE id = ?;`,
    [id]
  );
}
```

---

# services/product.service.ts

```ts
import { db } from "@/database/database";

export type Product = {
  id: number;
  title: string;
  description: string;
  quantity: number;
};

export async function getProducts() {
  return await db.getAllAsync<Product>(`
    SELECT * FROM Products ORDER BY id DESC;
  `);
}

export async function createProduct(
  title: string,
  description: string,
  quantity: number
) {
  await db.runAsync(
    `INSERT INTO Products (title, description, quantity)
     VALUES (?, ?, ?);`,
    [title, description, quantity]
  );
}

export async function updateProduct(
  id: number,
  title: string,
  description: string,
  quantity: number
) {
  await db.runAsync(
    `UPDATE Products
     SET title = ?,
         description = ?,
         quantity = ?
     WHERE id = ?;`,
    [title, description, quantity, id]
  );
}

export async function deleteProduct(id: number) {
  await db.runAsync(
    `DELETE FROM Products WHERE id = ?;`,
    [id]
  );
}
```

---

# app/index.tsx

```tsx
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
} from "react-native";

import { router } from "expo-router";

export default function Index() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>CRUD SQLite</Text>

      <TouchableOpacity
        style={styles.button}
        onPress={() => router.push("/users")}
      >
        <Text style={styles.buttonText}>Gestion des utilisateurs</Text>
      </TouchableOpacity>

      <TouchableOpacity
        style={styles.button}
        onPress={() => router.push("/products")}
      >
        <Text style={styles.buttonText}>Gestion des produits</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: "center",
    padding: 20,
    backgroundColor: "#f5f5f5",
  },

  title: {
    fontSize: 32,
    fontWeight: "bold",
    marginBottom: 30,
    textAlign: "center",
  },

  button: {
    backgroundColor: "black",
    padding: 16,
    borderRadius: 10,
    marginBottom: 15,
  },

  buttonText: {
    color: "white",
    textAlign: "center",
    fontSize: 16,
    fontWeight: "600",
  },
});
```

---

# app/users.tsx

```tsx
import {
  View,
  Text,
  StyleSheet,
  TextInput,
  TouchableOpacity,
  FlatList,
} from "react-native";

import { useEffect, useState } from "react";

import {
  createUser,
  deleteUser,
  getUsers,
  updateUser,
  User,
} from "@/services/user.service";

export default function UsersScreen() {
  const [users, setUsers] = useState<User[]>([]);

  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");

  const [editingId, setEditingId] = useState<number | null>(null);

  async function loadUsers() {
    const data = await getUsers();
    setUsers(data);
  }

  useEffect(() => {
    loadUsers();
  }, []);

  async function handleSave() {
    if (!firstName || !lastName || !email) {
      return;
    }

    if (editingId) {
      await updateUser(editingId, firstName, lastName, email);
      setEditingId(null);
    } else {
      await createUser(firstName, lastName, email);
    }

    setFirstName("");
    setLastName("");
    setEmail("");

    loadUsers();
  }

  function handleEdit(user: User) {
    setEditingId(user.id);
    setFirstName(user.first_name);
    setLastName(user.last_name);
    setEmail(user.email);
  }

  async function handleDelete(id: number) {
    await deleteUser(id);
    loadUsers();
  }

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Utilisateurs</Text>

      <TextInput
        placeholder="Prénom"
        style={styles.input}
        value={firstName}
        onChangeText={setFirstName}
      />

      <TextInput
        placeholder="Nom"
        style={styles.input}
        value={lastName}
        onChangeText={setLastName}
      />

      <TextInput
        placeholder="Email"
        style={styles.input}
        value={email}
        onChangeText={setEmail}
      />

      <TouchableOpacity style={styles.saveButton} onPress={handleSave}>
        <Text style={styles.buttonText}>
          {editingId ? "Modifier" : "Ajouter"}
        </Text>
      </TouchableOpacity>

      <FlatList
        data={users}
        keyExtractor={(item) => item.id.toString()}
        renderItem={({ item }) => (
          <View style={styles.card}>
            <Text style={styles.name}>
              {item.first_name} {item.last_name}
            </Text>

            <Text>{item.email}</Text>

            <View style={styles.actions}>
              <TouchableOpacity
                style={styles.editButton}
                onPress={() => handleEdit(item)}
              >
                <Text style={styles.buttonText}>Modifier</Text>
              </TouchableOpacity>

              <TouchableOpacity
                style={styles.deleteButton}
                onPress={() => handleDelete(item.id)}
              >
                <Text style={styles.buttonText}>Supprimer</Text>
              </TouchableOpacity>
            </View>
          </View>
        )}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: "#f5f5f5",
  },

  title: {
    fontSize: 28,
    fontWeight: "bold",
    marginBottom: 20,
  },

  input: {
    backgroundColor: "white",
    padding: 14,
    borderRadius: 10,
    marginBottom: 10,
  },

  saveButton: {
    backgroundColor: "black",
    padding: 14,
    borderRadius: 10,
    marginBottom: 20,
  },

  buttonText: {
    color: "white",
    textAlign: "center",
    fontWeight: "600",
  },

  card: {
    backgroundColor: "white",
    padding: 16,
    borderRadius: 10,
    marginBottom: 12,
  },

  name: {
    fontSize: 18,
    fontWeight: "bold",
    marginBottom: 5,
  },

  actions: {
    flexDirection: "row",
    marginTop: 10,
    gap: 10,
  },

  editButton: {
    flex: 1,
    backgroundColor: "orange",
    padding: 10,
    borderRadius: 8,
  },

  deleteButton: {
    flex: 1,
    backgroundColor: "red",
    padding: 10,
    borderRadius: 8,
  },
});
```

---

# Lancer le projet

```bash
npm install
```

```bash
npx expo start --clear
```

---

# Ce CRUD contient

✅ CREATE

✅ READ

✅ UPDATE

✅ DELETE

✅ SQLite local

✅ Architecture service

✅ Async/Await

✅ Interface React Native

✅ Expo Router

✅ FlatList

✅ Formulaire dynamique

✅ Edition en direct
