import datetime as dt

from src.managers.source_manager.domain import GroceriesExpense
from src.managers.source_manager.entrypoint import create_sourcedata_service
from tests.service import create_test_sourcedata_service


class TestSourceData:

    def test_insert_groceries(self):
        sourcedata_service = create_test_sourcedata_service()
        groceries = GroceriesExpense(
            date=dt.datetime(month=9, day=18, year=2001),
            amount=100,
            description="Publix groceries",
        )
        date = dt.datetime(month=9, day=18, year=2001)
        sourcedata_service.insert_groceries(groceries=groceries)
        groceries = sourcedata_service.get_groceries_by_date(date=date)
        assert groceries.date == date
