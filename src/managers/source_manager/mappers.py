from src.database.database import (
    ApartmentSpendingTable,
    CarTable,
    ClothingTable,
    EatingOutTable,
    GiftTable,
    GroceriesTable,
    IncomeTable,
    InvestmentsTable,
    InvestmentTypeTable,
    MiscExpenseTable,
    NetWorthTable,
    SinkingFundTable,
    SinkingFundTypeTable,
    SubscriptionTable,
    VenmoTable,
    LoginTable,
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
    Login,
    MiscExpense,
    NetWorth,
    SinkingFund,
    SinkingFundType,
    SubscriptionExpense,
    Venmo,
)
from src.security import hash_password


def map_entity_to_domain_apartment_spending(
    record: ApartmentSpendingTable,
) -> ApartmentExpense:
    """
    Convert an ``ApartmentSpendingTable`` row into a domain ``ApartmentExpense``.

    Args:
        record (ApartmentSpendingTable): Database entity to convert.

    Returns:
        expense (ApartmentExpense): Domain object created from the row.
    """
    return ApartmentExpense(
        date=record.Date,
        amount=record.Amount,
        description=record.Description,
    )


def map_domain_to_entity_apartment_spending(
    expense: ApartmentExpense,
) -> ApartmentSpendingTable:
    """
    Convert a domain ``ApartmentExpense`` into its ORM representation.

    Args:
        expense (ApartmentExpense): Domain model to convert.

    Returns:
        record (ApartmentSpendingTable): ORM entity ready for persistence.
    """
    return ApartmentSpendingTable(
        Date=expense.date,
        Amount=expense.amount,
        Description=expense.description,
    )


def map_entity_to_domain_car_expense(record: CarTable) -> CarExpense:
    """
    Convert a ``CarTable`` row into a domain ``CarExpense``.

    Args:
        record (CarTable): ORM record representing a car expense.

    Returns:
        expense (CarExpense): Domain model created from the record.
    """
    return CarExpense(
        date=record.Date,
        amount=record.Amount,
        description=record.Description,
    )


def map_domain_to_entity_car_expense(expense: CarExpense) -> CarTable:
    """
    Convert a domain ``CarExpense`` into a ``CarTable`` row.

    Args:
        expense (CarExpense): Domain object to convert.

    Returns:
        record (CarTable): ORM entity populated from the domain object.
    """
    return CarTable(
        Date=expense.date,
        Amount=expense.amount,
        Description=expense.description,
    )


def map_entity_to_domain_clothing_expense(record: ClothingTable) -> ClothingExpense:
    """
    Convert a ``ClothingTable`` row into a domain ``ClothingExpense``.

    Args:
        record (ClothingTable): ORM record for a clothing expense.

    Returns:
        expense (ClothingExpense): Domain object created from ``record``.
    """
    return ClothingExpense(
        date=record.Date,
        amount=record.Amount,
        description=record.Description,
    )


def map_domain_to_entity_clothing_expense(expense: ClothingExpense) -> ClothingTable:
    """
    Convert a domain ``ClothingExpense`` to its database representation.

    Args:
        expense (ClothingExpense): Domain model to convert.

    Returns:
        record (ClothingTable): ORM entity built from ``expense``.
    """
    return ClothingTable(
        Date=expense.date,
        Amount=expense.amount,
        Description=expense.description,
    )


def map_entity_to_domain_eating_out_expense(record: EatingOutTable) -> EatingOutExpense:
    """
    Convert an ``EatingOutTable`` row into a domain ``EatingOutExpense``.

    Args:
        record (EatingOutTable): ORM record for an eating out expense.

    Returns:
        expense (EatingOutExpense): Domain object derived from ``record``.
    """
    return EatingOutExpense(
        date=record.Date,
        place=record.Place,
        amount=record.Amount,
        description=record.Description,
    )


def map_domain_to_entity_eating_out_expense(
    expense: EatingOutExpense,
) -> EatingOutTable:
    """
    Convert a domain ``EatingOutExpense`` into an ``EatingOutTable`` row.

    Args:
        expense (EatingOutExpense): Domain object to convert.

    Returns:
        record (EatingOutTable): ORM entity populated from the domain object.
    """
    return EatingOutTable(
        Date=expense.date,
        Place=expense.place,
        Amount=expense.amount,
        Description=expense.description,
    )


def map_entity_to_domain_gift_expense(record: GiftTable) -> GiftExpense:
    """
    Convert a ``GiftTable`` row into a domain ``GiftExpense``.

    Args:
        record (GiftTable): ORM entity representing a gift expense.

    Returns:
        expense (GiftExpense): Domain object created from ``record``.
    """
    return GiftExpense(
        date=record.Date,
        amount=record.Amount,
        description=record.Description,
    )


def map_domain_to_entity_gift_expense(expense: GiftExpense) -> GiftTable:
    """
    Convert a domain ``GiftExpense`` into a ``GiftTable`` record.

    Args:
        expense (GiftExpense): Domain model to convert.

    Returns:
        record (GiftTable): ORM entity corresponding to the gift expense.
    """
    return GiftTable(
        Date=expense.date,
        Amount=expense.amount,
        Description=expense.description,
    )


