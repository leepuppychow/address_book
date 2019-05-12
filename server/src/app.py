from flask import Flask, jsonify
from .config import app_config

def create_app(env_name):
  app = Flask(__name__)

  app.config.from_object(app_config[env_name])

  @app.route('/ping', methods=['GET'])
  def index():
    return jsonify(
      status="OK"
    ), 200

  return app
