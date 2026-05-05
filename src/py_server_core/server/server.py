import asyncio


class Server:
    def __init__(self, host, port):
        self._listen_address = (host, port)
        self._asyncio_server: asyncio.Server | None = None

    def _status(self):
        ...

    @property
    def in_work(self):
        return ...

    def restart(self):
        self.__init__(*self._listen_address)

    async def _connection_reception(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        pass

    async def up(self):
        self._asyncio_server = await asyncio.start_server(self._connection_reception, *self._listen_address)

    def close(self):
        ...
