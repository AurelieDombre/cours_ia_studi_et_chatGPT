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