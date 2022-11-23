import unittest
from fastapi.testclient import TestClient
from fastapi import FastAPI
import pandas as pd
import numpy as np

from app import (
    main
)
from utils import (
    PATH_TO_DATA
)


class TestOnlineInf(unittest.TestCase):
    app = FastAPI

    def test_main(self):
        with TestClient(self.app) as client:
            response = client.get("/")
            assert response.status_code == 200

    def test_predict(self):
        with TestClient(self.app) as client:
            data = pd.read_csv(PATH_TO_DATA)
            data = data.drop(["condition"], axis=1)
            data["id"] = data.index + 1

            request_data = [
                x.item() if isinstance(x, np.generic) \
                else x for x in data.iloc[0].tolist()
            ]
            request_features = list(data.columns)

            response = client.get(
                "/predict",
                json={"data": [request_data], "features": request_features}
            )

            assert response.status_code == 200


