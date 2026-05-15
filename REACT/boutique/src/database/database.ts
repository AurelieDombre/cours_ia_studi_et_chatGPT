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

export async function seedDatabase() {
  await db.execAsync(`
    DELETE FROM Wishlist_Products;
    DELETE FROM WishLists;
    DELETE FROM Products;
    DELETE FROM Users;

    DELETE FROM sqlite_sequence;

    INSERT INTO Users (first_name, last_name, email)
    VALUES
      ('Jean', 'Dupont', 'jean@email.com'),
      ('Marie', 'Martin', 'marie@email.com'),
      ('Lucas', 'Bernard', 'lucas@email.com');

    INSERT INTO Products (title, description, quantity)
    VALUES
      ('Nike', 'Chaussures', 10),
      ('Adidas', 'T-shirt', 20),
      ('Puma', 'Sac', 5);

    INSERT INTO WishLists (owner_id, title, creation_date)
    VALUES
      (1, 'Liste Jean', 1715731200),
      (2, 'Liste Marie', 1715817600),
      (3, 'Liste Lucas', 1715904000);

    INSERT INTO Wishlist_Products (wishlist_id, product_id, list_order)
    VALUES
      (1, 1, 1),
      (1, 2, 2),
      (2, 3, 1);
  `);
}