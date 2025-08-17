import datetime as dt

from src.managers.source_manager.domain import (
    GroceriesExpense,
    User,
)
from src.managers.uow.sourcedata_uow import SourceDataUnitOfWork


class SelfFinanceService:

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

    def insert_new_user(self, user_info: User) -> None:
        """
        Inserts a new user record into the database.

        Args:
            user_info (User): User information to persist.
        """
        with self._source_data_uow as uow:
            uow.source_data_repo.insert_new_user(user_info=user_info)
            uow.commit()

    def get_login_by_username(self, username: str) -> User | None:
        """
        Retrieve a user by username if present.

        Args:
            username (str): Username to search for.

        Returns:
            user (User | None): Retrieved user record or None if not found.
        """
        with self._source_data_uow as uow:
            user = uow.source_data_repo.get_login_by_username(username=username)
        return user

    def get_monthly_expenses(self, date: dt.datetime, user_id: int):
        """
        Retrieve monthly expenses for the specified date from the repository.

        Args:
            date (datetime): Date of the monthly expenses.
            user_id (int): User ID to filter expenses by.

        Returns:
            monthly_expenses: Retrieved monthly expenses record.
        """
        with self._source_data_uow as uow:
            monthly_expenses = uow.source_data_repo.get_monthly_expenses(
                date=date, user_id=user_id
            )
        return monthly_expenses
