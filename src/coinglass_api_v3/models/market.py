"""Data models related to market price, volume, and performance."""

from typing import TypedDict, Optional, List


# Market Data Models
class OHLCData(TypedDict):
    """Represents OHLC (Open, High, Low, Close) and volume data.

    Attributes:
        t: Timestamp (Unix seconds).
        o: Open price.
        h: High price.
        l: Low price.
        c: Close price.
        v: Volume (in USD).
    """

    t: int
    o: float
    h: float
    l: float
    c: float
    v: float


# --- Base class for interval performance data ---
class _BaseIntervalPerformanceData(TypedDict, total=False):
    """Base class for market performance data across standard intervals.

    Intended for internal use via inheritance. Fields represent metrics over
    1h, 4h, 12h, 24h, and 1w intervals.
    """

    # 1-hour interval data
    priceChange1h: float
    priceChangePercent1h: float
    volUsd1h: float
    buyVolUsd1h: float
    sellVolUsd1h: float
    volUsdChange1h: float
    volUsdChangePercent1h: float
    flowsUsd1h: float

    # 4-hour interval data
    priceChange4h: float
    priceChangePercent4h: float
    volUsd4h: float
    buyVolUsd4h: float
    sellVolUsd4h: float
    volUsdChange4h: float
    volUsdChangePercent4h: float
    flowsUsd4h: float

    # 12-hour interval data
    priceChange12h: float
    priceChangePercent12h: float
    volUsd12h: float
    buyVolUsd12h: float
    sellVolUsd12h: float
    volUsdChange12h: float
    volUsdChangePercent12h: float
    flowsUsd12h: float

    # 24-hour interval data
    priceChange24h: float
    priceChangePercent24h: float
    volUsd24h: float
    buyVolUsd24h: float
    sellVolUsd24h: float
    volUsdChange24h: float
    volUsdChangePercent24h: float
    flowsUsd24h: float

    # 1-week interval data
    priceChange1w: float
    priceChangePercent1w: float
    volUsd1w: float
    buyVolUsd1w: float
    sellVolUsd1w: float
    volUsdChange1w: float
    volUsdChangePercent1w: float
    flowsUsd1w: float


# Coins Markets
class CoinMarketData(_BaseIntervalPerformanceData):
    """Represents market performance data per coin.

    Inherits common interval performance fields from _BaseIntervalPerformanceData.

    Attributes:
        symbol: Coin symbol.
        price: Current price.
        marketCap: Market capitalization.
        # Shorter interval data (5m, 15m, 30m)
        priceChange5m: Price change in the last 5 minutes.
        priceChangePercent5m: Percentage price change in the last 5 minutes.
        volUsd5m: Volume in USD over the last 5 minutes.
        buyVolUsd5m: Buy volume in USD over the last 5 minutes.
        sellVolUsd5m: Sell volume in USD over the last 5 minutes.
        flowsUsd5m: Net flow in USD over the last 5 minutes.
        volUsdChange5m: Change in USD volume over the last 5 minutes.
        volUsdChangePercent5m: Percentage change in USD volume over the last 5 minutes.
        priceChange15m: Price change in the last 15 minutes.
        priceChangePercent15m: Percentage price change in the last 15 minutes.
        volUsd15m: Volume in USD over the last 15 minutes.
        buyVolUsd15m: Buy volume in USD over the last 15 minutes.
        sellVolUsd15m: Sell volume in USD over the last 15 minutes.
        flowsUsd15m: Net flow in USD over the last 15 minutes.
        volUsdChange15m: Change in USD volume over the last 15 minutes.
        volUsdChangePercent15m: Percentage change in USD volume over the last 15 minutes.
        priceChange30m: Price change in the last 30 minutes.
        priceChangePercent30m: Percentage price change in the last 30 minutes.
        volUsd30m: Volume in USD over the last 30 minutes.
        buyVolUsd30m: Buy volume in USD over the last 30 minutes.
        sellVolUsd30m: Sell volume in USD over the last 30 minutes.
        flowsUsd30m: Net flow in USD over the last 30 minutes.
        volUsdChange30m: Change in USD volume over the last 30 minutes.
        volUsdChangePercent30m: Percentage change in USD volume over the last 30 minutes.
        # Inherited fields for 1h, 4h, 12h, 24h, 1w intervals
    """

    # Specific fields for CoinMarketData
    symbol: str
    price: float
    marketCap: float

    # 5-minute interval data
    priceChange5m: float
    priceChangePercent5m: float
    volUsd5m: float
    buyVolUsd5m: float
    sellVolUsd5m: float
    flowsUsd5m: float
    volUsdChange5m: float
    volUsdChangePercent5m: float

    # 15-minute interval data
    priceChange15m: float
    priceChangePercent15m: float
    volUsd15m: float
    buyVolUsd15m: float
    sellVolUsd15m: float
    flowsUsd15m: float
    volUsdChange15m: float
    volUsdChangePercent15m: float

    # 30-minute interval data
    priceChange30m: float
    priceChangePercent30m: float
    volUsd30m: float
    buyVolUsd30m: float
    sellVolUsd30m: float
    flowsUsd30m: float
    volUsdChange30m: float
    volUsdChangePercent30m: float


