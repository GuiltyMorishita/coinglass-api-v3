"""
Tests for the OrderbookClient.
"""

import os
import pytest
from typing import TYPE_CHECKING

from coinglass_api_v3.clients import OrderbookClient
from coinglass_api_v3.models import OrderbookHistoryData, LargeLimitOrderData

if TYPE_CHECKING:
    from _pytest.monkeypatch import MonkeyPatch


@pytest.mark.skipif(
    not os.environ.get("COINGLASS_API_KEY"),
    reason="API key not found in environment variables",
)
class TestOrderbookClient:
    """Tests for the OrderbookClient class, performing live API calls."""

    @pytest.fixture(scope="class")
    def client(self) -> OrderbookClient:
        """Provides an instance of the OrderbookClient."""
        api_key = os.environ.get("COINGLASS_API_KEY")
        if not api_key:
            pytest.skip("API key not found in environment variables")
        return OrderbookClient(api_key)

    def test_get_orderbook_heatmap(self, client: OrderbookClient) -> None:
        """Test retrieving order book heatmap."""
        result = client.get_orderbook_heatmap()
        assert isinstance(result, list)
        assert len(result) > 0
        # Check if all items in the outer list are lists
        assert all(isinstance(item, list) for item in result)

        # Validate structure of the first item as a sample
        first_item = result[0]
        assert len(first_item) >= 3  # Should have timestamp, bids, asks
        assert isinstance(first_item[0], int)  # Timestamp
        assert isinstance(first_item[1], list)  # Bids
        assert isinstance(first_item[2], list)  # Asks

        # Validate structure of bids list if not empty
        if first_item[1]:
            first_bid = first_item[1][0]
            assert isinstance(first_bid, list)
            assert len(first_bid) == 2
            assert isinstance(first_bid[0], (int, float))  # Price
            assert isinstance(first_bid[1], (int, float))  # Volume

        # Validate structure of asks list if not empty
        if first_item[2]:
            first_ask = first_item[2][0]
            assert isinstance(first_ask, list)
            assert len(first_ask) == 2
            assert isinstance(first_ask[0], (int, float))  # Price
            assert isinstance(first_ask[1], (int, float))  # Volume

    def test_get_large_orderbook(self, client: OrderbookClient) -> None:
        """Test retrieving large limit orders."""
        result = client.get_large_orderbook()
        assert isinstance(result, list)
        # Ensure all items are non-None dictionaries
        assert all(item is not None and isinstance(item, dict) for item in result)
        # Validate structure if the list is not empty
        if result:
            first_item = result[0]
            assert "price" in first_item
            assert "side" in first_item
            assert "symbol" in first_item
            assert "volUsd" in first_item
            # Check for keys present in the actual response based on the error
            assert "baseAsset" in first_item
            assert "count" in first_item
            assert "currentAmount" in first_item
            assert "currentTime" in first_item
            assert "state" in first_item

    def test_get_large_orderbook_history(self, client: OrderbookClient) -> None:
        """Test retrieving large limit order history."""
        result = client.get_large_orderbook_history()
        assert isinstance(result, list)
        # Ensure all items are non-None dictionaries
        assert all(item is not None and isinstance(item, dict) for item in result)
        # Validate structure if the list is not empty
        if result:
            first_item = result[0]
            assert "price" in first_item
            assert "side" in first_item
            assert "symbol" in first_item
            assert "volUsd" in first_item
            # Check for keys present in the actual response based on the error
            assert "baseAsset" in first_item
            assert "count" in first_item
            assert "currentAmount" in first_item
            assert "currentTime" in first_item
            assert "startTime" in first_item
            assert "endTime" in first_item
            assert "state" in first_item
            assert first_item["state"] == 2
            assert "id" in first_item
            assert "exName" in first_item
            assert "quoteAsset" in first_item
            assert "startAmount" in first_item
            assert "startUsd" in first_item
            assert "currentUsd" in first_item
            assert "vol" in first_item
