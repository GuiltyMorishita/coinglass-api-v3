"""
Coinglass On-chain Data Client
=============================

This module provides access to on-chain data related features of the Coinglass API.
"""

from typing import Dict, List, Union, Optional, cast, Any
from .base_client import BaseClient
from ..models import ExchangeOnchainTransferData


class OnchainClient(BaseClient):
    """
    Provides methods to access on-chain related endpoints of the Coinglass API.
    """

    def get_exchange_onchain_transfers(
        self,
        symbol: str = "ETH",
        start_time: Optional[int] = None,
        min_usd: Optional[float] = None,
        page_num: int = 1,
        page_size: int = 20,
    ) -> List[ExchangeOnchainTransferData]:
        """
        Retrieves ERC-20 on-chain transfer data for exchanges.

        Args:
            symbol: Currency symbol (default: "ETH").
            start_time: Start time (Unix timestamp in milliseconds).
            min_usd: Filter by minimum transfer amount in USD.
            page_num: Page number (starts from 1).
            page_size: Number of items per page (max 100).

        Returns:
            A list of exchange on-chain transfer data.
        """
        params: Dict[str, Union[str, int, float, None]] = {
            "symbol": symbol,
            "minUsd": min_usd,
            "pageNum": page_num,
            "pageSize": page_size,
        }

        if start_time:
            params["startTime"] = start_time

        # page_size limit is 100
        if page_size > 100:
            page_size = 100
            params["pageSize"] = page_size

        response = self._request("GET", "/api/exchange/chain/tx/list", params)

        # Map the raw data to the ExchangeOnchainTransferData model
        raw_data = response.get("data", [])
        transfer_data: List[ExchangeOnchainTransferData] = []
        for item in raw_data:
            # Rename 'from' to 'from_' to avoid keyword conflict
            item["from_"] = item.pop("from")
            transfer_data.append(cast(ExchangeOnchainTransferData, item))

        return transfer_data
