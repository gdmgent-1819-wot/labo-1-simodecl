from sense_hat import SenseHat
import time
from random import randint

sense = SenseHat()

letters = "NMD"

#While loop altijd laten doorlopen
while True:
    for letter in letters:
        #Array doorlopen en willekeurige kleur meegeven
        sense.show_letter(letter, text_colour=[randint(0,255),randint(0,255),randint(0,255)])
        #Na iedere loop een seconde pauzeren
        time.sleep(1)