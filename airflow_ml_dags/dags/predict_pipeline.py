from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount

from utils import (
    PATH_MODEL,
    PATH_PREDICTS,
    PATH_TARGET,
    PATH_VOLUME,
    PATH_SPLIT_DATA,
    PATH_DATA,
    SIZE_SPLIT,
    RANDOM_STATE,
    default_args
)


with DAG(
        "predict_daily_data",
        default_args=default_args,
        schedule_interval="@daily",
        start_date=datetime(2022, 11, 25),
) as dag:
    split_data = DockerOperator(
        image="airflow-split",
        command=f"--input-dir {PATH_DATA} --output-dir {PATH_SPLIT_DATA} --size {SIZE_SPLIT} --random-state {RANDOM_STATE}",
        task_id="docker-airflow-split",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[Mount(source=PATH_VOLUME, target=PATH_TARGET, type='bind')],
    )

    predict = DockerOperator(
        image="airflow-predict",
        command=f"--input-dir {PATH_SPLIT_DATA} --output-dir {PATH_PREDICTS} --model-dir {PATH_MODEL}",
        task_id="docker-airflow-predict",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[Mount(source=PATH_VOLUME, target=PATH_TARGET, type='bind')],
    )

    split_data >> predict