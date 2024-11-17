import logging
from statsmodels.tsa.arima.model import ARIMA

def train_arima(train_data, order):
    """
    :param train_data: Training time series data
    :param order: ARIMA model order (p, d, q)
    :return: Trained ARIMA model
    """
    logging.info(f"Starting ARIMA training with order {order}.")
    model = ARIMA(train_data, order=order)
    fitted_model = model.fit()
    logging.info(f"ARIMA training completed with order {order}.")
    return fitted_model
