import os
from flask import Flask
from database import db
from config import Config
from app.models import WhaleSighting
import requests

app = Flask(__name__)
app.config.from_object(Config())
db.init_app(app)

def setup_database(app):    
    with app.app_context():
        db.create_all()
        seed()

def seed():
    # Check if any sightings exist in the database
    if WhaleSighting.query.first() is None:
        try:
            # Retrieve data from the URL
            url = "https://geo.pointblue.org/whale-map/full_stack_excercise.php?timestamp=1"
            response = requests.get(url)
            response.raise_for_status()  # Raise an exception for any HTTP errors
            # Process data
            data = response.json()
            for sighting in data:
                whale_sighting = WhaleSighting(sighting)
                db.session.add(whale_sighting)
            
            db.session.commit()
            print("Sightings added to the database.")
        
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to retrieve data from {url}: {str(e)}")
        
        except Exception as e:
            raise Exception(f"An unexpected error occurred: {str(e)}")