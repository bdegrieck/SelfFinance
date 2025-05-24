from abc import ABC
import pandas as pd


class SourceDataValidator(ABC):
    """
    Base Validation class that all sheets should be validated for before being uploaded into the database
    """

    def __init__(self, data: pd.DataFrame):
        self.data = data
