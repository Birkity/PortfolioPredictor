import os
import pickle
import logging
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def train_and_save_model(data, model_type, model_name, order=None, seasonal_order=None):
    if model_type == "ARIMA":
        model = ARIMA(data, order=order)
    elif model_type == "SARIMA":
        model = SARIMAX(data, order=order, seasonal_order=seasonal_order)
    else:
        raise ValueError("Invalid model type. Use 'ARIMA' or 'SARIMA'.")

    logging.info(f"Training {model_type} model for {model_name}...")
    fitted_model = model.fit()

    base_path = r"C:\Users\USER\Documents\OPLearning\10_Academy\Week_11\models"
    model_path = os.path.join(base_path, f"{model_type.lower()}_{data.lower()}", "model.pkl")
    os.makedirs(model_path, exist_ok=True)

    with open(os.path.join(model_path, "model.pkl"), "wb") as f:
        pickle.dump(fitted_model, f)

    logging.info(f"{model_type} model for {model_name} saved at {model_path}. AIC: {fitted_model.aic}")


def main():
    datasets = {
        "TSLA": r"C:\Users\USER\Documents\OPLearning\10_Academy\Week_11\data\processed\TSLA_processed.csv",
        "SPY": r"C:\Users\USER\Documents\OPLearning\10_Academy\Week_11\data\processed\SPY_processed.csv",
        "BND": r"C:\Users\USER\Documents\OPLearning\10_Academy\Week_11\data\processed\BND_processed.csv"
    }

    for dataset_name, file_path in datasets.items():
        data = pd.read_csv(file_path, parse_dates=["Date"], index_col="Date")
        train_data = data["Close"]

       
        train_and_save_model(train_data, "ARIMA", dataset_name, order=(1, 1, 1))

        
        train_and_save_model(train_data, "SARIMA", dataset_name, order=(1, 1, 1), seasonal_order=(1, 1, 1, 12))


if __name__ == "__main__":
    main()
