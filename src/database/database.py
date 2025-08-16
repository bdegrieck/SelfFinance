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
    __tablename__ = "users"
    __table_args__ = (PrimaryKeyConstraint("id", name="PK_users_id"),)

    id = Column("id", Integer, Identity(start=1), nullable=False, unique=True)
    username = Column("username", String(50), nullable=False, unique=True)
    password_hash = Column("password_hash", String(255), nullable=False)
    first_name = Column("first_name", String(50), nullable=False)
    last_name = Column("last_name", String(50), nullable=False)
    email = Column("email", String(100), nullable=False, unique=True)

    # Relationships
    expenses = relationship("Expense", back_populates="user")
    incomes = relationship("Income", back_populates="user")
    investments = relationship("Investment", back_populates="user")
    sinking_funds = relationship("SinkingFund", back_populates="user")
    net_worth_entries = relationship("NetWorth", back_populates="user")


class Category(Base):
    """Expense and income categories"""
    __tablename__ = "categories"
    __table_args__ = (PrimaryKeyConstraint("id", name="PK_categories_id"),)

    id = Column("id", Integer, Identity(start=1), nullable=False, unique=True)
    name = Column("name", String(100), nullable=False, unique=True)
    type = Column("type", String(20), nullable=False)  # 'expense', 'income', 'investment'
    color = Column("color", String(7), nullable=True)  # Hex color for UI
    icon = Column("icon", String(50), nullable=True)   # Icon name for UI
    is_active = Column("is_active", Boolean, default=True, nullable=False)
    created_at = Column("created_at", DateTime, server_default=func.now(), nullable=False)

    # Relationships
    expenses = relationship("Expense", back_populates="category")
    incomes = relationship("Income", back_populates="category")


class Expense(Base):
    """Unified expenses table - replaces all the separate expense tables"""
    __tablename__ = "expenses"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="PK_expenses_id"),
        Index("IX_expenses_user_id", "user_id"),
        Index("IX_expenses_category_id", "category_id"),
        Index("IX_expenses_date", "date"),
        Index("IX_expenses_user_date", "user_id", "date"),
    )

    id = Column("id", Integer, Identity(start=1), nullable=False, unique=True)
    user_id = Column("user_id", Integer, ForeignKey("users.id"), nullable=False)
    category_id = Column("category_id", Integer, ForeignKey("categories.id"), nullable=False)
    amount = Column("amount", Numeric(10, 2), nullable=False)
    description = Column("description", Text, nullable=True)
    date = Column("date", Date, nullable=False)
    place = Column("place", String(100), nullable=True)  # For eating out, shopping, etc.
    tags = Column("tags", String(500), nullable=True)    # Comma-separated tags
    is_recurring = Column("is_recurring", Boolean, default=False, nullable=False)
    recurring_frequency = Column("recurring_frequency", String(20), nullable=True)  # monthly, weekly, etc.
    created_at = Column("created_at", DateTime, server_default=func.now(), nullable=False)
    updated_at = Column("updated_at", DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

    # Relationships
    user = relationship("User", back_populates="expenses")
    category = relationship("Category", back_populates="expenses")


class Income(Base):
    """Income sources and amounts"""
    __tablename__ = "incomes"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="PK_incomes_id"),
        Index("IX_incomes_user_id", "user_id"),
        Index("IX_incomes_date", "date"),
    )

    id = Column("id", Integer, Identity(start=1), nullable=False, unique=True)
    user_id = Column("user_id", Integer, ForeignKey("users.id"), nullable=False)
    category_id = Column("category_id", Integer, ForeignKey("categories.id"), nullable=False)
    source = Column("source", String(100), nullable=False)  # Company name, freelance client, etc.
    gross_pay = Column("gross_pay", Numeric(10, 2), nullable=False)
    taxes = Column("taxes", Numeric(10, 2), nullable=True)
    net_pay = Column("net_pay", Numeric(10, 2), nullable=False)
    date = Column("date", Date, nullable=False)
    description = Column("description", Text, nullable=True)
    is_recurring = Column("is_recurring", Boolean, default=False, nullable=False)
    recurring_frequency = Column("recurring_frequency", String(20), nullable=True)
    created_at = Column("created_at", DateTime, server_default=func.now(), nullable=False)

    # Relationships
    user = relationship("User", back_populates="incomes")
    category = relationship("Category", back_populates="incomes")


class Investment(Base):
    """Investment tracking"""
    __tablename__ = "investments"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="PK_investments_id"),
        Index("IX_investments_user_id", "user_id"),
        Index("IX_investments_type_id", "investment_type_id"),
        Index("IX_investments_date", "date"),
    )

    id = Column("id", Integer, Identity(start=1), nullable=False, unique=True)
    user_id = Column("user_id", Integer, ForeignKey("users.id"), nullable=False)
    investment_type_id = Column("investment_type_id", Integer, ForeignKey("investment_types.id"), nullable=False)
    amount = Column("amount", Numeric(10, 2), nullable=False)
    date = Column("date", Date, nullable=False)
    description = Column("description", Text, nullable=True)
    created_at = Column("created_at", DateTime, server_default=func.now(), nullable=False)

    # Relationships
    user = relationship("User", back_populates="investments")
    investment_type = relationship("InvestmentType", back_populates="investments")


