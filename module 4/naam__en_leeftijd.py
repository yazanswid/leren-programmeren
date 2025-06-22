def vraag_naam_en_leeftijd():
    naam = input("Wat is je naam? ").strip().capitalize()
    leeftijd = input("Wat is je leeftijd? ")
    while not leeftijd.isdigit():
        print("Ongeldige invoer. Voer een geldige leeftijd in.")
        leeftijd = input("Wat is je leeftijd? ")
    return {'naam': naam, 'leeftijd': leeftijd}

def verzamel_gegevens():
    gegevens_lijst = []
    while True:
        gegevens = vraag_naam_en_leeftijd()
        gegevens_lijst.append(gegevens)
        doorgaan = input("Toets enter om door te gaan of stop om te printen: ").strip()
        if doorgaan.lower() == 'stop':
            break
    return gegevens_lijst

alle_gegevens = verzamel_gegevens()
for persoon in alle_gegevens:
    print(f"{persoon['naam']} is {persoon['leeftijd']} jaar")