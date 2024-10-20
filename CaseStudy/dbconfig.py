import pyodbc
def create_db_connection():
    try:
        connection_string = (
            "Driver={ODBC Driver 18 for SQL Server};"
            "Server=ARES\\SQLEXPRESS;"
            "Database=EmployeeManagementDB;"
            "TrustServerCertificate=yes;"
            "Trusted_Connection=yes;"
        )
        conn = pyodbc.connect(connection_string)
        print (conn)
    except Exception as e:
        print("Error while connecting to the DB: {}".format(e))

create_db_connection()