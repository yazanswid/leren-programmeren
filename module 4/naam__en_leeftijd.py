def vraag_naam_en_leeftijd():
    naam = input("Wat is je naam? ")
    leeftijd = input("Wat is je leeftijd? ")
    return {'naam': naam, 'leeftijd': leeftijd}

gegevens = vraag_naam_en_leeftijd()
print(f"{gegevens['naam']} is {gegevens['leeftijd']} jaar")