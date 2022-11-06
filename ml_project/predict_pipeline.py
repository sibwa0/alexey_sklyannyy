import click
import logging
import json

from ml_project.data.make_dataset import (
    read_data,
    save_array_to_df,
    remove_id
)

from ml_project.entities.predict_pipeline_params import (
    read_predicting_pipeline_params,
    PredictingPipelineParams
)

from ml_project.models.model_fit_predict import (
    deserialize_model,
    predict_model
)


# to utils
def setup_logger(name, log_file, level=logging.INFO):
    """To setup as many loggers as you want"""

    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

    handler = logging.FileHandler(log_file, mode="w")        
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

logger = setup_logger("main", "predict.log")


def predict_pipeline(config_path: str):
    predicting_pipline_params = read_predicting_pipeline_params(config_path)

    return run_predict_pipeline(predicting_pipline_params)

def run_predict_pipeline(predicting_pipeline_params: PredictingPipelineParams):
    logger.info(f"__Start predicting :: params = {predicting_pipeline_params}")
    data_frame = read_data(predicting_pipeline_params.input_data_path)

    logger.info(f"__Shape got data_frame :: params = {data_frame.shape}")
    data_frame = remove_id(data_frame)
    logger.info(f"__Shape handled data_frame :: params = {data_frame.shape}")

    model_pipeline = deserialize_model(
        predicting_pipeline_params.input_model_path
    )
    logger.info(f"__Got Model :: {model_pipeline}")

    pred = predict_model(
        model_pipeline,
        data_frame
    )

    save_array_to_df(pred, predicting_pipeline_params.output_data_path)


@click.command()
@click.argument("config_path")
def main(config_path: str):
    predict_pipeline(config_path)

    
if __name__ == "__main__":
    main()
