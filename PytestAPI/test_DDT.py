import pytest
import requests

test_data_zip_codes = [
    ("us", "90210", "Beverly Hills"),
    ("ca", "B2A", "North Sydney South Central"),
    ("it", "50123", "Firenze") ]



@pytest.mark.parametrize('countrycode,zipcode,place',test_data_zip_codes)
def test_country_zip_code(countrycode, zipcode, place):

    response = requests.get(f"http://api.zippopotam.us/{countrycode}/{zipcode}")
    response_body = response.json()
    assert response_body['places'][0]['place name'] == place