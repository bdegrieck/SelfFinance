from sqlalchemy import Column, DateTime, Float, Unicode, Identity, PrimaryKeyConstraint, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Purchase(Base):
    __tablename__ = "Purchase"
    __tableargs__ = (PrimaryKeyConstraint("ID", name="PK_Purchase_ID"))

    ID = Column("ID", Identity(start=1), nullable=False)
    date = Column("Date", DateTime, nullable=False)
    Price = Column("Price", Float, nullable=False)
    PurchaseType = Column("PurchaseType", Unicode, nullable=False)


class