# Technopark
Склянный Алексей, ML-21


==============================

ml project

+- Step 0:
Необходимо использовать python3.8
~~~
sudo apt-get install python3.8
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.8 <input priority to choose python3.8>
sudo update-alternatives --config python3
<choose your input number>
~~~ 

Installation: 
~~~
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
~~~
Usage:
~~~
python setup.py build
python setup.py install

ml_project_train configs/train_config_randforest.yaml
ml_project_predict configs/predict_config.yaml

or

python ml_project/train_pipeline.py configs/train_config_randforest.yaml
python ml_project/predict_pipeline.py configs/predict_config.yaml 
~~~

Test:
~~~
python -m unittest
~~~

Project Organization
------------

    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   └── raw            <- The original, immutable data dump.
    │
    │
    ├── configs            <- configs for train and predict process 
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. 
    │
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── ml_project         <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- code to download or generate data
    │   │
    │   ├── features       <- code to turn raw data into features for modeling
    │   │
    │   ├── models         <- code to train models and then use trained models to make
    │   │
    │   ├── utils          <- dir for additional functions (logging, etc)
    │   │
    ├── tests
    │   ├── data           <- test functions from ml_project/data
    │   │
    │   ├── test_end2end_training.py   <- test train and predict 
    |   |
    │   └── tmp            <- initialized temprorary files, dataframes for tests 
    └──
--------
