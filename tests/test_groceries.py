import datetime as dt

from src.managers.source_manager.domain import Groceries
from src.managers.source_manager.entrypoint import create_sourcedata_service


class TestSourceData:

    def test_insert_groceries(self, clean_db):
        sourcedata_service = create_sourcedata_service()
        groceries = Groceries(
            date=dt.datetime(month=9, day=18, year=2001),
            amount=100,
            description="Publix groceries",
        )
        date = dt.datetime(month=9, day=18, year=2001)
        sourcedata_service.insert_groceries(groceries=groceries)
        groceries = sourcedata_service.get_groceries_by_date(date=date)
        assert groceries.date == date
