from flask import Flask, jsonify, request
import random
import config.sql_connection as conn
import tools.sql_queries as queries
import pandas as pd
import requests


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world!"

@app.route("/random-number")
def random_int():
    return str(random.randint(0, 10))

@app.route("/everything-employees")
def example ():
    return queries.get_everything()

@app.route("/table/<tablename>")
def example_table (tablename):
    return queries.table_ten(tablename)


#FLASK III

@app.route("/insert-into-employees", methods =["POST"])
def example_insert_db ():
    dict_ = {
    "emp_no": request.args["emp_no"],
    "birth_date": request.args["birth_date"],
    "first_name": request.args["first_name"],
    "last_name": request.args["last_name"],
    "gender": request.args["gender"],
    "hire_date": request.args["hire_date"]
    } 

    return queries.insert_new_employee(dict_)


#FLASK III

if __name__ == "__main__":
    app.run(port=9000, debug=False)


