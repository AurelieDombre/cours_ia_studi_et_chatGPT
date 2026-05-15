import { db } from "@/database/database";

export type WishList = {
    id: number;
    title: string;
    creation_date: string;
};

export async function getWishLists() {
    return await db.getAllAsync<WishList>(`
        SELECT * FROM WishLists
    `);

}


export async function createWishlist(
    ownerId: number,
    title: string
) {
    await db.runAsync(
        `
    INSERT INTO WishLists (owner_id, title, creation_date)
    VALUES (?, ?, strftime('%s','now'));
    `,
        [ownerId, title]
    );
}

export async function addProductToWishlist(
    wishlistId: number,
    productId: number,
    order: number = 0
) {
    await db.runAsync(
        `
    INSERT OR IGNORE INTO Wishlist_Products
    (wishlist_id, product_id, list_order)
    VALUES (?, ?, ?);
    `,
        [wishlistId, productId, order]
    );
}

/* export async function updateWishList(
    wishlistId: number,
    productId: string,
    order: string,
) {
    await db.runAsync(
        `UPDATE WishLists
        SET title = ?,
        creation_date = ?,
        = ?
        WHERE id = ?;
        `,
        [wishlistId, productId, order]
    );
}

export async function deleteWishList(id: number) {
    try {
        await db.runAsync(
            `DELETE FROM WishLists WHERE id = ?;`,
            [id]
        );

        console.log("Produit supprimé :", id);

    } catch (error) {
        console.error("Erreur suppression :", error);
    }
} */


export async function getWishListsByUser(userId: number) {
    const rows = await db.getAllAsync(
        `
    SELECT
      w.id AS wishlist_id,
      w.title,
      w.creation_date,

      p.id AS product_id,
      p.title AS product_title,
      p.description,
      p.quantity

    FROM WishLists w
    LEFT JOIN Wishlist_Products wp ON wp.wishlist_id = w.id
    LEFT JOIN Products p ON p.id = wp.product_id
    WHERE w.owner_id = ?
    ORDER BY w.id;
    `,
        [userId]
    );

    const result: any[] = [];

    rows.forEach((row: any) => {
        let wishlist = result.find(x => x.id === row.wishlist_id);

        if (!wishlist) {
            wishlist = {
                id: row.wishlist_id,
                title: row.title,
                creation_date: row.creation_date,
                products: []
            };
            result.push(wishlist);
        }

        if (row.product_id) {
            wishlist.products.push({
                id: row.product_id,
                title: row.product_title,
                description: row.description,
                quantity: row.quantity,
            });
        }
    });

    return result;
}


