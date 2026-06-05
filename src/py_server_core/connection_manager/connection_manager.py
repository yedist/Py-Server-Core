from ..connection import Connection
from .counter import Counter


class ConnectionManager:
    def __init__(self):
        self._connections_counter = Counter()

    @property
    async def num_connections(self):
        return await self._connections_counter.value

    async def new_connection(self, connection: Connection):
        await self.connections_counter.increment()

    async def close_connection(self, connection: Connection):
        await self.connections_counter.decrement()
        await connection.close()

    def close_all_connections(self):
        ...
