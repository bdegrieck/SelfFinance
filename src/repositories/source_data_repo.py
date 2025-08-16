import datetime as dt

from sqlalchemy.orm import Session

from src.database.database import (
    User as UserTable,
    Expense,
)
from src.managers.source_manager.domain import (
    User,
    GroceriesExpense,
)
from src.managers.source_manager.mappers import (
    map_domain_to_entity_groceries,
    map_entity_to_domain_groceries,
    map_domain_to_entity_user,
    map_entity_to_domain_user,
)


class SourceDataRepository:

    def __init__(self, session: Session):
        """
        Store the SQLAlchemy session used for all repository operations.

        Args:
            session (Session): Active database session.
        """
        self._session = session

    def insert_groceries(self, groceries: GroceriesExpense) -> None:
        """
        Add a groceries record to the database.

        Args:
            groceries (GroceriesExpense): Expense to persist.
        """
        groceries_record = map_domain_to_entity_groceries(expense=groceries)
        self._session.add(groceries_record)

    def get_groceries_by_date(self, date: dt.datetime) -> GroceriesExpense | None:
        """
        Fetch groceries for a specific date.

        Args:
            date (datetime): Date to query.

        Returns:
            groceries (GroceriesExpense | None): Retrieved groceries expense if present.
        """
        # TODO: Implement when category system is set up for groceries
        # record = (
        #     self._session.query(Expense)
        #     .join(Category)
        #     .where(Expense.date == date, Category.name == "Groceries")
        #     .first()
        # )
        # if record:
        #     groceries = map_entity_to_domain_groceries(record=record)
        #     return groceries
        pass

    def get_monthly_expenses(self, date: dt.datetime):
        """
        Fetch monthly expenses for a specific date.

        Args:
            date (datetime): Date to query.

        Returns:
            monthly_expenses: Retrieved monthly expenses if present.
        """
        # TODO: Implement monthly expenses query when MonthlyExpensesTable is available
        pass

    def insert_new_user(self, user_info: User) -> None:
        """Insert a login record into the database."""
        record = map_domain_to_entity_user(user_info)
        self._session.add(record)

    def get_login_by_username(self, username: str) -> User | None:
        """Retrieve a login by username if present."""

        record = (
            self._session.query(UserTable).where(UserTable.username == username).first()
        )
        if record:
            return map_entity_to_domain_user(record=record)
        return None
