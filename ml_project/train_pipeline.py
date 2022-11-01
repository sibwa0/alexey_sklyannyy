import json
import pandas as pd

from ml_project.data import read_data
from reports.utils.logger import log


def run_train_pipeline(training_pipeline_params):
    