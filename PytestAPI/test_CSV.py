"""
API Testing with the csv data file
"""
import csv
import requests
import pytest


def csv_data_read():
    # declare the empty array list
    test_csv_data = []

    # read the csv file
    filename = 'user.csv'

    with open(filename, newline='') as abc:
        csvreader = csv.reader(abc, delimiter=',')

    # exclude the hedear
    #data = csvreader.next()

    # if want to skip header
        next(csvreader)

    # use the for loop to iterate over the row
        for row in csvreader:
            test_csv_data.append(row)

        return test_csv_data

#print(csv_data_read())


@pytest.mark.parametrize("code,zipcode,place",csv_data_read())
def test_csv_row_data(code, zipcode, place):

    response = requests.get(f"http://api.zippopotam.us/{code}/{zipcode}")
    response_body = response.json()

    assert response_body['places'][0]['place name'] == place

