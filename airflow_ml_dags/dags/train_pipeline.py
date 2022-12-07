from datetime import datetime

from airflow import DAG
from airflow.providers.docker.operators.docker import DockerOperator
from docker.types import Mount

from utils import (
    PATH_DATA,
    PATH_MODEL,
    PATH_PREPROCESS,
    PATH_SPLIT_DATA,
    SIZE_SPLIT,
    RANDOM_STATE,
    PATH_TARGET,
    PATH_VOLUME,
    PATH_TRAIN_MODEL,
    default_args
)


with DAG(
        "train_pipeline",
        default_args=default_args,
        schedule_interval="@weekly",
        start_date=datetime(2022, 11, 25),
) as dag:
    download_daily_data = DockerOperator(
        image="airflow-download",
        command=f"--output-dir {PATH_DATA}",
        task_id="docker-airflow-download",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[Mount(source=PATH_VOLUME, target=PATH_TARGET, type='bind')],
    )

    split_data = DockerOperator(
        image="airflow-split",
        command=f"--input-dir {PATH_DATA} --output-dir {PATH_SPLIT_DATA} --size {SIZE_SPLIT} --random-state {RANDOM_STATE}",
        task_id="docker-airflow-split",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[Mount(source=PATH_VOLUME, target=PATH_TARGET, type='bind')],
    )

    preprocess_data = DockerOperator(
        image="airflow-preprocess",
        command=f"--input-dir {PATH_SPLIT_DATA} --output-dir {PATH_PREPROCESS}",
        task_id="docker-airflow-preprocess",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[Mount(source=PATH_VOLUME, target=PATH_TARGET, type='bind')],
    )

    init_model = DockerOperator(
        image="airflow-model",
        command=f"--output-dir {PATH_TRAIN_MODEL}",
        task_id="docker-airflow-model",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[Mount(source=PATH_VOLUME, target=PATH_TARGET, type='bind')],
    )

    train_model = DockerOperator(
        image="airflow-train",
        command=f"--input-dir {PATH_SPLIT_DATA} --model-dir {PATH_TRAIN_MODEL}",
        task_id="docker-airflow-train",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[Mount(source=PATH_VOLUME, target=PATH_TARGET, type='bind')],
    )

    val_model = DockerOperator(
        image="airflow-validate",
        command=f"--input-dir {PATH_SPLIT_DATA} --preproc-dir {PATH_PREPROCESS} --model-dir {PATH_TRAIN_MODEL}",
        task_id="docker-airflow-validate",
        do_xcom_push=False,
        mount_tmp_dir=False,
        mounts=[Mount(source=PATH_VOLUME, target=PATH_TARGET, type='bind')],
    )

    download_daily_data >> split_data >> preprocess_data >> init_model >> train_model >> val_model
