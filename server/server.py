# -*- coding: utf-8 -*-

## just a flask api


# from databricks import sql
# import pandas as pd
# from dotenv import load_dotenv
# import os
from flask import Flask

app = Flask(__name__)

## do check database here


# routing 
@app.route("/")
def index():
    ## make a query to get all distinct nutrients in our database
    return {
        "first": "page",
        "return": "index page",
        "make": "a drop down menu",
        "and": "a button"
    }

@app.route("/query_one")
def query_one():
    ## make a query to get {maybe 5} food with that nutrient
    return {
        "Result": "page",
        "display": "results for the selected nutrient"
    }


if __name__ == "__main__":
    app.run(debug=True)