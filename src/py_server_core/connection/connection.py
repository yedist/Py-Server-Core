from asyncio import StreamReader, StreamWriter
from time import monotonic

from ..connection_manager import ConnectionManager


noop_connection_manger = ConnectionManager()


class Connection:
    def __init__(
        self,
        reader: StreamReader,
        writer: StreamWriter,
        manager: ConnectionManager = noop_connection_manger
    ):
        self._reader = reader
        self._writer = writer
        self._manager = manager
        self.start_time = monotonic()

    async def get(self) -> bytes:
        return await self._reader.read(1024)

    async def send(self, data: bytes):
        self._writer.write(data)
        await self._writer.drain()

    async def close(self) -> bool:
        try:
            self._writer.close()
            await self._writer.wait_closed()
        except:
            ...  # log...
            return False  # closing failed
        else:
            return True  # closing success
        finally:
            await self._manager.unregistration(self)
