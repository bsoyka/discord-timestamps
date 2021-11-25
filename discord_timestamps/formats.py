"""Formats for discord-timestamps generation"""

from enum import Enum


class TimestampType(Enum):
    """Timestamp types supported by Discord"""

    SHORT_TIME = ":t"
    LONG_TIME = ":T"

    SHORT_DATE = ":d"
    LONG_DATE = ":D"

    SHORT_DATETIME = ""
    LONG_DATETIME = ":F"

    RELATIVE = ":R"
