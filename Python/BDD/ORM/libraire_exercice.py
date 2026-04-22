from sqlalchemy import create_engine, Column, Integer, String, types,MetaData, Table
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///LibrairieDatabase.db')
engine.connect()

Base = declarative_base()

class Bibliotheque(Base):
    __tablename__ = 'livres'
    id = Column(Integer, primary_key=True)
    titre = Column(String)
    auteur = Column(String)
    nombre_page = Column(Integer)
    Loue = Column(types.Boolean)

Base.metadata.create_all(engine)

# Creation d'une session
Session = sessionmaker(bind=engine)
session = Session()

# Creation d'un livre
newLivre = Bibliotheque(titre='Livre A', auteur='Auteur AB', nombre_page=123, Loue=True)
session.add(newLivre)

# Commiter la session
session.commit()

# Ajouter le livre
session.add(Bibliotheque(titre='Les aventures de Tom Sawyer', auteur='Mark Twain', nombre_page=133, Loue=False))
# Commiter la session
session.commit()

# livres = session.query(Bibliotheque).all()
# for livre in livres:
#     print(f'titre : {livre.titre}, auteur : {livre.auteur}, nombre : {livre.nombre_page}, Loue : {livre.Loue}')

livre_tom = session.query(Bibliotheque)\
    .filter_by(titre='Les aventures de Tom Sawyer')\
    .first()

if livre_tom:
    print(livre_tom.Loue)

# 1. Livres d’un auteur spécifique
livres_az = session.query(Bibliotheque)\
    .filter(Bibliotheque.auteur == 'Auteur AZ')\
    .all()

for livre in livres_az:
    print(livre.titre)
# ou bien par exemple :
# livres_mark_twain = session.query(Bibliotheque)\
#     .filter_by(auteur='Mark Twain')\
#     .all()

#2. Livres actuellement loués
livres_loues = session.query(Bibliotheque)\
    .filter(Bibliotheque.Loue == True)\
    .all()

for livre in livres_loues:
    print(livre.titre)
# ou
# from sqlalchemy import true
#
# livres_loues = session.query(Bibliotheque)\
#     .filter(Bibliotheque.Loue == true())\
#     .all()

# 3. Livres NON loués
livres_disponibles = session.query(Bibliotheque)\
    .filter(Bibliotheque.Loue == False)\
    .all()

# 4. Combiner plusieurs conditions (AND)
from sqlalchemy import and_

result = session.query(Bibliotheque)\
    .filter(and_(
        Bibliotheque.auteur == 'Mark Twain',
        Bibliotheque.Loue == False
    ))\
    .all()
# Version plus simple (SQLAlchemy combine automatiquement en AND) :
# result = session.query(Bibliotheque)\
#     .filter(
#         Bibliotheque.auteur == 'Mark Twain',
#         Bibliotheque.Loue == False
#     )\
#     .all()

