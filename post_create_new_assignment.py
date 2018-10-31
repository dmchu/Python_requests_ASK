import requests
import json

url = "http://local.school.portnov.com:4520/api/v1/assignment"

payload = {
	"quizId": 1279,
	"userIds": [951]
	}
headers = {
    'content-type': "application/json",
    'Authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImFsaW5hLmtvcm9sZXZpY2hAeW9wbWFpbC5jb20iLCJpYXQiOjE1NDEwMDE4NTQsImV4cCI6MTU0MTA4ODI1NH0.dTXQaWFfSwK5TxWU1cHdAgT4yHdOIoPjXPErVPh__TU"
    }

response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response.status_code)
print(response.text)

# 200
"""
[{"id":4541,"userId":951 ...}]
"""