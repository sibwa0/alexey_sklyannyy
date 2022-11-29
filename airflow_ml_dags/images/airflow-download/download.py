import os
from tkinter import Y
import click
import pandas as pd
import numpy as np

from airflow_ml_dags.utils import (
    FILENAME_DATA_FEATURES,
    FILENAME_DATA_TARGET
)


SIZE_DATASET = 50


def gerenate_rand_data() -> pd.DataFrame:
    X, y = pd.DataFrame(), pd.Series()

    X["age"] = np.random.randint(10, 80, size=SIZE_DATASET)
    X["sex"] = np.random.randint(0, 2, size=SIZE_DATASET)
    X["cp"] = np.random.randint(0, 4, size=SIZE_DATASET)
    X["trestbps"] = np.random.randint(0, 160, size=SIZE_DATASET)
    X["chol"] = np.random.randint(126, 540, size=SIZE_DATASET)
    X["fbs"] = np.random.randint(0, 2, size=SIZE_DATASET)
    X["restecg"] = np.random.randint(0, 3, size=SIZE_DATASET)
    X["thalach"] = np.random.randint(71, 202, size=SIZE_DATASET)
    X["exang"] = np.random.randint(0, 2, size=SIZE_DATASET)
    X["oldpeak"] = np.round(np.random.random(size=SIZE_DATASET) * 10, 1)
    X["slope"] = np.random.randint(0, 3, size=SIZE_DATASET)
    X["ca"] = np.random.randint(0, 4, size=SIZE_DATASET)
    X["thal"] = np.random.randint(0, 3, size=SIZE_DATASET)

    y["condition"] = np.random.randint(0, 2, size=SIZE_DATASET)

    return X, y


@click.command("download")
@click.argument("output_dir")
def download(output_dir: str):
    X, y = gerenate_rand_data()

    os.makedirs(output_dir, exist_ok=True)

    X.to_csv(os.path.join(output_dir, FILENAME_DATA_FEATURES), index=False)
    y.to_csv(os.path.join(output_dir, FILENAME_DATA_TARGET), index=False)


if __name__ == '__main__':
    download()