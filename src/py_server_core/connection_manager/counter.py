import asyncio


class Counter:
    def __init__(self, limit):
        self.limit = limit

        self.value = 0
        self._lock = asyncio.Lock()

    @property
    async def at_limit(self):
        async with self._lock:
            return self.limit <= self.value

    async def add(self):
        async with self._lock:
            self.value = min(self.limit, self.value + 1)

    async def reduce(self):
        async with self._lock:
            self.value = max(0, self.value - 1)
