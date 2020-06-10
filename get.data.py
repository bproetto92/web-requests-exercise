# get_data.py

print("REQUESTING SOME DATA FROM THE INTERNET...")
import json
import requests

#Part 1
request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products/2.json"
response = requests.get(request_url)
response_data = json.loads(response.text)


print(response_data["name"])

#Part 2
request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/products.json"
response2 = requests.get(request_url)
response_data2 = json.loads(response2.text)

for x in response_data2:
    print(x["id"],x["name"])

#Part 3 
request_url = "https://raw.githubusercontent.com/prof-rossetti/intro-to-python/master/data/gradebook.json"
response3 = requests.get(request_url)
response_data3 = json.loads(response3.text)

grades = []
students = response_data3["students"]
for x in students:
    grades.append(x["finalGrade"])

print(max(grades))