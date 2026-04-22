import sqlite3

my_db = sqlite3.connect("database.sqlite")

# Une fois que le cursor est créé, on peut créer des requêtes
my_cursor = my_db.cursor()

# my_cursor.execute("CREATE TABLE utilisateur(pseudo,email,prenom)")

# my_cursor.execute("""
#     INSERT INTO utilisateur VALUES
#         ('pseudo-user1', 'user1@domain.com', 'Jean'),
#         ('pseudo-user2', 'user2@domain.com', 'David')
#     """)

# my_db.commit()

# my_cursor.execute("SELECT * FROM utilisateur WHERE prenom='David' ")
# print(my_cursor.fetchall())

for row in my_cursor.execute("SELECT email, prenom FROM utilisateur"):
    print(row)

