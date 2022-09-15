# Add your Python code here. E.g.

from microbit import *
import speech
import random

lengtewoordArray = 3

onderwerp = ["Jamie", "Piet", "Steve"]
werkwoord = ["walks", "learns", "drinks"]
rest = ["hard", "at school", "water"]

def sayTheWords1(word):
    print(word)
    speech.say(word, speed=120, pitch=100, throat=100, mouth=200)
    sleep(500)
    
def sayTheWords2():
    willekeurigeGetal = random.randint(0, lengtewoordArray - 1)
    display.show(willekeurigeGetal)
    sayTheWords1(onderwerp[willekeurigeGetal])
    sayTheWords1(werkwoord[willekeurigeGetal])
    sayTheWords1(rest[willekeurigeGetal])
    
while True:
    if button_a.is_pressed():
        display.show(Image.Happy)
        sayTheWords1("hallo i am happy")
    elif button_b.is_pressed():
        display.show(Image.Sad)
        sayTheWords1("why are you sad")
    elif display.read_light_level() < 40:
        sayTheWords2()
    else:
        display.show(Image.SQUARE)