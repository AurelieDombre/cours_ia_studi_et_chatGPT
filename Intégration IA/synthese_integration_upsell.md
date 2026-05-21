# Synthèse détaillée du cours : Création et intégration d’une fonction Upsell IA dans un e-commerce

Le cours présente la conception d’une fonctionnalité **Upsell IA** pour un site e-commerce, depuis la logique métier jusqu’à l’intégration frontend/backend, en passant par les problématiques de performance et de déploiement. 

---

# 1. Objectif de l’Upsell IA

L’**upsell** consiste à proposer à un client :

* un produit complémentaire,
* ou une version supérieure,
* afin d’augmenter la valeur de sa commande. 

## Exemple

Si un client achète :

* du fromage,
* ou un brunch,

l’IA peut suggérer :

* une bouteille de vin,
* un dessert,
* ou un produit associé.

L’objectif principal est d’augmenter le **panier moyen**.

---

# 2. Notion de panier moyen

Le panier moyen représente :

> la dépense moyenne d’un client par commande. 

## Formule

\text{Panier moyen} = \frac{\text{Chiffre d'affaires}}{\text{Nombre de commandes}}

## Exemple

* Chiffre d’affaires : 10 000 €
* Nombre de commandes : 200

Donc :

\frac{10000}{200}=50

Le panier moyen est donc de **50 €**. 

Le cours insiste sur le fait qu’une simple suggestion pertinente peut générer des milliers d’euros supplémentaires sur une année.

---

# 3. Architecture générale du projet

Le système est séparé en deux parties :

## Backend

Technologies utilisées :

* Python
* FastAPI
* Pydantic
* Llama.cpp
* modèle Mistral GGUF 

Le backend :

* reçoit le panier,
* construit un prompt IA,
* interroge le modèle,
* retourne une suggestion.

---

## Frontend

Technologies utilisées :

* React
* Vite
* Tailwind CSS
* React Router 

Le frontend :

* affiche le panier,
* permet d’ajouter des produits,
* appelle l’API upsell,
* affiche la suggestion IA.

---

# 4. Le rôle central du prompt versionné

Le cours insiste fortement sur la notion de **prompt versionné**. 

## Pourquoi versionner les prompts ?

Parce qu’en IA :

* la formulation du prompt influence fortement les réponses,
* il faut pouvoir tester différentes formulations,
* revenir en arrière si une version est moins performante.

## Exemple de fichier

```txt
upsell_prompt_v1.0.txt
```

## Prompt utilisé

```txt
You are an assistant IA. A customer has these items in the cart: {cart_items}.
Suggest one complementary product and briefly explain why.
```



Le prompt est écrit en anglais car les modèles open source comprennent généralement mieux l’anglais.

---

# 5. Centralisation des prompts

Le chargement des prompts est centralisé dans un fichier :

```python
prompt_manager.py
```

## Objectif

Éviter :

* la duplication du code,
* les erreurs,
* le chargement manuel des prompts.

## Fonction créée

```python
def load_prompt(prompt_filename: str) -> str:
```

Cette fonction :

1. construit le chemin du fichier,
2. ouvre le fichier texte,
3. lit son contenu,
4. retourne le prompt. 

## Avantages

* maintenance simplifiée,
* ajout facile de nouvelles versions,
* architecture plus propre.

---

# 6. Intégration du modèle IA

Le modèle utilisé est :

```python
mistral-7b-q4_k_m.gguf
```

chargé via :

```python
from llama_cpp import Llama
```



## Paramètres importants

```python
llm = Llama(
    model_path=MODEL_PATH,
    n_gpu_layers=16,
    n_threads=4
)
```

### Signification

* `model_path` : emplacement du modèle,
* `n_gpu_layers` : nombre de couches exécutées sur le GPU,
* `n_threads` : nombre de threads CPU utilisés.

---

# 7. Fonction principale : get_upsell()

La logique métier principale est :

```python
def get_upsell(cart_items: list[str]) -> dict:
```

## Fonctionnement

### Étape 1 : chargement du prompt

```python
prompt_template = load_prompt(PROMPT_UPSELL)
```

### Étape 2 : insertion des produits du panier

```python
prompt = prompt_template.replace("{cart_items}", ", ".join(cart_items))
```

### Étape 3 : appel du modèle IA

```python
result = llm(prompt, max_tokens=50)
```

### Étape 4 : retour de la suggestion

```python
return {"suggestion": result["choices"][0]["text"].strip()}
```



---

# 8. Création de l’API FastAPI

Le backend expose une route :

```python
@app.post("/upsell")
```



## Fonctionnement

Le frontend envoie :

```json
{
  "cart_items": [...]
}
```

Le backend :

1. récupère les produits,
2. appelle `get_upsell()`,
3. retourne une suggestion.

---

# 9. Validation des données avec Pydantic

Deux schémas sont créés :

## Requête

```python
class UpsellRequest(BaseModel):
    cart_items: List[str]
```

## Réponse

```python
class UpsellResponse(BaseModel):
    suggestion: str
```



## Intérêt

Pydantic garantit :

* la structure des données,
* la validation automatique,
* des échanges frontend/backend fiables.

---

# 10. Intégration Frontend React

Le frontend ajoute :

* une nouvelle route `/upsell`,
* une page dédiée,
* un composant `Upsell.jsx`.



---

# 11. Fonctionnement du composant React

Le composant permet :

## Gestion du panier

L’utilisateur peut :

* ajouter des produits rapides,
* saisir un produit manuellement,
* supprimer des produits.

## Appel API

```javascript
fetch("http://localhost:8000/upsell")
```

Le panier est envoyé via :

```javascript
body: JSON.stringify({ cart_items: cart })
```



---

# 12. Affichage des suggestions IA

Lorsque la réponse est reçue :

```javascript
setSuggestion(data.suggestion)
```

La suggestion est ensuite :

* affichée à l’écran,
* ajoutable au panier via un bouton.

---

# 13. Tests et exécution

## Backend

```bash
uvicorn api.main:app --reload
```

## Frontend

```bash
npm run dev
```



Le système doit alors générer des recommandations personnalisées. 

---

# 14. Limites de la V1

Le cours explique que la V1 fonctionne :

* pour une démonstration,
* ou un petit volume d’utilisateurs.

Mais plusieurs problèmes apparaissent en production :

* lenteur,
* surcharge serveur,
* latence,
* mauvaise expérience utilisateur. 

---

# 15. Importance de la performance

Le cours rappelle qu’en e-commerce :

> au-delà de 3 secondes de latence sur une page de paiement, le taux d’abandon augmente fortement. 

Cela peut provoquer :

* perte de clients,
* baisse du taux de conversion,
* perte de confiance.

---

# 16. Solutions de montée en charge

## A. Serveur GPU dédié

Exemples :

* OVHcloud
* AWS 

### Avantages

* calculs IA plus rapides,
* traitement parallèle,
* meilleure stabilité,
* gestion de nombreux utilisateurs.

### Inconvénients

* coût d’infrastructure,
* maintenance plus complexe.

---

## B. API cloud IA

Exemples :

* OpenAI
* Mistral API 

### Avantages

* intégration rapide,
* pas besoin d’héberger le modèle,
* montée en charge automatique.

### Inconvénients

* coût par requête,
* dépendance à un prestataire,
* confidentialité des données,
* contraintes CNIL.

---

## C. File d’attente (queue)

Principe :

* les requêtes sont traitées dans l’ordre,
* cela évite les crashs.

### Avantage

* meilleure stabilité.

### Inconvénient

* augmentation de la latence utilisateur. 

---

# 17. Taux de conversion

Le cours définit le taux de conversion comme :

> le pourcentage de visiteurs qui réalisent l’action attendue. 

## Formule

\text{Taux de conversion} = \frac{\text{Nombre de conversions}}{\text{Nombre total de visiteurs}} \times 100

## Exemple

* 1000 visiteurs,
* 50 achats :

\frac{50}{1000}\times100=5%

---

# 18. Recommandations pour une V2

Le cours conseille :

## Technique

* utiliser GPU ou API cloud,
* tester différents prompts,
* limiter les abus,
* gérer les erreurs,
* mettre en place une queue.

## Produit

* tester avant déploiement,
* mesurer la latence,
* surveiller l’expérience utilisateur.

## Sécurité et conformité

* respecter la CNIL,
* limiter les données envoyées,
* informer les utilisateurs.



---

# 19. Concepts essentiels à retenir

| Concept                    | Définition                           |
| -------------------------- | ------------------------------------ |
| Upsell                     | Suggestion de produit complémentaire |
| Panier moyen               | Dépense moyenne par commande         |
| Prompt versionné           | Prompt IA sauvegardé par version     |
| Centralisation des prompts | Gestion unique des prompts           |
| Serveur GPU                | Infrastructure optimisée IA          |
| API cloud                  | IA externalisée                      |
| Queue                      | File d’attente des requêtes          |

---

# 20. Conclusion générale

Ce cours montre comment :

* concevoir une fonctionnalité IA concrète,
* structurer proprement un projet IA,
* intégrer IA + FastAPI + React,
* gérer les prompts intelligemment,
* préparer un passage en production.

L’idée principale est qu’une fonctionnalité IA ne se limite pas au modèle :

* l’architecture,
* la performance,
* la maintenance,
* la scalabilité,
* et l’expérience utilisateur

sont tout aussi importantes que la qualité des suggestions générées par l’IA.

# Qu'est ce que : * `n_gpu_layers`, `n_threads` ?

Ces deux paramètres servent à régler **comment le modèle IA utilise les ressources de ton ordinateur** lorsqu’il génère une réponse.

Dans ton cours, on a :

```python
llm = Llama(
    model_path=MODEL_PATH,
    n_gpu_layers=16,
    n_threads=4
)
```

---

# 1. `n_gpu_layers`

## Définition

```python
n_gpu_layers = 16
```

Cela signifie :

> “Le modèle IA va exécuter 16 couches du réseau neuronal sur la carte graphique (GPU).”

---

## C’est quoi une “couche” ?

Un modèle IA comme Mistral est composé de nombreuses couches de calcul.

Chaque couche :

* analyse le texte,
* transforme les données,
* affine la compréhension,
* puis transmet le résultat à la couche suivante.

Tu peux imaginer ça comme :

```txt
Texte utilisateur
   ↓
Couche 1
   ↓
Couche 2
   ↓
Couche 3
   ↓
...
   ↓
Réponse finale
```

---

## Pourquoi utiliser le GPU ?

Le GPU est extrêmement rapide pour faire :

* beaucoup de calculs en parallèle,
* des opérations mathématiques massives.

Donc :

* plus tu mets de couches sur le GPU,
* plus l’IA répond vite.

---

## Exemple concret

### Sans GPU

Tout est calculé par le processeur (CPU) :

* plus lent,
* surtout avec de gros modèles.

### Avec GPU

Une partie des calculs est envoyée à la carte graphique :

* génération plus rapide,
* moins de charge CPU.

---

## Attention

Mettre trop de couches sur le GPU peut :

* saturer la mémoire vidéo (VRAM),
* faire planter le chargement du modèle.

Donc la valeur dépend :

* de ta carte graphique,
* de sa mémoire,
* de la taille du modèle.

---

# 2. `n_threads`

## Définition

```python
n_threads = 4
```

Cela signifie :

> “Le modèle peut utiliser 4 threads du processeur en parallèle.”

---

## C’est quoi un thread ?

Un thread est une “mini tâche” exécutée par le processeur.

Ton CPU possède :

* plusieurs cœurs,
* capables d’exécuter plusieurs threads simultanément.

---

## Exemple

Si ton processeur possède :

* 8 threads disponibles,

et que tu mets :

```python
n_threads = 4
```

alors le modèle utilisera seulement 4 threads CPU.

---

## Pourquoi c’est utile ?

Plus de threads =

* plus de calculs parallèles,
* meilleure vitesse de traitement.

Mais :

Trop de threads peut :

* surcharger le CPU,
* ralentir le reste du PC,
* parfois diminuer les performances.

---

# Résumé simple

| Paramètre      | Sert à quoi ?                     | Plus la valeur est grande…         |
| -------------- | --------------------------------- | ---------------------------------- |
| `n_gpu_layers` | Utilisation de la carte graphique | plus l’IA est rapide               |
| `n_threads`    | Utilisation du processeur         | plus le CPU travaille en parallèle |

---

# Exemple imagé

Imagine une cuisine :

## CPU = quelques chefs très polyvalents

Ils savent tout faire mais travaillent un peu plus lentement.

## GPU = énorme brigade spécialisée

Elle peut faire des milliers d’actions simples en même temps très rapidement.

Le paramètre :

```python
n_gpu_layers
```

dit :

> “Combien de travail j’envoie à la brigade spécialisée ?”

Et :

```python
n_threads
```

dit :

> “Combien de chefs CPU travaillent en parallèle ?”

---

# En pratique

## Petit PC sans carte graphique puissante

```python
n_gpu_layers = 0
```

→ tout tourne sur CPU.

---

## PC gamer avec GPU NVIDIA

```python
n_gpu_layers = 20
```

→ une partie importante tourne sur GPU.

---

# Ce qu’il faut retenir pour ton cours

Le cours cherche à :

* accélérer la génération IA,
* répartir intelligemment les calculs,
* optimiser les performances du modèle Mistral local.
