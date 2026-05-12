import asyncio
import logging

from ..logs import LoggingCoordinator


class Server:
    def __init__(self, host: str, port: int, logs_handles: tuple[logging.Handler] = logging.NullHandler()):
        self._listen_address = (host, port)
        self._asyncio_server: asyncio.Server | None = None

        log_service = LoggingCoordinator(*logs_handles)
        self._logger = log_service.get_logger(__name__)

    @property
    def in_work(self) -> bool:
        return bool(self._asyncio_server)

    async def _connection_reception(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        pass

    async def up(self):
        if self.in_work:
            return

        try:
            self._asyncio_server = await asyncio.start_server(self._connection_reception, *self._listen_address)
        except Exception as exception:
            self._logger.error(
                "Server up error",
                extra={
                    "exception_message": str(exception),
                    "exception_type": type(exception).__name__
                }
            )
        else:
            self._logger.info(
                "Server up",
                extra={
                    "addresses": [
                        (sock.family, sock.getsockname()) for sock in self._asyncio_server.sockets
                    ]
                }
            )

    async def close(self):
        if not self.in_work:
            return

        try:
            self._asyncio_server.close()
            await self._asyncio_server.wait_closed()
            self._asyncio_server = None
        except Exception as exception:
            self._logger.error(
                "Server up error",
                extra={
                    "exception_message": str(exception),
                    "exception_type": type(exception).__name__
                }
            )
        else:
            self._logger.info("Server closed")
