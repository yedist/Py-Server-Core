import asyncio

from src.py_server_core import Logger, LogLevels


async def test():
    await logger.debug("debug event")
    assert await logs_stream.get() == {"level": LogLevels.DEBUG, "event": "debug event"}

    await logger.info("info event")
    assert await logs_stream.get() == {"level": LogLevels.INFO, "event": "info event"}

    await logger.warning("warning event")
    assert await logs_stream.get() == {"level": LogLevels.WARNING, "event": "warning event"}

    await logger.error("error event")
    assert await logs_stream.get() == {"level": LogLevels.ERROR, "event": "error event"}

    await logger.critical("critical event")
    assert await logs_stream.get() == {"level": LogLevels.CRITICAL, "event": "critical event"}


if __name__ == '__main__':
    # << initial >>
    logs_stream = asyncio.Queue()
    logger = Logger(logs_stream)

    # << test >>
    asyncio.run(test())
