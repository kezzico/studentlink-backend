# flaskapp.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import dotenv_values

config = dotenv_values(".env")

app = Flask(__name__)

if config.get("DEBUG"):
    CORS(app, origins=["http://localhost:3000"])
    print("poo")


@app.route("/")
def index():
    return "Hello World"


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5051)

