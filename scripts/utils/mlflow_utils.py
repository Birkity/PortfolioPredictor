import mlflow
import mlflow.sklearn
import mlflow.tensorflow
import logging

def start_mlflow_experiment(experiment_name):
    """
    Start or set an MLflow experiment.
    :param experiment_name: Name of the MLflow experiment
    """
    mlflow.set_experiment(experiment_name)
    mlflow.start_run()
    logging.info(f"Started MLflow experiment: {experiment_name}")

def log_params(params):
    """
    Log parameters to MLflow.
    :param params: Dictionary of parameters
    """
    for key, value in params.items():
        mlflow.log_param(key, value)

def log_metrics(metrics):
    """
    Log metrics to MLflow.
    :param metrics: Dictionary of metrics
    """
    for key, value in metrics.items():
        mlflow.log_metric(key, value)

def log_model(model, model_name):
    """
    Log a model to MLflow.
    :param model: The trained model
    :param model_name: Name under which the model will be logged
    """
    mlflow.sklearn.log_model(model, model_name)
    logging.info(f"Logged model: {model_name} to MLflow.")

def end_mlflow_experiment():
    """
    End the current MLflow experiment.
    """
    mlflow.end_run()
    logging.info("MLflow experiment ended.")
