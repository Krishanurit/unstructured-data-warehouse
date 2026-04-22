import logging
import os


def setup_logger(log_file="logs/app.log", level=logging.INFO):
    """Setup logger configuration"""

    # Create logs directory
    os.makedirs(os.path.dirname(log_file), exist_ok=True)

    logger = logging.getLogger("project_logger")
    logger.setLevel(level)

    # Avoid duplicate handlers
    if logger.hasHandlers():
        logger.handlers.clear()

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level)

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(level)

    # Formatter
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


# Example usage
if __name__ == "__main__":
    logger = setup_logger()

    logger.info("Application started")
    logger.warning("This is a warning")
    logger.error("This is an error")