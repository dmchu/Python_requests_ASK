import requests
import json

url = "http://local.school.portnov.com:4520/api/v1/sign-in"

payload = {'email': 'alina.korolevich@yopmail.com',
	'password': 'internship'
	}
headers = {
    'content-type': "application/json",
    'Connection': "keep-alive"
    }

response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response.text)

"""
{"user":{"id":951,"email":"john.smith3@yopmail.com",
"name":"John Smith","group":"A001","role":"STUDENT",
"createdAt":"2018-10-30T17:25:09.000Z",
"updatedAt":"2018-10-30T18:03:54.000Z"},
"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImpvaG4uc21pdGgzQHlvcG1haWwuY29tIiwiaWF0IjoxNTQwOTI0NTk4LCJleHAiOjE1NDEwMTA5OTh9.BYOWgao7TX1i3PAAEI1rogggUVsJH6PEmy6mCI8BZig"}
"""