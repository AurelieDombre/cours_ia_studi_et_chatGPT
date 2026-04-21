from model.reservation import Reservation
from model.gestion_reservations import GestionReservation


gestion = GestionReservation()
reservation = Reservation("Huet", 2, "19/04/2026 à 20h00", True)
reservation1 = Reservation("Alice", 4, "2024-10-05 20:00", True)
reservation2 = Reservation("Bob", 2, "2024-10-06 19:30")

gestion.add(reservation)
gestion.add(reservation1)
gestion.add(reservation2)


gestion.toute_reservations()