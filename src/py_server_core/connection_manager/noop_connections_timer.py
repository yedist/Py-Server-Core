from ..connection import Connection


class NoOpConnectionsTimer:
    async def start_timeout(self, connection: Connection):
        pass

    async def _loop(self):
        pass
