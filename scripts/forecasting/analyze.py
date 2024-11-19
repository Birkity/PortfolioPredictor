def analyze_trend(forecast_df):
    """
    Analyze the trend in the forecast data.
    """
    trend = np.polyfit(range(len(forecast_df)), forecast_df["forecast"], 1)[0]
    if trend > 0:
        return "Upward Trend"
    elif trend < 0:
        return "Downward Trend"
    else:
        return "Stable Trend"

def analyze_volatility(forecast_df):
    """
    Analyze the volatility using confidence intervals.
    """
    if "lower_ci" in forecast_df.columns and "upper_ci" in forecast_df.columns:
        volatility = forecast_df["upper_ci"] - forecast_df["lower_ci"]
        return volatility.mean()
    return None
