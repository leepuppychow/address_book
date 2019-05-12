from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)

db = SQLAlchemy(app)

@app.route("/ping", methods=['GET'])
def home():
  return jsonify(
    status="OK"
  ), 200

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080, debug=True)