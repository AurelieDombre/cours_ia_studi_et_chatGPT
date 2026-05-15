import {
    View,
    Text,
    StyleSheet,
    TextInput,
    TouchableOpacity,
    FlatList,
} from "react-native";

import { useEffect, useState } from "react";

import { createProduct, updateProduct, getProducts, deleteProduct, Product } from "@/services/product.service";

export default function ProductsScreen() {
    const [products, setProducts] = useState<Product[]>([])

    const [title, setTitle] = useState("");
    const [description, setDesciption] = useState("");
    const [quantity, setQuantity] = useState("");
    const [editingId, setEditingId] = useState<number | null>(null);

    async function loadProducts() {
        const data = await getProducts();
        setProducts(data);
    }

    useEffect(() => {
        loadProducts();
    }, []);

    async function handleSave() {

        const quantityNumber = Number(quantity);

        if (!title || !description || !quantity) {
            return
        }

        if (editingId) {
            await updateProduct(editingId, title, description, quantityNumber);
            setEditingId(null)
        } else {
            await createProduct(title, description, quantityNumber);
        }

        setTitle("");
        setDesciption("");
        setQuantity("");

        loadProducts();

    }

    function handleEdit(product: Product) {
        setEditingId(product.id);
        setTitle(product.title);
        setDesciption(product.description);
        setQuantity(product.quantity.toString());
    }

    async function handleDelete(id: number) {
        await deleteProduct(id);
        loadProducts();
    }

    return (

        <View>
            <Text>Produits</Text>
            <TextInput
                placeholder="Titre"
                style={styles.input}
                value={title}
                onChangeText={setTitle}
            />
            <TextInput
                placeholder="Description"
                style={styles.input}
                value={description}
                onChangeText={setDesciption}
            />
            <TextInput
                placeholder="Quantité"
                style={styles.input}
                value={quantity}
                onChangeText={setQuantity}
                keyboardType="numeric"
            />

            <TouchableOpacity style={styles.saveButton} onPress={handleSave}>
                <Text style={styles.buttonText}>
                    {editingId ? "Modifier" : "Ajouter"}
                </Text>
            </TouchableOpacity>

            <FlatList
                data={products}
                keyExtractor={(item) => item.id.toString()}
                renderItem={({ item }) => (
                    <View style={styles.card}>
                        <Text>{item.title}</Text>
                        <Text>{item.description}</Text>
                        <Text>{item.quantity}</Text>
                        <View>
                            <TouchableOpacity style={styles.editButton} onPress={() => handleEdit(item)}>
                                <Text style={styles.buttonText}>Modifier</Text>
                            </TouchableOpacity>
                            <TouchableOpacity style={styles.deleteButton} onPress={() => handleDelete(item.id)}>
                                <Text style={styles.buttonText}>Supprimer</Text>
                            </TouchableOpacity>
                        </View>
                    </View>
                )}

            />
        </View>

    )


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