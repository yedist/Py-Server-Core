import asyncio


class Server:
    def __init__(self, host: str, port: int):
        self._listen_address = (host, port)
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

    async def close(self):
        # אין עמידות לשגיאות \ timeout
        self._asyncio_server.close()
        await self._asyncio_server.wait_closed()
        self._asyncio_server = None
