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
    ITERS
)


if __name__ == "__main__":
    on_inf_logger.debug("Read Data")
    print("Read Data")

    data = pd.read_csv(PATH_TO_DATA).drop(["condition"], axis=1)
    data["id"] = data.index + 1
    request_features = list(data.columns)

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
        on_inf_logger.info(f"Response json :: ( response.json() )")
        print(response.status_code)
        print(response.json())


    # request_features.to_dict(orient="records")
    # on_inf_logger.debug(f"Request json :: ( {request_features} )")

    # response = requests.get(
    #     f"http://{LOCAL_HOST}:{PORT}/{ENDPOINT}",
    #     json.dumps(request_features)
    # )

    # on_inf_logger.info(f"Response Status code :: ( {response.status_code} )")
    # on_inf_logger.info(f"Response json :: ( response.json() )")
    # print(response.status_code)
    # print(response.json())

    