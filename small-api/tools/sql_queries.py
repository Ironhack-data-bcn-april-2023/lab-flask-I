import pandas as pd
import config.sql_connection as conn
from flask import jsonify

def get_everything():
    query = "SELECT * FROM salaries LIMIT 10;"
    engine = conn.connection_to_sql()
    df = pd.read_sql_query(query, engine)
    data = df.to_dict(orient="records")
    return  data
    