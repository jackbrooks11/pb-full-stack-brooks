import sys
import pytest
import sys
sys.path.append('../')
from app import app
from app.routes import get_sighting_data

@pytest.fixture(scope="class")
def client():
    app.config.update({'TESTING': True})
    print(app.config)
    with app.app_context():
        with app.test_client() as client:
            yield client
        
class TestRoutes:
    def test_get_sighting_data_success(self, client):
        resp = client.get('/get_sighting_data')
        assert resp.status == '200 OK'

