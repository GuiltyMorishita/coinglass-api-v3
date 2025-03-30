import os
import pytest
from typing import TYPE_CHECKING, List, Dict, Union, Optional, cast
from dotenv import load_dotenv

# Import necessary components from your library
from coinglass_api_v3.clients import FutureClient
from coinglass_api_v3.models import (
    OHLCData,
    ExchangeOpenInterestData,
    LongShortRatioData,
    ArbitrageOpportunityData,
    ExchangePair,
    TakerBuySellVolumeData,
    ExchangeHistoryChartData,
    SymbolFundingRateData,
    SymbolCumulativeFundingRateData,
    LiquidationHistoryData,
    LiquidationCoinData,
    LiquidationExchangeData,
    LiquidationOrderData,
    LiquidationAggregatedHeatmapData,
    AggregatedTakerBuySellRatioData,
    AggregatedTakerBuySellVolumeData,
    ExchangeTakerBuySellRatioData,
    HyperliquidWhalePositionData,
    HyperliquidWhaleAlertData,
    CoinMarketData,
    PairMarketData,
    CoinPriceChangeData,
    OrderbookHistoryData,
    RsiData,
)

if TYPE_CHECKING:
    from _pytest.capture import CaptureFixture
    from _pytest.fixtures import FixtureRequest
    from _pytest.logging import LogCaptureFixture
    from _pytest.monkeypatch import MonkeyPatch
    from pytest_mock.plugin import MockerFixture


# Fixture to initialize the FutureClient
# Skips tests if COINGLASS_API_KEY is not set in environment variables
@pytest.fixture(scope="module")
def future_client() -> FutureClient:
    """Provides a FutureClient instance for testing."""
    load_dotenv(".env.test")
    api_key = os.getenv("COINGLASS_API_KEY")
    if not api_key:
        pytest.skip(
            "COINGLASS_API_KEY not set in .env.test file. Skipping integration tests."
        )
    # Assuming your BaseClient or FutureClient accepts api_key
    # Adjust instantiation based on your actual client implementation
    return FutureClient(api_key=api_key)


# --- General Information Tests ---


def test_get_supported_coins(future_client: FutureClient) -> None:
    """Tests retrieving supported coins."""
    coins = future_client.get_supported_coins()
    assert isinstance(coins, list)
    assert len(coins) > 0
    assert all(isinstance(coin, str) for coin in coins)


def test_get_supported_exchange_pairs(future_client: FutureClient) -> None:
    """Tests retrieving supported exchange pairs."""
    exchange_pairs = future_client.get_supported_exchange_pairs()
    assert isinstance(exchange_pairs, dict)
    assert len(exchange_pairs) > 0
    # Check structure for a known exchange (e.g., Binance)
    assert "Binance" in exchange_pairs
    assert isinstance(exchange_pairs["Binance"], list)
    # Assuming ExchangePair is a TypedDict or similar structure
    # Add more specific checks if ExchangePair is a class instance
    if len(exchange_pairs["Binance"]) > 0:
        assert isinstance(
            exchange_pairs["Binance"][0], dict
        )  # Or your ExchangePair type
        assert "instrumentId" in exchange_pairs["Binance"][0]


# --- Open Interest Tests ---


def test_get_open_interest_ohlc_history(future_client: FutureClient) -> None:
    """Tests retrieving OI OHLC history."""
    data = future_client.get_open_interest_ohlc_history(limit=10)
    assert isinstance(data, list)
    assert len(data) <= 10
    if data:
        assert isinstance(data[0], dict)  # Assuming OHLCData is a TypedDict
        assert all(k in data[0] for k in ["t", "o", "h", "l", "c"])


def test_get_open_interest_ohlc_aggregated_history(future_client: FutureClient) -> None:
    """Tests retrieving aggregated OI OHLC history."""
    data = future_client.get_open_interest_ohlc_aggregated_history(limit=10)
    assert isinstance(data, list)
    assert len(data) <= 10
    if data:
        assert isinstance(data[0], dict)  # Assuming OHLCData is a TypedDict
        assert all(k in data[0] for k in ["t", "o", "h", "l", "c"])


