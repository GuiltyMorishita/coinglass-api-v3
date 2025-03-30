"""Data models related to trades and order execution."""

from typing import TypedDict, List


class TakerBuySellData(TypedDict):
    """Represents taker buy/sell data.

    Attributes:
        t: Timestamp (Unix seconds).
        buyVolume: Buy volume in USD.
        sellVolume: Sell volume in USD.
        buySellRatio: Buy/sell ratio.
    """

    t: int
    buyVolume: float
    sellVolume: float
    buySellRatio: float


class LongShortRatioData(TypedDict):
    """Represents long/short ratio data.

    Attributes:
        t: Timestamp (Unix seconds).
        longAccount: Long account ratio.
        shortAccount: Short account ratio.
        longShortRatio: Long/short ratio.
    """

    t: int
    longAccount: float
    shortAccount: float
    longShortRatio: float


class TakerBuySellVolumeData(TypedDict):
    """Represents taker buy/sell volume data.

    Attributes:
        t: Timestamp (Unix seconds).
        buyVolume: Buy volume in USD.
        sellVolume: Sell volume in USD.
        buySellRatio: Buy/sell ratio.
    """

    t: int
    buyVolume: float
    sellVolume: float
    buySellRatio: float


class AggregatedTakerBuySellRatioData(TypedDict):
    """Represents aggregated taker buy/sell ratio data.

    Attributes:
        t: Timestamp (Unix seconds).
        buyVolume: Buy volume in USD.
        sellVolume: Sell volume in USD.
        buySellRatio: Buy/sell ratio.
    """

    t: int
    buyVolume: float
    sellVolume: float
    buySellRatio: float


class AggregatedTakerBuySellVolumeData(TypedDict):
    """Represents aggregated taker buy/sell volume data.

    Attributes:
        t: Timestamp (Unix seconds).
        buyVolume: Buy volume in USD.
        sellVolume: Sell volume in USD.
        buySellRatio: Buy/sell ratio.
    """

    t: int
    buyVolume: float
    sellVolume: float
    buySellRatio: float


class ExchangeTakerBuySellRatioData(TypedDict):
    """Represents exchange-specific taker buy/sell ratio data.

    Attributes:
        symbol: Currency symbol (e.g., "BTC").
        h1BuySellRatio: List of buy/sell ratio data for h1 interval.
        h4BuySellRatio: List of buy/sell ratio data for h4 interval.
        h12BuySellRatio: List of buy/sell ratio data for h12 interval.
        h24BuySellRatio: List of buy/sell ratio data for h24 interval.
    """

    symbol: str
    h1BuySellRatio: List[TakerBuySellVolumeData]
    h4BuySellRatio: List[TakerBuySellVolumeData]
    h12BuySellRatio: List[TakerBuySellVolumeData]
    h24BuySellRatio: List[TakerBuySellVolumeData]
