"""
Coinglass API SDK
================

This module provides the main entry point for the Coinglass API SDK,
simplifying access to its functionalities.
"""

from .client import CoinglassAPI
from .exceptions import CoinglassAPIError

from .clients.future_client import FutureClient
from .clients.spot_client import SpotClient
from .clients.option_client import OptionClient
from .clients.bitcoin_etf_client import BitcoinETFClient
from .clients.ethereum_etf_client import EthereumETFClient
from .clients.indicator_client import IndicatorClient
from .clients.orderbook_client import OrderbookClient
from .clients.price_history_client import PriceHistoryClient
from .clients.onchain_client import OnchainClient
from .clients.websocket_client import CoinglassWebSocketClient as WebSocketClient

# Public API exports
__all__ = [
    "CoinglassAPI",
    "CoinglassAPIError",
    "FutureClient",
    "SpotClient",
    "OptionClient",
    "BitcoinETFClient",
    "EthereumETFClient",
    "IndicatorClient",
    "OrderbookClient",
    "PriceHistoryClient",
    "OnchainClient",
    "WebSocketClient",
]

__version__ = "0.1.0"
