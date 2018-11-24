import requests
import json


email = 'alina.korolevich@yopmail.com'

password = 'internship'

url = "http://local.school.portnov.com:4520/api/v1/sign-in"

payload = {
    'email': email,
    'password': password
}

headers = {
    'content-type': "application/json",
    'Connection': "keep-alive"
}

r = requests.post(url, data=json.dumps(payload), headers=headers)

print(r.status_code)
print(r.text)

parsed_json = json.loads(r.text)

token = parsed_json["token"]

url = "http://local.school.portnov.com:4520/api/v1/quizzes"

headers = {
    'Authorization': "Bearer {}".format(token)
}

r = requests.get(url, headers=headers)

print(r.status_code)
# print(r.text)

parsed_json = json.loads(r.text)


quiz_id = None

for i in parsed_json:
    if i["name"] == "QA BASIC 821":
        quiz_id = i["id"]
    else:
        continue

url = "http://local.school.portnov.com:4520/api/v1/quiz/{}".format(quiz_id)

r = requests.delete(url, headers=headers)

print(r.status_code)
print("Quiz {}: {} was permanently deleted".format(i["name"],quiz_id))