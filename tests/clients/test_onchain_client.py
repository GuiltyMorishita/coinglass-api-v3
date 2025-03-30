"""Tests for the OnchainClient making live API calls."""

import os
import pytest
from typing import List, Dict, Any
from coinglass_api_v3.clients import OnchainClient
from coinglass_api_v3.models import ExchangeOnchainTransferData

# Skip tests if the API key environment variable is not set
API_KEY = os.environ.get("COINGLASS_API_KEY")
pytestmark = pytest.mark.skipif(
    not API_KEY,
    reason="COINGLASS_API_KEY environment variable not set. Skipping live API tests.",
)


@pytest.fixture
def onchain_client() -> OnchainClient:
    """Provides an instance of OnchainClient for testing with a live API key."""
    assert API_KEY is not None  # Should be skipped if None by pytestmark
    return OnchainClient(api_key=API_KEY)


def test_get_exchange_onchain_transfers(onchain_client: OnchainClient) -> None:
    """Tests the get_exchange_onchain_transfers method with a live API call."""
    # Call the method with test parameters likely to return some data
    symbol = "USDT"
    page_num = 1
    page_size = 5  # Keep page size small for live test

    result = onchain_client.get_exchange_onchain_transfers(
        symbol=symbol,
        page_num=page_num,
        page_size=page_size,
    )

    # Assert the result structure and types
    assert isinstance(result, list)
    if result:
        assert len(result) <= page_size
        # Check the structure and types of the first item
        first_item = result[0]
        assert isinstance(first_item, dict)
        # Verify all expected keys are present
        expected_keys = ExchangeOnchainTransferData.__annotations__.keys()
        assert all(key in first_item for key in expected_keys)

        # Verify types for some key fields
        assert isinstance(first_item["txHash"], str)
        assert isinstance(first_item["symbol"], str)
        assert isinstance(first_item["usd"], float)
        assert isinstance(first_item["amount"], float)
        assert isinstance(first_item["exName"], str)
        assert isinstance(first_item["side"], int)
        assert isinstance(first_item["from_"], str)  # Check the renamed key
        assert isinstance(first_item["to"], str)


def test_get_exchange_onchain_transfers_page_size_limit(
    onchain_client: OnchainClient,
) -> None:
    """Tests that requesting a large page_size does not cause an error (capping is internal)."""
    page_size = 150  # Larger than the API limit

    try:
        result = onchain_client.get_exchange_onchain_transfers(page_size=page_size)
        # Assert basic success structure if the call didn't raise an error
        assert isinstance(result, list)
        # The actual number of items returned should be <= 100 due to internal capping
        assert len(result) <= 100
    except Exception as e:
        pytest.fail(f"API call failed even with page_size capping: {e}")


def test_get_exchange_onchain_transfers_no_data_scenario(
    onchain_client: OnchainClient,
) -> None:
    """Tests the method with parameters likely to return no data."""
    # Use parameters that are unlikely to yield results (e.g., very high min_usd)
    result = onchain_client.get_exchange_onchain_transfers(
        symbol="BTC", min_usd=9999999999.0
    )
    # We expect a list, which might be empty
    assert isinstance(result, list)
