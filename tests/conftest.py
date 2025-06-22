import pytest

from src.database.entrypoint import create_test_database, Base


@pytest.fixture(autouse=True)
def create_test_db():
    engine = create_test_database()
    yield engine
