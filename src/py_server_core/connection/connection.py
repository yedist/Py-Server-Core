from asyncio import StreamReader, StreamWriter


class Connection:
    def __init__(self, reader: StreamReader, writer: StreamWriter):
        self._reader = reader
        self._writer = writer

    async def get(self) -> bytes:
        return await self._reader.read(1024)

    async def send(self, data: bytes):
        self._writer.write(data)
        await self._writer.drain()
