import requests
import json

url = "http://local.school.portnov.com:4520/api/v1/reset-password/951/ae8d3d04865fcb76c981d9866174de5809edec22"

payload = {
	"password": "Internship321"
	}

headers = {
    'content-type': "application/json"
    }

response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response.text)

#{"status":"success","message":"Password was changed"}