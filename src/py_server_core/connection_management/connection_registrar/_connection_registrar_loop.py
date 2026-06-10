import asyncio


async def _unregistration_loop(closed_connections_queue: asyncio.Queue, connections_base: set):
    while True:
        connections_base.discard(
            await closed_connections_queue.get()
        )
