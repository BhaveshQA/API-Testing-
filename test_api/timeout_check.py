"""
https://httpbin.org/
https://httpbin.org/delay/5

"""

import requests

# positive case
res = requests.get("https://httpbin.org/delay/3",timeout =5)
print(res)

# negative case
res = requests.get("https://httpbin.org/delay/5",timeout =3)
print(res)