import asyncio


class Server:
    def __init__(self):
        ...

    def _status(self):
        ...

    @property
    def in_work(self):
        return ...

    def restart(self):
        self.__init__()

    def up(self):
        ...

    def close(self):
        ...
