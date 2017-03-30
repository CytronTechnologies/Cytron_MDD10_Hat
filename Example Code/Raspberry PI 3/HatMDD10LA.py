#This programe used to demonstare how to use Loch Antiphase with Hat-MDD10
#AN pin will act as sterring to control direction
#DIG pin will act to ON/OFF motor output.

import RPi.GPIO as GPIO			# using Rpi.GPIO module
from time import sleep			# import function sleep for delay
GPIO.setmode(GPIO.BCM)			# GPIO numbering
GPIO.setwarnings(False)			# enable warning from GPIO
AN2 = 13				# set pwm2 pin on MD10-Hat
AN1 = 12				# set pwm1 pin on MD10-hat
DIG2 = 24				# set dir2 pin on MD10-Hat
DIG1 = 26				# set dir1 pin on MD10-Hat
GPIO.setup(AN2, GPIO.OUT)		# set pin as output
GPIO.setup(AN1, GPIO.OUT)		# set pin as output
GPIO.setup(DIG2, GPIO.OUT)		# set pin as output
GPIO.setup(DIG1, GPIO.OUT)		# set pin as output
sleep(1)				# delay for 1 seconds
p1 = GPIO.PWM(DIG1, 100)		# set pwm for M1
p2 = GPIO.PWM(DIG2, 100)		# set pwm for M2

try:					
  while True:

   print "Forward"			# display "Forward" when programe run
   GPIO.output(AN1, GPIO.HIGH)		# set AN1 as HIGH, M1B will turn ON
   GPIO.output(AN2, GPIO.HIGH)		# set AN2 as HIGH, M2B will turn ON
   p1.start(0)				# set Direction for M1
   p2.start(0)				# set Direction for M2  
   sleep(2)				#delay for 2 second

   print "Left"
   GPIO.output(AN1, GPIO.HIGH)         
   GPIO.output(AN2, GPIO.HIGH)         
   p1.start(100)                       
   p2.start(100)                       
   sleep(2)                            

   print "Right"
   GPIO.output(AN1, GPIO.HIGH)       
   GPIO.output(AN2, GPIO.HIGH)       
   p1.start(0)                       
   p2.start(100)                     
   sleep(2)                          

   print "Backward"
   GPIO.output(AN1, GPIO.HIGH)       
   GPIO.output(AN2, GPIO.HIGH)       
   p1.start(100)                     
   p2.start(0)                       
   sleep(2)                          

   print "STOP"
   GPIO.output(AN1, GPIO.LOW)           # set AN1 as LOW, M1B will STOP
   GPIO.output(AN2, GPIO.LOW)           # set AN2 as HIGH, M2B will STOP
   p1.start(0)                          # Direction can ignore
   p2.start(0)                          # Direction can ignore
   sleep(3)                             #delay for 3 second


except:					# exit programe when keyboard interupt
   p1.start(0)				# set speed to 0
   p2.start(0)				# set speed to 0
					# Control+X to save and exit
						

