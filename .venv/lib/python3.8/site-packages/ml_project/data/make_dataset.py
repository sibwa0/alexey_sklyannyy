from typing import Tuple
import pandas as pd
from sklearn.model_selection import train_test_split

from ml_project.entities.split_params import SplitParams, SplitData


def read_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def divide_df_to_sings_marks(data: pd.DataFrame) -> SplitData:
    y = data.loc[:, "condition"]
    X = data.drop(["condition"], axis=1)

    return SplitData(X=X, y=y)

def split_train_test_data(
    data: SplitData, params: SplitParams
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:

    X_train, X_test, y_train, y_test = train_test_split(
        data.X, data.y, test_size=params.test_size, random_state=params.seed
    )

    return X_train, X_test, y_train, y_test
