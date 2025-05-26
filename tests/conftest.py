import pytest

from src.database.entrypoint import create_test_db, Base


@pytest.fixture(autouse=True)
def clean_db():
    engine = create_test_db()
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
