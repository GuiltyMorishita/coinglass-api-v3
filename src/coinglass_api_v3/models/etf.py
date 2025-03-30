"""Data models related to Bitcoin and Ethereum ETFs."""

from typing import TypedDict, List, Optional


# ETF Related Data Models
class ETFData(TypedDict):
    """Represents ETF data.

    Attributes:
        name: Name of the ETF.
        netAssets: Net asset value (USD).
        price: Current price (USD).
        change24h: 24-hour price change percentage (%).
        volume24h: 24-hour trading volume (USD).
    """

    name: str
    netAssets: float
    price: float
    change24h: float
    volume24h: float


class ETFFlowData(TypedDict):
    """Represents ETF fund flow data.

    Attributes:
        date: Date (format: YYYY-MM-DD).
        name: Name of the ETF.
        flow: Fund flow amount for the day (USD).
        bitcoinFlow: Fund flow amount in Bitcoin equivalent (BTC).
    """

    date: str
    name: str
    flow: float
    bitcoinFlow: float


# --- Bitcoin ETF Data Models ---


# Bitcoin ETF Asset Info
class BitcoinETFInfoAssetInfo(TypedDict):
    """Represents asset information within Bitcoin ETF data.

    Attributes:
        nav: Net Asset Value (NAV).
        premiumDiscount: Premium or discount percentage.
        btcHolding: Bitcoin holdings.
        btcChangePercent1d: Percentage change in Bitcoin holding (1 day).
        btcChange1d: Absolute change in Bitcoin holding (1 day).
        btcChangePercent7d: Percentage change in Bitcoin holding (7 day).
        btcChange7d: Absolute change in Bitcoin holding (7 day).
        date: Date of the last NAV update (e.g., "2024-08-06").
    """

    nav: float
    premiumDiscount: float
    btcHolding: float
    btcChangePercent1d: float
    btcChange1d: float
    btcChangePercent7d: float
    btcChange7d: float
    date: str


# Bitcoin ETF List Data
class BitcoinETFInfoData(TypedDict):
    """Represents detailed information for a specific Bitcoin ETF.

    Attributes:
        ticker: Ticker symbol.
        name: Name of the ETF.
        locale: Locale (e.g., "us").
        marketStatus: Market status (e.g., "closed").
        primaryExchange: Primary exchange.
        cik: Central Index Key.
        type: Type (e.g., "Spot", "Futures").
        marketCap: Market capitalization (as string, check API).
        listDate: Listing date timestamp (milliseconds).
        shareClassSharesOutstanding: Outstanding shares (as string, check API).
        aum: Assets Under Management (as string, check API).
        fee: Expense ratio (as string, check API, e.g., "1.5").
        lastTradeTime: Last trade timestamp (milliseconds).
        lastQuoteTime: Last quote timestamp (milliseconds).
        volume: Trading volume (API shows int, using float for safety).
        volumeUsd: Trading volume in USD.
        price: Current price.
        priceChange: Price change.
        priceChangePercent: Percentage price change.
        assetInfo: Detailed asset information.
        updateTime: Last update timestamp (milliseconds).
    """

    ticker: str
    name: str
    locale: str
    marketStatus: str
    primaryExchange: str
    cik: str
    type: str
    marketCap: str
    listDate: int
    shareClassSharesOutstanding: str
    aum: str
    fee: str
    lastTradeTime: int
    lastQuoteTime: int
    volume: float
    volumeUsd: float
    price: float
    priceChange: float
    priceChangePercent: float
    assetInfo: BitcoinETFInfoAssetInfo
    updateTime: int


# --- Hong Kong ETF Data Models ---


# Hong Kong ETF Flow Ticker Data
class HKEtFlowTickerData(TypedDict):
    """Represents flow data for a specific ticker within Hong Kong ETF flows.

    Attributes:
        ticker: Ticker symbol.
        changeUsd: USD inflow/outflow for the ticker.
    """

    ticker: str
    changeUsd: float


