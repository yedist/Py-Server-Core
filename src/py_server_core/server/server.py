import asyncio
import logging
from collections.abc import Iterable

from .errors import ServerStartingError, ServerClosingError
from ..logs import LoggingCoordinator


class Server:
    def __init__(self, host: str, port: int, log_handlers: Iterable[logging.Handler] = logging.NullHandler()):
        self._listen_address = (host, port)
        self._asyncio_server: asyncio.Server | None = None

        log_service = LoggingCoordinator(*log_handlers)
        self._logger = log_service.get_logger(__name__)

    @property
    def is_running(self) -> bool:
        return self._asyncio_server is not None

    async def _connection_reception(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        pass

    async def up(self):
        if self.is_running:
            return

        try:
            self._asyncio_server = await asyncio.start_server(self._connection_reception, *self._listen_address)
        except Exception as exception:
            self._logger.exception("Server up error")
            raise ServerStartingError(exception) from exception
        else:
            self._logger.info(
                "Server up",
                extra={
                    "addresses": [
                        (sock.family, sock.getsockname()) for sock in (self._asyncio_server.sockets or [])
                    ]
                }
            )

    async def close(self):
        if not self.is_running:
            return

        try:
            self._asyncio_server.close()
            await self._asyncio_server.wait_closed()
            self._asyncio_server = None
        except Exception as exception:
            self._logger.exception("Server close error")
            raise ServerClosingError(exception) from exception
        else:
            self._logger.info("Server closed")
