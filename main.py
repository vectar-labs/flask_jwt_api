from flask import Flask, request, jsonify
from extensions import db



def create_app():
    app = Flask(__name__)
    
    # setting up configuration from environment variables with a prefix
    app.config.from_prefixed_env()
    db.init_app(app)

    return app