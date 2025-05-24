from sqlalchemy import (
    Column,
    DateTime,
    Float,
    Unicode,
    Identity,
    PrimaryKeyConstraint,
    create_engine,
    Index,
)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Purchase(Base):
    __tablename__ = "Purchase"
    __table_args__ = (
        PrimaryKeyConstraint("ID", name="PK_Purchase_ID"),
        Index("Category", name="IX_Purchase_Category", mssql_clustered=False),
        Index("Date", name="IX_Purchase_Date", mssql_clustered=False),
    )

    ID = Column("ID", Identity(start=1), nullable=False)
    Date = Column("Date", DateTime, nullable=False)
    Price = Column("Price", Float, nullable=False)
    Category = Column("Category", Unicode(20), nullable=False)


class Category(Base):
    __tablename__ = "Category"
    __table_args__ = (
        PrimaryKeyConstraint("ID", name="PK_Category_ID"),
        Index("Name", name="IX_Category_Name", mssql_clustered=False),
    )

    ID = Column("ID", Identity(start=1), nullable=False)
    Name = Column("Name", Unicode(20), nullable=False)
