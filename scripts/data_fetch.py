import yfinance as yf
import logging
import os
from datetime import datetime


log_directory = "../logs"
if not os.path.isdir(log_directory):
    os.makedirs(log_directory)


log_path = os.path.join(log_directory, f'stock_download_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler(log_path)]
)

logger = logging.getLogger('StockDataLogger')

try:
    logger.info("Initiating historical stock data download")

    stock_symbols = ['TSLA', 'BND', 'SPY']
    logger.info(f"Fetching data for tickers: {', '.join(stock_symbols)}")


    stock_data = yf.download(stock_symbols, start="2015-01-01", end="2023-01-01", group_by='ticker')
    logger.info("Data download was successful")


    data_directory = "C:/Users/USER/Documents/OPLearning/10_Academy/Week_11/data"
    if not os.path.isdir(data_directory):
        os.makedirs(data_directory)

    
    for symbol in stock_symbols:
        try:
            
            symbol_data = stock_data[symbol]

            
            file_path = os.path.join(data_directory, f'{symbol}_data.csv')
            symbol_data.to_csv(file_path)
            logger.info(f"Data for {symbol} saved at {file_path}")

        except Exception as save_error:
            logger.error(f"Failed to save data for {symbol}: {save_error}")

except Exception as download_error:
    logger.error(f"Error occurred during the download process: {download_error}")
    raise

finally:
    logger.info("Stock data download process complete")
