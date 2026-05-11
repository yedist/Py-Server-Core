import asyncio
import socket

from src.py_server_core import Server


def initial():
    logs = asyncio.Queue()
    server = Server(
        host="127.0.0.1",
        port=0,  # == the system will select a free port
        logs_stream=logs
    )
    return server, logs


async def main():
    server, logs = initial()

    await server.up()
    await server.close()

    up_log, close_log = await logs.get(), await logs.get()

    # ['level'] test:
    assert up_log["level"] == close_log["level"] == 'INFO'

    # ['event'] test:
    assert up_log["event"] == "Server up"
    assert close_log["event"] == "Server closed"

    # content test (up_log):
    assert len(up_log["addresses"]) == 1
    family, address = up_log["addresses"][0]

    assert family == socket.AF_INET  # IPv4 ('127.0.0.1' is IPv4)
    host, port = address  # this is an IPv4 address structure.

    assert host == "127.0.0.1"
    assert 0 < port


if __name__ == '__main__':
    asyncio.run(main())
