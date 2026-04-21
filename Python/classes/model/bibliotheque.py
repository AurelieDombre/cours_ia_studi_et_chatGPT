from typing import List

from classes.model.livre import Livre


class Bibliotheque:

    def __init__(self):
        self.livres : List[Livre] = []

    def ajouter_livre(self, livre : Livre):

        for l in self.livres:
            if livre.titre == l.titre:
                print(f"Le livre {livre.titre} existe déjà.")
                return

            # Ajouter un livre
            self.livres.append(livre)
            print(f"Le livre {livre.titre} a été ajouter")


    def liste_livres(self):
        if self.livres:
            print(f"Livres dans la bibliothèque : ")

            for livre in self.livres:
                livre.afficher_info()
        else:
            print("La bibliothèque est vide.")
