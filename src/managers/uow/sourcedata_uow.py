from typing import Self

from sqlalchemy.orm import sessionmaker

from src.database.entrypoint import create_db
from src.repositories.source_data_repo import SourceDataRepository


class SourceDataUnitOfWork:

    def __init__(self, sessionfactory: sessionmaker):
        """
        Store the session factory used for creating database sessions.

        Args:
            sessionfactory (sessionmaker): Factory used to produce new sessions.
        """
        self._sessionfactory = sessionfactory

    def __enter__(self) -> Self:
        """
        Open a new database session and expose the repository.

        Returns:
            uow (SourceDataUnitOfWork): The active unit of work instance.
        """
        self._session = self._sessionfactory()
        self.source_data_repo = SourceDataRepository(session=self._session)
        return self

    def __exit__(self, *args):
        """
        Close the current database session.
        """
        self._session.close()

    def commit(self):
        """
        Commit the current transaction.
        """
        self._session.commit()

    def rollback(self):
        """
        Roll back the current transaction.
        """
        self._session.rollback()
