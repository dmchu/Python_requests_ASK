import requests

url = "http://local.school.portnov.com:4520/api/v1/users/955"

headers = {
	'Authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImFsaW5hLmtvcm9sZXZpY2hAeW9wbWFpbC5jb20iLCJpYXQiOjE1NDA5NDE2MDIsImV4cCI6MTU0MTAyODAwMn0.lc6EsSXzq9a5rJA3xSD4c8XmtCefvnmEA1Rk4C906Gs"
    }
r = requests.delete(url, headers=headers)

print(r.status_code)
print(r.text)

# 200
# {"status":"success","message":"Quiz was deleted"}