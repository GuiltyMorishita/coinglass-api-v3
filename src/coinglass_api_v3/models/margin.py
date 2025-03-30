"""Data models related to margin trading."""

from typing import TypedDict


class BitfinexMarginLongShortData(TypedDict):
    """Represents long/short position data for margin trading on Bitfinex.

    This TypedDict class represents long/short position data for margin trading
    obtained from the Bitfinex exchange.

    Attributes:
        time: Unix timestamp in seconds
        longQty: Quantity of long positions
        shortQty: Quantity of short positions
    """

    time: int
    longQty: float
    shortQty: float
