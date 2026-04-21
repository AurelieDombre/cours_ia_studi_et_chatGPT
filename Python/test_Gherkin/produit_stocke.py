class Produit:
    def __init__(self, nom, stock):
        self.nom = nom
        self.stock = stock

    def retirer_produit(self, quantite):
        if self.stock == 0:
            raise ValueError("Produit en rupture de stock")
        if quantite > self.stock:
            raise ValueError("Stock insuffisant pour retirer cette quantite")
        self.stock -= quantite
