import logging
import logging.handlers
from queue import Queue


def make_logger(name: str, handler: logging.Handler) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.addHandler(handler)
    logger.setLevel(logging.DEBUG)
    logger.propagate = False
    return logger


class LogManager:
    def __init__(self, *handlers: logging.Handler, auto_start=True):
        self._handler = logging.handlers.QueueHandler(Queue())
        self._listener = logging.handlers.QueueListener(self._handler.queue, *handlers)

        self.logger = make_logger(__name__, self._handler)

        if auto_start:
            self.start()

    def start(self):
        self._listener.start()

    def stop(self):
        self._listener.stop()
