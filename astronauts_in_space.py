#
# Astronaut Currently In Space API
#

#https://www.dataquest.io/blog/python-api-tutorial/

import requests
import json

# get request from API
response = requests.get("http://api.open-notify.org/astros.json")

# status code obtained
status_code = response.status_code
print(f'Status Code = {status_code}')

# response taken in a json format
message = response.json()

# printing names of astronauts
def names():
    for dict in message['people']:
        print (dict['name'])

#printing json object
def json_print(obj):
    #create a formated string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=5)
    print(text)

json_print(message)
