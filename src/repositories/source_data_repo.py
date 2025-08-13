import datetime as dt

from sqlalchemy.orm import Session

from src.database.database import (
    GroceriesTable,
    UserTable,
)
from src.managers.source_manager.domain import (
    ApartmentExpense,
    CarExpense,
    ClothingExpense,
    User,
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
    Venmo
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
    map_domain_to_entity_user,
    map_domain_to_entity_venmo,
    map_entity_to_domain_login,
    map_entity_to_domain_groceries,
    map_entity_to_domain_user,
)


class SourceDataRepository:

    def __init__(self, session: Session):
        """
        Store the SQLAlchemy session used for all repository operations.

        Args:
            session (Session): Active database session.
        """
        self._session = session

    def insert_groceries(self, groceries: GroceriesExpense) -> None:
        """
        Add a groceries record to the database.

        Args:
            groceries (GroceriesExpense): Expense to persist.
        """
        groceries_record = map_domain_to_entity_groceries(expense=groceries)
        self._session.add(groceries_record)

    def insert_apartment_expense(self, expense: ApartmentExpense) -> None:
        """
        Insert an apartment expense record.

        Args:
            expense (ApartmentExpense): Expense to add.
        """
        record = map_domain_to_entity_apartment_spending(expense)
        self._session.add(record)

    def insert_car_expense(self, expense: CarExpense) -> None:
        """
        Insert a car expense entry.

        Args:
            expense (CarExpense): Expense to add.
        """
        record = map_domain_to_entity_car_expense(expense)
        self._session.add(record)

    def insert_clothing_expense(self, expense: ClothingExpense) -> None:
        """
        Insert a clothing expense entry.

        Args:
            expense (ClothingExpense): Expense to add.
        """
        record = map_domain_to_entity_clothing_expense(expense)
        self._session.add(record)

    def insert_eating_out_expense(self, expense: EatingOutExpense) -> None:
        """
        Insert an eating out expense entry.

        Args:
            expense (EatingOutExpense): Expense to add.
        """
        record = map_domain_to_entity_eating_out_expense(expense)
        self._session.add(record)

    def insert_gift_expense(self, expense: GiftExpense) -> None:
        """
        Insert a gift expense record.

        Args:
            expense (GiftExpense): Expense to add.
        """
        record = map_domain_to_entity_gift_expense(expense)
        self._session.add(record)

    def insert_income(self, income: Income) -> None:
        """
        Insert an income record into the database.

        Args:
            income (Income): Income record to add.
        """
        record = map_domain_to_entity_income(income)
        self._session.add(record)

    def insert_investment(self, investment: Investment) -> None:
        """
        Insert an investment record.

        Args:
            investment (Investment): Investment to persist.
        """
        record = map_domain_to_entity_investment(investment)
        self._session.add(record)

    def insert_investment_type(self, investment_type: InvestmentType) -> None:
        """
        Insert a new investment type.

        Args:
            investment_type (InvestmentType): Investment type to persist.
        """
        record = map_domain_to_entity_investment_type(investment_type)
        self._session.add(record)

    def insert_new_user(self, user_info: User) -> None:
        """
        Insert a new user

        Args:
            user_info (CreateUser): new user info
        """
        record = map_domain_to_entity_new_user()
        self._session.add(record)

    def insert_misc_expense(self, expense: MiscExpense) -> None:
        """
        Insert a miscellaneous expense record.

        Args:
            expense (MiscExpense): Expense to add.
        """
        record = map_domain_to_entity_misc_expense(expense)
        self._session.add(record)

    def insert_net_worth(self, net_worth: NetWorth) -> None:
        """
        Insert a net worth entry.

        Args:
            net_worth (NetWorth): Net worth data to persist.
        """
        record = map_domain_to_entity_net_worth(net_worth)
        self._session.add(record)

    def insert_sinking_fund(self, fund: SinkingFund) -> None:
        """
        Insert a sinking fund entry.

        Args:
            fund (SinkingFund): Sinking fund to persist.
        """
        record = map_domain_to_entity_sinking_fund(fund)
        self._session.add(record)

    def insert_sinking_fund_type(self, fund_type: SinkingFundType) -> None:
        """
        Insert a sinking fund type record.

        Args:
            fund_type (SinkingFundType): Type to add.
        """
        record = map_domain_to_entity_sinking_fund_type(fund_type)
        self._session.add(record)

    def insert_subscription_expense(self, expense: SubscriptionExpense) -> None:
        """
        Insert a subscription expense entry.

        Args:
            expense (SubscriptionExpense): Subscription to add.
        """
        record = map_domain_to_entity_subscription_expense(expense)
        self._session.add(record)

    def insert_venmo(self, venmo: Venmo) -> None:
        """
        Insert a Venmo transaction entry.

        Args:
            venmo (Venmo): Venmo transaction to persist.
        """
        record = map_domain_to_entity_venmo(venmo)
        self._session.add(record)

    def get_groceries_by_date(self, date: dt.datetime) -> GroceriesExpense | None:
        """
        Fetch groceries for a specific date.

        Args:
            date (datetime): Date to query.

        Returns:
            groceries (GroceriesExpense | None): Retrieved groceries expense if present.
        """
        record = (
            self._session.query(GroceriesTable)
            .where(GroceriesTable.Date == date)
            .first()
        )
        if record:
            groceries = map_entity_to_domain_groceries(record=record)
            return groceries

    def insert_new_user(self, user_info: User) -> None:
        """Insert a login record into the database."""
        record = map_domain_to_entity_user(user_info)
        self._session.add(record)

    def get_login_by_username(self, username: str) -> User | None:
        """Retrieve a login by username if present."""

        record = (
            self._session.query(UserTable)
            .where(UserTable.Username == username)
            .first()
        )
        if record:
            return map_entity_to_domain_user(record=record)
        return None
