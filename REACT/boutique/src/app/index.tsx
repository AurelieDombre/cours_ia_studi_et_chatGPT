import { Text, View, StyleSheet } from "react-native";
import { useEffect, useState } from "react";
import { db, initDatabase } from "@/database/database";

type TableInfo = {
  name: string;
};

export default function Index() {
  const [message, setMessage] = useState("Initialisation de SQLite...");

  useEffect(() => {
    try {
      initDatabase();

      const tables = db.getAllSync<TableInfo>(
        "SELECT name FROM sqlite_master WHERE type = 'table' ORDER BY name"
      );

      setMessage(`Base initialisee. Tables: ${tables.map((table) => table.name).join(", ")}`);
    } catch (error) {
      const errorMessage = error instanceof Error ? error.message : "Erreur inconnue";
      setMessage(`Erreur SQLite: ${errorMessage}`);
      console.error(error);
    }
  }, []);

  return (
    <View style={styles.container}>
      <Text>{message}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    alignItems: "center",
    justifyContent: "center",
  },
});
