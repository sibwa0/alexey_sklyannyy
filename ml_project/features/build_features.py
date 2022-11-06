from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd


from ml_project.entities.feature_params import FeatureParams


def build_numerical_pipeline() -> Pipeline:
    num_pipeline = Pipeline([
        ("scaler", StandardScaler())
    ])
    return num_pipeline

def build_transformer(params: FeatureParams) -> ColumnTransformer:
    transformer = ColumnTransformer(
        [
            (
                "numerical_pipeline",
                build_numerical_pipeline(),
                params.numerical_features,
            ),
        ]
    )
    return transformer
