from pydantic import BaseModel
import datetime as dt

from sqlalchemy import Column


class Category(BaseModel):
    category: str


class Purchase(BaseModel):
    date: dt.datetime
    price: str
    category: str


class Report(BaseModel):
    date: dt.datetime
    total: float
    FKCategory: str
