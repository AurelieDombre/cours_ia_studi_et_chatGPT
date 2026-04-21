
class CompteBancaire:

    def __init__(self, titulaire, solde_initial):
        self.titulaire = titulaire
        self.solde = solde_initial

    @property
    def titulaire(self):
        return self._titulaire

    @titulaire.setter
    def titulaire(self, value):
        self._titulaire = value

    @property
    def solde(self):
          return self._solde

    @solde.setter
    def solde(self, solde):
        self._solde = solde



    def depot(self, montant):
        self.solde += montant

    def retrait(self, montant):
        if montant > self.solde:
            raise ValueError("Solde insuffisant")
        self.solde -= montant


