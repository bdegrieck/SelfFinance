import datetime as dt

import pandera as pa
from pandera import Field


class ApartmentSpendingDataFrame(pa.DataFrameModel):
    Date: dt.datetime = Field(nullable=False)
    Item: str = Field(nullable=False)
    Amount: float = Field(nullable=False)


class CarExpensesDataFrame(pa.DataFrameModel):
    Date: dt.datetime = Field(nullable=False)
    Item: str = Field(nullable=False)
    Amount: float = Field(nullable=False)


class ClothingDataFrame(pa.DataFrameModel):
    Date: dt.datetime = Field(nullable=False)
    Place: str = Field(nullable=False)
    Amount: float = Field(nullable=False)


class EatingOutDataFrame(pa.DataFrameModel):
    Date: dt.datetime = Field(nullable=False)
    Place: str = Field(nullable=False)
    Amount: str = Field(nullable=False)


class GiftsDataFrame(pa.DataFrameModel):
    Date: dt.datetime = Field(nullable=False)
    Amount: str = Field(nullable=False)


class GroceriesDataFrame(pa.DataFrameModel):
    Date: dt.datetime = Field(nullable=False)
    Place: str = Field(nullable=False)
    Amount: float = Field(nullable=False)


class IncomeDataFrame(pa.DataFrameModel):
    Date: dt.datetime = Field(nullable=False)
    Source: str = Field(nullable=False)
    GrossPay: float = Field(nullable=False)
    Taxes: float = Field(nullable=True)


class MetaDataFrame(pa.DataFrameModel):
    Month: str = Field(nullable=False)
    Year: str = Field(nullable=False)


class MiscDataFrame(pa.DataFrameModel):
    Date: dt.datetime = Field(nullable=False)
    Item: str = Field(nullable=False)
    Amount: str = Field(nullable=False)


class MonthlyExpensesDataFrame(pa.DataFrameModel):
    Date: dt.datetime = Field(nullable=False)
    Amount: float = Field(nullable=False)

class SubscriptionsDataFrame(pa.DataFrameModel):
    Date: dt.datetime = Field(nullable=False)
    Item: str = Field(nullable=False)
    Amount: float = Field(nullable=False)


class VenmoDataFrame(pa.DataFrameModel):
    Date: dt.datetime = Field(nullable=False)
    Description: str = Field(nullable=False)
    Amount: float = Field(nullable=False)
