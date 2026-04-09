from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd


RAW = "/opt/airflow/data/customers.csv"
OUT = "/opt/airflow/data/customers_clean.csv"
REJECTED = "/opt/airflow/data/customers_rejected.csv"

def extract(**context):
    df = pd.read_csv(RAW)
    context["ti"].xcom_push(key="rows", value=df.to_dict(orient="records"))
    
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
    
def load(**context):
    rows = context["ti"].xcom_pull(key="valid", task_ids="transform")
    if rows:
        pd.DataFrame(rows).to_csv(OUT, index=False)
        
def log_invalid(**context):
    rows = context["ti"].xcom_pull(key="invalid", task_ids="transform")
    if rows:
        pd.DataFrame(rows).to_csv(REJECTED, index=False)
        
        
            

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