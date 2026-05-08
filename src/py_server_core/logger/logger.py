from asyncio import Queue

from .log_level import LogLevel, HIERARCHY


class Logger:
    def __init__(self, logs_stream: Queue, filter_to_level: LogLevel = LogLevel.DEBUG):
        if not isinstance(logs_stream, Queue):
            raise TypeError(
                "logs_stream must be an instance of asyncio.Queue"
            )

        self.logs_stream = logs_stream
        self._legal_steps = HIERARCHY[
            HIERARCHY.index(filter_to_level):
        ]

    @classmethod
    def noop(cls):
        return cls(Queue())

    async def debug(self, event, **parameters):
        await self._write_log(LogLevel.DEBUG, event, parameters)

    async def info(self, event, **parameters):
        await self._write_log(LogLevel.INFO, event, parameters)

    async def error(self, event, **parameters):
        await self._write_log(LogLevel.ERROR, event, parameters)

    async def warning(self, event, **parameters):
        await self._write_log(LogLevel.WARNING, event, parameters)

    async def critical(self, event, **parameters):
        await self._write_log(LogLevel.CRITICAL, event, parameters)

    async def _write_log(self, level, event, parameters):
        if level in self._legal_steps:
            log = {"level": level, "event": event} | parameters
            await self.logs_stream.put(log)
