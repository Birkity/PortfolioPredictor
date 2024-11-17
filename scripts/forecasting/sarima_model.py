import logging
from statsmodels.tsa.statespace.sarimax import SARIMAX

def train_sarima(data, order, seasonal_order):
   
    logging.info(f"Training SARIMA model with order {order} and seasonal order {seasonal_order}.")
    try:
        model = SARIMAX(data, order=order, seasonal_order=seasonal_order)
        fitted_model = model.fit()
        logging.info(f"SARIMA model trained successfully. AIC: {fitted_model.aic}.")
        return fitted_model
    except Exception as e:
        logging.error(f"Error during SARIMA training: {str(e)}")
        raise
