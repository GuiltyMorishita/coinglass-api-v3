"""Data models related to the options market."""

from typing import TypedDict, List, Dict, Optional


# Option Max Pain Data
class OptionMaxPainData(TypedDict):
    """Represents Max Pain data for options.

    Attributes:
        callOi: Call open interest.
        maxPain: Max pain strike price (as string, check API).
        callOiByNotional: Notional value of call options.
        putOi: Put open interest.
        time: Option expiration identifier (e.g., "250312").
        putOiByMarket: Market value of put options.
        putOiByNotional: Notional value of put options.
        callOiByMarket: Market value of call options.
    """

    callOi: float
    maxPain: str
    callOiByNotional: float
    putOi: float
    time: str
    putOiByMarket: float
    putOiByNotional: float
    callOiByMarket: float


# Option Info Data
class OptionInfoData(TypedDict):
    """Represents general information about options on an exchange.

    Attributes:
        exchangeName: Name of the exchange (e.g., "Binance", "All").
        openInterest: Total open interest in base currency.
        rate: Percentage of total open interest.
        h24Change: 24-hour change percentage in open interest.
        exchangeLogo: URL of the exchange logo.
        openInterestUsd: Total open interest in USD.
        volUsd: 24-hour volume in USD.
        h24VolChangePercent: 24-hour change percentage in volume.
    """

    exchangeName: str
    openInterest: float
    rate: float
    h24Change: float
    exchangeLogo: str
    openInterestUsd: float
    volUsd: float
    h24VolChangePercent: float


# Option Exchange OI/Volume History Data
class OptionExchangeOIVolHistoryData(TypedDict):
    """Represents historical OI or Volume data across exchanges for options.

    Attributes:
        dateList: List of timestamps in milliseconds.
        priceList: List of corresponding prices.
        dataMap: Dictionary mapping exchange names to lists of OI/Volume values.
    """

    dateList: List[int]
    priceList: List[Optional[float]]
    dataMap: Dict[str, List[Optional[float]]]
