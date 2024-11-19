import mlflow.pyfunc
import pandas as pd
import numpy as np
import logging
from sklearn.preprocessing import MinMaxScaler

logging.basicConfig(filename='./logs/forecast.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

def load_model_from_mlflow(model_uri):
    """
    Load a model from MLflow by its URI.
    """
    try:
        model = mlflow.pyfunc.load_model(model_uri)
        logging.info(f"Model loaded from {model_uri}")
        return model
    except Exception as e:
        logging.error(f"Failed to load model: {str(e)}")
        raise

def forecast_arima_sarima(model, steps):
    """
    Forecast using ARIMA or SARIMA model.
    """
    result = model.forecast(steps=steps)
    return pd.DataFrame({
        "forecast": result.predicted_mean,
        "lower_ci": result.conf_int()["lower Adj Close"],
        "upper_ci": result.conf_int()["upper Adj Close"]
    })

def forecast_lstm(model, historical_data, steps, window_size=60):
    """
    Forecast using LSTM model.
    """
    scaler = MinMaxScaler(feature_range=(0, 1))
    scaled_data = scaler.fit_transform(historical_data.values.reshape(-1, 1))
    
    last_window = scaled_data[-window_size:]
    predictions = []
    
    for _ in range(steps):
        prediction = model.predict(last_window.reshape(1, window_size, 1))
        predictions.append(prediction[0, 0])
        last_window = np.append(last_window[1:], prediction)
    
    predictions = scaler.inverse_transform(np.array(predictions).reshape(-1, 1))
    return pd.DataFrame({"forecast": predictions.flatten()})
