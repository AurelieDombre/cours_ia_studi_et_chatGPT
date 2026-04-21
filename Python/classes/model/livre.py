class Livre:

    def __init__(self, titre : str, auteur : str, page: int):
        self.titre = titre
        self.auteur = auteur
        self.page = page

    def afficher_info(self):
        print(f"Le livre {self.titre}, a été écrit par {self.auteur}. Il contient {self.page} pages")
