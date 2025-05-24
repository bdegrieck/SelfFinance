import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import src.database.entrypoint as entrypoint
from src.database.entrypoint import Base
from src.managers.uow.sourcedata_uow import SourceDataUnitOfWork
from src.managers.source_manager.service import SourceDataService
from src.constants import Category
from src.database.database import CategoryTable


@pytest.fixture
def engine(monkeypatch):
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)

    def get_test_engine():
        return engine

    monkeypatch.setattr(entrypoint, "get_engine", get_test_engine)
    return engine


def test_insert_category(engine):
    Session = sessionmaker()
    service = SourceDataService(SourceDataUnitOfWork(Session))
    service.insert_category(Category(name="Food"))

    with Session(bind=engine) as session:
        result = session.query(CategoryTable).all()
        assert len(result) == 1
        assert result[0].Name == "Food"
