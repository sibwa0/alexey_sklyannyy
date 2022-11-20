import unittest
from unittest.mock import patch
import os
from typing import Optional
from dataclasses import dataclass
from io import StringIO

from ml_project.train_pipeline import run_train_pipeline
from ml_project.predict_pipeline import run_predict_pipeline
from sklearn.preprocessing import StandardScaler


from ml_project.entities import (
    TrainingPipelineParams,
    SplitParams,
    FeatureParams,
    TrainingParams
)

numerical_features = [
    "age",
    "sex",
    "cp",
    "trestbps",
    "chol",
    "fbs",
    "restecg",
    "thalach",
    "exang",
    "oldpeak",
    "slope",
    "ca",
    "thal",
]

@dataclass
class TestTrainingPipelineParams:
    input_data_path: str = "data/raw/heart_cleveland_upload.csv"
    output_model_path: str = "tests/tmp/test_model.pkl"
    metric_path: str = "tests/tmp/test_metrics.json"
    split_params: SplitParams = SplitParams(
        test_size=0.25,
        random_state=5
    )
    feature_params: FeatureParams = FeatureParams(
        numerical_features=numerical_features,
        target_col="condition"
    )
    train_params: TrainingParams = TrainingParams(
        model_type="RandomForestClassifier",
    )
    train_dataframe_path: Optional[str] = "data/raw/predict_dataset.csv"
    scaler: Optional[str] = None

@dataclass
class TestPredictPipelineParams:
    input_data_path: str = "data/raw/predict_dataset.csv"
    input_model_path: str = "models/model.pkl"
    output_data_path: str = "tests/tmp/test_model_predicts.csv"


class TestEnd2End(unittest.TestCase):
    test_train_piplein_params = TestTrainingPipelineParams()
    test_test_piplein_params = TestPredictPipelineParams()

    @unittest.mock.patch("ml_project.train_pipeline.logger")
    def test_train_end2end(self, mock_log):
        with patch("sys.stdout", new=StringIO()):
            path_to_model, metrics = run_train_pipeline(self.test_train_piplein_params)

            self.assertTrue(os.path.exists(path_to_model))
            self.assertTrue(metrics["0"]["f1-score"] > 0.6)
            self.assertTrue(metrics["1"]["f1-score"] > 0.6)

    @unittest.mock.patch("ml_project.train_pipeline.logger")
    def test_predict_end2end(self, mock_log):
        with patch("sys.stdout", new=StringIO()):
            run_predict_pipeline(self.test_test_piplein_params)

            self.assertTrue(os.path.exists(self.test_test_piplein_params.output_data_path))