# Hong Kong ETF Flow Data
class HKEtFlowData(TypedDict):
    """Represents historical flow data for Hong Kong ETFs for a specific date.

    Attributes:
        date: Timestamp in milliseconds.
        changeUsd: Total USD inflow/outflow for the date.
        price: Bitcoin price at the time.
        list: List of flow data per ticker.
    """

    date: int
    changeUsd: float
    price: float
    list: List[HKEtFlowTickerData]


# --- General ETF History/Detail Data Models ---


# ETF Net Assets History Data
class ETFNetAssetsHistoryData(TypedDict):
    """Represents historical net assets data for an ETF.

    Attributes:
        netAssets: Total net assets.
        change: Total USD inflow/outflow.
        date: Timestamp in milliseconds.
        price: Bitcoin price at the time.
    """

    netAssets: float
    change: float
    date: int
    price: float


# ETF Flow History Ticker Data
class ETFFlowHistoryTickerData(TypedDict):
    """Represents flow data for a specific ticker within ETF flow history.

    Attributes:
        ticker: Ticker symbol.
        changeUsd: Optional USD inflow/outflow (might be missing if not updated).
    """

    ticker: str
    changeUsd: Optional[float]


# ETF Flow History Data
class ETFFlowHistoryData(TypedDict):
    """Represents historical flow data for ETFs for a specific date.

    Attributes:
        date: Timestamp in milliseconds.
        changeUsd: Total USD inflow/outflow for the date.
        price: Bitcoin price at the time.
        closePrice: Bitcoin close price for the date.
        list: List of flow data per ticker.
    """

    date: int
    changeUsd: float
    price: float
    closePrice: float
    list: List[ETFFlowHistoryTickerData]


# ETF Premium/Discount Ticker Data
class ETFPremiumDiscountTickerData(TypedDict):
    """Represents premium/discount data for a specific ticker.

    Attributes:
        nav: Net Asset Value (NAV).
        marketPrice: Current market price.
        premiumDiscountPercent: Premium or discount percentage.
        ticker: Ticker symbol.
    """

    nav: float
    marketPrice: float
    premiumDiscountPercent: float
    ticker: str


# ETF Premium/Discount History Data
class ETFPremiumDiscountHistoryData(TypedDict):
    """Represents historical premium/discount data for ETFs for a specific date.

    Attributes:
        date: Timestamp in milliseconds.
        list: List of premium/discount data per ticker.
    """

    date: int
    list: List[ETFPremiumDiscountTickerData]


# ETF History Data
class ETFHistoryData(TypedDict):
    """Represents historical data for a specific ETF ticker.

    Attributes:
        assetsDate: Timestamp for assets data.
        amount: Amount (likely BTC holding, confirm unit/meaning).
        marketDate: Timestamp for market data.
        marketPrice: Market price at the marketDate.
        name: Name of the ETF.
        nav: Net Asset Value (NAV).
        netAssets: Net assets value.
        premiumDiscount: Premium or discount percentage.
        sharesOutstanding: Outstanding shares (API example shows int).
        ticker: Ticker symbol.
    """

    assetsDate: int
    amount: float
    marketDate: int
    marketPrice: float
    name: str
    nav: float
    netAssets: float
    premiumDiscount: float
    sharesOutstanding: int
    ticker: str


# ETF Price Data
class ETFPriceData(TypedDict):
    """Represents OHLC price data for an ETF for a specific time.

    Note: API example shows values as strings, confirm actual type if possible.

    Attributes:
        t: Timestamp in milliseconds (as string).
        o: Open price (as string).
        h: High price (as string).
        l: Low price (as string).
        c: Close price (as string).
        v: Volume (as string).
    """

    t: str
    o: str
    h: str
    l: str
    c: str
    v: str


