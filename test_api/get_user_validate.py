import requests



p ={"page" : 2}

# store response in variable
res = requests.get("https://reqres.in/api/users",params=p)
print(res.url)

# store response in json
json_resp = res.json()

# validate property of the JSON Response
print("Total Page count : ",json_resp['page'])
assert json_resp['page'] == 2 , "Page count not match"

print("Total Record :", json_resp['total'])
assert json_resp['total'] == 12

# validate json data
print(json_resp["data"][0]["email"])
assert json_resp["data"][0]["email"].endswith("reqres.in") , " email format not matching"

print(json_resp["data"][1]['first_name'])
assert json_resp["data"][1]['first_name'] != None , "firstname not be null"