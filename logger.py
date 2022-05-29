import logging


def create_logger():
    logger = logging.getLogger("basic")
    logger.setLevel("DEBUG")

    file_handler = logging.FileHandler("basic.txt")
    logger.addHandler(file_handler)

    logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")

    return logger

