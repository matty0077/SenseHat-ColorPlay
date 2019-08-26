import sys
import random
from random import randint
import time
from sense_hat import SenseHat
sense=SenseHat()
sense.clear()

while True:
    try:
        x = randint(0, 7)
        y = randint(0, 7)
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        sense.set_pixel(x, y, r, g, b)
        time.sleep(0.01)
    except KeyboardInterrupt:
        sense.clear()
        sys.exit()
