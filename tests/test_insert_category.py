import pytest

from src.constants import Category
from src.database.entrypoint import get_engine
from src.managers.source_manager.entrypoint import create_sourcedata_service


@pytest.fixture(scope="function")
def start_engine():
    get_engine()


def test_insert_category():
    sourcedata_service = create_sourcedata_service()
    sourcedata_service.insert_category(category=Category(category="Groceries"))
    category = sourcedata_service.get_category_by_name(category="Groceries")
    assert category.category == "Groceries"
