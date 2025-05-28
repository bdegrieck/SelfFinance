import datetime as dt

from pydantic import BaseModel


class Category(BaseModel):
    category: str


class Purchase(BaseModel):
    date: dt.datetime
    price: str
    category: str


class Report(BaseModel):
    date: dt.datetime
    total: float
    category: str
