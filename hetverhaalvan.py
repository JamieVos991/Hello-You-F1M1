Introductie = ('Hallo Dit is mijn eindproduct gebaseerd over het verhaal Zafel. De Syrische dichter Zafer deelt zijn aangrijpende vluchtverhaal op basis- en middelbare scholen. ''Ik wil dat leerlingen echt ervaren hoe angst, vluchten en hoop voelt.' ' Door de aangegeven letters te typen ga je door het verhaal.')

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
            print("Oke, doei!")
            exit()

        else:
            print("")
            print("Niks ingevuld...")
            question50()

    def question1():
        Vraag1 = input("Wil je graag het verhaal beginnen (A) of stoppen (B). ")

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
        Vraag2 = input("Jouw stad is in puin en er is oorlog in jouw thuis land. Je moet vluchten, naar welk land ga je? Turkije (T) of Griekenland (G)?. ")
        
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
            print("")
            question2()


    def question3():
        Vraag3 = input("Het is het is heel warm. Je krijgt een aanbod om met de vliegtuig naar Europa te gaan maar naar waar weet je nog niet. Je zit te denken, ga ik verder te voet in Turkije (V) of ga ik met de vliegtuig naar Europa (E)? ")

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
        Vraag4 = input("Het is 1 uur in de nacht. Alle lichten staan uit behalve de straat lampen. Ga je Turkije meer verkennen (V) of ga je een plek zoeken om te overnachten (O)? ")

        if Vraag4 == "V" or Vraag4 == "v":
            print("")
            print("")
            time.sleep(1)
            question12()

        elif Vraag4 == "O" or Vraag4 == "o":
            question5()

        else:
            time.sleep(0)
            print("")
            print("Onbekend toets ingevuld :( ")
            print("")
            question4()

    def question5():
        time.sleep(1)
        print("")
        print("Je bent aan het overnachten op een vreemde plek zonder toesteming ")
        time.sleep(1)
        print("")
        print("Onbekende mensen zien jullie en bellen de politie. Je wordt opgepakt en terug gestuurd naar jouw thuisland waar oorlog was. ")
        time.sleep(1)
        print("")
        print("")
        print("Je hebt een verkeerde keus gemaakt. Game Over ")
        print("")
        question50()

    def question6():
        Vraag6 = input("Je bent met de vliegtuig van Turkije naar Duitsland gegaan. Je krijgt weer een aanbod van waar je wilt verblijven. De keuze luid als volgt: Wil je naar Nederland (N) of Polen (P)? ")
  
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
        print("Welkom in Nederland. De land van de kaas, klompen en tulpen. ")
        print("")
        time.sleep(1)
        print("Je komt aan in Schiphol en het is allemaal heel nieuw voor jou. Je wond naar een huis gestuurd met andere mede vluchtelingen. Je bent blij met de keuze die je hebt gemaakt. ")
        print("")
        print("")
        time.sleep(1)
        print("Gefeliciteerd, je hebt 1 van de goedde eindes gevonden! ")
        question50()
        
    def question8():
        print("")
        print("Welkom in Polen")
        print("")
        time.sleep(1)
        print("Je komt aan in Warschau Airport. Mensen die jou begeleiden zijn heel bot tegen jou en je krijgt spijt van de keuze die je hebt gemaakt. ")
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
        print("Je bent onderweg aan het lopen om met de boot te gaan. Je hebt een slecht gevoel dat je het wel gaat redden van de ene naar de andere kant met de boot omdat het illegaal kan zijn. ")
        print("")
        Vraag10 = input("Je bent nu op de boot met andere vluchtelingen naar Griekenland. Wil je naar het Noordoosten (O) of Noordwesten (W)? ")
        if Vraag10 == "O" or Vraag10 == "o":
            print("")
            print("Je gaat nu richting het Noord oosten")
            print("")
            question15()
            

        elif Vraag10 == "W" or Vraag10 == "w":
            print("")
            print("Je gaat nu richting het Noordwesten")
            print("")
            question15()

        else:
            question10()
        
    def question11():
        print("Iemand bied zich vrijwillig aan om jou te brengen met de auto naar het eiland Lesbos. ")
        print("")
        print("Je komt op het eiland Lesbos ")
        print("")
        print("")
        Vraag11 = input("Zoek je ruzie (R) of maak je vrienden (V)? ")

        if Vraag11 == "R" or Vraag11 == "r":
            print("")
            print("Je bent onderweg naar iemand en je zegt: Je bent lelijk man. De andere man wordt boos en je raakt in een gevecht. ")
            question14()

        elif Vraag11 == "V" or Vraag11 == "v":
            print("")
            print("Je bent onderweg naar iemand en probeert een vriendschap te creëren ")
            question14()

        else:
            question11()
            
    def question12():
        print("Je loopt meer het land in met je mede vluchtelingen. Als iemand die niet bij het land behoort mag dit niet. ")
        time.sleep(1)
        print("")
        print("Iemand van de politie ziet jullie en je wordt weggestuurd")
        time.sleep(1)
        print("")
        print("")
        print("Je hebt een verkeerde keus gemaakt. Game Over. ")
        print("")
        question50()
        

    def question13():
        Vraag13 = input("Je bent met de vliegtuig van Turkije naar Duitsland gegaan. Je krijgt weer een aanbod van waar je wilt verblijven. De keuze luid als volgt: Wil je naar Nederland (N) of Polen (P)? ")

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
        print("Je bent aan het varen op de Middellandse zee. Plotseling komt er Zee wacht en je wordt weggestuurd. ")
        print("")
        time.sleep(1)
        print("")
        question14()
        print("")
        time.sleep(1)
        question50()
    
    question1()
main()
