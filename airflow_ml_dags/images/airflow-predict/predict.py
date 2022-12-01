import os
import pandas as pd

import pickle
import click
from sklearn.metrics import classification_report

FILENAME_DATA = "X_test.csv"
FILENAME_TARGET = "y_test.csv"
FILENAME_MODEL = "model.pkl"
FILENAME_PREDICTS = "predicts.csv"
FILENAME_METRICS = "metrics.json"
COL_TARGET = "condition"

@click.command("predict")
@click.option("--input-dir")
@click.option("--output-dir")
@click.option("--model-dir")
def predict(input_dir: str, output_dir: str, model_dir: str):
    dataset = pd.read_csv(os.path.join(input_dir, FILENAME_DATA))

    path_model = os.path.join(model_dir, FILENAME_MODEL)
    with open(path_model, "rb") as fd_model:
        model = pickle.load(fd_model)
    
    predicts = model.predict(dataset)
    pred_dataframe = pd.DataFrame()
    pred_dataframe[COL_TARGET] = predicts

    os.makedirs(output_dir, exist_ok=True)
    pred_dataframe.to_csv(os.path.join(output_dir, FILENAME_PREDICTS), index=False)

    # vals = pd.read_csv(os.path.join(input_dir, FILENAME_TARGET))
    # metrics = classification_report(vals, predicts, output_dict=True)

    # path_metric = os.path.join(metric_dir, FILENAME_METRICS)

    # os.makedirs(metric_dir, exist_ok=True)
    # with open(path_metric, "wb") as fd_metrics:
    #     pickle.dump(metrics, fd_metrics)


if __name__ == '__main__':
    predict()
