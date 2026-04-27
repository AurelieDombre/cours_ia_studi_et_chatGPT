Bonne idée 👍 — pour faire une API REST avec Django, le standard aujourd’hui c’est **Django REST Framework** (DRF).
Essayer de faire une API REST “à la main” en Django pur est possible, mais vite pénible et fragile.

Je te montre une mise en place **propre, simple et évolutive**.

---

# 🚀 1. Installer DRF

```bash
pip install djangorestframework
```

Dans `settings.py` :

```python
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

---

# 🧱 2. Exemple avec ton modèle Post

On part de ton modèle :

```python
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    tags = models.ManyToManyField("Tag")
```

---

# 🔄 3. Créer un Serializer (équivalent JSON du ModelForm)

👉 `serializers.py`

```python
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
```

---

# ⚙️ 4. Créer une vue API (nouvelle page)

👉 version simple avec ViewSet (recommandée)

```python
from rest_framework.viewsets import ModelViewSet
from .models import Post
from .serializers import PostSerializer

class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
```

👉 Ça te crée automatiquement :

* GET (liste)
* GET (detail)
* POST
* PUT / PATCH
* DELETE

---

# 🌐 5. Configurer les URLs

👉 créer un nouveau fichier `api_urls.py`

```python
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)

urlpatterns = router.urls
```


👉 Ajoute le path de ce fichier dans `urls.py`

```python
from django.urls import path, include

urlpatterns = [
    path('', include('blog.api_urls')),  # 👈 API
    path('accueil', index, name='accueil'),
    ...
]
```

---

# 🎯 Résultat

Tu obtiens une API REST complète :

* `GET /posts/` → liste
* `GET /posts/1/` → détail
* `POST /posts/` → créer
* `PUT /posts/1/` → modifier
* `DELETE /posts/1/` → supprimer

---

# 🧪 6. Tester ton API

Va sur :

```
http://127.0.0.1:8000/api/posts/
```

👉 DRF te donne une **interface web interactive** 🔥

---

# 💡 7. Gérer les relations (Author, Tags)

Par défaut :

* `author` = ID
* `tags` = liste d’IDs

### Option plus lisible :

```python
class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = Post
        fields = '__all__'
```

---

# 🔐 8. Bonus important (sécurité)

Dans `settings.py` :

```python
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ]
}
```

👉 Plus tard tu pourras mettre :

* authentification
* JWT
* permissions

---

# ⚡ 9. Alternative simple (si tu veux comprendre)

Sans ViewSet :

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def post_list(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)
```

---

# 🧠 Résumé

* DRF = standard pour API Django
* Serializer = transforme modèle → JSON
* ViewSet = CRUD automatique
* Router = URLs automatiques

---

