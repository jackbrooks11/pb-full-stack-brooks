from flask import Blueprint

routes = Blueprint("routes", __name__)

# Define the GET route
@routes.route('/get_sighting_data', methods=['GET'])
def get_sighting_data():
    return "This is a blank GET route"