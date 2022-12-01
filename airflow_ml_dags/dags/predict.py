from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount

from my_utils import (
    PATH_DATA,
    PATH_MODEL,
    PATH_PREDICTS,
    PATH_TARGET,
    PATH_VOLUME
)


default_args = {
    "owner": "airflow",
    "email": ["airflow@example.com"],
    "retries": 1,
    "retry_delay": timedelta(minutes=1),
}

with DAG(
        "predict_daily_data",
        default_args=default_args,
        schedule_interval="@daily",
        start_date=datetime(2022, 11, 29),
) as dag:

    predict = DockerOperator(
        image="airflow-predict",
        command=f"--input-dir {PATH_DATA} --output-dir {PATH_PREDICTS} --model-dir {PATH_MODEL}",
        task_id="docker-airflow-predict",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[Mount(source=PATH_VOLUME, target=PATH_TARGET, type='bind')],
    )

    predict