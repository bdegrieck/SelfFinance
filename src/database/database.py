from sqlalchemy import (
    Column,
    DateTime,
    Float,
    Identity,
    Index,
    Integer,
    PrimaryKeyConstraint,
    Unicode,
    ForeignKey,
    Text,
    Boolean,
    Date,
    Numeric,
    String,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from src.database.entrypoint import Base


class User(Base):
    """User accounts for the application"""

    __tablename__ = "Users"
    __table_args__ = (PrimaryKeyConstraint("Id", name="PK_users_id"),)

    Id = Column("Id", Integer, Identity(start=1), nullable=False, unique=True)
    Username = Column("Username", String(50), nullable=False, unique=True)
    PasswordHash = Column("PasswordHash", String(255), nullable=False)
    FirstName = Column("FirstName", String(50), nullable=False)
    LastName = Column("LastName", String(50), nullable=False)
    Email = Column("Email", String(100), nullable=False, unique=True)

    # Relationships
    Expenses = relationship("Expense", back_populates="User")
    Incomes = relationship("Income", back_populates="User")
    Investments = relationship("Investment", back_populates="User")
    SinkingFunds = relationship("SinkingFund", back_populates="User")
    NetWorthEntries = relationship("NetWorth", back_populates="User")


class Expense(Base):
    """Unified expenses table - replaces all the separate expense tables"""

    __tablename__ = "Expenses"
    __table_args__ = (
        PrimaryKeyConstraint("Id", name="PK_expenses_id"),
        Index("IX_expenses_date_user_id", "Date", "UserId"),
    )

    Id = Column("Id", Integer, Identity(start=1), nullable=False, unique=True)
    UserId = Column("UserId", Integer, ForeignKey("Users.Id"), nullable=False)
    Category = Column(
        "Category", String(50), nullable=False
    )  # Direct string field instead of foreign key
    Amount = Column("Amount", Numeric(10, 2), nullable=False)
    Description = Column("Description", Text, nullable=True)
    Date = Column("Date", Date, nullable=False)
    Place = Column(
        "Place", String(100), nullable=True
    )  # For eating out, shopping, etc.

    # Relationships
    User = relationship("User", back_populates="Expenses")


class Income(Base):
    """Income sources and amounts"""

    __tablename__ = "Incomes"
    __table_args__ = (
        PrimaryKeyConstraint("Id", name="PK_incomes_id"),
        Index("IX_incomes_user_id", "UserId"),
        Index("IX_incomes_date", "Date"),
    )

    Id = Column("Id", Integer, Identity(start=1), nullable=False, unique=True)
    UserId = Column("UserId", Integer, ForeignKey("Users.Id"), nullable=False)
    Category = Column(
        "Category", String(50), nullable=False
    )  # Direct string field instead of foreign key
    Source = Column(
        "Source", String(100), nullable=False
    )  # Company name, freelance client, etc.
    GrossPay = Column("GrossPay", Numeric(10, 2), nullable=False)
    Taxes = Column("Taxes", Numeric(10, 2), nullable=True)
    NetPay = Column("NetPay", Numeric(10, 2), nullable=False)
    Date = Column("Date", Date, nullable=False)
    Description = Column("Description", Text, nullable=True)
    IsRecurring = Column("IsRecurring", Boolean, default=False, nullable=False)

    # Relationships
    User = relationship("User", back_populates="Incomes")


class Investment(Base):
    """Investment tracking"""

    __tablename__ = "Investments"
    __table_args__ = (
        PrimaryKeyConstraint("Id", name="PK_investments_id"),
        Index("IX_investments_user_id", "UserId"),
        Index("IX_investments_date", "Date"),
    )

    Id = Column("Id", Integer, Identity(start=1), nullable=False, unique=True)
    UserId = Column("UserId", Integer, ForeignKey("Users.Id"), nullable=False)
    InvestmentType = Column("InvestmentType", Unicode(50), nullable=False)
    Amount = Column("Amount", Numeric(10, 2), nullable=False)
    Date = Column("Date", Date, nullable=False)
    Description = Column("Description", Text, nullable=True)

    # Relationships
    User = relationship("User", back_populates="Investments")


class SinkingFund(Base):
    """Sinking funds for future expenses"""

    __tablename__ = "SinkingFunds"
    __table_args__ = (
        PrimaryKeyConstraint("Id", name="PK_sinking_funds_id"),
        Index("IX_sinking_funds_user_id", "UserId"),
    )

    Id = Column("Id", Integer, Identity(start=1), nullable=False, unique=True)
    UserId = Column("UserId", Integer, ForeignKey("Users.Id"), nullable=False)
    SinkingFundType = Column("SinkingFundType", Unicode(50), nullable=False)
    Amount = Column("Amount", Numeric(10, 2), nullable=False)
    Date = Column("Date", Date, nullable=False)
    Description = Column("Description", Text, nullable=True)

    # Relationships
    User = relationship("User", back_populates="SinkingFunds")


class NetWorth(Base):
    """Net worth tracking over time"""

    __tablename__ = "NetWorth"
    __table_args__ = (
        PrimaryKeyConstraint("Id", name="PK_net_worth_id"),
        Index("IX_net_worth_user_id", "UserId"),
        Index("IX_net_worth_date", "Date"),
    )

    Id = Column("Id", Integer, Identity(start=1), nullable=False, unique=True)
    UserId = Column("UserId", Integer, ForeignKey("Users.Id"), nullable=False)
    Date = Column("Date", Date, nullable=False)
    TotalAssets = Column("TotalAssets", Numeric(12, 2), nullable=False)
    TotalLiabilities = Column("TotalLiabilities", Numeric(12, 2), nullable=False)
    NetWorth = Column("NetWorth", Numeric(12, 2), nullable=False)

    # Relationships
    User = relationship("User", back_populates="NetWorthEntries")


class Subscription(Base):
    """Recurring subscriptions"""

    __tablename__ = "Subscriptions"
    __table_args__ = (
        PrimaryKeyConstraint("Id", name="PK_subscriptions_id"),
        Index("IX_subscriptions_user_id", "UserId"),
        Index("IX_subscriptions_active", "IsActive"),
    )

    Id = Column("Id", Integer, Identity(start=1), nullable=False, unique=True)
    UserId = Column("UserId", Integer, ForeignKey("Users.Id"), nullable=False)
    Name = Column("Name", String(100), nullable=False)
    Amount = Column("Amount", Numeric(10, 2), nullable=False)
    Frequency = Column("Frequency", String(20), nullable=False)  # monthly, yearly, etc.
    StartDate = Column("StartDate", Date, nullable=False)
    EndDate = Column("EndDate", Date, nullable=True)
    IsActive = Column("IsActive", Boolean, default=True, nullable=False)
    Description = Column("Description", Text, nullable=True)
    CreatedAt = Column("CreatedAt", DateTime, server_default=func.now(), nullable=False)
    UpdatedAt = Column(
        "UpdatedAt",
        DateTime,
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    # Relationships
    User = relationship("User", back_populates="Subscriptions")


# Add subscriptions relationship to User
User.Subscriptions = relationship("Subscription", back_populates="User")
