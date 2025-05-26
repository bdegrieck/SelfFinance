import pytest

from src.database.entrypoint import get_engine, Base


@pytest.fixture(autouse=True)
def clean_db():
    engine = get_engine()
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