def test_get_open_interest_ohlc_aggregated_stablecoin_margin_history(
    future_client: FutureClient,
) -> None:
    """Tests retrieving aggregated stablecoin-margined OI OHLC history."""
    data = future_client.get_open_interest_ohlc_aggregated_stablecoin_margin_history(
        limit=10
    )
    assert isinstance(data, list)
    assert len(data) <= 10
    if data:
        assert isinstance(data[0], dict)
        assert all(k in data[0] for k in ["t", "o", "h", "l", "c"])


def test_get_open_interest_ohlc_aggregated_coin_margin_history(
    future_client: FutureClient,
) -> None:
    """Tests retrieving aggregated coin-margined OI OHLC history."""
    data = future_client.get_open_interest_ohlc_aggregated_coin_margin_history(limit=10)
    assert isinstance(data, list)
    assert len(data) <= 10
    if data:
        assert isinstance(data[0], dict)
        assert all(k in data[0] for k in ["t", "o", "h", "l", "c"])


def test_get_open_interest_exchange_list(future_client: FutureClient) -> None:
    """Tests retrieving OI data per exchange."""
    data = future_client.get_open_interest_exchange_list(symbol="BTC")
    assert isinstance(data, list)
    assert len(data) > 0
    if data:
        assert isinstance(
            data[0], dict
        )  # Assuming ExchangeOpenInterestData is TypedDict
        assert "exchange" in data[0]
        assert "openInterest" in data[0]


def test_get_open_interest_exchange_history_chart(future_client: FutureClient) -> None:
    """Tests retrieving OI history chart data."""
    data = future_client.get_open_interest_exchange_history_chart(
        symbol="BTC", range="1h"
    )
    assert isinstance(data, dict)  # Assuming ExchangeHistoryChartData is TypedDict
    assert "timeList" in data
    assert "priceList" in data
    assert "dataMap" in data
    assert isinstance(data["timeList"], list)
    assert isinstance(data["priceList"], list)
    assert isinstance(data["dataMap"], dict)


# --- Funding Rate Tests ---


def test_get_funding_rate_ohlc_history(future_client: FutureClient) -> None:
    """Tests retrieving funding rate OHLC history."""
    data = future_client.get_funding_rate_ohlc_history(limit=10)
    assert isinstance(data, list)
    assert len(data) <= 10
    if data:
        assert isinstance(data[0], dict)
        assert all(k in data[0] for k in ["t", "o", "h", "l", "c"])


def test_get_funding_rate_oi_weight_ohlc_history(future_client: FutureClient) -> None:
    """Tests retrieving OI weighted funding rate OHLC history."""
    data = future_client.get_funding_rate_oi_weight_ohlc_history(limit=10)
    assert isinstance(data, list)
    assert len(data) <= 10
    if data:
        assert isinstance(data[0], dict)
        assert all(k in data[0] for k in ["t", "o", "h", "l", "c"])


def test_get_funding_rate_vol_weight_ohlc_history(future_client: FutureClient) -> None:
    """Tests retrieving volume weighted funding rate OHLC history."""
    data = future_client.get_funding_rate_vol_weight_ohlc_history(limit=10)
    assert isinstance(data, list)
    assert len(data) <= 10
    if data:
        assert isinstance(data[0], dict)
        assert all(k in data[0] for k in ["t", "o", "h", "l", "c"])


