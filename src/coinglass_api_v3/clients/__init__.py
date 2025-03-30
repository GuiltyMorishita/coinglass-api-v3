"""
Coinglass API Clients
===================

This module provides various clients for accessing different aspects of the Coinglass API.
"""

from .future_client import FutureClient
from .spot_client import SpotClient
from .option_client import OptionClient
from .bitcoin_etf_client import BitcoinETFClient
from .ethereum_etf_client import EthereumETFClient
from .indicator_client import IndicatorClient
from .orderbook_client import OrderbookClient
from .price_history_client import PriceHistoryClient
from .onchain_client import OnchainClient
from .websocket_client import CoinglassWebSocketClient as WebSocketClient

__all__ = [
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
