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
    Login,
    MiscExpense,
    NetWorth,
    SinkingFund,
    SinkingFundType,
    SubscriptionExpense,
    User,
    Venmo,
)
from src.managers.uow.sourcedata_uow import SourceDataUnitOfWork

class SelfFinanceService:

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
        """
        Insert an ``ApartmentExpense`` record into the database.

        Args:
            expense (ApartmentExpense): Apartment expense to persist.
        """
        with self._source_data_uow as uow:
            uow.source_data_repo.insert_apartment_expense(expense=expense)
            uow.commit()

    def insert_car_expense(self, expense: CarExpense):
        """
        Insert a ``CarExpense`` record into the database.

        Args:
            expense (CarExpense): Car expense to persist.
        """
        with self._source_data_uow as uow:
            uow.source_data_repo.insert_car_expense(expense=expense)
            uow.commit()

    def insert_clothing_expense(self, expense: ClothingExpense):
        """
        Insert a ``ClothingExpense`` record into the database.

        Args:
            expense (ClothingExpense): Clothing expense to persist.
        """
        with self._source_data_uow as uow:
            uow.source_data_repo.insert_clothing_expense(expense=expense)
            uow.commit()

    def insert_eating_out_expense(self, expense: EatingOutExpense):
        """
        Insert an ``EatingOutExpense`` record into the database.

        Args:
            expense (EatingOutExpense): Eating out expense to persist.
        """
        with self._source_data_uow as uow:
            uow.source_data_repo.insert_eating_out_expense(expense=expense)
            uow.commit()

    def insert_gift_expense(self, expense: GiftExpense):
        """
        Insert a ``GiftExpense`` record into the database.

        Args:
            expense (GiftExpense): Gift expense to persist.
        """
        with self._source_data_uow as uow:
            uow.source_data_repo.insert_gift_expense(expense=expense)
            uow.commit()

    def insert_income(self, income: Income):
        """
        Insert an ``Income`` record into the database.

        Args:
            income (Income): Income record to persist.
        """
        with self._source_data_uow as uow:
            uow.source_data_repo.insert_income(income=income)
            uow.commit()

    def insert_investment(self, investment: Investment):
        """
        Insert an ``Investment`` record into the database.

        Args:
            investment (Investment): Investment record to persist.
        """
        with self._source_data_uow as uow:
            uow.source_data_repo.insert_investment(investment=investment)
            uow.commit()

    def insert_investment_type(self, investment_type: InvestmentType):
        """
        Insert an ``InvestmentType`` record into the database.

        Args:
            investment_type (InvestmentType): Investment type record to persist.
        """
        with self._source_data_uow as uow:
            uow.source_data_repo.insert_investment_type(investment_type=investment_type)
            uow.commit()

    def insert_misc_expense(self, expense: MiscExpense):
        """
        Insert a ``MiscExpense`` record into the database.

        Args:
            expense (MiscExpense): Miscellaneous expense to persist.
        """
        with self._source_data_uow as uow:
            uow.source_data_repo.insert_misc_expense(expense=expense)
            uow.commit()

    def insert_net_worth(self, net_worth: NetWorth):
        """
        Insert a ``NetWorth`` record into the database.

        Args:
            net_worth (NetWorth): Net worth record to persist.
        """
        with self._source_data_uow as uow:
            uow.source_data_repo.insert_net_worth(net_worth=net_worth)
            uow.commit()

    def insert_sinking_fund(self, fund: SinkingFund):
        """
        Insert a ``SinkingFund`` record into the database.

        Args:
            fund (SinkingFund): Sinking fund record to persist.
        """
        with self._source_data_uow as uow:
            uow.source_data_repo.insert_sinking_fund(fund=fund)
            uow.commit()

    def insert_sinking_fund_type(self, fund_type: SinkingFundType):
        """
        Insert a ``SinkingFundType`` record into the database.

        Args:
            fund_type (SinkingFundType): Sinking fund type record to persist.
        """
        with self._source_data_uow as uow:
            uow.source_data_repo.insert_sinking_fund_type(fund_type=fund_type)
            uow.commit()

    def insert_subscription_expense(self, expense: SubscriptionExpense):
        """
        Insert a ``SubscriptionExpense`` record into the database.

        Args:
            expense (SubscriptionExpense): Subscription expense to persist.
        """
        with self._source_data_uow as uow:
            uow.source_data_repo.insert_subscription_expense(expense=expense)
            uow.commit()

    def insert_venmo(self, venmo: Venmo):
        """
        Insert a ``Venmo`` record into the database.

        Args:
            venmo (Venmo): Venmo record to persist.
        """
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

    def insert_new_user(self, user_info: User) -> None:
        """
        Inserts a new user record into the database.

        Args:
            user_info (User): User information to persist.
        """
        with self._source_data_uow as uow:
            uow.source_data_repo.insert_new_user(user_info=user_info)
            uow.commit()

    def get_login_by_username(self, username: str) -> Login | None:
        """
        Retrieve a login by username if present.

        Args:
            username (str): Username to search for.

        Returns:
            login (Login | None): Retrieved login record or None if not found.
        """
        with self._source_data_uow as uow:
            login = uow.source_data_repo.get_login_by_username(username=username)
        return login


    def get_monthly_expenses(self, date: dt.datetime) -> MonthlyExpenses:
        """
        Retrieve monthly expenses for the specified date from the repository.

        Args:
            date (datetime): Date of the monthly expenses.

        Returns:
            monthly_expenses (MonthlyExpenses): Retrieved monthly expenses record.
        """
        with self._source_data_uow as uow:
            monthly_expenses = uow.source_data_repo.get_monthly_expenses(date=date)
        return monthly_expenses