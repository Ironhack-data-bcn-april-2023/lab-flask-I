import pandas as pd
import config.sql_connection as conn

def get_everything ():
    query = "SELECT * FROM salaries LIMIT 10;"
    engine = conn.connection_to_sql()
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")


def table_ten(tablename):
    query = f"SELECT * FROM {tablename} LIMIT 10;"
    engine = conn.connection_to_sql()
    df = pd.read_sql_query(query, engine)
    return df.to_dict(orient="records")
