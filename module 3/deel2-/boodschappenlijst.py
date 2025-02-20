def boodschappenlijst():
    lijst = {}
    while True:
        artikel = input('welke artikel wilt u toevoegen? ')
        aantal = int(input(f'hoeveel {artikel} wilt u toevoegen? '))

        if artikel in lijst:
            lijst[artikel] += aantal

        else:
            lijst[artikel] = aantal

        doorgaan = input('wilt u nog meer boodschappen toevoegen? (ja/nee) ').lower().strip()
        if doorgaan != 'ja':
            break



    print('\nUw boodschappenlijst is:')
    for artikel, aantal in lijst.items():
        print(f'{aantal} x {artikel}')
            
boodschappenlijst()