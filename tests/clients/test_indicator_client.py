"""Tests for the Coinglass Indicator API client."""

import os
from typing import TYPE_CHECKING, List, Dict, Any, Optional

import pytest

from src.coinglass_api_v3.clients import IndicatorClient
from src.coinglass_api_v3.models import (
    BullMarketPeakIndicatorData,
    BitcoinBubbleIndexData,
    AHR999Data,
    TwoYearMAMultiplierData,
    MovingAvgHeatmapData,
    PuellMultipleData,
    StockFlowData,
    PiCycleTopIndicatorData,
    GoldenRatioMultiplierData,
    BitcoinProfitableDaysData,
    BitcoinRainbowChartDataPoint,
    FearGreedHistoryData,
    GrayscaleHoldingData,
    GrayscalePremiumHistoryData,
    BorrowInterestRateData,
    ExchangeBalanceListData,
    ExchangeBalanceChartData,
)

if TYPE_CHECKING:
    from _pytest.capture import CaptureFixture
    from _pytest.fixtures import FixtureRequest
    from _pytest.logging import LogCaptureFixture
    from _pytest.monkeypatch import MonkeyPatch
    from pytest_mock.plugin import MockerFixture


@pytest.fixture
def indicator_client() -> IndicatorClient:
    """Fixture to create an IndicatorClient instance using API key from env var."""
    api_key = os.environ.get("COINGLASS_API_KEY")
    if not api_key:
        pytest.skip(
            "COINGLASS_API_KEY environment variable not set. Skipping live API test."
        )
    return IndicatorClient(api_key=api_key)


def test_get_bull_market_peak_indicators(
    indicator_client: IndicatorClient,
) -> None:
    """Tests the get_bull_market_peak_indicators method against the live API."""

    result: List[BullMarketPeakIndicatorData] = (
        indicator_client.get_bull_market_peak_indicators()
    )

    assert isinstance(result, list)
    assert len(result) > 0
    first_item = result[0]
    assert isinstance(first_item, dict)
    # Assert presence and type of required keys based on the updated model
    assert "name" in first_item
    assert isinstance(first_item["name"], str)
    assert "value" in first_item
    assert isinstance(first_item["value"], str)
    assert "targetValue" in first_item
    assert isinstance(first_item["targetValue"], str)

    # Assert presence and type of optional keys if they exist
    if "prevValue" in first_item:
        assert isinstance(first_item["prevValue"], (str, type(None)))
    if "change" in first_item:
        assert isinstance(first_item["change"], (str, type(None)))
    if "type" in first_item:
        assert isinstance(first_item["type"], (str, type(None)))
    if "hit" in first_item:
        assert isinstance(first_item["hit"], (bool, type(None)))


def test_get_bitcoin_bubble_index(indicator_client: IndicatorClient) -> None:
    """Tests the get_bitcoin_bubble_index method."""
    result: List[BitcoinBubbleIndexData] = indicator_client.get_bitcoin_bubble_index()
    assert isinstance(result, list)
    assert len(result) > 0
    first_item = result[0]
    assert isinstance(first_item, dict)
    assert "price" in first_item
    assert isinstance(first_item["price"], (float, int))
    assert "index" in first_item
    assert isinstance(first_item["index"], (float, int))
    assert "date" in first_item
    assert isinstance(first_item["date"], str)
    # Check other potentially important fields
    assert "googleTrend" in first_item
    assert "difficulty" in first_item
    assert "transcations" in first_item  # Note API typo


def test_get_ahr999_index(indicator_client: IndicatorClient) -> None:
    """Tests the get_ahr999_index method."""
    result: List[AHR999Data] = indicator_client.get_ahr999_index()
    assert isinstance(result, list)
    assert len(result) > 0
    first_item = result[0]
    assert isinstance(first_item, dict)
    assert "date" in first_item
    assert isinstance(first_item["date"], str)
    assert "ahr999" in first_item
    assert isinstance(first_item["ahr999"], (float, int))
    assert "value" in first_item  # Price
    assert isinstance(first_item["value"], str)
    assert "avg" in first_item
    assert isinstance(first_item["avg"], (float, int))


def test_get_two_year_ma_multiplier(indicator_client: IndicatorClient) -> None:
    """Tests the get_two_year_ma_multiplier method."""
    result: List[TwoYearMAMultiplierData] = (
        indicator_client.get_two_year_ma_multiplier()
    )
    assert isinstance(result, list)
    assert len(result) > 0
    first_item = result[0]
    assert isinstance(first_item, dict)
    assert "createTime" in first_item
    assert isinstance(first_item["createTime"], int)
    assert "price" in first_item
    assert isinstance(first_item["price"], (float, int))
    assert "mA730Mu5" in first_item
    assert isinstance(first_item["mA730Mu5"], (float, int))
    assert "mA730" in first_item
    assert isinstance(first_item["mA730"], (float, int))


