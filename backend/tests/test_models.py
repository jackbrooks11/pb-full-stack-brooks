from datetime import datetime
import sys
sys.path.append('../')
from app import create_app
from app.models import WhaleSighting
import pytest
import json
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = create_app()
app.app_context().push()

class TestModels:
    def test_create_sighting(self):
        json_str = '[{"spotter_project_id":3,"spotter_trip_id":204,"evt_date":"20131126","evt_datetime_utc":"2013-11-26T21:09:43+00:00","vessel":"Lighthouse Hill","lat_d":37.693351182343,"long_d":-123.0855248509,"commonname":"Humpback Whale","observationcount":2,"behavior":null,"distance":"7381.1061097744","reticle":1.50,"bearing":265,"comments":"Jim","corrected_latitude":37.693008,"corrected_longitude":-123.061835}]'

        data = json.loads(json_str)[0]

        whale_sighting = WhaleSighting(data)

        assert whale_sighting.spotter_project_id == 3

        assert whale_sighting.lat_d == 37.693351182343

        assert whale_sighting.evt_datetime_utc == datetime.fromisoformat("2013-11-26T21:09:43+00:00")

    @pytest.mark.parametrize("param", [('1998', 'bluewhale'), (1998, 5), (1998.1, 'bluewhale')])
    def test_get_sighting_with_invalid_input(self, param):
        with pytest.raises(TypeError):
            WhaleSighting.get_sighting(param[0], param[1])

    @pytest.mark.parametrize("param", [(1665, 'Unidentified Whale'), (2013, 'randomwhale')])
    def test_get_sighting_nonexistent_record(self, param):
        records = WhaleSighting.get_sighting(*param)
        assert records == []

    def test_get_sighting_existing_record(self):
        records = WhaleSighting.get_sighting(2013, 'Unidentified Whale')
        assert isinstance(records, list)
        assert all(isinstance(record, WhaleSighting) for record in records)
        assert hasattr(records[0], 'distance')
        assert records[0].distance == 4528.4481315453