# ETF Detail - Ticker Info
class ETFDetailTickerInfo(TypedDict):
    """Represents the ticker information part of ETF detail.

    NOTE: Contains many fields, only key ones might be explicitly typed if needed.
          Check API for types of string fields like aum, fee, etc.
          'active' field is likely boolean but shown as string 'true'/'false'.

    Attributes:
        id: ID.
        ticker: Ticker symbol.
        name: ETF name.
        market: Market identifier.
        locale: Locale (e.g., "us").
        primaryExchange: Primary exchange.
        type: Type identifier.
        active: Activity status ('true'/'false').
        currencyName: Currency name.
        cik: Central Index Key.
        compositeFigi: Composite FIGI.
        shareClassFigi: Share class FIGI.
        aum: Assets Under Management (string).
        phoneNumber: Phone number string.
        tag: Tag string.
        fee: Expense ratio (string).
        type2: Secondary type identifier (e.g., 'Spot').
        address: Address information (JSON string).
        sicCode: SIC code.
        sicDescription: SIC description.
        tickerRoot: Ticker root symbol.
        listDate: Listing date timestamp (milliseconds).
        shareClassSharesOutstanding: Outstanding shares (string).
        roundLot: Round lot size (string).
        status: Status code (integer).
        updateTime: Last update timestamp (milliseconds).
    """

    id: int
    ticker: str
    name: str
    market: str
    locale: str
    primaryExchange: str
    type: str
    active: str
    currencyName: str
    cik: str
    compositeFigi: str
    shareClassFigi: str
    aum: str
    phoneNumber: str
    tag: str
    fee: str
    type2: str
    address: str
    sicCode: str
    sicDescription: str
    tickerRoot: str
    listDate: int
    shareClassSharesOutstanding: str
    roundLot: str
    status: int
    updateTime: int


# ETF Detail - Session
class ETFDetailSession(TypedDict):
    """Represents the session information part of ETF detail.

    Attributes:
        change: Price change during the session.
        changePercent: Percentage price change during the session.
        earlyTradingChange: Price change during early trading.
        earlyTradingChangePercent: Percentage price change during early trading.
        close: Closing price.
        high: Highest price during the session.
        low: Lowest price during the session.
        open: Opening price.
        volume: Trading volume during the session.
        previousClose: Previous closing price.
        price: Current or last price.
    """

    change: float
    changePercent: float
    earlyTradingChange: float
    earlyTradingChangePercent: float
    close: float
    high: float
    low: float
    open: float
    volume: float
    previousClose: float
    price: float


# ETF Detail - Last Quote
class ETFDetailLastQuote(TypedDict):
    """Represents the last quote information part of ETF detail.

    Attributes:
        lastUpdated: Timestamp of the last update (milliseconds).
        timeframe: Timeframe identifier.
        ask: Ask price.
        askSize: Ask size.
        askExchange: Exchange identifier for the ask.
        bid: Bid price.
        bidSize: Bid size.
        bidExchange: Exchange identifier for the bid.
    """

    lastUpdated: int
    timeframe: str
    ask: float
    askSize: int
    askExchange: int
    bid: float
    bidSize: int
    bidExchange: int


# ETF Detail - Last Trade
class ETFDetailLastTrade(TypedDict):
    """Represents the last trade information part of ETF detail.

    Attributes:
        lastUpdated: Timestamp of the last update (milliseconds).
        timeframe: Timeframe identifier.
        id: Trade ID.
        price: Trade price.
        size: Trade size.
        exchange: Exchange identifier for the trade.
        conditions: List of trade conditions (integers).
    """

    lastUpdated: int
    timeframe: str
    id: str
    price: float
    size: int
    exchange: int
    conditions: List[int]


# ETF Detail - Performance
class ETFDetailPerformance(TypedDict):
    """Represents the performance information part of ETF detail.

    Attributes:
        lowPrice52week: 52-week low price.
        highPrice52week: 52-week high price.
        highPrice52weekDate: Timestamp of the 52-week high price (milliseconds).
        lowPrice52weekDate: Timestamp of the 52-week low price (milliseconds).
        ydtChangePercent: Year-to-date percentage change.
        yearChangePercent: 1-year percentage change.
        avgVolUsd10d: Average 10-day volume in USD.
    """

    lowPrice52week: float
    highPrice52week: float
    highPrice52weekDate: int
    lowPrice52weekDate: int
    ydtChangePercent: float
    yearChangePercent: float
    avgVolUsd10d: float


