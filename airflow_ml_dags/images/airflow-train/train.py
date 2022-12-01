import os
from sklearn.ensemble import RandomForestClassifier
import click
import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


FILENAME_TRAIN_DATA = "X_train.csv"
FILENAME_TARGET_DATA = "y_train.csv"
FILENAME_MODEL = "model.pkl"
FILENAME_METRICS = "metrics.json"


@click.command("train")
@click.option("--model-dir")
@click.option("--input-dir")
def train(model_dir: str, input_dir: str):
    path_x_train = os.path.join(input_dir, FILENAME_TRAIN_DATA)
    train_data = pd.read_csv(path_x_train)

    path_y_train = os.path.join(input_dir, FILENAME_TARGET_DATA)
    target_data = pd.read_csv(path_y_train)

    path_model = os.path.join(model_dir, FILENAME_MODEL)
    with open(path_model, "rb") as fd_read_model:
        model = pickle.dump(fd_read_model)

    model.fit(train_data, target_data)

    with open(path_model, "wb") as fd_write_model:
        pickle.dump(model, fd_write_model)

    # predicts = model.predict(X_test)

    # metrics = classification_report(y_test, predicts)

    # os.makedirs(output_dir, exist_ok=True)


    # path_metrics = os.path.join(output_dir, FILENAME_METRICS)
    # with open(path_metrics, "wb") as fd_metrics:
    #     pickle.dump(metrics, fd_metrics)

if __name__ == "__main__":
    train()