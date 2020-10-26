

Introductie = ('Dit is mijn eindproduct over Zafel. De Syrische dichter Zafer deelt zijn aangrijpende vluchtverhaal op basis- en middelbare scholen. Die voorlichtingslessen verzorgt hij samen met vrijwilliger Harry, die inmiddels naadloos is ingespeeld op Zafers bijzondere en beeldende vertellingen. ''Ik wil dat leerlingen echt ervaren hoe angst, vluchten en hoop voelt.') 
SpattendGeluk = ('Als ik voor een klas sta, begint mijn verhaal met een foto van mij als blij en schattig tweejarig jongetje vertelt Zafer. Daarna laat ik een foto zien van mijn gezin, lachend voor ons mooie huis in An-Nabk: een stad tussen Damascus en Homs. Zo krijgen de leerlingen een indruk van mijn leven in Syrië van vóór de oorlog. Op die beelden spat het geluk ervan af.')
Halsoverkoop = ('Enkele jaren later staan de gelukkige foto’s in schril contrast met Zafers leven tijdens de oorlog. Zafer uit kritiek op de onderdrukking in zijn land, waar in Syrië de doodstraf op staat. Ook probeert hij als gekozen bestuurslid van An-Nabk met man en macht zijn stad leefbaar te houden. Maar als het regime ingrijpt, wordt het leven voor hem en zijn gezin onhoudbaar. Zafer: ' 'Ik overleefde ternauwernood een aanslag en moest halsoverkop vluchten, niet wetende of ik naar de dood of het leven rende.')

def main():

    import time

    print("")
    print("")
    
    print(Introductie)

    print("")

    # Vraag 1 

    Vraag1 = input("Wil je graag naar het volgende Stukje (A) of stoppen (B). ")

    if Vraag1 == "A" or Vraag1 == "a":
            time.sleep(1)
            print("")
            print("")
            print(SpattendGeluk)
            print("")
    else:
        print("")
        print("Jammer.")
        print("")
        
        restart=input("Wil je als nog opnieuw beginnen? (O) of weggaan (W)" ) 
        if restart == "O":
            print("")
            time.sleep(1)
            main()
        else:
            print("")
            print("Doei!")
            time.sleep(1)
            exit()

    # Vraag 3 

    Vraag3 = input("Wil je graag naar het Volgende Stukje (A) of (B). ")
    
    if Vraag3 == "A" or Vraag3 == "a":
        print("")
        print("")
        print("Je bent nu op stuk3")
        print("")

    # Vraag 5 
        
        Vraag5 = input("Wil je verdergaan? (V)?")
        if Vraag5 == "V" or Vraag5 == "v":
            print("")
            print("")
            print("Dit is Stuk7")
            print("")
            print("")
            time.sleep(4)

    # Vraag 6
            
            Vraag6 = input("Wil je stuk11 of stuk12 lezen?")
            if Vraag6 == "11":
                print("")
                print("")
                print("dit is stuk 11")
                print("")
                print("")
                restart=input("Wil je dit eindproduct nog een keer bekijken (O) of weggaan (W)" ) 
                if restart == "O":
                    time.sleep(5)
                    main()
            else:
                print("")
                print("")
                print("Dit is stuk 12")
                print("")
                print("")
                restart=input("Wil je dit eindproduct nog een keer bekijken (O) of weggaan (W)" ) 
                if restart == "O":
                    time.sleep(2)
                    main()

    else:
        print("")
        print("")
        print("Je bent nu op Stuk4")
        print("")

    # Vraag 4
        
        Vraag4 = input("WIl je de versnelde route nemen (V) of de langzame route nemen (L)") 
        if Vraag4 == "V" or Vraag4 == "v":
            print("")
            print("")
            print("Dit is Stuk6")
            print("")

    # Vraag 7

            Vraag7 = input("Wil je naar stuk13 of Stuk10?")
            if Vraag7 == "13":
                print("")
                print("")
                print("Dit is stuk 13")
                print("")
                print("")
                restart=input("Wil je dit eindproduct nog een keer bekijken (O) of weggaan (W)" ) 
                if restart == "O":
                    main()
            else:
                print("")
                print("")
                print("Dit is stuk 10")
                time.sleep(4)
                print("")
                print("")
                restart=input("Wil je dit eindproduct nog een keer bekijken (O) of weggaan (W)" ) 
                if restart == "O":
                    main()


            
        else:
             print("")
             print("")
             print("Dit is stuk5")
             time.sleep(4)
             print("")
             print("Dit is stuk8")
             time.sleep(4)
             print("")
             print("Dit is Stuk 9")
             time.sleep(4)
             print("")
             print("Dit is stuk10")
             print("")
             print("")
             restart=input("Wil je dit eindproduct nog een keer bekijken (O) of weggaan (W)" ) 
             if restart == "O":
                time.sleep(2)
                main()
               
           
         
main()

    
        
             
              
            
