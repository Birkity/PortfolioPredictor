import matplotlib.pyplot as plt

def plot_forecast(historical_data, forecast_df, model_name):
    """
    Plot the forecast along with historical data.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(historical_data.index, historical_data, label="Historical Data", color="blue")
    forecast_range = range(len(historical_data), len(historical_data) + len(forecast_df))
    
    plt.plot(forecast_range, forecast_df["forecast"], label=f"{model_name} Forecast", color="red")
    
    if "lower_ci" in forecast_df.columns and "upper_ci" in forecast_df.columns:
        plt.fill_between(forecast_range, forecast_df["lower_ci"], forecast_df["upper_ci"], 
                         color="gray", alpha=0.3, label="Confidence Interval")
    
    plt.title(f"{model_name} Forecast")
    plt.legend()
    plt.grid()
    plt.show()
