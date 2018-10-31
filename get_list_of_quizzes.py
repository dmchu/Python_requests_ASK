import requests

url = "http://local.school.portnov.com:4520/api/v1/quizzes"

headers = {
	'Authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImFsaW5hLmtvcm9sZXZpY2hAeW9wbWFpbC5jb20iLCJpYXQiOjE1NDA5MzcyOTEsImV4cCI6MTU0MTAyMzY5MX0.nnMqH7R9f_SXjqQkOn2-DuHnOxvxgru4IqdPIQV4Fe4"
    }
r = requests.get(url, headers=headers)

print(r.status_code)
print(r.headers)