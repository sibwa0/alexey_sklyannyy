import os
import pandas as pd
import pickle
import click

from sklearn.ensemble import RandomForestClassifier


FILENAME_MODEL = "model.pkl"

@click.command("init_model")
@click.option("--output-dir")
def init_model(output_dir: str):
    os.makedirs(output_dir, exist_ok=True)

    path_model = os.path.join(output_dir, FILENAME_MODEL)

    model = RandomForestClassifier()

    with open(path_model, "wb") as fd_model:
        pickle.dump(model, fd_model)


if __name__ == "__main__":
    init_model()