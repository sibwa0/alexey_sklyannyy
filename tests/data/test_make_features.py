import numpy as np
import pytest
import pandas as pd


from ml_project.data.make_dataset import read_data
from ml_project.entities.feature_params import FeatureParams
from ml_project.features.build_features import build_transformer