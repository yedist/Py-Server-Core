import asyncio
from time import monotonic

from py_server_core.connection import Connection


async def _wait_for_monotonic(target: float):
    while monotonic() < target:
        await asyncio.sleep(0.01)


async def connections_timer_loop(queue: asyncio.Queue, ttl: float):
    while True:
        connection: Connection = await queue.get()
        await _wait_for_monotonic(connection.start_time + ttl)
        await connection.close()
