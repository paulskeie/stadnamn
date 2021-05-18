import requests
import json

uri="http://localhost:6788/score"
headers = {"Content-Type": "application/json"}
data = {"texts":["","","","","Vestr","Østre"],"samplingmethod":"temperature","temperature":1.0}
data = json.dumps(data)
response = requests.post(uri, data=data, headers=headers)
print(response.json())
