from sense_hat import SenseHat
import time
from random import randint

sense = SenseHat()

#Letters in array zetten om te kunnen gebruiken in de loop
letters = ["N","M","D"]

i = 0
while i < len(letters):
    #Array doorlopen en willekeurige kleur meegeven
    sense.show_letter(letters[i], text_colour=[randint(0,256),randint(0,256),randint(0,256)])
    print(i)
    i = i + 1
    #Na iedere loop een seconde pauzeren
    time.sleep(1)
    if i > 2:
        i = 0