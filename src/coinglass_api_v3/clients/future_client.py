"""
Coinglass Futures Client
======================

This module provides access to futures market related features of the Coinglass API.
"""

from typing import Dict, List, Union, Optional, cast, Any
from .base_client import BaseClient
from ..models import (
    OHLCData,
    ExchangeOpenInterestData,
    LongShortRatioData,
    ArbitrageOpportunityData,
    ExchangePair,
    TakerBuySellVolumeData,
    ExchangeHistoryChartData,
    SymbolFundingRateData,
    SymbolCumulativeFundingRateData,
    LiquidationHistoryData,
    LiquidationCoinData,
    LiquidationExchangeData,
    LiquidationOrderData,
    LiquidationAggregatedHeatmapData,
    AggregatedTakerBuySellRatioData,
    AggregatedTakerBuySellVolumeData,
    ExchangeTakerBuySellRatioData,
    HyperliquidWhalePositionData,
    HyperliquidWhaleAlertData,
    CoinMarketData,
    PairMarketData,
    CoinPriceChangeData,
    OrderbookHistoryData,
    RsiData,
)


class FutureClient(BaseClient):
    """Client providing access to futures market related endpoints.

    Also provides general information retrieval features.
    """

    # General Information Methods

    def get_supported_coins(self) -> List[str]:
        """Gets the list of supported currencies.

        Returns:
            A list of supported currency symbols.
        """
        response = self._request("GET", "/api/futures/supported-coins")
        return response["data"]

    def get_supported_exchange_pairs(self) -> Dict[str, List[ExchangePair]]:
        """Gets the list of supported exchanges and trading pairs.

        Returns:
            A dictionary mapping exchange names to lists of trading pairs.
        """
        response = self._request("GET", "/api/futures/supported-exchange-pairs")
        return cast(Dict[str, List[ExchangePair]], response["data"])

    # Open Interest Related Methods

    def get_open_interest_ohlc_history(
        self,
        exchange: str = "Binance",
        symbol: str = "BTCUSDT",
        interval: str = "1d",
        limit: int = 1000,
        startTime: Optional[int] = None,
        endTime: Optional[int] = None,
    ) -> List[OHLCData]:
        """Gets the OHLC history data for open interest.

        Args:
            symbol: Trading pair (e.g., "BTCUSDT"). Defaults to "BTCUSDT".
            exchange: Exchange name (e.g., "Binance"). Defaults to "Binance".
                      Check the 'support-exchange-pair' API for supported exchanges.
            interval: Data time interval (e.g., "1h", "4h", "1d"). Defaults to "1d".
                      Valid values: "1m", "3m", "5m", "15m", "30m", "1h", "4h", "6h", "8h", "12h", "1d", "1w".
            limit: Number of data points to return. Defaults to 1000, max 4500.
            startTime: Start time (Unix timestamp in seconds). E.g., 1641522717.
            endTime: End time (Unix timestamp in seconds). E.g., 1641522717.

        Returns:
            A list of OHLC history data. Each data point includes 't', 'o', 'h', 'l', 'c'.
        """
        params: Dict[str, Union[str, int]] = {
            "symbol": symbol,
            "exchange": exchange,
            "interval": interval,
            "limit": limit,
        }

        if startTime:
            params["startTime"] = startTime
        if endTime:
            params["endTime"] = endTime

        response = self._request(
            "GET", "/api/futures/openInterest/ohlc-history", params
        )
        return cast(List[OHLCData], response["data"])

    def get_open_interest_ohlc_aggregated_history(
        self,
        symbol: str = "BTC",
        interval: str = "1d",
        limit: int = 1000,
        startTime: Optional[int] = None,
        endTime: Optional[int] = None,
    ) -> List[OHLCData]:
        """Gets the aggregated OHLC history data for open interest.

        Args:
            symbol: Currency symbol (e.g., "BTC"). Defaults to "BTC".
                      Check the 'support-coins' API for supported coins.
            interval: Data time interval (e.g., "1h", "4h", "1d"). Defaults to "1d".
                      Valid values: "1m", "3m", "5m", "15m", "30m", "1h", "4h", "6h", "8h", "12h", "1d", "1w".
            limit: Number of data points to return. Defaults to 1000, max 4500.
            startTime: Start time (Unix timestamp in seconds). E.g., 1641522717.
            endTime: End time (Unix timestamp in seconds). E.g., 1641522717.

        Returns:
            A list of OHLC history data. Each data point includes 't', 'o', 'h', 'l', 'c'.
        """
        params: Dict[str, Union[str, int]] = {
            "symbol": symbol,
            "interval": interval,
            "limit": limit,
        }

        if startTime:
            params["startTime"] = startTime
        if endTime:
            params["endTime"] = endTime

        response = self._request(
            "GET", "/api/futures/openInterest/ohlc-aggregated-history", params
        )
        return cast(List[OHLCData], response["data"])

    def get_open_interest_ohlc_aggregated_stablecoin_margin_history(
        self,
        exchanges: str = "Binance",
        symbol: str = "BTC",
        interval: str = "1d",
        limit: int = 1000,
        startTime: Optional[int] = None,
        endTime: Optional[int] = None,
    ) -> List[OHLCData]:
        """Gets the aggregated stablecoin-margined open interest OHLC history data.

        Args:
            exchanges: Exchange names (comma-separated). E.g., "Binance,OKX,Bybit". Defaults to "Binance".
            symbol: Currency symbol (e.g., "BTC"). Defaults to "BTC".
                      Check the 'support-coins' API for supported coins.
            interval: Data time interval (e.g., "1h", "4h", "1d"). Defaults to "1d".
                      Valid values: "1m", "3m", "5m", "15m", "30m", "1h", "4h", "6h", "8h", "12h", "1d", "1w".
            limit: Number of data points to return. Defaults to 1000, max 4500.
            startTime: Start time (Unix timestamp in seconds). E.g., 1641522717.
            endTime: End time (Unix timestamp in seconds). E.g., 1641522717.

        Returns:
            A list of OHLC history data. Each data point includes 't', 'o', 'h', 'l', 'c'.
        """
        params: Dict[str, Union[str, int]] = {
            "exchanges": exchanges,
            "symbol": symbol,
            "interval": interval,
            "limit": limit,
        }

        if startTime:
            params["startTime"] = startTime
        if endTime:
            params["endTime"] = endTime

        response = self._request(
            "GET",
            "/api/futures/openInterest/ohlc-aggregated-stablecoin-margin-history",
            params,
        )
        return cast(List[OHLCData], response["data"])

    def get_open_interest_ohlc_aggregated_coin_margin_history(
        self,
        exchanges: str = "Binance",
        symbol: str = "BTC",
        interval: str = "1d",
        limit: int = 1000,
        startTime: Optional[int] = None,
        endTime: Optional[int] = None,
    ) -> List[OHLCData]:
        """Gets the aggregated coin-margined open interest OHLC history data.

        Args:
            exchanges: Exchange names (comma-separated). E.g., "Binance,OKX,Bybit". Defaults to "Binance".
            symbol: Currency symbol (e.g., "BTC"). Defaults to "BTC".
                      Check the 'support-coins' API for supported coins.
            interval: Data time interval (e.g., "1h", "4h", "1d"). Defaults to "1d".
                      Valid values: "1m", "3m", "5m", "15m", "30m", "1h", "4h", "6h", "8h", "12h", "1d", "1w".
            limit: Number of data points to return. Defaults to 1000, max 4500.
            startTime: Start time (Unix timestamp in seconds). E.g., 1641522717.
            endTime: End time (Unix timestamp in seconds). E.g., 1641522717.

        Returns:
            A list of OHLC history data. Each data point includes 't', 'o', 'h', 'l', 'c'.
        """
        params: Dict[str, Union[str, int]] = {
            "exchanges": exchanges,
            "symbol": symbol,
            "interval": interval,
            "limit": limit,
        }

        if startTime:
            params["startTime"] = startTime
        if endTime:
            params["endTime"] = endTime

        response = self._request(
            "GET",
            "/api/futures/openInterest/ohlc-aggregated-coin-margin-history",
            params,
        )
        return cast(List[OHLCData], response["data"])

    def get_open_interest_exchange_list(
        self, symbol: str = "BTC"
    ) -> List[ExchangeOpenInterestData]:
        """
        指定されたコインのオープンインタレストデータを取引所ごとに取得します。

        Args:
            symbol: 通貨シンボル (例: "BTC")。デフォルトは "BTC"。
                      サポートされているコインは 'support-coins' APIで確認してください。

        Returns:
            取引所ごとのオープンインタレストデータのリスト。
            各要素には、取引所名、シンボル、USD建てオープンインタレスト、コイン建てオープンインタレスト、
            コインマージン/ステーブルコインマージン別のオープンインタレスト（USD/コイン建て）、
            および様々な時間枠でのオープンインタレスト変化率が含まれます。
        """
        params: Dict[str, str] = {"symbol": symbol}

        response = self._request(
            "GET", "/api/futures/openInterest/exchange-list", params
        )
        return cast(List[ExchangeOpenInterestData], response["data"])

    def get_open_interest_exchange_history_chart(
        self, symbol: str = "BTC", range: str = "12h", unit: str = "USD"
    ) -> ExchangeHistoryChartData:
        """Gets the past open interest data per exchange for the specified cryptocurrency (for chart display).

        Args:
            symbol: Currency symbol (e.g., "BTC"). Defaults to "BTC".
                      Check the 'support-coins' API for supported coins.
            range: Data retrieval range. Defaults to "12h".
                   Valid values: "all", "1m", "15m", "1h", "4h", "12h".
            unit: Unit of the returned data. Defaults to "USD".
                  Valid values: "USD", "COIN".

        Returns:
            History data formatted for chart display.
            Includes 'timeList' (list of timestamps), 'priceList' (list of prices),
            and 'dataMap' (dictionary with exchange names as keys and lists of open interest as values).
        """
        params: Dict[str, str] = {"symbol": symbol, "range": range, "unit": unit}

        response = self._request(
            "GET", "/api/futures/openInterest/exchange-history-chart", params
        )
        return cast(ExchangeHistoryChartData, response["data"])

    # Funding Rate Related Methods

    def get_funding_rate_ohlc_history(
        self,
        exchange: str = "Binance",
        symbol: str = "BTCUSDT",
        interval: str = "1d",
        limit: int = 1000,
        startTime: Optional[int] = None,
        endTime: Optional[int] = None,
    ) -> List[OHLCData]:
        """Gets the OHLC history data for funding rates.

        Args:
            exchange: Exchange name (e.g., "Binance"). Defaults to "Binance".
                      Check the 'support-exchange-pair' API for supported exchanges.
            symbol: Trading pair (e.g., "BTCUSDT"). Defaults to "BTCUSDT".
                      Check the 'support-exchange-pair' API for supported pairs.
            interval: Data time interval (e.g., "1h", "4h", "1d"). Defaults to "1d".
                      Valid values: "1m", "3m", "5m", "15m", "30m", "1h", "4h", "6h", "8h", "12h", "1d", "1w".
            limit: Number of data points to return. Defaults to 1000, max 4500.
            startTime: Start time (Unix timestamp in seconds). E.g., 1641522717.
            endTime: End time (Unix timestamp in seconds). E.g., 1641522717.

        Returns:
            A list of funding rate OHLC history data.
            Each data point includes 't', 'o', 'h', 'l', 'c'.
        """
        params: Dict[str, Union[str, int]] = {
            "exchange": exchange,
            "symbol": symbol,
            "interval": interval,
            "limit": limit,
        }

        if startTime:
            params["startTime"] = startTime
        if endTime:
            params["endTime"] = endTime

        response = self._request("GET", "/api/futures/fundingRate/ohlc-history", params)
        return cast(List[OHLCData], response["data"])

    def get_funding_rate_oi_weight_ohlc_history(
        self,
        symbol: str = "BTC",
        interval: str = "1d",
        limit: int = 1000,
        startTime: Optional[int] = None,
        endTime: Optional[int] = None,
    ) -> List[OHLCData]:
        """Gets the open interest weighted OHLC history data for funding rates.

        Args:
            symbol: Trading coin (e.g., "BTC"). Defaults to "BTC".
                      Check the 'support-coins' API for supported coins.
            interval: Data time interval (e.g., "1h", "4h", "1d"). Defaults to "1d".
                      Valid values: "1m", "3m", "5m", "15m", "30m", "1h", "4h", "6h", "8h", "12h", "1d", "1w".
            limit: Number of data points to return. Defaults to 1000, max 4500.
            startTime: Start time (Unix timestamp in seconds). E.g., 1641522717.
            endTime: End time (Unix timestamp in seconds). E.g., 1641522717.

        Returns:
            A list of open interest weighted funding rate OHLC history data.
            Each data point includes 't', 'o', 'h', 'l', 'c'.
        """
        params: Dict[str, Union[str, int, None]] = {
            "symbol": symbol,
            "interval": interval,
            "limit": limit,
        }

        if startTime:
            params["startTime"] = startTime
        if endTime:
            params["endTime"] = endTime

        response = self._request(
            "GET", "/api/futures/fundingRate/oi-weight-ohlc-history", params
        )
        return cast(List[OHLCData], response["data"])

    def get_funding_rate_vol_weight_ohlc_history(
        self,
        symbol: str = "BTC",
        interval: str = "1d",
        limit: int = 1000,
        startTime: Optional[int] = None,
        endTime: Optional[int] = None,
    ) -> List[OHLCData]:
        """Gets the volume weighted OHLC history data for funding rates.

        Args:
            symbol: Currency symbol (e.g., "BTC").
            interval: Data time interval (e.g., "1h", "4h", "1d").
            limit: Number of data points to return.
            startTime: Start time (Unix timestamp in seconds). E.g., 1641522717.
            endTime: End time (Unix timestamp in seconds). E.g., 1641522717.

        Returns:
            A list of volume weighted OHLC history data.
        """
        params: Dict[str, Union[str, int, None]] = {
            "symbol": symbol,
            "interval": interval,
            "limit": limit,
        }

        if startTime:
            params["startTime"] = startTime
        if endTime:
            params["endTime"] = endTime

        response = self._request(
            "GET", "/api/futures/fundingRate/vol-weight-ohlc-history", params
        )
        return cast(List[OHLCData], response["data"])

    def get_funding_rate_exchange_list(self) -> List[SymbolFundingRateData]:
        """Gets the list of exchanges providing funding rate data.

        Returns:
            A list of funding rate data per symbol.
            Each element contains 'usdtOrUsdMarginList' and 'tokenMarginList',
            each holding funding rate information per exchange ('exchange', 'fundingRate', 'nextFundingTime').
        """
        response = self._request("GET", "/api/futures/fundingRate/exchange-list")
        return cast(List[SymbolFundingRateData], response["data"])

    def get_funding_rate_accumulated_exchange_list(
        self, range: str = "1d"
    ) -> List[SymbolCumulativeFundingRateData]:
        """Gets the cumulative funding rate data per exchange for the specified period.

        Args:
            range: Aggregation period (e.g., "1d", "7d", "30d", "365d"). Defaults to "1d".
                      Valid values: "1d", "7d", "30d", "365d"

        Returns:
            A list of cumulative funding rate data per symbol.
            Each element contains 'usdtOrUsdMarginList' and 'tokenMarginList',
            each holding cumulative funding rate information per exchange ('exchange', 'fundingRate').
        """
        params: Dict[str, str] = {"range": range}

        response = self._request(
            "GET", "/api/futures/fundingRate/accumulated-exchange-list", params
        )
        return cast(List[SymbolCumulativeFundingRateData], response["data"])

    def get_funding_rate_arbitrage(
        self, usd: int = 10000
    ) -> List[ArbitrageOpportunityData]:
        """Gets funding rate arbitrage opportunities.

        Args:
            usd: Investment amount in USD. Defaults to 10000.

        Returns:
            A list of funding rate arbitrage opportunities.
            Each element includes symbol, profit, fees, buy leg, and sell leg information.
        """
        params: Dict[str, int] = {"usd": usd}

        response = self._request("GET", "/api/futures/fundingRate/arbitrage", params)
        return cast(List[ArbitrageOpportunityData], response["data"])

    # Liquidation Related Methods

    def get_liquidation_history(
        self,
        exchange: str = "Binance",
        symbol: str = "BTCUSDT",
        interval: str = "1d",
        limit: int = 1000,
        startTime: Optional[int] = None,
        endTime: Optional[int] = None,
    ) -> List[LiquidationHistoryData]:
        """
        取引所の取引ペアのロングとショートの清算の履歴データを取得します。

        Args:
            exchange: 取引所名 (例: "Binance")。デフォルトは "Binance"。
                      サポートされている取引所は 'support-exchange-pair' APIで確認してください。
            symbol: 取引ペア (例: "BTCUSDT")。デフォルトは "BTCUSDT"。
                      サポートされているペアは 'support-exchange-pair' APIで確認してください。
            interval: データの時間間隔 (例: "1h", "4h", "1d")。デフォルトは "1d"。
                      有効な値: "1m", "3m", "5m", "15m", "30m", "1h", "4h", "6h", "8h", "12h", "1d", "1w".
            limit: 返されるデータポイントの数。デフォルトは 1000、最大 4500。
            startTime: 開始時刻（秒単位のタイムスタンプ）。例: 1641522717。
            endTime: 終了時刻（秒単位のタイムスタンプ）。例: 1641522717。

        Returns:
            清算履歴データのリスト。
            各データポイントには 'longLiquidationUsd', 'shortLiquidationUsd', 't' が含まれます。
        """
        params: Dict[str, Union[str, int, None]] = {
            "exchange": exchange,
            "symbol": symbol,
            "interval": interval,
            "limit": limit,
        }

        if startTime:
            params["startTime"] = startTime
        if endTime:
            params["endTime"] = endTime

        response = self._request("GET", "/api/futures/liquidation/v2/history", params)
        return cast(List[LiquidationHistoryData], response["data"])

    def get_liquidation_aggregated_history(
        self,
        exchanges: str = "ALL",
        symbol: str = "BTC",
        interval: str = "1d",
        limit: int = 1000,
        startTime: Optional[int] = None,
        endTime: Optional[int] = None,
    ) -> List[LiquidationHistoryData]:
        """
        指定された取引所（複数可）にわたるコインのロングとショートの集計された清算履歴データを取得します。

        Args:
            exchanges: Exchange names (comma-separated allowed). Defaults to "ALL".
                       E.g., "Binance,OKX", "ALL".
            symbol: Coin symbol (e.g., "BTC"). Defaults to "BTC".
                      Check the 'support-coins' API for supported coins.
            interval: Data time interval (e.g., "1h", "4h", "1d"). Defaults to "1d".
                      Valid values: "1m", "3m", "5m", "15m", "30m", "1h", "4h", "6h", "8h", "12h", "1d", "1w".
            limit: Number of data points to return. Defaults to 1000, max 4500.
            startTime: Start time (Unix timestamp in seconds). E.g., 1641522717.
            endTime: End time (Unix timestamp in seconds). E.g., 1641522717.

        Returns:
            A list of aggregated liquidation history data.
            Each data point includes 'longLiquidationUsd', 'shortLiquidationUsd', 't'.
        """
        params: Dict[str, Union[str, int, None]] = {
            "exchanges": exchanges,
            "symbol": symbol,
            "interval": interval,
            "limit": limit,
        }

        if startTime:
            params["startTime"] = startTime
        if endTime:
            params["endTime"] = endTime

        response = self._request(
            "GET", "/api/futures/liquidation/v3/aggregated-history", params
        )
        return cast(List[LiquidationHistoryData], response["data"])

    def get_liquidation_coin_list(
        self, ex: str = "Binance"
    ) -> List[LiquidationCoinData]:
        """Gets liquidation data for all coins on an exchange.

        Args:
            ex: Exchange name (e.g., "Binance"). Defaults to "Binance".
                  Check the 'support-exchange-pair' API for supported exchanges.

        Returns:
            A list of liquidation data per coin.
            Each element includes the symbol and liquidation data for different timeframes (24h, 12h, 4h, 1h).
        """
        params: Dict[str, str] = {"ex": ex}

        response = self._request("GET", "/api/futures/liquidation/coin-list", params)
        return cast(List[LiquidationCoinData], response["data"])

    def get_liquidation_exchange_list(
        self, symbol: str = "BTC", range: str = "1h"
    ) -> List[LiquidationExchangeData]:
        """Gets liquidation data across all exchanges for a specified coin.

        Args:
            symbol: Coin symbol (e.g., "BTC"). Defaults to "BTC".
                      Check the 'support-coins' API for supported coins.
            range: Data range ("1h", "4h", "12h", "24h"). Defaults to "1h".

        Returns:
            A list of liquidation data per exchange.
            Each element includes the exchange name and liquidation data (total, long, short) for the specified range.
        """
        params: Dict[str, str] = {"symbol": symbol, "range": range}

        response = self._request(
            "GET", "/api/futures/liquidation/exchange-list", params
        )
        return cast(List[LiquidationExchangeData], response["data"])

    def get_liquidation_order(
        self,
        exchange: str = "Binance",
        symbol: str = "BTC",
        minLiquidationAmount: str = "10000",
        startTime: Optional[int] = None,
        endTime: Optional[int] = None,
    ) -> List[LiquidationOrderData]:
        """Gets liquidation orders for the past 7 days (requires Standard Edition or higher account).
        Includes details such as exchange, trading pair, and liquidation amount.

        Args:
            exchange: Exchange name (e.g., "Binance"). Defaults to "Binance".
                      Check the 'support-exchange-pair' API for supported exchanges.
            symbol: Coin symbol (e.g., "BTC"). Defaults to "BTC".
                      Check the 'support-coins' API for supported coins.
            minLiquidationAmount: Minimum liquidation event amount threshold (string). Defaults to "10000".
            startTime: Start time (Unix timestamp in milliseconds). E.g., 1641522717000.
            endTime: End time (Unix timestamp in milliseconds). E.g., 1641522717000.

        Returns:
            A list of liquidation order data.
            Each element includes exchange name, symbol, price, amount in USD, side (1=long, 2=short), and time (ms).
        """
        params: Dict[str, Union[str, int, None]] = {
            "exchange": exchange,
            "symbol": symbol,
            "minLiquidationAmount": minLiquidationAmount,
        }

        if startTime:
            params["startTime"] = startTime
        if endTime:
            params["endTime"] = endTime

        response = self._request("GET", "/api/futures/liquidation/order", params)
        return cast(List[LiquidationOrderData], response["data"])

    def get_liquidation_aggregated_heatmap(
        self, symbol: str = "BTC", range: str = "3d"
    ) -> LiquidationAggregatedHeatmapData:
        """Gets aggregated liquidation heatmap data (requires Professional Edition or higher account).
        Shows aggregated liquidation levels on the chart, calculated from market data and various leverage amounts.

        Args:
            symbol: Coin symbol (e.g., "BTC"). Defaults to "BTC".
                      Check the 'support-coins' API for supported coins.
            range: Data range ("12h", "24h", "3d", "7d", "30d", "90d", "180d", "1y").
                   Defaults to "3d".

        Returns:
            Aggregated liquidation heatmap data.
            Includes 'y' (price list), 'liq' (x, y index and liquidation level), 'prices' (candlestick data).
        """
        params: Dict[str, str] = {"symbol": symbol, "range": range}

        response = self._request(
            "GET", "/api/futures/liquidation/aggregated-heatmap", params
        )
        return cast(LiquidationAggregatedHeatmapData, response["data"])

    def get_liquidation_aggregated_heatmap_model2(
        self, symbol: str = "BTC", range: str = "3d"
    ) -> LiquidationAggregatedHeatmapData:
        """Gets aggregated liquidation heatmap data (model 2) (requires Professional Edition or higher account).
        Shows aggregated liquidation levels on the chart, calculated from market data and various leverage amounts.

        Args:
            symbol: Coin symbol (e.g., "BTC"). Defaults to "BTC".
                      Check the 'support-coins' API for supported coins.
            range: Data range ("12h", "24h", "3d", "7d", "30d", "90d", "180d", "1y").
                   Defaults to "3d".

        Returns:
            Aggregated liquidation heatmap data.
            Includes 'y' (price list), 'liq' (x, y index and liquidation level), 'prices' (candlestick data).
        """
        params: Dict[str, str] = {"symbol": symbol, "range": range}

        response = self._request(
            "GET", "/api/futures/liquidation/model2/aggregated-heatmap", params
        )
        return cast(LiquidationAggregatedHeatmapData, response["data"])

    def get_liquidation_aggregated_heatmap_model3(
        self, symbol: str = "BTC", range: str = "3d"
    ) -> LiquidationAggregatedHeatmapData:
        """Gets aggregated liquidation heatmap data (model 3) (requires Professional Edition or higher account).
        Shows aggregated liquidation levels on the chart, calculated from market data and various leverage amounts.

        Args:
            symbol: Coin symbol (e.g., "BTC"). Defaults to "BTC".
                      Check the 'support-coins' API for supported coins.
            range: Data range ("12h", "24h", "3d", "7d", "30d", "90d", "180d", "1y").
                   Defaults to "3d".

        Returns:
            Aggregated liquidation heatmap data.
            Includes 'y' (price list), 'liq' (x, y index and liquidation level), 'prices' (candlestick data).
        """
        params: Dict[str, str] = {"symbol": symbol, "range": range}

        response = self._request(
            "GET", "/api/futures/liquidation/model3/aggregated-heatmap", params
        )
        return cast(LiquidationAggregatedHeatmapData, response["data"])

    def get_liquidation_heatmap(
        self, exchange: str = "Binance", symbol: str = "BTCUSDT", range: str = "3d"
    ) -> LiquidationAggregatedHeatmapData:
        """Gets liquidation heatmap data (requires Professional Edition or higher account).
        Shows liquidation levels on the chart, calculated based on market data and various leverage amounts.

        Args:
            exchange: Exchange name (e.g., "Binance"). Defaults to "Binance".
                      Check the 'support-exchange-pair' API for supported exchanges.
            symbol: Trading pair (e.g., "BTCUSDT"). Defaults to "BTCUSDT".
                      Check the 'support-exchange-pair' API for supported pairs.
            range: Data range ("12h", "24h", "3d", "7d", "30d", "90d", "180d", "1y").
                   Defaults to "3d".

        Returns:
            Liquidation heatmap data.
            Includes 'y' (price list), 'liq' (x, y index and liquidation level), 'prices' (candlestick data).
        """
        params: Dict[str, str] = {
            "exchange": exchange,
            "symbol": symbol,
            "range": range,
        }

        response = self._request("GET", "/api/futures/liquidation/heatmap", params)
        return cast(LiquidationAggregatedHeatmapData, response["data"])

    def get_liquidation_heatmap_model2(
        self, exchange: str = "Binance", symbol: str = "BTCUSDT", range: str = "3d"
    ) -> LiquidationAggregatedHeatmapData:
        """Gets liquidation heatmap data (model 2) (requires Professional Edition or higher account).
        Shows liquidation levels on the chart, calculated based on market data and various leverage amounts.

        Args:
            exchange: Exchange name (e.g., "Binance"). Defaults to "Binance".
                      Check the 'support-exchange-pair' API for supported exchanges.
            symbol: Trading pair (e.g., "BTCUSDT"). Defaults to "BTCUSDT".
                      Check the 'support-exchange-pair' API for supported pairs.
            range: Data range ("12h", "24h", "3d", "7d", "30d", "90d", "180d", "1y").
                   Defaults to "3d".

        Returns:
            Liquidation heatmap data.
            Includes 'y' (price list), 'liq' (x, y index and liquidation level), 'prices' (candlestick data).
        """
        params: Dict[str, str] = {
            "exchange": exchange,
            "symbol": symbol,
            "range": range,
        }

        response = self._request(
            "GET", "/api/futures/liquidation/model2/heatmap", params
        )
        return cast(LiquidationAggregatedHeatmapData, response["data"])

    def get_liquidation_heatmap_model3(
        self, exchange: str = "Binance", symbol: str = "BTCUSDT", range: str = "3d"
    ) -> LiquidationAggregatedHeatmapData:
        """Gets liquidation heatmap data (model 3) (requires Professional Edition or higher account).
        Shows liquidation levels on the chart, calculated based on market data and various leverage amounts.

        Args:
            exchange: Exchange name (e.g., "Binance"). Defaults to "Binance".
                      Check the 'support-exchange-pair' API for supported exchanges.
            symbol: Trading pair (e.g., "BTCUSDT"). Defaults to "BTCUSDT".
                      Check the 'support-exchange-pair' API for supported pairs.
            range: Data range ("12h", "24h", "3d", "7d", "30d", "90d", "180d", "1y").
                   Defaults to "3d".

        Returns:
            Liquidation heatmap data.
            Includes 'y' (price list), 'liq' (x, y index and liquidation level), 'prices' (candlestick data).
        """
        params: Dict[str, str] = {
            "exchange": exchange,
            "symbol": symbol,
            "range": range,
        }

        response = self._request(
            "GET", "/api/futures/liquidation/model3/heatmap", params
        )
        return cast(LiquidationAggregatedHeatmapData, response["data"])

    def get_liquidation_map(
        self, exchange: str = "Binance", symbol: str = "BTCUSDT", range: str = "1d"
    ) -> Dict[str, List[List[Union[float, int, None]]]]:
        """Gets liquidation map data (requires Professional Edition or higher account).
        Presents and maps liquidation events based on market data and diverse leverage amounts.

        Args:
            exchange: Exchange name (e.g., "Binance"). Defaults to "Binance".
                      Check the 'support-exchange-pair' API for supported exchanges.
            symbol: Trading pair (e.g., "BTCUSDT"). Defaults to "BTCUSDT".
                      Check the 'support-exchange-pair' API for supported pairs.
            range: Data range ("1d", "7d"). Defaults to "1d".

        Returns:
            Liquidation map data.
            A dictionary where keys are liquidation prices (string) and values are lists of lists:
            [liquidation price (number), liquidation level, leverage ratio, null].
        """
        params: Dict[str, str] = {
            "exchange": exchange,
            "symbol": symbol,
            "range": range,
        }

        response = self._request("GET", "/api/futures/liquidation/map", params)
        # Response format is {"code": ..., "msg": ..., "data": {"data": {...}}}
        # We need the inner "data" dictionary
        return cast(
            Dict[str, List[List[Union[float, int, None]]]], response["data"]["data"]
        )

    def get_liquidation_aggregated_map(
        self, symbol: str = "BTC", range: str = "1d"
    ) -> List[Dict[str, Any]]:
        """Gets aggregated liquidation map data (requires Professional Edition or higher account).
        Presents and maps liquidation events based on market data and diverse leverage amounts.

        Args:
            symbol: Trading pair (e.g., "BTC"). Defaults to "BTC".
                      Check the 'support-exchange-pair' API for supported pairs.
            range: Data range ("1d", "7d"). Defaults to "1d".

        Returns:
            A list of dictionaries containing liquidation map data per exchange.
            Each dictionary contains:
            - instrument: Exchange and trading pair information
            - liqMapV2: Dictionary mapping liquidation prices to lists of:
                [liquidation price, liquidation level, null, null]

            Example response structure:
            [
                {
                    "instrument": {
                        "instrumentId": "BTCUSDT",
                        "exName": "Binance",
                        ...
                    },
                    "liqMapV2": {
                        "74662": [[74662, 847226.59, null, null]],
                        "74749": [[74749, 1507896.16, null, null]],
                        ...
                    }
                },
                ...
            ]
        """
        params: Dict[str, str] = {"symbol": symbol, "range": range}

        response = self._request("GET", "/api/futures/liquidation/v2/exLiqMap", params)
        return cast(List[Dict[str, Any]], response["data"]["data"])

    # Long/Short Ratio Related Methods

    def get_global_long_short_account_ratio(
        self,
        exchange: str = "Binance",
        symbol: str = "BTCUSDT",
        interval: str = "1h",
        limit: int = 500,
        startTime: Optional[int] = None,
        endTime: Optional[int] = None,
    ) -> List[LongShortRatioData]:
        """Gets the historical data for the long/short account ratio for a specific trading pair on a given exchange.

        Args:
            exchange: Exchange name (e.g., "Binance"). Defaults to "Binance".
                            Check the 'support-exchange-pair' API for supported exchanges.
            symbol: Trading pair (e.g., "BTCUSDT"). Defaults to "BTCUSDT".
                          Check the 'support-exchange-pair' API for supported pairs.
            interval: Data time interval ("1m", "3m", "5m", "15m", "30m", "1h", "4h", "6h", "8h", "12h", "1d", "1w").
                            Defaults to "1h".
            limit: Number of data points to return. Defaults to 500.
            startTime: Start time (Unix timestamp in seconds). Defaults to None.
            endTime: End time (Unix timestamp in seconds). Defaults to None.

        Returns:
            A list of historical long/short ratio data.
            Each element includes time, longAccount, shortAccount, longShortRatio.
        """
        params: Dict[str, Union[str, int]] = {
            "exchange": exchange,
            "symbol": symbol,
            "interval": interval,
            "limit": limit,
        }
        if startTime is not None:
            params["startTime"] = startTime
        if endTime is not None:
            params["endTime"] = endTime

        response = self._request(
            "GET", "/api/futures/globalLongShortAccountRatio/history", params
        )
        return cast(List[LongShortRatioData], response["data"])

    def get_top_long_short_account_ratio(
        self,
        exchange: str = "Binance",
        symbol: str = "BTCUSDT",
        interval: str = "1h",
        limit: int = 500,
        startTime: Optional[int] = None,
        endTime: Optional[int] = None,
    ) -> List[LongShortRatioData]:
        """Gets the historical data for the long/short account ratio of top accounts on a given exchange.

        Args:
            exchange: Exchange name (e.g., "Binance"). Defaults to "Binance".
                            Check the 'support-exchange-pair' API for supported exchanges.
            symbol: Trading pair (e.g., "BTCUSDT"). Defaults to "BTCUSDT".
                          Check the 'support-exchange-pair' API for supported pairs.
            interval: Data time interval ("1m", "3m", "5m", "15m", "30m", "1h", "4h", "6h", "8h", "12h", "1d", "1w").
                            Defaults to "1h".
            limit: Number of data points to return. Defaults to 500.
            startTime: Start time (Unix timestamp in seconds). Defaults to None.
            endTime: End time (Unix timestamp in seconds). Defaults to None.

        Returns:
            A list of historical long/short ratio data for top accounts.
            Each element includes time, longAccount, shortAccount, longShortRatio.
        """
        params: Dict[str, Union[str, int]] = {
            "exchange": exchange,
            "symbol": symbol,
            "interval": interval,
            "limit": limit,
        }
        if startTime is not None:
            params["startTime"] = startTime
        if endTime is not None:
            params["endTime"] = endTime

        response = self._request(
            "GET", "/api/futures/topLongShortAccountRatio/history", params
        )
        return cast(List[LongShortRatioData], response["data"])

    def get_top_long_short_position_ratio(
        self,
        exchange: str = "Binance",
        symbol: str = "BTCUSDT",
        interval: str = "1h",
        limit: int = 500,
        startTime: Optional[int] = None,
        endTime: Optional[int] = None,
    ) -> List[LongShortRatioData]:
        """Gets the historical data for the long/short position ratio of top accounts on a given exchange.

        Args:
            exchange: Exchange name (e.g., "Binance"). Defaults to "Binance".
                            Check the 'support-exchange-pair' API for supported exchanges.
            symbol: Trading pair (e.g., "BTCUSDT"). Defaults to "BTCUSDT".
                          Check the 'support-exchange-pair' API for supported pairs.
            interval: Data time interval ("1m", "3m", "5m", "15m", "30m", "1h", "4h", "6h", "8h", "12h", "1d", "1w").
                            Defaults to "1h".
            limit: Number of data points to return. Defaults to 500.
            startTime: Start time (Unix timestamp in seconds). Defaults to None.
            endTime: End time (Unix timestamp in seconds). Defaults to None.

        Returns:
            A list of historical long/short position ratio data for top accounts.
            Each element includes time(createTime), longAccount, shortAccount, longShortRatio.
        """
        params: Dict[str, Union[str, int]] = {
            "exchange": exchange,
            "symbol": symbol,
            "interval": interval,
            "limit": limit,
        }
        if startTime is not None:
            params["startTime"] = startTime
        if endTime is not None:
            params["endTime"] = endTime

        response = self._request(
            "GET", "/api/futures/topLongShortPositionRatio/history", params
        )
        return cast(List[LongShortRatioData], response["data"])

    def get_aggregated_taker_buy_sell_history(
        self,
        exchange: str = "Binance",
        symbol: str = "BTCUSDT",
        interval: str = "1h",
        limit: int = 500,
        startTime: Optional[int] = None,
        endTime: Optional[int] = None,
    ) -> List[AggregatedTakerBuySellRatioData]:
        """Gets the historical data for the aggregated taker buy/sell volume ratio on a given exchange.

        Args:
            exchange: Exchange name (e.g., "Binance"). Defaults to "Binance".
                            Check the 'support-exchange-pair' API for supported exchanges.
            symbol: Trading pair (e.g., "BTCUSDT"). Defaults to "BTCUSDT".
                          Check the 'support-exchange-pair' API for supported pairs.
            interval: Data time interval ("1m", "3m", "5m", "15m", "30m", "1h", "4h", "6h", "8h", "12h", "1d", "1w").
                            Defaults to "1h".
            limit: Number of data points to return. Defaults to 500.
            startTime: Start time (Unix timestamp in seconds). Defaults to None.
            endTime: End time (Unix timestamp in seconds). Defaults to None.

        Returns:
            A list of historical aggregated taker buy/sell volume ratio data.
            Each element includes longShortRatio and time(createTime).
        """
        params: Dict[str, Union[str, int]] = {
            "exchange": exchange,
            "symbol": symbol,
            "interval": interval,
            "limit": limit,
        }
        if startTime is not None:
            params["startTime"] = startTime
        if endTime is not None:
            params["endTime"] = endTime

        response = self._request(
            "GET", "/api/futures/aggregatedTakerBuySellVolumeRatio/history", params
        )
        return cast(List[AggregatedTakerBuySellRatioData], response["data"])

    def get_aggregated_taker_buy_sell_volume_history(
        self,
        exchanges: str = "Binance",
        symbol: str = "BTC",
        interval: str = "1h",
        limit: int = 500,
        startTime: Optional[int] = None,
        endTime: Optional[int] = None,
    ) -> List[AggregatedTakerBuySellVolumeData]:
        """Gets the historical data for the aggregated taker buy/sell volume on specified exchanges.

        Args:
            exchanges: Exchange names (comma-separated allowed, e.g., "Binance,OKX"). Defaults to "Binance".
                             Check the 'support-exchange-pair' API for supported exchanges.
            symbol: Currency symbol (e.g., "BTC"). Defaults to "BTC".
                          Check the 'support-exchange-pair' API for supported symbols.
            interval: Data time interval ("1m", "3m", "5m", "15m", "30m", "1h", "4h", "6h", "8h", "12h", "1d", "1w").
                            Defaults to "1h".
            limit: Number of data points to return. Defaults to 500.
            startTime: Start time (Unix timestamp in seconds). Defaults to None.
            endTime: End time (Unix timestamp in seconds). Defaults to None.

        Returns:
            A list of historical aggregated taker buy/sell volume data.
            Each element includes buy, sell, time.
        """
        params: Dict[str, Union[str, int]] = {
            "exchanges": exchanges,
            "symbol": symbol,
            "interval": interval,
            "limit": limit,
        }
        if startTime is not None:
            params["startTime"] = startTime
        if endTime is not None:
            params["endTime"] = endTime

        response = self._request(
            "GET", "/api/futures/aggregatedTakerBuySellVolume/history", params
        )
        return cast(List[AggregatedTakerBuySellVolumeData], response["data"])

    def get_taker_buy_sell_ratio_history(
        self,
        exchange: str = "Binance",
        symbol: str = "BTCUSDT",
        interval: str = "1d",
        limit: int = 100,
    ) -> List[TakerBuySellVolumeData]:
        """Gets the historical data for the taker buy/sell volume on a given exchange.

        Args:
            exchange: Exchange name (e.g., "Binance"). Defaults to "Binance".
                            Check the 'support-exchange-pair' API for supported exchanges.
            symbol: Trading pair (e.g., "BTCUSDT"). Defaults to "BTCUSDT".
                          Check the 'support-exchange-pair' API for supported pairs.
            interval: Data time interval ("1m", "3m", "5m", "15m", "30m", "1h", "4h", "6h", "8h", "12h", "1d", "1w").
                            Defaults to "1d".
            limit: Number of data points to return. Defaults to 100.

        Returns:
            A list of historical taker buy/sell volume data.
            Each element includes buy, sell, time(createTime).
        """
        params: Dict[str, Union[str, int]] = {
            "exchange": exchange,
            "symbol": symbol,
            "interval": interval,
            "limit": limit,
        }

        response = self._request(
            "GET", "/api/futures/takerBuySellVolume/history", params
        )
        return cast(List[TakerBuySellVolumeData], response["data"])

    def get_exchange_taker_buy_sell_ratio(
        self, symbol: str = "BTC", range: str = "1h"
    ) -> ExchangeTakerBuySellRatioData:
        """Gets the taker buy/sell volume ratio (aggregated and detailed) per exchange.

        Args:
            symbol: Currency symbol (e.g., "BTC"). Defaults to "BTC".
                          Check the 'support-coins' API for supported coins.
            range: Data range ("5m", "15m", "30m", "1h", "4h", "12h", "24h"). Defaults to "1h".

        Returns:
            Exchange taker buy/sell volume ratio data.
            Includes overall ratio and volume, and a detailed list for each exchange.
        """
        params: Dict[str, str] = {"symbol": symbol, "range": range}

        response = self._request(
            "GET", "/api/futures/takerBuySellVolume/exchange-list", params
        )
        return cast(ExchangeTakerBuySellRatioData, response["data"])

    def get_hyperliquid_whale_position(self) -> List[HyperliquidWhalePositionData]:
        """Gets whale position data on Hyperliquid with values exceeding $1M.

        Note: This API requires Startup Edition or higher account level.

        Args:
            None

        Returns:
            A list of whale position data on Hyperliquid.
            Each element includes details like user address, symbol, position size, price, leverage,
            margin, PnL, fees, timestamp, etc.
        """
        response = self._request("GET", "/api/hyperliquid/whale-position")
        return cast(List[HyperliquidWhalePositionData], response["data"])

    def get_hyperliquid_whale_alert(self) -> List[HyperliquidWhaleAlertData]:
        """Gets real-time whale alerts (positions > $1M) on Hyperliquid.

        Note: This API requires Startup Edition or higher account level.

        Args:
            None

        Returns:
            A list of whale alert data on Hyperliquid.
            Each element includes details like user address, symbol, position size, price, position action,
            timestamp, etc.
        """
        response = self._request("GET", "/api/hyperliquid/whale-alert")
        return cast(List[HyperliquidWhaleAlertData], response["data"])

    # Global Information Methods

    def get_coins_markets(
        self, exchanges: str = "Binance,Okx", pageNum: int = 1, pageSize: int = 10
    ) -> List[CoinMarketData]:
        """Gets performance-related information for all available coins.

        Note: This API requires Professional Edition or higher account level.

        Args:
            exchanges: Exchange names. Comma-separated for multiple.
                                       Defaults to "Binance,Okx".
                                       Supported exchanges can be checked via 'support-exchange-pair' API.
            pageNum: Page number. Defaults to 1.
            pageSize: Page size. Defaults to 10.

        Returns:
            A list of market performance data per coin.
            Includes details like price, market cap, OI, volume, price change rates, LS ratio, liquidation amount, etc.
        """
        params: Dict[str, Union[str, int]] = {
            "exchanges": exchanges,
            "pageNum": pageNum,
            "pageSize": pageSize,
        }
        response = self._request("GET", "/api/futures/coins-markets", params)
        return cast(List[CoinMarketData], response["data"])

    def get_pairs_markets(self, symbol: str = "BTC") -> List[PairMarketData]:
        """Gets performance-related information for all trading pairs related to the specified coin symbol.

        Args:
            symbol: Coin symbol (e.g., "BTC").

        Returns:
            A list of market performance data per trading pair.
            Each element includes details like contract ID, exchange name, price, OI, volume, funding rate, etc.
        """
        params: Dict[str, str] = {"symbol": symbol}
        response = self._request("GET", "/api/futures/pairs-markets", params)
        return cast(List[PairMarketData], response["data"]["data"])

    def get_coins_price_change(self) -> List[CoinPriceChangeData]:
        """Gets information about price change rates and price amplitude rates for all coins.

        Note: This API requires Standard Edition or higher account level.

        Args:
            None

        Returns:
            A list of price change data per coin.
            Includes current price, price change rates for various intervals, and price amplitude rates.
        """
        response = self._request("GET", "/api/futures/coins-price-change")
        return cast(List[CoinPriceChangeData], response["data"])

    # Orderbook Related Methods

    def get_orderbook_bid_ask_range(
        self,
        symbol: str = "BTCUSDT",  # Updated default
        exchange: str = "Binance",
        interval: str = "1d",
        limit: int = 1000,
        startTime: Optional[int] = None,
        endTime: Optional[int] = None,
        range: str = "1",
    ) -> List[OrderbookHistoryData]:
        """Gets the historical data for bids and asks within a specified price range (±range) in the order book.
        (Example: https://www.coinglass.com/pro/depth-delta)

        Args:
            symbol: Trading pair (e.g., "BTCUSDT").
            exchange: Exchange name (e.g., "Binance").
            interval: Data interval ("1m", "3m", "5m", "15m", "30m", "1h", "4h", "6h", "8h", "12h", "1d", "1w").
                                    Defaults to "1d".
            limit: Number of data points to return. Defaults to 1000, max 4500.
            startTime: Start time (Unix timestamp, seconds).
            endTime: End time (Unix timestamp, seconds).
            range: Price depth (%) (e.g., "0.25", "1", "10"). Defaults to "1".

        Returns:
            A list of order book history data for the specified range.
            Each element includes the total USD value and quantity of bids and asks within the range at the specified time.
        """
        params: Dict[str, Union[str, int]] = {
            "symbol": symbol,
            "exchange": exchange,
            "interval": interval,
            "limit": limit,
            "range": range,
        }
        if startTime is not None:
            params["startTime"] = startTime
        if endTime is not None:
            params["endTime"] = endTime

        response = self._request("GET", "/api/futures/orderbook/history", params)
        return cast(List[OrderbookHistoryData], response["data"])

    def get_aggregated_orderbook_bid_ask_range(
        self,
        exchanges: str = "Binance",
        symbol: str = "BTC",
        interval: str = "h1",
        limit: int = 500,
        startTime: Optional[int] = None,
        endTime: Optional[int] = None,
        range: str = "1",
    ) -> List[OrderbookHistoryData]:
        """Gets the historical data for aggregated bids and asks within a specified price range (±range) in the order book.
        (Example: https://www.coinglass.com/pro/depth-delta)

        Args:
            exchanges: Exchange names (comma-separated, e.g., "Binance,OKX,Bybit"). Defaults to "Binance".
            symbol: Currency symbol (e.g., "BTC").
            interval: Data interval ("1m", "3m", "5m", "15m", "30m", "1h", "4h", "6h", "8h", "12h", "1d", "1w").
                                    Defaults to "h1". # Note: API might expect 'h1' specifically here.
            limit: Number of data points to return. Defaults to 500, max 4500.
            startTime: Start time (Unix timestamp, seconds).
            endTime: End time (Unix timestamp, seconds).
            range: Price depth (%) (e.g., "0.25", "1", "10"). Defaults to "1".

        Returns:
            A list of order book history data for the specified range.
            Each element includes the total USD value and quantity of bids and asks within the range at the specified time.
        """
        params: Dict[str, Union[str, int]] = {
            "exchanges": exchanges,
            "symbol": symbol,
            "interval": interval,
            "limit": limit,
            "range": range,
        }
        if startTime is not None:
            params["startTime"] = startTime
        if endTime is not None:
            params["endTime"] = endTime

        response = self._request(
            "GET", "/api/futures/orderbook/aggregated-history", params
        )
        return cast(List[OrderbookHistoryData], response["data"])

    # Indicator Related Methods

    def get_rsi_list(self) -> List[RsiData]:
        """Gets RSI (Relative Strength Index) values for multiple cryptocurrencies at different time frames.

        Note: This API requires Standard Edition or higher account level.

        Args:
            None

        Returns:
            A list of RSI data per coin.
            Each element includes the symbol, RSI values for various time frames, price change rates, and current price.
        """
        response = self._request("GET", "/api/futures/rsi/list")
        return cast(List[RsiData], response["data"])
