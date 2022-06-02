import pyodbc


def config_db():
    string_connection = 'Driver={SQL Server};Server=LAPTOP-65C1BIEB\SQLEXPRESS;Database=FLASK_API;Truted_Connection=yes'

    conn = pyodbc.connect(string_connection)

    return conn.cursor()