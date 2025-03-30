"""Coinglass API Client
====================

This module implements the client providing access to the Coinglass API.
It provides client classes split by functionality and a main CoinglassAPI class
that integrates them.
"""

from .clients.future_client import FutureClient
from .clients.spot_client import SpotClient
from .clients.onchain_client import OnchainClient
from .clients.price_history_client import PriceHistoryClient
from .clients.indicator_client import IndicatorClient
from .clients.option_client import OptionClient
from .clients.bitcoin_etf_client import BitcoinETFClient
from .clients.ethereum_etf_client import EthereumETFClient
from .clients.orderbook_client import OrderbookClient


class CoinglassAPI:
    """Main Coinglass API client class.

    This class integrates all functional clients.
    Use this class to access all features of the Coinglass API.
    """

    def __init__(self, api_key: str) -> None:
        """Initializes the Coinglass client.

        Args:
            api_key: Your Coinglass API key.
        """
        self.api_key = api_key
        self.future = FutureClient(api_key)
        self.spot = SpotClient(api_key)
        self.onchain = OnchainClient(api_key)
        self.price_history = PriceHistoryClient(api_key)
        self.indicator = IndicatorClient(api_key)
        self.option = OptionClient(api_key)
        self.bitcoin_etf = BitcoinETFClient(api_key)
        self.ethereum_etf = EthereumETFClient(api_key)
        self.orderbook = OrderbookClient(api_key)
