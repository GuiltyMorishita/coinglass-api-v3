"""Data models specific to Hyperliquid exchange."""

from typing import TypedDict


class HyperliquidWhalePositionData(TypedDict):
    """Represents a whale position on Hyperliquid.

    Attributes:
        address: Wallet address of the whale.
        symbol: Trading pair symbol.
        position: Position size.
        notionalValue: Position value in USD.
        side: Position direction (1=Long, 2=Short).
        leverage: Leverage used.
        time: Timestamp (milliseconds).
    """

    address: str
    symbol: str
    position: float
    notionalValue: float
    side: int
    leverage: float
    time: int


class HyperliquidWhaleAlertData(TypedDict):
    """Represents a whale alert from Hyperliquid.

    Attributes:
        address: Wallet address of the whale.
        symbol: Trading pair symbol.
        position: Position size.
        notionalValue: Position value in USD.
        side: Position direction (1=Long, 2=Short).
        leverage: Leverage used.
        time: Timestamp (milliseconds).
        type: Alert type (e.g., "New Position", "Position Change").
        changeAmount: Change in position size.
        changeNotionalValue: Change in position value in USD.
    """

    address: str
    symbol: str
    position: float
    notionalValue: float
    side: int
    leverage: float
    time: int
    type: str
    changeAmount: float
    changeNotionalValue: float
