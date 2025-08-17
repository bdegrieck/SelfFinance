from src.database.database import (
    User,
    Expense,
    Income,
    Investment,
    SinkingFund,
    NetWorth,
    Subscription,
)
from src.managers.source_manager.domain import (
    User as DomainUser,
    Expense as DomainExpense,
    GroceriesExpense,
    Income as DomainIncome,
    Investment as DomainInvestment,
    NetWorth as DomainNetWorth,
    SinkingFund as DomainSinkingFund,
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
    return Expense(
        Category="Groceries",  # Set category directly as string
        Amount=expense.amount,
        Description=expense.description,
        Date=expense.date,
        # UserId will need to be set when implementing
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
        date=record.Date,
        amount=record.Amount,
        description=record.Description,
    )


def map_entity_to_domain_expenses(records: list[Expense]) -> list[DomainExpense]:
    """
    Convert a list of ``Expense`` rows into a list of domain ``Expense`` objects.
    """
    return [map_entity_to_domain_expense(record) for record in records]


def map_domain_to_entity_expense(expense: DomainExpense) -> Expense:
    """
    Convert a domain ``Expense`` into an ``Expense`` entity.

    Args:
        expense (DomainExpense): Domain object to convert.

    Returns:
        record (Expense): ORM entity created from ``expense``.
    """
    return Expense(
        Id=expense.id,
        UserId=expense.user_id,
        Category=expense.category,
        Amount=expense.amount,
        Description=expense.description,
        Date=expense.date,
        Place=expense.place,
    )


def map_entity_to_domain_expense(record: Expense) -> DomainExpense:
    """
    Convert an ``Expense`` row into a domain ``Expense``.

    Args:
        record (Expense): ORM record representing an expense.

    Returns:
        expense (DomainExpense): Domain model derived from ``record``.
    """
    return DomainExpense(
        id=record.Id,
        user_id=record.UserId,
        category=record.Category,
        amount=record.Amount,
        description=record.Description,
        date=record.Date,
        place=record.Place,
    )


def map_domain_to_entity_user(user: DomainUser) -> User:
    """
    Maps domain user to new user table.

    Args:
        user (DomainUser): domain model of a user
    """
    return User(
        Username=user.username,
        PasswordHash=hash_password(user.password),
        FirstName=user.first_name,
        LastName=user.last_name,
        Email=user.email,
    )


def map_entity_to_domain_user(record: User) -> DomainUser:
    """
    Maps user from table to domain object

    Args:
        record (User): Entity object of the user
    """
    return DomainUser(
        username=record.Username,
        password=record.PasswordHash,  # Note: returning hash, not plain text
        first_name=record.FirstName,
        last_name=record.LastName,
        email=record.Email,
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
        Date=income.date,
        Category=income.source,  # Use source as category
        Amount=income.gross_pay,
        Description=f"Source: {income.source}",
        # UserId will need to be set when implementing
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
        date=record.Date,
        source=record.Category,  # Category field now contains the source
        gross_pay=record.Amount,
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


def map_domain_to_entity_net_worth(net_worth: DomainNetWorth) -> NetWorth:
    """
    Convert a domain ``NetWorth`` into a ``NetWorth`` entity.

    Args:
        net_worth (DomainNetWorth): Domain model containing net worth data.

    Returns:
        record (NetWorth): ORM entity built from ``net_worth``.
    """
    return NetWorth(
        Date=net_worth.date,
        NetWorth=net_worth.net_worth,
        # UserId will need to be set when implementing
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
        date=record.Date,
        net_worth=record.NetWorth,
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
        Amount=fund.amount,
        Date=fund.date,
        # UserId will need to be set when implementing
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
        amount=record.Amount,
        fk_sinking_fund_type=0,  # TODO: Implement when category system is set up
        date=record.Date,
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
        Name=expense.description or "Subscription",
        Amount=expense.amount,
        Frequency="monthly",  # Default to monthly, can be made configurable
        StartDate=expense.date,
        # UserId will need to be set when implementing
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
        date=record.StartDate,
        amount=record.Amount,
        description=record.Name,
    )
