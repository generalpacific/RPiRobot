import robotGPIO as robot
import sys
import termios
import tty


# This script contains logic for controlling the robot
# using keyboard arrow keys.

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


def get():
    inkey = _Getch()
    while (1):
        k = inkey()
        if k != '':
            break
    if k == '\x1b[A':
        print("up")
        robot.forward();
    elif k == '\x1b[B':
        print("down")
        robot.reverse();
    elif k == '\x1b[C':
        print("right")
        robot.right()
    elif k == '\x1b[D':
        print("left")
        robot.left()
    else:
        if k == 'rrr':
            print("rotateRight")
            robot.rotateRight()
        elif k == 'rrl':
            print("rotateLeft")
            robot.rotateLeft()
        else:
            print("not an arrow key!")
            return True
    return False


def main():
    robot.cleanUp()
    robot.setupGPIO()
    while True:
        is_exit = get()
        if is_exit == True:
            print("Exit is true.")
            break
    print("Cleaning up state.")
    robot.cleanUp()


if __name__ == "__main__":
    main()
