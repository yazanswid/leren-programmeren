import random
import math

# Speler-object met statistieken
player = {
    "health": 100,
    "attack": 10,
    "defense": 5,
    "inventory": []
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
        print("Correct! Je ontvangt de sleutel.")
        player["inventory"].append("sleutel")
    else:
        print("Fout antwoord. Geen sleutel voor jou.")

def kamer_3():
    print("Je bent in kamer 3. Je vindt hier een item.")
    item = random.choice(["schild", "zwaard"])
    
    if item == "schild":
        player["defense"] += 1
        print("Je hebt een schild gekregen. +1 verdediging!")
    elif item == "zwaard":
        player["attack"] += 2
        print("Je hebt een zwaard gekregen. +2 aanvalskracht!")

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


def dungeon():
    kamer_1()
    kamer_2()
    kamer_6()  
    kamer_3()
    kamer_4()
    kamer_5()

# Start het spel
dungeon()
