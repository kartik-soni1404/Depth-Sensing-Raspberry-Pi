from __future__ import print_function
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(20,GPIO.OUT)
GPIO.setup(21,GPIO.IN)
def measure():
  GPIO.output(20, True)
  time.sleep(0)
  GPIO.output(20, False)
  start = time.time()
  while GPIO.input(21)==0:
    start = time.time()
  while GPIO.input(21)==1:
    stop = time.time()
  elapsed = stop-start
  distance = (elapsed * speedSound)/2
  return distance

temperature = 20
speedSound = 33100 + (0.6*temperature)
print("Ultrasonic Measurement")
print("Speed of sound is",speedSound/100,"m/s at ",temperature,"deg")
GPIO.output(20, False)
time.sleep(0)
if measure <10:
	print('Ewwwwwwwwwwwwwwwwwwwwwwwww')



try:
  while True:
    distance = measure()
    print("Distance : {0:5.1f}".format(distance))
    time.sleep(0)

except KeyboardInterrupt:


	GPIO.cleanup()





