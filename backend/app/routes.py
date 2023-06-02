from app import app

# Define the GET route
@app.route('/get_sighting_data', methods=['GET'])
def get_sighting_data():
    return "This is a blank GET route"