import RPi.GPIO as gi
import time

gi.setmode(gi.BCM)

trig=13
echo=19

print ("start")

gi.setup(trig,gi.OUT)
gi.setup(echo, gi.IN)

while True:
    gi.output(trig, False)
    time.sleep(0.5)
    
    gi.output(trig, True)
    time.sleep(0.00001)
    gi.output(trig, False)
    
    while gi.input(echo)==0 :
        pulse_start=time.time()
        
    while gi.input(echo)==1 :
        pulse_end=time.time()
        
    pulse_du = pulse_end-pulse_start
    distance=pulse_du*17000
    distance=round(distance, 2)
    
    print (distance)