import os 

from flask import Flask, jsonify
from flask_migrate import Migrate 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://%s:%s@%s/%s' % (
  os.environ['DB_USER'], os.environ['DB_PASS'], os.environ['DB_HOST'], os.environ['DB_NAME']
)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

@app.route("/ping")
def health_check():
  return jsonify(
    status="OK THEN"
  ), 200
