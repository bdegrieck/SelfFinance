import pytest
import datetime as dt
from src.constants import Category, Report
from src.database.entrypoint import create_test_db
from src.managers.source_manager.entrypoint import create_sourcedata_service


class SourceDataTest:

    def test_insert_category(clean_db):
        sourcedata_service = create_sourcedata_service()
        sourcedata_service.insert_category(category=Category(category="Groceries"))
        category = sourcedata_service.get_category_by_name(category="Groceries")
        assert category.category == "Groceries"

    def test_insert_report(clean_db):
        sourcedata_service = create_sourcedata_service()
        sourcedata_service.insert_report(
            report=Report(
                date=dt.datetime(day=18, month=9, year=2001),
                total=100,
                category="Groceries"
            )
        )
        report =
