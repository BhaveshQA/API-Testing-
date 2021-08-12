"""
PATCH = Update / Modify
- in this we need to pass the particular parameter which need to update

"""

import requests

payload = {
    "name" : "hina"
}


rsp = requests.patch("https://reqres.in/api/users/2",data=payload)
print(rsp)
