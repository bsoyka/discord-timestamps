from arrow import Arrow

from discord_timestamps import format_timestamp


def test_timestamp_from_int():
    assert format_timestamp(1609459200) == "<t:1609459200>"


def test_timestamp_from_float():
    assert format_timestamp(1609459200.567) == "<t:1609459200>"


def test_timestamp_from_arrow():
    assert format_timestamp(Arrow(2021, 1, 1)) == "<t:1609459200>"
