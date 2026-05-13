import logging
import logging.handlers
from queue import Queue


class LoggingCoordinator:
    def __init__(self, *handlers: logging.Handler, auto_start=True):
        self._handler = logging.handlers.QueueHandler(Queue())
        self.listener = logging.handlers.QueueListener(self._handler.queue, *handlers)

        if auto_start:
            self.start()

    def start(self):
        self.listener.start()

    def stop(self):
        self.listener.stop()

    def get_logger(self, name: str) -> logging.Logger:
        logger = logging.getLogger(name)
        logger.addHandler(self._handler)
        logger.setLevel(logging.DEBUG)
        logger.propagate = False
        return logger
