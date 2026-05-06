import asyncio

from tools import LoggerTester


TEST_LOGS = (
    ["debug", "debug event", {}],
    ["info", "info event", {}],
    ["warning", "warning event", {}],
    ["error", "error event", {}],
    ["critical", "critical event", {}]
)


async def test():
    tester = LoggerTester()
    object_id = await tester.send_all(TEST_LOGS)
    assert await tester.get_all(TEST_LOGS, object_id=object_id)


if __name__ == '__main__':
    asyncio.run(test())
