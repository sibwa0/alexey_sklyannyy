import os
from sklearn.ensemble import RandomForestClassifier
import click
import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

from airflow_ml_dags.utils import (
    FILENAME_DATA_TRAIN,
    FILENAME_MODEL,
    COL_TARGET,
    FILENAME_METRICS
)

@click.command("train")
@click.option("--input-dir")
@click.option("--output-dir")
def train(input_dir: str, output_dir: str):
    train_data = pd.read_csv(os.path.join(input_dir, FILENAME_DATA_TRAIN))

    model = RandomForestClassifier()

    y = train_data[COL_TARGET]
    X = train_data.drop([COL_TARGET], axis=1)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=5
    )

    model.fit(X_train, y_train)
    predicts = model.predict(X_test)

    metrics = classification_report(y_test, predicts)

    os.makedirs(output_dir, exist_ok=True)

    path_model = os.path.join(output_dir, FILENAME_MODEL)
    with open(path_model, "wb") as fd_model:
        pickle.dump(model, fd_model)

    path_metrics = os.path.join(output_dir, FILENAME_METRICS)
    with open(path_metrics, "wb") as fd_metrics:
        pickle.dump(metrics, fd_metrics)