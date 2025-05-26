from sqlalchemy.orm import sessionmaker

from src.database.entrypoint import get_engine
from src.managers.source_manager.service import SourceDataService
from src.managers.uow.sourcedata_uow import SourceDataUnitOfWork


def create_sourcedata_service():
    service = SourceDataService(
        source_data_uow=SourceDataUnitOfWork(
            sessionfactory=sessionmaker(bind=get_engine())
        )
    )
    return service
