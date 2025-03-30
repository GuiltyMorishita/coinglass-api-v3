"""
Tests for the Coinglass OptionClient using live API calls.

Note: These tests require a valid API key set in the COINGLASS_API_KEY
environment variable or a .env file in the project root.
These tests will make actual calls to the Coinglass API.
"""

import os
import pytest
from typing import List, TYPE_CHECKING
from dotenv import load_dotenv

# Adjust the import path based on your project structure
from src.coinglass_api_v3.clients import OptionClient
from src.coinglass_api_v3.models import (
    OptionMaxPainData,
    OptionInfoData,
    OptionExchangeOIVolHistoryData,
)

if TYPE_CHECKING:
    from _pytest.fixtures import FixtureRequest

# Load environment variables from .env file
load_dotenv()


@pytest.fixture(scope="module")
def option_client() -> OptionClient:
    """Fixture to provide an instance of the OptionClient."""
    api_key = os.getenv("COINGLASS_API_KEY")
    if not api_key:
        pytest.skip(
            "API key not found. Set COINGLASS_API_KEY environment variable or in .env file."
        )
    # Ensure you pass the api_key correctly to your client constructor
    return OptionClient(api_key=api_key)  # Modified line


def test_get_option_max_pain_default(option_client: OptionClient) -> None:
    """Tests the get_option_max_pain method with default parameters."""
    result: List[OptionMaxPainData] = option_client.get_option_max_pain()
    assert isinstance(result, list)
    if result:
        # Check the structure of the first item if the list is not empty
        item = result[0]
        assert isinstance(item, dict)
        assert "maxPain" in item
        assert "callOi" in item
        assert "putOi" in item
        # Add more specific type checks if needed, e.g., assert isinstance(item['price'], float)


def test_get_option_max_pain_custom(option_client: OptionClient) -> None:
    """Tests the get_option_max_pain method with custom parameters."""
    result: List[OptionMaxPainData] = option_client.get_option_max_pain(
        symbol="ETH", exName="Binance"
    )
    assert isinstance(result, list)
    # Add similar structure checks as above if needed


def test_get_option_info_default(option_client: OptionClient) -> None:
    """Tests the get_option_info method with default parameters."""
    result: List[OptionInfoData] = option_client.get_option_info()
    assert isinstance(result, list)
    if result:
        item = result[0]
        assert isinstance(item, dict)
        assert "exchangeName" in item
        assert "volUsd" in item
        assert "openInterestUsd" in item
        # Removed assertion for pcRatio as it might not be present for 'All'
        # Removed assertions for optional fields not present for 'All'
        # assert "putVol" in item
        # assert "callVol" in item
        # assert "putOi" in item
        # assert "callOi" in item


def test_get_option_info_custom(option_client: OptionClient) -> None:
    """Tests the get_option_info method with a custom symbol."""
    result: List[OptionInfoData] = option_client.get_option_info(symbol="ETH")
    assert isinstance(result, list)
    # Add similar structure checks as above


def test_get_exchange_open_interest_history_default(
    option_client: OptionClient,
) -> None:
    """Tests the get_exchange_open_interest_history method with default parameters."""
    result: OptionExchangeOIVolHistoryData = (
        option_client.get_exchange_open_interest_history()
    )
    assert isinstance(result, dict)
    assert "dateList" in result
    assert "dataMap" in result
    assert "priceList" in result
    assert isinstance(result["dateList"], list)
    assert isinstance(result["dataMap"], dict)
    assert isinstance(result["priceList"], list)


@pytest.mark.parametrize(
    "symbol, currency, range_val",
    [
        ("ETH", "USD", "all"),
        ("BTC", "BTC", "1h"),
        ("BTC", "USD", "12h"),
    ],
)
def test_get_exchange_open_interest_history_custom(
    option_client: OptionClient, symbol: str, currency: str, range_val: str
) -> None:
    """Tests the get_exchange_open_interest_history method with custom parameters."""
    result: OptionExchangeOIVolHistoryData = (
        option_client.get_exchange_open_interest_history(
            symbol=symbol, currency=currency, range=range_val
        )
    )
    assert isinstance(result, dict)
    assert "dateList" in result
    assert "dataMap" in result
    assert "priceList" in result


def test_get_exchange_volume_history_default(option_client: OptionClient) -> None:
    """Tests the get_exchange_volume_history method with default parameters."""
    result: OptionExchangeOIVolHistoryData = option_client.get_exchange_volume_history()
    assert isinstance(result, dict)
    assert "dateList" in result
    assert "dataMap" in result
    assert "priceList" in result
    assert isinstance(result["dateList"], list)
    assert isinstance(result["dataMap"], dict)
    assert isinstance(result["priceList"], list)


@pytest.mark.parametrize("symbol, currency", [("ETH", "USD"), ("BTC", "BTC")])
def test_get_exchange_volume_history_custom(
    option_client: OptionClient, symbol: str, currency: str
) -> None:
    """Tests the get_exchange_volume_history method with custom parameters."""
    result: OptionExchangeOIVolHistoryData = option_client.get_exchange_volume_history(
        symbol=symbol, currency=currency
    )
    assert isinstance(result, dict)
    assert "dateList" in result
    assert "dataMap" in result
    assert "priceList" in result
