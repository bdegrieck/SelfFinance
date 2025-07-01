import datetime as dt
from typing import Optional

from pydantic import BaseModel


class ApartmentExpense(BaseModel):
    """Domain model for :class:`ApartmentSpendingTable`."""

    date: dt.datetime
    amount: float
    description: Optional[str] = None


class CarExpense(BaseModel):
    """Domain model for :class:`CarTable`."""

    date: dt.datetime
    amount: float
    description: Optional[str] = None


class ClothingExpense(BaseModel):
    """Domain model for :class:`ClothingTable`."""

    date: dt.datetime
    amount: float
    description: Optional[str] = None


class EatingOutExpense(BaseModel):
    """Domain model for :class:`EatingOutTable`."""

    date: dt.datetime
    place: str
    amount: float
    description: Optional[str] = None


class GiftExpense(BaseModel):
    """Domain model for :class:`GiftTable`."""

    date: dt.datetime
    amount: float
    description: Optional[str] = None


class GroceriesExpense(BaseModel):
    date: dt.datetime
    amount: float
    description: Optional[str]


class Income(BaseModel):
    date: dt.datetime
    source: str
    gross_pay: float
    taxes: float


class Meta(BaseModel):
    month: str
    year: str


class MiscExpense(BaseModel):
    """Domain model for :class:`MiscExpenseTable`."""

    date: dt.datetime
    amount: float
    description: str


class SubscriptionExpense(BaseModel):
    """Domain model for :class:`SubscriptionTable`."""

    date: dt.datetime
    amount: float
    description: Optional[str] = None


class Venmo(BaseModel):
    date: dt.datetime
    amount: float
    description: Optional[str]


class Investment(BaseModel):
    """Domain model for :class:`InvestmentsTable`."""

    fk_investment_type: int


class InvestmentType(BaseModel):
    """Domain model for :class:`InvestmentTypeTable`."""

    investment_type: str


class NetWorth(BaseModel):
    """Domain model for :class:`NetWorthTable`."""

    date: dt.datetime
    net_worth: float


class SinkingFund(BaseModel):
    """Domain model for :class:`SinkingFundTable`."""

    amount: float
    fk_sinking_fund_type: int
    date: dt.datetime


class SinkingFundType(BaseModel):
    """Domain model for :class:`SinkingFundTypeTable`."""

    fund_type: str
    total: float


class Login(BaseModel):
    """Domain model for :class:`LoginTable`."""

    username: str
    password: str
