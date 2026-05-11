class LogLevel(str):
    def __new__(cls, level: str, rank: int):
        obj = super().__new__(cls, level)
        obj.rank = rank
        return obj

    def __lt__(self, other):
        return self.rank < other.rank

    def __le__(self, other):
        return self.rank <= other.rank

    def __gt__(self, other):
        return self.rank > other.rank

    def __ge__(self, other):
        return self.rank >= other.rank


class LogLevels:
    DEBUG = LogLevel("DEBUG", 1)
    INFO = LogLevel("INFO", 2)
    WARNING = LogLevel("WARNING", 3)
    ERROR = LogLevel("ERROR", 4)
    CRITICAL = LogLevel("CRITICAL", 5)
