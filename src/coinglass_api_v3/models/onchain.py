"""Data models for on-chain data, such as whale activities."""

from typing import TypedDict


class ExchangeOnchainTransferData(TypedDict):
    """Represents a single on-chain transfer involving an exchange.

    Attributes:
        txHash: Transaction hash.
        symbol: Asset symbol (e.g., "USDT").
        usd: Value of the transfer in USD.
        amount: Amount of the asset transferred.
        exName: Name of the exchange involved.
        side: Transaction side (1: Inflow to exchange, 2: Outflow from exchange).
        from_: Sender address (renamed from 'from' due to keyword conflict).
        to: Receiver address.
    """

    txHash: str
    symbol: str
    usd: float
    amount: float
    exName: str
    side: int
    from_: str  # Mapped from 'from'
    to: str
