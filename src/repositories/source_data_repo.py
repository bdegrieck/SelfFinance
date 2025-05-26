from sqlalchemy.orm import Session

from src.constants import Category
from src.database.database import CategoryTable


class SourceDataRepository:

    def __init__(self, session: Session):
        self._session = session

    def map_domain_to_entity_category(self, category: Category):
        return CategoryTable(Category=category.category)

    def map_entity_to_domain_category(self, entity: CategoryTable):
        return Category(category=entity.Category)

    def get_category_by_name(self, category_name: str) -> Category:
        record = self._session.query(CategoryTable).where(
            CategoryTable.Category == category_name
        ).first()
        if record:
            return self.map_entity_to_domain_category(entity=record)

    def insert_category(self, category: Category):
        entity = self.map_domain_to_entity_category(category=category)
        self._session.add(entity)
