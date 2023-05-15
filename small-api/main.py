from flask import Flask, request, jsonify
import random
import requests


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world!"

@app.route("/random-number")
def random_int():
    return str(random.randint(0,10))

if __name__ == "__main__":
     app.run(port=9000, debug=False)