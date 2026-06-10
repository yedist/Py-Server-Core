import asyncio
from typing import Final

from py_server_core.connection import Connection
from ._connection_registrar_loop import unregistration_loop


class ConnectionRegistrar:
    def __init__(self, max_connections: int | None = None):
        self.max_connections: Final[int | float] = max_connections or float('inf')
        self.closed_connections_queue: asyncio.Queue[Connection] = asyncio.Queue()
        self._all_connections: set[Connection] = set()

        self._unregistration_task = asyncio.create_task(
            unregistration_loop(self.closed_connections_queue, self._all_connections)
        )

    @property
    async def num_connections(self):
        return len(self._all_connections)

    async def registration(self, connection: Connection):
        if self.max_connections < self.num_connections:
            self._all_connections.add(connection)
        else:
            ...  # reached the limit
