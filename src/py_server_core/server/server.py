import asyncio
import logging

from ..logger import Logger


class Server:
    def __init__(self, host: str, port: int, logs_handles: tuple[logging.Handler]):
        self._listen_address = (host, port)
        self._asyncio_server: asyncio.Server | None = None

        main_logger = Logger(*logs_handles)
        self._logger = main_logger.get_logger(__name__)

    @property
    def in_work(self) -> bool:
        return bool(self._asyncio_server)

    async def _connection_reception(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        pass

    async def up(self):
        self._asyncio_server = await asyncio.start_server(self._connection_reception, *self._listen_address)

        addresses = [(sock.family, sock.getsockname()) for sock in self._asyncio_server.sockets]
        self._logger.info("Server up", extra={"addresses": addresses})

    async def close(self):
        self._asyncio_server.close()
        await self._asyncio_server.wait_closed()
        self._asyncio_server = None
        self._logger.info("Server closed")
