import requests
import json
import re

# Sign in wtth role TEACHER


email = 'alina.korolevich@yopmail.com'

password = 'internship'



#=======================Code starts here=======================

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

parsed_json=json.loads(response.text)

token = parsed_json["token"]

# Get list of quizes

url = "http://local.school.portnov.com:4520/api/v1/quizzes"

headers = {
	'Authorization': "Bearer {}".format(token)
    }

response = requests.get(url, headers=headers)
unique_list = []
parsed_json=json.loads(response.text)
for i in parsed_json:
	# if re.match(r"^([' '])", i['name']):
	# print(i['name'])
# 	if i['name'] not in unique_list:
# 		unique_list.append(i['name'])
# 	else:
	quiz_id = i["id"]
	url = "http://local.school.portnov.com:4520/api/v1/quiz/{}".format(quiz_id)
	r = requests.delete(url, headers=headers)
	print("Quiz: {}  with id {} was permanently deleted".format(i['name'], quiz_id))

# print('unique_list:',unique_list)
	# if len(i["name"]) < 5:
	# 	quiz_id = i["id"]
	# 	url = "http://local.school.portnov.com:4520/api/v1/quiz/{}".format(quiz_id)
	# 	r = requests.delete(url, headers=headers)
	# 	print("Quiz: {}  with id {} was permanently deleted".format(i['name'], quiz_id))
