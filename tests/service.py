from sqlalchemy.orm import sessionmaker

from src.database.entrypoint import create_test_database
from src.managers.source_manager.service import SourceDataService
from src.managers.uow.sourcedata_uow import SourceDataUnitOfWork


def create_test_sourcedata_service():
    service = SourceDataService(
        source_data_uow=SourceDataUnitOfWork(
            sessionfactory=sessionmaker(bind=create_test_database())
        )
    )
    return service
