import numpy as np

def add_technical_indicators(data: pd.DataFrame) -> pd.DataFrame:
    """
    Args:
        data (pd.DataFrame): Preprocessed data.

    Returns:
        pd.DataFrame: Data with additional features.
    """
    data['Daily_Return'] = data['Adj Close'].pct_change()
    data['MA_10'] = data['Adj Close'].rolling(window=10).mean()
    data['MA_50'] = data['Adj Close'].rolling(window=50).mean()
    data['Volatility'] = data['Adj Close'].rolling(window=20).std()
    return data
