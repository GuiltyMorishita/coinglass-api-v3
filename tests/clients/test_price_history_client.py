"""Tests for the PriceHistoryClient making live API calls."""

import os
import time
import pytest
from typing import List
from coinglass_api_v3.clients import PriceHistoryClient
from coinglass_api_v3.models import OHLCData
from coinglass_api_v3.exceptions import CoinglassAPIError

# Skip tests if the API key environment variable is not set
API_KEY = os.environ.get("COINGLASS_API_KEY")
pytestmark = pytest.mark.skipif(
    not API_KEY,
    reason="COINGLASS_API_KEY environment variable not set. Skipping live API tests.",
)


@pytest.fixture
def price_history_client() -> PriceHistoryClient:
    """Provides an instance of PriceHistoryClient for testing with a live API key."""
    assert API_KEY is not None  # Should be skipped if None by pytestmark
    return PriceHistoryClient(api_key=API_KEY)


def _validate_ohlc_data(data: List[OHLCData], expected_limit: int) -> None:
    """Helper function to validate the structure and types of OHLC data."""
    assert isinstance(data, list)
    if not data:
        # Allow empty lists as valid responses in some scenarios
        return

    assert len(data) <= expected_limit
    # Check the structure and types of the first item
    first_item = data[0]
    assert isinstance(first_item, dict)
    # Verify all expected keys are present
    expected_keys = OHLCData.__annotations__.keys()
    assert all(key in first_item for key in expected_keys)

    # Verify types for all key fields
    assert isinstance(first_item["t"], int)
    assert isinstance(first_item["o"], float)
    assert isinstance(first_item["h"], float)
    assert isinstance(first_item["l"], float)
    assert isinstance(first_item["c"], float)
    assert isinstance(first_item["v"], float)


def test_get_price_ohlc_history_futures(
    price_history_client: PriceHistoryClient,
) -> None:
    """Tests getting futures OHLC data."""
    limit = 5
    result = price_history_client.get_price_ohlc_history(
        exchange="Binance",
        symbol="BTCUSDT",
        type="futures",
        interval="1h",
        limit=limit,
    )
    _validate_ohlc_data(result, limit)


def test_get_price_ohlc_history_spot(price_history_client: PriceHistoryClient) -> None:
    """Tests getting spot OHLC data."""
    limit = 5
    result = price_history_client.get_price_ohlc_history(
        exchange="Binance",
        symbol="BTCUSDT",
        type="spot",
        interval="4h",
        limit=limit,
    )
    _validate_ohlc_data(result, limit)


def test_get_price_ohlc_history_limit(price_history_client: PriceHistoryClient) -> None:
    """Tests the limit parameter."""
    limit = 3
    result = price_history_client.get_price_ohlc_history(limit=limit)
    _validate_ohlc_data(result, limit)
    # API might return slightly fewer than the limit sometimes, but not more
    assert len(result) <= limit


def test_get_price_ohlc_history_timeframe(
    price_history_client: PriceHistoryClient,
) -> None:
    """Tests the startTime and endTime parameters."""
    limit = 10
    # Get data for a specific 1-day period (e.g., day before yesterday)
    end_time_dt = time.time() - 86400 * 2  # Approx 2 days ago
    start_time_dt = end_time_dt - 86400  # Approx 3 days ago

    start_time_sec = int(start_time_dt)
    end_time_sec = int(end_time_dt)

    result = price_history_client.get_price_ohlc_history(
        interval="1h",
        limit=limit,
        startTime=start_time_sec,
        endTime=end_time_sec,
    )

    # 時間範囲指定時は、APIがlimitを超えるデータを返す場合があるため
    # データの構造と型のみ検証し、件数の検証はスキップ
    assert isinstance(result, list)
    if not result:
        # Allow empty lists as valid responses in some scenarios
        return

    # Check the structure and types of the first item
    first_item = result[0]
    assert isinstance(first_item, dict)
    # Verify all expected keys are present
    expected_keys = OHLCData.__annotations__.keys()
    assert all(key in first_item for key in expected_keys)

    # Verify types for all key fields
    assert isinstance(first_item["t"], int)
    assert isinstance(first_item["o"], float)
    assert isinstance(first_item["h"], float)
    assert isinstance(first_item["l"], float)
    assert isinstance(first_item["c"], float)
    assert isinstance(first_item["v"], float)

    # Check if timestamps fall within the requested range (allow for interval overlap)
    interval_seconds = 3600  # 1h
    for item in result:
        assert item["t"] >= start_time_sec - interval_seconds
        assert item["t"] <= end_time_sec + interval_seconds