def test_get_200w_ma_heatmap(indicator_client: IndicatorClient) -> None:
    """Tests the get_200w_ma_heatmap method."""
    result: List[MovingAvgHeatmapData] = indicator_client.get_200w_ma_heatmap()
    assert isinstance(result, list)
    assert len(result) > 0
    first_item = result[0]
    assert isinstance(first_item, dict)
    assert "createTime" in first_item
    assert isinstance(first_item["createTime"], int)
    assert "price" in first_item
    assert isinstance(first_item["price"], (float, int))
    assert "mA1440" in first_item
    assert isinstance(first_item["mA1440"], (float, int))
    if "mA1440IP" in first_item:
        assert isinstance(first_item["mA1440IP"], (float, int, type(None)))


def test_get_puell_multiple(indicator_client: IndicatorClient) -> None:
    """Tests the get_puell_multiple method."""
    result: List[PuellMultipleData] = indicator_client.get_puell_multiple()
    assert isinstance(result, list)
    assert len(result) > 0
    first_item = result[0]
    assert isinstance(first_item, dict)
    assert "createTime" in first_item
    assert isinstance(first_item["createTime"], int)
    assert "price" in first_item
    assert isinstance(first_item["price"], (float, int))
    assert "puellMultiple" in first_item
    assert isinstance(first_item["puellMultiple"], (float, int))


def test_get_stock_flow(indicator_client: IndicatorClient) -> None:
    """Tests the get_stock_flow method."""
    result: List[StockFlowData] = indicator_client.get_stock_flow()
    assert isinstance(result, list)
    assert len(result) > 0
    first_item = result[0]
    assert isinstance(first_item, dict)
    assert "createTime" in first_item
    assert isinstance(first_item["createTime"], str)
    assert "price" in first_item
    assert isinstance(first_item["price"], (float, int))
    assert "nextHalving" in first_item
    assert isinstance(first_item["nextHalving"], int)


def test_get_pi_cycle_top_indicator(indicator_client: IndicatorClient) -> None:
    """Tests the get_pi_cycle_top_indicator method."""
    result: List[PiCycleTopIndicatorData] = (
        indicator_client.get_pi_cycle_top_indicator()
    )
    assert isinstance(result, list)
    assert len(result) > 0
    first_item = result[0]
    assert isinstance(first_item, dict)
    assert "createTime" in first_item
    assert isinstance(first_item["createTime"], int)
    assert "price" in first_item
    assert isinstance(first_item["price"], (float, int))
    assert "ma110" in first_item
    assert isinstance(first_item["ma110"], str)
    assert "ma350Mu2" in first_item
    assert isinstance(first_item["ma350Mu2"], str)


def test_get_golden_ratio_multiplier(indicator_client: IndicatorClient) -> None:
    """Tests the get_golden_ratio_multiplier method."""
    result: List[GoldenRatioMultiplierData] = (
        indicator_client.get_golden_ratio_multiplier()
    )
    assert isinstance(result, list)
    assert len(result) > 0
    first_item = result[0]
    assert isinstance(first_item, dict)
    assert "createTime" in first_item
    assert isinstance(first_item["createTime"], int)
    assert "price" in first_item
    assert isinstance(first_item["price"], (float, int))
    assert "ma350" in first_item
    assert isinstance(first_item["ma350"], (float, int))
    assert "LowBullHigh2" in first_item
    assert isinstance(
        first_item["LowBullHigh2"], (float, int, type(None))
    )  # Allow None due to potential missing key handling
    assert "AccumulationHigh1_6" in first_item
    assert isinstance(first_item["AccumulationHigh1_6"], (float, int, type(None)))
    # Check a few multiplier keys
    assert "x8" in first_item
    assert isinstance(first_item["x8"], (float, int, type(None)))
    assert "x5" in first_item
    assert isinstance(first_item["x5"], (float, int, type(None)))


def test_get_bitcoin_profitable_days(indicator_client: IndicatorClient) -> None:
    """Tests the get_bitcoin_profitable_days method."""
    result: List[BitcoinProfitableDaysData] = (
        indicator_client.get_bitcoin_profitable_days()
    )
    assert isinstance(result, list)
    assert len(result) > 0
    first_item = result[0]
    assert isinstance(first_item, dict)
    assert "createTime" in first_item
    assert isinstance(first_item["createTime"], int)
    assert "price" in first_item
    assert isinstance(first_item["price"], (float, int))
    assert "side" in first_item
    assert isinstance(first_item["side"], int)
    assert first_item["side"] in [1, -1]


