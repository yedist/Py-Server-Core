from typing import Final

from ..connection import Connection
from .connections_timer import ConnectionsTimer
from .noop_connections_timer import NoOpConnectionsTimer


class ConnectionManager:
    def __init__(self, max_connections: int | None = None, connection_ttl: float = NoOpConnectionsTimer()):
        self.max_connections: Final[int | float] = max_connections or float('inf')
        self.connection_timer = ConnectionsTimer(connection_ttl)
        self._all_connections = set()

    @property
    async def num_connections(self):
        return len(self._all_connections)

    async def registration(self, connection: Connection):
        if self.max_connections < self.num_connections:
            self._all_connections.add(connection)
            await self.connection_timer.start_timeout(connection)

    async def unregistration(self, connection: Connection):
        self._all_connections.discard(connection)

    def close_all_connections(self):
        ...
