-- Create the database if not exists

CREATE DATABASE EmployeeManagementDB;

USE EmployeeManagementDB;

-- Employee Table
CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY IDENTITY(1,1),
    FirstName NVARCHAR(50),
    LastName NVARCHAR(50),
    DateOfBirth DATE,
    Gender NVARCHAR(10),
    Email NVARCHAR(100),
    PhoneNumber NVARCHAR(15),
    Address NVARCHAR(255),
    Position NVARCHAR(100),
    Salary DECIMAL(10, 2),  -- Added Salary column
    JoiningDate DATE,
    TerminationDate DATE NULL
);

CREATE TABLE Payroll (
    PayrollID INT PRIMARY KEY IDENTITY(1,1),
    EmployeeID INT FOREIGN KEY REFERENCES Employee(EmployeeID),
    PayPeriodStartDate DATE,
    PayPeriodEndDate DATE,
    BasicSalary DECIMAL(10, 2),
    OvertimePay DECIMAL(10, 2),
    Deductions DECIMAL(10, 2),
    NetSalary DECIMAL(10, 2)
);

CREATE TABLE Tax (
    TaxID INT PRIMARY KEY IDENTITY(1,1),
    EmployeeID INT FOREIGN KEY REFERENCES Employee(EmployeeID),
    TaxYear INT,
    TaxableIncome DECIMAL(10, 2),
    TaxAmount DECIMAL(10, 2)
);

CREATE TABLE FinancialRecord (
    RecordID INT PRIMARY KEY IDENTITY(1,1),
    EmployeeID INT FOREIGN KEY REFERENCES Employee(EmployeeID),
    RecordDate DATE,
    Description NVARCHAR(255),
    Amount DECIMAL(10, 2),
    RecordType NVARCHAR(50)
);

-- Insert sample data into Employee table
INSERT INTO Employee (FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, Address, Position, Salary, JoiningDate, TerminationDate)
VALUES 
('Sashank', 'Reddy', '1990-04-15', 'Male', 'sashankreddy@example.com', '1234567890', '123 Main St, Cityville', 'Software Engineer', 60000.00, '2020-01-15', NULL),
('Lahari', 'Podutur', '1985-11-23', 'Female', 'poduturlahari@example.com', '0987654321', '456 Maple Ave, Townville', 'HR Manager', 75000.00, '2019-05-01', NULL),
('Akarsh', 'Kumar', '1992-07-08', 'Male', 'kumarakarsh@example.com', '5555555555', '789 Oak St, Villagetown', 'Accountant', 50000.00, '2021-06-21', NULL),
('Yazhini', 'Sakthivel', '1995-09-12', 'Female', 'yazhinisakthivel@example.com', '4444444444', '321 Pine Rd, Hamletcity', 'Marketing Executive', 55000.00, '2022-03-01', NULL),
('Rakesh', 'Niha', '1988-02-20', 'Male', 'rakeshniha@example.com', '3333333333', '654 Birch Blvd, Countryside', 'Project Manager', 90000.00, '2018-11-30', NULL);

-- Insert sample data into Payroll table
INSERT INTO Payroll (EmployeeID, PayPeriodStartDate, PayPeriodEndDate, BasicSalary, OvertimePay, Deductions, NetSalary)
VALUES 
(2, '2024-09-01', '2024-09-30', 60000.00, 500.00, 100.00, 60400.00),
(3, '2024-09-01', '2024-09-30', 75000.00, 700.00, 150.00, 75550.00),
(4, '2024-09-01', '2024-09-30', 50000.00, 400.00, 80.00, 50320.00),
(5, '2024-09-01', '2024-09-30', 55000.00, 450.00, 90.00, 55360.00),
(6, '2024-09-01', '2024-09-30', 90000.00, 800.00, 200.00, 90600.00);

-- Insert sample data into Tax table
INSERT INTO Tax (EmployeeID, TaxYear, TaxableIncome, TaxAmount)
VALUES 
(2, 2023, 720000.00, 144000.00),
(3, 2023, 900000.00, 180000.00),
(4, 2023, 600000.00, 120000.00),
(5, 2023, 660000.00, 132000.00),
(6, 2023, 1080000.00, 216000.00);

-- Insert sample data into FinancialRecord table
INSERT INTO FinancialRecord (EmployeeID, RecordDate, Description, Amount, RecordType)
VALUES 
(2, '2024-09-15', 'Bonus for performance', 1000.00, 'Credit'),
(3, '2024-08-25', 'Medical Reimbursement', 500.00, 'Credit'),
(4, '2024-07-10', 'Salary Advance', 2000.00, 'Debit'),
(5, '2024-09-01', 'Travel Allowance', 700.00, 'Credit'),
(6, '2024-06-20', 'Training Fee Deduction', 300.00, 'Debit');

-- Query to verify the inserted data
SELECT * FROM Employee;
SELECT * FROM Payroll;
SELECT * FROM Tax;
SELECT * FROM FinancialRecord;

-- Verify the EmployeeID values in Employee table
SELECT EmployeeID, FirstName, LastName FROM Employee;

drop table Tax;
