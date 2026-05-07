import asyncio


class Logger:
    def __init__(self, logs_stream: asyncio.Queue | None):
        self._logs_stream = logs_stream or asyncio.Queue()
        self.queue = logs_stream

    async def _write_log(self, level, event, object_id, parameters):
        log = {"level": level, "event": event, "object_id": object_id} | parameters
        await self._logs_stream.put(log)

    async def debug(self, event, object_id, **parameters):
        await self._write_log("debug", event, object_id, parameters)

    async def info(self, event, object_id, **parameters):
        await self._write_log("info", event, object_id, parameters)

    async def error(self, event, object_id, **parameters):
        await self._write_log("error", event, object_id, parameters)

    async def warning(self, event, object_id, **parameters):
        await self._write_log("warning", event, object_id, parameters)

    async def critical(self, event, object_id, **parameters):
        await self._write_log("critical", event, object_id, parameters)
