import movedetect as mvd
import time

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
        camera.stop_recording() #will end when move is not detected
        endtime=datetime.now().strftime("%y-%m-%d %H-%M-%S")
        end=time.time()
        length=str(start-end)
        logoutput=starttime + ' ' + endtime + ' ' + length + '\n'
        log=open('/home/pi/record/log.txt','a')
        log.write(logoutput)
        log.close()


