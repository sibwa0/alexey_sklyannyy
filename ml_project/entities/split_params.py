from dataclasses import dataclass
import pandas as pd


@dataclass
class SplitParams:
    test_size: float = 0.2
    seed: int = 0

@dataclass
class SplitData:
    X: pd.DataFrame
    y: pd.DataFrame
