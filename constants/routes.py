from enum import Enum, verify, UNIQUE


@verify(UNIQUE)
class Routes(Enum):
    USER = "/user"
