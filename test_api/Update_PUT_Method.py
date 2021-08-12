"""
PUT = Update / Replace
- in this put request we need to provide all data
- if record exist on database then it update , get status code = 200
- if record not exist then it crete new record in database, get status code = 201
"""


import requests


payload = \
    {
        "name": "Bhavesh",
        "job": "QA Engineer"
    }


rsp = requests.put("https://reqres.in/api/users/2",data=payload)
print(rsp)
print(rsp.json())