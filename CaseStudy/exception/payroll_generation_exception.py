class PayrollGenerationException(Exception):
    """Exception raised when there is an issue with payroll generation."""
    def __init__(self, message="Error generating payroll"):
        super().__init__(message)