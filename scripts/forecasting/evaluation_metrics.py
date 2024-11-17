import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error

def evaluate_forecast(y_true, y_pred):
    """
    Evaluate forecast performance.
    :param y_true: Actual values
    :param y_pred: Predicted values
    :return: Dictionary of metrics
    """
    metrics = {
        "MAE": mean_absolute_error(y_true, y_pred),
        "RMSE": np.sqrt(mean_squared_error(y_true, y_pred))
    }
    return metrics
