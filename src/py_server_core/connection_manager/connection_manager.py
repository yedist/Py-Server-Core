from ..connection import Connection


class ConnectionManager:
    def __init__(self):
        self._all_connections = set()

    async def num_connections(self):
        return len(self._all_connections)

    async def registration(self, connection: Connection):
        self._all_connections.add(connection)

    async def unregistration(self, connection: Connection):
        self._all_connections.remove(connection)

    def close_all_connections(self):
        ...
