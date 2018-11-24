import requests

url = "http://local.school.portnov.com:4520/api/v1/activate/951/be66c53931bdfc7aca80f9aa60d9e5f243af6a10"

response = requests.get(url)

print(response.text)

#{"status":"success","message":"User was activated"}
http://ask-stage.portnov.com//#/activate/976/0e89cc2cedb61629396c7cb0ec9d62915138e894