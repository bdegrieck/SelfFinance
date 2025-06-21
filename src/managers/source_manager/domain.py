import datetime as dt
from typing import Optional

from pydantic import BaseModel


class ApartmentExpense(BaseModel):
    date: dt.datetime
    item: str
    amount: float


class CarExpense(BaseModel):
    date: dt.datetime
    item: str
    amount: float


class ClothingExpense(BaseModel):
    date: dt.datetime
    place: str
    amount: float


class EatingOutExpense(BaseModel):
    date: dt.datetime
    place: str
    amount: float


class GiftExpense(BaseModel):
    date: dt.datetime
    amount: float


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
    date: dt.datetime
    item: str
    amount: str


class SubscriptionExpense(BaseModel):
    date: dt.datetime
    item: str
    amount: float


class Venmo(BaseModel):
    date: dt.datetime
    amount: float
    description: Optional[str]
