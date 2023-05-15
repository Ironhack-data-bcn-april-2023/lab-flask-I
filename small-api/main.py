from flask import Flask, request, jsonify
import random

import config.sql_connection as conn
import tools.sql_queries as queries
import pandas as pd


app = Flask(__name__)


# your code here
@app.route("/")
def hello_world():
    return "Hello world!"

@app.route("/random-number")
def random_int ():
    x = random.randint(0, 10)
    return f"{x}"

@app.route("/everything-employees")
def example():
    return queries.get_everything()

@app.route("/table/<tablename>")
def ultima(tablename):
    return queries.table_ten(tablename)

if __name__ == "__main__":
     app.run(port=9000, debug=False)