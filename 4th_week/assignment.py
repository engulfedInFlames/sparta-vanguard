import json
import requests

data = {"title": "homework", "body": "Gyeong Su Gim", "userId": 1}

response = requests.post("https://jsonplaceholder.typicode.com/posts", data=data)
result = json.loads(response.text)

with open("4th_week/result.txt", "w") as file:
    for key, value in result.items():
        file.write(f"My_{key} : {value}\n")
