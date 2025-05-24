from src.constants import Category
from src.managers.uow.sourcedata_uow import SourceDataUnitOfWork


class SourceDataService:

    def __init__(self, source_data_uow: SourceDataUnitOfWork):
        self._source_data_uow = source_data_uow

    def insert_category(self, category: Category):
        with self._source_data_uow as uow:
            uow.source_data_repo.insert_category(category=category)
            uow.commit()
