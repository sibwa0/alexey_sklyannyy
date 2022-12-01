import os
import pandas as pd

from sklearn.model_selection import train_test_split
import click

FILENAME_DATA = "data.csv"
FILENAME_TARGET = "target.csv"

FILENAME_TRAIN_X = "X_train.csv"
FILENAME_TRAIN_Y = "y_train.csv"
FILENAME_TEST_X = "X_test.csv"
FILENAME_TEST_Y = "y_test.csv"


@click.command("split_data")
@click.option("--input-dir")
@click.option("--output-dir")
@click.option("--size")
@click.option("--random-state")
def split_data(input_dir: str, output_dir: str, size: float, random_state: int):
    path_data = os.path.join(input_dir, FILENAME_DATA)
    features_df = pd.read_csv(path_data)
    X_train, X_test = train_test_split(features_df, test_size=size, random_state=random_state)

    path_target = os.path.join(input_dir, FILENAME_TARGET)
    target_df = pd.read_csv(path_target)
    y_train, y_test = train_test_split(target_df, test_size=size, random_state=random_state)

    os.makedirs(output_dir, exist_ok=True)
    X_train.to_csv(os.path.join(output_dir, FILENAME_TRAIN_X), index=False)
    X_test.to_csv(os.path.join(output_dir, FILENAME_TEST_X), index=False)
    y_train.to_csv(os.path.join(output_dir, FILENAME_TRAIN_Y), index=False)
    y_test.to_csv(os.path.join(output_dir, FILENAME_TEST_Y), index=False)


if __name__ == '__main__':
    split_data()