"""
Orderbook Client Module.

This module provides access to order book related features of the Coinglass API.
"""

from typing import Dict, List, Union, Optional, cast
from .base_client import BaseClient
from ..models import OrderbookHistoryData, LargeLimitOrderData


class OrderbookClient(BaseClient):
    """
    Provides methods to access order book related endpoints of the Coinglass API.
    """

    def get_orderbook_heatmap(
        self,
        exName: str = "Binance",
        symbol: str = "BTCUSDT",
        type: str = "futures",
        interval: str = "1h",
        limit: int = 10,
        startTime: Optional[int] = None,
        endTime: Optional[int] = None,
    ) -> List[OrderbookHistoryData]:
        """
        Retrieves historical data of the order book heatmap for futures or spot trading.

        Required Account Level: Standard Edition and Above.

        Args:
            exName: Exchange name (e.g., "Binance", "OKX", "Coinbase").
            symbol: Trading pair (e.g., "BTCUSDT", "ETHUSDT").
            type: Market type ("futures" or "spot").
            interval: Time interval ("1h", "4h", "8h", "12h", "1d").
            limit: Number of data points to return.
            startTime: Start time in seconds (Unix timestamp).
            endTime: End time in seconds (Unix timestamp).

        Returns:
            A list of historical order book entries.
        """
        params: Dict[str, Union[str, int]] = {
            "exName": exName,
            "symbol": symbol,
            "type": type,
            "interval": interval,
            "limit": limit,
        }
        if startTime is not None:
            params["startTime"] = startTime
        if endTime is not None:
            params["endTime"] = endTime

        response = self._request("GET", "/api/orderbook/history", params)
        return cast(List[OrderbookHistoryData], response["data"])

    def get_large_orderbook(
        self, exName: str = "Binance", symbol: str = "BTCUSDT", type: str = "futures"
    ) -> List[LargeLimitOrderData]:
        """
        Retrieves large open orders from the current order book for futures or spot trading.

        Required Account Level: Standard Edition and Above.

        Args:
            exName: Exchange name (e.g., "Binance", "OKX", "Coinbase").
            symbol: Trading pair (e.g., "BTCUSDT").
            type: Market type ("futures" or "spot").

        Returns:
            A list of current large limit orders.
        """
        params: Dict[str, str] = {"exName": exName, "symbol": symbol, "type": type}
        response = self._request("GET", "/api/orderbook/large-limit-order", params)
        return cast(List[LargeLimitOrderData], response["data"])

    def get_large_orderbook_history(
        self,
        exName: str = "Binance",
        symbol: str = "BTCUSDT",
        type: str = "futures",
        startTime: Optional[int] = None,
        endTime: Optional[int] = None,
        state: int = 2,
    ) -> List[LargeLimitOrderData]:
        """
        Retrieves completed historical large orders from the order book for futures or spot trading.

        Required Account Level: Standard Edition and Above.
        Data is limited to the last 7 days.

        Args:
            exName: Exchange name (e.g., "Binance", "OKX", "Coinbase").
            symbol: Trading pair (e.g., "BTCUSDT").
            type: Market type ("futures" or "spot").
            startTime: Start time in seconds (Unix timestamp). Optional.
            endTime: End time in seconds (Unix timestamp). Optional.
            state: Order state (2-Finish, 3-Revoke). Defaults to 2.

        Returns:
            A list of historical large limit orders.
        """
        params: Dict[str, Union[str, int]] = {
            "exName": exName,
            "symbol": symbol,
            "type": type,
            "state": state,
        }
        if startTime is not None:
            params["startTime"] = startTime
        if endTime is not None:
            params["endTime"] = endTime

        response = self._request(
            "GET", "/api/orderbook/large-limit-order-history", params
        )
        return cast(List[LargeLimitOrderData], response["data"])
