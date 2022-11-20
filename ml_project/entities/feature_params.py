from typing import List, Optional
from dataclasses import dataclass

@dataclass
class FeatureParams:
    numerical_features: List[str]
    target_col: Optional[str]
