import requests
import json

url = "http://local.school.portnov.com:4520/api/v1/users/change-group/954"

headers = {
	'content-type': "application/json",
	'Authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImFsaW5hLmtvcm9sZXZpY2hAeW9wbWFpbC5jb20iLCJpYXQiOjE1NDA5NDE2MDIsImV4cCI6MTU0MTAyODAwMn0.lc6EsSXzq9a5rJA3xSD4c8XmtCefvnmEA1Rk4C906Gs"
    }

payload = {
	"group": "B002"
	}
r = requests.put(url, data=json.dumps(payload), headers=headers)

print(r.status_code)
print(r.text)
