import unittest
from fastapi.testclient import TestClient
from fastapi import FastAPI
from unittest.mock import patch
import pandas as pd
import numpy as np

from app import (
    load_object,
    app,
)
from utils import (
    PATH_TO_DATA
)

client =  TestClient(app)


class TestOnlineInf(unittest.TestCase):

    def test_main(self):
        response = client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_status(self):
        response = client.get("/status")
        self.assertEqual(response.status_code, 200)

    def test_predict(self):
        with patch("app.model") as mock_model:
            data = pd.read_csv(PATH_TO_DATA)
            data = data.drop(["condition"], axis=1)
            data["id"] = data.index + 1

            mock_model.predict.return_value = np.random.randint(2, size=data.shape[1])
            request_data = [
                x.item() if isinstance(x, np.generic) \
                else x for x in data.iloc[0].tolist()
            ]
            request_features = list(data.columns)
        
            response = client.get(
                "/predict",
                json={"data": [request_data], "features": request_features}
            )

            self.assertEqual(response.status_code, 200)
