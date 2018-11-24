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

list_of_quizzes = ['QA BASIC 105', 'QA BASIC 115', 'QA BASIC 128', 'QA BASIC 159', 'QA BASIC 167', 'QA BASIC 182', 'QA BASIC 214', 'QA BASIC 228', 'QA BASIC 247', 'QA BASIC 249', 'QA BASIC 254', 'QA BASIC 266', 'QA BASIC 317', 'QA BASIC 337', 'QA BASIC 343', 'QA BASIC 349', 'QA BASIC 396', 'QA BASIC 405', 'QA BASIC 411', 'QA BASIC 414', 'QA BASIC 424', 'QA BASIC 431', 'QA BASIC 437', 'QA BASIC 449', 'QA BASIC 460', 'QA BASIC 485', 'QA BASIC 502', 'QA BASIC 544', 'QA BASIC 558', 'QA BASIC 564', 'QA BASIC 574', 'QA BASIC 589', 'QA BASIC 601', 'QA BASIC 603', 'QA BASIC 614', 'QA BASIC 642', 'QA BASIC 656', 'QA BASIC 658', 'QA BASIC 702', 'QA BASIC 825', 'QA BASIC 908', 'QA BASIC 931', 'QA BASIC 960', 'QA BASIC 972']

for quiz in list_of_quizzes:
    for i in parsed_json:
        if i["name"] == quiz:
            quiz_id = i["id"]
            url = "http://local.school.portnov.com:4520/api/v1/quiz/{}".format(quiz_id)
            r = requests.delete(url, headers=headers)
            print(r.status_code)
            print("Quiz {}: {} was permanently deleted".format(i["name"],quiz_id))
        else:
            continue