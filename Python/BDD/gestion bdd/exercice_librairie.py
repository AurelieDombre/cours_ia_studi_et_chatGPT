import sqlite3

my_db = sqlite3.connect("librairie.sqlite")

my_cursor = my_db.cursor()

# my_cursor.execute("CREATE TABLE livres(titre, auteur, edition, pages)")
#
# my_cursor.execute("CREATE TABLE clients(nom, prenom, telephone)")
#
# my_cursor.execute("""
#     INSERT INTO livres VALUES
#         ('LivreA', 'Auteur 1', 'De Boeck', 273),
#         ('LivreB', 'Auteur 2', 'Gallimard', 156)
#     """)
#
# my_cursor.execute("""
#     INSERT INTO clients VALUES
#         ('Dupont', 'Albert', 02123456789),
#         ('Durand', 'Alexandre', 02123456798)
#     """)
#
# my_cursor.execute("""CREATE TABLE locations(ref,
#             livre,
#             client,
#             date_fin,
#             FOREIGN KEY(livre) REFERENCES livres(titre),
#             FOREIGN KEY(client) REFERENCES clients(nom))""")
#

# my_cursor.execute("""
#     INSERT INTO locations ("ref", "livre", "client", "date_fin") VALUES ('1', 'LivreF', 'Michel', '01/2025')""")
#
# my_cursor.execute("""
#     INSERT INTO locations ("ref", "livre", "client", "date_fin") VALUES ('1', 'LivreA', 'Durand', '12/2024')""")

# my_db.commit()

my_cursor.execute("SELECT nom, telephone FROM locations, clients WHERE locations.client=clients.nom AND locations.livre='LivreA'")
print(my_cursor.fetchall())
