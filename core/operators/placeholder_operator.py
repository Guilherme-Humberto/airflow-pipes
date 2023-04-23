import sys
sys.path.append("core")

import json
from os.path import join
from pathlib import Path
from requests import request as http
from airflow.models import BaseOperator, DagRun

class PlaceholderOpareator(BaseOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def get_dag_runs(self, dag_id, state=None):
        dag_runs = list()
        state = state.lower() if state else None
        for run in DagRun.find(dag_id=dag_id, state=state):
            dag_runs.append(run.id)

        return dag_runs

    def create_parent_folder(self, file_path):
        Path(file_path).parent.mkdir(
            parents=True, 
            exist_ok=True
        )

    def register_user(self, users, file_path): 
        self.create_parent_folder(file_path)

        def write_user(user):
            json.dump(user, output_file, ensure_ascii=False)
            output_file.write("\n")

        with open(file_path, "w") as output_file:
            for user in users: write_user(user)
                

    def execute(self, context):
        dag_id = context['dag'].dag_id
        dag_runs = self.get_dag_runs(dag_id)
        dag_count = len(dag_runs)

        response = http(method='GET', url=f'https://randomuser.me/api/?results=1&page={dag_count}')
        users = response.json()

        file_path = join(
            "datalake/users",
            f"user_{dag_count}.json"
        )

        return self.register_user(users['results'], file_path)