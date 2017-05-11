from twitter import *
import random
import numpy
import datetime
import RPi.GPIO as GPIO
import time

twitter = Twitter(auth=OAuth(
token="", token_secret="", consumer_key="", consumer_secret=""))

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)

# Define GPIO to use on Pi
GPIO_PIR = 7


# Set pin as input
GPIO.setup(GPIO_PIR,GPIO.IN)      # Echo

Current_State  = 0
Previous_State = 0

#grabs random number
RandNum = random.randrange(0, 16)

#array for all the tweets
TheTweets = ["1", "2", "3"]

try:

  print "Waiting for PIR to settle ..."

  # Loop until PIR output is 0
  while GPIO.input(GPIO_PIR)==1:
    Current_State  = 0

  print "  Ready"

  # Loop until users quits with CTRL-C
  while True :

    # Read PIR state
    Current_State = GPIO.input(GPIO_PIR)

    if Current_State==1 and Previous_State==0:
      # PIR is triggered
      print "  Motion detected!"
      c = str(datetime.datetime.now().time())

	  # Now work with Twitter
      twitter.statuses.update(status = TheTweets[RandNum] + " --- Timestamp " + c[:8])
      # Record previous state
      Previous_State=1
    elif Current_State==0 and Previous_State==1:
      # PIR has returned to ready state
      print "  Ready"
      Previous_State=0

    # Wait for 10 milliseconds
    time.sleep(0.01)

except KeyboardInterrupt:
  print "  Quit"
  # Reset GPIO settings
  GPIO.cleanup()














