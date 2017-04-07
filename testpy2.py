import requests
import json

#parking_status = json.loads(requests.get('https://smartparkproject.tk/parking/available'))
    
parking_status = json.loads(requests.get('https://smartparkproject.tk/api/lot/1/available').text)
#print(parking_status.status_code)
#print(parking_status.text)

#json_data = json.loads(parking_status.text)

print(parking_status['result'][0])
print(parking_status['result'][0])

#print(parking_status)
