"""
https://reqres.in/api/users
"""

import requests

# data which we pass in post() method

payload = {
    "name": "morpheus",
    "job": "leader"
}


resp = requests.post("https://reqres.in/api/users", data=payload)
print("status code", resp)
res_json = resp.json()
print(res_json)
assert res_json['job'] == 'leader' , " job data mismatch"