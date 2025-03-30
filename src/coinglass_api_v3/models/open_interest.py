"""Data models related to open interest and its historical data."""

from typing import TypedDict, List, Dict


class ExchangeOpenInterestData(TypedDict):
    """Represents exchange open interest data.

    Attributes:
        exchangeName: Name of the exchange.
        openInterest: Open interest in native units.
        openInterestUsd: Open interest converted to USD.
    """

    exchangeName: str
    openInterest: float
    openInterestUsd: float


class ExchangeHistoryChartData(TypedDict):
    """Data type for the response of the Exchange History Chart API (often used for OI/Funding).

    Attributes:
        timeList: List of timestamps (Unix seconds).
        priceList: List of price data.
        dataMap: Dictionary mapping exchange names to lists of values (e.g., OI, Funding Rate).
    """

    timeList: List[int]
    priceList: List[float]
    dataMap: Dict[str, List[float]]
