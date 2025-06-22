import pytest

from src.database.entrypoint import Base, create_db


@pytest.fixture(autouse=True)
def clean_db():
    engine = create_db()
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield
