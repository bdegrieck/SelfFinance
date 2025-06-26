import pandas as pd

from src.managers.dataframe_schemas import MetaDataFrame
from src.managers.source_manager.entrypoint import create_sourcedata_service
from src.managers.source_manager.service import SourceDataService



def insert_expenses(expense_sheets: list[str], source_data_service: SourceDataService):
    """
    Read a collection of CSV files and send their contents to the service for insertion.

    Args:
        expense_sheets (list[str]): Paths to the expense CSV files.
        source_data_service (SourceDataService): Service used to persist the data.
    """

    for expense_sheet in expense_sheets:
        df = pd.read_csv(expense_sheet)
        print(df)

    # insert groceries
    source_data_service.insert_groceries()


if __name__ == "__main__":
    source_data_service = create_sourcedata_service()
    month_directories = [
        "/Users/bende/SelfFinance/datasources/Janurary.xlsx",
        "/Users/bende/SelfFinance/datasources/Feburary",
        "/Users/bende/SelfFinance/datasources/March",
        "/Users/bende/SelfFinance/datasources/April",
    ]
    for month in month_directories:
        all_sheets: dict[str, pd.DataFrame] = pd.read_excel(month, sheet_name=None)
        all_sheets["Meta"] = pd.DataFrame({"Month": ["12"], "Year": ["2025"]})
        date_df = MetaDataFrame(all_sheets["Meta"])
        print(all_sheets)