# Pairs Markets
class PairMarketData(TypedDict):
    """Represents market performance data per trading pair.

    Attributes:
        instrumentId: Instrument ID.
        exName: Exchange name.
        symbol: Symbol.
        longVolUsd: Long volume in USD.
        shortVolUsd: Short volume in USD.
        longNumber: Number of long positions/accounts.
        shortNumber: Number of short positions/accounts.
        volUsd: Total volume in USD.
        volUsdChangePercent24h: Percentage change in USD volume over 24h.
        price: Current price.
        indexPrice: Index price.
        priceChangePercent24h: Percentage price change over 24h.
        openInterestAmount: Open interest amount (native units).
        openInterest: Open interest value (USD).
        oiChangePercent24h: Percentage change in open interest over 24h.
        longLiquidationUsd24h: Long liquidation amount in USD over 24h.
        shortLiquidationUsd24h: Short liquidation amount in USD over 24h.
        fundingRate: Current funding rate (for perpetual contracts).
        nextFundingTime: Next funding time (milliseconds, for perpetual contracts).
        oiVolRadio: Open interest / Volume ratio (Name might be misspelled in API).
        oiVolRadioChangePercent24h: Percentage change in OI/Volume ratio over 24h (Name might be misspelled in API).
        expiryDate: Expiry date timestamp (milliseconds, for futures contracts).
        predictedRate: Predicted funding rate (Not in API example, from documentation).
    """

    instrumentId: str
    exName: str
    symbol: str
    longVolUsd: float
    shortVolUsd: float
    longNumber: int
    shortNumber: int
    volUsd: float
    volUsdChangePercent24h: float
    price: float
    indexPrice: float
    priceChangePercent24h: float
    openInterestAmount: float
    openInterest: float
    oiChangePercent24h: float
    longLiquidationUsd24h: float
    shortLiquidationUsd24h: float
    fundingRate: Optional[float]
    nextFundingTime: Optional[int]
    oiVolRadio: float
    oiVolRadioChangePercent24h: float
    expiryDate: Optional[int]
    predictedRate: Optional[float]


# Spot Market Data (Refactored)
class SpotPairMarketData(_BaseIntervalPerformanceData):
    """Represents performance-related information for a spot trading pair.

    Inherits common interval performance fields from _BaseIntervalPerformanceData.

    Attributes:
        symbol: Trading pair symbol (e.g., "BTC/USDT").
        exName: Exchange name (e.g., "Binance").
        price: Current price.
        # Inherited fields for 1h, 4h, 12h, 24h, 1w intervals
    """

    # Specific fields for SpotPairMarketData
    symbol: str
    exName: str
    price: float


# Perpetual Market Data (Refactored)
class PerpetualMarketData(_BaseIntervalPerformanceData):
    """Represents perpetual market data.

    Inherits common interval performance fields from _BaseIntervalPerformanceData.

    Attributes:
        symbol: Trading pair symbol (e.g., "BTC/USDT").
        exName: Exchange name (e.g., "Binance").
        price: Current price.
        # Inherited fields for 1h, 4h, 12h, 24h, 1w intervals
    """

    # Specific fields for PerpetualMarketData
    symbol: str
    exName: str
    price: float
