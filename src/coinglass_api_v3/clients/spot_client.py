"""
Coinglass Spot Market Client
==========================

This module provides access to spot market related features of the Coinglass API.
"""

from typing import Dict, List, Union, Optional, cast
from .base_client import BaseClient
from ..models import (
    ExchangePair,
    SpotTakerBuySellData,
    SpotOrderbookHistoryData,
    CoinMarketData,
    SpotPairMarketData,
    CoinbasePremiumIndexData,
    BitfinexMarginLongShortData,
)


class SpotClient(BaseClient):
    """Client providing access to spot market related endpoints."""

    # General Information Methods

    def get_supported_coins(self) -> List[str]:
        """Gets the list of supported currencies.

        Returns:
            A list of supported currency symbols.
        """
        response = self._request("GET", "/api/spot/supported-coins")
        return cast(List[str], response["data"])

    def get_supported_exchange_pairs(self) -> Dict[str, List[ExchangePair]]:
        """Gets the list of supported exchanges and trading pairs.

        Returns:
            A dictionary mapping exchange names to lists of trading pairs.
        """
        response = self._request("GET", "/api/spot/supported-exchange-pairs")
        return cast(Dict[str, List[ExchangePair]], response["data"])

    # Taker Buy/Sell Related Methods

    def get_taker_buy_sell_history(
        self,
        symbol: str = "BTCUSDT",
        exchange: str = "Binance",
        interval: str = "h1",
        limit: int = 1000,
        startTime: Optional[int] = None,
        endTime: Optional[int] = None,
    ) -> List[SpotTakerBuySellData]:
        """Gets the historical data for spot market taker buy/sell volume.

        Args:
            symbol: Trading pair (e.g., "BTCUSDT").
            exchange: Exchange name (e.g., "Binance").
            interval: Data time interval (e.g., "1m", "3m", ..., "1d", "1w").
            limit: Number of data points to return (default: 1000, max: 4500).
            startTime: Start timestamp (Unix seconds, optional).
            endTime: End timestamp (Unix seconds, optional).

        Returns:
            A list of spot market taker buy/sell history data.
        """
        params: Dict[str, Union[str, int]] = {
            "symbol": symbol,
            "exchange": exchange,
            "interval": interval,
            "limit": limit,
        }
        if startTime is not None:
            params["startTime"] = startTime
        if endTime is not None:
            params["endTime"] = endTime

        response = self._request("GET", "/api/spot/takerBuySellVolume/history", params)
        return cast(List[SpotTakerBuySellData], response["data"])

    def get_aggregated_taker_buy_sell_history(
        self,
        exchanges: str = "Binance",
        symbol: str = "BTC",
        interval: str = "h1",
        limit: int = 1000,
        startTime: Optional[int] = None,
        endTime: Optional[int] = None,
        unit: Optional[str] = None,
    ) -> List[SpotTakerBuySellData]:
        """Gets the aggregated historical data for spot market taker buy/sell volume.

        Args:
            exchanges: Exchange names (comma-separated, e.g., "Binance,OKX").
            symbol: Currency symbol (e.g., "BTC").
            interval: Data time interval (e.g., "1m", "3m", ..., "1d", "1w").
            limit: Number of data points to return (default: 1000, max: 4500).
            startTime: Start timestamp (Unix seconds, optional).
            endTime: End timestamp (Unix seconds, optional).
            unit: Unit ('coin' or 'usd', optional).

        Returns:
            A list of aggregated spot market taker buy/sell history data.
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
        if unit is not None:
            params["unit"] = unit

        response = self._request(
            "GET", "/api/spot/aggregatedTakerBuySellVolume/history", params
        )
        return cast(List[SpotTakerBuySellData], response["data"])

    # Orderbook Related Methods

    def get_orderbook_history(
        self,
        exchange: str = "Binance",
        symbol: str = "BTCUSDT",
        interval: str = "1d",
        limit: int = 1000,
        startTime: Optional[int] = None,
        endTime: Optional[int] = None,
        range: str = "1",
    ) -> List[SpotOrderbookHistoryData]:
        """Gets the spot market order book history data for the specified range.

        Args:
            exchange: Exchange name (e.g., "Binance").
            symbol: Trading pair (e.g., "BTCUSDT").
            interval: Data time interval (e.g., "1m", "3m", ..., "1d", "1w").
            limit: Number of data points to return (default: 1000, max: 4500).
            startTime: Start timestamp (Unix seconds, optional).
            endTime: End timestamp (Unix seconds, optional).
            range: Depth range (%) (e.g., "0.25", "0.5", ..., "10").

        Returns:
            A list of order book history data.
        """
        params: Dict[str, Union[str, int]] = {
            "exchange": exchange,
            "symbol": symbol,
            "interval": interval,
            "range": range,
        }
        params["limit"] = limit
        if startTime is not None:
            params["startTime"] = startTime
        if endTime is not None:
            params["endTime"] = endTime

        response = self._request("GET", "/api/spot/orderbook/history", params)
        return cast(List[SpotOrderbookHistoryData], response["data"])

    def get_aggregated_orderbook_history(
        self,
        exchanges: str = "Binance",
        symbol: str = "BTC",
        interval: str = "h1",
        limit: int = 500,
        startTime: Optional[int] = None,
        endTime: Optional[int] = None,
        range: str = "1",
    ) -> List[SpotOrderbookHistoryData]:
        """Gets the aggregated spot market order book history data for the specified range.

        Args:
            exchanges: Exchange names (comma-separated, e.g., "Binance,OKX").
            symbol: Currency symbol (e.g., "BTC").
            interval: Data time interval (e.g., "1m", "3m", ..., "1d", "1w").
            limit: Number of data points to return (default: 1000, max: 4500).
            startTime: Start timestamp (Unix seconds, optional).
            endTime: End timestamp (Unix seconds, optional).
            range: Depth range (%) (e.g., "0.25", "0.5", ..., "10").

        Returns:
            A list of aggregated order book history data.
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
            "GET", "/api/spot/orderbook/aggregated-history", params
        )
        return cast(List[SpotOrderbookHistoryData], response["data"])

    # Global Information Methods

    def get_coins_markets(
        self, pageNum: int = 1, pageSize: int = 10
    ) -> List[CoinMarketData]:
        """Gets performance-related information for all available coins.

        **Note:** Requires Standard Edition account level or above.

        Args:
            pageNum: Page number (default: 1).
            pageSize: Page size (default: 10).

        Returns:
            A list of market performance data per coin.
        """
        params: Dict[str, int] = {"pageNum": pageNum, "pageSize": pageSize}
        response = self._request("GET", "/api/spot/coins-markets", params)
        return cast(List[CoinMarketData], response["data"])

    def get_pairs_markets(
        self, symbol: str = "BTC"
    ) -> List[Dict[str, Union[str, float, int]]]:
        """Gets performance-related information for all available trading pairs for the specified coin.

        Args:
            symbol: Coin symbol (e.g., "BTC").

        Returns:
            A list of market performance data per trading pair.
        """
        params: Dict[str, str] = {"symbol": symbol}
        response = self._request("GET", "/api/spot/pairs-markets", params)
        return cast(List[SpotPairMarketData], response["data"])

    # Indicator Related Methods

    def get_coinbase_premium_index(
        self,
        interval: str = "1d",
        limit: int = 1000,
        startTime: Optional[int] = None,
        endTime: Optional[int] = None,
    ) -> List[CoinbasePremiumIndexData]:
        """Gets the Coinbase Premium Index history data.

        Args:
            interval: Data time interval (e.g., "1m", "3m", ..., "1d", "1w").
            limit: Number of data points to return (default: 1000, max: 4500).
            startTime: Start timestamp (Unix seconds, optional).
            endTime: End timestamp (Unix seconds, optional).

        Returns:
            A list of Coinbase Premium Index history data.
        """
        params: Dict[str, Union[str, int]] = {"interval": interval, "limit": limit}
        if startTime is not None:
            params["startTime"] = startTime
        if endTime is not None:
            params["endTime"] = endTime

        response = self._request("GET", "/api/coinbase-premium-index", params)
        return cast(List[CoinbasePremiumIndexData], response["data"])

    def get_bitfinex_margin_long_short(
        self,
        symbol: str = "BTC",
        interval: str = "1d",
        limit: int = 1000,
        startTime: Optional[int] = None,
        endTime: Optional[int] = None,
    ) -> List[BitfinexMarginLongShortData]:
        """Gets the Bitfinex margin long/short ratio history data.

        Args:
            symbol: Coin symbol (e.g., "BTC").
            interval: Data time interval (e.g., "1m", "3m", ..., "1d", "1w").
            limit: Number of data points to return (default: 1000, max: 4500).
            startTime: Start timestamp (Unix seconds, optional).
            endTime: End timestamp (Unix seconds, optional).

        Returns:
            A list of Bitfinex margin long/short history data.
        """
        params: Dict[str, Union[str, int]] = {
            "symbol": symbol,
            "interval": interval,
            "limit": limit,
        }
        if startTime is not None:
            params["startTime"] = startTime
        if endTime is not None:
            params["endTime"] = endTime

        response = self._request("GET", "/api/bitfinex-margin-long-short", params)
        return cast(List[BitfinexMarginLongShortData], response["data"])
