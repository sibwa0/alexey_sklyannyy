from dataclasses import dataclass
from typing import Optional

from marshmallow_dataclass import class_schema
import yaml

from .split_params import SplitParams
from .feature_params import FeatureParams
from .train_params import TrainingParams


@dataclass()
class TrainingPipelineParams:
    input_data_path: str
    output_model_path: str
    metric_path: str
    split_params: SplitParams
    feature_params: FeatureParams
    train_params: TrainingParams
    train_dataframe_path: Optional[str] = "data/raw/predict_dataset.csv"
    scaler: Optional[str] = None


TrainingPipelineParamsSchema = class_schema(TrainingPipelineParams)


def read_training_pipeline_params(config_path: str) -> TrainingPipelineParams:
    with open(config_path, "r") as input_stream:
        schema = TrainingPipelineParamsSchema()
        return schema.load(yaml.safe_load(input_stream))
