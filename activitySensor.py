import urllib.request
import json

import RPi.GPIO as GPIO
import time



inPin = x #Replace x with the GPIO pin
count = 0
timeCount = 0
cars = 0
   

while true:
    
    if GPIO.input(inPin): #Checks if there is an input detected (IE a car in the way)
        count = count + 1 #This count checks to make sure it actually is detecting a car, rather than a glitch. Needs 2 consecutive ticks

        if count >= 2:
            cars = cars + 1 #Adds 1 to the car count
            count = 0

            while GPIO.input(inPin):
                time.sleep(.2)#Need to add a catch in here so that if the button stays pressed it won't continue

    if !GPIO.input(inPin):
        count = 0

            
        time.sleep(.2)
        

    timeCount = timeCount + 1 #Counts the time compelted, for roughly ~4.5 mins sending data

    if timeCount == 1400:
        
        try:
            url = 'https://smartparkproject.tk/api/statistics/traffic'
            payload = {'cars': cars, 'lot':1}

            r = requests.post(url, json=payload)
            #Send data and zero everything else out
            #Statement
            timeCount = 0
            cars = 0
            count = 0
        except:
            print('Error Sending Data')
