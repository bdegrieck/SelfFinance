from sqlalchemy import (
    Column,
    DateTime,
    Float,
    Identity,
    Index,
    Integer,
    PrimaryKeyConstraint,
    Unicode,
)

from src.database.entrypoint import Base


class ApartmentSpendingTable(Base):
    __tablename__ = "ApartmentSpending"
    __table_args__ = (PrimaryKeyConstraint("ID", name="PK_ApartmentSpending_ID"),)

    ID = Column("ID", Integer, Identity(start=1), nullable=False, unique=True)
    Date = Column("Date", DateTime, nullable=False, unique=False)
    Amount = Column("Amount", Float, nullable=False, unique=False)
    Description = Column("Description", Unicode(100), nullable=True, unique=False)


class CarTable(Base):
    __tablename__ = "Car"
    __table_args__ = (PrimaryKeyConstraint("ID", name="PK_Car_ID"),)

    ID = Column("ID", Integer, Identity(start=1), nullable=False)
    Date = Column("Date", DateTime, nullable=False, unique=False)
    Amount = Column("Amount", Float, nullable=False, unique=False)
    Description = Column("Description", Unicode(100), nullable=True, unique=False)


class ClothingTable(Base):
    __tablename__ = "Clothing"
    __table_args__ = (PrimaryKeyConstraint("ID", name="PK_Clothing_ID"),)

    ID = Column("ID", Integer, Identity(start=1), nullable=False, unique=True)
    Date = Column("Date", DateTime, nullable=False, unique=False)
    Amount = Column("Amount", Float, nullable=False, unique=False)
    Description = Column("Description", Unicode(100), nullable=True, unique=False)


class EatingOutTable(Base):
    __tablename__ = "EatingOut"
    __table_args__ = (PrimaryKeyConstraint("ID", name="PK_EatingOutExpense_ID"),)

    ID = Column("ID", Integer, nullable=False, unique=True)
    Date = Column("Date", DateTime, nullable=False, unique=False)
    Amount = Column("Amount", Float, nullable=False, unique=False)
    Place = Column("Place", Unicode(50), nullable=False, unique=False)
    Description = Column("Description", Unicode(100), nullable=True, unique=False)


class GiftTable(Base):
    __tablename__ = "Gift"
    __table_args__ = (PrimaryKeyConstraint("ID", name="PK_Gift_ID"),)

    ID = Column("ID", Integer, nullable=False, unique=True)
    Date = Column("Date", DateTime, nullable=False, unique=False)
    Amount = Column("Amount", Float, nullable=False, unique=False)
    Description = Column("Description", Unicode(100), nullable=True, unique=False)


class GroceriesTable(Base):
    __tablename__ = "Groceries"
    __table_args__ = (PrimaryKeyConstraint("ID", name="PK_Groceries_ID"),)

    ID = Column("ID", Integer, Identity(start=1), nullable=False)
    Date = Column("Date", DateTime, nullable=False, unique=False)
    Amount = Column("Amount", Float, nullable=False, unique=False)
    Description = Column("Description", Unicode(100), nullable=True, unique=False)


class IncomeTable(Base):
    __tablename__ = "Income"
    __table_args__ = (PrimaryKeyConstraint("ID", name="PK_Income_ID"),)

    ID = Column("ID", Integer, Identity(start=1), nullable=False, primary_key=True)
    Date = Column("Date", DateTime, nullable=False, unique=False)
    Source = Column("Source", Unicode(50), nullable=False, unique=False)
    GrossPay = Column("GrossPay", Float, nullable=False, unique=False)
    Taxes = Column("Taxes", Float, nullable=True, unique=False)
    NetPay = Column("NetPay", Float, nullable=False, unique=False)


