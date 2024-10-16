class TaxCalculationException(Exception):
    """Exception raised when there is an error in tax calculation."""
    def __init__(self, message="Error calculating taxes"):
        super().__init__(message)