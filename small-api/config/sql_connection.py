import sqlalchemy as alch
from dotenv import load_dotenv
import os

def connection_to_sql ():
    password = os.getenv("password")
    dbName = "employees"
    connectionData=f"mysql+pymysql://root:{password}@localhost/{dbName}"
    engine = alch.create_engine(connectionData)
    return engine