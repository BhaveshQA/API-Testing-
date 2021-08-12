"""
payload data read from the external file and pass to the post request
"""

import requests
import json

# read the file

datafile = open("data.json","r").read()

# loads() : this method deserialize str, byte json object  into the python object
res = requests.post("https://reqres.in/api/users", json.loads(datafile))
print(res)
