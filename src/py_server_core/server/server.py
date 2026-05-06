import asyncio

from ..logger import Logger


# אין אימותים במתודות לפרמטרים, לאובייקטים שבאמת קיימים

class Server:
    def __init__(self, host: str, port: int, logger=None):
        self._logger = logger or Logger()
        self._listen_address = (host, port)

        self._server_id = self._logger.get_object_id()
        self._asyncio_server: asyncio.Server | None = None

    @property
    def in_work(self) -> bool:
        # אסור שיהיה מצב שקיים אובייקט והוא באמת לא פעיל, כי  קיומו מצביע גם על פעילותו
        return bool(self._asyncio_server)

    def restart(self):
        self.__init__(*self._listen_address)

    async def _connection_reception(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        pass

    async def up(self):
        # אין עמידות לשגיאות \ timeout
        self._asyncio_server = await asyncio.start_server(self._connection_reception, *self._listen_address)

        address = [sock.getsockname() for sock in self._asyncio_server.sockets]
        await self._logger.info("Server up", self._server_id, address=address)

    async def close(self):
        # אין עמידות לשגיאות \ timeout
        self._asyncio_server.close()
        await self._asyncio_server.wait_closed()
        self._asyncio_server = None
        await self._logger.info("Server closed", self._server_id)  # exception?