def test_get_funding_rate_exchange_list(future_client: FutureClient) -> None:
    """Tests retrieving funding rate data per exchange."""
    data = future_client.get_funding_rate_exchange_list()

    # 基本的な構造のテスト
    assert isinstance(data, list)
    assert len(data) > 0

    # 各取引所のデータ構造をテスト
    for exchange_data in data:
        # 必須フィールドの存在確認
        required_fields = [
            "symbol",
            "usdtMarginList",
            "tokenMarginList",
            "usdtOrUsdMarginList",
        ]
        # いずれかのマージンリストが存在することを確認
        has_margin_list = any(
            field in exchange_data and exchange_data[field]
            for field in ["usdtMarginList", "tokenMarginList", "usdtOrUsdMarginList"]
        )
        assert has_margin_list

        # 値の型チェック
        assert isinstance(exchange_data["symbol"], str)

        # マージンリストの構造をチェック
        for list_type in ["usdtMarginList", "tokenMarginList", "usdtOrUsdMarginList"]:
            if list_type in exchange_data and exchange_data[list_type]:
                margin_list = exchange_data[list_type]
                assert isinstance(margin_list, list)
                for margin_data in margin_list:
                    assert isinstance(margin_data, dict)
                    # 必須フィールド
                    assert "exchange" in margin_data
                    assert isinstance(margin_data["exchange"], str)

                    # オプショナルフィールド
                    if "fundingRate" in margin_data:
                        assert isinstance(margin_data["fundingRate"], (int, float))
                    if "fundingIntervalHours" in margin_data:
                        assert isinstance(margin_data["fundingIntervalHours"], int)
                    if "nextFundingTime" in margin_data:
                        assert isinstance(margin_data["nextFundingTime"], int)


def test_get_funding_rate_accumulated_exchange_list(
    future_client: FutureClient,
) -> None:
    """Tests retrieving accumulated funding rate data per exchange."""
    data = future_client.get_funding_rate_accumulated_exchange_list(range="7d")
    assert isinstance(data, list)
    assert len(data) > 0
    if data:
        assert isinstance(
            data[0], dict
        )  # Assuming SymbolCumulativeFundingRateData is TypedDict
        assert "symbol" in data[0]
        assert (
            "usdtMarginList" in data[0]
            or "tokenMarginList" in data[0]
            or "usdtOrUsdMarginList" in data[0]
        )  # Adjust based on actual possible keys


def test_get_funding_rate_arbitrage(future_client: FutureClient) -> None:
    """Tests retrieving funding rate arbitrage opportunities."""
    data = future_client.get_funding_rate_arbitrage()
    assert isinstance(data, list)
    # This might be empty depending on market conditions, so check type if non-empty
    if data:
        assert isinstance(
            data[0], dict
        )  # Assuming ArbitrageOpportunityData is TypedDict
        assert "symbol" in data[0]
        assert "profit" in data[0]


# --- Liquidation Tests ---
# Note: Some liquidation endpoints might require specific account levels,
# but per user instruction, we assume the API key has full access.


def test_get_liquidation_history(future_client: FutureClient) -> None:
    """Tests retrieving liquidation history data."""
    data = future_client.get_liquidation_history(limit=10)

    # 基本的な構造のテスト
    assert isinstance(data, list)
    assert len(data) <= 10

    # 各清算データの構造をテスト
    for liquidation in data:
        # 必須フィールドの存在確認
        required_fields = ["longLiquidationUsd", "shortLiquidationUsd", "t"]
        for field in required_fields:
            assert field in liquidation

        # 値の型チェック
        assert isinstance(
            liquidation["longLiquidationUsd"], (int, float, str)
        )  # 数値または文字列として返される
        assert isinstance(
            liquidation["shortLiquidationUsd"], (int, float, str)
        )  # 数値または文字列として返される
        assert isinstance(liquidation["t"], int)

        # 値の範囲チェック
        long_liq = (
            float(liquidation["longLiquidationUsd"])
            if isinstance(liquidation["longLiquidationUsd"], str)
            else liquidation["longLiquidationUsd"]
        )
        short_liq = (
            float(liquidation["shortLiquidationUsd"])
            if isinstance(liquidation["shortLiquidationUsd"], str)
            else liquidation["shortLiquidationUsd"]
        )
        assert long_liq >= 0
        assert short_liq >= 0
        assert liquidation["t"] > 0


