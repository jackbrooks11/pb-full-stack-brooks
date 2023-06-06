from datetime import datetime
import json
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import and_, func, extract

db = SQLAlchemy()

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

    def to_dict(self):
        sighting_dict = {
            'id': self.id,
            'spotter_project_id': self.spotter_project_id,
            'spotter_trip_id': self.spotter_trip_id,
            'evt_date': self.evt_date,
            'evt_datetime_utc': self.evt_datetime_utc.isoformat(),
            'vessel': self.vessel,
            'lat_d': self.lat_d,
            'long_d': self.long_d,
            'commonname': self.commonname,
            'observationcount': self.observationcount,
            'behavior': self.behavior,
            'distance': self.distance,
            'reticle': self.reticle,
            'bearing': self.bearing,
            'comments': self.comments,
            'corrected_latitude': self.corrected_latitude,
            'corrected_longitude': self.corrected_longitude
        }
        return sighting_dict
    
    @staticmethod
    def get_sightings(year: int, species: str):
        if not isinstance(year, int) or not isinstance(species, str):
            raise TypeError("Year must be an integer and species must be a str")
        sightings = WhaleSighting.query.filter(and_(WhaleSighting.evt_date.startswith(str(year)),
                                                    WhaleSighting.commonname == species)) \
                                                    .all()
        return sightings
    
    @staticmethod
    def get_unique_years():
        unique_years = db.session.query(
            extract('year', WhaleSighting.evt_datetime_utc)
        ).distinct().order_by(
            func.extract('year', WhaleSighting.evt_datetime_utc).desc()
        ).all()
        print(unique_years)
        return [str(year[0]) for year in unique_years]

    @staticmethod
    def get_unique_commonnames():
        commonnames = db.session.query(
            WhaleSighting.commonname
        ).distinct().order_by(
            WhaleSighting.commonname
        ).all()
        unique_commonnames = [commonname[0] for commonname in commonnames]
        return unique_commonnames