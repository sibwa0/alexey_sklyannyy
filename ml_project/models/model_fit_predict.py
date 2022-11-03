import pandas as pd
import numpy as np
import pickle
from typing import Union, Dict

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report

from sklearn.ensemble import (
    RandomForestClassifier,
    GradientBoostingClassifier
)

from ml_project.entities.train_params import TrainingParams


SklearnClassifierModel = Union[
    RandomForestClassifier,
    GradientBoostingClassifier
    ]


def train_model(
    features: pd.DataFrame, target: pd.Series, train_params: TrainingParams
) -> SklearnClassifierModel:
    if train_params.model_type == "RandomForestClassifier":
        model = RandomForestClassifier(
            n_estimators=train_params.n_estimators, random_state=train_params.random_state
        )
    elif train_params.model_type == "GradientBoostingClassifier":
        model = GradientBoostingClassifier()
    else:
        raise NotImplementedError()

    model.fit(features, target)
    return model

def create_inference_pipeline(
    model: SklearnClassifierModel, transformer: ColumnTransformer
) -> Pipeline:
    return Pipeline([("feature_handling", transformer), ("model_handling", model)])

def predict_model(
    model: Pipeline, features: pd.DataFrame
) -> np.ndarray:
    return model.predict(features)

def evaluate_model(
    predicts: np.ndarray, target: pd.Series
) -> Dict[str, str]:
    return classification_report(
        target,
        predicts,
        output_dict=True
    )

def serialize_model(model: object, output: str) -> str:
    with open(output, "wb") as f:
        pickle.dump(model, f)
    return output