from typing import Self

from sqlalchemy.orm import sessionmaker

from src.repositories.source_data_repo import SourceDataRepository


class SourceDataUnitOfWork:

    def __init__(self, sessionfactory: sessionmaker):
        self._sessionfactory = sessionfactory

    def __enter__(self) -> Self:
        # Use the session factory provided at construction time. This
        # allows the caller to control which engine and database schema
        # the unit of work operates on (e.g. the test database).
        self._session = self._sessionfactory()
        self.source_data_repo = SourceDataRepository(session=self._session)
        return self

    def __exit__(self, *args):
        self._session.close()

    def commit(self):
        self._session.commit()

    def rollback(self):
        self._session.rollback()