def map_entity_to_domain_groceries(record: GroceriesTable) -> GroceriesExpense:
    """
    Convert a ``GroceriesTable`` row into a domain ``GroceriesExpense``.

    Args:
        record (GroceriesTable): ORM record representing grocery spending.

    Returns:
        expense (GroceriesExpense): Domain model derived from ``record``.
    """
    return GroceriesExpense(
        date=record.Date,
        amount=record.Amount,
        description=record.Description,
    )


def map_domain_to_entity_groceries(expense: GroceriesExpense) -> GroceriesTable:
    """
    Convert a ``GroceriesExpense`` domain object into a ``GroceriesTable`` row.

    Args:
        expense (GroceriesExpense): Domain object to convert.

    Returns:
        record (GroceriesTable): ORM entity created from ``expense``.
    """
    return GroceriesTable(
        Date=expense.date,
        Amount=expense.amount,
        Description=expense.description,
    )


def map_entity_to_domain_income(record: IncomeTable) -> Income:
    """
    Convert an ``IncomeTable`` row into the ``Income`` domain model.

    Args:
        record (IncomeTable): ORM record representing income.

    Returns:
        income (Income): Domain object built from the record.
    """
    return Income(
        date=record.Date,
        source=record.Source,
        gross_pay=record.GrossPay,
        taxes=record.Taxes,
    )


def map_domain_to_entity_income(income: Income) -> IncomeTable:
    """
    Convert a domain ``Income`` instance into an ``IncomeTable`` row.

    Args:
        income (Income): Domain model to convert.

    Returns:
        record (IncomeTable): ORM entity created from ``income``.
    """
    net_pay = income.gross_pay - (income.taxes or 0)
    return IncomeTable(
        Date=income.date,
        Source=income.source,
        GrossPay=income.gross_pay,
        Taxes=income.taxes,
        NetPay=net_pay,
    )


def map_entity_to_domain_investment(record: InvestmentsTable) -> Investment:
    """
    Convert an ``InvestmentsTable`` row into a domain ``Investment``.

    Args:
        record (InvestmentsTable): ORM investment record.

    Returns:
        investment (Investment): Domain object created from the record.
    """
    return Investment(
        fk_investment_type=record.FKInvestmentType,
    )


def map_domain_to_entity_investment(investment: Investment) -> InvestmentsTable:
    """
    Convert a domain ``Investment`` into an ``InvestmentsTable`` record.

    Args:
        investment (Investment): Domain model describing an investment.

    Returns:
        record (InvestmentsTable): ORM entity built from the domain data.
    """
    return InvestmentsTable(
        FKInvestmentType=investment.fk_investment_type,
    )


def map_entity_to_domain_investment_type(record: InvestmentTypeTable) -> InvestmentType:
    """
    Convert an ``InvestmentTypeTable`` row into the ``InvestmentType`` domain model.

    Args:
        record (InvestmentTypeTable): ORM record describing an investment type.

    Returns:
        investment_type (InvestmentType): Domain object derived from ``record``.
    """
    return InvestmentType(
        investment_type=record.InvestmentType,
    )


def map_domain_to_entity_investment_type(
    investment_type: InvestmentType,
) -> InvestmentTypeTable:
    """
    Convert a domain ``InvestmentType`` into an ``InvestmentTypeTable`` row.

    Args:
        investment_type (InvestmentType): Domain investment type model.

    Returns:
        record (InvestmentTypeTable): ORM entity created from ``investment_type``.
    """
    return InvestmentTypeTable(
        InvestmentType=investment_type.investment_type,
    )


def map_entity_to_domain_misc_expense(record: MiscExpenseTable) -> MiscExpense:
    """
    Convert a ``MiscExpenseTable`` row into a domain ``MiscExpense``.

    Args:
        record (MiscExpenseTable): ORM record for miscellaneous expenses.

    Returns:
        expense (MiscExpense): Domain object derived from ``record``.
    """
    return MiscExpense(
        date=record.Date,
        amount=record.Amount,
        description=record.Description,
    )


def map_domain_to_entity_misc_expense(expense: MiscExpense) -> MiscExpenseTable:
    """
    Convert a domain ``MiscExpense`` into a ``MiscExpenseTable`` record.

    Args:
        expense (MiscExpense): Domain model describing the expense.

    Returns:
        record (MiscExpenseTable): ORM entity built from ``expense``.
    """
    return MiscExpenseTable(
        Date=expense.date,
        Amount=expense.amount,
        Description=expense.description,
    )


def map_entity_to_domain_net_worth(record: NetWorthTable) -> NetWorth:
    """
    Convert a ``NetWorthTable`` row into the ``NetWorth`` domain model.

    Args:
        record (NetWorthTable): ORM row for net worth.

    Returns:
        net_worth (NetWorth): Domain object created from ``record``.
    """
    return NetWorth(
        date=record.Date,
        net_worth=record.NetWorth,
    )


