from sense_hat import SenseHat
import time
from random import randint

sense = SenseHat()

O = [0, 0, 0]  # Black
pixels = [
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
]
sense.set_pixels(pixels)

i = 0
while True:
    #i staat voor index, p staat voor de pixel value (de value moet niet opgeroepen worden)
    for i, p in enumerate(pixels):
        pixels[i-1] = O
        pixels[i] = [randint(0,255), randint(0,255), randint(0,255)]
        sense.set_pixels(pixels)
        time.sleep(0.2)
        i + 1
        if i > 63:
            i = 0
    
sense.clear()