import asyncio

from ..logger import Logger


class Server:
    def __init__(self, host: str, port: int, logger=None):
        self._logger = logger or Logger()
        self._listen_address = (host, port)

        self._server_id = self._logger.get_object_id()
        self._asyncio_server: asyncio.Server | None = None

    @property
    def in_work(self) -> bool:
        return bool(self._asyncio_server)

    def restart(self):
        self.__init__(*self._listen_address, logger=self._logger)

    async def _connection_reception(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        pass

    async def up(self):
        self._asyncio_server = await asyncio.start_server(self._connection_reception, *self._listen_address)

        address = [sock.getsockname() for sock in self._asyncio_server.sockets]
        await self._logger.info("server up", self._server_id, address=address)

    async def close(self):
        self._asyncio_server.close()
        await self._asyncio_server.wait_closed()
        self._asyncio_server = None
        await self._logger.info("server closed", self._server_id)
