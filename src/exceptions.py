class SourceDataException(Exception):

    def __init__(self, message: str):
        """
        Initialize the base source data exception.

        Args:
            message (str): Explanation of the error.
        """
        self.message = message
        super().__init__(message)


class MissingColumnsSourceDataLoad(SourceDataException):

    @classmethod
    def init_with_params(cls, missing_columns: list[str]):
        """
        Raise an exception indicating which columns are missing from the dataset.

        Args:
            missing_columns (list[str]): Column names that were not found.
        """
        message = f"Failure loading dataset: Missing the following columns: {', '.join(missing_columns)}"
        raise MissingColumnsSourceDataLoad(message=message)


class ExtraColumnsSourceDataLoad(SourceDataException):

    @classmethod
    def init_with_params(cls, extra_columns: list[str]):
        """
        Raise an exception when unexpected columns are present in the dataset.

        Args:
            extra_columns (list[str]): Column names that should not be present.
        """
        message = f"Failure loading dataset: Extra columns were found: {', '.join(extra_columns)}"
        raise ExtraColumnsSourceDataLoad(message=message)


class InvalidSourceDataType(SourceDataException):

    @classmethod
    def init_with_params(cls, path_name: str):
        """
        Raise an exception for an invalid dataset type.

        Args:
            path_name (str): Path that did not point to an ``.xlsx`` file.
        """
        message = f"The path name: {path_name} is not a valid excel sheet. Must be an .xlsx file"
        raise InvalidSourceDataType(message=message)
