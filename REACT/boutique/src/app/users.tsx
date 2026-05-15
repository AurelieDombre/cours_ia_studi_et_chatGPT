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
                placeholder="E-mail"
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