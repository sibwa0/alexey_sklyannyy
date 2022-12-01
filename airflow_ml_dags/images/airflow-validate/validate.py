import os
from sklearn.ensemble import RandomForestClassifier
import click
import pandas as pd
import pickle
import json

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


FILENAME_TEST_DATA = "X_test.csv"
FILENAME_TARGET_DATA = "y_test.csv"
FILENAME_MODEL = "model.pkl"
FILENAME_METRICS = "metrics.json"
FILENAME_PREDICTS = "predicts.csv"


@click.command("train")
@click.option("--input-dir")
@click.option("--model-dir")
def train(model_dir: str, input_dir: str):
    path_x_test = os.path.join(input_dir, FILENAME_TEST_DATA)
    test_data = pd.read_csv(path_x_test)

    path_y_test = os.path.join(input_dir, FILENAME_TARGET_DATA)
    target_data = pd.read_csv(path_y_test)

    path_model = os.path.join(model_dir, FILENAME_MODEL)
    with open(path_model, "rb") as fd_read_model:
        model = pickle.load(fd_read_model)

    predicts = model.predict(test_data)
    metrics = classification_report(target_data, predicts, output_dict=True)

    path_metrics = os.path.join(model_dir, FILENAME_METRICS)
    with open(path_metrics, "w") as fd_metrics:
        json.dump(metrics, fd_metrics)


if __name__ == "__main__":
    train()