import requests

url = "http://local.school.portnov.com:4520/api/v1/activate/951/be66c53931bdfc7aca80f9aa60d9e5f243af6a10"

response = requests.get(url)

print(response.text)

#{"status":"success","message":"User was activated"}
