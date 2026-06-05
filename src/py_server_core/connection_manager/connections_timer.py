import asyncio
from time import monotonic

from ..connection import Connection


async def _wait_for_monotonic(target: float):
    while monotonic() < target:
        await asyncio.sleep(0.01)


class ConnectionsTimer:
    def __init__(self, ttl: float):
        self._ttl = ttl
        self.connections_queue = asyncio.Queue()
        self._timer_task = asyncio.create_task(self._loop())

    async def start_timeout(self, connection: Connection):
        await self.connections_queue.put(connection)

    async def _loop(self):
        while True:
            connection: Connection = await self.connections_queue.get()
            await _wait_for_monotonic(connection.start_time + self._ttl)
            await connection.close()
