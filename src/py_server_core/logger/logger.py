import asyncio


class Logger:
    # no typing
    def __init__(self, *outputs):  # name not good
        self.outputs_task = None
        self._log_pipes =[]
        self._outputs = []

        for output in outputs:
            self._log_pipes.append(q := asyncio.Queue())
            self._outputs.append(output(q))

    async def _start(self):
        self.outputs_task = asyncio.create_task(asyncio.gather(*self._outputs))

    async def _save_log(self, level, event, time=None, **data):
        # no save time
        log = {"level": level, "event": event} | data
        for pipe in self._log_pipes:
            await pipe.put(log)

    async def __call__(self, *args, **kwargs):
        await self(*args, **kwargs)

    async def debug(self, event, **kwargs):
        await self("debug", event, **kwargs)

    async def info(self, event, **kwargs):
        await self("info", event, **kwargs)

    async def error(self, event, **kwargs):
        await self("error", event, **kwargs)

    async def warning(self, event, **kwargs):
        await self("warning", event, **kwargs)

    async def critical(self, event, **kwargs):
        await self("critical", event, **kwargs)
