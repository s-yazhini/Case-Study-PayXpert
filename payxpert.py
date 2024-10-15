#------------------YSTART----------------

from datetime import date

class Employee:
    def __init__(self, employee_id=None, first_name=None, last_name=None, date_of_birth=None, gender=None,
                 email=None, phone_number=None, address=None, position=None, joining_date=None, termination_date=None):
        self.__employee_id = employee_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__date_of_birth = date_of_birth
        self.__gender = gender
        self.__email = email
        self.__phone_number = phone_number
        self.__address = address
        self.__position = position
        self.__joining_date = joining_date
        self.__termination_date = termination_date

    # Getters and setters
    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self):
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_date_of_birth(self):
        return self.__date_of_birth

    def set_date_of_birth(self, date_of_birth):
        self.__date_of_birth = date_of_birth

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_phone_number(self):
        return self.__phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    def get_position(self):
        return self.__position

    def set_position(self, position):
        self.__position = position

    def get_joining_date(self):
        return self.__joining_date

    def set_joining_date(self, joining_date):
        self.__joining_date = joining_date

    def get_termination_date(self):
        return self.__termination_date

    def set_termination_date(self, termination_date):
        self.__termination_date = termination_date

    # Method to calculate age
    def calculate_age(self):
        today = date.today()
        age = today.year - self.__date_of_birth.year - \
              ((today.month, today.day) < (self.__date_of_birth.month, self.__date_of_birth.day))
        return age



class Payroll:
    def __init__(self, payroll_id=None, employee_id=None, pay_period_start_date=None, pay_period_end_date=None,
                 basic_salary=None, overtime_pay=None, deductions=None, net_salary=None):
        self.__payroll_id = payroll_id
        self.__employee_id = employee_id
        self.__pay_period_start_date = pay_period_start_date
        self.__pay_period_end_date = pay_period_end_date
        self.__basic_salary = basic_salary
        self.__overtime_pay = overtime_pay
        self.__deductions = deductions
        self.__net_salary = net_salary

    # Getters and setters
    def get_payroll_id(self):
        return self.__payroll_id

    def set_payroll_id(self, payroll_id):
        self.__payroll_id = payroll_id

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_pay_period_start_date(self):
        return self.__pay_period_start_date

    def set_pay_period_start_date(self, pay_period_start_date):
        self.__pay_period_start_date = pay_period_start_date

    def get_pay_period_end_date(self):
        return self.__pay_period_end_date

    def set_pay_period_end_date(self, pay_period_end_date):
        self.__pay_period_end_date = pay_period_end_date

    def get_basic_salary(self):
        return self.__basic_salary

    def set_basic_salary(self, basic_salary):
        self.__basic_salary = basic_salary

    def get_overtime_pay(self):
        return self.__overtime_pay

    def set_overtime_pay(self, overtime_pay):
        self.__overtime_pay = overtime_pay

    def get_deductions(self):
        return self.__deductions

    def set_deductions(self, deductions):
        self.__deductions = deductions

    def get_net_salary(self):
        return self.__net_salary

    def set_net_salary(self, net_salary):
        self.__net_salary = net_salary



class Tax:
    def __init__(self, tax_id=None, employee_id=None, tax_year=None, taxable_income=None, tax_amount=None):
        self.__tax_id = tax_id
        self.__employee_id = employee_id
        self.__tax_year = tax_year
        self.__taxable_income = taxable_income
        self.__tax_amount = tax_amount

    # Getters and setters
    def get_tax_id(self):
        return self.__tax_id

    def set_tax_id(self, tax_id):
        self.__tax_id = tax_id

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_tax_year(self):
        return self.__tax_year

    def set_tax_year(self, tax_year):
        self.__tax_year = tax_year

    def get_taxable_income(self):
        return self.__taxable_income

    def set_taxable_income(self, taxable_income):
        self.__taxable_income = taxable_income

    def get_tax_amount(self):
        return self.__tax_amount

    def set_tax_amount(self, tax_amount):
        self.__tax_amount = tax_amount


class FinancialRecord:
    def __init__(self, record_id=None, employee_id=None, record_date=None, description=None, amount=None, record_type=None):
        self.__record_id = record_id
        self.__employee_id = employee_id
        self.__record_date = record_date
        self.__description = description
        self.__amount = amount
        self.__record_type = record_type

    # Getters and setters
    def get_record_id(self):
        return self.__record_id

    def set_record_id(self, record_id):
        self.__record_id = record_id

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_record_date(self):
        return self.__record_date

    def set_record_date(self, record_date):
        self.__record_date = record_date

    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    def get_amount(self):
        return self.__amount

    def set_amount(self, amount):
        self.__amount = amount

    def get_record_type(self):
        return self.__record_type

    def set_record_type(self, record_type):
        self.__record_type = record_type


from abc import ABC, abstractmethod

class IEmployeeService(ABC):
    @abstractmethod
    def get_employee_by_id(self, employee_id):
        pass

    @abstractmethod
    def get_all_employees(self):
        pass

    @abstractmethod
    def add_employee(self, employee):
        pass

    @abstractmethod
    def update_employee(self, employee):
        pass

    @abstractmethod
    def remove_employee(self, employee_id):
        pass


class IPayrollService(ABC):
    @abstractmethod
    def generate_payroll(self, employee_id, pay_period_start_date, pay_period_end_date):
        pass

    @abstractmethod
    def get_payroll_by_id(self, payroll_id):
        pass

    @abstractmethod
    def get_payrolls_for_employee(self, employee_id):
        pass

    @abstractmethod
    def get_payrolls_for_period(self, pay_period_start_date, pay_period_end_date):
        pass


class ITaxService(ABC):
    @abstractmethod
    def calculate_tax(self, employee_id, taxable_income):
        pass

    @abstractmethod
    def get_tax_by_id(self, tax_id):
        pass

    @abstractmethod
    def get_taxes_for_employee(self, employee_id):
        pass

    @abstractmethod
    def get_taxes_for_year(self, tax_year):
        pass


class IFinancialRecordService(ABC):
    @abstractmethod
    def add_financial_record(self, financial_record):
        pass

    @abstractmethod
    def get_financial_record_by_id(self, record_id):
        pass

    @abstractmethod
    def get_financial_records_for_employee(self, employee_id):
        pass

    @abstractmethod
    def get_financial_records_for_date(self, record_date):
        pass

#-------------------YSEND-------------------------