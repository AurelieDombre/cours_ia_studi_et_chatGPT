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
        WHERE id = ?;
        `,
        [title, description, quantity, id]
    );
}

export async function deleteProduct(id: number) {
    try {
        await db.runAsync(
            `DELETE FROM Products WHERE id = ?;`,
            [id]
        );

        console.log("Produit supprimé :", id);

    } catch (error) {
        console.error("Erreur suppression :", error);
    }
}

