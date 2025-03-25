from enum import Enum, auto

class GameMode(Enum):
    SHAREWARE = auto()
    REGISTERED = auto()
    COMMERCIAL = auto()
    RETAIL = auto()
    INDETERMINED = auto()
