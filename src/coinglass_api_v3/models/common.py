"""Common data models used across different categories."""

from typing import TypedDict


class ExchangePair(TypedDict):
    """Represents exchange trading pair data.

    Attributes:
        instrumentId: Exchange-specific trading pair ID.
        baseAsset: Base asset symbol (e.g., BTC).
        quoteAsset: Quote asset symbol (e.g., USDT).
    """

    instrumentId: str
    baseAsset: str
    quoteAsset: str