def map_domain_to_entity_new_user(new_user: CreateUser) -> User


def map_domain_to_entity_net_worth(net_worth: NetWorth) -> NetWorthTable:
    """
    Convert a domain ``NetWorth`` into a ``NetWorthTable`` record.

    Args:
        net_worth (NetWorth): Domain model containing net worth data.

    Returns:
        record (NetWorthTable): ORM entity built from ``net_worth``.
    """
    return NetWorthTable(
        Date=net_worth.date,
        NetWorth=net_worth.net_worth,
    )


def map_entity_to_domain_sinking_fund(record: SinkingFundTable) -> SinkingFund:
    """
    Convert a ``SinkingFundTable`` row into a ``SinkingFund`` domain object.

    Args:
        record (SinkingFundTable): ORM record for a sinking fund entry.

    Returns:
        fund (SinkingFund): Domain model created from ``record``.
    """
    return SinkingFund(
        amount=record.Amount,
        fk_sinking_fund_type=record.FKSinkingFundType,
        date=record.Date,
    )


def map_domain_to_entity_sinking_fund(fund: SinkingFund) -> SinkingFundTable:
    """
    Convert a ``SinkingFund`` domain object into a ``SinkingFundTable`` row.

    Args:
        fund (SinkingFund): Domain sinking fund instance to convert.

    Returns:
        record (SinkingFundTable): ORM entity built from ``fund``.
    """
    return SinkingFundTable(
        Amount=fund.amount,
        FKSinkingFundType=fund.fk_sinking_fund_type,
        Date=fund.date,
    )


def map_entity_to_domain_sinking_fund_type(
    record: SinkingFundTypeTable,
) -> SinkingFundType:
    """
    Convert a ``SinkingFundTypeTable`` row into a ``SinkingFundType`` domain model.

    Args:
        record (SinkingFundTypeTable): ORM record for a sinking fund type.

    Returns:
        fund_type (SinkingFundType): Domain object derived from ``record``.
    """
    return SinkingFundType(
        fund_type=record.FundType,
        total=record.Total,
    )


def map_domain_to_entity_sinking_fund_type(
    fund_type: SinkingFundType,
) -> SinkingFundTypeTable:
    """
    Convert a ``SinkingFundType`` domain object into a ``SinkingFundTypeTable`` row.

    Args:
        fund_type (SinkingFundType): Domain fund type to convert.

    Returns:
        record (SinkingFundTypeTable): ORM entity created from ``fund_type``.
    """
    return SinkingFundTypeTable(
        FundType=fund_type.fund_type,
        Total=fund_type.total,
    )


def map_entity_to_domain_subscription_expense(
    record: SubscriptionTable,
) -> SubscriptionExpense:
    """
    Convert a ``SubscriptionTable`` row into a domain ``SubscriptionExpense``.

    Args:
        record (SubscriptionTable): ORM record for subscription spending.

    Returns:
        expense (SubscriptionExpense): Domain object created from ``record``.
    """
    return SubscriptionExpense(
        date=record.Date,
        amount=record.Amount,
        description=record.Description,
    )


def map_domain_to_entity_subscription_expense(
    expense: SubscriptionExpense,
) -> SubscriptionTable:
    """
    Convert a domain ``SubscriptionExpense`` into a ``SubscriptionTable`` record.

    Args:
        expense (SubscriptionExpense): Domain subscription expense.

    Returns:
        record (SubscriptionTable): ORM entity created from ``expense``.
    """
    return SubscriptionTable(
        Date=expense.date,
        Amount=expense.amount,
        Description=expense.description,
    )


def map_entity_to_domain_venmo(record: VenmoTable) -> Venmo:
    """
    Convert a ``VenmoTable`` row into a domain ``Venmo`` record.

    Args:
        record (VenmoTable): ORM record representing a Venmo transaction.

    Returns:
        venmo (Venmo): Domain object built from ``record``.
    """
    return Venmo(
        date=record.Date,
        amount=record.Amount,
        description=record.Description,
    )


def map_domain_to_entity_venmo(venmo: Venmo) -> VenmoTable:
    """
    Convert a domain ``Venmo`` object into a ``VenmoTable`` row.

    Args:
        venmo (Venmo): Domain transaction data to convert.

    Returns:
        record (VenmoTable): ORM entity created from ``venmo``.
    """
    return VenmoTable(
        Date=venmo.date,
        Amount=venmo.amount,
        Description=venmo.description,
    )


def map_entity_to_domain_login(record: LoginTable) -> Login:
    """Convert a ``LoginTable`` row into a ``Login`` domain object."""

    return Login(
        username=record.Username,
        password=record.Password,
    )


def map_domain_to_entity_login(login: Login) -> LoginTable:
    """Convert a ``Login`` domain object into a ``LoginTable`` row."""

    return LoginTable(
        Username=login.username,
        Password=hash_password(login.password),
    )
