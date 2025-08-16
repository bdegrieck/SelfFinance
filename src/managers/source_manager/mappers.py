from src.database.database import (
    User,
    Expense,
    Category,
    Income,
    Investment,
    InvestmentType,
    SinkingFund,
    SinkingFundType,
    NetWorth,
    Subscription,
)
from src.managers.source_manager.domain import (
    User as DomainUser,
    GroceriesExpense,
    Income as DomainIncome,
    Investment as DomainInvestment,
    InvestmentType as DomainInvestmentType,
    NetWorth as DomainNetWorth,
    SinkingFund as DomainSinkingFund,
    SinkingFundType as DomainSinkingFundType,
    SubscriptionExpense as DomainSubscriptionExpense,
)
from src.security import hash_password


def map_domain_to_entity_groceries(expense: GroceriesExpense) -> Expense:
    """
    Convert a domain ``GroceriesExpense`` into an ``Expense`` entity.

    Args:
        expense (GroceriesExpense): Domain object to convert.

    Returns:
        record (Expense): ORM entity created from ``expense``.
    """
    # TODO: Need to get or create a "Groceries" category first
    return Expense(
        amount=expense.amount,
        description=expense.description,
        date=expense.date,
        # category_id will need to be set when category system is implemented
    )


def map_entity_to_domain_groceries(record: Expense) -> GroceriesExpense:
    """
    Convert an ``Expense`` row into a domain ``GroceriesExpense``.

    Args:
        record (Expense): ORM record representing grocery spending.

    Returns:
        expense (GroceriesExpense): Domain model derived from ``record``.
    """
    return GroceriesExpense(
        date=record.date,
        amount=record.amount,
        description=record.description,
    )


def map_domain_to_entity_user(user: DomainUser) -> User:
    """
    Maps domain user to new user table.

    Args:
        user (DomainUser): domain model of a user
    """
    return User(
        username=user.username,
        password_hash=hash_password(user.password),
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
    )


def map_entity_to_domain_user(record: User) -> DomainUser:
    """
    Maps user from table to domain object

    Args:
        record (User): Entity object of the user
    """
    return DomainUser(
        username=record.username,
        password=record.password_hash,  # Note: returning hash, not plain text
        first_name=record.first_name,
        last_name=record.last_name,
        email=record.email,
    )


def map_domain_to_entity_income(income: DomainIncome) -> Income:
    """
    Convert a domain ``Income`` instance into an ``Income`` entity.

    Args:
        income (DomainIncome): Domain model to convert.

    Returns:
        record (Income): ORM entity created from ``income``.
    """
    return Income(
        date=income.date,
        amount=income.gross_pay,
        description=f"Source: {income.source}",
        # user_id and category_id will need to be set when implementing
    )


def map_entity_to_domain_income(record: Income) -> DomainIncome:
    """
    Convert an ``Income`` row into the ``Income`` domain model.

    Args:
        record (Income): ORM record representing income.

    Returns:
        income (DomainIncome): Domain object built from the record.
    """
    # TODO: Parse source from description when category system is implemented
    return DomainIncome(
        date=record.date,
        source="Unknown",  # Will need to parse from description or category
        gross_pay=record.amount,
        taxes=0,  # Not stored in new schema
    )


def map_domain_to_entity_investment(investment: DomainInvestment) -> Investment:
    """
    Convert a domain ``Investment`` into an ``Investment`` entity.

    Args:
        investment (DomainInvestment): Domain model describing an investment.

    Returns:
        record (Investment): ORM entity built from the domain data.
    """
    # TODO: Implement when investment system is set up
    pass


def map_entity_to_domain_investment(record: Investment) -> DomainInvestment:
    """
    Convert an ``Investment`` row into a domain ``Investment``.

    Args:
        record (Investment): ORM investment record.

    Returns:
        investment (DomainInvestment): Domain object created from the record.
    """
    # TODO: Implement when investment system is set up
    pass


def map_domain_to_entity_investment_type(
    investment_type: DomainInvestmentType,
) -> InvestmentType:
    """
    Convert a domain ``InvestmentType`` into an ``InvestmentType`` entity.

    Args:
        investment_type (DomainInvestmentType): Domain investment type model.

    Returns:
        record (InvestmentType): ORM entity created from ``investment_type``.
    """
    return InvestmentType(
        name=investment_type.investment_type,
        type="investment",
    )


