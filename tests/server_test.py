import asyncio

from src.py_server_core import Server

from tools import LoggerTester


TEST_LOGS = (
    ["info", "server up", {}],
    ["info", "server closed", {}],
)


async def test():
    tester = LoggerTester()
    server = Server("localhost", 0, logger=tester.logger)

    await server.up()
    await server.close()
    assert await tester.get_all(TEST_LOGS, object_id=server._server_id, key=lambda a, b: a[:-1] == b[:-1])

    server.restart()

    await server.up()
    await server.close()
    assert await tester.get_all(TEST_LOGS, object_id=server._server_id, key=lambda a, b: a[:-1] == b[:-1])


if __name__ == '__main__':
    asyncio.run(test())
