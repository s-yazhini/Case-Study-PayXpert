class EmployeeNotFoundException(Exception):
    """Exception raised when an employee is not found in the database."""
    def __init__(self, employee_id):
        super().__init__(f"Employee with ID {employee_id} not found.")