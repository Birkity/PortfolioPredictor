import matplotlib.pyplot as plt
import seaborn as sns

def plot_trends(data: pd.DataFrame):
    """
    Plot time series trends for closing prices.

    Args:
        data (pd.DataFrame): Processed data.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Adj Close'], label='Adjusted Close')
    plt.title('Adjusted Close Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.show()

def plot_volatility(data: pd.DataFrame):
    """
    Plot volatility over time.

    Args:
        data (pd.DataFrame): Processed data.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Volatility'], label='Volatility', color='orange')
    plt.title('Volatility Over Time')
    plt.xlabel('Date')
    plt.ylabel('Volatility')
    plt.legend()
    plt.show()
