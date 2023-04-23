import sys
sys.path.append("core")

from airflow.models import DAG
from airflow.utils.dates import days_ago
from operators.placeholder_operator import PlaceholderOpareator

with DAG(
    dag_id = "PlaceholderDAG", 
    start_date=days_ago(1), 
    schedule_interval="@daily"
) as dag:
    task_1 = PlaceholderOpareator(
        task_id='placeholder_task_1'
    )