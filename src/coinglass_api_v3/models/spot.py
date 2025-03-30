"""Data models specific to spot markets."""

from typing import TypedDict


class SpotTakerBuySellData(TypedDict):
    """Represents spot market taker buy/sell data.

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


class SpotOrderbookHistoryData(TypedDict):
    """Represents spot market order book history data.

    Attributes:
        bidsUsd: Total value of bids in USD.
        bidsAmount: Total amount of bids.
        asksUsd: Total value of asks in USD.
        asksAmount: Total amount of asks.
        time: Timestamp (Unix seconds).
    """

    bidsUsd: float
    bidsAmount: float
    asksUsd: float
    asksAmount: float
    time: int


class SpotPairMarketData(TypedDict):
    """Represents spot market data for a trading pair.

    Attributes:
        instrumentId: Instrument ID.
        exName: Exchange name.
        symbol: Trading pair symbol.
        price: Current price.
        volUsd: Trading volume in USD.
        volUsdChangePercent24h: 24h volume change percentage.
        priceChangePercent24h: 24h price change percentage.
    """

    instrumentId: str
    exName: str
    symbol: str
    price: float
    volUsd: float
    volUsdChangePercent24h: float
    priceChangePercent24h: float


class CoinbasePremiumIndexData(TypedDict):
    """Represents Coinbase premium index data.

    Attributes:
        t: Timestamp (Unix seconds).
        price: Price on Coinbase.
        indexPrice: Index price.
        premium: Premium value (price - indexPrice).
        premiumRate: Premium rate as a percentage.
    """

    t: int
    price: float
    indexPrice: float
    premium: float
    premiumRate: float
