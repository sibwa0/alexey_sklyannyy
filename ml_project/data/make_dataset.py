from typing import Tuple
import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split

from ml_project.entities.split_params import SplitParams, SplitData


def read_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def divide_df_to_sings_marks(data: pd.DataFrame, path: str) -> SplitData:
    y = data.loc[:, "condition"]
    X = data.drop(["condition"], axis=1)

    if not os.path.exists(path):
        save_df(X, path)

    return SplitData(X=X, y=y)

def split_train_test_data(
    data: SplitData, params: SplitParams
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:

    X_train, X_test, y_train, y_test = train_test_split(
        data.X, data.y, test_size=params.test_size, random_state=params.random_state
    )

    return X_train, X_test, y_train, y_test

# save to df
def save_df(data: pd.DataFrame, path: str):
    data.to_csv(path)

def save_array_to_df(data: np.ndarray, path: str) -> None:
    data = pd.Series(data)
    data.to_csv(path)

def remove_id(df: pd.DataFrame) -> pd.DataFrame:
    if hasattr(df, "Unnamed: 0"):
        df = df.drop(["Unnamed: 0"],  axis=1)
    return df