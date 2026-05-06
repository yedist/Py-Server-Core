import asyncio
import time
import uuid


class Logger:
    # no typing
    def __init__(self):  # name not good
        self._output_pipes = []

    def make_pipe(self):
        self._output_pipes.append(q := asyncio.Queue())
        return q

    @staticmethod
    def get_object_id():
        return uuid.uuid4()

    async def _save_log(self, log):
        for pipe in self._output_pipes:
            await pipe.put(log)

    async def debug(self, event, object_id, **kwargs):
        await self._save_log(["debug", event, object_id, kwargs])

    async def info(self, event, object_id, **kwargs):
        await self._save_log(["info", event, object_id, kwargs])

    async def error(self, event, object_id, **kwargs):
        await self._save_log(["error", event, object_id, kwargs])

    async def warning(self, event, object_id, **kwargs):
        await self._save_log(["warning", event, object_id, kwargs])

    async def critical(self, event, object_id, **kwargs):
        await self._save_log(["critical", event, object_id, kwargs])

    async def close(self):
        await self._save_log(None)