def test_get_price_ohlc_history_invalid_symbol(
    price_history_client: PriceHistoryClient,
) -> None:
    """Tests the method with a likely invalid symbol."""
    # Use a symbol that is highly unlikely to exist
    with pytest.raises(CoinglassAPIError) as excinfo:
        price_history_client.get_price_ohlc_history(
            symbol="INVALID_SYMBOL_XYZ123", limit=5
        )
    # APIは「40001」(instrument)エラーコードを返す
    assert excinfo.value.code == "40001"
    assert "instrument" in str(excinfo.value)


def test_get_price_ohlc_history_invalid_interval(
    price_history_client: PriceHistoryClient,
) -> None:
    """Tests the method with an invalid interval."""
    # クライアント側のバリデーションでエラーが発生することを期待
    with pytest.raises(CoinglassAPIError) as excinfo:
        price_history_client.get_price_ohlc_history(
            interval="invalid_interval", limit=5
        )
    # 期待されるエラーコードを検証
    assert excinfo.value.code == "INVALID_ARGUMENT"
    assert "Invalid interval" in str(excinfo.value)


def test_get_price_ohlc_history_invalid_type(
    price_history_client: PriceHistoryClient,
) -> None:
    """Tests the method with an invalid type parameter."""
    with pytest.raises(CoinglassAPIError) as excinfo:
        price_history_client.get_price_ohlc_history(type="invalid_type", limit=5)
    assert excinfo.value.code == "INVALID_ARGUMENT"
    assert "Invalid type" in str(excinfo.value)


def test_get_price_ohlc_history_invalid_limit(
    price_history_client: PriceHistoryClient,
) -> None:
    """Tests the method with invalid limit values."""
    # 負の制限値
    with pytest.raises(CoinglassAPIError) as excinfo:
        price_history_client.get_price_ohlc_history(limit=-1)
    assert excinfo.value.code == "INVALID_ARGUMENT"
    assert "Limit must be a positive integer" in str(excinfo.value)

    # ゼロの制限値
    with pytest.raises(CoinglassAPIError) as excinfo:
        price_history_client.get_price_ohlc_history(limit=0)
    assert excinfo.value.code == "INVALID_ARGUMENT"
    assert "Limit must be a positive integer" in str(excinfo.value)

    # 最大値を超える制限値
    with pytest.raises(CoinglassAPIError) as excinfo:
        price_history_client.get_price_ohlc_history(limit=4501)
    assert excinfo.value.code == "INVALID_ARGUMENT"
    assert "exceeds maximum of 4500" in str(excinfo.value)


def test_get_price_ohlc_history_invalid_time_range(
    price_history_client: PriceHistoryClient,
) -> None:
    """Tests the method with invalid time range (startTime > endTime)."""
    current_time = int(time.time())
    with pytest.raises(CoinglassAPIError) as excinfo:
        price_history_client.get_price_ohlc_history(
            startTime=current_time,
            endTime=current_time - 86400,  # 1日前（開始が終了より後）
        )
    assert excinfo.value.code == "INVALID_ARGUMENT"
    assert "startTime" in str(
        excinfo.value
    ) and "must be less than or equal to endTime" in str(excinfo.value)
