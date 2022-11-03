from dataclasses import dataclass


@dataclass
class TrainingParams:
    model_type: str = "RandomForestClassifier"
    random_state: int = 0
    n_estimators: int = 100
