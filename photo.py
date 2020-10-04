from picamera import PiCamera
from time import sleep
from datetime import datetime
camera = PiCamera()

camera.resolution = (1920, 1080)
camera.rotation = 180
camera.annotate_text = f'{datetime.now()}'
camera.annotate_text_size = 160
camera.start_preview() 
sleep(1)
camera.capture(f"./image_{datetime.now()}.jpg")
camera.stop_preview()