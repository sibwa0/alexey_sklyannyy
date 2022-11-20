import unittest


from ml_project.data.make_dataset import (
    read_data,
    split_train_test_data,
    divide_df_to_sings_marks
)
from ml_project.entities.feature_params import FeatureParams
from ml_project.features.build_features import build_transformer
from ml_project.entities.split_params import SplitParams


class TestMakeDataset(unittest.TestCase):
    def test_load_dataset(self):
        data = read_data("data/raw/heart_cleveland_upload.csv")

        assert "condition" in data

    def test_split_dataset(self):
        val_size = 0.2
        split_params = SplitParams(random_state=0, test_size=val_size)
        data = read_data("tests/tmp/test_df.csv")
        split_data = divide_df_to_sings_marks(
            data,
            "tests/tmp/test_path.csv"
        )
        assert (split_data.X.shape[0],) == split_data.y.shape

        X_train, X_test, y_train, y_test = split_train_test_data(
            split_data,
            split_params
        )
        assert (X_train.shape[0],) == y_train.shape
        assert (X_test.shape[0],) == y_test.shape