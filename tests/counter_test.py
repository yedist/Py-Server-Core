from src.py_server_core.connection_manager.counter import Counter
import asyncio


async def test():
    test_counter = Counter(limit=1)

    assert await test_counter.value == 0
    assert not await test_counter.at_limit

    await test_counter.decrement()
    assert await test_counter.value == 0

    await test_counter.increment()
    await test_counter.increment()
    assert await test_counter.value == 1

    assert await test_counter.at_limit


if __name__ == '__main__':
    asyncio.run(test())
