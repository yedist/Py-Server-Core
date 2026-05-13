class ServerError(Exception):
    pass


class ServerStartError(ServerError):
    pass


class ServerCloseError(ServerError):
    pass
