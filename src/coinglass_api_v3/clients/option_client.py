"""
Coinglass Option Client
======================

This module provides access to options trading related features of the Coinglass API.
"""

from typing import Dict, Any, List, cast, Union
from .base_client import BaseClient
from ..models import (
    OptionMaxPainData,
    OptionInfoData,
    OptionExchangeOIVolHistoryData,
)


class OptionClient(BaseClient):
    """Client providing access to option-related endpoints."""

    def get_option_max_pain(
        self, symbol: str = "BTC", exName: str = "Deribit"
    ) -> List[OptionMaxPainData]:
        """Gets the option Max Pain data for the specified symbol and exchange.

        Args:
            symbol: Currency symbol (e.g., "BTC", "ETH").
            exName: Exchange name (e.g., "Deribit", "Binance", "Okx").

        Returns:
            A list of option Max Pain data.
        """
        params: Dict[str, str] = {"symbol": symbol, "exName": exName}
        response = self._request("GET", "/api/option/max-pain", params)
        return cast(List[OptionMaxPainData], response["data"])

    def get_option_info(self, symbol: str = "BTC") -> List[OptionInfoData]:
        """Gets general option information for the specified symbol.
        Includes aggregated data for each exchange and "All".

        Args:
            symbol: Currency symbol (e.g., "BTC").

        Returns:
            A list of option information data ([OptionInfoData]).
        """
        params: Dict[str, str] = {"symbol": symbol}
        response = self._request("GET", "/api/option/info", params)
        return cast(List[OptionInfoData], response["data"])

    def get_exchange_open_interest_history(
        self,
        symbol: str = "BTC",
        currency: str = "USD",
        range: str = "all",
    ) -> OptionExchangeOIVolHistoryData:
        """Gets the historical data for option open interest by exchange.

        Args:
            symbol: Currency symbol (e.g., "BTC").
            currency: Currency for the returned data ("USD" or base currency "BTC"/"ETH"). Defaults to "USD".
            range: Time range ("1h", "4h", "12h", "all"). Defaults to "all".

        Returns:
            A dictionary containing historical open interest data by exchange (OptionExchangeOIVolHistoryData).
        """
        params: Dict[str, Any] = {
            "symbol": symbol,
            "currency": currency,
        }
        if range is not None:
            params["range"] = range

        response = self._request("GET", "/api/option/v2/exchange-oi-history", params)
        return cast(OptionExchangeOIVolHistoryData, response["data"])

    def get_exchange_volume_history(
        self, symbol: str = "BTC", currency: str = "USD"
    ) -> OptionExchangeOIVolHistoryData:
        """Gets the historical data for option volume by exchange.

        Args:
            symbol: Currency symbol (e.g., "BTC").
            currency: Currency for the returned data ("USD" or base currency "BTC", "ETH"). Defaults to "USD".

        Returns:
            A dictionary containing historical volume data by exchange (OptionExchangeOIVolHistoryData).
        """
        params: Dict[str, Union[str, int]] = {
            "symbol": symbol,
            "currency": currency,
        }
        response = self._request("GET", "/api/option/exchange-vol-history", params)
        return cast(OptionExchangeOIVolHistoryData, response["data"])
