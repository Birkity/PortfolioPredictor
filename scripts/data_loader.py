import logging
import pandas as pd

def load_data(filepath):
    """
    Load data from a CSV file.

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data as a DataFrame.
    """
    logging.info("Loading data from %s", filepath)
    try:
        data = pd.read_csv(filepath)
        logging.info("Data loaded successfully. Shape: %s", data.shape)
        return data
    except Exception as e:
        logging.error("Failed to load data from %s: %s", filepath, str(e))
        raise
