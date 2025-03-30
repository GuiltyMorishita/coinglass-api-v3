"""Data models related to exchange information and balances."""

from typing import TypedDict, List


class ExchangeBalanceListData(TypedDict):
    """Represents summary data for an exchange's balance.

    Attributes:
        exchangeName: Name of the exchange.
        totalBalance: Total balance amount.
        totalBalanceUsd: Total balance value in USD.
        flowIn: Inflow amount.
        flowInUsd: Inflow value in USD.
        flowOut: Outflow amount.
        flowOutUsd: Outflow value in USD.
        netFlow: Net flow amount.
        netFlowUsd: Net flow value in USD.
    """

    exchangeName: str
    totalBalance: float
    totalBalanceUsd: float
    flowIn: float
    flowInUsd: float
    flowOut: float
    flowOutUsd: float
    netFlow: float
    netFlowUsd: float


class ExchangeBalanceChartData(TypedDict):
    """Represents a data point for an exchange balance chart.

    Attributes:
        balance: Balance amount at the timestamp.
        price: Corresponding price at the timestamp.
        createTime: Timestamp in milliseconds.
    """

    balance: float
    price: float
    createTime: int
