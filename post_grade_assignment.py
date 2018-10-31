import requests
import json

url = "http://local.school.portnov.com:4520/api/v1/assignment/4540"

payload = {
	"summary": "Summary from teacher",
	"result": "PASSED",
	"grades": [
	{
	  "comment": "Teacher comment",
	  "additionalScore": 5
	}
	]
	}
headers = {
    'content-type': "application/json",
    'Authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImFsaW5hLmtvcm9sZXZpY2hAeW9wbWFpbC5jb20iLCJpYXQiOjE1NDEwMDg5NDMsImV4cCI6MTU0MTA5NTM0M30.pkCTTfgFIjJ9iB9CDrpbTdvjCSuGCG8Tii0AJljFFUM"
    }

response = requests.put(url, data=json.dumps(payload), headers=headers)

print(response.status_code)
print(response.text)

# 200
