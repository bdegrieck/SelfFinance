class SourceDataException(Exception):

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class MissingColumnsSourceDataLoad(SourceDataException):

    @classmethod
    def init_with_params(cls, missing_columns: list[str]):
        message = f"Failure loading dataset: Missing the following columns: {', '.join(missing_columns)}"
        raise MissingColumnsSourceDataLoad(message=message)


class ExtraColumnsSourceDataLoad(SourceDataException):

    @classmethod
    def init_with_params(cls, extra_columns: list[str]):
        message = f"Failure loading dataset: Extra columns were found: {', '.join(extra_columns)}"
        raise ExtraColumnsSourceDataLoad(message=message)


class InvalidSourceDataType(SourceDataException):

    @classmethod
    def init_with_params(cls, path_name: str):
        message = f"The path name: {path_name} is not a valid excel sheet. Must be an .xlsx file"
        raise InvalidSourceDataType(message=message)
