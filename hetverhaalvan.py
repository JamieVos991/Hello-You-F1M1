Introductie = ('Hallo Dit is mijn eindproduct gebasseerd over het verhaal Zafel. De Syrische dichter Zafer deelt zijn aangrijpende vluchtverhaal op basis- en middelbare scholen. Die voorlichtingslessen verzorgt hij samen met vrijwilliger Harry, die inmiddels naadloos is ingespeeld op Zafers bijzondere en beeldende vertellingen. ''Ik wil dat leerlingen echt ervaren hoe angst, vluchten en hoop voelt.')

import time
import os 

def main():

    print("")

    os.system("cls")
    print(Introductie)

    print("")

    def question50():
        Repeat = input("Wil je opnieuw beginnen (A) of stoppen (B)? ")

        if Repeat == "A" or Repeat == "a":
            main()
        
        elif Repeat == "B" or Repeat == "b":
            print("")
            print("OKI, DOEI")
            exit()

        else:
            print("")
            print("Niks ingevuld...")
            question50()

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
            print("Onbekend toets ingevuld :( ")
            print("")
            question1()

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
            question2()


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
            question3()

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
            question4()

    def question5():
        time.sleep(1)
        print("")
        print("Je bent aan het overnachten in Turkije")
        time.sleep(1)
        print("")
        print("Onbekende mensen zien jullie en bellen de politie.")
        time.sleep(1)
        print("")
        print("")
        print("Je hebt een verkeerde keus gemaakt. Game Over ")
        print("")
        question50()

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
            question6()
        
    def question7():
        print("")
        print("Welkom in Nederland")
        print("")
        time.sleep(1)
        print("Je komt in Nederland Terecht")
        print("")
        print("")
        time.sleep(1)
        print("Gefeliciteerd, je hebt 1 van de goedde eindes gevonden. ")
        question50()
        
    def question8():
        print("")
        print("Welkom in Polen")
        print("")
        time.sleep(1)
        print("Je komt in Polen terecht ")
        print("")
        print("")
        time.sleep(1)
        print("Je hebt een verkeerde keus gemaakt. Game Over ")
        question50()

    def question9():
        Vraag9 = input("Je bent nu in Griekenland. Wil je met de boot (B) of ga je lopend naar Griekenland (L) ")

        if Vraag9 == "B" or Vraag9 == "b":
            print("")
            print("")
            time.sleep(1)
            question10()

        elif Vraag9 == "L" or Vraag9 == "l":
            print("")
            print("")
            time.sleep(1)
            question11()
        
        else:
            time.sleep(1)
            question9()

    def question10():
        time.sleep(1)
        print("Met de boot")
        print("")
        Vraag10 = input("Je bent nu met de boot naar Griekenland. Wil je naar het NO (O) of NW (W)? ")
        if Vraag10 == "O" or Vraag10 == "o":
            print("")
            print("Je gaat nu naar het Noord oosten")
            print("")
            question15()
            

        elif Vraag10 == "W" or Vraag10 == "w":
            print("")
            print("Je gaat nu naar het Noordwesten")
            print("")
            question15()

        else:
            question10()
        
    def question11():
        print("Je wordt gebracht")
        print("")
        print("Je komt op het eiland lesbos")
        print("")
        print("")
        Vraag11 = input("Zoek je ruzie (R) of maak je vrienden (V)? ")

        if Vraag11 == "R" or Vraag11 == "r":
            print("")
            print("ruzie")
            question14()

        elif Vraag11 == "V" or Vraag11 == "v":
            print("")
            print("Maak vrienden")
            question14()

        else:
            question11()
            
    def question12():
        print("Je bent Turkije aan het verkennen ")
        time.sleep(1)
        print("")
        print("Iemand ziet jullie en je wordt weggestuurd")
        time.sleep(1)
        print("")
        print("")
        print("Je hebt een verkeerde keus gemaakt. Game Over. ")
        print("")
        question50()
        

    def question13():
        Vraag13 = input("Je bent in de vliegtuig naar Europa. Wil je naar Polen (P) of Nederland (N)? ")

        if Vraag13 == "P" or Vraag13 == "p":
            time.sleep(1)
            question8()

        elif Vraag13 == "N" or Vraag13 == "n":
            time.sleep(1)
            question7()

        else:
            print("")
            question13()

    def question14():
        time.sleep(1)
        print("")
        print("")
        print("Je hebt een verkeerde keus gemaakt. Game Over. ")
        time.sleep(1)
        print("")
        question50()
        

    def question15():
        time.sleep(1)
        print("Zeewacht")
        print("")
        time.sleep(1)
        print("")
        question14()
        print("")
        time.sleep(1)
        question50()
    
    question1()
main()
