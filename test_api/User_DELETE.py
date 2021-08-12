"""
This return 204 response code when record get deleted

"""

import requests

res = requests.delete("https://reqres.in/api/users/2")
print(res.status_code)
