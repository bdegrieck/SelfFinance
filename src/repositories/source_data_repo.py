import datetime as dt

from sqlalchemy.orm import Session

from src.database.database import (
    GroceriesTable,
)
from src.managers.source_manager.domain import (
    ApartmentExpense,
    CarExpense,
    ClothingExpense,
    EatingOutExpense,
    GiftExpense,
    GroceriesExpense,
    Income,
    Investment,
    InvestmentType,
    MiscExpense,
    NetWorth,
    SinkingFund,
    SinkingFundType,
    SubscriptionExpense,
    Venmo,
)
from src.managers.source_manager.mappers import (
    map_domain_to_entity_apartment_spending,
    map_domain_to_entity_car_expense,
    map_domain_to_entity_clothing_expense,
    map_domain_to_entity_eating_out_expense,
    map_domain_to_entity_gift_expense,
    map_domain_to_entity_groceries,
    map_domain_to_entity_income,
    map_domain_to_entity_investment,
    map_domain_to_entity_investment_type,
    map_domain_to_entity_misc_expense,
    map_domain_to_entity_net_worth,
    map_domain_to_entity_sinking_fund,
    map_domain_to_entity_sinking_fund_type,
    map_domain_to_entity_subscription_expense,
    map_domain_to_entity_venmo,
    map_entity_to_domain_groceries,
)


class SourceDataRepository:

    def __init__(self, session: Session):
        self._session = session

    def insert_groceries(self, groceries: GroceriesExpense) -> None:
        groceries_record = map_domain_to_entity_groceries(expense=groceries)
        self._session.add(groceries_record)

    def insert_apartment_expense(self, expense: ApartmentExpense) -> None:
        record = map_domain_to_entity_apartment_spending(expense)
        self._session.add(record)

    def insert_car_expense(self, expense: CarExpense) -> None:
        record = map_domain_to_entity_car_expense(expense)
        self._session.add(record)

    def insert_clothing_expense(self, expense: ClothingExpense) -> None:
        record = map_domain_to_entity_clothing_expense(expense)
        self._session.add(record)

    def insert_eating_out_expense(self, expense: EatingOutExpense) -> None:
        record = map_domain_to_entity_eating_out_expense(expense)
        self._session.add(record)

    def insert_gift_expense(self, expense: GiftExpense) -> None:
        record = map_domain_to_entity_gift_expense(expense)
        self._session.add(record)

    def insert_income(self, income: Income) -> None:
        record = map_domain_to_entity_income(income)
        self._session.add(record)

    def insert_investment(self, investment: Investment) -> None:
        record = map_domain_to_entity_investment(investment)
        self._session.add(record)

    def insert_investment_type(self, investment_type: InvestmentType) -> None:
        record = map_domain_to_entity_investment_type(investment_type)
        self._session.add(record)

    def insert_misc_expense(self, expense: MiscExpense) -> None:
        record = map_domain_to_entity_misc_expense(expense)
        self._session.add(record)

    def insert_net_worth(self, net_worth: NetWorth) -> None:
        record = map_domain_to_entity_net_worth(net_worth)
        self._session.add(record)

    def insert_sinking_fund(self, fund: SinkingFund) -> None:
        record = map_domain_to_entity_sinking_fund(fund)
        self._session.add(record)

    def insert_sinking_fund_type(self, fund_type: SinkingFundType) -> None:
        record = map_domain_to_entity_sinking_fund_type(fund_type)
        self._session.add(record)

    def insert_subscription_expense(self, expense: SubscriptionExpense) -> None:
        record = map_domain_to_entity_subscription_expense(expense)
        self._session.add(record)

    def insert_venmo(self, venmo: Venmo) -> None:
        record = map_domain_to_entity_venmo(venmo)
        self._session.add(record)

    def get_groceries_by_date(self, date: dt.datetime) -> GroceriesExpense | None:
        record = (
            self._session.query(GroceriesTable)
            .where(GroceriesTable.Date == date)
            .first()
        )
        if record:
            groceries = map_entity_to_domain_groceries(record=record)
            return groceries
