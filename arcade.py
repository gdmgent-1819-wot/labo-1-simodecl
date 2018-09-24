
from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
sense.clear()

x = 0
y = 0

c = (255,255,255)

while True:
    on_off = randint(0,1)
    if on_off < 1:
        #Pixel zowel aan linkerzijde als rechterzijde aanzetten (mirrored)
        sense.set_pixel(x,y,c)
        sense.set_pixel(7-x,y,c)
        
    x += 1
    if x > 3:
        x = 0
        y += 1
        
        if y > 7:
            y = 0
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            c = (r,g,b)
            sleep(1)
            sense.clear()