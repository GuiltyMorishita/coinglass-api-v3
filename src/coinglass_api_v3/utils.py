"""Coinglass utility functions.
=======================

This module provides utility functions used by the Coinglass API client.
"""

from typing import Dict, List, Any
from datetime import datetime


def timestamp_to_datetime(timestamp: int) -> datetime:
    """Converts a Unix timestamp (seconds) to a datetime object.

    Args:
        timestamp: Unix timestamp in seconds.

    Returns:
        The corresponding datetime object.
    """
    return datetime.fromtimestamp(timestamp)


def parse_ohlc_data(data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Parses OHLC data, converting the timestamp to datetime.

    Args:
        data: OHLC data list from the API.

    Returns:
        The OHLC data list with timestamps converted to datetime objects
        under the key 'datetime'.
    """
    for item in data:
        if "t" in item:
            item["datetime"] = timestamp_to_datetime(item["t"])
    return data


def format_interval(interval: str) -> str:
    """Normalizes the time interval string.

    Args:
        interval: The time interval (e.g., "5m", "1h", "1d", "1w").

    Returns:
        The normalized interval string.

    Raises:
        ValueError: If the provided interval is not valid.
    """
    # Based on intervals mentioned in client docstrings (e.g., future_client)
    valid_intervals = [
        "1m",
        "3m",
        "5m",
        "15m",
        "30m",
        "1h",
        "4h",
        "6h",
        "8h",
        "12h",
        "1d",
        "1w",
        "7d",
        "30d",
    ]
    interval = interval.lower()

    if interval not in valid_intervals:
        raise ValueError(
            f"Invalid interval '{interval}'. Valid intervals: {', '.join(valid_intervals)}"
        )

    return interval
