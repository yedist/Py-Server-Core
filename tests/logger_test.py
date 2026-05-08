import asyncio

from src.py_server_core import Logger, LogLevel


async def test():
    await logger.debug("debug event")
    assert await logs_stream.get() == {"level": LogLevel.DEBUG, "event": "debug event"}

    await logger.info("info event")
    assert await logs_stream.get() == {"level": LogLevel.INFO, "event": "info event"}

    await logger.warning("warning event")
    assert await logs_stream.get() == {"level": LogLevel.WARNING, "event": "warning event"}

    await logger.error("error event")
    assert await logs_stream.get() == {"level": LogLevel.ERROR, "event": "error event"}

    await logger.critical("critical event")
    assert await logs_stream.get() == {"level": LogLevel.CRITICAL, "event": "critical event"}


if __name__ == '__main__':
    # << initial >>
    logs_stream = asyncio.Queue()
    logger = Logger(logs_stream)

    # << test >>
    asyncio.run(test())
