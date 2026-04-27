# 📘 Cours Django ORM : Méthodes de recherche et boucles

---

## 1. Exemple de modèle

```python
from django.db import models

class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.FloatField()
    stock = models.IntegerField()
    categorie = models.CharField(max_length=100)

    def __str__(self):
        return self.nom
```

---

## 2. Récupération de données

### 🔹 Tout récupérer
```python
produits = Produit.objects.all()
```

### 🔹 get() → récupérer UN SEUL objet
```python
produit = Produit.objects.get(id=1)
```

⚠️ `get()` lève une erreur si :
- aucun résultat
- plusieurs résultats

---

## 3. filter() → filtrer

```python
# Prix exact
Produit.objects.filter(prix=10)

# Prix > 10
Produit.objects.filter(prix__gt=10)

# Prix <= 10
Produit.objects.filter(prix__lte=10)

# Recherche texte
Produit.objects.filter(nom__icontains="phone")

# Conditions multiples
Produit.objects.filter(prix__gt=10, stock__gt=0)
```

---

## 4. exclude()

```python
Produit.objects.exclude(stock=0)
```

---

## 5. Trier avec order_by()

```python
# Croissant
Produit.objects.order_by("prix")

# Décroissant
Produit.objects.order_by("-prix")
```

---

## 6. count()

```python
Produit.objects.count()
```

---

## 7. Boucles

```python
for produit in Produit.objects.all():
    print(produit.nom)
```

### Avec condition
```python
for produit in Produit.objects.filter(stock__gt=0):
    print(produit.nom)
```

---

## 8. values()

```python
produits = Produit.objects.values("nom", "prix")

for p in produits:
    print(p["nom"], p["prix"])
```

---

## 9. first() / last()

```python
Produit.objects.first()
Produit.objects.last()
```

---

## 10. exists()

```python
Produit.objects.filter(stock=0).exists()
```

---

## 11. Agrégations

```python
from django.db.models import Avg, Max

Produit.objects.aggregate(Avg("prix"))
Produit.objects.aggregate(Max("prix"))
```

---

## 12. Bonnes pratiques

❌ Mauvais :
```python
for produit in Produit.objects.all():
    Produit.objects.get(id=produit.id)
```

✅ Bon :
```python
for produit in Produit.objects.all():
    print(produit)
```

---

## 13. Exercices

1. Trouver les produits avec un prix > 50  
2. Compter les produits en stock  
3. Afficher uniquement les noms  
4. Trier par stock décroissant  
5. Vérifier si un produit "Laptop" existe  

---

💡 Astuce : Django ORM = SQL simplifié → chaque méthode correspond à une requête SQL.

---

## 14. Les QuerySets (explication détaillée)

Les QuerySets permettent de récupérer et manipuler les données de la base.
Ils sont **chaînables** et **lazy (évalués à la demande)**.

---

### 🔹 all()
Retourne tous les objets :
```python
MyModel.objects.all()
```

---

### 🔹 filter()
Filtrer selon des conditions :
```python
MyModel.objects.filter(field="value")
```
Recherche mutlicritere :
Il existe une classe qui permets cela : la class Q

```python
from django.db.models import Q
# Nom commence par la lettre G et prénom par la B
Etudiant.objects.filter(Q(nom__startswith='G') | Q(nom__startswith='B'))

#Nom ne commence pas par B ou prenom commence par A
Etudiant.objects.filter(~Q(nom__startswith='B') | Q(nom__startswith='A'))

```

---

### 🔹 exclude()
Exclure des résultats :
```python
MyModel.objects.exclude(field="value")
```

---

### 🔹 order_by()
Trier les résultats :
```python
MyModel.objects.order_by('field')   # croissant
MyModel.objects.order_by('-field')  # décroissant
```

---

### 🔹 get()
Retourne un seul objet :
```python
MyModel.objects.get(id=1)
```
⚠️ Erreur si 0 ou plusieurs résultats

---

### 🔹 values()
Retourne des dictionnaires :
```python
MyModel.objects.values('field1', 'field2')
```

---

### 🔹 values_list()
Retourne des tuples :
```python
MyModel.objects.values_list('field1', 'field2')
```

---

### 🔹 annotate()
Ajoute des calculs par ligne :
```python
from django.db.models import Count

MyModel.objects.values('field').annotate(count=Count('field'))
```

---

### 🔹 aggregate()
Calcule sur tout le QuerySet :
```python
from django.db.models import Avg

MyModel.objects.aggregate(Avg('field'))
```

---

## ⚡ Points importants

- Les QuerySets sont **lazy** → pas exécutés tant qu'on ne les utilise pas
- Ils sont **chaînables** :
```python
MyModel.objects.filter(field="value").order_by("-id")
```
- Chaque QuerySet correspond à une requête SQL

---

## 🧠 Exemple complet

```python
from django.db.models import Avg

produits = Produit.objects.filter(stock__gt=0) \
                          .exclude(prix__lt=5) \
                          .order_by('-prix')

for p in produits:
    print(p.nom)

# moyenne des prix
Produit.objects.aggregate(Avg("prix"))
```

