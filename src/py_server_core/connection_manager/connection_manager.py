from ..connection import Connection


class ConnectionManager:
    def __init__(self):
        self.connections_counter = 0

    def new_connection(self, connection: Connection):
        self.connections_counter += 1

    def close_connection(self, connection: Connection):
        self.connections_counter -= 1

    def close_all_connections(self):
        ...
