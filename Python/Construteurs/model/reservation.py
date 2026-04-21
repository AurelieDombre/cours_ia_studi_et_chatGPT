
class Reservation:
    def __init__(self, client : str, personnes : int, date_heure : str, confirmee : bool = False):
        self.client = client
        self.personnes = personnes
        self.date_heure = date_heure
        self.confirmee = confirmee


    def display(self):
        statut = "Confirmée" if self.confirmee else "Non confirmée"
        print(
            f"Client : {self.client}, Nombre de personnes : {self.personnes}, Date et heure : {self.date_heure}, Statut : {statut}")


    def confirme(self):
        self.confirmee = True

    def cancel(self):
        self.confirmee = False
        print(f"La réservation de {self.client} a été annulée.")



