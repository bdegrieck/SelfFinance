from sqlalchemy import Column, DateTime, Float, Unicode, Identity, PrimaryKeyConstraint
from sqlalchemy.orm import declarative_base

from .entrypoint import get_engine

Base = declarative_base()


class Purchase(Base):
    __tablename__ = "Purchase"
    __table_args__ = (PrimaryKeyConstraint("ID", name="PK_Purchase_ID"),)

    ID = Column("ID", Identity(start=1), nullable=False)
    date = Column("Date", DateTime, nullable=False)
    Price = Column("Price", Float, nullable=False)
    PurchaseType = Column("PurchaseType", Unicode, nullable=False)


# Engine that can be imported by other modules
engine = get_engine()
