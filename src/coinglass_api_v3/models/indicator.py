"""Data models related to technical indicators and market sentiment."""

from typing import TypedDict, List, Optional, Dict


class CoinPriceChangeData(TypedDict):
    """Represents price change data per coin over various timeframes.

    Attributes:
        symbol: Coin symbol.
        price: Current price.
        priceChangePercent5m: Percentage price change in the last 5 minutes.
        priceChangePercent15m: Percentage price change in the last 15 minutes.
        priceChangePercent30m: Percentage price change in the last 30 minutes.
        priceChangePercent1h: Percentage price change in the last 1 hour.
        priceChangePercent4h: Percentage price change in the last 4 hours.
        priceChangePercent12h: Percentage price change in the last 12 hours.
        priceChangePercent24h: Percentage price change in the last 24 hours.
        priceAmplitudePercent5m: Percentage price amplitude in the last 5 minutes.
        priceAmplitudePercent15m: Percentage price amplitude in the last 15 minutes.
        priceAmplitudePercent30m: Percentage price amplitude in the last 30 minutes.
        priceAmplitudePercent1h: Percentage price amplitude in the last 1 hour.
        priceAmplitudePercent4h: Percentage price amplitude in the last 4 hours.
        priceAmplitudePercent12h: Percentage price amplitude in the last 12 hours.
        priceAmplitudePercent24h: Percentage price amplitude in the last 24 hours.
    """

    symbol: str
    price: float
    priceChangePercent5m: Optional[float]
    priceChangePercent15m: Optional[float]
    priceChangePercent30m: Optional[float]
    priceChangePercent1h: Optional[float]
    priceChangePercent4h: Optional[float]
    priceChangePercent12h: Optional[float]
    priceChangePercent24h: Optional[float]
    priceAmplitudePercent5m: Optional[float]
    priceAmplitudePercent15m: Optional[float]
    priceAmplitudePercent30m: Optional[float]
    priceAmplitudePercent1h: Optional[float]
    priceAmplitudePercent4h: Optional[float]
    priceAmplitudePercent12h: Optional[float]
    priceAmplitudePercent24h: Optional[float]


class RsiData(TypedDict):
    """Represents RSI (Relative Strength Index) data across multiple timeframes.

    Attributes:
        symbol: Coin symbol.
        rsi4h: RSI value for the 4-hour timeframe.
        priceChangePercent4h: Percentage price change in the last 4 hours.
        rsi24h: RSI value for the 24-hour timeframe.
        priceChangePercent24h: Percentage price change in the last 24 hours.
        rsi1w: RSI value for the 1-week timeframe.
        priceChangePercent1w: Percentage price change in the last 1 week.
        rsi1h: RSI value for the 1-hour timeframe.
        priceChangePercent1h: Percentage price change in the last 1 hour.
        rsi15m: RSI value for the 15-minute timeframe.
        priceChangePercent15m: Percentage price change in the last 15 minutes.
        price: Current price.
        rsi12h: RSI value for the 12-hour timeframe.
        priceChangePercent12h: Percentage price change in the last 12 hours.
    """

    symbol: str
    rsi4h: float
    priceChangePercent4h: float
    rsi24h: float
    priceChangePercent24h: float
    rsi1w: float
    priceChangePercent1w: float
    rsi1h: float
    priceChangePercent1h: float
    rsi15m: float
    priceChangePercent15m: float
    price: float
    rsi12h: float
    priceChangePercent12h: float


class CoinbasePremiumIndexData(TypedDict):
    """Represents the Coinbase Bitcoin Premium Index data point.

    Attributes:
        time: Timestamp in seconds.
        premium: Price difference in USD between Coinbase and Binance.
        premiumRate: Percentage difference (Premium / Binance price).
    """

    time: int
    premium: float
    premiumRate: float


class BitfinexMarginLongShortData(TypedDict):
    """Represents data on margin long and short positions from Bitfinex.

    Attributes:
        time: Timestamp in seconds.
        longQty: Long quantity for the symbol.
        shortQty: Short quantity for the symbol.
    """

    time: int
    longQty: float
    shortQty: float


class BullMarketPeakIndicatorData(TypedDict):
    """Represents data for a single bull market peak indicator.

    Attributes:
        name: The name of the indicator.
        value: The current value of the indicator (as a string).
        targetValue: The target value associated with a market peak (as a string).
        prevValue: The previous value of the indicator (optional, as a string).
        change: The change from the previous value (optional, as a string).
        type: The comparison type used for hitting the target (e.g., '>=', '<=') (optional).
        hit: Whether the indicator has hit its target value (optional).
    """

    name: str
    value: str
    targetValue: str
    prevValue: Optional[str]
    change: Optional[str]
    type: Optional[str]
    hit: Optional[bool]


