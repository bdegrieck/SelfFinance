from abc import ABC
import pandas as pd


class SourceDataValidator(ABC):
    """Base validation class for data sources."""

    def __init__(self, data: pd.DataFrame):
        self.data = data

