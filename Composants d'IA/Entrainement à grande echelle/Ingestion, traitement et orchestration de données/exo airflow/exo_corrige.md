Parfait 👌 on va le faire **ensemble étape par étape**, comme si tu étais en TP.

Je vais te guider de manière simple, et tu peux tester à chaque étape.

---

# 🧩 Étape 1 — créer le fichier DAG

Dans ton dossier :

```bash
airflow-demo/dags/
```

👉 Crée un fichier :

```bash
etl_csv.py
```
Pour générer des données : https://www.mockaroo.com/
---

# 🧠 Étape 2 — structure minimale du DAG

Copie ça pour commencer :

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

with DAG(
    dag_id="etl_csv",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    def hello():
        print("Hello ETL")

    task = PythonOperator(
        task_id="test_task",
        python_callable=hello
    )
```

---

# ▶️ Étape 3 — tester si Airflow voit ton DAG

👉 Fais :

```bash
docker compose restart
```

👉 Va sur :

```
http://localhost:8080
```

👉 Tu dois voir :

```
etl_csv
```

👉 Clique dessus → bouton ▶️ → lance-le

---

👉 Si ça marche = 🔥 parfait
👉 Sinon dis-moi ce que tu vois

---

# 🧩 Étape 4 — ajouter les chemins (comme le cours)

Maintenant on passe au vrai pipeline

Ajoute en haut du fichier :

```python
import pandas as pd

RAW = "/opt/airflow/data/customers.csv"
OUT = "/opt/airflow/data/customers_clean.csv"
REJECTED = "/opt/airflow/data/customers_rejected.csv"
```

---

# 📥 Étape 5 — fonction extract

Ajoute cette fonction :

```python
def extract(**context):
    df = pd.read_csv(RAW)
    context["ti"].xcom_push(key="rows", value=df.to_dict(orient="records"))
```

👉 Explication rapide :

* lit le CSV
* envoie les données à la tâche suivante

---

# 🔄 Étape 6 — fonction transform

Ajoute :

```python
def transform(**context):
    rows = context["ti"].xcom_pull(key="rows", task_ids="extract")
    df = pd.DataFrame(rows)

    # nettoyage
    df["first_name"] = df["first_name"].astype(str).str.strip().str.title()
    df["last_name"] = df["last_name"].astype(str).str.strip().str.title()
    df["city"] = df["city"].astype(str).str.strip().str.title()
    df["email"] = df["email"].astype(str).str.strip()

    # validation
    invalid = df[
        (~df["email"].str.contains("@", na=False)) |
        (df["first_name"] == "") |
        (df["last_name"] == "")
    ]

    valid = df.drop(invalid.index)

    context["ti"].xcom_push(key="valid", value=valid.to_dict(orient="records"))
    context["ti"].xcom_push(key="invalid", value=invalid.to_dict(orient="records"))
```

---

# 📤 Étape 7 — fonction load

```python
def load(**context):
    rows = context["ti"].xcom_pull(key="valid", task_ids="transform")
    if rows:
        pd.DataFrame(rows).to_csv(OUT, index=False)
```

---

# 🚨 Étape 8 — gérer les erreurs

```python
def log_invalid(**context):
    rows = context["ti"].xcom_pull(key="invalid", task_ids="transform")
    if rows:
        pd.DataFrame(rows).to_csv(REJECTED, index=False)
```

---

# 🔗 Étape 9 — connecter les tâches

Remplace ton DAG par :

```python
with DAG(
    dag_id="etl_csv",
    start_date=datetime(2024, 1, 1),
    schedule_interval=None,
    catchup=False,
) as dag:

    t1 = PythonOperator(task_id="extract", python_callable=extract)
    t2 = PythonOperator(task_id="transform", python_callable=transform)
    t3 = PythonOperator(task_id="load", python_callable=load)
    t4 = PythonOperator(task_id="log_invalid", python_callable=log_invalid)

    t1 >> t2 >> [t3, t4]
```

---

# 📁 Étape 10 — ajouter le CSV

Dans :

```bash
airflow-demo/data/customers.csv
```

👉 mets le dataset du cours (ou un simple test)

---

# ▶️ Étape 11 — lancer le pipeline

```bash
docker compose restart
```

Puis :

1. va sur Airflow
2. active le DAG
3. clique ▶️

---

# ✅ Résultat attendu

Dans `data/` tu dois avoir :

```
customers_clean.csv
customers_rejected.csv
```

---

# 🎯 Si ça ne marche pas

Dis-moi :

* ce que tu vois dans Airflow
* ou l’erreur dans les logs

et je te corrige DIRECT 👌

---

