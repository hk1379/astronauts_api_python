#
# spacestation_next_visit
#

# this API tells you the next time the international space station will next pass a specific location
# this API requires two parameters, one for the lat(latitude) and one for the long(longitude) of the location


import requests
import json
from datetime import datetime

risetimes = []
times = []

# parameters for get request (London lat and long below)
parameters = {
    "lat": 51.5074,
    "lon": 0.1278
}

# get request from API
response = requests.get("http://api.open-notify.org/iss-pass.json", params = parameters)

# print json message
def jprint(obj):
    message = json.dumps(obj, sort_keys=True, indent=4)
    print(message)

# documentation states there are three keys and the third key 'response'  contains a list of pass times with risetime (pass start time)
pass_time = response.json()['response']

# getting the risetime (pass start time)
def risetime():
    for x in pass_time:
        time = x['risetime']
        risetimes.append(time)
        
risetime()

for rt in risetimes:
    time = datetime.fromtimestamp(rt)
    times.append(time)
    print(time)





