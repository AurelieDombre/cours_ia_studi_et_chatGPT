from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///MyDatabase.db')
engine.connect()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)

Base.metadata.create_all(engine)

# Creation d'une session
Session = sessionmaker(bind=engine)
session = Session()

# Creation d'un utilisateur
newUser = User(username='user1', email='user1@userDomain.com', password='1234')

# Ajouter l'utilisateur à la session
session.add(newUser)

# Commiter la session
session.commit()

# Appel des utilisateurs de la BDD
users = session.query(User).all()

for user in users:
    print(f'ID: {user.id}, Username: {user.username}, Email: {user.email}, Password: {user.password}')