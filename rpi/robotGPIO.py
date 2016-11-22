import RPi.GPIO as GPIO
from time import sleep

# Module for core logic for controlling the GPIO functions
# and functions to navigate the robot

motorRightpin1 = 21
motorRightpin2 = 20
motorLeftpin1 = 26
motorLeftpin2 = 19
interval = 0.5 
turninterval = 0.3 

def forwardMotorRight():
  GPIO.output(motorRightpin1, GPIO.HIGH)
  GPIO.output(motorRightpin2, GPIO.LOW)

def stopMotorRight():
  GPIO.output(motorRightpin1, GPIO.LOW)
  GPIO.output(motorRightpin2, GPIO.LOW)

def forwardMotorLeft():
  GPIO.output(motorLeftpin1, GPIO.HIGH)
  GPIO.output(motorLeftpin2, GPIO.LOW)

def stopMotorLeft():
  GPIO.output(motorLeftpin1, GPIO.LOW)
  GPIO.output(motorLeftpin2, GPIO.LOW)

def reverseMotorRight():
  GPIO.output(motorRightpin2, GPIO.HIGH)
  GPIO.output(motorRightpin1, GPIO.LOW)

def reverseMotorLeft():
  GPIO.output(motorLeftpin2, GPIO.HIGH)
  GPIO.output(motorLeftpin1, GPIO.LOW)

def right():
  forwardMotorLeft()
  sleep(turninterval)
  stopMotorLeft()

def left():
  forwardMotorRight()
  sleep(turninterval)
  stopMotorRight()

def reverse():
  reverseMotorRight()
  reverseMotorLeft()
  sleep(interval)
  stopMotorRight()
  stopMotorLeft()

def forward():
  forwardMotorRight()
  forwardMotorLeft()
  sleep(interval)
  stopMotorRight()
  stopMotorLeft()

def rotateRight():
  reverseMotorRight()
  forwardMotorLeft()
  sleep(interval)
  stopMotorRight()
  stopMotorLeft()

def rotateLeft():
  forwardMotorRight()
  reverseMotorLeft()
  sleep(interval)
  stopMotorRight()
  stopMotorLeft()

def setupGPIO():
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(motorRightpin1, GPIO.OUT)
  GPIO.setup(motorRightpin2, GPIO.OUT)
  GPIO.setup(motorLeftpin1, GPIO.OUT)
  GPIO.setup(motorLeftpin2, GPIO.OUT)
  GPIO.output(motorRightpin1, GPIO.LOW)
  GPIO.output(motorRightpin2, GPIO.LOW)
  GPIO.output(motorLeftpin1, GPIO.LOW)
  GPIO.output(motorLeftpin2, GPIO.LOW)

def cleanUp():
  GPIO.cleanup()
