class Produit:
    def __init__(self, nom, stock):
        self.nom = nom
        self.stock = stock

    def retirer_produit(self, quantite):
        if quantite > self.stock:
            raise ValueError("Stock insuffisant pour retirer cette quantité")
        self.stock -= quantite