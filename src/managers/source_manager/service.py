import datetime as dt

from src.managers.source_manager.domain import GroceriesExpense
from src.managers.uow.sourcedata_uow import SourceDataUnitOfWork


class SourceDataService:

    def __init__(self, source_data_uow: SourceDataUnitOfWork):
        """
        Initialize the service with the provided unit of work.

        Args:
            source_data_uow (SourceDataUnitOfWork): Unit of work for database access.
        """
        self._source_data_uow = source_data_uow

    def insert_groceries(self, groceries: GroceriesExpense):
        """
        Insert a ``GroceriesExpense`` record into the database.

        Args:
            groceries (GroceriesExpense): Grocery expense to persist.
        """
        with self._source_data_uow as uow:
            uow.source_data_repo.insert_groceries(groceries=groceries)
            uow.commit()

    def get_groceries_by_date(self, date: dt.datetime) -> GroceriesExpense:
        """
        Retrieve groceries for the specified date from the repository.

        Args:
            date (datetime): Date of the grocery purchase.

        Returns:
            groceries (GroceriesExpense): Retrieved groceries record.
        """
        with self._source_data_uow as uow:
            groceries = uow.source_data_repo.get_groceries_by_date(date=date)
        return groceries
