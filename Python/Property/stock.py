import Property.product
from typing import List

class Stock:

    def __init__(self):
        self._quantite_stock = 0
        self.list_product = List[Property.product.Product]= []

    def add_product(self, product):
        self.list_product.append(product)


    def calculate_stock(self):
        prix_total = 0
        for product in self.list_product:
            prix_total += product.prix * product.quantite_stock
        return prix_total

    def remove_product(self, product):
        for product in self.list_product:
            if product.product == product:
                self.list_product.remove(product)
                print(f"Produit {product} supprimé ")
                return



