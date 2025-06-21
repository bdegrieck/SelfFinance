import datetime as dt
from typing import Literal, Optional

import pandas as pd
from pydantic import BaseModel


class ExpenseCategory(BaseModel):
    category: Literal[
        "Car",
        "Groceries",
        "Eating Out",
        "Clothing",
        "Apartment Spending",
        "Gifts",
        "Subscriptions",
        "Venmo",
        "Misc",
    ]


class SinkingFundType(BaseModel):
    fund_type: Literal["Vacation", "Emergency", "House"]


class MonthExpenses(BaseModel):
    apartment: pd.DataFrame
    car: pd.DataFrame
    clothing: pd.DataFrame
    eating_out: pd.DataFrame
    gifts: pd.DataFrame
    groceries: pd.DataFrame
    income: pd.DataFrame
    meta: pd.DataFrame
    misc: pd.DataFrame
    subscriptions: pd.DataFrame
    venmo: pd.DataFrame

    class Config:
        allow_arbitrary_types = True


class Expense(BaseModel):
    """
    Expense Base Model Class

    date - date of the expense
    price - price of the expense
    category - category of the purchase
    description - optional description of the description (e.g where the expense is from, what the expense is, why the expense was made)
    """

    date: dt.datetime
    price: str
    category: ExpenseCategory
    descriptions: Optional[str]


class Reports(BaseModel):
    data: list[pd.DataFrame]
    month: int
    year: int

    class Config:
        allow_arbitrary_types = True
