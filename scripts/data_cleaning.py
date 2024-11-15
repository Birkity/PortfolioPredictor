def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the dataset by handling missing values and ensuring correct types.

    Args:
        data (pd.DataFrame): Raw data.

    Returns:
        pd.DataFrame: Cleaned data.
    """
    # Check for duplicates
    data = data.drop_duplicates()
    
    # Handle missing values
    if data.isnull().sum().sum() > 0:
        data = data.interpolate(method='time').fillna(method='bfill').fillna(method='ffill')
    
    # Ensure numeric columns have correct types
    numeric_cols = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    data[numeric_cols] = data[numeric_cols].apply(pd.to_numeric, errors='coerce')
    
    return data
