import os
from flask import Flask
from database import db
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
from config import Config
from app.models.whale_sighting import WhaleSighting

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    db.init_app(app)
    return app 

def setup_database(app):    
    with app.app_context():
        db.create_all()

if __name__ == '__main__':
    app = create_app()
    # Because this is just a demonstration, we set up the database like this.
    setup_database(app)
    app.run()