class BitcoinBubbleIndexData(TypedDict):
    """Represents data for the Bitcoin Bubble Index.

    Attributes:
        price: Bitcoin price.
        index: Bitcoin bubble index value.
        googleTrend: Bitcoin Google Trends value.
        difficulty: Bitcoin difficulty.
        transcations: Number of Bitcoin transactions (API typo).
        sentByAddress: Number of Bitcoin sent by address.
        tweets: Number of Bitcoin tweets.
        date: Date string (e.g., "2010-07-17").
    """

    price: float
    index: float
    googleTrend: float
    difficulty: float
    transcations: int
    sentByAddress: int
    tweets: int
    date: str


class AHR999Data(TypedDict):
    """Represents data for the AHR999 Index.

    Attributes:
        date: Date string (e.g., "2011/02/01").
        avg: 200-day cost average.
        ahr999: AHR999 index value.
        value: Bitcoin price value (as string).
    """

    date: str
    avg: float
    ahr999: float
    value: str


class TwoYearMAMultiplierData(TypedDict):
    """Represents data for the Two Year MA Multiplier indicator.

    Attributes:
        buyQty: Buy quantity (potentially unused, often 0).
        createTime: Timestamp in milliseconds.
        price: Bitcoin price.
        mA730Mu5: 2-year moving average multiplied by 5.
        mA730: 2-year moving average.
        sellQty: Sell quantity (potentially unused, often 0).
    """

    buyQty: int
    createTime: int
    price: float
    mA730Mu5: float
    mA730: float
    sellQty: int


class MovingAvgHeatmapData(TypedDict):
    """Represents data for the 200-Week Moving Average Heatmap.

    Attributes:
        buyQty: Buy quantity (potentially unused, often 0).
        createTime: Timestamp in milliseconds.
        price: Bitcoin price.
        mA1440: 200-week moving average heatmap value.
        mA1440IP: Integer value related to the heatmap (optional, purpose unclear).
        sellQty: Sell quantity (potentially unused, often 0).
    """

    buyQty: int
    createTime: int
    price: float
    mA1440: float
    mA1440IP: Optional[float]
    sellQty: int


class PuellMultipleData(TypedDict):
    """Represents data for the Puell Multiple indicator.

    Attributes:
        buyQty: Buy quantity (potentially unused, often 0).
        createTime: Timestamp in milliseconds.
        price: Bitcoin price.
        puellMultiple: Puell Multiple value.
        sellQty: Sell quantity (potentially unused, often 0).
    """

    buyQty: int
    createTime: int
    price: float
    puellMultiple: float
    sellQty: int


class StockFlowData(TypedDict):
    """Represents data for the Stock-to-Flow Model.

    Attributes:
        createTime: Timestamp string (e.g., "2010-08-17T00:00:00").
        price: Bitcoin price.
        nextHalving: Days until the next halving.
    """

    createTime: str
    price: float
    nextHalving: int


class PiCycleTopIndicatorData(TypedDict):
    """Represents data for the Pi Cycle Top Indicator.

    Attributes:
        ma110: 110-day moving average (as string).
        createTime: Timestamp in milliseconds.
        ma350Mu2: 350-day moving average multiplied by 2 (as string).
        price: Bitcoin price.
    """

    ma110: str
    createTime: int
    ma350Mu2: str
    price: float


class GoldenRatioMultiplierData(TypedDict):
    """Represents data for the Golden Ratio Multiplier.

    Note: Keys with special characters ('.') or starting with numbers
          are mapped to valid Python identifiers.

    Attributes:
        x8: Multiplier value (x8).
        LowBullHigh2: Upper bull high band 2 (mapped from '2LowBullHigh').
        createTime: Timestamp in milliseconds.
        price: Bitcoin price.
        ma350: 350-day moving average.
        AccumulationHigh1_6: Accumulation high band 1.6 (mapped from '1.6AccumulationHigh').
        x21: Multiplier value (x21).
        x13: Multiplier value (x13).
        x3: Multiplier value (x3).
        x5: Multiplier value (x5).
    """

    x8: float
    LowBullHigh2: float
    createTime: int
    price: float
    ma350: float
    AccumulationHigh1_6: float
    x21: float
    x13: float
    x3: float
    x5: float


class BitcoinProfitableDaysData(TypedDict):
    """Represents data for Bitcoin Profitable Days.

    Attributes:
        side: 1 for profit, -1 for loss.
        createTime: Timestamp in milliseconds.
        price: Bitcoin price.
    """

    side: int
    createTime: int
    price: float


