import os
import pandas as pd
import click

from typing import List

from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


FILENAME_DATA = "X_train.csv"


def build_numerical_pipeline() -> Pipeline:
    num_pipeline = Pipeline([
        ("scaler", StandardScaler())
    ])
    return num_pipeline

def build_transformer(numerical_features: List[str]) -> ColumnTransformer:
    transformer = ColumnTransformer(
        [
            (
                "numerical_pipeline",
                build_numerical_pipeline(),
                numerical_features,
            ),
        ]
    )
    return transformer


@click.command("preprocess")
@click.option("--input-dir")
@click.option("--output-dir")
def preprocess(input_dir: str, output_dir):
    path_data = os.path.join(input_dir, FILENAME_DATA)
    train_df = pd.read_csv(path_data)

    transformer = build_transformer(train_df.columns)

    preprocess_train_df = transformer.fit_transform(train_df)
    train_df[train_df.columns] = preprocess_train_df

    os.makedirs(output_dir, exist_ok=True)
    train_df.to_csv(os.path.join(output_dir, FILENAME_DATA), index=False)


if __name__ == '__main__':
    preprocess()