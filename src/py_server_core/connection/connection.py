from asyncio import StreamReader, StreamWriter

from ..connection_manager import ConnectionManager


class Connection:
    def __init__(self, reader: StreamReader, writer: StreamWriter, manager: ConnectionManager | None = None):
        self._reader = reader
        self._writer = writer
        self._manager = manager

        self.closed = False

    async def get(self) -> bytes:
        return await self._reader.read(1024)

    async def send(self, data: bytes):
        self._writer.write(data)
        await self._writer.drain()

    async def close(self):
        if self.closed:
            return

        self._writer.close()
        await self._writer.wait_closed()
        self.closed = True

        if self._manager:
            await self._manager.close_connection(self)
