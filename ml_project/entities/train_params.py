from dataclasses import dataclass
from typing import Optional


@dataclass
class TrainingParams:
    model_type: str = "RandomForestClassifier"
    random_state: int = 5
    n_iters: Optional[int] = None
    scaler: Optional[str] = None
