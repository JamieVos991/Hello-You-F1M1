Introductie = ('Hallo Dit is mijn eindproduct gebasseerd over het verhaal Zafel. De Syrische dichter Zafer deelt zijn aangrijpende vluchtverhaal op basis- en middelbare scholen. Die voorlichtingslessen verzorgt hij samen met vrijwilliger Harry, die inmiddels naadloos is ingespeeld op Zafers bijzondere en beeldende vertellingen. ''Ik wil dat leerlingen echt ervaren hoe angst, vluchten en hoop voelt.')

import time

print("")

print(Introductie)

print("")
        
def question0():
    print("")
    Vraag0 = input("Je bent bij een onbekend zone. ")

def question1():
    Vraag1 = input("Wil je graag naar het volgende Stukje (A) of stoppen (B). ")

    if Vraag1 == "A" or Vraag1 == "a":
        time.sleep(1)
        print("")
        print("")
        question2()
        print("")

    elif Vraag1 == "B" or Vraag1 == "b":
        print("")
        print("")
        question50()
        print("")

    else:
        time.sleep(1)
        print("")
        print("Onbekend toets ingevuld :(")
        question0()

def question2():
    Vraag2 = input("Er is oorlog in jouw thuis land. Je moet vluchten, naar welk land ga je? Turkije (T) of Griekenland (G)?. ")
    
    if Vraag2 == "T" or Vraag2 == "t":
        time.sleep(1)
        print("")
        print("")
        question3()
        print("")

    elif Vraag2 == "G" or Vraag2 == "g":
        time.sleep(1)
        print("")
        print("")
        question9()
        print("")

    else:
        print("")
        print("")
        print("Onbekend Toets Ingevuld :(")
        question0()


def question3():
    Vraag3 = input("Je zit te denken. Ga ik verder te voet in Turkije (V) of ga ik met de vliegtuig naar Europa (E)? ")

    if Vraag3 == "V" or Vraag3 == "v":
        time.sleep(1)
        print("")
        print("")
        question4()
        
    elif Vraag3 == "E" or Vraag3 == "e":
        time.sleep(1)
        print("")
        print("")
        question13()

    else:
        time.sleep(1)
        question0()

def question4():
    Vraag4 = input("Het is 1 uur in de nacht. Ga je Turkije meer verkennen (V) of overnachten (O)?. ")

    if Vraag4 == "V" or Vraag4 == "v":
        print("")
        print("")
        time.sleep(1)
        question12()

    elif Vraag4 == "O" or Vraag4 == "o":
        question5()

    else:
        time.sleep(0)
        question0()

def question5():
    time.sleep(1)
    print("")
    print("Je bent aan het overnachten in Turkije")
    print("")
    print("Onbekende mensen zien jullie en bellen de politie.")

def question6():
    Vraag6 = input("Je bent nu in EU. Wil je naar Nederland (N) of Polen (P)? ")

    if Vraag6 == "N" or Vraag6 == "n":
        time.sleep(1)
        print("")
        print("")
        question7()

    elif Vraag6 == "P" or Vraag6 == "P":
        time.sleep(1)
        print("")
        print("")
        question8()

    else:
        time.sleep(1)
        question0()
    
def question7():
    print("")
    print("")
    print("Welkom in Nederland")
    print("")
    time.sleep(1)
    print("Je komt in Nederland Terecht")
    
def question8():
    print("")
    print("")
    print("Welkom in Polen")
    print("")
    time.sleep(1)
    print("Je komt in Polen terecht ")

def question9():
    Vraag9 = input("Je bent nu in Griekenland. Wil je met de boot (B) of ga je lopend naar Griekenland (L) ")

    if Vraag9 == "B" or Vraag9 == "b":
        print("")
        print("")
        question10()

    elif Vraag9 == "L" or Vraag9 == "l":
        print("")
        print("")
        question11()
    
    else:
        time.sleep(1)
        question0()

def question10():
    time.sleep(1)
    print("Met de boot")
    print("")
    Vraag10 = input("Je bent nu met de boot naar Griekenland. Wil je naar het NO (O) of NW (W)? ")
    if Vraag10 == "O" or Vraag10 == "o":
        print("")
        print("Je gaat nu naar het Noord oosten")

    elif Vraag10 == "W" or Vraag10 == "w":
        print("")
        print("Je gaat nu naar het Noordwesten")

    else:
        question0()
    
def question11():
    print("")
    print("Dit is 4")
    print("")
    print("Dit is 12")
    print("")
    Vraag11 = input("Wil je naar 13 of 14? ")

    if Vraag11 == "13":
        print("")
        print("Dit is 13")
        question14()

    elif Vraag11 == "14":
        print("")
        print("Dit is 14")
        question14()

    else:
        question0()
        
def question12():
    print("Je bent Turkije aan het verkennen ")
    print("")
    print("Iemand ziet jullie en je wordt weggestuurd")

def question13():
    Vraag13 = input("Je bent in de vliegtuig naar Europa. Wil je naar Polen (P) of Nederland (N)? ")

    if Vraag13 == "P" or Vraag13 == "p":
        question8()

    elif Vraag13 == "N" or Vraag13 == "n":
        question7()

def question14():
    print("")
    time.sleep(2)
    print("Dit is 15")
    
question1()
