import logging


def setup_logger(log_file="log_scan_results.log", level=logging.INFO):
    """Set up the logger."""
    logger = logging.getLogger("PortScanner")
    logger.setLevel(level)

    # Create a file handler to write logs to a file
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level)

    # Create a formatter and set it for the handler
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(formatter)

    # Add the handler to the logger
    logger.addHandler(file_handler)

    # Avoid duplicate logs
    logger.propagate = False

    return logger
