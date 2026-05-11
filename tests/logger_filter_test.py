import asyncio

from src.py_server_core import Logger, LogLevels


async def test():
    await logger.debug("debug event")
    await logger.critical("critical event")

    assert await logs_stream.get() == {"level": LogLevels.CRITICAL, "event": "critical event"}


if __name__ == '__main__':
    # << initial >>
    logs_stream = asyncio.Queue()
    logger = Logger(logs_stream, filter_to_level=LogLevels.CRITICAL)

    # << test >>
    asyncio.run(test())
