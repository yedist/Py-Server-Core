import logging
import logging.handlers


def get_logger(name: str, handler: logging.Handler) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.addHandler(handler or logging.NullHandler())
    return logger
