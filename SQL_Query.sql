CREATE TABLE Employee (
    EmployeeID INT PRIMARY KEY IDENTITY(1,1),
    FirstName VARCHAR(50) NOT NULL,
    LastName VARCHAR(50) NOT NULL,
    DateOfBirth DATE NOT NULL,
    Gender VARCHAR(10) NOT NULL,
    Email VARCHAR(100) UNIQUE NOT NULL,
    PhoneNumber VARCHAR(15) UNIQUE NOT NULL,
    Address TEXT NOT NULL,
    Position VARCHAR(50) NOT NULL,
    JoiningDate DATE NOT NULL,
    TerminationDate DATE
);

CREATE TABLE Payroll (
    PayrollID INT PRIMARY KEY IDENTITY(1,1),
    EmployeeID INT,
    PayPeriodStartDate DATE NOT NULL,
    PayPeriodEndDate DATE NOT NULL,
    BasicSalary DECIMAL(10, 2) NOT NULL,
    OvertimePay DECIMAL(10, 2) NOT NULL,
    Deductions DECIMAL(10, 2) NOT NULL,
    NetSalary DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID) ON DELETE CASCADE
);

CREATE TABLE Tax (
    TaxID INT PRIMARY KEY IDENTITY(1,1),
    EmployeeID INT,
    TaxYear INT NOT NULL,
    TaxableIncome DECIMAL(12, 2) NOT NULL,
    TaxAmount DECIMAL(12, 2) NOT NULL,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID) ON DELETE CASCADE
);

CREATE TABLE FinancialRecord (
    RecordID INT PRIMARY KEY IDENTITY(1,1),
    EmployeeID INT,
    RecordDate DATE NOT NULL,
    Description TEXT NOT NULL,
    Amount DECIMAL(12, 2) NOT NULL,
    RecordType VARCHAR(20) NOT NULL,
    FOREIGN KEY (EmployeeID) REFERENCES Employee(EmployeeID) ON DELETE CASCADE
);

INSERT INTO Employee (FirstName, LastName, DateOfBirth, Gender, Email, PhoneNumber, Address, Position, JoiningDate)
VALUES 
('Lahari', 'Reddy', '1990-05-15', 'Female', 'laharireddy@email.com', '9586863257', 'Pedha steert, Tirupati', 'Manager', '2020-01-10'),
('Yazhini', 'S', '1993-04-21', 'Female', 'yazhiniS@email.com', '8012030000', 'St, Salem', 'Executive', '2023-09-12'),
('Akarsh', 'Kumar', '1985-08-20', 'Male', 'akarshkumar@email.com', '9521478632', 'Avenue, Patna', 'HR', '2019-03-12'),
('Sashank', 'Sun', '1992-11-25', 'Male', 'sashanksun@email.com', '8456321789', 'Road, nagar', 'Engineer', '2021-06-15'),
('Kavitha', 'kumari', '1995-03-30', 'Female', 'kavithakumari@email.com', '7214563897', 'Marina, Beach', 'Designer', '2022-02-20'),
('Para', 'Yeva', '1988-09-10', 'Male', 'parayeva@email.com', '9514782655', 'Lane, Nagar', 'Accountant', '2021-04-05'),
('Hanvith', 'tinku', '1990-12-14', 'Male', 'hanvithtin@email.com', '7412589632', 'Street, Nows', 'Marketing', '2023-07-10'),
('Hanvika', 'dolly', '1987-06-17', 'Female', 'hanvikadol@email.com', '8523697410', 'Ave, Bihar', 'Developer', '2020-11-21'),
('Sadaf', 'Shaik', '1989-07-05', 'Female', 'sadafshaik@email.com', '7895201460', 'Blvd, Gwalior', 'Admin', '2022-01-15'),
('Ragini', 'Swift', '1994-02-09', 'Female', 'raginithu@email.com', '4520630120', 'Street, Himachal', 'Research', '2021-03-10');

-- Insert values into the Payroll table
INSERT INTO Payroll (EmployeeID, PayPeriodStartDate, PayPeriodEndDate, BasicSalary, OvertimePay, Deductions, NetSalary)
VALUES 
(1, '2024-01-01', '2024-01-31', 60000, 3000, 500, 62500),
(2, '2024-01-01', '2024-01-31', 50000, 2000, 700, 51300),
(3, '2024-01-01', '2024-01-31', 55000, 2500, 800, 56700),
(4, '2024-01-01', '2024-01-31', 45000, 1500, 300, 46200),
(5, '2024-01-01', '2024-01-31', 52000, 1800, 600, 53200),
(6, '2024-01-01', '2024-01-31', 47000, 2000, 700, 48300),
(7, '2024-01-01', '2024-01-31', 68000, 3500, 1200, 70300),
(8, '2024-01-01', '2024-01-31', 40000, 1000, 200, 40800),
(9, '2024-01-01', '2024-01-31', 48000, 2000, 600, 49400),
(10, '2024-01-01', '2024-01-31', 53000, 2500, 900, 54600);

-- Insert values into the Tax table
INSERT INTO Tax (EmployeeID, TaxYear, TaxableIncome, TaxAmount)
VALUES 
(1, 2024, 720000, 144000),
(2, 2024, 600000, 120000),
(3, 2024, 660000, 132000),
(4, 2024, 540000, 108000),
(5, 2024, 624000, 124800),
(6, 2024, 564000, 112800),
(7, 2024, 816000, 163200),
(8, 2024, 480000, 96000),
(9, 2024, 576000, 115200),
(10, 2024, 636000, 127200);

-- Insert values into the FinancialRecord table
INSERT INTO FinancialRecord (EmployeeID, RecordDate, Description, Amount, RecordType)
VALUES 
(1, '2024-01-10', 'Salary Payment', 60000.00, 'Income'),
(2, '2024-01-15', 'Salary Payment', 50000.00, 'Income'),
(3, '2024-01-20', 'Salary Payment', 55000.00, 'Income'),
(4, '2024-01-25', 'Salary Payment', 45000.00, 'Income'),
(5, '2024-01-30', 'Salary Payment', 52000.00, 'Income'),
(6, '2024-02-05', 'Salary Payment', 47000.00, 'Income'),
(7, '2024-02-10', 'Salary Payment', 68000.00, 'Income'),
(8, '2024-02-15', 'Medical Reimbursement', 3000.00, 'Expense'),
(9, '2024-02-20', 'Training Expense', 5000.00, 'Expense'),
(10, '2024-02-25', 'Travel Expense', 8000.00, 'Expense');
