#import RPi.GPIO as GPIO
import time
#import turn_off
import requests
import json


#GPIO.setmode(GPIO.BCM)
count = 0

#parking_status = json.loads((urllib.request.urlopen('http://66.227.234.12:3000/parking/available').read()).decode('utf-8'))

#print (parking_status['result'][1])


pins = ([5,6,13,19,26,21,20,16])


#for x in range(0,8):
#    GPIO.setup(pins[x],GPIO.OUT)



while True:

    parking_status = json.loads(requests.get('https://smartparkproject.tk/api/lot/1/available').text)
    
    for LED in range(0,7):
        time.sleep(0.2)
        print(parking_status['result'][LED])
        #GPIO.output(pins[LED],parking_status['result'][LED])
        
    count = count + 1
    print 'count: ',count    
    time.sleep(1.0)
