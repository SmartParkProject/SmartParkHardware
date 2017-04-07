import requests
import json

#import RPi.GPIO as GPIO #Need to check this import on the pi itself
import time

inPin = 10 #Replace x with the GPIO pin
count = 0
timeCount = 0
cars = 0
variable = 0


while 1:
    variable = raw_input("Input the senesors state: ")
    
    if variable == '1': #GPIO.input(inPin): #Checks if there is an input detected (IE a car in the way)
        count = count + 1 #This count checks to make sure it actually is detecting a car, rather than a glitch. Needs 2 consecutive ticks
        print('Count: ')
        print(count)

        if count >= 2:
            cars = cars + 1 #Adds 1 to the car count
            print('Cars: ')
            print(cars)
            count = 0

            while variable == '1': #GPIO.input(inPin): Note, during running it will check the input every time, no need to check again inside of the loop
                variable = raw_input("Input the senesors sate: ") #Not needed in PROD
                time.sleep(.2)#Need to add a catch in here so that if the button stays pressed it won't continue
            
    if variable <> '1':
        count = 0


            
        #time.sleep(.2) #In prod put this back in
        

    timeCount = timeCount + 1 #Counts the time compelted, for roughly ~4.5 mins sending data

    if timeCount == 10: #1400, should be around 4-5 mins, I think
        
        try:
            print('Sending Data')
            url = 'https://smartparkproject.tk/api/statistics/traffic'
            payload = {'cars': cars}

            r = requests.post(url, json=payload)
            #Send data and zero everything else out
            #Statement
            timeCount = 0
            cars = 0
        except:
            print('Error Sending Data')
