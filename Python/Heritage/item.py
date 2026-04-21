class Item:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    def get_infos_specifiques(self):
        return self.titre, self.auteur

class Livre(Item):
    def __init__(self, titre, auteur, nombre_pages):
        super().__init__(titre, auteur)
        self.nombre_pages = nombre_pages

    def get_infos_specifiques(self):

        return f" {super().get_infos_specifiques()} Nombre de pages : {self.nombre_pages}"

class Magazine(Item):
    def __init__(self, titre, auteur, periodicite):
        super().__init__(titre, auteur)
        self.periodicite = periodicite

    def get_infos_specifiques(self):
        return f" {super().get_infos_specifiques()} {self.periodicite}"

def afficher_info(item):
    print(f"{item.get_infos_specifiques()}")

livre = Livre("Le Petit Prince", "Antoine de Saint-Exupéry", 96)
magazine = Magazine("Nature", "John Smith", "Mensuel")

afficher_info(livre)
afficher_info(magazine)