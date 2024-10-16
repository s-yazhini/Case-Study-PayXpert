class FinancialRecordException(Exception):
    """Exception raised when there is an issue with financial record operations."""
    def __init__(self, message="Error managing financial records"):
        super().__init__(message)