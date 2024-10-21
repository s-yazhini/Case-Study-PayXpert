import sys
import pyodbc
from dao.EmployeeServiceImpl import EmployeeServiceImpl
from dao.PayrollServiceImpl import PayrollServiceImpl
from dao.ReportGenerator import ReportGenerator
from dao.TaxServiceImpl import TaxServiceImpl
from dao.FinancialRecordServiceImpl import FinancialRecordServiceImpl
from entity.Employee import Employee
from entity.Payroll import Payroll
from exception import FinancialRecordException
from util.DBConnUtil import DBConnUtil
from util.DBPropertyUtil import DBPropertyUtil
from exception.EmployeeNotFoundException import EmployeeNotFoundException
from exception.PayrollGenerationException import PayrollGenerationException
from exception.TaxCalculationException import TaxCalculationException
from exception.InvalidInputException import InvalidInputException


class MainModule:
    def __init__(self):
        
        self.conn = None
        self.employee_service = None
        self.payroll_service = None
        self.tax_service = None
        self.financial_service = None
        self.report_generator = None
        self.initialize_services()

    def initialize_services(self):
        try:
            self.conn = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};SERVER=localhost\\SQLEXPRESS;Database=EmployeeManagementDB;Trusted_Connection=yes;'
            )
            print("Database connection successful.")
        except pyodbc.Error as e:
            print(f"Error connecting to the database: {e}")
            sys.exit(1)

        # Initialize services with the connection
        self.employee_service = EmployeeServiceImpl(self.conn)
        self.payroll_service = PayrollServiceImpl(self.conn)
        self.tax_service = TaxServiceImpl(self.conn)
        self.financial_service = FinancialRecordServiceImpl(self.conn)

        # Report generator service
        self.report_generator = ReportGenerator(
            self.payroll_service, self.tax_service, self.financial_service
        )

    def main_menu(self):
        print("\nEmployee Management System")
        print("1. Manage Employees")
        print("2. Process Payroll")
        print("3. Calculate Tax")
        print("4. Financial Reporting")
        print("5. Generate Report")
        print("6. Exit")


    def employee_menu(self):
        print("\nEmployee Management")
        print("1. Add Employee")
        print("2. Update Employee")
        print("3. Remove Employee")
        print("4. View Employee by ID")
        print("5. View All Employees")
        print("6. Back to Main Menu")


    def payroll_menu(self):
        print("Payroll Processing")
        print("1. Generate Payroll")
        print("2. View Payroll by ID")
        print("3. View Payrolls for Employee")
        print("4. View Payrolls for Pay Period")
        print("5. Delete Payroll by Employee ID")
        print("6. Update Payroll")  
        print("7. Back to Main Menu")

    def tax_menu(self):
        print("\nTax Calculation")
        print("1. Calculate Tax for Employee")
        print("2. View Tax Record by ID")
        print("3. View Taxes for Employee")
        print("4. View Taxes for Year")
        print("5. Delete Tax Record by employeeid")
        print("6. Back TO Main Menu")


    def financial_report_menu(self):
        print("\nFinancial Reporting")
        print("1. View Financial Records for Employee")
        print("2. View financial records for date")
        print("3. View Financial Record By ID")
        print("4. add financial record")
        print("5. Delete financial record")
        print("6. Back to Main Menu")

    def report_menu(self):
        print("\nReport Generation")
        print("1. Generate Payroll Report for a Period")
        print("2. Generate Tax Report for a Year")
        print("3.Generate Financial Report for an Employee")
        print("4. View Report For An Employee")
        print("5. Back to Main Menu")

    def handle_main_menu(self):
        while True:
            self.main_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                while True:               
                    self.employee_menu()
                    emp_choice = input("Enter your choice: ")

                    if emp_choice == "1":
                        try:
                            employee_data = {
                                'FirstName': input("Enter First Name: "),
                                'LastName': input("Enter Last Name: "),
                                'DateOfBirth': input("Enter Date of Birth (YYYY-MM-DD): "),
                                'Gender': input("Enter Gender: "),
                                'Email': input("Enter Email: "),
                                'PhoneNumber': input("Enter Phone Number: "),
                                'Address': input("Enter Address: "),
                                'Position': input("Enter Position: "),
                                'Salary': float(input("Enter Salary: ")),  # Convert to float
                                'JoiningDate': input("Enter Joining Date (YYYY-MM-DD): "),
                                'TerminationDate': input("Enter Termination Date (YYYY-MM-DD) [optional]: ") or None
                            }

                            # Convert the dictionary to an Employee object
                            employee = Employee(
                                first_name=employee_data['FirstName'],
                                last_name=employee_data['LastName'],
                                dob=employee_data['DateOfBirth'],
                                gender=employee_data['Gender'],
                                email=employee_data['Email'],
                                phone=employee_data['PhoneNumber'],
                                address=employee_data['Address'],
                                position=employee_data['Position'],
                                salary=employee_data['Salary'],
                                joining_date=employee_data['JoiningDate'],
                                termination_date=employee_data['TerminationDate']
                            )

                            # Add the employee to the database
                            self.employee_service.add_employee(employee)

                        except Exception as e:
                            print(f"An error occurred: {e}")

                    elif emp_choice == "2":
                        try:
                            emp_id = input("Enter Employee ID to update: ")

                            # Fetch the current employee details to modify them
                            employee = self.employee_service.get_employee_by_id(emp_id)

                            if employee is None:
                                raise EmployeeNotFoundException(f"Employee with ID {emp_id} not found.")

                            # Gather updated employee information from the user
                            updated_data = {
                                'first_name': input(f"Enter First Name [{employee.first_name}]: ") or employee.first_name,
                                'last_name': input(f"Enter Last Name [{employee.last_name}]: ") or employee.last_name,
                                'dob': input(f"Enter Date of Birth (YYYY-MM-DD) [{employee.dob}]: ") or employee.dob,
                                'gender': input(f"Enter Gender [{employee.gender}]: ") or employee.gender,
                                'email': input(f"Enter Email [{employee.email}]: ") or employee.email,
                                'phone': input(f"Enter Phone Number [{employee.phone}]: ") or employee.phone,
                                'address': input(f"Enter Address [{employee.address}]: ") or employee.address,
                                'position': input(f"Enter Position [{employee.position}]: ") or employee.position,
                                'salary': float(input(f"Enter Salary [{employee.salary}]: ") or employee.salary),
                                'joining_date': input(
                                    f"Enter Joining Date (YYYY-MM-DD) [{employee.joining_date}]: ") or employee.joining_date,
                                'termination_date': input(
                                    f"Enter Termination Date (YYYY-MM-DD) [{employee.termination_date or 'N/A'}]: ") or employee.termination_date
                            }

                            # Convert the dictionary to an Employee object
                            updated_employee = Employee(
                                employee_id=employee.employee_id,
                                first_name=updated_data['first_name'],
                                last_name=updated_data['last_name'],
                                dob=updated_data['dob'],
                                gender=updated_data['gender'],
                                email=updated_data['email'],
                                phone=updated_data['phone'],
                                address=updated_data['address'],
                                position=updated_data['position'],
                                salary=updated_data['salary'],
                                joining_date=updated_data['joining_date'],
                                termination_date=updated_data['termination_date']
                            )

                            # Update employee details
                            self.employee_service.update_employee(updated_employee)
                            print("Employee updated successfully!")

                        except EmployeeNotFoundException as e:
                            print(f"Error: {e}")
                        except Exception as e:
                            print(f"An unexpected error occurred: {e}")


                    elif emp_choice == "3":
                        try:
                            emp_id = input("Enter Employee ID to remove: ")
                            self.employee_service.remove_employee(emp_id)
                        except EmployeeNotFoundException as e:
                            print(f"Error: {e}")

                    elif emp_choice == "4":
                        try:
                            emp_id = input("Enter Employee ID: ")
                            employee = self.employee_service.get_employee_by_id(emp_id)
                            print(employee)  # Will now display correct employee details
                        except EmployeeNotFoundException as e:
                            print(f"Error: {e}")


                    elif emp_choice == "5":
                        employees = self.employee_service.get_all_employees()
                        for emp in employees:
                            print(emp)  # This will now print the correct details thanks to the __str__ method


                    elif emp_choice == "6":
                        break


            elif choice == "2":
                while True:
                    print('\n')
                    self.payroll_menu()
                    payroll_choice = input("Enter your choice: ")

                    if payroll_choice == "1":
                        try:
                            emp_id = input("Enter Employee ID: ")
                            start_date = input("Enter Pay Period Start Date (YYYY-MM-DD): ")
                            end_date = input("Enter Pay Period End Date (YYYY-MM-DD): ")

                            # Take Basic Salary, Overtime Pay, and Deductions from user input
                            basic_salary = float(input("Enter Basic Salary: "))
                            overtime_pay = float(input("Enter Overtime Pay: "))
                            deductions = float(input("Enter Deductions: "))

                            # Generate payroll using the collected information
                            self.payroll_service.generate_payroll(emp_id, start_date, end_date, basic_salary, overtime_pay,
                                                            deductions)
                            print("Payroll generated successfully!")
                        except PayrollGenerationException as e:
                            print(f"Error: {e}")

                    elif payroll_choice == "2":
                        payroll_id = input("Enter Payroll ID: ")
                        try:
                            payroll = self.payroll_service.get_payroll_by_id(payroll_id)
                            print(payroll.display_payroll_info())  # Use display method to show payroll info
                        except PayrollGenerationException as e:
                            print(f"Error: {e}")

                    elif payroll_choice == "3":
                        emp_id = input("Enter Employee ID: ")
                        try:
                            payrolls = self.payroll_service.get_payrolls_for_employee(emp_id)
                            if payrolls:
                                for payroll in payrolls:
                                    print(payroll.display_payroll_info())  # Display payroll info using the method
                            else:
                                print(f"No payroll records found for Employee ID: {emp_id}")
                        except PayrollGenerationException as e:
                            print(f"Error: {e}")

                    elif payroll_choice == "4":
                        start_date = input("Enter Start Date (YYYY-MM-DD): ")
                        end_date = input("Enter End Date (YYYY-MM-DD): ")
                        try:
                            payrolls = self.payroll_service.get_payrolls_for_period(start_date, end_date)
                            if payrolls:
                                for payroll in payrolls:
                                    print(payroll.display_payroll_info())  # Display payroll info using the method
                            else:
                                print(f"No payroll records found for the given period: {start_date} to {end_date}")
                        except PayrollGenerationException as e:
                            print(f"Error: {e}")


                    elif payroll_choice == "5":
                        emp_id = input("Enter Employee ID to delete payroll: ")
                        try:
                            self.payroll_service.delete_payroll_by_employee_id(emp_id)
                            print(f"Payroll records for Employee ID {emp_id} deleted successfully!")
                        except PayrollGenerationException as e:
                            print(f"Error: {e}")


                    elif payroll_choice == "6":
                        try:
                            payroll_id = input("Enter Payroll ID to update: ")

                            # Get the updated details from the user
                            new_basic_salary = float(input("Enter new Basic Salary: "))
                            new_overtime_pay = float(input("Enter new Overtime Pay: "))
                            new_deductions = float(input("Enter new Deductions: "))

                            # Update the payroll record using the payroll service
                            self.payroll_service.update_payroll(payroll_id, new_basic_salary, new_overtime_pay, new_deductions)

                            print(f"Payroll ID {payroll_id} updated successfully!")
                        except PayrollGenerationException as e:
                            print(f"Error: {e}")
                        except ValueError:
                            print("Invalid input! Please enter numeric values for salary, overtime, and deductions.")


                    elif payroll_choice == "7":
                        break


            elif choice == "3":
                while True:
                    self.tax_menu()
                    tax_choice = input("Enter your choice: ")

                    if tax_choice == "1":
                        try:
                            emp_id = int(input("Enter Employee ID: "))  # Convert to int
                            tax_year = int(input("Enter Tax Year: "))  # Convert to int
                            tax = self.tax_service.calculate_tax(emp_id, tax_year)  # Store the returned Tax object
                            print("Tax calculated successfully!")
                            print(tax.display_tax_info())  # Display the calculated tax information

                        except TaxCalculationException as e:
                            print(f"Error: {e}")
                        except ValueError:
                            print("Invalid input! Please enter numeric values.")

                    elif tax_choice == "2":
                        try:
                            tax_id = int(input("Enter Tax ID: "))  # Convert to int
                            tax_record = self.tax_service.get_tax_by_id(tax_id)
                            print(tax_record.display_tax_info())  # Display tax info, including Tax ID

                        except TaxCalculationException as e:
                            print(f"Error: {e}")
                        except ValueError:
                            print("Invalid input! Please enter a numeric value.")

                    elif tax_choice == "3":
                        try:
                            emp_id = int(input("Enter Employee ID: "))  # Convert to int
                            taxes = self.tax_service.get_taxes_for_employee(emp_id)
                            if taxes:
                                for tax in taxes:
                                    print(tax.display_tax_info())  # Display each tax record with Tax ID
                            else:
                                print(f"No tax records found for Employee ID {emp_id}.")

                        except ValueError:
                            print("Invalid input! Please enter a numeric value.")

                    elif tax_choice == "4":
                        try:
                            tax_year = int(input("Enter Tax Year: "))  # Convert to int
                            taxes = self.tax_service.get_taxes_for_year(tax_year)
                            if taxes:
                                for tax in taxes:
                                    print(tax.display_tax_info())  # Display each tax record with Tax ID
                            else:
                                print(f"No tax records found for Tax Year {tax_year}.")

                        except ValueError:
                            print("Invalid input! Please enter a numeric value.")

                    elif tax_choice == "5":
                        try:
                            emp_id = int(input("Enter Employee ID: "))  # Convert to int
                            self.tax_service.delete_tax_by_employee_id(emp_id)
                            print(f"Tax record(s) for Employee ID {emp_id} successfully deleted.")

                        except TaxCalculationException as e:
                            print(f"Error: {e}")
                        except ValueError:
                            print("Invalid input! Please enter a numeric value.")

                    elif tax_choice == "6":
                        break  # Exit to main menu

                    else:
                        print("Invalid choice! Please select a valid option.")


            elif choice == "4":
                while True:
                    self.financial_report_menu()
                    report_choice = input("Enter your choice: ")

                    if report_choice == "1":
                        emp_id = input("Enter Employee ID: ")
                        financial_records = self.financial_service.get_financial_records_for_employee(emp_id)
                        for record in financial_records:
                            print(record)

                    elif report_choice == "2":
                        record_date = input("Enter Record Date (YYYY-MM-DD): ")
                        financial_records = self.financial_service.get_financial_records_for_date(record_date)
                        for record in financial_records:
                            print(record)

                    elif report_choice == "3":
                        record_id = input("Enter Record ID: ")
                        try:
                            record = self.financial_service.get_financial_record_by_id(record_id)
                            print(record)
                        except FinancialRecordException as e:
                            print(f"Error: {e}")

                    elif report_choice == "4":
                        emp_id = input("Enter Employee ID: ")
                        description = input("Enter Description: ")
                        amount = input("Enter Amount: ")
                        record_type = input("Enter Record Type: ")
                        record_date = input("Enter Record Date (YYYY-MM-DD): ")
                        self.financial_service.add_financial_record(emp_id, description, amount, record_type, record_date)
                        print("Financial record added successfully!")

                    elif report_choice == "5":
                        emp_id = input("Enter Employee ID: ")
                        try:
                            self.financial_service.delete_financial_records_by_employee_id(emp_id)
                            print(f"Financial records for Employee ID {emp_id} have been successfully deleted.")
                        except FinancialRecordException as e:
                            print(f"Error: {e}")

                    elif report_choice == "6":
                        break  # Exit to main menu


            elif choice == "5":
                while True:
                    self.report_menu()
                    report_choice = input("Enter your choice: ")

                    if report_choice == "1":
                        # Generate Payroll Report
                        start_date = input("Enter Start Date (YYYY-MM-DD): ")
                        end_date = input("Enter End Date (YYYY-MM-DD): ")
                        self.report_generator.generate_payroll_report(start_date, end_date)

                    elif report_choice == "2":
                        # Generate Tax Report
                        tax_year = int(input("Enter Tax Year: "))  # Convert to int
                        self.report_generator.generate_tax_report(tax_year)

                    elif report_choice == "3":
                        # Generate Financial Report
                        emp_id = input("Enter Employee ID: ")
                        self.report_generator.generate_financial_report(emp_id)

                    elif report_choice == "4":  # View Report For An Employee
                        try:
                            emp_id = int(input("Enter Employee ID: "))  # Convert to int

                            # Fetch records
                            try:
                                payroll_records = self.payroll_service.get_payrolls_for_employee(emp_id)
                                print("Fetched Payroll Records:", payroll_records)  # Debugging line
                            except Exception as e:
                                print(f"Error fetching payroll records: {e}")

                            try:
                                tax_records = self.tax_service.get_taxes_for_employee(emp_id)
                                print("Fetched Tax Records:", tax_records)  # Debugging line
                            except Exception as e:
                                print(f"Error fetching tax records: {e}")

                            try:
                                financial_records = self.financial_service.get_financial_records_for_employee(emp_id)
                                print("Fetched Financial Records:", financial_records)  # Debugging line
                            except Exception as e:
                                print(f"Error fetching financial records: {e}")

                            print("Payroll Records:")
                            if payroll_records:
                                for payroll in payroll_records:
                                    print(payroll.display_payroll_info())  # Call display method for payroll
                            else:
                                print("No payroll records found for this employee.")

                            print("\nTax Records:")
                            if tax_records:
                                for tax in tax_records:
                                    print(tax.display_tax_info())  # Display each Tax record
                            else:
                                print("No tax records found for this employee.")

                            print("\nFinancial Records:")
                            if financial_records:
                                for record in financial_records:
                                    print(record)  # This will automatically call the __str__ method
                            else:
                                print("No financial records found for this employee.")

                        except ValueError:
                            print("Invalid input! Please enter a numeric Employee ID.")

                    elif report_choice == "5":
                        break  # Exit to main menu


            elif choice == "6":
                print("Exiting the system.")
                sys.exit(0)


            else:
                print("Invalid choice, please try again.")
                

if __name__ == "__main__":
    main_module = MainModule()
    main_module.handle_main_menu()