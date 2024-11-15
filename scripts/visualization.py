import logging
import matplotlib.pyplot as plt

def plot_column(data, column, dataset_name):
    """
    Plot a specific column from a dataset.

    Args:
        data (pd.DataFrame): Dataset containing the column.
        column (str): Column to plot.
        dataset_name (str): Name of the dataset.

    Returns:
        None
    """
    logging.info("Plotting column: %s from dataset: %s", column, dataset_name)
    try:
        plt.figure(figsize=(12, 6))
        plt.plot(data.index, data[column], label=column)
        plt.title(f"{column} Over Time ({dataset_name})")
        plt.xlabel("Date")
        plt.ylabel(column)
        plt.legend()
        plt.grid(True)
        plt.show()
        logging.info("Plot for %s generated successfully.", column)
    except Exception as e:
        logging.error("Error generating plot for %s: %s", column, str(e))
        raise
