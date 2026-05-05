import asyncio
import time


class Logger:
    # no typing
    def __init__(self, *outputs):  # name not good
        self.outputs_task = None
        self._log_pipes =[]
        self._outputs = []

        for output in outputs:
            self._log_pipes.append(q := asyncio.Queue())
            self._outputs.append(output(q))

    async def start(self):
        self.outputs_task = [asyncio.create_task(o) for o in self._outputs]

    @staticmethod
    def get_object_id():
        return time.monotonic_ns()

    async def _save_log(self, level, event, object_id, time=None, **data):
        # no save time
        log = {"level": level, "event": event, "object_id": object_id} | data
        for pipe in self._log_pipes:
            await pipe.put(log)

    async def debug(self, event, object_id, **kwargs):
        await self._save_log("debug", event, object_id, **kwargs)

    async def info(self, event, object_id, **kwargs):
        await self._save_log("info", event, object_id, **kwargs)

    async def error(self, event, object_id, **kwargs):
        await self._save_log("error", event, object_id, **kwargs)

    async def warning(self, event, object_id, **kwargs):
        await self._save_log("warning", event, object_id, **kwargs)

    async def critical(self, event, object_id, **kwargs):
        await self._save_log("critical", event, object_id, **kwargs)
