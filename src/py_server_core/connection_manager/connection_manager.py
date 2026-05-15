from .counter import Counter


class ConnectionManager:
    def __init__(self, handler, max_connections: int):
        self.max_connections = max_connections
        self._connections_counter = Counter(max_connections)

    async def new_connection(self, connection):
        if self._connections_counter.at_limit:
            ...
        else:
            await self._connections_counter.up()
            try:
                await handler(connection)
            finally:
                await self._connections_counter.down()
