from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import requests
import json
import re


def delete_quiz_api():

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

    response = requests.post(url, data=json.dumps(payload), headers=headers)

    parsed_json = json.loads(response.text)

    token = parsed_json["token"]

    url = "http://local.school.portnov.com:4520/api/v1/quizzes"

    headers = {
        'Authorization': "Bearer {}".format(token)
    }

    r = requests.get(url, headers=headers)
    parsed_json = json.loads(r.text)

    for i in parsed_json:
        if re.match(r"^([Q][A]\s[B][A][S][I][C]\s[1-9][0-9][0-9]$)", i['name']):
            quiz_id = i["id"]

            url = "http://local.school.portnov.com:4520/api/v1/quiz/{}".format(quiz_id)

            r = requests.delete(url, headers=headers)
            print("Quiz: {}  with id {} was permanently deleted".format(i['name'], quiz_id))
        else:
            continue

delete_quiz_api()
