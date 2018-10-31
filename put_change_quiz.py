import requests
import json

url = "http://local.school.portnov.com:4520/api/v1/quiz"

payload = { 
      "name": "Demo Quiz 10/30/2018", 
      "totalScore": 18, 
      "passingPercentage": 75, 
      "showStopperQuestion": 1, 
      "questions": [ 
        { 
          "type": "TEXTUAL", 
          "question": "What is your name?", 
          "score": 5 
        }, 
        { 
          "type": "SINGLE_CHOICE", 
          "question": "Which city is city largest in California?", 
          "score": 7, 
          "answer": 2, 
          "hasOtherOption": False, 
          "options": [ 
            "San Francisco", 
            "Sacramento", 
            "Los Angeles", 
            "Redding" 
          ] 
        }, 
        { 
          "type": "MULTIPLE_CHOICE", 
          "question": "Who was apple founded by?", 
          "score": 6, 
          "answers": [ 
            0, 
            1, 
            2 
          ], 
          "hasOtherOption": True, 
          "options": [ 
            "Steve Jobs", 
            "Steve Wozniak", 
            "Ronald Wayne", 
            "Ronald Reagan" 
          ] 
        } 
      ],
      "id": 2001 
    }

headers = {
    'content-type': "application/json",
    'Authorization': "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6ImFsaW5hLmtvcm9sZXZpY2hAeW9wbWFpbC5jb20iLCJpYXQiOjE1NDA5Mzk1MTUsImV4cCI6MTU0MTAyNTkxNX0.JR-XK-Z9QqgDUv7H4-rqw9BYDjyv6Uf-7EavRgxXodA"
    }

response = requests.put(url, data=json.dumps(payload), headers=headers)

print(response.text)

