from asyncio import Queue

from .log_level import LogLevel, LogLevels


class Logger:
    def __init__(self, logs_stream: Queue, filter_to_level: LogLevel = LogLevels.DEBUG):
        if not isinstance(logs_stream, Queue):
            raise TypeError(
                "logs_stream must be an instance of asyncio.Queue"
            )

        self.logs_stream = logs_stream
        self._level_filter = filter_to_level

    @classmethod
    def noop(cls):
        return cls(Queue())

    async def debug(self, event, **parameters):
        await self._write_log(LogLevels.DEBUG, event, parameters)

    async def info(self, event, **parameters):
        await self._write_log(LogLevels.INFO, event, parameters)

    async def error(self, event, **parameters):
        await self._write_log(LogLevels.ERROR, event, parameters)

    async def warning(self, event, **parameters):
        await self._write_log(LogLevels.WARNING, event, parameters)

    async def critical(self, event, **parameters):
        await self._write_log(LogLevels.CRITICAL, event, parameters)

    async def _write_log(self, level, event, parameters):
        if level >= self._level_filter:
            log = {"level": level, "event": event} | parameters
            await self.logs_stream.put(log)
