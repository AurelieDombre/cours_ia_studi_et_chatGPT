class Product:

    def __init__(self, nom : str, prix : int, quantite_stock : int):
        self._nom = nom
        self._prix = prix
        self._quantite_stock = quantite_stock

    @property
    def nom(self):
        return self._nom
    @property
    def prix(self):
        return self._prix
    @property
    def quantite_stock(self):
        return self._quantite_stock

    @nom.setter
    def nom(self, value):
        self._nom = value
    @prix.setter
    def prix(self, value):
        if value < 0:
            raise ValueError('quantite must be >= 0')
        self._prix = value

    @quantite_stock.setter
    def quantite_stock(self, value):
        if value > 1000:
            raise ValueError('quantite must be >= 0')
        self._quantite_stock = value



produit_1 = Product("Produit 1",10,100)
produit_2 = Product("Produit 2",15,150)

for produit in [produit_1, produit_2]:
    print(f"Le produit : {produit.nom} coute : {produit.prix}, quantite : {produit.quantite_stock}")



