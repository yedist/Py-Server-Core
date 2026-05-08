from asyncio import Queue

from . import _fixed


class Logger:
    def __init__(self, logs_stream: Queue):
        if not isinstance(logs_stream, Queue):
            raise TypeError(
                "logs_stream must be an instance of asyncio.Queue"
            )

        self._logs_stream = logs_stream
        self.queue = logs_stream

    @classmethod
    def noop(cls):
        return cls(Queue())

    async def debug(self, event, **parameters):
        await self._write_log(_fixed.DEBUG, event, parameters)

    async def info(self, event, **parameters):
        await self._write_log(_fixed.INFO, event, parameters)

    async def error(self, event, **parameters):
        await self._write_log(_fixed.ERROR, event, parameters)

    async def warning(self, event, **parameters):
        await self._write_log(_fixed.WARNING, event, parameters)

    async def critical(self, event, **parameters):
        await self._write_log(_fixed.CRITICAL, event, parameters)

    async def _write_log(self, level, event, parameters):
        log = {"level": level, "event": event} | parameters
        await self._logs_stream.put(log)
