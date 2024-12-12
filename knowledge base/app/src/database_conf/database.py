import os
from sqlalchemy import create_engine
import pyodbc
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.conn_string = f"mssql+pyodbc://{os.getenv('SQL_USER')}:{os.getenv('SQL_PASSWORD')}@" \
                           f"{os.getenv('SQL_SERVER')}/{os.getenv('SQL_DATABASE')}?driver=ODBC Driver 17 for SQL Server"
        self.engine = create_engine(self.conn_string)

    def test_connection(self):
        try:
            self.engine.connect()
            print("Connection established successfully!")
        except Exception as e:
            print(f"Connection error: {e}")

    def get_pyodbc_connection(self):
        return pyodbc.connect(
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={os.getenv('SQL_SERVER')};"
            f"DATABASE={os.getenv('SQL_DATABASE')};"
            f"UID={os.getenv('SQL_USER')};"
            f"PWD={os.getenv('SQL_PASSWORD')};"
        )
