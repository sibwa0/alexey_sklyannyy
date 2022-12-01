from airflow.models import Variable

# PATH_VOLUME = "/home/sklaa00/main_course/second/mlops/alexey_sklyannyy/airflow_ml_dags/data"
PATH_VOLUME = Variable.get("PATH_VOLUME", default_var="/home/sklaa00/main_course/second/mlops/alexey_sklyannyy/airflow_ml_dags/data")
PATH_DATA = "/data/raw/{{ ds }}"
PATH_PREPROCESS = "/data/preprocess/{{ ds }}"
PATH_SPLIT_DATA = "/data/split_data/{{ ds }}"
PATH_MODEL = "/data/models/{{ ds }}"
PATH_PREDICTS = "/data/predicts/{{ ds }}"
PATH_METRICS = "/data/metrics/{{ ds }}"
PATH_TARGET = "/data"

SIZE_SPLIT = 0.2
RANDOM_STATE = 5

FILENAME_DATA_FEATURES = "data.csv"
FILENAME_DATA_TARGET = "target.csv"

FILENAME_DATA_TRAIN = "train.csv"
FILENAME_MODEL = "model.pkl"
FILENAME_METRICS = "metrics.json"
COL_TARGET = "condition"