def test_get_liquidation_aggregated_history(future_client: FutureClient) -> None:
    """Tests retrieving aggregated liquidation history."""
    data = future_client.get_liquidation_aggregated_history(limit=10)
    assert isinstance(data, list)
    assert len(data) <= 10
    if data:
        assert isinstance(data[0], dict)
        assert "longLiquidationUsd" in data[0]
        assert "shortLiquidationUsd" in data[0]
        assert "t" in data[0]


def test_get_liquidation_coin_list(future_client: FutureClient) -> None:
    """Tests retrieving liquidation data per coin for an exchange."""
    data = future_client.get_liquidation_coin_list(ex="Binance")
    assert isinstance(data, list)
    assert len(data) > 0
    if data:
        assert isinstance(data[0], dict)  # Assuming LiquidationCoinData is TypedDict
        assert "symbol" in data[0]
        assert "liquidationUsd24h" in data[0]  # Check for one of the timeframes


def test_get_liquidation_exchange_list(future_client: FutureClient) -> None:
    """Tests retrieving liquidation data per exchange for a coin."""
    data = future_client.get_liquidation_exchange_list(symbol="BTC", range="4h")
    assert isinstance(data, list)
    assert len(data) > 0
    if data:
        assert isinstance(
            data[0], dict
        )  # Assuming LiquidationExchangeData is TypedDict
        assert "exchange" in data[0]


def test_get_liquidation_order(future_client: FutureClient) -> None:
    """Tests retrieving liquidation orders."""
    # This might return an empty list depending on recent liquidations and threshold
    data = future_client.get_liquidation_order(
        symbol="BTC", minLiquidationAmount="5000"
    )
    assert isinstance(data, list)
    if data:
        assert isinstance(data[0], dict)  # Assuming LiquidationOrderData is TypedDict
        assert "exName" in data[0]


@pytest.mark.skip(reason="Requires Professional Edition")
def test_get_liquidation_aggregated_heatmap(future_client: FutureClient) -> None:
    """Tests retrieving aggregated liquidation heatmap data."""
    data = future_client.get_liquidation_aggregated_heatmap(symbol="BTC", range="3d")
    assert isinstance(data, dict)
    if data:
        assert "data" in data
        assert isinstance(data["data"], list)


@pytest.mark.skip(reason="Requires Professional Edition")
def test_get_liquidation_aggregated_heatmap_model2(future_client: FutureClient) -> None:
    """Tests retrieving aggregated liquidation heatmap data (model 2)."""
    data = future_client.get_liquidation_aggregated_heatmap_model2(
        symbol="BTC", range="3d"
    )
    assert isinstance(data, dict)
    if data:
        assert "data" in data
        assert isinstance(data["data"], list)


@pytest.mark.skip(reason="Requires Professional Edition")
def test_get_liquidation_aggregated_heatmap_model3(future_client: FutureClient) -> None:
    """Tests retrieving aggregated liquidation heatmap data (model 3)."""
    data = future_client.get_liquidation_aggregated_heatmap_model3(
        symbol="BTC", range="3d"
    )
    assert isinstance(data, dict)
    if data:
        assert "data" in data
        assert isinstance(data["data"], list)


@pytest.mark.skip(reason="Requires Professional Edition")
def test_get_liquidation_heatmap(future_client: FutureClient) -> None:
    """Tests retrieving liquidation heatmap data."""
    data = future_client.get_liquidation_heatmap(symbol="BTCUSDT", range="3d")
    assert isinstance(data, dict)
    if data:
        assert "data" in data
        assert isinstance(data["data"], list)


@pytest.mark.skip(reason="Requires Professional Edition")
def test_get_liquidation_heatmap_model2(future_client: FutureClient) -> None:
    """Tests retrieving liquidation heatmap data (model 2)."""
    data = future_client.get_liquidation_heatmap_model2(symbol="BTCUSDT", range="3d")
    assert isinstance(data, dict)
    if data:
        assert "data" in data
        assert isinstance(data["data"], list)


