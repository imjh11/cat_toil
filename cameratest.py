from picamera import PiCamera

import time

camera=PiCamera()


camera.start_preview()
sleep(10)
camera.stop_preview()
