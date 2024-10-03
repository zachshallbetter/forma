import logging

def get_logger(name):
    logger = logging.getLogger(name)
    if not logger.handlers:
        # Configure logging handlers if needed
        ch = logging.StreamHandler()
        formatter = logging.Formatter('[%(levelname)s] %(asctime)s - %(name)s - %(message)s')
        ch.setFormatter(formatter)
        logger.addHandler(ch)
    return logger