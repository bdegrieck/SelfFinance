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


def map_entity_to_domain_apartment_spending(
    record: ApartmentSpendingTable,
) -> ApartmentExpense:
    return ApartmentExpense(
        date=record.Date,
        item=record.Item,
        amount=record.Amount,
        description=record.Description,
    )


def map_domain_to_entity_apartment_spending(
    expense: ApartmentExpense,
) -> ApartmentSpendingTable:
    return ApartmentSpendingTable(
        Date=expense.date,
        Item=expense.item,
        Amount=expense.amount,
        Description=expense.description,
    )


def map_entity_to_domain_car_expense(record: CarTable) -> CarExpense:
    return CarExpense(
        date=record.Date,
        item=record.Item,
        amount=record.Amount,
        description=record.Description,
    )


def map_domain_to_entity_car_expense(expense: CarExpense) -> CarTable:
    return CarTable(
        Date=expense.date,
        Item=expense.item,
        Amount=expense.amount,
        Description=expense.description,
    )


def map_entity_to_domain_clothing_expense(record: ClothingTable) -> ClothingExpense:
    return ClothingExpense(
        date=record.Date,
        amount=record.Amount,
        description=record.Description,
    )


def map_domain_to_entity_clothing_expense(expense: ClothingExpense) -> ClothingTable:
    return ClothingTable(
        Date=expense.date,
        Amount=expense.amount,
        Description=expense.description,
    )


def map_entity_to_domain_eating_out_expense(record: EatingOutTable) -> EatingOutExpense:
    return EatingOutExpense(
        date=record.Date,
        place=record.Place,
        amount=record.Amount,
        description=record.Description,
    )


def map_domain_to_entity_eating_out_expense(expense: EatingOutExpense) -> EatingOutTable:
    return EatingOutTable(
        Date=expense.date,
        Place=expense.place,
        Amount=expense.amount,
        Description=expense.description,
    )


def map_entity_to_domain_gift_expense(record: GiftTable) -> GiftExpense:
    return GiftExpense(
        date=record.Date,
        amount=record.Amount,
        description=record.Description,
    )


def map_domain_to_entity_gift_expense(expense: GiftExpense) -> GiftTable:
    return GiftTable(
        Date=expense.date,
        Amount=expense.amount,
        Description=expense.description,
    )


def map_entity_to_domain_groceries(record: GroceriesTable) -> GroceriesExpense:
    return GroceriesExpense(
        date=record.Date,
        amount=record.Amount,
        description=record.Description,
    )


def map_domain_to_entity_groceries(expense: GroceriesExpense) -> GroceriesTable:
    return GroceriesTable(
        Date=expense.date,
        Amount=expense.amount,
        Description=expense.description,
    )


def map_entity_to_domain_income(record: IncomeTable) -> Income:
    return Income(
        date=record.Date,
        source=record.Source,
        gross_pay=record.GrossPay,
        taxes=record.Taxes,
    )


def map_domain_to_entity_income(income: Income) -> IncomeTable:
    net_pay = income.gross_pay - (income.taxes or 0)
    return IncomeTable(
        Date=income.date,
        Source=income.source,
        GrossPay=income.gross_pay,
        Taxes=income.taxes,
        NetPay=net_pay,
    )


def map_entity_to_domain_investment(record: InvestmentsTable) -> Investment:
    return Investment(
        fk_investment_type=record.FKInvestmentType,
    )


def map_domain_to_entity_investment(investment: Investment) -> InvestmentsTable:
    return InvestmentsTable(
        FKInvestmentType=investment.fk_investment_type,
    )


def map_entity_to_domain_investment_type(record: InvestmentTypeTable) -> InvestmentType:
    return InvestmentType(
        investment_type=record.InvestmentType,
    )


def map_domain_to_entity_investment_type(investment_type: InvestmentType) -> InvestmentTypeTable:
    return InvestmentTypeTable(
        InvestmentType=investment_type.investment_type,
    )


def map_entity_to_domain_misc_expense(record: MiscExpenseTable) -> MiscExpense:
    return MiscExpense(
        date=record.Date,
        amount=record.Amount,
        description=record.Description,
    )


def map_domain_to_entity_misc_expense(expense: MiscExpense) -> MiscExpenseTable:
    return MiscExpenseTable(
        Date=expense.date,
        Amount=expense.amount,
        Description=expense.description,
    )


def map_entity_to_domain_net_worth(record: NetWorthTable) -> NetWorth:
    return NetWorth(
        date=record.Date,
        net_worth=record.NetWorth,
    )


def map_domain_to_entity_net_worth(net_worth: NetWorth) -> NetWorthTable:
    return NetWorthTable(
        Date=net_worth.date,
        NetWorth=net_worth.net_worth,
    )


def map_entity_to_domain_sinking_fund(record: SinkingFundTable) -> SinkingFund:
    return SinkingFund(
        amount=record.Amount,
        fk_sinking_fund_type=record.FKSinkingFundType,
        date=record.Date,
    )


def map_domain_to_entity_sinking_fund(fund: SinkingFund) -> SinkingFundTable:
    return SinkingFundTable(
        Amount=fund.amount,
        FKSinkingFundType=fund.fk_sinking_fund_type,
        Date=fund.date,
    )


def map_entity_to_domain_sinking_fund_type(record: SinkingFundTypeTable) -> SinkingFundType:
    return SinkingFundType(
        fund_type=record.FundType,
        total=record.Total,
    )


def map_domain_to_entity_sinking_fund_type(fund_type: SinkingFundType) -> SinkingFundTypeTable:
    return SinkingFundTypeTable(
        FundType=fund_type.fund_type,
        Total=fund_type.total,
    )


def map_entity_to_domain_subscription_expense(record: SubscriptionTable) -> SubscriptionExpense:
    return SubscriptionExpense(
        date=record.Date,
        item=record.Item,
        amount=record.Amount,
        description=record.Description,
    )


def map_domain_to_entity_subscription_expense(expense: SubscriptionExpense) -> SubscriptionTable:
    return SubscriptionTable(
        Date=expense.date,
        Item=expense.item,
        Amount=expense.amount,
        Description=expense.description,
    )


def map_entity_to_domain_venmo(record: VenmoTable) -> Venmo:
    return Venmo(
        date=record.Date,
        amount=record.Amount,
        description=record.Description,
    )


def map_domain_to_entity_venmo(venmo: Venmo) -> VenmoTable:
    return VenmoTable(
        Date=venmo.date,
        Amount=venmo.amount,
        Description=venmo.description,
    )
