# JSON - JavaScript Object Notation : Raw Data returned from API after sending the HTTP request
# API - Application Programming Interface

# JSON format: Mixed of lists and dictionaries

import requests

response = requests.get("http://api.open-notify.org/astros.json")
json = response.json()

print(json)

for person in json['people']:
    print(person['name'])