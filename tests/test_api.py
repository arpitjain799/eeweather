import pytest

from eeweather import get_version
from eeweather.api import (
    get_lat_long_climate_zones,
    get_zcta_metadata,
)
from eeweather.exceptions import (
    UnrecognizedZCTAError,
    UnrecognizedUSAFIDError,
)


def test_get_version():
    assert get_version() is not None


def test_get_zcta_metadata():
    metadata = get_zcta_metadata('90006')
    assert metadata == {
        'ba_climate_zone': 'Hot-Dry',
        'ca_climate_zone': 'CA_09',
        'geometry': None,
        'iecc_climate_zone': '3',
        'iecc_moisture_regime': 'B',
        'latitude': '34.0480061236777',
        'longitude': '-118.294181179333',
        'zcta_id': '90006'
    }

    with pytest.raises(UnrecognizedZCTAError) as excinfo:
        get_zcta_metadata('00000')
    assert excinfo.value.value == '00000'


def test_get_lat_long_climate_zones():
    climate_zones = get_lat_long_climate_zones(35.1, -119.2)
    assert climate_zones == {
        'iecc_climate_zone': '3',
        'iecc_moisture_regime': 'B',
        'ba_climate_zone': 'Hot-Dry',
        'ca_climate_zone': 'CA_13',
    }


def test_get_lat_long_climate_zones_out_of_range():
    climate_zones = get_lat_long_climate_zones(0, 0)
    assert climate_zones == {
        'iecc_climate_zone': None,
        'iecc_moisture_regime': None,
        'ba_climate_zone': None,
        'ca_climate_zone': None,
    }
