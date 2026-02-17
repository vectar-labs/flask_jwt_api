from flask import Flask, request, jsonify
from extensions import db
from auth import auth_bp



def create_app():
    app = Flask(__name__)
    
    # setting up configuration from environment variables with a prefix
    app.config.from_prefixed_env()
    
    # intialize extensions
    db.init_app(app)
    app.register_blueprint(auth_bp, url_prefix='/auth')
    
    # intialize the database   
    # with app.app_context():
        # db.create_all()

    return app