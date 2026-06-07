import asyncio

from py_server_core.connection import Connection
from ._connections_timer_loop import connections_timer_loop


class ConnectionsTimer:
    def __init__(self, ttl: float = -1):
        self.ttl = ttl
        self.connections_queue = asyncio.Queue()  # with lock?

        self._timer_task = asyncio.create_task(
            connections_timer_loop(self.connections_queue, self.ttl)
        )

    async def start_timeout(self, connection: Connection):
        if 0 <= self.ttl:
            await self.connections_queue.put(connection)
