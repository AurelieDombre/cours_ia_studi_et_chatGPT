class Utilisateur:
    # Cette variable de classe est partagee par tous les objets.
    # Elle stocke les utilisateurs selon leur role.
    utilisateurs_par_role = {
        "visiteur": set(),
        "moderateur": set(),
        "administrateur": set(),
    }

    def __init__(self, role: str):
        # Chaque objet connait simplement son role.
        self.role = role

    def ajouter_utilisateur(self, email: str) -> None:
        # On ajoute l'email dans l'ensemble correspondant au role.
        # Un set evite automatiquement les doublons.
        self.utilisateurs_par_role[self.role].add(email)


    def supprimer_utilisateur(self, email: str) -> None:
        # discard supprime l'email s'il existe, sans erreur sinon.
        self.utilisateurs_par_role[self.role].discard(email)

    def lister_utilisateurs(self):
        # sorted permet d'afficher les emails dans un ordre lisible.
        return sorted(self.utilisateurs_par_role[self.role])

    @classmethod
    def compter_utilisateurs(cls) -> int:
        # Cette methode compte tous les utilisateurs de tous les roles.
        return sum(len(utilisateurs) for utilisateurs in cls.utilisateurs_par_role.values())


class Visiteur(Utilisateur):
    def __init__(self):
        # Un visiteur est un Utilisateur avec le role "visiteur".
        super().__init__("visiteur")


class Moderateur(Utilisateur):
    def __init__(self):
        # Un moderateur est un Utilisateur avec le role "moderateur".
        super().__init__("moderateur")


class Administrateur(Utilisateur):
    def __init__(self):
        # Un administrateur est un Utilisateur avec le role "administrateur".
        super().__init__("administrateur")


# Creation de trois objets differents, un par type d'utilisateur.
visiteurs = Visiteur()
moderateurs = Moderateur()
administrateurs = Administrateur()

# Ajout de quelques utilisateurs de demonstration.
visiteurs.ajouter_utilisateur("alice@test.fr")
visiteurs.ajouter_utilisateur("bob@test.fr")
moderateurs.ajouter_utilisateur("claire@test.fr")
administrateurs.ajouter_utilisateur("admin@test.fr")

# Affichage des utilisateurs par role et du total general.
print("Visiteurs :", visiteurs.lister_utilisateurs())
print("Moderateurs :", moderateurs.lister_utilisateurs())
print("Administrateurs :", administrateurs.lister_utilisateurs())
print("Nombre total d'utilisateurs :", Utilisateur.compter_utilisateurs())

# Suppression d'un visiteur.
visiteurs.supprimer_utilisateur("bob@test.fr")

# Nouvel affichage apres suppression.
print("Visiteurs apres suppression :", visiteurs.lister_utilisateurs())
print("Nombre total d'utilisateurs :", Utilisateur.compter_utilisateurs())
