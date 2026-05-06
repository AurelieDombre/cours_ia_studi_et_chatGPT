Voici un **récap clair et structuré** de ton cours sur les API avec AWS et Google Cloud 👇

---

# 🧠 1. Notions de base : API, Front & Back

* Une **API (Interface de Programmation d’Application)** permet :

  * d’échanger des données
  * d’ajouter des fonctionnalités dynamiques
* Une application est composée de :

  * **Front-end** → partie visible
  * **Back-end** → logique + traitement (souvent via API)

👉 Le front appelle l’API pour récupérer ou envoyer des données.

---

# ☁️ 2. Hébergement des API

Deux cas principaux :

### 🔹 API interne

* Front et API sur le même serveur
* Appels via :

  * `localhost`
  * un **port spécifique**
  * un **chemin spécifique**

### 🔹 API externe

* API hébergée séparément :

  * serveur dédié
  * **CAAS** (containers)
  * **SAAS**

---

# ⚙️ 3. CAAS vs SAAS

### 🧩 CAAS (Container as a Service)

* Déploiement via des containers (ex : Docker)

### 💻 SAAS (Software as a Service)

* Application/API accessible comme service web

### ✅ Avantages du SAAS :

* Déploiement simplifié
* Maintenance souvent déléguée
* Sécurité facilitée
* Pas besoin d’être expert DevOps

### ⚠️ Limite :

* Facturation souvent basée sur le **nombre d’appels API**

---

# ☁️ 4. AWS (Amazon Web Services)

### 📌 Présentation

* Lancé en **2002 (public en 2006)**
* Énorme écosystème (hébergement, base de données, stockage…)

### 🔧 API Gateway (service clé)

Permet de :

* créer et gérer des API
* sécuriser les requêtes
* gérer l’authentification
* transformer requêtes/réponses

### 🔌 Types d’API supportés :

* HTTP
* REST
* WebSocket

---

## ⚡ AWS Lambda

* Permet d’exécuter du code sans serveur
* Utilisé avec API Gateway

👉 Fonctionnement :

1. Client → API Gateway
2. API Gateway → Lambda
3. Lambda → réponse

---

## 💰 Tarification

* Gratuit :

  * **1 million de requêtes/mois pendant 12 mois**
* Ensuite :

  * coût basé sur :

    * nombre de requêtes
    * taille des données

---

## 🧪 Exemple

Créer une API “Hello World” :

* API Gateway → crée l’API
* Lambda → contient le code
* Méthode GET → renvoie “Hello World”

---

# 🌐 5. Google Cloud Platform (GCP)

### 📌 Présentation

* Lancé en **2011**
* Infrastructure similaire à Google (très fiable)

---

## 🔧 Gestion des API

### 🏢 Apigee

* Solution entreprise
* gestion + monétisation des API

### 🧰 Service Management API

* Alternative plus simple

---

## 🚀 Déploiement avec App Engine

* Service SAAS pour héberger une API
* Fonctionne avec plusieurs langages (Node.js, etc.)

---

## ⚙️ Fonctionnement global

1. Créer un projet GCP
2. Activer une API
3. Créer des identifiants
4. Développer l’API (ex : Node.js + Express)
5. Déployer avec :

   ```
   gcloud app deploy
   ```

---

## 💰 Tarification GCP

* Pas de gratuité longue comme AWS
* Mais :

  * **300 à 400 $ de crédit (90 jours)**
  * **1 million d’appels suivis gratuitement**

---

# 🔄 6. Comparaison AWS vs GCP

| Critère        | AWS          | Google Cloud       |
| -------------- | ------------ | ------------------ |
| API management | API Gateway  | Apigee             |
| Exécution code | Lambda       | App Engine         |
| Gratuité       | 12 mois      | Crédit 90 jours    |
| Complexité     | Moyenne      | Plus guidé         |
| Popularité     | Très répandu | Très utilisé aussi |

---

# 📌 7. Points essentiels à retenir

* Les API sont **indispensables** aux apps modernes
* Le **SAAS simplifie énormément** le déploiement
* AWS et GCP offrent :

  * hébergement
  * sécurité
  * scalabilité
* Architecture fréquente :

  ```
  Client → API Gateway → Fonction (Lambda / App Engine)
  ```
* Le coût dépend surtout :
  👉 du **nombre d’appels API**

---

# 🎯 Conclusion rapide

👉 Tu dois retenir :

* API = cœur du back-end
* SAAS = solution simple pour déployer
* AWS = très flexible + gratuit au début
* GCP = puissant + crédits de test
* Lambda / App Engine = exécution du code

---

Voici un **schéma visuel simplifié** pour bien comprendre le fonctionnement 👇

---

# 🌐 Architecture d’une API en SAAS

```
        👤 Utilisateur (Front-end)
                 |
                 | Requête HTTP (GET, POST…)
                 ↓
        🌍 API Gateway (AWS / GCP)
        - Sécurité
        - Authentification
        - Gestion des requêtes
                 |
                 ↓
        ⚙️ Fonction (Back-end)
        (AWS Lambda / App Engine)
        - Exécute le code
        - Traite la requête
                 |
                 ↓
        🗄️ Données / Base de données (optionnel)
                 |
                 ↓
        📦 Réponse (JSON, texte…)
                 |
                 ↑
        👤 Retour vers le Front-end
```

---

# 🔁 Version ultra simplifiée

```
Client → API → Code → Réponse
```

---

# ⚖️ Différence AWS vs Google (visuel)

```
AWS :
Client → API Gateway → Lambda → Réponse

Google Cloud :
Client → API (Apigee / Service API) → App Engine → Réponse
```

---

# 🧠 À retenir visuellement

* 🧑‍💻 **Client** = envoie une requête
* 🌐 **API Gateway** = filtre et dirige
* ⚙️ **Fonction** = fait le travail
* 📦 **Réponse** = renvoyée au client

---

