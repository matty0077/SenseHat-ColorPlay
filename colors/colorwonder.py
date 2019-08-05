import sys
sys.path.append("/home/pi/Desktop/NAVI/WANDER_LUST")
import random
from random import randint
import time
from sense_hat import SenseHat
sense=SenseHat()
sense.set_rotation(90)
sense.clear()

blue=(0,0,255)
yellow=(255,255,0)
red = (255, 0, 0)
white=(255,255,255)
black=(0,0,0)
green = (0, 255, 0)

#solids

r = 255#change shades according to mood
g = 0
b = 0
colour_value = 0
#cycle
rr=0
gg=0
bb=0

pixels = [
    [255, 0, 0], [255, 0, 0], [255, 87, 0], [255, 196, 0], [205, 255, 0], [95, 255, 0], [0, 255, 13], [0, 255, 122],
    [255, 0, 0], [255, 96, 0], [255, 205, 0], [196, 255, 0], [87, 255, 0], [0, 255, 22], [0, 255, 131], [0, 255, 240],
    [255, 105, 0], [255, 214, 0], [187, 255, 0], [78, 255, 0], [0, 255, 30], [0, 255, 140], [0, 255, 248], [0, 152, 255],
    [255, 223, 0], [178, 255, 0], [70, 255, 0], [0, 255, 40], [0, 255, 148], [0, 253, 255], [0, 144, 255], [0, 34, 255],
    [170, 255, 0], [61, 255, 0], [0, 255, 48], [0, 255, 157], [0, 243, 255], [0, 134, 255], [0, 26, 255], [83, 0, 255],
    [52, 255, 0], [0, 255, 57], [0, 255, 166], [0, 235, 255], [0, 126, 255], [0, 17, 255], [92, 0, 255], [201, 0, 255],
    [0, 255, 66], [0, 255, 174], [0, 226, 255], [0, 117, 255], [0, 8, 255], [100, 0, 255], [210, 0, 255], [255, 0, 192],
    [0, 255, 183], [0, 217, 255], [0, 109, 255], [0, 0, 255], [110, 0, 255], [218, 0, 255], [255, 0, 183], [255, 0, 74]
]

msleep = lambda x: time.sleep(x / 1000.0)

class ColorWonder:
    def next_colour(self,pix):
        r = pix[0]
        g = pix[1]
        b = pix[2]

        if (r == 255 and g < 255 and b == 0):
            g += 1

        if (g == 255 and r > 0 and b == 0):
            r -= 1

        if (g == 255 and b < 255 and r == 0):
            b += 1

        if (b == 255 and g > 0 and r == 0):
            g -= 1

        if (b == 255 and r < 255 and g == 0):
            r += 1

        if (r == 255 and b > 0 and g == 0):
            b -= 1

        pix[0] = r
        pix[1] = g
        pix[2] = b

    def rainbow(self):
        running=True
        while True:
            try:
                if running==True:
                    for pix in pixels:
                        self.next_colour(pix)

                    sense.set_pixels(pixels)
                    msleep(.75)#thread manual
            except KeyboardInterrupt:
                sense.clear()
                #import Saving_Grace
                sys.exit()    
#////////////////////////////////rando
    def Rando(self):
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
                #import Saving_Grace
                sys.exit()
#//////////////solids
    def next_colour(self):
        global r
        global g
        global b

        if (r == 255 and g < 255 and b == 0):
            g += 1

        if (g == 255 and r > 0 and b == 0):
            r -= 1

        if (g == 255 and b < 255 and r == 0):
            b += 1

        if (b == 255 and g > 0 and r == 0):
            g -= 1

        if (b == 255 and r < 255 and g == 0):
            r += 1

        if (r == 255 and b > 0 and g == 0):
            b -= 1

    def Solids(self):
        while True:
            try:
                sense.clear([r, g, b])
                msleep(2)
                self.next_colour()
            except KeyboardInterrupt:
                sense.clear()
                #import Saving_Grace
                sys.exit()
#/////////////color cycles
    def TrueColors(self):
        global colour_value,rr,gg,bb
        while colour_value < 16581375:
            print (colour_value)   
            O = [rr, gg, bb]
            rgb_showcase = [
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O,
                O, O, O, O, O, O, O, O
                ]
            sense.set_pixels(rgb_showcase)
            colour_value =colour_value + 1
            rr = rr+1
           
            if rr == 255:
               rr = 0
               gg = gg+5
            if gg == 255:
               gg = 0
               bb = bb+5
            if bb == 255:
               rr=0
               gg=0
               bb=0
            
            sense.set_pixels(rgb_showcase)

        else:
            sense.show_message("You have reached " + str(colour_value), text_colour=[255, 255, 255])
            
#///////////////////////////timed colors
#msleep = lambda x: time.sleep(x / 1000.0)
    def Solidus(self):
        timer=255
        def next_colour():
            global r
            global g
            global b

            if (r == 255 and g < 255 and b == 0):
                g += 1

            if (g == 255 and r > 0 and b == 0):
                r -= 1

            if (g == 255 and b < 255 and r == 0):
                b += 1

            if (b == 255 and g > 0 and r == 0):
                g -= 1

            if (b == 255 and r < 255 and g == 0):
                r += 1

            if (r == 255 and b > 0 and g == 0):
                b -= 1

        while True:
            if timer>0:
                timer-=1
                try:
                    sense.clear([r, g, b])
                    msleep(.25)#2
                    next_colour()
                except KeyboardInterrupt:
                    sense.clear()
                    import Saving_Grace
                    sys.exit()
            else:
                sense.clear()
                break
#//////////////////////////
    def TRando(self):
        timer=35
        while True:
            if timer>0:
                timer-=1
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
                    import Saving_Grace
                    sys.exit()
            else:
                sense.clear()
                break

        
C=ColorWonder()
#C.Solidus()
#C.TRando()
#C.rainbow()
#C.Rando()
#C.Solids()
#C.TrueColors()