class InvestmentType(Base):
    """Types of investments"""
    __tablename__ = "investment_types"
    __table_args__ = (PrimaryKeyConstraint("id", name="PK_investment_types_id"),)

    id = Column("id", Integer, Identity(start=1), nullable=False, unique=True)
    name = Column("name", String(100), nullable=False, unique=True)
    description = Column("description", Text, nullable=True)
    is_active = Column("is_active", Boolean, default=True, nullable=False)
    created_at = Column("created_at", DateTime, server_default=func.now(), nullable=False)

    # Relationships
    investments = relationship("Investment", back_populates="investment_type")


class SinkingFund(Base):
    """Sinking funds for future expenses"""
    __tablename__ = "sinking_funds"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="PK_sinking_funds_id"),
        Index("IX_sinking_funds_user_id", "user_id"),
        Index("IX_sinking_funds_type_id", "sinking_fund_type_id"),
    )

    id = Column("id", Integer, Identity(start=1), nullable=False, unique=True)
    user_id = Column("user_id", Integer, ForeignKey("users.id"), nullable=False)
    sinking_fund_type_id = Column("sinking_fund_type_id", Integer, ForeignKey("sinking_fund_types.id"), nullable=False)
    amount = Column("amount", Numeric(10, 2), nullable=False)
    date = Column("date", Date, nullable=False)
    description = Column("description", Text, nullable=True)
    created_at = Column("created_at", DateTime, server_default=func.now(), nullable=False)

    # Relationships
    user = relationship("User", back_populates="sinking_funds")
    sinking_fund_type = relationship("SinkingFundType", back_populates="sinking_funds")


class SinkingFundType(Base):
    """Types of sinking funds"""
    __tablename__ = "sinking_fund_types"
    __table_args__ = (PrimaryKeyConstraint("id", name="PK_sinking_fund_types_id"),)

    id = Column("id", Integer, Identity(start=1), nullable=False, unique=True)
    name = Column("name", String(100), nullable=False, unique=True)
    target_amount = Column("target_amount", Numeric(10, 2), nullable=True)
    description = Column("description", Text, nullable=True)
    is_active = Column("is_active", Boolean, default=True, nullable=False)
    created_at = Column("created_at", DateTime, server_default=func.now(), nullable=False)

    # Relationships
    sinking_funds = relationship("SinkingFund", back_populates="sinking_fund_type")


class NetWorth(Base):
    """Net worth tracking over time"""
    __tablename__ = "net_worth"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="PK_net_worth_id"),
        Index("IX_net_worth_user_id", "user_id"),
        Index("IX_net_worth_date", "date"),
    )

    id = Column("id", Integer, Identity(start=1), nullable=False, unique=True)
    user_id = Column("user_id", Integer, ForeignKey("users.id"), nullable=False)
    date = Column("date", Date, nullable=False)
    total_assets = Column("total_assets", Numeric(12, 2), nullable=False)
    total_liabilities = Column("total_liabilities", Numeric(12, 2), nullable=False)
    net_worth = Column("net_worth", Numeric(12, 2), nullable=False)
    notes = Column("notes", Text, nullable=True)
    created_at = Column("created_at", DateTime, server_default=func.now(), nullable=False)

    # Relationships
    user = relationship("User", back_populates="net_worth_entries")


class Subscription(Base):
    """Recurring subscriptions"""
    __tablename__ = "subscriptions"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="PK_subscriptions_id"),
        Index("IX_subscriptions_user_id", "user_id"),
        Index("IX_subscriptions_active", "is_active"),
    )

    id = Column("id", Integer, Identity(start=1), nullable=False, unique=True)
    user_id = Column("user_id", Integer, ForeignKey("users.id"), nullable=False)
    name = Column("name", String(100), nullable=False)
    amount = Column("amount", Numeric(10, 2), nullable=False)
    frequency = Column("frequency", String(20), nullable=False)  # monthly, yearly, etc.
    start_date = Column("start_date", Date, nullable=False)
    end_date = Column("end_date", Date, nullable=True)
    is_active = Column("is_active", Boolean, default=True, nullable=False)
    description = Column("description", Text, nullable=True)
    created_at = Column("created_at", DateTime, server_default=func.now(), nullable=False)
    updated_at = Column("updated_at", DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

    # Relationships
    user = relationship("User", back_populates="subscriptions")


# Add subscriptions relationship to User
User.subscriptions = relationship("Subscription", back_populates="user")
