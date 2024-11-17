import logging
import os

def setup_logger(log_file="project.log", log_level=logging.INFO):
    """
    Configures the logger to log messages to a file and the console.

    Args:
        log_file (str): Name of the log file.
        log_level (int): Logging level (e.g., logging.INFO, logging.DEBUG).
    """
    # Create logs directory if not exists
    os.makedirs("logs", exist_ok=True)
    log_file_path = os.path.join("logs", log_file)

    # Logging Configuration
    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file_path),
            logging.StreamHandler()
        ]
    )
    logging.info("Logger initialized. Log file: %s", log_file_path)
