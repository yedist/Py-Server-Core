from .default_events import (
    connection_handler,
    on_resume_connection,
    on_close_connection,
)
from .counter import Counter


class ConnectionManager:
    def __init__(self, max_connections: int, events):
        self.max_connections = max_connections
        self._counter = Counter(max_connections)

        self._connection_handler = events.get(
            "connection_handler",
            connection_handler
        )
        self._on_close_connection = events.get(
            "on_close_connection",
            on_close_connection
        )
        self._on_resume_connection = events.get(
            "on_resume_connection",
            on_resume_connection
        )

    async def new_connection(self, connection):
        if self._counter.at_limit:
            await self._on_resume_connection(connection)
            await self.close_connection(connection)
            return

        await self._counter.increment()

        try:
            await self._connection_handler(connection)
        finally:
            await self._on_close_connection(connection)
            await self.close_connection(connection)
            await self._counter.decrement()

    async def close_connection(self, connection):
        ...  # closing
