import random
import string

SPECIALE_TEKENS = "@#$%&_?"
WACHTWOORD_LENGTE = 24
MIDDELSTE_POSITIES = {WACHTWOORD_LENGTE // 2 - 1, WACHTWOORD_LENGTE // 2}

# bepaalt hoeveel tekens van elk type in het wachtwoord moeten komen
def kies_aantallen():
    while True:
        aantal_hoofdletters = random.randint(2, 6)
        aantal_cijfers = random.randint(4, 7)
        aantal_speciale = 3
        aantal_kleine_letters = WACHTWOORD_LENGTE - aantal_hoofdletters - aantal_cijfers - aantal_speciale
        if aantal_kleine_letters >= 8:
            return aantal_hoofdletters, aantal_kleine_letters, aantal_cijfers, aantal_speciale


def genereer_wachtwoord():
    aantal_hoofdletters, aantal_kleine_letters, aantal_cijfers, aantal_speciale = kies_aantallen()
    wachtwoord = [None] * WACHTWOORD_LENGTE

    speciale_posities = random.sample(list(range(1, WACHTWOORD_LENGTE - 1)), aantal_speciale)
    for positie in speciale_posities:
        wachtwoord[positie] = random.choice(SPECIALE_TEKENS)

    hoofdletter_posities = random.sample(
        [positie for positie in range(WACHTWOORD_LENGTE) if positie not in MIDDELSTE_POSITIES and wachtwoord[positie] is None],
        aantal_hoofdletters,
    )
    for positie in hoofdletter_posities:
        wachtwoord[positie] = random.choice(string.ascii_uppercase)

    cijfer_posities = random.sample(
        [positie for positie in range(3, WACHTWOORD_LENGTE) if wachtwoord[positie] is None],
        aantal_cijfers,
    )
    for positie in cijfer_posities:
        wachtwoord[positie] = random.choice(string.digits)

    for i in range(WACHTWOORD_LENGTE):
        if wachtwoord[i] is None:
            wachtwoord[i] = random.choice(string.ascii_lowercase)

    if wachtwoord[-1].islower():
        for i in range(WACHTWOORD_LENGTE - 1):
            if wachtwoord[i] in string.ascii_uppercase + string.digits + SPECIALE_TEKENS:
                wachtwoord[i], wachtwoord[-1] = wachtwoord[-1], wachtwoord[i]
                break

    return "".join(wachtwoord)


if __name__ == "__main__":
    print(genereer_wachtwoord())
