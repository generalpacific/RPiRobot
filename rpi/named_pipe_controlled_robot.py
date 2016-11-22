import robotGPIO as robot
import os, sys
import atexit

# Module to get the inputs from a named Pipe

FIFOPIPE = "/tmp/robotpipe"

def setupPipe():
  os.mkfifo(FIFOPIPE)
  print "Pipe Created: " + FIFOPIPE
  while True:
    fifo = open(FIFOPIPE, 'r')
    line = fifo.readline()
    print "Read: " + line
    if line == "f":
      robot.forward()
    elif line == "b":
      robot.reverse()
    elif line == "r":
      robot.right()
    elif line == "l":
      robot.left()
    elif line == "rr":
      robot.rotateRight()
    elif line == "rl":
      robot.rotateLeft()
    else :
      print "not a valid action"

def main(): 
  robot.setupGPIO()
  setupPipe()

@atexit.register
def cleanup():
  print "Cleaning up after"
  try:
    GPIO.cleanup()
    os.unlink(FIFOPIPE)
  except:
    print "Error while unlinking"
    pass

if __name__=='__main__':
  main()
