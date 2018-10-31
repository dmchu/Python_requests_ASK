import requests

url = "http://local.school.portnov.com:4520/api/v1/assignments"

headers = {
    'Authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImFsaW5hLmtvcm9sZXZpY2hAeW9wbWFpbC5jb20iLCJpYXQiOjE1NDEwMDE4NTQsImV4cCI6MTU0MTA4ODI1NH0.dTXQaWFfSwK5TxWU1cHdAgT4yHdOIoPjXPErVPh__TU"
    }

r = requests.get(url, headers=headers)

print(r.status_code)



