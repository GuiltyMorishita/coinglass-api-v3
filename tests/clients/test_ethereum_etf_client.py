import os
import pytest
from typing import Generator, TYPE_CHECKING, List, Dict, Any

from coinglass_api_v3.clients import EthereumETFClient
from coinglass_api_v3.models import (
    EthereumETFNetAssetsHistoryData,
    EthereumETFInfoData,
    EthereumETFFlowHistoryData,
)

if TYPE_CHECKING:
    from _pytest.capture import CaptureFixture
    from _pytest.fixtures import FixtureRequest
    from _pytest.logging import LogCaptureFixture
    from _pytest.monkeypatch import MonkeyPatch
    from pytest_mock.plugin import MockerFixture


@pytest.fixture(scope="module")
def ethereum_etf_client() -> Generator[EthereumETFClient, None, None]:
    """Provides an EthereumETFClient instance for testing."""
    api_key = os.environ.get("COINGLASS_API_KEY")
    if not api_key:
        pytest.skip("API key not found in environment variables.")
    client = EthereumETFClient(api_key)
    yield client


@pytest.mark.skip(reason="API endpoint is too slow")
def test_get_etf_net_assets_history(ethereum_etf_client: EthereumETFClient) -> None:
    """Tests the get_etf_net_assets_history method."""
    data: List[EthereumETFNetAssetsHistoryData] = (
        ethereum_etf_client.get_etf_net_assets_history()
    )
    assert isinstance(data, list)
    if data:
        assert all(isinstance(item, dict) for item in data)
        first_item = data[0]
        assert "date" in first_item
        assert "netAssets" in first_item
        assert "change" in first_item
        assert "price" in first_item


def test_get_etf_list(ethereum_etf_client: EthereumETFClient) -> None:
    """Tests the get_etf_list method."""
    data: List[EthereumETFInfoData] = ethereum_etf_client.get_etf_list()
    assert isinstance(data, list)
    if data:
        assert all(isinstance(item, dict) for item in data)
        first_item = data[0]
        assert "ticker" in first_item
        assert "name" in first_item
        assert "assetInfo" in first_item
        assert "nav" in first_item["assetInfo"]
        assert "holding" in first_item["assetInfo"]
        assert "date" in first_item["assetInfo"]


def test_get_etf_flows_history(ethereum_etf_client: EthereumETFClient) -> None:
    """Tests the get_etf_flows_history method."""
    data: List[EthereumETFFlowHistoryData] = ethereum_etf_client.get_etf_flows_history()
    assert isinstance(data, list)
    if data:
        assert all(isinstance(item, dict) for item in data)
        first_item = data[0]
        assert "date" in first_item
        assert "changeUsd" in first_item
        assert "closePrice" in first_item
        assert "list" in first_item
        assert isinstance(first_item["list"], list)
        if first_item["list"]:
            assert all(
                isinstance(ticker_data, dict) for ticker_data in first_item["list"]
            )
            first_ticker_item = first_item["list"][0]
            assert "ticker" in first_ticker_item
            assert "changeUsd" in first_ticker_item
