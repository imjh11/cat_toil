import time
import picamera
import movedetect


with picamera.PiCamera() as camera:
    while True:
        movedetect.detectmove(True) #will end when move is detected
        print ("start")
        camera.start_recording('/home/pi/Desktop/video.h264')
        time.sleep(1)
        movedetect.detectmove(False)
        print("stop")
        camera.stop_recording() #will end when move is not detected
    