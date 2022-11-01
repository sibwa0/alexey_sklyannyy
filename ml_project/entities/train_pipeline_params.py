from dataclasses import dataclass

from marshmallow_dataclass import class_schema

@dataclass()
class TrainingPipelineParams:
    train_data_path: str
    test_data_path: str


TrainingPipelineParamsSchema = class_schema(TrainingPipelineParams)



