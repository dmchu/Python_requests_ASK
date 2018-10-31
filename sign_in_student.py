import requests
import json

url = "http://local.school.portnov.com:4520/api/v1/sign-in"

payload = {'email': 'john.smith3@yopmail.com',
	'password': 'internship123'
	}
headers = {
    'content-type': "application/json",
    }

response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response.text)

"""
{"user":{"id":951,"email":"john.smith3@yopmail.com",
"name":"John Smith","group":"A001","role":"STUDENT",
"createdAt":"2018-10-30T17:25:09.000Z",
"updatedAt":"2018-10-30T21:46:26.000Z"},
"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImpvaG4uc21pdGgzQHlvcG1haWwuY29tIiwiaWF0IjoxNTQwOTQ1MTc5LCJleHAiOjE1NDEwMzE1Nzl9.pY9ETUMlqZ6yXR42EREDeHAJZx9U8-_48IAzGnH6zvI"}

"""