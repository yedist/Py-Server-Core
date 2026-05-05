import asyncio

from tools import initial_logger

test_id = None


async def test(pipe):
    test_logs = [await pipe.get() for _ in range(5)]

    for log in test_logs:
        assert "event" in log and "level" in log and "object_id" in log

    assert all(log.get("object_id") == test_id for log in test_logs)

async def main():
    global test_id
    logger = await initial_logger(test)
    test_id = logger.get_object_id()

    await logger.debug("test(d)", test_id)
    await logger.info("test(i)", test_id)
    await logger.error("test(e)", test_id)
    await logger.warning("test(w)", test_id)
    await logger.critical("test(c)", test_id)

if __name__ == '__main__':
    asyncio.run(main())
