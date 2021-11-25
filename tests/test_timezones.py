from arrow import Arrow

from discord_timestamps import format_timestamp


def test_timestamp_from_local_arrow():
    assert (
        format_timestamp(Arrow(2021, 1, 1, 1, tzinfo="UTC+1"))
        == "<t:1609459200>"
    )
