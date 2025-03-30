import os
import pytest
from typing import TYPE_CHECKING, List, Dict, Union, Optional, cast
from dotenv import load_dotenv

from coinglass_api_v3.clients import SpotClient
from coinglass_api_v3.models import (
    ExchangePair,
    SpotTakerBuySellData,
    SpotOrderbookHistoryData,
    CoinMarketData,
    SpotPairMarketData,
    CoinbasePremiumIndexData,
    BitfinexMarginLongShortData,
)

if TYPE_CHECKING:
    from _pytest.capture import CaptureFixture
    from _pytest.fixtures import FixtureRequest
    from _pytest.logging import LogCaptureFixture
    from _pytest.monkeypatch import MonkeyPatch
    from pytest_mock.plugin import MockerFixture


@pytest.fixture(scope="module")
def spot_client() -> SpotClient:
    """SpotClientインスタンスを提供するフィクスチャ。"""
    load_dotenv(".env.test")
    api_key = os.getenv("COINGLASS_API_KEY")
    if not api_key:
        pytest.skip(
            "COINGLASS_API_KEY not set in .env.test file. Skipping integration tests."
        )
    return SpotClient(api_key=api_key)


def test_get_supported_coins(spot_client: SpotClient) -> None:
    """サポートされているコインのリスト取得をテスト。"""
    coins = spot_client.get_supported_coins()
    assert isinstance(coins, list)
    assert len(coins) > 0
    assert all(isinstance(coin, str) for coin in coins)


def test_get_supported_exchange_pairs(spot_client: SpotClient) -> None:
    """サポートされている取引所ペアのリスト取得をテスト。"""
    exchange_pairs = spot_client.get_supported_exchange_pairs()
    assert isinstance(exchange_pairs, dict)
    assert len(exchange_pairs) > 0

    # Binanceの構造をチェック
    assert "Binance" in exchange_pairs
    assert isinstance(exchange_pairs["Binance"], list)

    if len(exchange_pairs["Binance"]) > 0:
        pair = exchange_pairs["Binance"][0]
        assert isinstance(pair, dict)
        assert "instrumentId" in pair


def test_get_taker_buy_sell_history(spot_client: SpotClient) -> None:
    """Taker買い/売り履歴データの取得をテスト。"""
    data = spot_client.get_taker_buy_sell_history(limit=10)
    assert isinstance(data, list)
    assert len(data) <= 10

    if data:
        entry = data[0]
        assert isinstance(entry, dict)
        required_fields = ["buy", "sell", "time"]
        for field in required_fields:
            assert field in entry

        assert isinstance(entry["buy"], (int, float))
        assert isinstance(entry["sell"], (int, float))
        assert isinstance(entry["time"], int)


def test_get_aggregated_taker_buy_sell_history(spot_client: SpotClient) -> None:
    """集計されたTaker買い/売り履歴データの取得をテスト。"""
    data = spot_client.get_aggregated_taker_buy_sell_history(limit=10)
    assert isinstance(data, list)
    assert len(data) <= 10

    if data:
        entry = data[0]
        assert isinstance(entry, dict)
        required_fields = ["buy", "sell", "time"]
        for field in required_fields:
            assert field in entry

        assert isinstance(entry["buy"], (int, float))
        assert isinstance(entry["sell"], (int, float))
        assert isinstance(entry["time"], int)


def test_get_orderbook_history(spot_client: SpotClient) -> None:
    """オーダーブック履歴データの取得をテスト。"""
    data = spot_client.get_orderbook_history(limit=10)
    assert isinstance(data, list)
    assert len(data) <= 10

    if data:
        entry = data[0]
        assert isinstance(entry, dict)
        required_fields = ["asksAmount", "bidsAmount", "time"]
        for field in required_fields:
            assert field in entry

        assert isinstance(entry["asksAmount"], (int, float))
        assert isinstance(entry["bidsAmount"], (int, float))
        assert isinstance(entry["time"], int)


def test_get_aggregated_orderbook_history(spot_client: SpotClient) -> None:
    """集計されたオーダーブック履歴データの取得をテスト。"""
    data = spot_client.get_aggregated_orderbook_history(limit=10)
    assert isinstance(data, list)
    assert len(data) <= 10

    if data:
        entry = data[0]
        assert isinstance(entry, dict)
        required_fields = ["asksAmount", "bidsAmount", "time"]
        for field in required_fields:
            assert field in entry

        assert isinstance(entry["asksAmount"], (int, float))
        assert isinstance(entry["bidsAmount"], (int, float))
        assert isinstance(entry["time"], int)


def test_get_coins_markets(spot_client: SpotClient) -> None:
    """コイン市場データの取得をテスト。"""
    data = spot_client.get_coins_markets(pageSize=5)
    assert isinstance(data, list)
    assert len(data) <= 5

    if data:
        entry = data[0]
        assert isinstance(entry, dict)
        required_fields = ["symbol", "price"]
        for field in required_fields:
            assert field in entry

        assert isinstance(entry["symbol"], str)
        assert isinstance(entry["price"], (int, float))


def test_get_pairs_markets(spot_client: SpotClient) -> None:
    """取引ペア市場データの取得をテスト。"""
    data = spot_client.get_pairs_markets(symbol="BTC")
    assert isinstance(data, list)
    assert len(data) > 0

    if data:
        entry = data[0]
        assert isinstance(entry, dict)

        # 必須フィールドの確認
        required_fields = [
            "buyVolUsd1h",
            "buyVolUsd24h",
            "buyVolUsd12h",
            "buyVolUsd1w",
            "sellVolUsd1h",
            "sellVolUsd24h",
            "sellVolUsd12h",
            "sellVolUsd1w",
        ]
        for field in required_fields:
            assert field in entry

        # 値の型チェック
        volume_fields = [
            "buyVolUsd1h",
            "buyVolUsd24h",
            "buyVolUsd12h",
            "buyVolUsd1w",
            "sellVolUsd1h",
            "sellVolUsd24h",
            "sellVolUsd12h",
            "sellVolUsd1w",
        ]
        for field in volume_fields:
            assert isinstance(entry[field], (int, float))
            assert entry[field] >= 0  # 取引量は負にならない


def test_get_coinbase_premium_index(spot_client: SpotClient) -> None:
    """Coinbaseプレミアムインデックスデータの取得をテスト。"""
    data = spot_client.get_coinbase_premium_index(limit=10)
    assert isinstance(data, list)
    assert len(data) <= 10

    if data:
        entry = data[0]
        assert isinstance(entry, dict)
        required_fields = ["premium", "time"]
        for field in required_fields:
            assert field in entry

        assert isinstance(entry["premium"], (int, float))
        assert isinstance(entry["time"], int)


def test_get_bitfinex_margin_long_short(spot_client: SpotClient) -> None:
    """Bitfinexマージンロング/ショートデータの取得をテスト。"""
    data = spot_client.get_bitfinex_margin_long_short(limit=10)
    assert isinstance(data, list)
    assert len(data) <= 10

    if data:
        entry = data[0]
        assert isinstance(entry, dict)
        required_fields = ["longQty", "shortQty", "time"]
        for field in required_fields:
            assert field in entry

        assert isinstance(entry["longQty"], (int, float))
        assert isinstance(entry["shortQty"], (int, float))
        assert isinstance(entry["time"], int)
