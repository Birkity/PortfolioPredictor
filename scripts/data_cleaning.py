import logging
import pandas as pd

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("data_cleaning.log"),
        logging.StreamHandler()
    ]
)

def clean_data(data: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the dataset by handling missing values and ensuring correct types.

    Args:
        data (pd.DataFrame): Raw data.

    Returns:
        pd.DataFrame: Cleaned data.
    """
    logging.info("Starting data cleaning.")
    
    # Initial data shape
    logging.info(f"Initial data shape: {data.shape}")
    
    # Check for duplicates
    initial_duplicates = data.duplicated().sum()
    if initial_duplicates > 0:
        data = data.drop_duplicates()
        logging.info(f"Removed {initial_duplicates} duplicate rows.")
    
    # Handle missing values
    total_missing_before = data.isnull().sum().sum()
    if total_missing_before > 0:
        data = data.interpolate(method='time').fillna(method='bfill').fillna(method='ffill')
        total_missing_after = data.isnull().sum().sum()
        logging.info(f"Handled missing values: {total_missing_before} → {total_missing_after} remaining.")
    
    # Ensure numeric columns have correct types
    numeric_cols = ['Open', 'High', 'Low', 'Close', 'Adj Close', 'Volume']
    for col in numeric_cols:
        if col in data.columns:
            data[col] = pd.to_numeric(data[col], errors='coerce')
            logging.info(f"Ensured numeric type for column: {col}")
    
    # Final data shape
    logging.info(f"Final data shape: {data.shape}")
    logging.info("Data cleaning completed.")
    
    return data

def clean_multiple_datasets(datasets: dict) -> dict:
    """
    Clean multiple datasets.

    Args:
        datasets (dict): A dictionary of datasets with names as keys and DataFrames as values.

    Returns:
        dict: A dictionary of cleaned datasets.
    """
    cleaned_datasets = {}
    for name, df in datasets.items():
        logging.info(f"Cleaning dataset: {name}")
        try:
            cleaned_datasets[name] = clean_data(df)
        except Exception as e:
            logging.error(f"Error cleaning dataset {name}: {e}")
            cleaned_datasets[name] = None
    return cleaned_datasets
