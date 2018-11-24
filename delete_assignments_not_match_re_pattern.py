from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import requests
import json
import re



def delete_assignment_api():

    url = "http://local.school.portnov.com:4520/api/v1/sign-in"

    email = 'alina.korolevich@yopmail.com'

    password = 'internship'

    payload = {
        'email': email,
        'password': password
    }

    headers = {
        'content-type': "application/json",
        'Connection': "keep-alive"
    }

    r = requests.post(url, data=json.dumps(payload), headers=headers)


    parsed_json = json.loads(r.text)

    token = parsed_json["token"]

    url = "http://local.school.portnov.com:4520/api/v1/assignments"

    headers = {
        'Authorization': "Bearer {}".format(token)
    }

    r = requests.get(url, headers=headers)

    parsed_json = json.loads(r.text)

    for i in parsed_json:
        if re.match(r"^([Q][A]\s[B][A][S][I][C]\s[1-9][0-9][0-9]$)", i['quiz']['name']):
            assignment_group_id = i['assignmentGroupID']

            url = "http://local.school.portnov.com:4520/api/v1/assignment/{}".format(assignment_group_id)
            response = requests.delete(url, headers=headers)

            print(response.status_code)
            print("Assignment: with {}  with id {} was permanently deleted".format(i['quiz']['name'], assignment_group_id))


        else:
            continue


delete_assignment_api()
