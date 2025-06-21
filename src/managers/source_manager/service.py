import datetime as dt

from src.managers.source_manager.domain import GroceriesExpense
from src.managers.uow.sourcedata_uow import SourceDataUnitOfWork


class SourceDataService:

    def __init__(self, source_data_uow: SourceDataUnitOfWork):
        self._source_data_uow = source_data_uow

    def insert_groceries(self, groceries: GroceriesExpense):
        with self._source_data_uow as uow:
            uow.source_data_repo.insert_groceries(groceries=groceries)
            uow.commit()

    def get_groceries_by_date(self, date: dt.datetime) -> GroceriesExpense:
        with self._source_data_uow as uow:
            groceries = uow.source_data_repo.get_groceries_by_date(date=date)
        return groceries
