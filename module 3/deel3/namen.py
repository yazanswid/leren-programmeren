import random

def naam_loting():
    """Vraagt minimaal 3 unieke namen op."""
    namen = []
    while len(namen) < 3:
        naam = input(f'Voer naam {len(namen) + 1} in: ').strip()
        if naam and naam not in namen:
            namen.append(naam)
        else:
            print('Naam moet uniek zijn en mag niet leeg zijn. Probeer opnieuw.')
    return namen

def naam_toevoegen(namen):
    """Geeft de gebruiker de optie om extra namen toe te voegen."""
    while True:
        keuze = input('Wilt u nog een naam invoeren? (ja/nee): ').strip().lower()
        if keuze == 'ja':
            naam = input('Voeg een extra naam in: ').strip()
            if naam and naam not in namen:
                namen.append(naam)
            else:
                print('Naam moet uniek zijn en mag niet leeg zijn. Probeer opnieuw.')
        elif keuze == 'nee':
            break
        else:
            print('Ongeldige invoer. Gebruik "ja" of "nee".')
    return namen

def verdeel_lotting(namen):
    """Verdeelt de lootjes willekeurig zodat niemand zichzelf trekt."""
    lootjes = namen[:]  
    random.shuffle(lootjes)

    
    while any(namen[i] == lootjes[i] for i in range(len(namen))):
        random.shuffle(lootjes)

    return dict(zip(namen, lootjes))

def print_lotting(lijst):
    """Print de lootjesverdeling."""
    print("\n Lootjesverdeling ")
    for naam, lootje in lijst.items():
        print(f'{naam} krijgt lootje van: {lootje}')

def main():
    print(" Welkom bij de lootjestrekking! \n")
    namen = naam_loting()
    namen = naam_toevoegen(namen)
    lootjes = verdeel_lotting(namen)
    print_lotting(lootjes)

if __name__ == "__main__":
    main()
