import random
import string

speciale_characters = '!@#$%^&*()_?'
wachtwoord_lengte = 24
middle_positie = {wachtwoord_lengte // 2 - 1, wachtwoord_lengte // 2}

def kies_aantallen():
    while True:
        aantal_hoofdletters = random.randint(2, 6)
        aantal_cijfers = random.randint(4, 7)
        aantal_speciale = 3
        kleine_letters = wachtwoord_lengte - aantal_hoofdletters - aantal_cijfers - aantal_speciale
        if kleine_letters >= 8:
            return aantal_hoofdletters, aantal_cijfers, aantal_speciale, kleine_letters
        
        def genereer_wachtwoord():
            aantal_hoofdletters, aantal_cijfers, aantal_speciale, kleine_letters = kies_aantallen()
            wachtwoord = [None] * wachtwoord_lengte