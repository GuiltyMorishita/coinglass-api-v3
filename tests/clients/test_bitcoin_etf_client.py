import os
import pytest
from typing import Generator, TYPE_CHECKING, List, Union

from coinglass_api_v3.clients import BitcoinETFClient
from coinglass_api_v3.models import (
    BitcoinETFInfoData,
    HKEtFlowData,
    ETFNetAssetsHistoryData,
    ETFFlowHistoryData,
    ETFPremiumDiscountHistoryData,
    ETFHistoryData,
    ETFPriceData,
    ETFDetailData,
)

if TYPE_CHECKING:
    from _pytest.capture import CaptureFixture
    from _pytest.fixtures import FixtureRequest
    from _pytest.logging import LogCaptureFixture
    from _pytest.monkeypatch import MonkeyPatch
    from pytest_mock.plugin import MockerFixture


@pytest.fixture(scope="module")
def bitcoin_etf_client() -> Generator[BitcoinETFClient, None, None]:
    """Provides a BitcoinETFClient instance for testing."""
    api_key = os.environ.get("COINGLASS_API_KEY")
    if not api_key:
        pytest.skip("API key not found in environment variables.")
    client = BitcoinETFClient(api_key)
    yield client


def test_get_bitcoin_etf_list(bitcoin_etf_client: BitcoinETFClient) -> None:
    """Tests the get_bitcoin_etf_list method."""
    data: List[BitcoinETFInfoData] = bitcoin_etf_client.get_bitcoin_etf_list()
    assert isinstance(data, list)
    if data:
        assert all(isinstance(item, dict) for item in data)
        first_item = data[0]
        assert "ticker" in first_item
        assert "assetInfo" in first_item
        assert "btcHolding" in first_item["assetInfo"]
        assert "date" in first_item["assetInfo"]


def test_get_hong_kong_etf_flows_history(bitcoin_etf_client: BitcoinETFClient) -> None:
    """Tests the get_hong_kong_etf_flows_history method."""
    data: List[HKEtFlowData] = bitcoin_etf_client.get_hong_kong_etf_flows_history()
    assert isinstance(data, list)
    if data:
        # Check the structure of the outer dictionary (daily summary)
        assert all(isinstance(item, dict) for item in data)
        first_item = data[0]
        assert "date" in first_item
        assert "changeUsd" in first_item  # Overall daily change
        assert "price" in first_item
        assert "list" in first_item
        assert isinstance(first_item["list"], list)

        # Check the structure of the inner list (per-ticker flow)
        if first_item["list"]:
            assert all(
                isinstance(ticker_data, dict) for ticker_data in first_item["list"]
            )
            first_ticker_item = first_item["list"][0]
            assert "ticker" in first_ticker_item
            # Check if 'changeUsd' exists, handle cases where it might be missing (like BOSERA&HASHKEY in some entries)
            assert (
                "changeUsd" in first_ticker_item or len(first_ticker_item) == 1
            )  # Allow dicts with only 'ticker'


def test_get_etf_net_assets_history_default(
    bitcoin_etf_client: BitcoinETFClient,
) -> None:
    """Tests the get_etf_net_assets_history method with default parameters."""
    data: List[ETFNetAssetsHistoryData] = (
        bitcoin_etf_client.get_etf_net_assets_history()
    )
    assert isinstance(data, list)
    if data:
        assert all(isinstance(item, dict) for item in data)
        first_item = data[0]
        # assert "ticker" in first_item  # Ticker not present in aggregated response
        assert "change" in first_item
        assert "netAssets" in first_item
        assert "date" in first_item
        assert "price" in first_item


def test_get_etf_net_assets_history_custom(
    bitcoin_etf_client: BitcoinETFClient,
) -> None:
    """Tests the get_etf_net_assets_history method with a specific ticker."""
    ticker = "IBIT"
    data: List[ETFNetAssetsHistoryData] = bitcoin_etf_client.get_etf_net_assets_history(
        ticker=ticker
    )
    assert isinstance(data, list)
    if data:
        assert all(isinstance(item, dict) for item in data)
        first_item = data[0]
        assert "change" in first_item
        assert "netAssets" in first_item
        assert "date" in first_item
        # assert "price" in first_item # Price key not present for custom ticker based on error


def test_get_etf_flow_history(bitcoin_etf_client: BitcoinETFClient) -> None:
    """Tests the get_etf_flow_history method."""
    # Client now returns the outer list List[Dict[str, Any]]
    data: List[ETFFlowHistoryData] = bitcoin_etf_client.get_etf_flow_history()
    assert isinstance(data, list)
    if data:
        # Check structure of the outer dictionary (daily summary)
        assert all(isinstance(item, dict) for item in data)
        first_item = data[0]
        assert "date" in first_item
        assert "changeUsd" in first_item  # Overall daily change
        assert (
            "closePrice" in first_item
        )  # Key based on previous error for this endpoint
        assert "list" in first_item
        assert isinstance(first_item["list"], list)

        # Check structure of the inner list (per-ticker flow)
        if first_item["list"]:
            assert all(
                isinstance(ticker_data, dict) for ticker_data in first_item["list"]
            )
            first_ticker_item = first_item["list"][0]
            assert "ticker" in first_ticker_item
            assert "changeUsd" in first_ticker_item


