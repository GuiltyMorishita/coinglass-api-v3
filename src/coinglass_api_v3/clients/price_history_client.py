"""
Coinglass Price History Client
===========================

This module provides access to price history related features of the Coinglass API.
"""

from typing import Dict, List, Union, Optional, cast
from .base_client import BaseClient
from ..models import OHLCData
from ..exceptions import CoinglassAPIError


class PriceHistoryClient(BaseClient):
    """Client providing access to price history related endpoints."""

    def get_price_ohlc_history(
        self,
        exchange: str = "Binance",
        symbol: str = "BTCUSDT",
        type: str = "futures",
        interval: str = "1h",
        limit: int = 10,
        startTime: Optional[int] = None,
        endTime: Optional[int] = None,
    ) -> List[OHLCData]:
        """
        Retrieves historical OHLC (Open, High, Low, Close) price data for a cryptocurrency.

        Args:
            exchange: Exchange name (futures or spot, default: "Binance").
            symbol: Currency pair (e.g., "BTCUSDT", default: "BTCUSDT").
            type: Market type ("futures" or "spot", default: "futures").
            interval: Data time interval (e.g., "1m", "3m", ..., "1w", default: "1h").
            limit: Number of data points to return (default: 10, max: 4500).
            startTime: Start timestamp (Unix seconds, optional).
            endTime: End timestamp (Unix seconds, optional).

        Returns:
            A list of historical OHLC price data.

        Raises:
            CoinglassAPIError: If invalid arguments are provided or if API returns an error.
        """
        # 引数の検証
        valid_types = ["futures", "spot"]
        if type not in valid_types:
            raise CoinglassAPIError(
                f"Invalid type: {type}. Must be one of: {', '.join(valid_types)}",
                code="INVALID_ARGUMENT",
            )

        valid_intervals = [
            "1m",
            "3m",
            "5m",
            "15m",
            "30m",
            "1h",
            "2h",
            "4h",
            "6h",
            "8h",
            "12h",
            "1d",
            "1w",
            "1M",
        ]
        if interval not in valid_intervals:
            raise CoinglassAPIError(
                f"Invalid interval: {interval}. Must be one of: {', '.join(valid_intervals)}",
                code="INVALID_ARGUMENT",
            )

        if limit <= 0:
            raise CoinglassAPIError(
                f"Limit must be a positive integer, got {limit}",
                code="INVALID_ARGUMENT",
            )

        if limit > 4500:
            raise CoinglassAPIError(
                f"Limit {limit} exceeds maximum of 4500",
                code="INVALID_ARGUMENT",
            )

        if startTime is not None and endTime is not None and startTime > endTime:
            raise CoinglassAPIError(
                f"startTime ({startTime}) must be less than or equal to endTime ({endTime})",
                code="INVALID_ARGUMENT",
            )

        params: Dict[str, Union[str, int]] = {
            "exchange": exchange,
            "symbol": symbol,
            "type": type,
            "interval": interval,
            "limit": limit,
        }
        if startTime is not None:
            params["startTime"] = startTime
        if endTime is not None:
            params["endTime"] = endTime

        response_data = self._request("GET", "/api/price/ohlc-history", params)

        # Convert API response (list of lists) to List[OHLCData]
        ohlc_data_list: List[OHLCData] = []
        raw_data = response_data.get("data")

        if isinstance(raw_data, list):
            for item in raw_data:
                if isinstance(item, list) and len(item) == 6:
                    try:
                        # Type conversion and mapping to dictionary
                        ohlc_point: OHLCData = {
                            "t": int(item[0]),
                            "o": float(str(item[1])),
                            "h": float(str(item[2])),
                            "l": float(str(item[3])),
                            "c": float(str(item[4])),
                            "v": float(str(item[5])),
                        }
                        ohlc_data_list.append(ohlc_point)
                    except (ValueError, TypeError, IndexError) as e:
                        # エラー処理: 無効なデータポイントの場合は例外を発生させる
                        raise CoinglassAPIError(
                            f"Error parsing OHLC data item: {item}, Error: {e}",
                            code="DATA_PARSE_ERROR",
                        )
                elif isinstance(item, dict) and all(
                    key in item for key in ["t", "o", "h", "l", "c", "v"]
                ):
                    try:
                        # 辞書形式のデータを適切に変換
                        ohlc_point: OHLCData = {
                            "t": int(item["t"]),
                            "o": float(str(item["o"])),
                            "h": float(str(item["h"])),
                            "l": float(str(item["l"])),
                            "c": float(str(item["c"])),
                            "v": float(str(item["v"])),
                        }
                        ohlc_data_list.append(ohlc_point)
                    except (ValueError, TypeError, KeyError) as e:
                        raise CoinglassAPIError(
                            f"Error parsing dict OHLC data item: {item}, Error: {e}",
                            code="DATA_PARSE_ERROR",
                        )
                else:
                    raise CoinglassAPIError(
                        f"Invalid data item format: {item}",
                        code="INVALID_DATA_FORMAT",
                    )
        elif raw_data is not None:
            raise CoinglassAPIError(
                f"Unexpected data format received from API: {type(raw_data)}",
                code="DATA_FORMAT_ERROR",
            )
        else:
            raise CoinglassAPIError(
                "No data found in the API response",
                code="NO_DATA_ERROR",
            )

        return ohlc_data_list