@pytest.mark.skip(reason="Requires Professional Edition")
def test_get_liquidation_heatmap_model3(future_client: FutureClient) -> None:
    """Tests retrieving liquidation heatmap data (model 3)."""
    data = future_client.get_liquidation_heatmap_model3(symbol="BTCUSDT", range="3d")
    assert isinstance(data, dict)
    if data:
        assert "data" in data
        assert isinstance(data["data"], list)


@pytest.mark.skip(reason="Requires Professional Edition")
def test_get_liquidation_map(future_client: FutureClient) -> None:
    """Tests retrieving liquidation map data."""
    data = future_client.get_liquidation_map(symbol="BTCUSDT", range="1d")
    assert isinstance(data, dict)
    if data:
        assert "data" in data
        assert isinstance(data["data"], list)


@pytest.mark.skip(reason="Requires Professional Edition")
def test_get_liquidation_aggregated_map(future_client: FutureClient) -> None:
    """Tests retrieving aggregated liquidation map data."""
    data = future_client.get_liquidation_aggregated_map(symbol="BTC", range="1d")

    # 基本的な構造のテスト
    assert isinstance(data, list)
    assert len(data) > 0

    # 各取引所のデータ構造をテスト
    for exchange_data in data:
        # 必須フィールドの存在確認
        assert isinstance(exchange_data, dict)
        assert "instrument" in exchange_data
        assert "liqMapV2" in exchange_data

        # instrument フィールドの詳細テスト
        instrument = exchange_data["instrument"]
        assert isinstance(instrument, dict)
        assert "instrumentId" in instrument
        assert "exName" in instrument
        assert "baseAsset" in instrument
        assert "quoteAsset" in instrument
        assert "priceTick" in instrument
        assert "fundingInterval" in instrument
        assert "pricePrecision" in instrument
        assert "maxLeverage" in instrument
        assert "type" in instrument

        # 値の型チェック
        assert isinstance(instrument["instrumentId"], str)
        assert isinstance(instrument["exName"], str)
        assert isinstance(instrument["baseAsset"], str)
        assert isinstance(instrument["quoteAsset"], str)
        assert isinstance(instrument["priceTick"], (int, float))
        assert isinstance(instrument["fundingInterval"], int)
        assert isinstance(instrument["pricePrecision"], int)
        assert isinstance(instrument["maxLeverage"], int)
        assert isinstance(instrument["type"], int)

        # liqMapV2 フィールドの詳細テスト
        liq_map = exchange_data["liqMapV2"]
        assert isinstance(liq_map, dict)

        # 少なくとも1つの価格レベルがあることを確認
        assert len(liq_map) > 0

        # 各価格レベルのデータ構造をテスト
        for price, levels in liq_map.items():
            assert isinstance(price, str)
            assert isinstance(levels, list)
            assert len(levels) > 0

            for level in levels:
                assert isinstance(level, list)
                assert len(level) == 4
                assert isinstance(level[0], (int, float))  # 清算価格
                assert isinstance(level[1], (int, float))  # 清算レベル
                assert level[2] is None  # 常にNull
                assert level[3] is None  # 常にNull


# --- Long/Short Ratio Tests ---


def test_get_global_long_short_account_ratio(future_client: FutureClient) -> None:
    """Tests retrieving global long/short account ratio history."""
    data = future_client.get_global_long_short_account_ratio(limit=10)

    # 基本的な構造のテスト
    assert isinstance(data, list)
    assert len(data) <= 10

    # 各データポイントの構造をテスト
    for ratio_data in data:
        # 必須フィールドの存在確認
        required_fields = ["longAccount", "shortAccount", "longShortRatio", "time"]
        for field in required_fields:
            assert field in ratio_data

        # 値の型チェック
        assert isinstance(ratio_data["longAccount"], (int, float))
        assert isinstance(ratio_data["shortAccount"], (int, float))
        assert isinstance(ratio_data["longShortRatio"], (int, float))
        assert isinstance(ratio_data["time"], int)

        # 値の範囲チェック
        assert ratio_data["longAccount"] >= 0
        assert ratio_data["shortAccount"] >= 0
        assert ratio_data["longShortRatio"] >= 0
        assert ratio_data["time"] > 0