class BitcoinRainbowChartDataPoint(TypedDict):
    """Represents a single data point from the Bitcoin Rainbow Chart.

    The data is returned as a list, mapped to these fields by index (0-11).

    Attributes:
        price: Bitcoin price (index 0).
        model_price: Model price (index 1).
        fire_sale: 'Fire sale' band price (index 2).
        buy: 'Buy' band price (index 3).
        accumulate: 'Accumulate' band price (index 4).
        still_cheap: 'Still cheap' band price (index 5).
        hold: 'Hold' band price (index 6).
        is_bubble: 'Is this a bubble?' band price (index 7).
        fomo: 'FOMO intensifies' band price (index 8).
        sell: 'Sell. Seriously, sell' band price (index 9).
        max_bubble: 'Maximum bubble territory' band price (index 10).
        t: Timestamp in milliseconds (index 11).
    """

    price: Optional[float]  # 0
    model_price: Optional[float]  # 1
    fire_sale: Optional[float]  # 2
    buy: Optional[float]  # 3
    accumulate: Optional[float]  # 4
    still_cheap: Optional[float]  # 5
    hold: Optional[float]  # 6
    is_bubble: Optional[float]  # 7
    fomo: Optional[float]  # 8
    sell: Optional[float]  # 9
    max_bubble: Optional[float]  # 10
    t: int  # 11


class FearGreedHistoryData(TypedDict):
    """Represents Crypto Fear & Greed Index historical data.

    Attributes:
        t: Timestamp in milliseconds.
        value: Index value.
        price: Bitcoin price at the time of the index reading.
    """

    t: int
    value: float
    price: float


class GrayscaleHoldingData(TypedDict):
    """Represents data for a single Grayscale holding.

    Attributes:
        symbol: The asset symbol (e.g., "ETH").
        primaryMarketPrice: Price in the primary market.
        secondaryMarketPrice: Price in the secondary market.
        premiumRate: Premium or discount rate.
        holdingsAmount: Amount of the asset held.
        holdingsUsd: USD value of the holdings.
        holdingsAmountChange30d: Change in holdings amount over 30 days.
        holdingsAmountChange7d: Change in holdings amount over 7 days.
        holdingsAmountChange1d: Change in holdings amount over 1 day.
        closeTime: Closing timestamp in milliseconds.
        updateTime: Last update timestamp in milliseconds.
    """

    symbol: str
    primaryMarketPrice: float
    secondaryMarketPrice: float
    premiumRate: float
    holdingsAmount: float
    holdingsUsd: float
    holdingsAmountChange30d: float
    holdingsAmountChange7d: float
    holdingsAmountChange1d: float
    closeTime: int
    updateTime: int


class GrayscalePremiumHistoryData(TypedDict):
    """Represents Grayscale premium history data for a single timestamp.

    Corresponds to data points derived from the /api/grayscale/premium-history endpoint.

    Attributes:
        t: Timestamp in milliseconds.
        secondaryMarketPrice: Price in the secondary market (Optional).
        premiumRate: Premium or discount rate (Optional).
    """

    t: int
    secondaryMarketPrice: Optional[float]
    premiumRate: Optional[float]


class BorrowInterestRateData(TypedDict):
    """Represents borrow interest rate data.

    Attributes:
        time: Timestamp (Unix seconds).
        interestRate: Interest rate value.
    """

    time: int
    interestRate: float


class ExchangeBalanceListData(TypedDict):
    """Represents exchange balance list data.

    Attributes:
        exchangeName: Exchange name.
        balance: Balance amount.
        change1d: Change in balance over 1 day.
        changePercent1d: Percentage change in balance over 1 day.
        change7d: Change in balance over 7 days.
        changePercent7d: Percentage change in balance over 7 days.
        change30d: Change in balance over 30 days.
        changePercent30d: Percentage change in balance over 30 days.
    """

    exchangeName: str
    balance: float
    change1d: float
    changePercent1d: float
    change7d: float
    changePercent7d: float
    change30d: float
    changePercent30d: float


class ExchangeBalanceChartData(TypedDict):
    """Represents exchange balance chart data.

    Attributes:
        timeList: List of timestamps in milliseconds.
        dataMap: Dictionary mapping exchange names to lists of their
                 balance amounts at corresponding timestamps.
                 Balances can be float or None.
        priceList: List of prices at corresponding timestamps.
    """

    timeList: List[int]
    dataMap: Dict[str, List[Optional[float]]]
    priceList: List[Optional[float]]
