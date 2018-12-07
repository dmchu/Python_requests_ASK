curl -H "Content-Type: application/json" -d "{\"email\":\"alina.korolevich@yopmail.com\",\"password\":\"internship\"}" http://local.school.portnov.com:4520/api/v1/sign-in
or
curl -X POST -H "Content-Type: application/json" -d "{\"email\":\"alina.korolevich@yopmail.com\",\"password\":\"internship\"}" http://local.school.portnov.com:4520/api/v1/sign-in
"""
{"user":{"id":949,"email":"alina.korolevich@yopmail.com",
"name":"Alina Korolevich","group":"A01","role":"TEACHER",
"createdAt":"2018-10-29T18:47:56.000Z",
"updatedAt":"2018-10-29T18:52:22.000Z"},
"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImFsaW5hLmtvcm9sZXZpY2hAeW9wbWFpbC5jb20iLCJpYXQiOjE1NDMxOTM5MzIsImV4cCI6MTU0MzI4MDMzMn0.m1NwLoyQ9PV1Pw-ndXa83h_h1CP2rQ8vn1PT44e6M5o"}
"""



import requests
import json

url = "http://local.school.portnov.com:4520/api/v1/sign-in"

payload = {
	'email': 'alina.korolevich@yopmail.com',
	'password': 'internship'
	}
headers = {
    'content-type': "application/json",
    'Connection': "keep-alive"
    }

response = requests.post(url, data=json.dumps(payload), headers=headers)

parsed_json=json.loads(response.text)

token = parsed_json["token"]

"""
{"user":{"id":951,"email":"john.smith3@yopmail.com",
"name":"John Smith","group":"A001","role":"STUDENT",
"createdAt":"2018-10-30T17:25:09.000Z",
"updatedAt":"2018-10-30T18:03:54.000Z"},
"token":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImpvaG4uc21pdGgzQHlvcG1haWwuY29tIiwiaWF0IjoxNTQwOTI0NTk4LCJleHAiOjE1NDEwMTA5OTh9.BYOWgao7TX1i3PAAEI1rogggUVsJH6PEmy6mCI8BZig"}
"""

