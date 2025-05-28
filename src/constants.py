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
    # Name of the category this report refers to.  Earlier the field was named
    # ``FKCategory`` which caused confusion when constructing ``Report``
    # instances in tests and when mapping the model to the database entity.
    # Using ``category`` keeps it consistent with ``Purchase`` and the
    # repository/service layer expectations.
    category: str
