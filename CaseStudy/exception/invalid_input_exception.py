class InvalidInputException(Exception):
    """Exception raised when invalid input data is provided."""
    def __init__(self, message="Invalid input provided"):
        super().__init__(message)