import * as SQLite from "expo-sqlite";

export const db = SQLite.openDatabaseSync("boutique.db");

export function initDatabase() {
  db.execSync(`
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

    CREATE TABLE IF NOT EXISTS WishLists (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      owner_id INTEGER NOT NULL,
      title TEXT NOT NULL,
      creation_date INTEGER NOT NULL,

      FOREIGN KEY (owner_id)
        REFERENCES Users(id)
        ON DELETE CASCADE
    );

    CREATE TABLE IF NOT EXISTS Wishlist_Products (
      wishlist_id INTEGER NOT NULL,
      product_id INTEGER NOT NULL,
      list_order INTEGER,

      PRIMARY KEY (wishlist_id, product_id),

      FOREIGN KEY (wishlist_id)
        REFERENCES WishLists(id)
        ON DELETE CASCADE,

      FOREIGN KEY (product_id)
        REFERENCES Products(id)
        ON DELETE CASCADE
    );
  `);
}
