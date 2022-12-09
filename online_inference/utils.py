import logging


PATH_TO_DATA = "../data/raw/heart_cleveland_upload.csv"
LOCAL_HOST = "0.0.0.0"
PORT = 8000
ENDPOINT = "predict"
ITERS = 5
ID = "id"
TARGET = "condition"


# logging
def setup_logger(name, log_file, level=logging.INFO):
    """To setup as many loggers as you want"""

    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    handler = logging.FileHandler(log_file, mode="w")        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

on_inf_logger = setup_logger("on_inf", "online_inference.log", level=logging.DEBUG)