def test_get_top_long_short_account_ratio(future_client: FutureClient) -> None:
    """Tests retrieving top long/short account ratio history."""
    data = future_client.get_top_long_short_account_ratio(limit=10)
    assert isinstance(data, list)
    assert len(data) <= 10
    if data:
        assert isinstance(data[0], dict)
        assert (
            "longAccount" in data[0]
            and "shortAccount" in data[0]
            and "longShortRatio" in data[0]
            and "time" in data[0]
        )


def test_get_top_long_short_position_ratio(future_client: FutureClient) -> None:
    """Tests retrieving top long/short position ratio history."""
    data = future_client.get_top_long_short_position_ratio(limit=10)
    assert isinstance(data, list)
    assert len(data) <= 10
    if data:
        assert isinstance(data[0], dict)
        assert (
            "longAccount" in data[0]
            and "shortAccount" in data[0]
            and "longShortRatio" in data[0]
            and "time" in data[0]
        )


def test_get_aggregated_taker_buy_sell_history(future_client: FutureClient) -> None:
    """Tests retrieving aggregated taker buy/sell ratio history."""
    data = future_client.get_aggregated_taker_buy_sell_history(limit=10)
    assert isinstance(data, list)
    assert len(data) <= 10
    if data:
        assert isinstance(
            data[0], dict
        )  # Assuming AggregatedTakerBuySellRatioData is TypedDict
        assert "longShortRatio" in data[0]
        assert "time" in data[0]


def test_get_aggregated_taker_buy_sell_volume_history(
    future_client: FutureClient,
) -> None:
    """Tests retrieving aggregated taker buy/sell volume history."""
    data = future_client.get_aggregated_taker_buy_sell_volume_history(limit=10)
    assert isinstance(data, list)
    assert len(data) <= 10
    if data:
        assert isinstance(
            data[0], dict
        )  # Assuming AggregatedTakerBuySellVolumeData is TypedDict
        assert "buy" in data[0]
        assert "sell" in data[0]
        assert "time" in data[0]  # 'time' represents timestamp


def test_get_taker_buy_sell_ratio_history(future_client: FutureClient) -> None:
    """Tests retrieving taker buy/sell volume history."""
    data = future_client.get_taker_buy_sell_ratio_history(limit=10)
    assert isinstance(data, list)
    assert len(data) <= 10
    if data:
        assert isinstance(data[0], dict)  # Assuming TakerBuySellVolumeData is TypedDict
        assert "buy" in data[0]  # Actual field names from API response


def test_get_exchange_taker_buy_sell_ratio(future_client: FutureClient) -> None:
    """Tests retrieving taker buy/sell ratio per exchange."""
    data = future_client.get_exchange_taker_buy_sell_ratio(symbol="BTC", range="1h")
    assert isinstance(data, dict)  # Assuming ExchangeTakerBuySellRatioData is TypedDict
    assert "buyVolUsd" in data


def test_get_hyperliquid_whale_position(future_client: FutureClient) -> None:
    """Tests retrieving Hyperliquid whale positions."""
    # This endpoint requires Startup Edition or higher, but assumed OK per user.
    data = future_client.get_hyperliquid_whale_position()
    assert isinstance(data, list)
    if data:
        assert isinstance(
            data[0], dict
        )  # Assuming HyperliquidWhalePositionData is TypedDict
        assert "user" in data[0]
        assert "symbol" in data[0]
        assert "positionSize" in data[0]


