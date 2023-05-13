
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set the pin 17 to output mode
GPIO.setup(17, GPIO.OUT)

# Turn off pin 17
GPIO.output(17, GPIO.LOW)
