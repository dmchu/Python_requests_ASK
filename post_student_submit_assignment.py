import requests
import json

url = "http://local.school.portnov.com:4520/api/v1/submit-assignment"

payload = {
	"assignmentId":4538,
	"answers":[
	{"textAnswer":"Test answer"},
	{"textAnswer":"Test answer"}]
	}
headers = {
    'content-type': "application/json",
    'Authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImpvaG4uc21pdGgzQHlvcG1haWwuY29tIiwiaWF0IjoxNTQwOTk4MjE0LCJleHAiOjE1NDEwODQ2MTR9.TVAa7kIfmlIted0x-mPRjdlGvyzFAXQ4RNxrZTzrDP4"
    }

response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response.status_code)
print(response.text)


