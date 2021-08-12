"""
use the api to get the details of the country/zipcode and location

"""

import requests

response = requests.get("http://api.zippopotam.us/us/90210")

def test_location():

    print(response.text)
    print(response.json())

    # check the response code

    assert response.status_code == 200


def test_response_header_check():

    assert response.headers['Content-Type'] == 'application/json'


def test_response_body_element():

    request_body = response.json()

    assert request_body['country'] == 'United States'



def test_check_city_name():
    response_body = response.json()
    assert response_body['places'][0]['place name'] == 'Beverly Hills'


