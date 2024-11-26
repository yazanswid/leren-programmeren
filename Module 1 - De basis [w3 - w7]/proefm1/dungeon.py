import random
import math

# Speler-object met statistieken
player = {
    "health": 100,
    "attack": 10,
    "defense": 5,
    "inventory": [],
    "rupees": 0  # Aantal rupees van de speler
}

def gevecht(vijand):
    """Herbruikbare gevechtsfunctie tussen speler en vijand."""
    print(f"Je vecht tegen een vijand met {vijand['attack']} aanval, {vijand['defense']} verdediging, en {vijand['health']} gezondheid.")
    
    # Bereken schade per hit
    vijand_damage = max(0, vijand["attack"] - player["defense"])
    player_damage = max(0, player["attack"] - vijand["defense"])
    
    if vijand_damage <= 0:
        print("De vijand kan je geen schade toebrengen. Je loopt veilig door.")
        return
    
    vijand_hits = math.ceil(player["health"] / vijand_damage)
    player_hits = math.ceil(vijand["health"] / player_damage)
    
    if player_hits <= vijand_hits:
        print("Je hebt de vijand verslagen!")
        damage_taken = player_hits * vijand_damage
        player["health"] -= damage_taken
        print(f"Je gezondheid is nu: {player['health']}")
    else:
        print("De vijand heeft je verslagen. Het spel is voorbij.")
        exit()

def kamer_1():
    print("Je bent in kamer 1. Welkom in de dungeon!")


def kamer_2():
    print("Je bent in kamer 2. Hier staat een standbeeld met een rekensom.")
    # Genereer een willekeurige som
    num1 = random.randint(10, 25)
    num2 = random.randint(-5, 75)
    operator = random.choice(["+", "-", "*"])
    correct_answer = eval(f"{num1} {operator} {num2}")
    
    print(f"De som is: {num1} {operator} {num2}")
    player_answer = float(input("Wat is het antwoord? "))
    
    if player_answer == correct_answer:
        print("Correct! Je ontvangt een rupee.")
        player["rupees"] += 1
        print(f"Je hebt nu {player['rupees']} rupee(s).")
    else:
        print("Fout antwoord. Geen rupee voor jou.")
    
    # Keuze maken: naar kamer 8 of kamer 6
    keuze = input("Wil je naar kamer 8 (de gokmachine) of kamer 6 (de zombie)? Typ '8' voor kamer 8 of '6' voor kamer 6: ")
    
    if keuze == '8':
        kamer_8()  # Ga naar kamer 8 (gokmachine)
    elif keuze == '6':
        kamer_6()  # Ga naar kamer 6 (zombie)
    else:
        print("Ongeldige keuze. Je blijft in kamer 2.")
        kamer_2()


def kamer_3():
    print("Je bent in kamer 3. De goblin is verhuisd naar kamer 9.")
    keuze = input("Wil je naar kamer 8, kamer 6 of kamer 9? Typ '8', '6' of '9': ")
    if keuze == "8":
        kamer_8()
    elif keuze == "6":
        kamer_6()
    elif keuze == "9":
        kamer_9()
    else:
        print("Ongeldige keuze. Je blijft in kamer 3.")
        kamer_3()



def kamer_9():
    print("Je bent in kamer 9. Er hangt een mysterieuze betovering in de lucht.")
    
    # Toepassen van de betovering
    betovering = random.choice(["defense", "health"])
    if betovering == "defense":
        player["defense"] += 1
        print("Je voelt je sterker! Je verdediging is met 1 punt verhoogd.")
    else:  # health
        player["health"] += 2
        print("Je voelt je vitaler! Je gezondheid is met 2 punten verhoogd.")
    
    print(f"Je huidige statistieken: Gezondheid: {player['health']}, Verdediging: {player['defense']}")
    
    print("\nHier is ook de goblin die spullen verkoopt.")
    items = {
        "schild": {"cost": 1, "effect": "+1 verdediging"},
        "zwaard": {"cost": 1, "effect": "+2 aanval"},
        "sleutel": {"cost": 5, "effect": "Opent de schatkist in kamer 5"}
    }
    
    print(f"De goblin merkt op dat je {player['rupees']} rupee(s) hebt.")
    if player["rupees"] > 0:
        print("Hij vraagt: 'Wat wil je kopen?'")
        while player["rupees"] > 0:
            print("Beschikbare items:")
            for item, details in items.items():
                print(f"{item}: {details['cost']} rupee(s), effect: {details['effect']}")
            keuze = input("Typ de naam van het item om het te kopen, of 'nee' om verder te gaan: ").lower()
            if keuze in items:
                if player["rupees"] >= items[keuze]["cost"]:
                    player["rupees"] -= items[keuze]["cost"]
                    if keuze == "schild":
                        player["defense"] += 1
                    elif keuze == "zwaard":
                        player["attack"] += 2
                    elif keuze == "sleutel":
                        player["inventory"].append("sleutel")
                    print(f"Je hebt een {keuze} gekocht! Je statistieken zijn geüpdatet.")
                else:
                    print("Je hebt niet genoeg rupees.")
            elif keuze == "nee":
                break
            else:
                print("Ongeldige keuze.")
    else:
        print("Je hebt geen rupees. De goblin stuurt je weg.")
    
    volgende = input("Wil je naar kamer 8, kamer 6 of kamer 3? Typ '8', '6' of '3': ")
    if volgende == "8":
        kamer_8()
    elif volgende == "6":
        kamer_6()
    elif volgende == "3":
        kamer_3()
    else:
        print("Ongeldige keuze. Je blijft in kamer 9.")
        kamer_9()



