import asyncio

from src import py_server_core


async def ps(pipe):
    await pipe.get()

async def main():
    logger = py_server_core.Logger(ps)
    await logger.start()
    await logger.info("hay", 102, x=10)


if __name__ == '__main__':
    asyncio.run(main())
