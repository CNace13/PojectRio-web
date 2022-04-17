from decouple import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
import logging
from logging.handlers import RotatingFileHandler

# Globally accessible libraries
db = SQLAlchemy()
bc = Bcrypt()
ma = Marshmallow()
jwt = JWTManager()

def init_app():
    # Construct core application
    app = Flask(__name__)
    app.config.from_pyfile('config.py')

    # Initialize Plugins
    db.init_app(app)
    bc.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)

    #Set logger properties
    #Rotating log file
    handler = RotatingFileHandler('endpoint_log.log', maxBytes=10000, backupCount=2)
    handler.setLevel(logging.INFO)
    app.logger.addHandler(handler)

    with app.app_context():
        #import routes
        from .views import populate_db
        from .views import user
        from .views import db_setup
        from .views import client_routes
        from .views import stat_retrieval
        from .views import api_key
        from .views import log
        
        #create sql tables for data models
        db.create_all()

        return app
