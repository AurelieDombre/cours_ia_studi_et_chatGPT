# Exemple de requête
---
## Création de la base de donnée, de la table et de la session :

````python
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

````
---

## 🔎 1. Livres d’un auteur spécifique

```python
livres_mark_twain = session.query(Bibliotheque)\
    .filter(Bibliotheque.auteur == 'Mark Twain')\
    .all()

for livre in livres_mark_twain:
    print(livre.titre)
```

👉 Variante plus lisible :

```python
livres_mark_twain = session.query(Bibliotheque)\
    .filter_by(auteur='Mark Twain')\
    .all()
```

---

## 📚 2. Livres actuellement loués

```python
livres_loues = session.query(Bibliotheque)\
    .filter(Bibliotheque.Loue == True)\
    .all()

for livre in livres_loues:
    print(livre.titre)
```

👉 Astuce : plus “Pythonic”

```python
from sqlalchemy import true

livres_loues = session.query(Bibliotheque)\
    .filter(Bibliotheque.Loue == true())\
    .all()
```

---

## 📖 3. Livres NON loués

```python
livres_disponibles = session.query(Bibliotheque)\
    .filter(Bibliotheque.Loue == False)\
    .all()
```

---

## 🔗 4. Combiner plusieurs conditions (AND)

Exemple : livres de Mark Twain **et** non loués

```python
from sqlalchemy import and_

result = session.query(Bibliotheque)\
    .filter(and_(
        Bibliotheque.auteur == 'Mark Twain',
        Bibliotheque.Loue == False
    ))\
    .all()
```

👉 Version plus simple (SQLAlchemy combine automatiquement en AND) :

```python
result = session.query(Bibliotheque)\
    .filter(
        Bibliotheque.auteur == 'Mark Twain',
        Bibliotheque.Loue == False
    )\
    .all()
```

---

## 🔀 5. Conditions OR

Exemple : livres de Mark Twain **OU** loués

```python
from sqlalchemy import or_

result = session.query(Bibliotheque)\
    .filter(or_(
        Bibliotheque.auteur == 'Mark Twain',
        Bibliotheque.Loue == True
    ))\
    .all()
```

---

## 🔍 6. Recherche partielle (LIKE)

Exemple : titres contenant "Tom"

```python
result = session.query(Bibliotheque)\
    .filter(Bibliotheque.titre.like('%Tom%'))\
    .all()
```

---

## 🔢 7. Trier les résultats

```python
from sqlalchemy import desc

livres = session.query(Bibliotheque)\
    .order_by(Bibliotheque.nombre_page)\
    .all()
```

👉 décroissant :

```python
livres = session.query(Bibliotheque)\
    .order_by(desc(Bibliotheque.nombre_page))\
    .all()
```

---

## 🔝 8. Limiter les résultats

```python
livres = session.query(Bibliotheque)\
    .limit(3)\
    .all()
```

---

## 🎯 Exemple complet (réaliste)

👉 "Donne-moi les 5 livres disponibles les plus courts de Mark Twain"

```python
livres = session.query(Bibliotheque)\
    .filter(
        Bibliotheque.auteur == 'Mark Twain',
        Bibliotheque.Loue == False
    )\
    .order_by(Bibliotheque.nombre_page)\
    .limit(5)\
    .all()
```

---

## 🧠 Petit conseil important

Évite de nommer ton champ `Loue` avec une majuscule → en Python on préfère :

```python
loue = Column(Boolean)
```

Ça évite des bugs subtils et rend ton code plus propre.

---