class InvestmentsTable(Base):
    __tablename__ = "Investment"
    __table_args__ = (
        PrimaryKeyConstraint("ID", name="PK_Investment_ID"),
        Index(
            "IX_Investments_ID_FKInvestmentType", "ID", "FKInvestmentType", unique=True
        ),
    )

    ID = Column("ID", Integer, Identity(start=1), nullable=False, unique=True)
    FKInvestmentType = Column("FKInvestmentType", Integer, nullable=False, unique=False)


class InvestmentTypeTable(Base):
    __tablename__ = "InvestmentType"
    __table_args__ = (PrimaryKeyConstraint("ID", name="PK_InvestmentType_ID"),)

    ID = Column("ID", Integer, Identity(start=1), unique=True, nullable=False)
    InvestmentType = Column("InvestmentType", Unicode(50), unique=True, nullable=False)


class MiscExpenseTable(Base):
    __tablename__ = "MiscExpense"
    __table_args__ = (PrimaryKeyConstraint("ID", name="PK_MiscExpense_ID"),)

    ID = Column("ID", Integer, nullable=False, unique=True)
    Date = Column("Date", DateTime, nullable=False, unique=True)
    Amount = Column("Amount", Float, nullable=False, unique=True)
    Description = Column(
        "Description", Unicode(100), nullable=False, unique=True
    )  # have to provide description


class NetWorthTable(Base):
    __tablename__ = "NetWorth"
    __table_args__ = (PrimaryKeyConstraint("ID", name="PK_NetWorth_ID"),)

    ID = Column("ID", Integer, Identity(start=1), unique=True, nullable=False)
    Date = Column("Date", DateTime, unique=False, nullable=False)
    NetWorth = Column("NetWorth", Float, unique=False, nullable=False)


class SinkingFundTable(Base):
    __tablename__ = "SinkingFund"
    __table_args__ = (
        PrimaryKeyConstraint("ID", name="PK_SinkingFund_ID"),
        Index(
            "IX_SinkingFund_ID_FKSinkingFundType",
            "ID",
            "FKSinkingFundType",
            unique=True,
        ),
    )

    ID = Column("ID", Integer, Identity(start=1), unique=True, nullable=False)
    Amount = Column("Amount", Float, unique=False, nullable=False)
    FKSinkingFundType = Column(
        "FKSinkingFundType", Integer, unique=False, nullable=False
    )
    Date = Column("Date", DateTime, unique=False, nullable=False)


class SinkingFundTypeTable(Base):
    __tablename__ = "SinkingFundType"
    __table_args__ = (PrimaryKeyConstraint("ID", name="PK_SinkingFundTypes_ID"),)

    ID = Column("ID", Integer, Identity(start=1), nullable=False, unique=True)
    FundType = Column("FundType", Unicode(50), nullable=False, unique=False)
    Total = Column("Total", Float, nullable=False, unique=False)


class SubscriptionTable(Base):
    __tablename__ = "Subscription"
    __table_args__ = (PrimaryKeyConstraint("ID", name="PK_Subscription_ID"),)

    ID = Column("ID", Integer, unique=False, nullable=False)
    Date = Column("Date", DateTime, unique=False, nullable=False)
    Amount = Column("Amount", Float, unique=False, nullable=False)
    Description = Column("Description", Unicode(100), unique=False, nullable=True)


class VenmoTable(Base):
    __tablename__ = "Venmo"
    __table_args__ = (PrimaryKeyConstraint("ID", name="PK_Venmo_ID"),)

    ID = Column("ID", Integer, unique=True, nullable=False)
    Date = Column("Date", DateTime, unique=False, nullable=False)
    Amount = Column("Amount", Float, unique=False, nullable=False)
    Description = Column("Description", Unicode(100), unique=False, nullable=True)


class LoginTable(Base):
    __tablename__ = "Login"
    __table_args__ = (PrimaryKeyConstraint("ID", name="PK_Login_ID"),)

    ID = Column("ID", Integer, Identity(start=1), nullable=False)
    Username = Column("Username", Unicode(50), nullable=False, unique=True)
    Password = Column("Password", Unicode(100), nullable=False, unique=False)
