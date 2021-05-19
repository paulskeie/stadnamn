import requests
import json

uri="http://localhost:6788/score"
headers = {"Content-Type": "application/json"}
seeds=["","","","","Vestr","Østre"]
data = {"texts":seeds,"samplingmethod":"temperature","temperature":1.0}
data = json.dumps(data)
# Formatting a markdown table
print(' | '+' | '.join(seeds))
# Header separator
print(' | '+' | '.join(['--------' for i in range(len(seeds))]))
# Number of times to hit the API
n = 10
# Looping over n rows
for i in range(n):
    response = requests.post(uri, data=data, headers=headers)
    placenames=json.loads(response.json())['placenames']
    print(' | '+' | '.join(placenames))


