"""Data models for the Coinglass API v3.

This package aggregates all data models defined in the submodules.
"""

from .common import *
from .market import *
from .liquidation import *
from .funding_rate import *
from .open_interest import *
from .etf import *
from .indicator import *
from .onchain import *
from .exchange import *
from .orderbook import *
from .trade import *
from .option import *
from .websocket import *
from .margin import *
from .hyperliquid import *
from .spot import *

__all__ = [
    # Common models
    "ExchangePair",
    "ExchangeInfo",
    "ExchangeSymbolInfo",
    "SymbolInfo",
    "TimeRange",
    "PaginatedData",
    "PaginationInfo",
    # Market models
    "OHLCData",
    "CoinMarketData",
    "PairMarketData",
    "MarketData",
    "MarketInfo",
    "MarketPriceData",
    "MarketTradeData",
    "MarketVolumeData",
    # Liquidation models
    "LiquidationHistoryData",
    "LiquidationCoinData",
    "LongShortRatioData",
    "LiquidationData",
    "LiquidationInfo",
    "LiquidationRankData",
    "LiquidationStatisticsData",
    # Funding Rate models
    "ExchangeFundingRateData",
    "CumulativeFundingRateData",
    "FundingRateArbitrageData",
    "SymbolFundingRateData",
    "ExchangeCumulativeFundingRateData",
    "SymbolCumulativeFundingRateData",
    "ArbitrageLegData",
    "ArbitrageOpportunityData",
    # Open Interest models
    "ExchangeOpenInterestData",
    "ExchangeHistoryChartData",
    # ETF models
    "ETFData",
    "ETFInfo",
    "ETFPriceData",
    "ETFTradeData",
    "ETFVolumeData",
    # Indicator models
    "BullMarketPeakIndicatorData",
    "BitcoinBubbleIndexData",
    "AHR999Data",
    "TwoYearMAMultiplierData",
    "MovingAvgHeatmapData",
    "PuellMultipleData",
    "StockFlowData",
    "PiCycleTopIndicatorData",
    "GoldenRatioMultiplierData",
    "BitcoinProfitableDaysData",
    "BitcoinRainbowChartDataPoint",
    "FearGreedHistoryData",
    "GrayscaleHoldingData",
    "GrayscalePremiumHistoryData",
    "BorrowInterestRateData",
    "ExchangeBalanceListData",
    "ExchangeBalanceChartData",
    "CoinPriceChangeData",
    "RsiData",
    # On-chain models
    "ExchangeOnchainTransferData",
    # Exchange models
    "ExchangeBalanceListData",
    "ExchangeBalanceChartData",
    # Orderbook models
    "OrderbookHistoryData",
    "LargeLimitOrderData",
    "HyperliquidWhalePositionData",
    "HyperliquidWhaleAlertData",
    "FuturesTradeOrderData",
    # Trade models
    "TakerBuySellData",
    "TakerBuySellVolumeData",
    "AggregatedTakerBuySellRatioData",
    "AggregatedTakerBuySellVolumeData",
    "ExchangeTakerBuySellRatioData",
    # Option models
    "OptionInfoData",
    "OptionData",
    "OptionInfo",
    "OptionPriceData",
    "OptionTradeData",
    "OptionVolumeData",
    # WebSocket models
    "WebSocketMessage",
    "WebSocketSubscription",
    "WebSocketUnsubscription",
    # Margin models
    "BitfinexMarginLongShortData",
    # Hyperliquid models
    "HyperliquidWhalePositionData",
    "HyperliquidWhaleAlertData",
    # Spot models
    "SpotTakerBuySellData",
    "SpotOrderbookHistoryData",
    "SpotPairMarketData",
    "CoinbasePremiumIndexData",
]
