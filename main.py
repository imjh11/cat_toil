import movedetect as mvd
import time
import picamera
from datetime import datetime


with picamera.PiCamera() as camera:
    while True:
        mvd.detectmove(True) #will end when move is detected
        print ("start")
        start=time.time()
        starttime=datetime.now().strftime("%y-%m-%d %H-%M-%S")
        filename=starttime + '.h264'
        filepath='/home/pi/record/' + filename 
        camera.start_recording(filepath)
        time.sleep(1)
        mvd.detectmove(True)
        print("stop")
        camera.stop_recording() #will end when move is detected again
        endtime=datetime.now().strftime("%y-%m-%d %H-%M-%S")
        end=time.time()
        length=int(end-start)
        if length > 120 or length < 10: #warn too short or too long usage
            logoutput=starttime + ' ' + endtime + ' ' + str(length) + ' seconds ' + 'Warning!'+ '\n' + '\n'
        else:
            logoutput=starttime + ' ' + endtime + ' ' + str(length) + ' seconds' + '\n' + '\n'    
        log=open('/home/pi/record/log.txt','a')
        log.write(logoutput)
        log.close()