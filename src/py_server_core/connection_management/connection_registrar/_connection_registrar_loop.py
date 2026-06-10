from asyncio import Queue

from py_server_core.connection import Connection


async def unregistration_loop(closed_connections_queue: Queue, connections_base: set[Connection]):
    while True:
        connections_base.discard(
            await closed_connections_queue.get()
        )
