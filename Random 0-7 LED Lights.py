import RPi.GPIO as GPIO
import time
import turn_off
import urllib.request
import json
import random

GPIO.setmode(GPIO.BCM)
random.seed()




pins = ([5,6,13,19,26,21,20,16])
state = ([0,0,0,0,0,0,0,0])



print ('here')


for x in range(0,8):
    GPIO.setup(pins[x],GPIO.OUT)





while True:
    LED = random.randint(0,7)
    
    time.sleep(0.1)
    
    if (state[LED] == 0):
        state[LED] = 1
    else:
        state[LED] = 0

        
    GPIO.output(pins[LED],state[LED])
        



    
