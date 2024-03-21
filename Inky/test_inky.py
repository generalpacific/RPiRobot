from inky.auto import auto
from inky import InkyPHAT
import inky

# Setup auto display
display = auto()

# Set colour to RED
colour = inky.RED
display.set_border(colour)

display.show()
