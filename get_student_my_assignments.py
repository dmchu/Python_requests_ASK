import requests

url = "http://local.school.portnov.com:4520/api/v1/my-assignments"

headers = {
    'Authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImpvaG4uc21pdGgzQHlvcG1haWwuY29tIiwiaWF0IjoxNTQwOTk4MjE0LCJleHAiOjE1NDEwODQ2MTR9.TVAa7kIfmlIted0x-mPRjdlGvyzFAXQ4RNxrZTzrDP4"
    }

r = requests.get(url, headers=headers)

print(r.status_code)



