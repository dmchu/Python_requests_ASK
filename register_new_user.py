import requests
import json

url = "http://local.school.portnov.com:4520/api/v1/sign-up"

payload = {'email': 'john.smith3@yopmail.com',
	'group': 'A001',
	'name': 'John Smith',
	'password': 'Internship123'
	}
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    }

response = requests.post(url, data=json.dumps(payload), headers=headers)

print(response.text)