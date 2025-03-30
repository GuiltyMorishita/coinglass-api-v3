"""Data models related to funding rates and funding rate arbitrage."""

from typing import TypedDict, List


class ExchangeFundingRateData(TypedDict):
    """Represents exchange funding rate data.

    Attributes:
        exchangeName: Name of the exchange.
        fundingRate: Current funding rate.
        nextFundingRate: Predicted next funding rate.
        nextFundingTime: Next funding time (Unix seconds).
    """

    exchangeName: str
    fundingRate: float
    nextFundingRate: float
    nextFundingTime: int


class CumulativeFundingRateData(TypedDict):
    """Represents cumulative funding rate data.

    Attributes:
        exchangeName: Name of the exchange.
        cumulativeFundingRate: Cumulative funding rate for the specified period.
    """

    exchangeName: str
    cumulativeFundingRate: float


class FundingRateArbitrageData(TypedDict):
    """Represents funding rate arbitrage data.

    Attributes:
        longExchange: Name of the exchange for the long position.
        shortExchange: Name of the exchange for the short position.
        longFundingRate: Funding rate of the long position exchange.
        shortFundingRate: Funding rate of the short position exchange.
        spread: Difference in funding rates between the two exchanges (arbitrage opportunity size).
    """

    longExchange: str
    shortExchange: str
    longFundingRate: float
    shortFundingRate: float
    spread: float


class SymbolFundingRateData(TypedDict):
    """Represents funding rate data per symbol.

    Attributes:
        symbol: Currency symbol (e.g., "BTC").
        usdtOrUsdMarginList: List of funding rate data for exchanges using USDT or USD as margin.
        tokenMarginList: List of funding rate data for exchanges using the token itself as margin.
    """

    symbol: str
    usdtOrUsdMarginList: List[ExchangeFundingRateData]
    tokenMarginList: List[ExchangeFundingRateData]


class ExchangeCumulativeFundingRateData(TypedDict):
    """Represents cumulative funding rate data per exchange.

    Attributes:
        exchange: Exchange name.
        fundingRate: Cumulative funding rate value.
    """

    exchange: str
    fundingRate: float


class SymbolCumulativeFundingRateData(TypedDict):
    """Represents cumulative funding rate data per symbol.

    Attributes:
        symbol: Currency symbol (e.g., "BTC").
        usdtOrUsdMarginList: List of cumulative funding rate data for USDT/USD margined exchanges.
        tokenMarginList: List of cumulative funding rate data for token margined exchanges.
    """

    symbol: str
    usdtOrUsdMarginList: List[ExchangeCumulativeFundingRateData]
    tokenMarginList: List[ExchangeCumulativeFundingRateData]


class ArbitrageLegData(TypedDict):
    """Represents the buy/sell leg of an arbitrage opportunity.

    Attributes:
        exName: Exchange name.
        fundingRate: Current funding rate.
        nextFundingTime: Next funding time (Unix seconds).
        takerFee: Taker fee rate.
        makerFee: Maker fee rate.
    """

    exName: str
    fundingRate: float
    nextFundingTime: int
    takerFee: float
    makerFee: float


class ArbitrageOpportunityData(TypedDict):
    """Represents the overall picture of a funding rate arbitrage opportunity.

    Attributes:
        symbol: Currency symbol.
        profit: Expected profit rate (%).
        fee: Total fee cost (%).
        buy: Data for the buy position leg.
        sell: Data for the sell position leg.
    """

    symbol: str
    profit: float
    fee: float
    buy: ArbitrageLegData
    sell: ArbitrageLegData
