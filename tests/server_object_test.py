import asyncio
import socket

from src.py_server_core import Server


async def main():
    await server.up()
    await server.close()

    up_log, close_log = await logs.get(), await logs.get()

    # level test:
    assert up_log["level"] == close_log["level"] == 'INFO'

    # event test:
    assert up_log["event"] == "Server up"
    assert close_log["event"] == "Server closed"

    # content test (up_log):
    """
    up_log["addresses"] is list of all the addresses the server is listening on,
    deep down they come from asyncio itself.
    
    Each address belongs to a specific address type (defined in the socket library),
    for example, there are different addresses for IPv4 and IPv6.
    
    The addresses in up_log["addresses"] are always a tuple that contains the address type and the address itself,
    even the type of which can be different between different address families.
    """
    assert len(up_log["addresses"]) == 1
    family, address = up_log["addresses"][0]

    assert family == socket.AF_INET  # IPv4 ('127.0.0.1' is IPv4)
    host, port = address  # this is an IPv4 address structure.

    assert host == "127.0.0.1"
    assert 0 < port


if __name__ == '__main__':
    # << initial >>
    logs = asyncio.Queue()
    server = Server(
        host="127.0.0.1",
        port=0,  # == the system will select a free port
        logs_stream=logs
    )

    # << test >>
    asyncio.run(main())
