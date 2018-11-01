import requests
import json
import re

# Sign in wtth role TEACHER


email = 'alina.korolevich@yopmail.com'

password = 'internship'



#=======================Code starts here=======================

url = "http://local.school.portnov.com:4520/api/v1/sign-in"


payload = {
	'email': email,
	'password': password
	}

headers = {
    'content-type': "application/json",
    'Connection': "keep-alive"
    }

response = requests.post(url, data=json.dumps(payload), headers=headers)

parsed_json=json.loads(response.text)

token = parsed_json["token"]

# Get list of users

url = "http://local.school.portnov.com:4520/api/v1/users"

headers = {
	'Authorization': "Bearer {}".format(token)
    }
r = requests.get(url, headers=headers)
parsed_json=json.loads(r.text)

list_for_delete = []

for i in parsed_json:

	if not re.match(r"^([A-Z][a-z]{2,9}\s[A-Z][a-z]{2,11}$)", i["name"]):
		list_for_delete.append(i)
	else:
		continue

# Delete users with bad names

print("{} users are going to be deleted".format(len(list_for_delete)))
		
for i in list_for_delete:

	url = "http://local.school.portnov.com:4520/api/v1/users/{}".format(i["id"])

	r = requests.delete(url, headers=headers)

	print(r.status_code)
	print("User: {} '{}' was permanently deleted".format(i["id"],i["name"]))
