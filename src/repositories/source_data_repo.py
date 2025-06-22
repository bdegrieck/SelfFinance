import datetime as dt

from sqlalchemy.orm import Session

from src.database.database import GroceriesTable
from src.managers.source_manager.domain import GroceriesExpense
from src.managers.source_manager.mappers import (
    map_domain_to_entity_groceries,
    map_entity_to_domain_groceries,
)


class SourceDataRepository:

    def __init__(self, session: Session):
        self._session = session

    def insert_groceries(self, groceries: GroceriesExpense) -> None:
        groceries_record = map_domain_to_entity_groceries(groceries=groceries)
        self._session.add(groceries_record)

    def get_groceries_by_date(self, date: dt.datetime) -> GroceriesExpense | None:
        record = (
            self._session.query(GroceriesTable)
            .where(GroceriesTable.Date == date)
            .first()
        )
        if record:
            groceries = map_entity_to_domain_groceries(groceries_record=record)
            return groceries
