import asyncio

from src.py_server_core import Logger


async def main():
    logger = Logger()
    pipe = logger.make_pipe()

    await logger.debug("debug event", None)
    assert await pipe.get() == {"level": "debug", "event": "debug event", "object_id": None}

    await logger.info("info event", None)
    assert await pipe.get() == {"level": "info", "event": "info event", "object_id": None}

    await logger.warning("warning event", None)
    assert await pipe.get() == {"level": "warning", "event": "warning event", "object_id": None}

    await logger.error("error event", None)
    assert await pipe.get() == {"level": "error", "event": "error event", "object_id": None}

    await logger.critical("critical event", None)
    assert await pipe.get() == {"level": "critical", "event": "critical event", "object_id": None}


if __name__ == '__main__':
    asyncio.run(main())
