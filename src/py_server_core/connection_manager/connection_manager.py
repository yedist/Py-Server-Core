from ..connection import Connection


class ConnectionManager:
    def __init__(self):
        ...

    def new_connection(self, connection: Connection):
        ...

    def close_all_connections(self):
        ...
