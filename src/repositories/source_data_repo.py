from sqlalchemy.orm import Session
import datetime as dt
from src.constants import Category, Purchase, Report
from src.database.database import CategoryTable, PurchaseTable, ReportTable


class SourceDataRepository:

    def __init__(self, session: Session):
        self._session = session

    def map_domain_to_entity_category(self, category: Category):
        return CategoryTable(Category=category.category)

    def map_entity_to_domain_category(self, entity: CategoryTable):
        return Category(category=entity.Category)

    def map_domain_to_entity_purchase(self, purchase: Purchase) -> PurchaseTable:
        return PurchaseTable(
            Date=purchase.date, Price=purchase.price, FKCategory=purchase.category
        )

    def map_entity_to_domain_purchase(self, entity: PurchaseTable) -> Purchase:
        return Purchase(
            date=entity.Date, price=entity.Price, category=entity.FKCategory
        )

    def map_entity_to_domain_report(self, entity: ReportTable) -> Report:
        return Report(date=entity.Date, total=entity.Total, category=entity.FKCategory)

    def map_domain_to_entity_report(self, report: Report) -> PurchaseTable:
        return ReportTable(
            Date=report.date, Total=report.total, FKCategory=report.category
        )

    def get_category_by_name(self, category_name: str) -> Category:
        record = (
            self._session.query(CategoryTable)
            .where(CategoryTable.Category == category_name)
            .first()
        )
        if record:
            return self.map_entity_to_domain_category(entity=record)

    def get_report_by_name_date(self, date: dt.datetime, category: str) -> Report:
        record = (
            self._session.query(ReportTable)
            .where(ReportTable.Date == date, ReportTable.FKCategory == category)
            .first()
        )
        if record:
            return self.map_entity_to_domain_report(entity=record)

    def insert_category(self, category: Category):
        entity = self.map_domain_to_entity_category(category=category)
        self._session.add(entity)

    def insert_purchase(self, purchase: Purchase) -> None:
        entity = self.map_domain_to_entity_purchase(purchase=purchase)
        self._session.add(entity)

    def insert_report(self, report: Report) -> None:
        entity = self.map_domain_to_entity_report(report=report)
        self._session.add(entity)