def test_get_hyperliquid_whale_alert(future_client: FutureClient) -> None:
    """Tests retrieving Hyperliquid whale alerts."""
    # This endpoint requires Startup Edition or higher, but assumed OK per user.
    data = future_client.get_hyperliquid_whale_alert()
    assert isinstance(data, list)
    if data:
        assert isinstance(
            data[0], dict
        )  # Assuming HyperliquidWhaleAlertData is TypedDict
        assert "user" in data[0]
        assert "symbol" in data[0]
        assert "positionSize" in data[0]
        assert "positionAction" in data[0]  # Instead of 'type'


# --- Global Information Tests ---


@pytest.mark.skip(reason="Requires Professional Edition")
def test_get_coins_markets(future_client: FutureClient) -> None:
    """Tests retrieving coin market performance data."""
    data = future_client.get_coins_markets(pageSize=5)
    assert isinstance(data, dict)
    if data:
        assert "data" in data
        assert isinstance(data["data"], list)


def test_get_pairs_markets(future_client: FutureClient) -> None:
    """Tests retrieving pair market performance data."""
    data = future_client.get_pairs_markets(symbol="BTC")

    # データの存在確認
    assert isinstance(data, list)
    assert len(data) > 0

    # 各取引所のデータ構造をテスト
    for market_data in data:
        assert isinstance(market_data, dict)

        # 必須フィールドの存在確認
        required_fields = ["instrumentId", "exName"]
        for field in required_fields:
            assert field in market_data

        # 値の型チェック
        assert isinstance(market_data["instrumentId"], str)
        assert isinstance(market_data["exName"], str)

        # オプショナルフィールドの型チェック
        optional_fields = {
            "fundingRate": (int, float, type(None)),
            "indexPrice": (int, float, type(None)),
            "openInterest": (int, float, type(None)),
            "volUsd": (int, float, type(None)),
            "price": (int, float, type(None)),
            "longNumber": (int, type(None)),
            "shortNumber": (int, type(None)),
            "nextFundingTime": (int, type(None)),
            "expiryDate": (int, type(None)),
        }
        for field, expected_type in optional_fields.items():
            if field in market_data:
                assert isinstance(market_data[field], expected_type)


def test_get_coins_price_change(future_client: FutureClient) -> None:
    """Tests retrieving coin price change data."""
    # Requires Standard Edition or higher, assumed OK.
    data = future_client.get_coins_price_change()
    assert isinstance(data, list)
    assert len(data) > 0
    if data:
        assert isinstance(data[0], dict)  # Assuming CoinPriceChangeData is TypedDict
        assert "symbol" in data[0]
        assert "price" in data[0]
        assert "priceChangePercent1h" in data[0]


# --- Orderbook Tests ---


def test_get_orderbook_bid_ask_range(future_client: FutureClient) -> None:
    """Tests retrieving order book bid/ask range history."""
    data = future_client.get_orderbook_bid_ask_range(limit=10, range="0.5")
    assert isinstance(data, list)
    assert len(data) <= 10
    if data:
        assert isinstance(data[0], dict)  # Assuming OrderbookHistoryData is TypedDict
        assert "asksAmount" in data[0]  # Updated field name


def test_get_aggregated_orderbook_bid_ask_range(future_client: FutureClient) -> None:
    """Tests retrieving aggregated order book bid/ask range history."""
    data = future_client.get_aggregated_orderbook_bid_ask_range(
        limit=10, range="0.5", interval="1h"
    )  # Use '1h' not 'h1'
    assert isinstance(data, list)
    assert len(data) <= 10
    if data:
        assert isinstance(data[0], dict)  # Assuming OrderbookHistoryData is TypedDict
        assert "asksAmount" in data[0]  # Updated field name


# --- Indicator Tests ---


def test_get_rsi_list(future_client: FutureClient) -> None:
    """Tests retrieving RSI data for coins."""
    # Requires Standard Edition or higher, assumed OK.
    data = future_client.get_rsi_list()
    assert isinstance(data, list)
    assert len(data) > 0
    if data:
        assert isinstance(data[0], dict)  # Assuming RsiData is TypedDict
        assert "symbol" in data[0]
        assert "rsi15m" in data[0]  # Check one of the RSI timeframes
        assert "price" in data[0]
