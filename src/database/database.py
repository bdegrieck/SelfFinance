from sqlalchemy import (
    Column,
    DateTime,
    Float,
    Unicode,
    Identity,
    PrimaryKeyConstraint,
    Index,
    Integer,
)

from src.database.entrypoint import Base


class PurchaseTable(Base):
    __tablename__ = "Purchase"
    __table_args__ = (
        PrimaryKeyConstraint("ID", name="PK_Purchase_ID"),
        Index(
            "IX_Purchase_FKCategory",
            "FKCategory",
            mssql_clustered=False,
            unique=True,
        ),
        Index("IX_Purchase_Date", "Date", mssql_clustered=False),
    )

    ID = Column("ID", Integer, Identity(start=1), nullable=False)
    Date = Column("Date", DateTime, nullable=False)
    Price = Column("Price", Float, nullable=False)
    FKCategory = Column("FKCategory", Unicode(20), nullable=False)


class CategoryTable(Base):
    __tablename__ = "Category"
    __table_args__ = (
        PrimaryKeyConstraint("ID", name="PK_Category_ID"),
        Index("IX_Category_Category", "Category", mssql_clustered=False, unique=True),
    )

    ID = Column("ID", Integer, Identity(start=1), nullable=False)
    Category = Column("Category", Unicode(20), nullable=False)


class ReportTable(Base):
    __tablename__ = "Report"
    __table_args__ = (
        PrimaryKeyConstraint("ID", name="PK_Report_ID"),
        Index(
            "IX_Report_Date",
            "FKCategory",
            "Date",
            mssql_clustered=False,
            unique=True,
        ),
    )

    ID = Column("ID", Integer, Identity(start=1), nullable=False)
    Date = Column("Date", DateTime, nullable=False, unique=True)
    Total = Column("Total", Float, nullable=False)
    FKCategory = Column("FKCategory", Unicode(20), nullable=False)
