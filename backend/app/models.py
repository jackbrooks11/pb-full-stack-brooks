from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from database import db

class WhaleSighting(db.Model):
    __tablename__ = 'whale_sightings'
    
    id = db.Column(db.Integer, primary_key=True)
    spotter_project_id = db.Column(db.Integer)
    spotter_trip_id = db.Column(db.Integer)
    evt_date = db.Column(db.String(8))
    evt_datetime_utc = db.Column(db.DateTime)
    vessel = db.Column(db.String(100))
    lat_d = db.Column(db.Float)
    long_d = db.Column(db.Float)
    commonname = db.Column(db.String(100))
    observationcount = db.Column(db.Integer)
    behavior = db.Column(db.String(100))
    distance = db.Column(db.Float)
    reticle = db.Column(db.Float)
    bearing = db.Column(db.Integer)
    comments = db.Column(db.String(255))
    corrected_latitude = db.Column(db.Float)
    corrected_longitude = db.Column(db.Float)

    def __init__(self, data):
        self.spotter_project_id = data.get('spotter_project_id')
        self.spotter_trip_id = data.get('spotter_trip_id')
        self.evt_date = data.get('evt_date')
        self.evt_datetime_utc = datetime.fromisoformat(data.get('evt_datetime_utc'))
        self.vessel = data.get('vessel')
        self.lat_d = data.get('lat_d')
        self.long_d = data.get('long_d')
        self.commonname = data.get('commonname')
        self.observationcount = data.get('observationcount')
        self.behavior = data.get('behavior')
        self.distance = data.get('distance')
        self.reticle = data.get('reticle')
        self.bearing = data.get('bearing')
        self.comments = data.get('comments')
        self.corrected_latitude = data.get('corrected_latitude')
        self.corrected_longitude = data.get('corrected_longitude')
