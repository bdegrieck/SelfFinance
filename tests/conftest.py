import pytest

from src.database.entrypoint import create_test_database, Base


@pytest.fixture(autouse=True)
def create_test_db():
    """
    Create and yield a fresh test database for each test.

    Returns:
        engine (Engine): SQLAlchemy engine bound to the test database.
    """
    engine = create_test_database()
    yield engine
