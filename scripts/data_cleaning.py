import logging

def clean_dataset(data):
    """
    Clean a single dataset by removing missing values and converting columns.

    Args:
        data (pd.DataFrame): Raw dataset.

    Returns:
        pd.DataFrame: Cleaned dataset.
    """
    logging.info("Starting data cleaning.")
    logging.info("Initial data shape: %s", data.shape)
    try:
        # Drop duplicates
        data.drop_duplicates(inplace=True)
        
        # Remove rows with missing values
        data.dropna(inplace=True)

        # Ensure appropriate datatypes
        if 'Date' in data.columns:
            data['Date'] = pd.to_datetime(data['Date'])
            data.set_index('Date', inplace=True)
        
        logging.info("Final data shape: %s", data.shape)
        logging.info("Data cleaning completed.")
        return data
    except Exception as e:
        logging.error("Error during data cleaning: %s", str(e))
        raise

def clean_multiple_datasets(datasets):
    """
    Clean multiple datasets.

    Args:
        datasets (dict): Dictionary of datasets to clean.

    Returns:
        dict: Cleaned datasets.
    """
    cleaned_datasets = {}
    for name, data in datasets.items():
        logging.info("Cleaning dataset: %s", name)
        cleaned_datasets[name] = clean_dataset(data)
    return cleaned_datasets
