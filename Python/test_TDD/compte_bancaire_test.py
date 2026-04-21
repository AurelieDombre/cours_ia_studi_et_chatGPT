import unittest
from compte_bancaire import CompteBancaire


class CompteBancaireTest(unittest.TestCase):

    def test_creation_compte(self):
        compte = CompteBancaire(titulaire = "José", solde_initial= 100)
        self.assertEqual(compte.solde, 100)


    def test_depot(self):
        compte = CompteBancaire(titulaire = "José",solde_initial= 100)
        compte.depot(50)
        self.assertEqual(compte.solde, 150)



    def test_retrait(self):
        compte = CompteBancaire(titulaire ="José", solde_initial= 100)
        compte.retrait(30)
        self.assertEqual(compte.solde, 70)



    def test_solde_insuffisant(self):
        compte = CompteBancaire(titulaire ="José", solde_initial=100)
        with self.assertRaises(ValueError):
            compte.retrait(200)



    # Exécution des tests
    if __name__ == "__main__":
        unittest.main()