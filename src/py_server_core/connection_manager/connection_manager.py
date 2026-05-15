class ConnectionManager:
    def __init__(self, handler, max_connections: int):
        self.max_connections = max_connections
        self._connections_counter = 0

    async def new_connection(self, connection):
        self._connections_counter += 1
        await handler(connection)
        self._connections_counter -= 1
