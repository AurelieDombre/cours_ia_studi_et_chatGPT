class Utilisateur:
    # Variable partagee par tous les utilisateurs.
    nb_total_utilisateurs = 0

    def __init__(self):
        # Chaque objet aura sa propre liste d'emails.
        self.liste_utilisateurs = []

    def ajouter_utilisateur(self, email):
        # On ajoute l'email dans la liste.
        self.liste_utilisateurs.append(email)
        Utilisateur.nb_total_utilisateurs += 1

    def supprimer_utilisateur(self, email):
        # On supprime l'email de la liste s'il existe.
        if email in self.liste_utilisateurs:
            self.liste_utilisateurs.remove(email)
            Utilisateur.nb_total_utilisateurs -= 1

    def afficher_utilisateurs(self):
        return self.liste_utilisateurs

    def compter_utilisateurs(self):
        return Utilisateur.nb_total_utilisateurs


class Visiteur(Utilisateur):
    pass


class Moderateur(Utilisateur):
    pass


class Administrateur(Utilisateur):
    pass


visiteurs = Visiteur()
moderateurs = Moderateur()
administrateurs = Administrateur()

visiteurs.ajouter_utilisateur("alice@test.fr")
visiteurs.ajouter_utilisateur("bob@test.fr")
moderateurs.ajouter_utilisateur("claire@test.fr")
administrateurs.ajouter_utilisateur("admin@test.fr")

print("Visiteurs :", visiteurs.afficher_utilisateurs())
print("Moderateurs :", moderateurs.afficher_utilisateurs())
print("Administrateurs :", administrateurs.afficher_utilisateurs())
print("Nombre total d'utilisateurs :", visiteurs.compter_utilisateurs())

visiteurs.supprimer_utilisateur("bob@test.fr")

print("Visiteurs apres suppression :", visiteurs.afficher_utilisateurs())
print("Nombre total d'utilisateurs :", visiteurs.compter_utilisateurs())
