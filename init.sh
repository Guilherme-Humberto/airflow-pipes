AIRFLOW_VERSION=2.3.2 && PYTHON_VERSION=3.10 && CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
pip install "apache-airflow[postgres,celery,redis]==${AIRFLOW_VERSION}" --constraint "${CONSTRAINT_URL}"
echo "Instalação do airflow finalizada!!"