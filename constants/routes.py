from enum import Enum

class Routes(str, Enum):
    USER = "/user"

    def __str__(self) -> str:
        return self.value