from ..connection import Connection
from .counter import Counter


class ConnectionManager:
    def __init__(self):
        self._connections_counter = Counter()

    @property
    async def num_connections(self):
        return await self._connections_counter.value

    async def registration(self, connection: Connection):
        await self.connections_counter.increment()

    async def unregistration(self, connection: Connection):
        await self.connections_counter.decrement()

    def close_all_connections(self):
        ...
