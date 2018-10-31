import requests

url = "http://local.school.portnov.com:4520/api/v1/quiz/2002"

headers = {
	'Authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImFsaW5hLmtvcm9sZXZpY2hAeW9wbWFpbC5jb20iLCJpYXQiOjE1NDA5Mzk1MTUsImV4cCI6MTU0MTAyNTkxNX0.JR-XK-Z9QqgDUv7H4-rqw9BYDjyv6Uf-7EavRgxXodA"
    }
r = requests.delete(url, headers=headers)

print(r.status_code)
print(r.text)

# 200
# {"status":"success","message":"Quiz was deleted"}