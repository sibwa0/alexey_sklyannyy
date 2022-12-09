import requests
import json
import pandas as pd
import numpy as np

from utils import (
    on_inf_logger,
    ENDPOINT,
    LOCAL_HOST,
    PATH_TO_DATA,
    PORT,
    ITERS,
    ID,
    TARGET
)


if __name__ == "__main__":
    on_inf_logger.debug("Read Data")

    data = pd.read_csv(PATH_TO_DATA).drop([TARGET], axis=1)
    data[ID] = data.index + 1
    request_features = list(data.columns)
    on_inf_logger.debug(f"Request features :: ( {request_features} )")

    for i in range(ITERS):
        request_data = [
            x.item() if isinstance(x, np.generic) \
            else x for x in data.iloc[i].tolist()
        ]

        response = requests.get(
            f"http://{LOCAL_HOST}:{PORT}/{ENDPOINT}",
            json={"data": [request_data], "features": request_features}
        )
        on_inf_logger.info(f"Response Status code :: ( {response.status_code} )")
        on_inf_logger.info(f"Response json :: ( {response.json()} )")
        print(response.status_code)
        print(response.json())
    