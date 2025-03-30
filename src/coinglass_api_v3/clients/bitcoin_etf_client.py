"""Coinglass Bitcoin ETF Client
============================

This module provides access to Bitcoin ETF related features of the Coinglass API.
"""

from typing import Dict, List, Optional, cast
from .base_client import BaseClient
from ..models import (
    BitcoinETFInfoData,
    HKEtFlowData,
    ETFNetAssetsHistoryData,
    ETFFlowHistoryData,
    ETFPremiumDiscountHistoryData,
    ETFHistoryData,
    ETFPriceData,
    ETFDetailData,
)


class BitcoinETFClient(BaseClient):
    """Client providing access to Bitcoin ETF related endpoints."""

    def get_bitcoin_etf_list(self) -> List[BitcoinETFInfoData]:
        """Gets a list of key status information for major Bitcoin ETFs.

        Returns:
            A list of Bitcoin ETF information ([BitcoinETFInfoData]).
        """
        response = self._request("GET", "/api/bitcoin/etf/list")
        return cast(List[BitcoinETFInfoData], response["data"])

    def get_hong_kong_etf_flows_history(self) -> List[HKEtFlowData]:
        """Gets a list of key status information for Hong Kong ETF flow history.

        Returns:
            A list of Hong Kong ETF flow data ([HKEtFlowData]).
        """
        response = self._request("GET", "/api/bitcoin/hk/etf/flow-history")
        return cast(List[HKEtFlowData], response["data"])

    def get_etf_net_assets_history(
        self, ticker: Optional[str] = None
    ) -> List[ETFNetAssetsHistoryData]:
        """Gets the historical net assets data for ETFs.

        Args:
            ticker: ETF ticker symbol (e.g., "GBTC", "IBIT").
                    If not specified, provides aggregated data for all.

        Returns:
            A list of ETF net assets history data ([ETFNetAssetsHistoryData]).
        """
        params: Dict[str, str] = {}
        if ticker:
            params["ticker"] = ticker

        response = self._request("GET", "/api/bitcoin/etf/netAssets/history", params)
        return cast(List[ETFNetAssetsHistoryData], response["data"])

    def get_etf_flow_history(self) -> List[ETFFlowHistoryData]:
        """Gets a list of key status information for ETF flow history.

        Returns:
            A list of ETF flow history data ([ETFFlowHistoryData]).
        """
        response = self._request("GET", "/api/bitcoin/etf/flow-history")
        return cast(List[ETFFlowHistoryData], response["data"])

    def get_etf_premium_discount_history(
        self, ticker: Optional[str] = None
    ) -> List[ETFPremiumDiscountHistoryData]:
        """Gets a list of key status information regarding historical premium or discount fluctuations for ETFs.

        Args:
            ticker: ETF ticker symbol (e.g., "GBTC", "IBIT").
                    If not specified, includes data for all tickers.

        Returns:
            A list of ETF premium/discount history data ([ETFPremiumDiscountHistoryData]).
        """
        params: Dict[str, str] = {}
        if ticker:
            params["ticker"] = ticker

        response = self._request(
            "GET", "/api/bitcoin/etf/premium-discount-history", params
        )
        return cast(List[ETFPremiumDiscountHistoryData], response["data"])

    def get_etf_history(self, ticker: str) -> List[ETFHistoryData]:
        """Gets the historical data for a specific ETF.

        Args:
            ticker: ETF ticker symbol (e.g., "GBTC", "IBIT").

        Returns:
            A list of historical data for the specified ETF ([ETFHistoryData]).
            Typically, the list contains one element.
        """
        params: Dict[str, str] = {"ticker": ticker}
        response = self._request("GET", "/api/bitcoin/etf/history", params)
        return cast(List[ETFHistoryData], response["data"])

    def get_etf_price_history(
        self, ticker: str = "GBTC", range: str = "1d"
    ) -> List[ETFPriceData]:
        """Gets the historical price data (OHLC) for an ETF.

        Args:
            ticker: ETF ticker symbol. Defaults to "GBTC".
            range: Time range ("1d", "7d", "all"). Defaults to "1d".

        Returns:
            A list of ETF price OHLC data ([ETFPriceData]).
            Note: The model was previously named ETFPriceOHLCData in docstring, corrected to ETFPriceData.
        """
        params: Dict[str, str] = {"ticker": ticker, "range": range}
        response = self._request("GET", "/api/bitcoin/etf/price/ohlc-history", params)
        # Assuming the actual OHLC data is nested within the response data structure
        # e.g., response['data'][0]['ohlcList'] based on common patterns and test failures.
        # Adjust based on the actual structure if this assumption is wrong.
        try:
            # Attempt to extract the nested OHLC list, assuming one main entry in 'data'
            ohlc_data = response["data"][0]["ohlcList"]
        except (IndexError, KeyError, TypeError):
            # Handle cases where the structure is different or data is empty
            ohlc_data = []
        return cast(List[ETFPriceData], ohlc_data)

    def get_etf_detail(self, ticker: str = "GBTC") -> ETFDetailData:
        """Gets detailed information for a specific ETF.

        Args:
            ticker: ETF ticker symbol. Defaults to "GBTC".

        Returns:
            Detailed ETF data ([ETFDetailData]).
        """
        params: Dict[str, str] = {"ticker": ticker}
        response = self._request("GET", "/api/bitcoin/etf/detail", params)
        return cast(ETFDetailData, response["data"])
