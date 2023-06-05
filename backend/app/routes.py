from http.client import BAD_REQUEST
import json
from flask import Blueprint, request
from app.models import WhaleSighting

routes = Blueprint("routes", __name__)

# Define the GET route
@routes.route('/get_sighting_data', methods=['GET'])
def get_sighting_data():
    year = request.args.get('year')
    species = request.args.get('species')
    if not year or not species:
        return "Year or species missing", 400
    try:
        year = int(year)
    except ValueError:
        return "Year not a number", 400
    sightings = WhaleSighting.get_sightings(year, species)
    sightings_list = []
    for sighting in sightings:
        sightings_list.append(sighting.to_dict())
    return json.dumps(sightings_list)
