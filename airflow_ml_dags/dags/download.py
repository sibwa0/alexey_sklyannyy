from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount

from airflow_ml_dags.utils import (
    PATH_DATA,
    PATH_TARGET,
    PATH_VOLUME
)

default_args = {
    "owner": "airflow",
    "email": ["airflow@example.com"],
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
        "download_daily_data",
        default_args=default_args,
        schedule_interval="@daily",
        start_date=datetime(2022, 11, 29),
) as dag:
    download_data = DockerOperator(
        image="airflow-download",
        command=f"--input-dir {PATH_DATA}",
        task_id="docker-airflow-download",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[Mount(source=PATH_VOLUME, target=PATH_TARGET, type='bind')],
    )

    download_data