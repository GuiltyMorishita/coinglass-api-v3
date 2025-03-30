"""Data models related to order books and large limit orders."""

from typing import TypedDict, List


class OrderbookHistoryData(TypedDict):
    """Represents historical order book data (Bid/Ask range).

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


class LargeLimitOrderData(TypedDict):
    """Represents a large limit order (current or historical).

    Attributes:
        exName: Exchange name.
        symbol: Trading pair.
        baseAsset: Base asset.
        quoteAsset: Quote asset.
        price: Price.
        startTime: Start timestamp (milliseconds).
        startAmount: Initial order size.
        startUsd: Initial order value in USD.
        currentAmount: Current order amount.
        currentUsd: Current order value in USD.
        currentTime: Current timestamp (milliseconds).
        vol: Trading volume associated with the order.
        volUsd: Trading volume in USD associated with the order.
        count: Number of trades associated with the order.
        side: Trade direction (1-Buy, 2-Sell).
        state: Order status (1-In Progress, 2-Completed, 3-Revoked for history).
        endTime: End timestamp (milliseconds).
    """

    exName: str
    symbol: str
    baseAsset: str
    quoteAsset: str
    price: float
    startTime: int
    startAmount: float
    startUsd: float
    currentAmount: float
    currentUsd: float
    currentTime: int
    vol: float
    volUsd: float
    count: int
    side: int
    state: int
    endTime: int


class FuturesTradeOrderData(TypedDict):
    """Represents a futures trade order.

    Attributes:
        exName: Exchange name.
        symbol: Trading pair symbol.
        baseAsset: Base asset symbol.
        price: Trade price.
        volUsd: Trade volume in USD.
        side: Trade direction (1=Buy, 2=Sell).
        time: Timestamp (milliseconds).
    """

    exName: str
    symbol: str
    baseAsset: str
    price: float
    volUsd: float
    side: int
    time: int
