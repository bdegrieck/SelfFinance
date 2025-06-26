from sqlalchemy.orm import sessionmaker

from src.database.entrypoint import create_db
from src.managers.source_manager.service import SourceDataService
from src.managers.uow.sourcedata_uow import SourceDataUnitOfWork


def create_sourcedata_service():
    """
    Construct a ``SourceDataService`` wired with its unit of work and database engine.

    Returns:
        service (SourceDataService): Configured service instance ready for use.
    """
    service = SourceDataService(
        source_data_uow=SourceDataUnitOfWork(
            sessionfactory=sessionmaker(bind=create_db())
        )
    )
    return service
