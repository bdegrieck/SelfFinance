import datetime as dt
from typing import Optional

from pydantic import BaseModel, Field


class ApartmentExpense(BaseModel):
    """Apartment related spending.

    date (datetime): date of the expense
    amount (float): amount spent on the apartment
    description (str, optional): details of the expense
    """

    date: dt.datetime
    amount: float
    description: Optional[str] = None


class CarExpense(BaseModel):
    """Expenses related to car ownership.

    date (datetime): when the expense occurred
    amount (float): cost of the expense
    description (str, optional): explanation of the expense
    """

    date: dt.datetime
    amount: float
    description: Optional[str] = None


class ClothingExpense(BaseModel):
    """Clothing purchases.

    date (datetime): date of purchase
    amount (float): amount spent on clothing
    description (str, optional): notes about the purchase
    """

    date: dt.datetime
    amount: float
    description: Optional[str] = None


class EatingOutExpense(BaseModel):
    """Meals or snacks purchased outside the home.

    date (datetime): when the meal was purchased
    place (str): location of the purchase
    amount (float): cost of the meal
    description (str, optional): extra details
    """

    date: dt.datetime
    place: str
    amount: float
    description: Optional[str] = None


class GiftExpense(BaseModel):
    """Gifts purchased for others.

    date (datetime): when the gift was bought
    amount (float): cost of the gift
    description (str, optional): notes about the gift
    """

    date: dt.datetime
    amount: float
    description: Optional[str] = None


class GroceriesExpense(BaseModel):
    """Groceries and household supplies.

    date (datetime): date of purchase
    amount (float): total amount spent
    description (str, optional): additional notes
    """

    date: dt.datetime
    amount: float
    description: Optional[str]


class Income(BaseModel):
    """Income received from any source.

    date (datetime): date the income was received
    source (str): source of the income
    gross_pay (float): total income before taxes
    taxes (float): taxes withheld
    """

    date: dt.datetime
    source: str
    gross_pay: float
    taxes: float


class Meta(BaseModel):
    """Meta information for data exports.

    month (str): month represented by the data
    year (str): year represented by the data
    """

    month: str
    year: str


class MiscExpense(BaseModel):
    """Miscellaneous expenses that don't fit other categories.

    date (datetime): when the expense occurred
    amount (float): amount of the expense
    description (str): description of the expense
    """

    date: dt.datetime
    amount: float
    description: str


class SubscriptionExpense(BaseModel):
    """Recurring subscription costs.

    date (datetime): date of the charge
    amount (float): subscription amount
    description (str, optional): notes about the subscription
    """

    date: dt.datetime
    amount: float
    description: Optional[str] = None


class Venmo(BaseModel):
    """Transactions sent or received via Venmo.

    date (datetime): date of the transaction
    amount (float): amount of money transferred
    description (str, optional): notes about the transaction
    """

    date: dt.datetime
    amount: float
    description: Optional[str]


class Investment(BaseModel):
    """Investment holding record.

    fk_investment_type (int): foreign key to the investment type
    """

    fk_investment_type: int


class InvestmentType(BaseModel):
    """Type of investment available.

    investment_type (str): descriptive name of the investment type
    """

    investment_type: str


class NetWorth(BaseModel):
    """Snapshot of overall financial value.

    date (datetime): date of calculation
    net_worth (float): total value of assets minus liabilities
    """

    date: dt.datetime
    net_worth: float


class SinkingFund(BaseModel):
    """Money set aside for a specific future purpose.

    amount (float): value of the fund
    fk_sinking_fund_type (int): foreign key to the fund type
    date (datetime): date of the entry
    """

    amount: float
    fk_sinking_fund_type: int
    date: dt.datetime


class SinkingFundType(BaseModel):
    """Types of sinking funds that can be created.

    fund_type (str): name of the fund type
    total (float): current total balance for the type
    """

    fund_type: str
    total: float


class Login(BaseModel):
    """Login for the user

    username (str): username of the user
    password (str): password of the user
    """

    username: str
    password: str


class CreateUser(BaseModel):
    """
    Info for creating a user

    username (str): username for the new user
    password (str): password for the new user
    first_name (str): first name of the new user
    last_name (str): last name of teh new user
    email (str): email of the new user
    """

    username: str = Field(min_length=5, max_length=25)
    password: str = Field(min_length=5, max_length=25)
    first_name: str = Field(min_length=2, max_length=25)
    last_name: str = Field(min_length=2, max_length=25)
    email: str =  Field(min_length=2, max_length=25)