# ETF Detail Data
class ETFDetailData(TypedDict):
    """Represents the complete detail data for an ETF.

    Attributes:
        tickerInfo: Detailed ticker information.
        marketStatus: Market status string.
        name: ETF name.
        ticker: Ticker symbol.
        type: Type string (e.g., 'stocks').
        session: Session data.
        lastQuote: Last quote data.
        lastTrade: Last trade data.
        performance: Performance data.
    """

    tickerInfo: ETFDetailTickerInfo
    marketStatus: str
    name: str
    ticker: str
    type: str
    session: ETFDetailSession
    lastQuote: ETFDetailLastQuote
    lastTrade: ETFDetailLastTrade
    performance: ETFDetailPerformance


# --- Ethereum ETF Data Models ---


# Ethereum ETF Net Assets History Data
class EthereumETFNetAssetsHistoryData(TypedDict):
    """Represents historical net assets data for an Ethereum ETF.

    Attributes:
        netAssets: Total net assets.
        change: Total USD inflow/outflow.
        date: Timestamp in milliseconds.
        price: Ethereum price at the time.
    """

    netAssets: float
    change: float
    date: int
    price: float


# Ethereum ETF Asset Info
class EthereumETFInfoAssetInfo(TypedDict):
    """Represents asset information within Ethereum ETF data.

    Attributes:
        nav: Net Asset Value (NAV).
        premiumDiscount: Premium or discount percentage.
        holding: Ethereum holdings.
        changePercent1d: Percentage change in Ethereum holding (1 day).
        change1d: Absolute change in Ethereum holding (1 day).
        changePercent7d: Percentage change in Ethereum holding (7 day).
        change7d: Absolute change in Ethereum holding (7 day).
        date: Date of the last NAV update (e.g., "2024-08-05").
    """

    nav: float
    premiumDiscount: float
    holding: float
    changePercent1d: float
    change1d: float
    changePercent7d: float
    change7d: float
    date: str


# Ethereum ETF List Data
class EthereumETFInfoData(TypedDict):
    """Represents detailed information for a specific Ethereum ETF.

    Attributes:
        ticker: Ticker symbol.
        name: Name of the ETF.
        locale: Locale (e.g., "us").
        marketStatus: Market status (e.g., "closed").
        primaryExchange: Primary exchange.
        cik: Central Index Key.
        type: Type (e.g., "Spot", "Futures").
        marketCap: Market capitalization (as string, check API).
        listDate: Listing date timestamp (milliseconds).
        shareClassSharesOutstanding: Outstanding shares (as string, check API).
        aum: Assets Under Management (as string, can be empty, check API).
        fee: Expense ratio (as string, check API).
        lastTradeTime: Last trade timestamp (milliseconds).
        lastQuoteTime: Last quote timestamp (milliseconds).
        volume: Trading volume.
        volumeUsd: Trading volume in USD.
        price: Current price.
        priceChange: Price change.
        priceChangePercent: Percentage price change.
        assetInfo: Detailed asset information.
        updateTime: Last update timestamp (milliseconds).
    """

    ticker: str
    name: str
    locale: str
    marketStatus: str
    primaryExchange: str
    cik: str
    type: str
    marketCap: str
    listDate: int
    shareClassSharesOutstanding: str
    aum: str
    fee: str
    lastTradeTime: int
    lastQuoteTime: int
    volume: float
    volumeUsd: float
    price: float
    priceChange: float
    priceChangePercent: float
    assetInfo: EthereumETFInfoAssetInfo
    updateTime: int


# Ethereum ETF Flow History Ticker Data
class EthereumETFFlowHistoryTickerData(TypedDict):
    """Represents flow data for a specific ticker within Ethereum ETF flow history.

    Attributes:
        ticker: Ticker symbol.
        changeUsd: Optional USD inflow/outflow (might be missing if not updated).
    """

    ticker: str
    changeUsd: Optional[float]


# Ethereum ETF Flow History Data
class EthereumETFFlowHistoryData(TypedDict):
    """Represents historical flow data for Ethereum ETFs for a specific date.

    Attributes:
        date: Timestamp in milliseconds.
        changeUsd: Total USD inflow/outflow for the date.
        price: Ethereum price at the time.
        closePrice: Ethereum close price for the date.
        list: List of flow data per ticker.
    """

    date: int
    changeUsd: float
    price: float
    closePrice: float
    list: List[EthereumETFFlowHistoryTickerData]
