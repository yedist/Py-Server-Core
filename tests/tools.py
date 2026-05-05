from src import py_server_core


async def initial_logger(*outputs):
    logger = py_server_core.Logger(*outputs)
    await logger.start()
    return logger
