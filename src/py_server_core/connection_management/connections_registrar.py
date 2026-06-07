import asyncio
from typing import Final

from ..connection import Connection


class ConnectionRegistrar:
    def __init__(self, max_connections: int | None = None):
        self.max_connections: Final[int | float] = max_connections or float('inf')
        self.closed_connections_queue: asyncio.Queue[Connection] = asyncio.Queue()
        self._all_connections = set()

        self._unregistration_task = asyncio.create_task(self._unregistration_loop())

    @property
    async def num_connections(self):
        return len(self._all_connections)

    async def registration(self, connection: Connection):
        if self.max_connections < self.num_connections:
            self._all_connections.add(connection)
        else:
            ...  # reached the limit

    async def _unregistration_loop(self):
        while True:
            connection: Connection = await self.closed_connections_queue.get()
            self._all_connections.discard(connection)
