# Guide Complet — Créer un Bundle de Chatbots Réutilisables

## Objectif

Créer une architecture de chatbot moderne, modulaire et réutilisable basée sur :

* Frontend React + Vite
* Backend FastAPI
* Ollama (local)
* Switch OpenAI / Mistral / Ollama
* Analyse d'image
* Analyse vocale
* Recherche locale de fichiers
* Système de prompts versionnés
* Architecture multi-bots
* Mode démo configurable

Ce guide est conçu comme un cours étape par étape.

---

# 1. Architecture finale du projet

```txt
chatbot_bundle/
│
├── backend/
│   ├── core/
│   ├── bots/
│   ├── api/
│   ├── prompts/
│   ├── services/
│   ├── models/
│   ├── config/
│   ├── tests/
│   └── main.py
│
├── frontend/
│   ├── src/
│   ├── components/
│   ├── services/
│   └── App.jsx
│
├── data/
├── scripts/
├── docker/
├── .env
├── requirements.txt
└── README.md
```

---

# 2. Technologies utilisées

## Frontend

| Technologie         | Usage             |
| ------------------- | ----------------- |
| React               | Interface chatbot |
| Vite                | Build rapide      |
| TailwindCSS         | UI moderne        |
| Axios               | Requêtes API      |
| Zustand (optionnel) | State global      |
| Tauri (optionnel)   | App desktop       |

---

## Backend

| Technologie  | Usage                 |
| ------------ | --------------------- |
| FastAPI      | API backend           |
| Pydantic     | Validation            |
| Uvicorn      | Serveur               |
| Ollama       | LLM local             |
| OpenAI SDK   | GPT                   |
| Mistral SDK  | Mistral               |
| Transformers | IA locale             |
| Pillow       | Traitement image      |
| Vosk         | Reconnaissance vocale |
| pyttsx3      | Synthèse vocale       |

---

# 3. Installation du projet

## Installer Python

Télécharger :

