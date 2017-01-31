import urllib.request
import json


parking_status = json.loads((urllib.request.urlopen("http://66.227.234.12:3000/parking/available").read()).decode('utf-8'))

#string = parking_status.decode('utf-8')

# parking_status = json.loads(string)

#This is the number of parking spots reported in the system
number_of_spots = (len(parking_status['result']))



available = number_of_spots

for x in range(0,number_of_spots):
    if (x == 0):
        available -= 1
        
    print (parking_status['result'][x])
    





    
print ('There are:', number_of_spots, 'spots in the system')
print ('There are:', available, 'spots available')
#print (result)





#https://api.twitter.com/1.1/statuses/mentions_timeline.json
#http://172.20.10.3:3000/parking/available/1


#172.20.10.3:3000
#/parking/1

#This is how to get all of the information on the page to display, IE the JSON package
#information = urllib.request.urlopen("http://66.227.234.12:3000/parking/available").read()
#print (information)