def map_entity_to_domain_investment_type(
    record: InvestmentType,
) -> DomainInvestmentType:
    """
    Convert an ``InvestmentType`` row into the ``InvestmentType`` domain model.

    Args:
        record (InvestmentType): ORM record describing an investment type.

    Returns:
        investment_type (DomainInvestmentType): Domain object derived from ``record``.
    """
    return DomainInvestmentType(
        investment_type=record.name,
    )


def map_domain_to_entity_net_worth(net_worth: DomainNetWorth) -> NetWorth:
    """
    Convert a domain ``NetWorth`` into a ``NetWorth`` entity.

    Args:
        net_worth (DomainNetWorth): Domain model containing net worth data.

    Returns:
        record (NetWorth): ORM entity built from ``net_worth``.
    """
    return NetWorth(
        date=net_worth.date,
        amount=net_worth.net_worth,
        # user_id will need to be set when implementing
    )


def map_entity_to_domain_net_worth(record: NetWorth) -> DomainNetWorth:
    """
    Convert a ``NetWorth`` row into the ``NetWorth`` domain model.

    Args:
        record (NetWorth): ORM row for net worth.

    Returns:
        net_worth (DomainNetWorth): Domain object created from ``record``.
    """
    return DomainNetWorth(
        date=record.date,
        net_worth=record.amount,
    )


def map_domain_to_entity_sinking_fund(fund: DomainSinkingFund) -> SinkingFund:
    """
    Convert a domain ``SinkingFund`` domain object into a ``SinkingFund`` entity.

    Args:
        fund (DomainSinkingFund): Domain sinking fund instance to convert.

    Returns:
        record (SinkingFund): ORM entity built from ``fund``.
    """
    return SinkingFund(
        amount=fund.amount,
        date=fund.date,
        # user_id and category_id will need to be set when implementing
    )


def map_entity_to_domain_sinking_fund(record: SinkingFund) -> DomainSinkingFund:
    """
    Convert a ``SinkingFund`` row into a ``SinkingFund`` domain object.

    Args:
        record (SinkingFund): ORM record for a sinking fund entry.

    Returns:
        fund (DomainSinkingFund): Domain model created from ``record``.
    """
    return DomainSinkingFund(
        amount=record.amount,
        fk_sinking_fund_type=0,  # TODO: Implement when category system is set up
        date=record.date,
    )


def map_domain_to_entity_sinking_fund_type(
    fund_type: DomainSinkingFundType,
) -> SinkingFundType:
    """
    Convert a domain ``SinkingFundType`` domain object into a ``SinkingFundType`` entity.

    Args:
        fund_type (DomainSinkingFundType): Domain fund type to convert.

    Returns:
        record (SinkingFundType): ORM entity created from ``fund_type``.
    """
    return SinkingFundType(
        name=fund_type.fund_type,
        type="sinking_fund",
        total=fund_type.total,
    )


def map_entity_to_domain_sinking_fund_type(
    record: SinkingFundType,
) -> DomainSinkingFundType:
    """
    Convert a ``SinkingFundType`` row into a ``SinkingFundType`` domain model.

    Args:
        record (SinkingFundType): ORM record for a sinking fund type.

    Returns:
        fund_type (DomainSinkingFundType): Domain object derived from ``record``.
    """
    return DomainSinkingFundType(
        fund_type=record.name,
        total=record.total,
    )


def map_domain_to_entity_subscription_expense(
    expense: DomainSubscriptionExpense,
) -> Subscription:
    """
    Convert a domain ``SubscriptionExpense`` into a ``Subscription`` entity.

    Args:
        expense (DomainSubscriptionExpense): Domain subscription expense.

    Returns:
        record (Subscription): ORM entity created from ``expense``.
    """
    return Subscription(
        name=expense.description or "Subscription",
        amount=expense.amount,
        frequency="monthly",  # Default to monthly, can be made configurable
        start_date=expense.date,
        # user_id and category_id will need to be set when implementing
    )


def map_entity_to_domain_subscription_expense(
    record: Subscription,
) -> DomainSubscriptionExpense:
    """
    Convert a ``Subscription`` row into a domain ``SubscriptionExpense``.

    Args:
        record (Subscription): ORM record for subscription spending.

    Returns:
        expense (DomainSubscriptionExpense): Domain object created from ``record``.
    """
    return DomainSubscriptionExpense(
        date=record.start_date,
        amount=record.amount,
        description=record.name,
    )
