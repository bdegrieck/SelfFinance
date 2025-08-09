from sqlalchemy.orm import sessionmaker

from src.database.entrypoint import create_db
from src.managers.uow.sourcedata_uow import SourceDataUnitOfWork
from src.managers.source_manager.service import SelfFinanceService


def create_selfFinance_service() -> SelfFinanceService:
    """
    Construct a ``SelfFinanceService`` wired with its unit of work and database engine.

    Returns:
        service (SelfFinanceService): Configured service instance ready for use.
    """
    service = SelfFinanceService(
        source_data_uow=SourceDataUnitOfWork(
            sessionfactory=sessionmaker(bind=create_db())
        )
    )
    return service
