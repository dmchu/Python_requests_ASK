import requests
import json
import re

url = "http://local.school.portnov.com:4520/api/v1/users"

headers = {
	'Authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImFsaW5hLmtvcm9sZXZpY2hAeW9wbWFpbC5jb20iLCJpYXQiOjE1NDEwMTEzMTIsImV4cCI6MTU0MTA5NzcxMn0.059-8JYNgQsgtMc_zLCT8V3fq3XGnZdsc1KPLx8mcoI"
    }
r = requests.get(url, headers=headers)
parsed_json=json.loads(r.text)

list_for_delete = []

for i in parsed_json:

	if not re.match(r"^([A-Z][a-z]{2,9}\s[A-Z][a-z]{2,11}$)", i["name"]):
		list_for_delete.append(i)
	else:
		continue
		
for i in list_for_delete:

	url = "http://local.school.portnov.com:4520/api/v1/users/{}".format(i["id"])

	r = requests.delete(url, headers=headers)

	print(r.status_code)
	print("User: {} '{}' was permanently deleted".format(i["id"],i["name"]))
