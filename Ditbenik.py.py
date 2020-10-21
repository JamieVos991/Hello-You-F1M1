# variabelen 
# input()
# print()

# Doel: Voornaam en achternaam kunnen invoeren. Het programma weergeeft de volledige naam.

Score = 0
import time

print("Hello You!, ik ben Jamie Vos")
print("Wie ben jij?")
voornaam = input()

print("")

print("Hello" + " " + voornaam)

print("")

print("Ik ben een nieuwkomer op het Mediacollege Amsterdam")
print("Door een aantal vragen over mij te beantwoorden leer je mij beter kennen.")

print("")
print("")
time.sleep(3)

# Vraag 1
antwoord1 = input("Hoe oud ben ik? \na 15 \nb 16 \nc 17 \nd 18 \nAnswer: ")
if antwoord1 == "b" or antwoord1 == "16" or antwoord1 == "B":
    Score +=1
    print("Goed!")
    print("Score: ", Score)
    print("\n")
else:
    Score -=1
    print("Niet goed! Het antwoord is B (16)")
    print("Score: ", Score)
    print("\n")

time.sleep(1)

# Vraag 2
antwoord2 = input("Welk niveau deed ik op mijn vorige school? \na Kader \nb GL \nc TL \nd Havo \nAnswer: ")
if antwoord2 == "a" or antwoord2 == "Kader" or antwoord2 == "A":
    Score +=1 
    print("Goed!")
    print("Score: ", Score)
    print("\n")
else:
    Score -=1
    print("Niet goed! Het antwoord is A (Kader)")
    print("Score: ", Score)
    print("\n")

time.sleep(1)

# Vraag 3
antwoord2 = input("Wat is mijn favoriete kleur? \na Groen \nb Goud \nc Aqua \nd Beige \nAnswer: ")
if antwoord2 == "c" or antwoord2 == "Aqua" or antwoord2 == "C":
    Score +=1 
    print("Goed!")
    print("Score: ", Score)
    print("\n")
else:
    Score -=1
    print("Niet goed! Het antwoord is C (Aqua)")
    print("Score: ", Score)
    print("\n")

time.sleep(1)

# Vraag 4
antwoord2 = input("Welk spel speel ik het meest? \na Fortnite \nb Paladins \nc Minecraft \nd Roblox \nAnswer: ")
if antwoord2 == "b" or antwoord2 == "Paladins" or antwoord2 == "B":
    Score +=1 
    print("Goed!")
    print("Score: ", Score)
    print("\n")
else:
    Score -=1
    print("Niet goed! Het antwoord is B (Paladins)")
    print("Score: ", Score)
    print("\n")

print("")
time.sleep(1)

# Vraag 5
antwoord2 = input("Welk muziek artiest luister ik naar? \na Coldplay \nb Juice wrld \nc Avicii \nd The Weeknd \nAnswer: ")
if antwoord2 == "d" or antwoord2 == "The Weeknd" or antwoord2 == "D":
    Score +=1 
    print("Goed!")
    print("Score: ", Score)
    print("\n")
else:
    Score -=1
    print("Niet goed! Het antwoord is D (The Weeknd)")
    print("Score: ", Score)
    print("\n")

print("")
time.sleep(1)
    
# Eind score
print("Jouw eind score is: ", Score)
if Score == 0:
    print("Veel voortgang gemaakt lol")
