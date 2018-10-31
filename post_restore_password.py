import requests
import json

url = "http://local.school.portnov.com:4520/api/v1/forgot-password"

payload = {
	'email': 'john.smith3@yopmail.com'
	}

headers = {
    'content-type': "application/json"
    }

response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response.text)

#{"status":"success","message":"Reset password email was sent"}