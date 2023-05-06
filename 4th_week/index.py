### JSON 다루기 ###
# load, loads, dump, dumps
import json

"""
# JSON 문자열
json_data = '{"name": "John", "age": 30, "city": "New York"}'

# JSON 문자열을 Python 객체로 변환
data = json.loads(json_data)

# Python 객체 출력
print(data)
print(type(data))
"""

"""
# Python 객체
data = {"name": "John", "age": 30, "city": "New York"}

# Python 객체를 JSON 파일로 변환
with open("data2.json", "w") as file:
    json.dump(data, file)
"""

### requests 모듈 ###
# https://jsonplaceholder.typicode.com/posts
import requests

# response = requests.get("https://jsonplaceholder.typicode.com/posts")
# print(response.text)

data = {"title": "foo", "body": "bar", "userId": 1}
response = requests.post("https://jsonplaceholder.typicode.com/posts", data=data)
print(response.text)
print(response.status_code)
