import asyncio
import logging
from collections.abc import Iterable

from .errors import ServerStartError, ServerCloseError
from ..logs import get_logger


class Server:
    def __init__(self, host: str, port: int, log_handler: Iterable[logging.Handler] = logging.NullHandler()):
        self._host = host
        self._port = port
        self._server: asyncio.Server | None = None

        self._logger = get_logger(__name__, log_handler)

    @property
    def is_running(self) -> bool:
        return self._server is not None

    async def _on_connection(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        pass

    async def up(self):
        if self.is_running:
            return

        try:
            self._server = await asyncio.start_server(self._on_connection, self._host, self._port)
        except Exception as exc:
            self._logger.exception("Server up error")
            raise ServerStartError(exc) from exc
        else:
            addresses = [
                (sock.family, sock.getsockname())
                for sock in (self._server.sockets or [])
            ]
            self._logger.info("Server up", extra={"addresses": addresses})

    async def close(self):
        if not self.is_running:
            return

        try:
            self._server.close()
            await self._server.wait_closed()
            self._server = None
        except Exception as exc:
            self._logger.exception("Server close error")
            raise ServerCloseError(exc) from exc
        else:
            self._logger.info("Server closed")