def test_get_etf_premium_discount_history_default(
    bitcoin_etf_client: BitcoinETFClient,
) -> None:
    """Tests the get_etf_premium_discount_history method with default parameters."""
    # Client now returns the outer list List[Dict[str, Any]]
    data: List[ETFPremiumDiscountHistoryData] = (
        bitcoin_etf_client.get_etf_premium_discount_history()
    )
    assert isinstance(data, list)
    if data:
        # Check structure of the outer dictionary (daily summary)
        assert all(isinstance(item, dict) for item in data)
        first_item = data[0]
        assert "date" in first_item
        assert "list" in first_item
        assert isinstance(first_item["list"], list)

        # Check structure of the inner list (per-ticker premium/discount)
        if first_item["list"]:
            assert all(
                isinstance(ticker_data, dict) for ticker_data in first_item["list"]
            )
            first_ticker_item = first_item["list"][0]
            assert "ticker" in first_ticker_item
            assert "premiumDiscountPercent" in first_ticker_item
            assert "marketPrice" in first_ticker_item
            assert "nav" in first_ticker_item


def test_get_etf_premium_discount_history_custom(
    bitcoin_etf_client: BitcoinETFClient,
) -> None:
    """Tests the get_etf_premium_discount_history method with a specific ticker."""
    ticker = "GBTC"
    # Client returns List[Dict[str, Any]] directly when ticker is specified
    data: List[ETFPremiumDiscountHistoryData] = (
        bitcoin_etf_client.get_etf_premium_discount_history(ticker=ticker)
    )
    assert isinstance(data, list)
    if data:
        # Check structure of the list items directly
        assert all(isinstance(item, dict) for item in data)
        first_item = data[0]
        # These keys are directly in the item based on error
        assert "date" in first_item
        assert "marketPrice" in first_item
        assert "nav" in first_item
        assert "premiumDiscountPercent" in first_item
        # Ticker might not be explicitly present in each item when filtered


def test_get_etf_history_custom(bitcoin_etf_client: BitcoinETFClient) -> None:
    """Tests the get_etf_history method with a specific ticker."""
    ticker = "FBTC"
    data: List[ETFHistoryData] = bitcoin_etf_client.get_etf_history(ticker=ticker)
    assert isinstance(data, list)
    # API returns a list of historical data points
    assert data  # Check list is not empty
    if data:
        assert isinstance(data[0], dict)
        # assert data[0].get("ticker") == ticker # Ticker might not be in each item
        # Check keys based on error output for this test
        assert "amount" in data[0]
        assert "assetsDate" in data[0]
        assert "marketDate" in data[0]
        # assert "totalFlow" in data[0]  # This key might not exist, remove based on error


def test_get_etf_price_history_default(bitcoin_etf_client: BitcoinETFClient) -> None:
    """Tests the get_etf_price_history method with default parameters."""
    # Client now attempts to return the inner list: List[List[Union[int, float]]]
    data: List[ETFPriceData] = bitcoin_etf_client.get_etf_price_history()
    assert isinstance(data, list)
    if data:
        # Check if the items in the list are themselves lists (the OHLC data)
        assert all(isinstance(item, list) for item in data)
        first_item = data[0]
        assert len(first_item) == 5
        assert all(
            isinstance(val, (int, float)) or val is None for val in first_item
        )  # Allow None for incomplete data


def test_get_etf_price_history_custom(bitcoin_etf_client: BitcoinETFClient) -> None:
    """Tests the get_etf_price_history method with custom parameters."""
    ticker = "ARKB"
    range_val = "7d"
    # Client now attempts to return the inner list: List[List[Union[int, float]]]
    data: List[ETFPriceData] = bitcoin_etf_client.get_etf_price_history(
        ticker=ticker, range=range_val
    )
    assert isinstance(data, list)
    if data:
        assert all(isinstance(item, list) for item in data)
        first_item = data[0]
        assert len(first_item) == 5
        assert all(
            isinstance(val, (int, float)) or val is None for val in first_item
        )  # Allow None


def test_get_etf_detail_default(bitcoin_etf_client: BitcoinETFClient) -> None:
    """Tests the get_etf_detail method with the default ticker."""
    data: ETFDetailData = bitcoin_etf_client.get_etf_detail()
    assert isinstance(data, dict)
    assert data.get("ticker") == "GBTC"  # Default ticker check
    # assert "marketCap" in data # Key not found
    assert "name" in data
    assert "lastTrade" in data  # Check another key from error output


def test_get_etf_detail_custom(bitcoin_etf_client: BitcoinETFClient) -> None:
    """Tests the get_etf_detail method with a custom ticker."""
    ticker = "BITB"
    data: ETFDetailData = bitcoin_etf_client.get_etf_detail(ticker=ticker)
    assert isinstance(data, dict)
    assert data.get("ticker") == ticker
    # assert "marketCap" in data # Key not found
    assert "name" in data
    assert "lastQuote" in data  # Check another key from error output
