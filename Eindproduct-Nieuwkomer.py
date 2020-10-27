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
    Vraag2 = input("Er is oorlog in jouw thuis land. Je moet vluchten, naar welk land ga je? Turkije (T) of Griekenland (G)?.")
    
    if Vraag2 == "T" or Vraag2 == "t":
        time.sleep(1)
        print("")
        print("")
        question3()
        print("")

    elif Vraag2 == "G" or Vraag2 == "g":
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
    Vraag3 = input("Je zit te denken. Ga ik verder te voet in Turkije (V) of ga ik met de vliegtuig naar Europa (E)?")

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
    Vraag4 = input("Het is 1 uur in de nacht. Ga je Turkije meer verkennen (V) of overnachten (O)?.")

    if Vraag4 == "V" or Vraag4 == "v":
        print("")
        print("")
        time.sleep(1)
        question12()

    elif Vraag4 == "O" or Vraag4 == "o":
        print("")
        print("")
        question5()

    else:
        time.sleep(0)
        question0()

def question5():
    time.sleep(1)
    print("")
    print("Je bent aan het overnachten in Turkije")
    print("")
    print("Dit is 9")

def question6():
    Vraag6 = input("Je bent nu in EU. Wil je naar 1 of 2")

    if Vraag6 == "1":
        time.sleep(1)
        print("")
        print("")
        question7()

    elif Vraag6 == "2":
        time.sleep(1)
        print("")
        print("")
        question8()

    else:
        time.sleep(1)
        question0()
    
def question7():
    print("")
    print("Dit is 1")
    print("")
    time.sleep(1)
    print("Dit is 10")
    
def question8():
    print("")
    print("Dit is 2")
    print("")
    time.sleep(1)
    print("Dit is 11")

def question9():
    Vraag9 = input("Je bent nu in Griekenland. Wil je naar 3 of naar 4? ")

    if Vraag9 == "3":
        print("")
        print("")
        question10()

    elif Vraag9 == "4":
        print("")
        print("")
        question11()
    
    else:
        time.sleep(1)
        question0()

def question10():
    time.sleep(1)
    print("Dit is 3")
    print("")
    Vraag10 = input("Dit is 5 wil je naar 6 of 7 gaan?")
    if Vraag10 == "6":
        print("")
        print("Dit is 6")

    elif Vraag10 == "7":
        print("")
        print("Dit is 7")

    else:
        question0()
    
def question11():
    print("")
    print("Dit is 4")
    print("")
    print("Dit is 12")
    print("")
    Vraag11 = input("Wil je naar 13 of 14?")

    if Vraag11 == "13":
        print("Dit is 13")
        question14()

    elif Vraag11 == "14":
        print("Dit is 14")
        question14()

    else:
        question0()
        
def question12():
    print("Je bent Turkije aan het verkennen")
    print("")
    print("Dit is 8")

def question13():
    Vraag13 = input("Je bent in de vliegtuig naar Europa. Wil je naar 1 of 2?")

    if Vraag13 == "1":
        question7()

    elif Vraag13 == "2":
        question8()

def question14():
    print("")
    print("Dit is 15")
    
question1()
main()
