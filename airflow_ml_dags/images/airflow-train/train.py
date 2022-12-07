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
@click.option("--input-dir")
@click.option("--model-dir")
def train(model_dir: str, input_dir: str):
    path_x_train = os.path.join(input_dir, FILENAME_TRAIN_DATA)
    train_data = pd.read_csv(path_x_train)

    path_y_train = os.path.join(input_dir, FILENAME_TARGET_DATA)
    target_data = pd.read_csv(path_y_train)

    path_model = os.path.join(model_dir, FILENAME_MODEL)
    with open(path_model, "rb") as fd_read_model:
        model = pickle.load(fd_read_model)

    model.fit(train_data, target_data)

    with open(path_model, "wb") as fd_write_model:
        pickle.dump(model, fd_write_model)


if __name__ == "__main__":
    train()