import RPi.GPIO as gi
import time

gi.setmode(gi.BCM)

trig=13 #setting GPIO pin 
echo=19

ismoving=False #true if movement is dected

listfordis=[] #list for store recent values of distance 

gi.setup(trig,gi.OUT)
gi.setup(echo, gi.IN)

def detectmove (ToF):
    while True:
    gi.output(trig, False) # make sure ultrasonic is turned off
    time.sleep(0.5)
    
    gi.output(trig, True)# activate ultrasonic  and trun off
    time.sleep(0.00001)
    gi.output(trig, False)
    
    while gi.input(echo)==0 :
        pulse_start=time.time()
        
    while gi.input(echo)==1 :
        pulse_end=time.time()
        
    pulse_du = pulse_end-pulse_start # get RETURN TIME OF ULTRASONIC 
    
    
    distance=pulse_du*17000
    distance=round(distance, 2) #get actual distance from travle time of ultrasonic
    
    if len(listfordis)==3:
        listfordis.pop(0)
        listfordis.append(distance) # add new value to list and remove old one
        avg=sum(listfordis)/3  # get average value for compare 
        if avg>=min(listfordis)+1 or avg<=max(listfordis)-1: 
            ismoving=True # there is a movement if min value is too small or max value is too big
        else :
            ismoving=False
    else :
        listfordis.append(distance) # do not calculte movement if list is not filled. 
    if ToF :
        if ismoving:
            return
    else:
        if not ismoving :
            return