* [https://www.python.org/downloads/](https://www.python.org/downloads/)

Vérifier :

```bash
python --version
```

---

## Installer Node.js

Télécharger :

* [https://nodejs.org/](https://nodejs.org/)

Vérifier :

```bash
node -v
npm -v
```

---

# 4. Installer Ollama

## Télécharger

* [https://ollama.com/](https://ollama.com/)

---

## Installer un modèle

```bash
ollama pull llama3
```

Autres modèles :

```bash
ollama pull mistral
ollama pull phi3
ollama pull gemma
```

---

## Tester Ollama

```bash
ollama run llama3
```

---

# 5. Création du backend FastAPI

## Initialisation

```bash
mkdir chatbot_bundle
cd chatbot_bundle
mkdir backend
cd backend
```

---

## Créer l'environnement virtuel

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux/Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# 6. Installer les dépendances backend

```bash
pip install fastapi uvicorn pydantic requests python-dotenv
```

---

## Support OpenAI

```bash
pip install openai
```

---

## Support Mistral

```bash
pip install mistralai
```

---

## Analyse IA locale

```bash
pip install transformers torch
```

---

## Vision

```bash
pip install pillow
```

---

## Audio

```bash
pip install vosk pyttsx3 sounddevice
```

---

# 7. Fichier .env

Créer :

```txt
backend/.env
```

---

## Exemple

```env
USE_OLLAMA=true
USE_OPENAI=false
USE_MISTRAL=false

OLLAMA_MODEL=llama3

OPENAI_API_KEY=xxxxx
MISTRAL_API_KEY=xxxxx

USE_DEMO_MODE=false
USE_VISION=true
USE_VOICE=true
```

---

# 8. Core réutilisable

## Structure du core

```txt
core/
├── llm_client.py
├── prompt_manager.py
├── toggle.py
├── schema.py
├── vision.py
├── voice.py
├── sentiment.py
└── file_search.py
```

---

# 9. Gestion des toggles

## toggle.py

```python
TRUE_SET = {"1", "true", "yes", "on"}
FALSE_SET = {"0", "false", "no", "off"}


def env_bool(value: str, default=False):
    if value is None:
        return default

    v = value.strip().lower()

    if v in TRUE_SET:
        return True

    if v in FALSE_SET:
        return False

    return default
```

---

# 10. Gestion des prompts

## prompt_manager.py

```python
from pathlib import Path

PROMPT_DIR = Path("prompts")


def load_prompt(name: str):
    path = PROMPT_DIR / name
    return path.read_text(encoding="utf-8")
```

---

# 11. Client LLM universel

## llm_client.py

Architecture importante :

* Un seul client
* Plusieurs providers
* Switch automatique

---

## Exemple simplifié

```python
import os
import requests
from openai import OpenAI
from mistralai.client import MistralClient

USE_OLLAMA = os.getenv("USE_OLLAMA") == "true"
USE_OPENAI = os.getenv("USE_OPENAI") == "true"
USE_MISTRAL = os.getenv("USE_MISTRAL") == "true"


class LLMClient:

    def ask(self, prompt: str):

        if USE_OLLAMA:
            return self.ask_ollama(prompt)

        if USE_OPENAI:
            return self.ask_openai(prompt)

        if USE_MISTRAL:
            return self.ask_mistral(prompt)

        return "No provider enabled"

    def ask_ollama(self, prompt):

        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )

        return response.json()["response"]
```

---

# 12. Schémas Pydantic

## schema.py

```python
from pydantic import BaseModel
from typing import List


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    messages: List[Message]
```

---

# 13. Création du moteur de chat

## chat_engine.py

```python
from core.llm_client import LLMClient


class ChatEngine:

    def __init__(self):
        self.client = LLMClient()

    def chat(self, message: str):

        prompt = f"""
        User: {message}
        Assistant:
        """

        return self.client.ask(prompt)
```

---

# 14. API FastAPI

## main.py

```python
from fastapi import FastAPI
from core.chat_engine import ChatEngine
from core.schema import ChatRequest

app = FastAPI()
engine = ChatEngine()


@app.post("/chat")
def chat(req: ChatRequest):

    user_message = req.messages[-1].content

    reply = engine.chat(user_message)

    return {
        "reply": reply
    }
```

---

# 15. Lancer le backend

```bash
uvicorn main:app --reload
```

API :

```txt
http://127.0.0.1:8000/docs
```

---

# 16. Création du frontend React

## Initialisation

```bash
npm create vite@latest frontend
```

Choisir :

```txt
React
JavaScript
```

---

## Installer les dépendances

```bash
cd frontend
npm install
npm install axios
```

---

# 17. Installation Tailwind

```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init -p
```

---

## Configuration Tailwind

```js
content: [
  "./index.html",
  "./src/**/*.{js,ts,jsx,tsx}",
]
```

---

# 18. Chat UI

## App.jsx

```jsx
import { useState } from "react"
import axios from "axios"

function App() {

  const [messages, setMessages] = useState([])
  const [query, setQuery] = useState("")

  async function handleSend() {

    const newMessages = [
      ...messages,
      {
        role: "user",
        content: query
      }
    ]

    setMessages(newMessages)

    const response = await axios.post(
      "http://localhost:8000/chat",
      {
        messages: newMessages
      }
    )

    setMessages([
      ...newMessages,
      {
        role: "assistant",
        content: response.data.reply
      }
    ])

    setQuery("")
  }

  return (
    <div>
      <h1>ChatBot</h1>

      {messages.map((msg, i) => (
        <div key={i}>
          <b>{msg.role}</b>: {msg.content}
        </div>
      ))}

      <input
        value={query}
        onChange={(e) => setQuery(e.target.value)}
      />

      <button onClick={handleSend}>
        Envoyer
      </button>
    </div>
  )
}

export default App
```

---

# 19. Analyse de sentiment

## sentiment.py

```python
from transformers import pipeline

_sentiment_pipeline = None


def get_pipeline():
    global _sentiment_pipeline

    if _sentiment_pipeline is None:
        _sentiment_pipeline = pipeline(
            "sentiment-analysis"
        )

    return _sentiment_pipeline


def analyze_sentiment(text: str):

    pipe = get_pipeline()

    return pipe(text)
```

---

# 20. Analyse d'image

## vision.py

```python
from PIL import Image


def analyze_image(path: str):

    image = Image.open(path)

    return {
        "width": image.width,
        "height": image.height,
        "mode": image.mode
    }
```

---

# 21. Voice Chat

## voice.py

```python
import pyttsx3

engine = pyttsx3.init()


def speak(text: str):
    engine.say(text)
    engine.runAndWait()
```

---

# 22. Recherche de fichiers

## file_search.py

```python
from pathlib import Path


def search_files(query: str, base_path="."):

    results = []

    for path in Path(base_path).rglob("*"):

        if query.lower() in path.name.lower():
            results.append(str(path))

    return results
```

---

# 23. Architecture multi-bots

## Structure

```txt
bots/
├── file_bot/
├── image_bot/
├── support_bot/
├── notes_bot/
└── assistant_bot/
```

---

# 24. Structure d'un bot

```txt
bots/file_bot/
├── handler.py
├── router.py
├── schemas.py
└── prompt_v1.txt
```

---

# 25. Handler métier

## handler.py

```python
from core.file_search import search_files


def handle(query: str):

    files = search_files(query)

    return {
        "reply": f"{len(files)} fichiers trouvés",
        "files": files
    }
```

---

# 26. Router FastAPI

## router.py

```python
from fastapi import APIRouter
from .handler import handle

router = APIRouter()


@router.post("/chat")
def chat(data: dict):

    query = data["query"]

    return handle(query)
```

---

# 27. Brancher les bots

## main.py

```python
from bots.file_bot.router import router as file_router

app.include_router(file_router)
```

---

# 28. Ajouter OpenAI

## Exemple

```python
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)
```

---

# 29. Ajouter Mistral

## Exemple

```python
from mistralai.client import MistralClient

client = MistralClient(
    api_key=os.getenv("MISTRAL_API_KEY")
)
```

---

# 30. Ajouter Tauri (desktop)

## Installation

```bash
npm install --save-dev @tauri-apps/cli
```

---

## Initialisation

```bash
npx tauri init
```

---

# 31. Ajouter Docker

## Dockerfile backend

```dockerfile
FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

# 32. Docker Compose

```yaml
version: '3'

services:

  backend:
    build: ./backend
    ports:
      - "8000:8000"

  frontend:
    build: ./frontend
    ports:
      - "5173:5173"
```

---

# 33. Bonnes pratiques importantes

## Séparer :

* Core réutilisable
* Logique métier
* UI
* Prompts
* Providers LLM

---

## Toujours prévoir :

* fallback local
* mode demo
* logs
* timeout
* blacklist
* gestion erreurs

---

## Versionner les prompts

Exemple :

```txt
prompt_v1.txt
prompt_v1.1.txt
prompt_v2.txt
```

---

# 34. Features bonus avancées

## Suggestions automatiques

Le bot peut proposer :

* commandes rapides
* actions
* boutons contextuels
* suggestions IA

---

## Mémoire conversationnelle

Ajouter :

* historique
* résumé de conversation
* mémoire persistante

---

## RAG local

Ajouter :

* ChromaDB
* FAISS
* embeddings
* PDF parsing

---

## Multi-agent

Exemple :

* agent vision
* agent code
* agent recherche
* agent assistant

---

# 35. Roadmap idéale

## Niveau 1

* Chat simple
* Ollama
* React
* FastAPI

---

## Niveau 2

* Multi-provider
* Prompts versionnés
* Bots modulaires

---

## Niveau 3

* Vision
* Voice
* Sentiment
* Suggestions

---

## Niveau 4

* RAG
* Mémoire
* Multi-agent
* Docker
* Tauri

---

# 36. Architecture finale recommandée

```txt
Frontend React/Tauri
        ↓
FastAPI API Layer
        ↓
Chat Engine
        ↓
LLM Provider Layer
        ↓
Ollama / OpenAI / Mistral
        ↓
Services IA
(vision, voice, sentiment, rag)
        ↓
Handlers métiers
        ↓
Données
(files, DB, APIs)
```

---

# 37. Conseils de développement

## Commencer petit

Ne fais pas tout d'un coup.

Ordre recommandé :

1. Chat simple
2. Ollama
3. Frontend
4. Multi-provider
5. File search
6. Vision
7. Voice
8. RAG
9. Multi-bots

---

## Toujours tester les modules séparément

Exemple :

* tester Ollama seul
* tester FastAPI seul
* tester React seul
* tester vision seule

---

## Créer un vrai socle réutilisable

Ton objectif n'est pas :

❌ créer un seul chatbot

Ton objectif est :

✅ créer un framework de chatbots réutilisable

---

# 38. Conclusion

Avec cette architecture tu peux créer :

* assistant local
* moteur de recherche fichiers
* assistant vocal
* chatbot SAV
* chatbot e-commerce
* assistant code
* assistant notes
* IA desktop
* IA web
* IA multimodale

Le plus important :

* modularité
* séparation des responsabilités
* abstraction des providers
* prompts versionnés
* architecture scalable
---

Je t’ai préparé un guide complet structuré comme un vrai cours de développement pour créer un bundle de chatbots modulaires avec :

* FastAPI
* React + Vite
* Ollama
* Switch OpenAI / Mistral
* Analyse d’image
* Voice chat
* Recherche de fichiers
* Architecture multi-bots
* Core réutilisable
* Docker
* Tauri
* Prompt management
* Vision / sentiment / suggestions

Le guide est pensé comme une base de framework réutilisable, inspirée directement des patterns communs de tes projets C3PO et Bon Vivant.

