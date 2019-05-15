import os 

from flask import Flask, jsonify
from flask_migrate import Migrate 
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql+psycopg2://%s:%s@%s/%s' % (
  os.environ['DB_USER'], os.environ['DB_PASS'], os.environ['DB_HOST'], os.environ['DB_NAME']
)

db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)

from models import User, Address, users_schema, addresses_schema

@app.route("/api/v1/ping", methods=["GET"])
def health_check():
  return jsonify(
    status="OK"
  ), 200

@app.route("/api/v1/users", methods=["GET"])
def all_users():
  all_users = User.all()
  result = users_schema.dump(all_users)
  return jsonify(result.data), 200

@app.route("/api/v1/addresses", methods=["GET"])
def all_addresses():
  all_addresses = Address.all()
  result = addresses_schema.dump(all_addresses)
  return jsonify(result.data), 200
