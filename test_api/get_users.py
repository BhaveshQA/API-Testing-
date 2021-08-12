"""
Install two package
1. requests
2. jsonpath
"""

import requests

# get() = pass the api url and store the response in variable
resp = requests.get("https://reqres.in/api/users?page=2")
print(resp)
code=resp.status_code

# assertion for the code verification
assert code == 200, " Code not matched "

# different way to get the data

# print(resp.text) # this return data in unicode format means in plain text

# print(resp.content) # this return data in byte format

print(resp.json()) # this return data in JSON encoded format

# print the different property of the api

print(resp.headers)

print(resp.cookies)

print(resp.encoding)
