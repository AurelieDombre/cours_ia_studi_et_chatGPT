import { Text, View, StyleSheet, ScrollView } from "react-native";
import { useEffect, useState } from "react";
import { db, initDatabase, seedDatabase } from "@/database/database";

type TableInfo = {
  name: string;
};

type User = {
  id: number;
  first_name: string;
  last_name: string;
  email: string;
};

type Product = {
  id: number;
  title: string;
  quantity: number;
};

export default function Index() {
  const [message, setMessage] = useState("");
  const [tables, setTables] = useState<TableInfo[]>([]);
  const [users, setUsers] = useState<User[]>([]);
  const [products, setProducts] = useState<Product[]>([]);

  useEffect(() => {
    try {
      initDatabase();
      seedDatabase();

      // Tables
      const tablesResult = db.getAllSync<TableInfo>(
        `SELECT name FROM sqlite_master WHERE type='table';`
      );

      setTables(tablesResult);

      // Users
      const usersResult = db.getAllSync<User>(
        `SELECT * FROM Users;`
      );

      setUsers(usersResult);

      // Products
      const productsResult = db.getAllSync<Product>(
        `SELECT * FROM Products;`
      );

      setProducts(productsResult);

      setMessage("Base SQLite initialisée avec succès ✅");
    } catch (error) {
      const errorMessage =
        error instanceof Error ? error.message : "Erreur inconnue";

      setMessage(`Erreur SQLite: ${errorMessage}`);
      console.error(error);
    }
  }, []);

  return (
    <ScrollView contentContainerStyle={styles.container}>
      <Text style={styles.title}>SQLite Expo Demo</Text>

      <View>
        <form>
          
        </form>
      </View>


      <View style={styles.card}>
        <Text style={styles.cardTitle}>Statut</Text>
        <Text style={styles.text}>{message}</Text>
      </View>

      <View style={styles.card}>
        <Text style={styles.cardTitle}>Tables</Text>

        {tables.map((table, index) => (
          <Text key={index} style={styles.item}>
            • {table.name}
          </Text>
        ))}
      </View>

      <View style={styles.card}>
        <Text style={styles.cardTitle}>Utilisateurs</Text>

        {users.map((user) => (
          <View key={user.id} style={styles.row}>
            <Text style={styles.bold}>
              {user.first_name} {user.last_name}
            </Text>

            <Text style={styles.small}>{user.email}</Text>
          </View>
        ))}
      </View>

      <View style={styles.card}>
        <Text style={styles.cardTitle}>Produits</Text>

        {products.map((product) => (
          <View key={product.id} style={styles.row}>
            <Text style={styles.bold}>{product.title}</Text>

            <Text style={styles.small}>
              Stock : {product.quantity}
            </Text>
          </View>
        ))}
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    padding: 20,
    backgroundColor: "#f5f5f5",
    flexGrow: 1,
  },

  title: {
    fontSize: 28,
    fontWeight: "bold",
    marginBottom: 20,
    textAlign: "center",
  },

  card: {
    backgroundColor: "white",
    padding: 16,
    borderRadius: 12,
    marginBottom: 16,

    shadowColor: "#000",
    shadowOffset: {
      width: 0,
      height: 2,
    },

    shadowOpacity: 0.1,
    shadowRadius: 4,

    elevation: 3,
  },

  cardTitle: {
    fontSize: 20,
    fontWeight: "600",
    marginBottom: 10,
  },

  text: {
    fontSize: 16,
    color: "#333",
  },

  item: {
    fontSize: 16,
    marginBottom: 6,
  },

  row: {
    marginBottom: 12,
    paddingBottom: 8,
    borderBottomWidth: 1,
    borderBottomColor: "#eee",
  },

  bold: {
    fontSize: 16,
    fontWeight: "600",
  },

  small: {
    fontSize: 14,
    color: "#666",
    marginTop: 2,
  },
});