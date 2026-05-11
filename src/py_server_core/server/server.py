import asyncio

from ..logger import Logger


class Server:
    def __init__(self, host: str, port: int, logs_stream: asyncio.Queue[dict] | None = None):
        self._logger = Logger(logs_stream) if logs_stream else Logger.noop()
        self._listen_address = (host, port)

        self._asyncio_server: asyncio.Server | None = None

    @property
    def in_work(self) -> bool:
        return bool(self._asyncio_server)

    async def _connection_reception(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        pass

    async def up(self):
        self._asyncio_server = await asyncio.start_server(self._connection_reception, *self._listen_address)

        address = [sock.getsockname() for sock in self._asyncio_server.sockets]
        await self._logger.info("Server up", address=address)

    async def close(self):
        self._asyncio_server.close()
        await self._asyncio_server.wait_closed()
        self._asyncio_server = None
        await self._logger.info("Server closed")
