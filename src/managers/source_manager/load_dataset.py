from pathlib import Path

import pandas as pd

from src.constants import MonthExpenses
from src.exceptions import (
    MissingColumnsSourceDataLoad,
    ExtraColumnsSourceDataLoad,
    InvalidSourceDataType,
)
from src.managers.dataframe_schemas import (
    MetaDataFrame,
    ApartmentSpendingDataFrame,
    CarExpensesDataFrame,
    ClothingDataFrame,
    SubscriptionsDataFrame,
    MiscDataFrame,
    VenmoDataFrame,
    EatingOutDataFrame,
    GiftsDataFrame,
    GroceriesDataFrame,
    IncomeDataFrame,
)
from src.managers.source_manager.entrypoint import create_sourcedata_service

required_sheet_names = {
    "Apartment Spending.csv",
    "Car.csv",
    "Clothing.csv",
    "Eating Out.csv",
    "Gifts.csv",
    "Groceries.csv",
    "Income.csv",
    "Meta.csv",
    "Misc.csv",
    "Sinking Funds.csv",
    "Subscriptions.csv",
    "Venmo.csv",
}


class SourceDataManager:

    def _validate_sheets(self, dataset_path: str):
        """
        Ensure the dataset directory contains exactly the required CSV sheets.

        Args:
            dataset_path (str): Directory that holds the monthly dataset.
        """
        path = Path(dataset_path)
        present = {p.name for p in path.glob("*.csv")}

        # get any missing or extra columns
        missing = required_sheet_names - present
        extra = present - required_sheet_names

        if missing:
            raise MissingColumnsSourceDataLoad.init_with_params(
                missing_columns=list(missing)
            )
        if extra:
            raise ExtraColumnsSourceDataLoad.init_with_params(extra_columns=list(extra))

    def insert_dataset(
        self, dataset_path: str, dataset_month: int, dataset_year: int
    ) -> None:
        """
        Load an Excel workbook and insert its validated contents into the database.

        Args:
            dataset_path (str): Path to the ``.xlsx`` workbook.
            dataset_month (int): Month represented by the dataset.
            dataset_year (int): Year represented by the dataset.
        """
        path = Path(dataset_path)
        dataset_service = create_sourcedata_service()

        # check that the dataset is an excel sheet
        if path.suffix.lower() != ".xlsx":
            raise InvalidSourceDataType.init_with_params(path_name=dataset_path)

        # validate sheet names
        self._validate_sheets(dataset_path=dataset_path)

        # get all of the dataframes
        all_sheets: dict[str, pd.DataFrame] = pd.read_excel(path, sheet_name=None)

        # validate data in the dataframes
        expenses: MonthExpenses = MonthExpenses(
            apartment=ApartmentSpendingDataFrame(all_sheets["Apartment Spending"]),
            car=CarExpensesDataFrame(all_sheets["Car"]),
            clothing=ClothingDataFrame(all_sheets["Clothing"]),
            date=MetaDataFrame(all_sheets["Meta"]),
            eating_out=EatingOutDataFrame(all_sheets["Eating Out"]),
            gifts=GiftsDataFrame(all_sheets["Gifts"]),
            groceries=GroceriesDataFrame(all_sheets["Groceries"]),
            income=IncomeDataFrame(all_sheets["Income"]),
            misc=MiscDataFrame(all_sheets["Misc"]),
            subscription=SubscriptionsDataFrame(all_sheets["Subscriptions"]),
            venmo_df=VenmoDataFrame(all_sheets["Venmo"]),
        )

        # insert data

        # insert apartment
