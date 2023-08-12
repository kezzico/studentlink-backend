# flaskapp.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import dotenv_values
from database import execute_select_query, execute_insert_query

config = dotenv_values(".env")

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World"

@app.route("/health")
def health():
    return "✅"

# for demonstrative purposes only
@app.route("/roommate")
def get_data():
    select_query = "SELECT * FROM ROOMMATE_PROFILE"
    select_result = execute_select_query(select_query)
    print("SELECT Result:", select_result)

    return jsonify(select_result)


# flask configuration
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5051)

if config.get("DEBUG") == "True":
    CORS(app, origins=["http://localhost:3000"])

