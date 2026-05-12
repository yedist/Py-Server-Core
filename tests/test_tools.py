import logging.handlers
import queue


def test_log_queue():
    logs = queue.Queue()
    return logs, logging.handlers.QueueHandler(logs)
