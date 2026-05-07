import copy

from src import py_server_core


class LoggerTester:
    def __init__(self):
        self.logger = py_server_core.Logger()
        self.pipe = self.logger.make_pipe()

    async def send_all(self, logs, object_id=None):
        if not object_id:
            object_id = self.logger.get_object_id()
        for log in logs:
            level, event, data = log
            match level:
                case "debug":
                    await self.logger.debug(event, object_id, **data)
                case "info":
                    await self.logger.info(event, object_id, **data)
                case "warning":
                    await self.logger.warning(event, object_id, **data)
                case "error":
                    await self.logger.error(event, object_id, **data)
                case "critical":
                    await self.logger.critical(event, object_id, **data)
                case _:
                    raise NotImplementedError()
        return object_id

    async def get_all(self, logs, object_id, noise_cancellation=False, key=lambda a, b: a == b):
        for log in copy.deepcopy(logs):
            log.insert(2, object_id)
            while True:
                log_output = await self.pipe.get()
                if log_output is None:
                    return False
                if key(log, log_output):
                    break
                if not noise_cancellation:
                    return False
        return True
