from src.database.database import (
    GroceriesTable,
    ApartmentSpendingTable,
    CarTable,
    ClothingTable,
    EatingOutTable,
    GiftTable,
    IncomeTable,
    SubscriptionTable,
    VenmoTable,
)
from src.managers.source_manager.domain import (
    ApartmentExpense,
    CarExpense,
    ClothingExpense,
    EatingOutExpense,
    GiftExpense,
    Income,
    SubscriptionExpense,
    Venmo,
    GroceriesExpense,
)


def map_entity_to_domain_apartment_spending(
    apartment_spending_record: ApartmentSpendingTable,
) -> ApartmentExpense:
    return ApartmentExpense(
        date=apartment_spending_record.Date,
        item=apartment_spending_record.Item,
        amount=apartment_spending_record.Amount,
    )


def map_domain_to_entity_apartment_spending(
    apartment_spending: ApartmentExpense,
) -> ApartmentSpendingTable:
    return ApartmentSpendingTable(
        Date=apartment_spending.date,
        Item=apartment_spending.item,
        Amount=apartment_spending.amount,
    )


def map_entity_to_domain_car_expense(car_expense_record: CarTable) -> CarExpense:
    return CarExpense(
        date=car_expense_record.Date,
        item=car_expense_record.Item,
        amount=car_expense_record.Amount,
    )


def map_domain_to_entity_car_expense(car_expense: CarExpense) -> CarTable:
    return CarTable(
        Date=car_expense.date, Item=car_expense.item, Amount=car_expense.amount
    )


def map_entity_to_domain_clothing_expense(
    clothing_expense_record: ClothingTable,
) -> ClothingExpense:
    return ClothingExpense(
        date=clothing_expense_record.Date, amount=clothing_expense_record.Amount
    )


def map_domain_to_entity_clothing_expense(
    clothing_expense: ClothingExpense,
) -> CarTable:
    return ClothingTable(Date=clothing_expense.date, Amount=clothing_expense.amount)


def map_entity_to_domain_eating_out_expense(
    eating_out_expense_record: EatingOutTable,
) -> EatingOutExpense:
    return EatingOutExpense(
        date=eating_out_expense_record.Date,
        place=eating_out_expense_record.Place,
        amount=eating_out_expense_record.Amount,
    )


def map_domain_to_entity_eating_out_expense(
    eating_out_expense: EatingOutExpense,
) -> EatingOutTable:
    return EatingOutTable(
        Date=eating_out_expense.date,
        Place=eating_out_expense.place,
        Amount=eating_out_expense.amount,
    )


def map_entity_to_domain_gift_expense(gift_expense_record: GiftTable) -> GiftExpense:
    return GiftExpense(date=gift_expense_record.Date, amount=gift_expense_record.Amount)


def map_domain_to_entity_gift_expense(gift_expense: GiftExpense) -> GiftTable:
    return GiftTable(Date=gift_expense.date, Amount=gift_expense.amount)


def map_entity_to_domain_groceries(
    groceries_record: GroceriesTable,
) -> GroceriesExpense:
    return GroceriesExpense(
        date=groceries_record.Date,
        amount=groceries_record.Amount,
        description=groceries_record.Description,
    )


def map_domain_to_entity_groceries(groceries: GroceriesExpense) -> GroceriesTable:
    return GroceriesTable(
        Date=groceries.date, Amount=groceries.amount, Description=groceries.description
    )


def map_entity_to_domain_income(income_record: IncomeTable) -> Income:
    return Income(
        date=income_record.date,
        source=income_record.Source,
        gross_pay=income_record.GrossPay,
        taxes=income_record.Taxes,
    )


def map_domain_to_entity_income(income: Income) -> IncomeTable:
    net_pay = Income.gross_pay - Income.taxes
    return CarTable(
        Date=income.date,
        Source=income.source,
        GrossPay=income.gross_pay,
        Taxes=income.taxes,
        NeyPay=net_pay,
    )


def map_entity_to_domain_subscription_expense(
    subscription_record: SubscriptionTable,
) -> SubscriptionExpense:
    return SubscriptionExpense(
        date=subscription_record.Date,
        item=subscription_record.Item,
        amount=subscription_record.Amount,
    )


def map_domain_to_entity_subscription_expense(
    subscription_expense: SubscriptionExpense,
) -> SubscriptionTable:
    return SubscriptionTable(
        Date=subscription_expense.date,
        Item=subscription_expense.item,
        Amount=subscription_expense.amount,
    )


def map_entity_to_domain_venmo(venmo_record: VenmoTable) -> Venmo:
    return Venmo(
        date=venmo_record.Date,
        amount=venmo_record.Amount,
        description=venmo_record.Description,
    )


def map_domain_to_entity_venmo(venmo: Venmo) -> VenmoTable:
    return SubscriptionTable(
        Date=venmo.date, Amount=venmo.amount, Description=venmo.description
    )
