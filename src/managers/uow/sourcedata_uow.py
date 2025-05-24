from typing import Self

from sqlalchemy.orm import sessionmaker

from src.database.entrypoint import get_engine
from src.repositories.source_data_repo import SourceDataRepository


class SourceDataUnitOfWork:

    def __init__(self, sessionfactory: sessionmaker):
        self._sessionfactory = sessionfactory

    def __enter__(self) -> Self:
        self._session = self._sessionfactory(bind=get_engine())
        self.source_data_repo = SourceDataRepository(session=self._session)
        return self

    def __exit__(self):
        self._session.close()

    def commit(self):
        self._session.commit()

    def rollback(self):
        self._session.rollback()
