"""Data models related to liquidations."""

from typing import TypedDict, List, Union


# Liquidation and Position Data Models
class LiquidationData(TypedDict):
    """Represents liquidation data.

    Attributes:
        t: Timestamp (Unix seconds).
        longLiquidationUsd: Long liquidation amount (in USD).
        shortLiquidationUsd: Short liquidation amount (in USD).
    """

    t: int
    longLiquidationUsd: str
    shortLiquidationUsd: str


# Real-time Order Data Models (subset relevant to liquidation)
class LiquidationOrderData(TypedDict):
    """Represents a liquidation order.

    Attributes:
        exName: Exchange name.
        symbol: Currency symbol (e.g., "BTC").
        baseAsset: Base asset.
        price: Liquidation price.
        volUsd: Liquidation amount (USD).
        side: Direction of the liquidated position (1=Long liquidation, 2=Short liquidation).
        time: Timestamp (milliseconds).
    """

    exName: str
    symbol: str
    baseAsset: str
    price: float
    volUsd: float
    side: int
    time: int


# Liquidation History Related Data Models
class LiquidationHistoryData(TypedDict):
    """Represents liquidation history data.

    Note: API might return USD values as strings, conversion to float might be needed.

    Attributes:
        longLiquidationUsd: Liquidation amount for long positions (USD).
        shortLiquidationUsd: Liquidation amount for short positions (USD).
        t: Timestamp (Unix seconds).
    """

    longLiquidationUsd: float
    shortLiquidationUsd: float
    t: int


class LiquidationCoinData(TypedDict):
    """Represents liquidation data per coin.

    Attributes:
        symbol: Currency symbol (e.g., "BTC").
        liquidationUsd24h: Total liquidation amount in the last 24h (USD).
        longLiquidationUsd24h: Long liquidation amount in the last 24h (USD).
        shortLiquidationUsd24h: Short liquidation amount in the last 24h (USD).
        liquidationUsd12h: Total liquidation amount in the last 12h (USD).
        longLiquidationUsd12h: Long liquidation amount in the last 12h (USD).
        shortLiquidationUsd12h: Short liquidation amount in the last 12h (USD).
        liquidationUsd4h: Total liquidation amount in the last 4h (USD).
        longLiquidationUsd4h: Long liquidation amount in the last 4h (USD).
        shortLiquidationUsd4h: Short liquidation amount in the last 4h (USD).
        liquidationUsd1h: Total liquidation amount in the last 1h (USD).
        longLiquidationUsd1h: Long liquidation amount in the last 1h (USD).
        shortLiquidationUsd1h: Short liquidation amount in the last 1h (USD).
    """

    symbol: str
    liquidationUsd24h: float
    longLiquidationUsd24h: float
    shortLiquidationUsd24h: float
    liquidationUsd12h: float
    longLiquidationUsd12h: float
    shortLiquidationUsd12h: float
    liquidationUsd4h: float
    longLiquidationUsd4h: float
    shortLiquidationUsd4h: float
    liquidationUsd1h: float
    longLiquidationUsd1h: float
    shortLiquidationUsd1h: float


class LiquidationExchangeData(TypedDict):
    """Represents liquidation data per exchange.

    Attributes:
        exchange: Exchange name.
        liquidationUsd: Total liquidation amount (USD).
        longLiquidationUsd: Liquidation amount for long positions (USD).
        shortLiquidationUsd: Liquidation amount for short positions (USD).
    """

    exchange: str
    liquidationUsd: float
    longLiquidationUsd: float
    shortLiquidationUsd: float


# Heatmap Related Data Models (subset relevant to liquidation)
class LiquidationAggregatedHeatmapData(TypedDict):
    """Represents aggregated liquidation heatmap data.

    Attributes:
        y: List of Y-axis values for the heatmap (price levels).
        liq: 2D array of liquidation data.
        prices: 2D array of price data.
    """

    y: List[float]
    liq: List[List[Union[int, float]]]
    prices: List[List[Union[int, str]]]
