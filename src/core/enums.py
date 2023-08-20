from enum import IntEnum


class Limits(IntEnum):
    MAX_LENGTH_EMAIL = 50
    MAX_LENGTH_PASSWORD = 50
    MAX_SIZE_FILE = 10


limits = Limits
