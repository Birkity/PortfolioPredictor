import logging
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def perform_eda(data, dataset_name):
    """
    Perform exploratory data analysis on a dataset.

    Args:
        data (pd.DataFrame): Dataset to analyze.
        dataset_name (str): Name of the dataset.

    Returns:
        None
    """
    logging.info("Performing EDA for dataset: %s", dataset_name)
    try:
        # Summary statistics
        logging.info("Summary statistics:\n%s", data.describe())

        # Correlation analysis
        corr = data.corr()
        logging.info("Correlation matrix:\n%s", corr)

        # Identify outliers
        outliers = data[(data['Close'] > data['Close'].quantile(0.99)) |
                        (data['Close'] < data['Close'].quantile(0.01))]
        logging.info("Outliers identified: %d", len(outliers))

        # Visualize correlation matrix
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
        plt.title('Correlation Matrix')
        plt.tight_layout()
        plt.show()

    except Exception as e:
        logging.error("Error during EDA: %s", str(e))
        raise
