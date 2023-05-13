import RPi.GPIO as GPIO
from time import sleep

# Module for core logic for controlling the GPIO functions
# and functions to navigate the robot

motorRightOut1 = 21
motorRightOut2 = 20
motorLeftOut1 = 26
motorLeftOut2 = 19

# Interval between each forward and backward activations. 
interval = 0.5

# Interval between each right / left activations. 
# Eventually controls how much the robot turns for each command.
turninterval = 0.3


def forwardMotorRight():
    GPIO.output(motorRightOut1, GPIO.HIGH)
    GPIO.output(motorRightOut2, GPIO.LOW)


def stopMotorRight():
    GPIO.output(motorRightOut1, GPIO.LOW)
    GPIO.output(motorRightOut2, GPIO.LOW)


def forwardMotorLeft():
    GPIO.output(motorLeftOut1, GPIO.HIGH)
    GPIO.output(motorLeftOut2, GPIO.LOW)


def stopMotorLeft():
    GPIO.output(motorLeftOut1, GPIO.LOW)
    GPIO.output(motorLeftOut2, GPIO.LOW)


def reverseMotorRight():
    GPIO.output(motorRightOut2, GPIO.HIGH)
    GPIO.output(motorRightOut1, GPIO.LOW)


def reverseMotorLeft():
    GPIO.output(motorLeftOut2, GPIO.HIGH)
    GPIO.output(motorLeftOut1, GPIO.LOW)


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
    GPIO.setup(motorRightOut1, GPIO.OUT)
    GPIO.setup(motorRightOut2, GPIO.OUT)
    GPIO.setup(motorLeftOut1, GPIO.OUT)
    GPIO.setup(motorLeftOut2, GPIO.OUT)
    GPIO.output(motorRightOut1, GPIO.LOW)
    GPIO.output(motorRightOut2, GPIO.LOW)
    GPIO.output(motorLeftOut1, GPIO.LOW)
    GPIO.output(motorLeftOut2, GPIO.LOW)


def cleanUp():
    GPIO.cleanup()
