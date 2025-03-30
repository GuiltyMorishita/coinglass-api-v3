"""
Coinglass Indicator Client
=========================

This module provides access to indicator-related features of the Coinglass API.
"""

from typing import List, cast, Dict, Any, Optional
from .base_client import BaseClient
from ..models import (
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


class IndicatorClient(BaseClient):
    """Client providing access to indicator-related endpoints."""

    # Indicator Related Methods

    def get_bull_market_peak_indicators(self) -> List[BullMarketPeakIndicatorData]:
        """Gets the list of bull market peak indicators.

        Returns:
            A list of bull market peak indicator data.
        """
        response = self._request("GET", "/api/bull-market-peak-indicator")
        return cast(List[BullMarketPeakIndicatorData], response["data"])

    def get_bitcoin_bubble_index(self) -> List[BitcoinBubbleIndexData]:
        """Gets the historical data for the Bitcoin Bubble Index.

        Returns:
            A list of Bitcoin Bubble Index data.
        """
        response = self._request("GET", "/api/index/bitcoin-bubble-index")
        return cast(List[BitcoinBubbleIndexData], response["data"])

    def get_ahr999_index(self) -> List[AHR999Data]:
        """Gets the historical data for the AHR999 index.

        Returns:
            A list of AHR999 index data.
        """
        response = self._request("GET", "/api/index/ahr999")
        return cast(List[AHR999Data], response["data"])

    def get_two_year_ma_multiplier(self) -> List[TwoYearMAMultiplierData]:
        """Gets the historical data for the Two Year MA Multiplier index.

        Returns:
            A list of Two Year MA Multiplier index data.
        """
        # Note: API endpoint has a typo "tow" instead of "two"
        response = self._request("GET", "/api/index/tow-year-ma-multiplier")
        return cast(List[TwoYearMAMultiplierData], response["data"])

    def get_200w_ma_heatmap(self) -> List[MovingAvgHeatmapData]:
        """Gets the historical data for the 200-Week Moving Average Heatmap.

        Returns:
            A list of 200-Week Moving Average Heatmap data.
        """
        # Note: API endpoint has a typo "tow" instead of "two"
        response = self._request(
            "GET", "/api/index/tow-hundred-week-moving-avg-heatmap"
        )
        return cast(List[MovingAvgHeatmapData], response["data"])

    def get_puell_multiple(self) -> List[PuellMultipleData]:
        """Gets the historical data for the Puell Multiple index.

        Returns:
            A list of Puell Multiple index data.
        """
        response = self._request("GET", "/api/index/puell-multiple")
        return cast(List[PuellMultipleData], response["data"])

    def get_stock_flow(self) -> List[StockFlowData]:
        """Gets the historical data for the Stock-to-Flow model.

        Returns:
            A list of Stock-to-Flow model data.
        """
        response = self._request("GET", "/api/index/stock-flow")
        return cast(List[StockFlowData], response["data"])

    def get_pi_cycle_top_indicator(self) -> List[PiCycleTopIndicatorData]:
        """Gets the historical data for the Pi Cycle Top Indicator.

        Returns:
            A list of Pi Cycle Top Indicator data.
        """
        response = self._request("GET", "/api/index/pi")
        return cast(List[PiCycleTopIndicatorData], response["data"])

    def get_golden_ratio_multiplier(self) -> List[GoldenRatioMultiplierData]:
        """Gets the historical data for the Golden Ratio Multiplier.

        Returns:
            A list of Golden Ratio Multiplier data.
        """
        response = self._request("GET", "/api/index/golden-ratio-multiplier")
        raw_data_list = response.get("data", [])
        processed_data: List[GoldenRatioMultiplierData] = []

        key_map = {
            "1.6AccumulationHigh": "AccumulationHigh1_6",
            "2LowBullHigh": "LowBullHigh2",
        }
        float_keys = [
            "x8",
            "x21",
            "x13",
            "x3",
            "x5",
            "ma350",
            "LowBullHigh2",
            "AccumulationHigh1_6",
        ]

        for raw_item in raw_data_list:
            processed_item: Dict[str, Any] = {}
            for key, value in raw_item.items():
                new_key = key_map.get(key, key)
                if new_key in GoldenRatioMultiplierData.__annotations__:
                    if new_key in float_keys and isinstance(value, str):
                        processed_item[new_key] = float(value)
                    elif new_key == "createTime" and isinstance(value, int):
                        processed_item[new_key] = value
                    elif new_key == "price" and isinstance(value, (int, float)):
                        processed_item[new_key] = float(value)
                    elif isinstance(value, (str, int, float, bool)):
                        processed_item[new_key] = value
                    else:
                        processed_item[new_key] = value
                else:
                    pass

            # Ensure all keys from the model are present, adding None if missing
            for model_key in GoldenRatioMultiplierData.__annotations__.keys():
                if model_key not in processed_item:
                    processed_item[model_key] = None

            processed_data.append(cast(GoldenRatioMultiplierData, processed_item))

        return processed_data

    def get_bitcoin_profitable_days(self) -> List[BitcoinProfitableDaysData]:
        """Gets the historical data for Bitcoin Profitable Days.

        Returns:
            A list of Bitcoin Profitable Days data.
        """
        response = self._request("GET", "/api/index/bitcoin-profitable-days")
        return cast(List[BitcoinProfitableDaysData], response["data"])

    def get_bitcoin_rainbow_chart(self) -> List[BitcoinRainbowChartDataPoint]:
        """Gets the historical data for the Bitcoin Rainbow Chart.

        The API returns a list of lists. This method converts it into a list of
        BitcoinRainbowChartDataPoint dictionaries.

        Returns:
            A list of Bitcoin Rainbow Chart data points.
        """
        response = self._request("GET", "/api/index/bitcoin-rainbow-chart")
        raw_data = response.get("data", [])
        processed_data: List[BitcoinRainbowChartDataPoint] = []

        keys = list(BitcoinRainbowChartDataPoint.__annotations__.keys())

        if len(keys) != 12:
            # Definition mismatch, return empty
            return []

        for item_list in raw_data:
            if isinstance(item_list, list) and len(item_list) == 12:
                point_data: Dict[str, Any] = {}
                valid_point = True
                for i, key in enumerate(keys):
                    value = item_list[i]
                    if i < 11:  # Float fields
                        if value is None:
                            point_data[key] = None
                        else:
                            try:
                                point_data[key] = float(value)
                            except (ValueError, TypeError):
                                # Invalid float value, skip this point
                                valid_point = False
                                break
                    else:  # Timestamp field 't'
                        try:
                            point_data[key] = int(value)
                        except (ValueError, TypeError):
                            # Invalid int value, skip this point
                            valid_point = False
                            break
                if valid_point:
                    processed_data.append(
                        cast(BitcoinRainbowChartDataPoint, point_data)
                    )
            # Skip invalid formats silently

        return processed_data

    def get_fear_greed_history(self) -> List[FearGreedHistoryData]:
        """Gets historical data for the Crypto Fear & Greed Index.

        The API returns a dictionary with lists for dates, values, and prices.
        This method combines them into a list of FearGreedHistoryData objects.

        Returns:
            A list of Fear & Greed Index historical data points.
        """
        response = self._request("GET", "/api/index/fear-greed-history")
        raw_data = response.get("data", {})
        dates = raw_data.get("dates", [])
        values = raw_data.get("values", [])
        prices = raw_data.get("prices", [])
        processed_data: List[FearGreedHistoryData] = []

        if not (len(dates) == len(values) == len(prices)):
            raise ValueError("Mismatched lengths in Fear & Greed history data")

        for i in range(len(dates)):
            timestamp = int(dates[i])
            index_value = float(values[i])
            price_value = float(prices[i])
            processed_data.append(
                cast(
                    FearGreedHistoryData,
                    {"t": timestamp, "value": index_value, "price": price_value},
                )
            )

        return processed_data

    # TODO: Implement StableCoin MarketCap History (documentation pending)

    # Grayscale Related Methods

    def get_grayscale_holdings_list(self) -> List[GrayscaleHoldingData]:
        """Gets the list of Grayscale holdings.

        Returns:
            A list of Grayscale holding data.
        """
        response = self._request("GET", "/api/grayscale/holdings-list")
        return cast(List[GrayscaleHoldingData], response["data"])

    def get_grayscale_premium_history(
        self, symbol: str = "BTC"
    ) -> List[GrayscalePremiumHistoryData]:
        """Gets the Grayscale premium history for the specified symbol.

        Combines data from multiple lists in the API response into a list of objects.

        Args:
            symbol: Symbol (e.g., "BTC"). Defaults to "BTC".

        Returns:
            A list of Grayscale premium history data points.
        """
        params: Dict[str, str] = {"symbol": symbol}
        response = self._request("GET", "/api/grayscale/premium-history", params)
        raw_data = response.get("data", {})

        dates = raw_data.get("dateList", [])
        prices = raw_data.get("secondaryMarketPricePriceList", [])
        rates = raw_data.get("premiumRateList", [])

        processed_data: List[GrayscalePremiumHistoryData] = []

        if not (len(dates) == len(prices) == len(rates)):
            raise ValueError("Mismatched lengths in Grayscale premium history data")

        for i in range(len(dates)):
            timestamp = int(dates[i])
            price_val = prices[i]
            rate_val = rates[i]
            price = float(price_val) if price_val is not None else None
            rate = float(rate_val) if rate_val is not None else None

            processed_data.append(
                cast(
                    GrayscalePremiumHistoryData,
                    {
                        "t": timestamp,
                        "secondaryMarketPrice": price,
                        "premiumRate": rate,
                    },
                )
            )

        return processed_data

    def get_borrow_interest_rate_history(
        self,
        exchange: str = "Binance",
        symbol: str = "BTC",
        interval: str = "h1",
        limit: Optional[int] = None,  # Optional parameter
        start_time: Optional[int] = None,  # Optional parameter
        end_time: Optional[int] = None,  # Optional parameter
    ) -> List[BorrowInterestRateData]:
        """Gets the borrow interest rate history for the specified exchange and symbol.

        Args:
            exchange: Exchange name (e.g., "Binance", "OKX"). Defaults to "Binance".
            symbol: Trading coin (e.g., "BTC"). Defaults to "BTC".
            interval: Time interval ("1m", "3m", "5m", "15m", "30m", "1h", "4h", "6h", "8h", "12h", "1d", "1w"). Defaults to "h1".
            limit: Number of data points to fetch. Defaults to API setting (500 or 1000). Max 4500.
            start_time: Start timestamp (seconds).
            end_time: End timestamp (seconds).

        Returns:
            A list of borrow interest rate history data.
        """
        params: Dict[str, Any] = {
            "exchange": exchange,
            "symbol": symbol,
            "interval": interval,
        }
        if limit is not None:
            params["limit"] = limit
        if start_time is not None:
            params["startTime"] = start_time
        if end_time is not None:
            params["endTime"] = end_time

        response = self._request("GET", "/api/borrowInterestRate/history", params)
        return cast(List[BorrowInterestRateData], response["data"])

    def get_exchange_balance_list(
        self, symbol: str = "BTC"
    ) -> List[ExchangeBalanceListData]:
        """Gets the list of exchange balances for the specified symbol.

        Args:
            symbol: Trading coin (e.g., "BTC"). Defaults to "BTC".

        Returns:
            A list of exchange balance data.
        """
        params: Dict[str, str] = {"symbol": symbol}
        response = self._request("GET", "/api/exchange/balance/v2/list", params)
        return cast(List[ExchangeBalanceListData], response["data"])

    def get_exchange_balance_chart(self, symbol: str) -> ExchangeBalanceChartData:
        """Retrieves exchange balance chart data for a given symbol.

        Args:
            symbol: The symbol for which to retrieve data (e.g., "BTC").

        Returns:
            ExchangeBalanceChartData: A dictionary containing the timestamp list
                                       and a map of exchange balances.

        Raises:
            RequestException: If the API request fails.
            ValueError: If the response data is not in the expected format.
        """
        endpoint = "/api/exchange/balance/chart"
        params = {"symbol": symbol}
        response = self._request("GET", endpoint, params=params)
        response_data = response.get("data")  # Access the 'data' field

        # Validate the structure within the 'data' field
        if (
            isinstance(response_data, dict)
            and "timeList" in response_data
            and isinstance(response_data["timeList"], list)
            and "dataMap" in response_data
            and isinstance(response_data["dataMap"], dict)
            and "priceList" in response_data  # Check for priceList
            and isinstance(response_data["priceList"], list)
        ):
            # Further validation could be added here if needed,
            # e.g., checking list lengths and types within dataMap and priceList.
            return ExchangeBalanceChartData(**response_data)
        else:
            # If data format is unexpected, raise ValueError
            raise ValueError("Unexpected data format received from API.")
