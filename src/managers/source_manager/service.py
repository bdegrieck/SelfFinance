import datetime as dt

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
from src.managers.uow.sourcedata_uow import SourceDataUnitOfWork


class SourceDataService:

    def __init__(self, source_data_uow: SourceDataUnitOfWork):
        """
        Initialize the service with the provided unit of work.

        Args:
            source_data_uow (SourceDataUnitOfWork): Unit of work for database access.
        """
        self._source_data_uow = source_data_uow

    def insert_groceries(self, groceries: GroceriesExpense):
        """
        Insert a ``GroceriesExpense`` record into the database.

        Args:
            groceries (GroceriesExpense): Grocery expense to persist.
        """
        with self._source_data_uow as uow:
            uow.source_data_repo.insert_groceries(groceries=groceries)
            uow.commit()

    def insert_apartment_expense(self, expense: ApartmentExpense):
        with self._source_data_uow as uow:
            uow.source_data_repo.insert_apartment_expense(expense=expense)
            uow.commit()

    def insert_car_expense(self, expense: CarExpense):
        with self._source_data_uow as uow:
            uow.source_data_repo.insert_car_expense(expense=expense)
            uow.commit()

    def insert_clothing_expense(self, expense: ClothingExpense):
        with self._source_data_uow as uow:
            uow.source_data_repo.insert_clothing_expense(expense=expense)
            uow.commit()

    def insert_eating_out_expense(self, expense: EatingOutExpense):
        with self._source_data_uow as uow:
            uow.source_data_repo.insert_eating_out_expense(expense=expense)
            uow.commit()

    def insert_gift_expense(self, expense: GiftExpense):
        with self._source_data_uow as uow:
            uow.source_data_repo.insert_gift_expense(expense=expense)
            uow.commit()

    def insert_income(self, income: Income):
        with self._source_data_uow as uow:
            uow.source_data_repo.insert_income(income=income)
            uow.commit()

    def insert_investment(self, investment: Investment):
        with self._source_data_uow as uow:
            uow.source_data_repo.insert_investment(investment=investment)
            uow.commit()

    def insert_investment_type(self, investment_type: InvestmentType):
        with self._source_data_uow as uow:
            uow.source_data_repo.insert_investment_type(
                investment_type=investment_type
            )
            uow.commit()

    def insert_misc_expense(self, expense: MiscExpense):
        with self._source_data_uow as uow:
            uow.source_data_repo.insert_misc_expense(expense=expense)
            uow.commit()

    def insert_net_worth(self, net_worth: NetWorth):
        with self._source_data_uow as uow:
            uow.source_data_repo.insert_net_worth(net_worth=net_worth)
            uow.commit()

    def insert_sinking_fund(self, fund: SinkingFund):
        with self._source_data_uow as uow:
            uow.source_data_repo.insert_sinking_fund(fund=fund)
            uow.commit()

    def insert_sinking_fund_type(self, fund_type: SinkingFundType):
        with self._source_data_uow as uow:
            uow.source_data_repo.insert_sinking_fund_type(fund_type=fund_type)
            uow.commit()

    def insert_subscription_expense(self, expense: SubscriptionExpense):
        with self._source_data_uow as uow:
            uow.source_data_repo.insert_subscription_expense(expense=expense)
            uow.commit()

    def insert_venmo(self, venmo: Venmo):
        with self._source_data_uow as uow:
            uow.source_data_repo.insert_venmo(venmo=venmo)
            uow.commit()

    def get_groceries_by_date(self, date: dt.datetime) -> GroceriesExpense:
        """
        Retrieve groceries for the specified date from the repository.

        Args:
            date (datetime): Date of the grocery purchase.

        Returns:
            groceries (GroceriesExpense): Retrieved groceries record.
        """
        with self._source_data_uow as uow:
            groceries = uow.source_data_repo.get_groceries_by_date(date=date)
        return groceries
