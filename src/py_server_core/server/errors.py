class ServerError(Exception):
    pass

class ServerStartingError(ServerError):
    pass

class ServerClosingError(ServerError):
    pass
