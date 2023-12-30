"""Generation of properly-formatted dynamic timestamps for Discord messages"""

from typing import Union

from arrow import Arrow

from .formats import TimestampType

__version__ = "1.0.2"


def format_timestamp(
    timestamp: Union[int, float, Arrow],
    timestamp_type: TimestampType = TimestampType.SHORT_DATETIME,
) -> str:
    """Generate a properly-formatted timestamp for Discord messages

    Args:
        timestamp: The timestamp to format
        timestamp_type (TimestampType): The type of timestamp to format

    Returns:
        str: The formatted timestamp
    """

    if isinstance(timestamp, int):
        # The timestamp is already an int, leave it as-is
        int_timestamp = timestamp

    elif isinstance(timestamp, float):
        # The timestamp is a float, convert it to an int
        int_timestamp = int(timestamp)

    elif isinstance(timestamp, Arrow):
        # The timestamp is an Arrow object, convert it to an int in UTC
        timestamp = timestamp.to("UTC")
        int_timestamp = timestamp.int_timestamp

    # Combine the timestamp and the format
    return f"<t:{int_timestamp}{timestamp_type.value}>"
