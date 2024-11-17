import logging
from pmdarima import auto_arima

def train_auto_arima(data, seasonal=False, m=1):
  
    logging.info(f"Training Auto ARIMA model. Seasonal: {seasonal}, Periodicity: {m}.")
    try:
        model = auto_arima(data, seasonal=seasonal, m=m, trace=True, error_action='ignore', suppress_warnings=True)
        logging.info(f"Auto ARIMA selected order: {model.order}. AIC: {model.aic()}.")
        return model
    except Exception as e:
        logging.error(f"Error during Auto ARIMA training: {str(e)}")
        raise
