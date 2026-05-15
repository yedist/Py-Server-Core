import asyncio


class Counter:
    def __init__(self, limit):
        self.limit = limit
        self._value = 0
        self._lock = asyncio.Lock()

    @property
    async def at_limit(self):
        async with self._lock:
            return self._value >= self._limit

    @property
    async def value(self):
        async with self._lock:
            return self._value

    async def increment(self):
        async with self._lock:
            self._value = min(self.limit, self._value + 1)

    async def decrement(self):
        async with self._lock:
            self._value = max(0, self._value - 1)