def test_get_bitcoin_rainbow_chart(indicator_client: IndicatorClient) -> None:
    """Tests the get_bitcoin_rainbow_chart method."""
    result: List[BitcoinRainbowChartDataPoint] = (
        indicator_client.get_bitcoin_rainbow_chart()
    )
    assert isinstance(result, list)
    assert len(result) > 0
    first_item = result[0]
    assert isinstance(first_item, dict)
    # Check essential keys based on the model
    assert "t" in first_item
    assert isinstance(first_item["t"], int)
    assert "price" in first_item
    assert isinstance(first_item["price"], (float, int, type(None)))
    assert "model_price" in first_item
    assert isinstance(first_item["model_price"], (float, int, type(None)))
    # Check one band key
    assert "hold" in first_item
    assert isinstance(first_item["hold"], (float, int, type(None)))


def test_get_fear_greed_history(indicator_client: IndicatorClient) -> None:
    """Tests the get_fear_greed_history method."""
    result: List[FearGreedHistoryData] = indicator_client.get_fear_greed_history()
    assert isinstance(result, list)
    assert len(result) > 0
    first_item = result[0]
    assert isinstance(first_item, dict)
    assert "t" in first_item
    assert isinstance(first_item["t"], int)
    assert "value" in first_item
    assert isinstance(first_item["value"], (float, int))
    assert "price" in first_item
    assert isinstance(first_item["price"], (float, int))


def test_get_grayscale_holdings_list(indicator_client: IndicatorClient) -> None:
    """Tests the get_grayscale_holdings_list method."""
    result: List[GrayscaleHoldingData] = indicator_client.get_grayscale_holdings_list()
    assert isinstance(result, list)
    # API might return empty list if no holdings currently?
    if len(result) > 0:
        first_item = result[0]
        assert isinstance(first_item, dict)
        assert "symbol" in first_item
        assert isinstance(first_item["symbol"], str)
        assert "holdingsAmount" in first_item
        assert isinstance(first_item["holdingsAmount"], (float, int))
        assert "holdingsUsd" in first_item
        assert isinstance(first_item["holdingsUsd"], (float, int))
        assert "updateTime" in first_item
        assert isinstance(first_item["updateTime"], int)


def test_get_grayscale_premium_history(indicator_client: IndicatorClient) -> None:
    """Tests the get_grayscale_premium_history method."""
    result: List[GrayscalePremiumHistoryData] = (
        indicator_client.get_grayscale_premium_history(symbol="BTC")
    )
    assert isinstance(result, list)
    assert len(result) > 0
    first_item = result[0]
    assert isinstance(first_item, dict)
    assert "t" in first_item
    assert isinstance(first_item["t"], int)
    assert "secondaryMarketPrice" in first_item
    assert isinstance(first_item["secondaryMarketPrice"], (float, int, type(None)))
    assert "premiumRate" in first_item
    assert isinstance(first_item["premiumRate"], (float, int, type(None)))


def test_get_borrow_interest_rate_history(indicator_client: IndicatorClient) -> None:
    """Tests the get_borrow_interest_rate_history method."""
    result: List[BorrowInterestRateData] = (
        indicator_client.get_borrow_interest_rate_history(
            exchange="Binance",
            symbol="BTC",
            interval="h1",
            limit=10,  # Limit for faster test
        )
    )
    assert isinstance(result, list)
    assert len(result) <= 10  # Check if limit is respected (or fewer if less data)
    if len(result) > 0:
        first_item = result[0]
        assert isinstance(first_item, dict)
        assert "time" in first_item
        assert isinstance(first_item["time"], int)
        assert "interestRate" in first_item
        assert isinstance(first_item["interestRate"], (float, int))


def test_get_exchange_balance_list(indicator_client: IndicatorClient) -> None:
    """Tests the get_exchange_balance_list method."""
    result: List[ExchangeBalanceListData] = indicator_client.get_exchange_balance_list(
        symbol="BTC"
    )
    assert isinstance(result, list)
    assert len(result) > 0
    first_item = result[0]
    assert isinstance(first_item, dict)
    assert "exchangeName" in first_item
    assert isinstance(first_item["exchangeName"], str)
    assert "balance" in first_item
    assert isinstance(first_item["balance"], (float, int))
    # Check one change field
    assert "change1d" in first_item
    assert isinstance(first_item["change1d"], (float, int))
    assert "changePercent1d" in first_item
    assert isinstance(first_item["changePercent1d"], (float, int))


def test_get_exchange_balance_chart(indicator_client: IndicatorClient) -> None:
    """Tests the get_exchange_balance_chart method."""
    result: ExchangeBalanceChartData = indicator_client.get_exchange_balance_chart(
        symbol="BTC"
    )
    assert isinstance(result, dict)
    assert "timeList" in result
    assert isinstance(result["timeList"], list)
    assert "dataMap" in result
    assert isinstance(result["dataMap"], dict)

    if result["timeList"]:
        assert isinstance(result["timeList"][0], int)

    if result["dataMap"]:
        # Check structure of one exchange's data if available
        first_exchange = next(iter(result["dataMap"]))  # Get first key
        assert isinstance(result["dataMap"][first_exchange], list)
        if result["dataMap"][first_exchange]:
            assert isinstance(
                result["dataMap"][first_exchange][0], (float, int, type(None))
            )
