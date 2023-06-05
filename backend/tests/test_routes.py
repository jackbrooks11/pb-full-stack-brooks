import json
import pytest
from unittest.mock import patch
import sys
sys.path.append('../')
from app import create_app
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

    @patch('app.models.WhaleSighting.get_sighting')
    def test_get_sighting_data_existing_data(self, mock_get_sighting, client):
        mock_get_sighting.return_value = ['mocked_sighting1', 'mocked_sighting2']
        
        query_params = {
            'year': 2023,
            'species': 'whale'
        }
        resp = client.get('/get_sighting_data', query_string=query_params)
        assert resp.status == '200 OK'
        assert json.loads(resp.data.decode('utf-8')) == ['mocked_sighting1', 'mocked_sighting2']
        mock_get_sighting.assert_called_once_with(2023, 'whale')
