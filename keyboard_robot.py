import sys,tty,termios
import RPi.GPIO as GPIO
from time import sleep

# Keyboard based robot control. 
# Based on arrow keys pressed the robot tis moved.
# Check README.md for electronic design and usage.

motorRightpin1 = 21
motorRightpin2 = 20
motorLeftpin1 = 26
motorLeftpin2 = 19
interval = 0.5
turninterval = 0.3

class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(3)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

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

def get():
        inkey = _Getch()
        while(1):
                k=inkey()
                if k!='':break
        if k=='\x1b[A':
                print "up"
		forward();
        elif k=='\x1b[B':
                print "down"
		reverse();
        elif k=='\x1b[C':
                print "right"
		right()
        elif k=='\x1b[D':
                print "left"
		left()
        else:
		if k=='rrr':
			print "rotateRight"
			rotateRight()
		elif k=='rrl':
			print "rotateLeft"
			rotateLeft()
                else :
			print "not an arrow key!"
			return True
	return False

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

def main():
	setupGPIO()
        while True:
                isExit = get()
		if isExit == True:
			break
	GPIO.cleanup()

if __name__=='__main__':
        main()
