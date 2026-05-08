import asyncio

from src.py_server_core import Logger


async def test():
    await logger.debug("debug event")
    assert await logs_stream.get() == {"level": "debug", "event": "debug event"}

    await logger.info("info event")
    assert await logs_stream.get() == {"level": "info", "event": "info event"}

    await logger.warning("warning event")
    assert await logs_stream.get() == {"level": "warning", "event": "warning event"}

    await logger.error("error event")
    assert await logs_stream.get() == {"level": "error", "event": "error event"}

    await logger.critical("critical event")
    assert await logs_stream.get() == {"level": "critical", "event": "critical event"}


if __name__ == '__main__':
    # << initial >>
    logs_stream = asyncio.Queue()
    logger = Logger(logs_stream)

    # << test >>
    asyncio.run(test())
