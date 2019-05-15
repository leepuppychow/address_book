import os 

from flask import Flask, request, jsonify
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

from models import User, Address, addresses_schema, address_schema

@app.route("/api/v1/ping", methods=["GET"])
def health_check():
  return jsonify(message="OK"), 200

@app.route("/api/v1/addresses", methods=["GET"])
def all_addresses():
  all_addresses = Address.all()
  result = addresses_schema.dump(all_addresses)
  return jsonify(result.data), 200

@app.route("/api/v1/addresses", methods=["POST"])
def create_address():
  street = request.json['street']
  city = request.json['city']
  state = request.json['state']
  zip = request.json['zip']

  new_address = Address.create(street, city, state, zip)
  if new_address is not None:
    return address_schema.jsonify(new_address), 201
  else:
    return jsonify(message="Unable to create address"), 400

@app.route("/api/v1/addresses/<id>", methods=["GET"])
def find_address(id):
  address = Address.find(id)
  if address is None:
    return jsonify(message="Address not found"), 404
  else:
    return address_schema.jsonify(address), 200

@app.route("/api/v1/addresses/<id>", methods=["PUT"])
def update_address(id):
  street = request.json['street']
  city = request.json['city']
  state = request.json['state']
  zip = request.json['zip']

  address = Address.find(id)
  if address is None:
    return jsonify(message="Error updating address, not found"), 404
  
  updated_address = address.update(street, city, state, zip)
  return address_schema.jsonify(updated_address), 200

@app.route("/api/v1/addresses/<id>", methods=["DELETE"])
def delete_address(id):
  address = Address.find(id)
  if address is None:
    return jsonify(message="Error deleting address, not found"), 404
  success = address.delete()
  if success:
    return jsonify(message="Successfully deleted address"), 204
  else:
    return jsonify(message="Error deleting address"), 400
