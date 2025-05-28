from src.constants import Category, Purchase, Report
from src.managers.uow.sourcedata_uow import SourceDataUnitOfWork
import datetime as dt

class SourceDataService:

    def __init__(self, source_data_uow: SourceDataUnitOfWork):
        self._source_data_uow = source_data_uow

    def get_category_by_name(self, category: str) -> Category:
        with self._source_data_uow as uow:
            category = uow.source_data_repo.get_category_by_name(category_name=category)
        return category

    def get_report_by_name_date(self, category: str, date: dt.datetime) -> Report:
        """Return a :class:`Report` for the given category and date if one
        exists."""
        with self._source_data_uow as uow:
            report = uow.source_data_repo.get_report_by_name_date(
                date=date,
                category=category,
            )
        return report

    def insert_category(self, category: Category) -> None:
        with self._source_data_uow as uow:
            uow.source_data_repo.insert_category(category=category)
            uow.commit()

    def insert_purchase(self, purchase: Purchase) -> None:
        with self._source_data_uow as uow:
            uow.source_data_repo.insert_purchase(purchase=purchase)
            uow.commit()

    def insert_report(self, report: Report) -> None:
        with self._source_data_uow as uow:
            uow.source_data_repo.insert_report(report=report)
            uow.commit()
