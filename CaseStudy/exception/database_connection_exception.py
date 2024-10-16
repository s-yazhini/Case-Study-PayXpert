class DatabaseConnectionException(Exception):
    """Exception raised when there is a database connection issue."""
    def __init__(self, message="Failed to connect to the database"):
        super().__init__(message)