def kamer_4():
    print("Je bent in kamer 4. Je vecht tegen een nieuwe vijand!")
    vijand = {
        "attack": 2,
        "defense": 0,
        "health": 3
    }
    gevecht(vijand)

def kamer_5():
    print("Je bent in kamer 5. Hier staat een schatkist.")
    if "sleutel" in player["inventory"]:
        print("Je hebt de sleutel! Je opent de schatkist en wint het spel!")
    else:
        print("Je hebt geen sleutel. Je kunt de schatkist niet openen. Het spel is voorbij.")



def kamer_6():
    print("Je bent in kamer 6. De zombie uit kamer 4 is hier!")
    vijand = {
        "attack": random.randint(5, 15),
        "defense": 0,
        "health": 50
    }
    gevecht(vijand)
    
    # Nieuwe keuze na het gevecht
    keuze = input("Wil je naar kamer 8 (gokmachine), kamer 3 (goblin) of blijven? Typ '8', '3' of 'blijven': ")
    if keuze == "8":
        kamer_8()
    elif keuze == "3":
        kamer_3()
    elif keuze == "blijven":
        print("Je besluit in kamer 6 te blijven.")
        kamer_6()
    else:
        print("Ongeldige keuze. Je blijft in kamer 6.")
        kamer_6()


def kamer_7():
    print("Je bent in kamer 7.")
    if random.randint(1, 10) != 1:  # 90% kans (9 op 10)
        print("Je hebt een rupee gevonden!")
        player["rupees"] += 1
        print(f"Je hebt nu {player['rupees']} rupee(s).")
    else:
        print("Helaas, je vindt geen rupee in deze kamer.")
    
    keuze = input("Wil je naar kamer 3 (verkooppunt) of kamer 6 (de zombie)? Typ '3' of '6': ")
    if keuze == "3":
        kamer_3()
    elif keuze == "6":
        kamer_6()
    else:
        print("Ongeldige keuze. Je blijft in kamer 7.")
        kamer_7()


def kamer_8():
    print("Je bent in kamer 8. Hier staat een gokmachine.")
    keuze = input("Wil je de gokmachine gebruiken? Typ 'ja' of 'nee': ").lower()
    if keuze == "ja":
        dobbel1 = random.randint(1, 6)
        dobbel2 = random.randint(1, 6)
        totaal = dobbel1 + dobbel2
        print(f"De dobbelstenen rollen {dobbel1} en {dobbel2}. Totaal: {totaal}.")
        if totaal > 7:
            player["rupees"] *= 2
            print(f"Geweldig! Je hebt nu {player['rupees']} rupee(s).")
        elif totaal < 7:
            player["health"] -= 1
            print(f"Helaas, je verliest 1 health. Je gezondheid is nu: {player['health']}.")
        else:  # totaal == 7
            player["rupees"] += 1
            player["health"] += 4
            print(f"Perfect! Je krijgt 1 rupee en 4 health. Je hebt nu {player['rupees']} rupee(s) en {player['health']} gezondheid.")
        if player["health"] <= 0:
            print("Je gezondheid is 0. Je hebt verloren.")
            exit()
    else:
        print("Je besluit de gokmachine niet te gebruiken.")
    
    # Nieuwe keuze na het gebruik van de gokmachine
    volgende = input("Wil je naar kamer 3 (goblin), kamer 6 (zombie) of blijven? Typ '3', '6' of 'blijven': ")
    if volgende == "3":
        kamer_3()
    elif volgende == "6":
        kamer_6()
    elif volgende == "blijven":
        print("Je besluit in kamer 8 te blijven.")
        kamer_8()
    else:
        print("Ongeldige keuze. Je blijft in kamer 8.")
        kamer_8()



    # Ga naar kamer 3
    kamer_3()


# Dungeon logica
def dungeon():
    kamer_1()
    kamer_2()

# Start het spel
dungeon()


