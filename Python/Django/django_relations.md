# 📘 Cours Django ORM : Les relations


---
👉 Un produit a UNE seule catégorie

---

### 🔹 Accès aux données

```python
# Accéder à la catégorie d'un produit
produit = Produit.objects.get(id=1)
print(produit.categorie.nom)

# Accéder aux produits d'une catégorie
categorie = Categorie.objects.get(id=1)
produits = categorie.produit_set.all()
```

---

### 🔹 filter avec relation

```python
# Produits d'une catégorie spécifique
Produit.objects.filter(categorie__nom="Informatique")
```

---

### 🔹 ManyToMany (relation N ↔ N)

Un objet peut être lié à plusieurs autres, et inversement.

```python
class Tag(models.Model):
    nom = models.CharField(max_length=100)

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag)
```

👉 Un produit peut avoir plusieurs tags
👉 Un tag peut appartenir à plusieurs produits

---

### 🔹 Manipulation ManyToMany

```python
produit = Produit.objects.get(id=1)
tag1 = Tag.objects.get(id=1)

# Ajouter
produit.tags.add(tag1)

# Supprimer
produit.tags.remove(tag1)

# Tout supprimer
produit.tags.clear()
```

---

### 🔹 Accès aux relations

```python
# Tous les tags d'un produit
produit.tags.all()

# Tous les produits d'un tag
tag.produit_set.all()
```

---

### 🔹 Bonnes pratiques (performance)

```python
from django.db.models import Prefetch

# ForeignKey (optimisation)
Produit.objects.select_related('categorie')

# ManyToMany (optimisation)
Produit.objects.prefetch_related('tags')
```

👉 évite les requêtes multiples (N+1 problem)

---

## 🧠 Exemple complet avec relations

```python
# récupérer produits + catégorie
produits = Produit.objects.select_related('categorie').all()

for p in produits:
    print(p.nom, p.categorie.nom)

# produits avec tag spécifique
Produit.objects.filter(tags__nom="promo")
```