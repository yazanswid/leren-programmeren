import random

# Speler-object met statistieken
player = {
    "health": 100,
    "attack": 10,
    "defense": 5,
    "inventory": [],
    "rupees": 0  # Het aantal rupees dat de speler bezit
}


def kamer_1():
    print("Welkom in kamer 1. Je avontuur begint hier!")
    keuze = input("Wil je naar kamer 7? Typ '7': ")
    if keuze == "7":
        kamer_7()
    else:
        print("Ongeldige keuze. Probeer opnieuw.")
        kamer_1()


def kamer_7():
    print("Je bent in kamer 7. Je vindt een rupee!")
    player["rupees"] += 1
    keuze = input("Wil je naar kamer 2 of kamer 8? Typ '2' of '8': ")
    if keuze == "2":
        kamer_2()
    elif keuze == "8":
        kamer_8()
    else:
        print("Ongeldige keuze. Je blijft in kamer 7.")
        kamer_7()


def kamer_2():
    print("Je bent in kamer 2. Hier is een rekensomstandbeeld.")
    num1 = random.randint(10, 25)
    num2 = random.randint(5, 15)
    operator = random.choice(["+", "-", "*"])
    correct_answer = eval(f"{num1} {operator} {num2}")

    print(f"De som is: {num1} {operator} {num2}")
    try:
        player_answer = int(input("Wat is het antwoord? "))
    except ValueError:
        print("Ongeldig antwoord.")
        kamer_2()
        return

    if player_answer == correct_answer:
        print("Correct! Je ontvangt een rupee.")
        player["rupees"] += 1
    else:
        print("Fout antwoord. Geen beloning.")

    keuze = input("Wil je naar kamer 6 of kamer 8? Typ '6' of '8': ")
    if keuze == "6":
        kamer_6()
    elif keuze == "8":
        kamer_8()
    else:
        print("Ongeldige keuze. Je blijft in kamer 2.")
        kamer_2()


def kamer_6():
    print("Je bent in kamer 6. Een zombie valt je aan!")
    vijand = {"health": 50, "attack": 10, "defense": 0}
    gevecht(vijand)
    kamer_8()


def kamer_8():
    print("Je bent in kamer 8. Hier is een gokmachine.")
    
    while True:  
        keuze = input("Wil je gokken? Typ 'ja' of 'nee': ").lower()
        if keuze == "ja":
            dobbel1 = random.randint(1, 6)
            dobbel2 = random.randint(1, 6)
            totaal = dobbel1 + dobbel2
            print(f"De dobbelstenen rollen {dobbel1} en {dobbel2}. Totaal: {totaal}.")
            
            if totaal > 7:
                player["rupees"] *= 2
                print(f"Je wint! Je hebt nu {player['rupees']} rupee(s).")
            elif totaal < 7:
                player["health"] -= 10
                print(f"Je verliest! Je gezondheid is nu {player['health']}.")
            else:
                print("Perfect! Je gezondheid stijgt met 10 en je krijgt 1 rupee.")
                player["health"] += 10
                player["rupees"] += 1

            
            if player["health"] <= 0:
                print("Je gezondheid is te laag. Het spel is afgelopen.")
                exit()
        elif keuze == "nee":
            print("Je besluit te stoppen met gokken.")
            break
        else:
            print("Ongeldige invoer. Typ 'ja' of 'nee'.")
    
    
    kamer_9()

def kamer_9():
    print("Je bent in kamer 9. Een magische kracht verhoogt je statistieken!")
    upgrade = random.choice(["health", "defense"])
    if upgrade == "health":
        player["health"] += 2
        print("Je gezondheid is verhoogd met 2!")
    else:
        player["defense"] += 1
        print("Je verdediging is verhoogd met 1!")
    kamer_3()

def kamer_3():
    print("Je bent in kamer 3. Hier is een handelaar.")

    # Beschikbare items met kosten en effecten
    items = {
        "schild": {"cost": 1, "effect": "+1 verdediging"},
        "zwaard": {"cost": 1, "effect": "+2 aanval"},
        "sleutel": {"cost": 5, "effect": "Nodig om de schatkist te openen"}
    }

    print(f"Je hebt {player['rupees']} rupee(s).")
    while player["rupees"] > 0:  # Zolang de speler rupees heeft, kan hij items kopen
        print("\nBeschikbare items:")
        for item, details in items.items():
            print(f"{item.capitalize()}: {details['cost']} rupee(s) - {details['effect']}")
        
        keuze = input("Wat wil je kopen? Typ 'schild', 'zwaard', 'sleutel' of 'stop' om te stoppen: ").lower()
        
        if keuze in items:
            if player["rupees"] >= items[keuze]["cost"]:
                player["rupees"] -= items[keuze]["cost"]
                
                if keuze == "schild":
                    player["defense"] += 1
                    print("Je hebt een schild gekocht! Je verdediging is verhoogd met 1.")
                elif keuze == "zwaard":
                    player["attack"] += 2
                    print("Je hebt een zwaard gekocht! Je aanval is verhoogd met 2.")
                elif keuze == "sleutel":
                    player["has_key"] = True
                    print("Je hebt de sleutel gekocht! Hiermee kun je de schatkist in kamer 5 openen.")
            else:
                print("Je hebt niet genoeg rupees om dit item te kopen.")
        elif keuze == "stop":
            print("Je besluit te stoppen met winkelen.")
            break
        else:
            print("Ongeldige keuze. Probeer opnieuw.")
    
    if player["rupees"] == 0:
        print("Je hebt geen rupees meer en kunt niets meer kopen.")

    volgende = input("Wil je naar kamer 4? Typ '4' om door te gaan: ")
    if volgende == "4":
        kamer_4()
    else:
        print("Ongeldige keuze. Je blijft in kamer 3.")
        kamer_3()


def kamer_4():
    print("Je bent in kamer 4. Een nieuwe vijand valt je aan!")
    vijand = {"health": 30, "attack": 20, "defense": 0}
    gevecht(vijand)
    kamer_5()


def kamer_5():
    print("Je bent in kamer 5. Hier is de schatkist.")

    if player["has_key"]:
        print("Je hebt de sleutel! Je opent de schatkist en wint het spel. Gefeliciteerd!")
    else:
        print("Je hebt de sleutel niet. Je kunt de schatkist niet openen en verliest het spel.")
    
    print("Het spel is voorbij. Bedankt voor het spelen!")



def gevecht(vijand):
    print(f"Je vecht tegen een vijand met {vijand['health']} gezondheid!")
    while vijand["health"] > 0 and player["health"] > 0:
        schade_vijand = max(0, vijand["attack"] - player["defense"])
        schade_player = max(0, player["attack"] - vijand["defense"])
        vijand["health"] -= schade_player
        player["health"] -= schade_vijand
        print(f"Vijand gezondheid: {vijand['health']}, Jouw gezondheid: {player['health']}")

    if player["health"] <= 0:
        print("Je bent verslagen! Het spel is afgelopen.")
        exit()
    else:
        print("Je hebt de vijand verslagen!")


def dungeon():
    kamer_1()


# Start het spel
dungeon()
