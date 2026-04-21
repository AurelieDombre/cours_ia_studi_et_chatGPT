class GestionReservation:

    def __init__(self):
        self._reservation = []

    def add(self, reservation):
        self._reservation.append(reservation)

    def remove(self, reservation):
        self._reservation.remove(reservation)

    def toute_reservations(self):
        for reservation in self._reservation:
            reservation.display()

