from __future__ import print_function
import RPi.GPIO as GPIO
import time
import os
def BACK():
    os.system('python rightback.py') 
    os.system('python leftback.py') 
def measure():

  GPIO.output(GPIO_TRIGGER, True)

  time.sleep(0.00001)
  GPIO.output(GPIO_TRIGGER, False)
  start = time.time()
  
  while GPIO.input(GPIO_ECHO)==0:
    start = time.time()

  while GPIO.input(GPIO_ECHO)==1:
    stop = time.time()

  elapsed = stop-start
  distance = (elapsed * speedSound)/2

  return distance

GPIO.setmode(GPIO.BCM)


GPIO_TRIGGER = 20
GPIO_ECHO    = 21


temperature = 20
speedSound = 33100 + (0.6*temperature)



GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO,GPIO.IN)      # Echo

GPIO.output(GPIO_TRIGGER, False)

time.sleep(0.5)

try:
  while True:
    distance = measure()
    print("Distance : {0:5.1f}".format(distance))
    time.sleep(1)
    if distance < 20:
    print ("YESSSSSSSSSSSSSSSSS")
	command=BACK
    else:
	print("NONOONOn")

except KeyboardInterrupt:
  GPIO.cleanup()