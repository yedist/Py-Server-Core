import asyncio


class Connection:
    def __init__(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        self._reader = reader
        self._writer = writer

    async def close(self):
        self._writer.close()
        await self._writer.wait_closed()
