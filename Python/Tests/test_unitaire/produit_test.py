import unittest
from Tests.test_unitaire.produit import Produit

class TestProduit(unittest.TestCase):

    def test_retirer_produit(self):
        produit = Produit("ProduitA", 10)
        produit.retirer_produit(4)
        self.assertEqual(produit.stock, 6)

    def test_retrait_insuffisant(self):
        produit = Produit("ProduitA", 5)
        with self.assertRaises(ValueError):
            produit.retirer_produit(6)

if __name__ == "__main__":
    unittest.main()
