import os
import pickle
import logging
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

def load_model(model_type, dataset_name):
    base_path = r"C:\Users\USER\Documents\OPLearning\10_Academy\Week_11\models"
    model_path = os.path.join(base_path, f"{model_type.lower()}_{dataset_name.lower()}", "model.pkl")
    
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found at {model_path}")
    
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    logging.info(f"Loaded {model_type} model for {dataset_name} from {model_path}.")
    return model


def forecast_and_visualize(model, data, steps, model_name, model_type):
    forecast = model.get_forecast(steps=steps)
    forecast_index = pd.date_range(start=data.index[-1], periods=steps+1, freq='B')[1:]
    forecast_values = forecast.predicted_mean
    conf_int = forecast.conf_int()

    # Visualization
    plt.figure(figsize=(10, 6))
    plt.plot(data, label="Historical Data")
    plt.plot(forecast_index, forecast_values, label="Forecast")
    plt.fill_between(forecast_index, conf_int.iloc[:, 0], conf_int.iloc[:, 1], color="pink", alpha=0.3, label="Confidence Interval")
    plt.title(f"{model_type} Forecast for {model_name}")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid()
    plt.show()

    logging.info(f"{model_type} forecast for {model_name} completed and visualized.")

def main():
    datasets = {
        "TSLA": r"C:\Users\USER\Documents\OPLearning\10_Academy\Week_11\data\processed\TSLA_processed.csv",
        "SPY": r"C:\Users\USER\Documents\OPLearning\10_Academy\Week_11\data\processed\SPY_processed.csv",
        "BND": r"C:\Users\USER\Documents\OPLearning\10_Academy\Week_11\data\processed\BND_processed.csv"
    }
    steps = 252  # Approx. one year of trading days

    for dataset_name, file_path in datasets.items():
        data = pd.read_csv(file_path, parse_dates=["Date"], index_col="Date")
        close_data = data["Close"]

        # Load ARIMA
        arima_model = load_model("ARIMA", dataset_name)
        forecast_and_visualize(arima_model, close_data, steps, dataset_name, "ARIMA")

        # Load SARIMA
        sarima_model = load_model("SARIMA", dataset_name)
        forecast_and_visualize(sarima_model, close_data, steps, dataset_name, "SARIMA")


if __name__ == "__main__":
    main()
