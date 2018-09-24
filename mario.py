from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
import time

sense = SenseHat()

X = [255, 0, 0]  # Red
O = [0, 0, 0]  # Black
F = [255, 255 ,50] # Face

mario = [
O, O, O, O, O, O, O, O,
O, O, O, X, O, O, O, O,
O, O, X, X, X, O, O, O,
O, O, O, F, O, O, O, O,
O, O, O, X, O, O, O, O,
O, O, X, X, X, O, O, O,
O, O, O, X, O, O, O, O,
O, O, X, O, X, O, O, O
]

mario_jump = [
O, O, O, X, O, O, O, O,
O, O, X, X, X, O, O, O,
O, O, O, F, O, O, O, O,
O, O, O, X, O, O, O, O,
O, O, X, X, X, O, O, O,
O, O, O, X, O, O, O, O,
O, O, X, O, X, O, O, O,
O, O, O, O, O, O, O, O
]

sense.set_pixels(mario)

def pushed_up(event):
    #Als er een actie gebeurt, wordt de pixelset verandert naar de springende mario
    #Na een seconde verandert de pixelset weer naar de gewone mario
    if event.action != ACTION_RELEASED:
        print("Jump!")
        sense.set_pixels(mario_jump)
        time.sleep(1)
        sense.set_pixels(mario)
        
        
sense.stick.direction_up = pushed_up