import {
    View,
    Text,
    TextInput,
    TouchableOpacity,
    FlatList,
    StyleSheet
} from "react-native";
import { useEffect, useState } from "react";
import {
    createWishlist,
    addProductToWishlist,
    getWishListsByUser,
    WishList
} from "@/services/wishList.service";


import { getProducts, Product } from "@/services/product.service";


export default function WishListScreen() {

    const [wishlists, setWishlists] = useState<WishList[]>([]);
    const [products, setProducts] = useState<Product[]>([]);

    const [title, setTitle] = useState("");
    const [selectedWishlist, setSelectedWishlist] = useState<number | null>(null);

    async function loadData() {
        const wishListsByUser = await getWishListsByUser(1);
        const products = await getProducts();

        setWishlists(wishListsByUser);
        setProducts(products);
    }

    async function handleCreateWishlist() {
        if (!title) return;

        await createWishlist(1, title);
        setTitle("");

        loadData();
    }

    async function handleAddProduct(productId: number) {
        if (!selectedWishlist) return;

        await addProductToWishlist(selectedWishlist, productId);

        loadData();
    }

    return (
        <View style={styles.container}>

            {/* CREATE WISHLIST */}
            <Text style={styles.header}>Créer une Wishlist</Text>

            <TextInput
                placeholder="Nom wishlist"
                value={title}
                onChangeText={setTitle}
                style={styles.input}
            />

            <TouchableOpacity
                style={styles.button}
                onPress={handleCreateWishlist}
            >
                <Text style={styles.buttonText}>Créer</Text>
            </TouchableOpacity>

            {/* SELECT WISHLIST */}
            <Text style={styles.header}>Choisir Wishlist</Text>

            <FlatList
                data={wishlists}
                horizontal
                keyExtractor={(item) => item.id.toString()}
                renderItem={({ item }) => (
                    <TouchableOpacity
                        style={[
                            styles.wishlistBtn,
                            selectedWishlist === item.id && styles.selected
                        ]}
                        onPress={() => setSelectedWishlist(item.id)}
                    >
                        <Text>{item.title}</Text>
                    </TouchableOpacity>
                )}
            />

            {/* PRODUCTS */}
            <Text style={styles.header}>Produits</Text>

            <FlatList
                data={products}
                keyExtractor={(item) => item.id.toString()}
                renderItem={({ item }) => (
                    <View style={styles.productCard}>
                        <Text style={styles.productTitle}>{item.title}</Text>

                        <TouchableOpacity
                            style={styles.addBtn}
                            onPress={() => handleAddProduct(item.id)}
                        >
                            <Text style={{ color: "white" }}>
                                Ajouter
                            </Text>
                        </TouchableOpacity>
                    </View>
                )}
            />

        </View>
    );

}

const styles = StyleSheet.create({
    container: {
        flex: 1,
        padding: 16,
        backgroundColor: "#f5f5f5",
    },

    header: {
        fontSize: 20,
        fontWeight: "bold",
        marginTop: 10,
        marginBottom: 10,
    },

    input: {
        backgroundColor: "white",
        padding: 12,
        borderRadius: 10,
    },

    button: {
        backgroundColor: "black",
        padding: 12,
        borderRadius: 10,
        marginTop: 10,
    },

    buttonText: {
        color: "white",
        textAlign: "center",
    },

    wishlistBtn: {
        backgroundColor: "white",
        padding: 10,
        borderRadius: 10,
        marginRight: 10,
    },

    selected: {
        borderWidth: 2,
        borderColor: "black",
    },

    productCard: {
        backgroundColor: "white",
        padding: 12,
        marginTop: 10,
        borderRadius: 10,
    },

    productTitle: {
        fontWeight: "bold",
        marginBottom: 6,
    },

    addBtn: {
        backgroundColor: "green",
        padding: 10,
        borderRadius: 8,
        marginTop: 10,
        alignItems: "center",
    },
});