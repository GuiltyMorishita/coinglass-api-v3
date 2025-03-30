"""
Ethereum ETF Client Module.

This module provides access to Ethereum ETF related features of the Coinglass API.
"""

from typing import List, cast
from .base_client import BaseClient
from ..models import (
    EthereumETFNetAssetsHistoryData,
    EthereumETFInfoData,
    EthereumETFFlowHistoryData,
)


class EthereumETFClient(BaseClient):
    """
    Provides methods to access Ethereum ETF related endpoints of the Coinglass API.
    """

    def get_etf_net_assets_history(
        self,
    ) -> List[EthereumETFNetAssetsHistoryData]:
        """
        Retrieves the historical net assets data for Ethereum ETFs.

        Returns:
            A list of historical net assets data for Ethereum ETFs.
        """
        response = self._request("GET", "/api/ethereum/etf/netAssets/history")
        return cast(List[EthereumETFNetAssetsHistoryData], response["data"])

    def get_etf_list(self) -> List[EthereumETFInfoData]:
        """
        Retrieves a list of key status information for Ethereum ETFs.

        Returns:
            A list of detailed information for Ethereum ETFs.
        """
        response = self._request("GET", "/api/ethereum/etf/list")
        return cast(List[EthereumETFInfoData], response["data"])

    def get_etf_flows_history(self) -> List[EthereumETFFlowHistoryData]:
        """
        Retrieves a list of key status information regarding the history of ETF flows.

        Returns:
            A list of historical flow data for Ethereum ETFs.
        """
        response = self._request("GET", "/api/ethereum/etf/flow-history")
        return cast(List[EthereumETFFlowHistoryData], response["data"])
