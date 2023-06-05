import json
import pytest
from unittest.mock import patch
import sys
sys.path.append('../')
from app import create_app
from app.models import WhaleSighting
from app.routes import get_sighting_data

app = create_app()
app.app_context().push()

@pytest.fixture(scope="class")
def client():
    app.config.update({'TESTING': True})
    print(app.config)
    with app.app_context():
        with app.test_client() as client:
            yield client
        
class TestRoutes:
    @pytest.mark.parametrize("param1, param2", [
        ("value3", None),          # Test case 1: param1 provided, param2 missing
        (None, "value4"),          # Test case 2: param1 missing, param2 provided
        (None, None),              # Test case 3: Both params missing
    ])
    def test_get_sighting_data_incorrect_params(self, client, param1, param2):
        query_params = {}
        if param1 is not None:
            query_params["year"] = param1
        if param2 is not None:
            query_params["species"] = param2
        resp = client.get('/get_sighting_data', query_string=query_params)

        assert resp.status_code == 400

    @patch('app.models.WhaleSighting.get_sightings')
    def test_get_sighting_data_existing_data(self, mock_get_sightings, client):
        json_str = '[{"spotter_project_id":3,"spotter_trip_id":204,"evt_date":"20131126","evt_datetime_utc":"2013-11-26T21:14:29+00:00","vessel":"Lighthouse Hill","lat_d":37.683406857798,"long_d":-123.03782066012,"commonname":"Humpback Whale","observationcount":2,"behavior":null,"distance":"3611.7165040668","reticle":4.00,"bearing":241,"comments":"Jim","corrected_latitude":37.68246,"corrected_longitude":-123.026598}, \
                    {"spotter_project_id":3,"spotter_trip_id":204,"evt_date":"20131126","evt_datetime_utc":"2013-11-26T20:40:24+00:00","vessel":"Lighthouse Hill","lat_d":37.68861195765,"long_d":-123.05164335385,"commonname":"Unidentified Whale","observationcount":1,"behavior":null,"distance":"4528.4481315453","reticle":3.00,"bearing":255,"comments":"Jim","corrected_latitude":37.68798,"corrected_longitude":-123.036458}]'

        data = json.loads(json_str)[0]
        data2 = json.loads(json_str)[1]
        mock_get_sightings.return_value = [WhaleSighting(data), WhaleSighting(data2)]
        
        query_params = {
            'year': 2023,
            'species': 'whale'
        }
        resp = client.get('/get_sighting_data', query_string=query_params)
        assert resp.status == '200 OK'
        assert len(json.loads(resp.data)) == 2
        mock_get_sightings.assert_called_once_with(2023, 'whale')
